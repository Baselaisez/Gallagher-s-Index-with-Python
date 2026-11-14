# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 18: THE SECOND BĀB, ON THE GOVERNED WORD (الْبَابُ الثَّانِي فِي الْمَعْمُولِ), its opening: coined
# words outside composition are neither governed nor governing; inside it they fall into three divisions. The FIRST division — never
# governed: the particle absolutely, and the imperative without the lām (the Basrans: with the muḍāriʿ's letter dropped it leaves the
# noun's likeness and returns to its origin, the binaʾ; the Kufans: it is declined, jazm'd by an estimated lām). The SECOND —
# always governed: the noun absolutely (so that even the noun-verbs were ruled to have a maḥall — raised by the ibtidāʾ with their
# doer filling the khabar's place, or in naṣb as a maṣdar — though some said they have no maḥall since they carry a verb's sense;
# and the ḍamīr al-faṣl in كَانَ زَيْدٌ هُوَ الْقَائِمَ was ruled a particle, against those who call it a noun without a maḥall; and the
# lām on the participles — a particle for some, for most a relative noun meaning الَّذِي whose iʿrāb passed to what follows it when
# the verb became a noun: جَاءَنِي الضَّارِبُ زَيْدًا from جَاءَنِي الَّذِي ضَرَبَ زَيْدًا, the ruling reversed to favour the wording's side)
# — and the muḍāriʿ verb. Print pp. 115–117.
#   python3 author_izhar_ch18.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-mamul-wa-aqsamuh"
K17 = "al-amil-al-manawi"
TITLE = {"ar": "الْبَابُ الثَّانِي فِي الْمَعْمُولِ: مَا لَا يُعْمَلُ فِيهِ أَصْلًا وَمَا يُعْمَلُ فِيهِ دَائِمًا", "en": "The second bāb, on the governed word: what is never governed and what is always governed", "tr": "İkinci bab, ma'mûl: hiç amel edilmeyen ve dâimâ amel edilen"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; F7 = "form-vii-verbs"; F8 = "form-viii-verbs"; MSD = "masdar"; LN = "la-nafiya"; IN = "inna-wa-akhawatuha"; BD = "badal"; JT = "jam-taksir"; JMS = "jam-mudhakkar-salim"; JMU = "jam-muannath-salim"; ISH = "asma-al-ishara"; MQ = "ism-maqsur-manqus"; AQ = "al-amil-wa-aqsamuh"; MR = "mudari-marfu"; MJZ = "nawasib-wa-jawazim-al-mudari"; MAW = "ism-mawsul"; JS = "jumla-sifa"; MM = "maful-mutlaq"
AMR = "imperative-amr"; IFL = "ism-fil"; DF = "damir-fasl"; KK = "al-kalima-wal-kalam"; SH = "in-shartiyya"; MFL = "maful-lah"; MH = "mahall-al-majrur"; LAJ = "la-nafiya-lil-jins"; NSB = "ism-mansub"; AMS = "an-masdariyya"; TM = "tamyiz"

def minhu_fa(): return tok("فَمِنْهُ", "min", "prep", [K, HJ, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَمِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«of it»", "«ondan»", segments=[seg("فَ", "fa", "conj"), seg("مِنْ", "min", "prep"), pr3ms()])
def awwal(punct=None, ar="مُبْتَدَأٌ مَرْفُوعٌ."): return tok("الْأَوَّلُ", "awwal", "noun", [K, MK], ar, "«the first» — the mubtada.", "«ilki» — mübtedâ.", punct=punct)
def thani_wa(punct=None): return tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«and the second» — the mubtada.", "«ikincisi» — mübtedâ.", punct=punct, segments=wa("الثَّانِي", "thani", "noun"))
def mahall_la(): return [tok("لَا", "la-nafiya", "part", [K, LAJ], "لَا النَّافِيَةُ لِلْجِنْسِ.", "«no» — the lā that denies the kind.", "«hiçbir … yok» — cins nefyeden lâ."), tok("مَحَلَّ", "mahall", "noun", [K, LAJ, MK], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«place» — the ism of lā, built on the fatḥa.", "«mahal» — lâ'nın ismi, fetha üzere mebnî.")]

# ----------- s1 — words outside composition are neither governed nor governing; inside it, three divisions
S.append({"id": "s1", "translation": {"en": "Know first that the coined words, when they do not occur in a composition, are not governed, just as they do not govern; and if they occur in it, they are of three divisions.", "tr": "Önce bil ki vaz' edilmiş lafızlar terkipte bulunmadıklarında, amel etmedikleri gibi ma'mûl de olmazlar; terkipte bulunurlarsa üç kısım üzeredirler."},
 "tokens": [
  tok("اعْلَمْ", "alima", "verb", [K, AMR], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، هَمْزَتُهُ هَمْزَةُ وَصْلٍ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«know!» — the imperative that opens a bāb.", "«bil!» — babı açan emir."),
  tok("أَوَّلًا", "awwalan", "adv", [K, MF], "ظَرْفٌ مَنْصُوبٌ — فِي أَوَّلِ الْأَمْرِ.", "«first»", "«önce»"),
  tok("أَنَّ", "anna", "part", [K, IN, MB], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيِ اعْلَمْ.", "«that» — the clause fills the place of both objects of «know».", "«ki» — cümle i'lem'in iki mef'ûlünün yerini tutar."),
  tok("الْأَلْفَاظَ", "lafz", "noun", [K, IN, JT], "اسْمُ أَنَّ مَنْصُوبٌ — جَمْعُ لَفْظٍ.", "«the words» — the ism of anna.", "«lafızlar» — enne'nin ismi."),
  tok("الْمَوْضُوعَةَ", "mawdua", "noun", [K, NA, IMF, KK], "نَعْتٌ مَنْصُوبٌ — الْمَوْضُوعَةُ لِمَعْنًى: الْكَلِمُ.", "«coined» — a naʿt: the words set for a meaning.", "«vaz' edilmiş» — na't: bir mânâ için konulmuş kelimeler."),
  tok("إِذَا", "idha", "part", [K, MF, SH], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the conditional time-adverb.", "«-diğinde» — şart mânâlı zaman zarfı."),
  tok("لَمْ", "lam-jazima", "part", [K, MJZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mez»"),
  tok("تَقَعْ", "waqaa", "verb", [K, MJZ, FL, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — مِثَالٌ وَاوِيٌّ سَقَطَتْ وَاوُهُ.", "«occur» — jussive; the initial wāw of «to fall» dropped.", "«bulunmaz» — meczûm; vakaa'nın vâvı düşmüş."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("التَّرْكِيبِ", "tarkib", "noun", [K, HJ, KK], "مَجْرُورٌ بِفِي — تَرْكِيبُ الْكَلَامِ.", "«a composition» — the putting together of speech.", "«terkipte» — kelâmın terkibi."),
  tok("لَمْ", "lam-jazima", "part", [K, MJZ, SH], "حَرْفُ نَفْيٍ وَجَزْمٍ — وَالْجُمْلَةُ جَوَابُ إِذَا.", "«not» — the apodosis.", "«-mez» — cevap."),
  tok("تَكُنْ", "kana", "verb", [K, MJZ, KN, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، حُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«are» — kāna jussive, its wāw dropped.", "«olmaz» — meczûm kâne, vâvı düşmüş."),
  tok("مَعْمُولَةً", "mamul", "noun", [K, KN, IMF], "خَبَرُ تَكُنْ مَنْصُوبٌ.", "«governed» — the khabar of kāna.", "«ma'mûl» — kâne'nin haberi."),
  tok("كَمَا", "ka", "prep", [K, HJ, AMS], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ — كَعَدَمِ كَوْنِهَا عَامِلَةً.", "«just as»", "«… gibi»", segments=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-mez»"),
  tok("تَكُونُ", "kana", "verb", [K, KN, HV, MR], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«they are»", "«olurlar»"),
  tok("عَامِلَةً", "amil-governor", "noun", [K, KN, IFA], "خَبَرُ تَكُونُ مَنْصُوبٌ.", "«governing» — the khabar of kāna.", "«âmil» — kâne'nin haberi.", punct="،"),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("وَقَعَتْ", "waqaa", "verb", [K, SH, FL], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«they occur» — the protasis.", "«bulunurlarsa» — şart fiili."),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — فِي التَّرْكِيبِ.", "«in it»", "«onda»", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("فَعَلَى", "ala", "prep", [K, HJ, SH, MK, HT], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَعَلَى حَرْفُ جَرٍّ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: فَهِيَ عَلَى.", "«then [they are] of» — the khabar of a dropped «they».", "«o hâlde … üzeredir» — hazfedilmiş mübtedânın haberi.", segments=fa("عَلَى", "ala", "prep")),
  tok("ثَلَاثَةِ", "thalatha", "noun", [K, HJ, ID, TM], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«three»", "«üç»"),
  tok("أَقْسَامٍ", "aqsam", "noun", [K, ID, JT, TM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَمْيِيزُ الْعَدَدِ: جَمْعُ قِسْمٍ.", "«divisions» — the number's plural specifier.", "«kısım» — sayının çoğul temyizi.", punct="."),
 ]})
# ----------- s2 — the first division: never governed — the particle, and the imperative without the lām
S.append({"id": "s2", "translation": {"en": "The first division is what is never governed at all, and it is two: the first is the particle, absolutely; and the second is the imperative without the lām, according to the Basrans.", "tr": "Birinci kısım asla ma'mûl olmayandır; o da ikidir: ilki mutlak olarak harf, ikincisi Basralılara göre lâmsız emirdir."},
 "tokens": [
  tok("الْقِسْمُ", "qism", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the division» — the mubtada.", "«kısım» — mübtedâ."),
  tok("الْأَوَّلُ", "awwal", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«first» — a naʿt.", "«birinci» — na't."),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the khabar.", "«… olan» — haber."),
  tok("لَا", "la-nafiya", "part", [K, LN, MAW], "حَرْفُ نَفْيٍ.", "«not»", "«-maz»"),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MAW], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةٌ.", "«is» — the relative clause.", "«olan» — sıla."),
  tok("مَعْمُولًا", "mamul", "noun", [K, KN, IMF], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«governed» — the khabar of kāna.", "«ma'mûl» — kâne'nin haberi."),
  tok("أَصْلًا", "asl", "noun", [K, MM], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — بِمَعْنَى: الْبَتَّةَ.", "«at all» — the absolute object: «ever».", "«asla» — mef'ûl-i mutlak.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("اثْنَانِ", "ithnan", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى.", "«two» — the khabar, declined like the dual.", "«iki» — haber, tesniyeye mülhak.", punct=":"),
  awwal(),
  tok("الْحَرْفُ", "harf", "noun", [K, MK, KK], "خَبَرٌ مَرْفُوعٌ.", "«the particle» — the khabar.", "«harf» — haber."),
  tok("مُطْلَقًا", "mutlaq", "noun", [K, HL, IMF], "حَالٌ مَنْصُوبٌ — بِلَا قَيْدٍ.", "«absolutely» — a ḥāl: without restriction.", "«mutlak olarak» — hâl: kayıtsız.", punct="،"),
  thani_wa(),
  tok("الْأَمْرُ", "amr", "noun", [K, MK, AMR], "خَبَرٌ مَرْفُوعٌ — فِعْلُ الْأَمْرِ.", "«the imperative» — the khabar.", "«emir» — haber."),
  tok("بِغَيْرِ", "ghayr", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ.", "«without»", "«-sız»", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  tok("اللَّامِ", "lam-letter", "noun", [K, ID, AMR], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَامُ الْأَمْرِ: لِيَضْرِبْ.", "«the lām» — the lām of command.", "«lâm» — emir lâmı."),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«according to»", "«… göre»"),
  tok("الْبَصْرِيِّينَ", "basri", "noun", [K, ID, JMS, NSB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — نُحَاةُ الْبَصْرَةِ.", "«the Basrans» — the grammarians of Basra.", "«Basralılar» — Basra nahivcileri.", punct="."),
 ]})
# ----------- s3 — the Basrans' reason: the muḍāriʿ's letter dropped, the likeness to the noun gone, the origin regained
S.append({"id": "s3", "translation": {"en": "For when the letter of the muḍāriʿ — by which the muḍāriʿ had come to resemble the noun, and so was declined and governed — was dropped from it, it left the likeness and returned to its origin, which is the binaʾ.", "tr": "Çünkü muzâriyi isme benzeten — bu yüzden i'râb alan ve kendisinde amel edilen — muzâraat harfi ondan düşünce, benzerlikten çıktı ve aslına, yani binâya döndü."},
 "tokens": [
  tok("فَإِنَّهُ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا — ضَمِيرُ الشَّأْنِ أَوِ الْأَمْرِ.", "«for it» — inna with its pronoun ism.", "«çünkü o» — inne, zamir ismi.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("لَمَّا", "lamma", "part", [K, MF], "ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the time-adverb with conditional force.", "«-ince» — şart mânâlı zaman zarfı."),
  tok("حُذِفَ", "hadhafa", "verb", [K, NF, MF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«was dropped»", "«düşürüldü»"),
  tok("عَنْهُ", "an", "prep", [K, HJ], "عَنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — عَنِ الْأَمْرِ.", "«from it» — from the imperative.", "«ondan» — emirden.", segments=[seg("عَنْ", "an", "prep"), pr3ms()]),
  tok("حَرْفُ", "harf", "noun", [K, NF, ID], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«the letter of» — the deputy doer.", "«harfi» — nâib-i fâil."),
  tok("الْمُضَارَعَةِ", "mudaraa", "noun", [K, ID, MSD, MR], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَحَدُ حُرُوفِ أَنَيْتُ.", "«resemblance» — one of the four letters أَنَيْتُ.", "«muzâraat» — eneytü harflerinden biri."),
  tok("الَّتِي", "allati", "pron", [K, NA, MAW], "اسْمٌ مَوْصُولٌ نَعْتٌ لِحَرْفِ الْمُضَارَعَةِ فِي مَحَلِّ رَفْعٍ.", "«which» — the relative, a naʿt.", "«ki o» — mevsûl, na't."),
  tok("بِسَبَبِهَا", "sabab", "noun", [K, HJ, ID, MAW], "الْبَاءُ حَرْفُ جَرٍّ، وَسَبَبِهَا مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«by reason of which»", "«onun sebebiyle»", segments=[seg("بِ", "bi", "prep"), seg("سَبَبِ", "sabab", "noun"), pr3fs()]),
  tok("صَارَ", "sara", "verb", [K, KN, HV, MAW], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةُ الَّتِي.", "«had come to be» — the relative clause.", "«olmuştu» — sıla."),
  tok("الْمُضَارِعُ", "mudari", "noun", [K, KN, MR], "اسْمُ صَارَ مَرْفُوعٌ.", "«the muḍāriʿ» — the ism of ṣāra.", "«muzâri» — sâra'nın ismi."),
  tok("مُشَابِهًا", "mushabih", "noun", [K, KN, IFA], "خَبَرُ صَارَ مَنْصُوبٌ — اسْمُ فَاعِلِ شَابَهَ.", "«resembling» — the khabar of ṣāra.", "«benzer» — sâra'nın haberi."),
  tok("لِلِاسْمِ", "ism", "noun", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالِاسْمِ مَجْرُورٌ.", "«the noun»", "«isme»", segments=[seg("لِ", "li", "prep"), seg("الِاسْمِ", "ism", "noun")]),
  tok("فَأُعْرِبَ", "araba", "verb", [K, AT, NF, F4], "الْفَاءُ عَاطِفَةٌ لِلتَّرْتِيبِ، وَأُعْرِبَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«and so was declined»", "«ve i'râb aldı»", segments=fa("أُعْرِبَ", "araba", "verb")),
  tok("وَعُمِلَ", "amila", "verb", [K, AT, NF], "الْوَاوُ عَاطِفَةٌ، وَعُمِلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and was governed»", "«ve amel edildi»", segments=wa("عُمِلَ", "amila", "verb")),
  tok("فِيهِ", "fi", "prep", [K, HJ, NF], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَائِبُ الْفَاعِلِ.", "«in it» — the jarr phrase stands as the deputy doer.", "«onda» — câr-mecrûr nâib-i fâil.", punct="،", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("خَرَجَ", "kharaja", "verb", [K, FL, IN], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جَوَابُ لَمَّا، وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«it left» — the answer of «when»; the khabar of inna.", "«çıktı» — lemmâ'nın cevabı; inne'nin haberi."),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  tok("الْمُشَابَهَةِ", "mushabaha", "noun", [K, HJ, MSD], "مَجْرُورٌ بِعَنْ.", "«the likeness»", "«benzerlikten»"),
  tok("فَعَادَ", "ada-return", "verb", [K, AT, FL, HV], "الْفَاءُ عَاطِفَةٌ، وَعَادَ فِعْلٌ مَاضٍ.", "«and returned»", "«ve döndü»", segments=fa("عَادَ", "ada-return", "verb")),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("أَصْلِهِ", "asl", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its origin»", "«aslına»", segments=[seg("أَصْلِ", "asl", "noun"), pr3msi()]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«which is» — the mubtada.", "«ki o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْبِنَاءُ", "bina", "noun", [K, MK, KK], "خَبَرٌ مَرْفُوعٌ — الْبِنَاءُ: لُزُومُ آخِرِ الْكَلِمَةِ حَرَكَةً أَوْ سُكُونًا.", "«the binaʾ» — the khabar: the fixed ending.", "«binâ» — haber: sabit son.", punct="."),
 ]})
# ----------- s4 — the Kufans: declined, jazm'd by an estimated lām
S.append({"id": "s4", "translation": {"en": "And the Kufans said: it is declined, in jazm by an estimated lām.", "tr": "Kûfeliler ise dediler ki: o mu'rebdir, takdîrî bir lâmla meczûmdur."},
 "tokens": [
  tok("وَقَالَ", "qala", "verb", [K, AT, FL, HV], "الْوَاوُ عَاطِفَةٌ، وَقَالَ فِعْلٌ مَاضٍ.", "«and said»", "«ve dedi»", segments=wa("قَالَ", "qala", "verb")),
  tok("الْكُوفِيُّونَ", "kufi", "noun", [K, FL, JMS, NSB], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — نُحَاةُ الْكُوفَةِ.", "«the Kufans» — the doer: the grammarians of Kufa.", "«Kûfeliler» — fâil: Kûfe nahivcileri.", punct=":"),
  tok("هُوَ", "huwa", "pron", [K, MK], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — مَقُولُ الْقَوْلِ.", "«it» — the mubtada; the saying's content.", "«o» — mübtedâ; makûlü'l-kavl."),
  tok("مُعْرَبٌ", "murab", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«declined» — the khabar.", "«mu'reb» — haber."),
  tok("مَجْزُومٌ", "majzum", "noun", [K, MK, IMF, MJZ], "خَبَرٌ ثَانٍ مَرْفُوعٌ (أَوْ نَعْتٌ).", "«in jazm» — a second khabar.", "«meczûm» — ikinci haber."),
  tok("بِلَامٍ", "lam-letter", "noun", [K, HJ, AMR], "الْبَاءُ حَرْفُ جَرٍّ، وَلَامٍ مَجْرُورٌ — لَامِ الْأَمْرِ.", "«by a lām» — the lām of command.", "«bir lâmla» — emir lâmı.", segments=[seg("بِ", "bi", "prep"), seg("لَامٍ", "lam-letter", "noun")]),
  tok("مُقَدَّرَةٍ", "muqaddar", "noun", [K, NA, IMF, HT], "نَعْتٌ مَجْرُورٌ — مُقَدَّرَةٍ لَا مَلْفُوظَةٍ: اضْرِبْ أَصْلُهُ لِتَضْرِبْ.", "«estimated» — supplied, not spoken: اضْرِبْ from لِتَضْرِبْ.", "«takdîrî» — söylenmeyen: idrib aslı li-tadrib.", punct="."),
 ]})
# ----------- s5 — the second division: always governed — the noun absolutely
S.append({"id": "s5", "translation": {"en": "And the second division is what is always governed, and it too is two: the first is the noun, absolutely.", "tr": "İkinci kısım dâimâ ma'mûl olandır; o da ikidir: ilki mutlak olarak isimdir."},
 "tokens": [
  tok("وَالْقِسْمُ", "qism", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْقِسْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the division» — the mubtada.", "«ve kısım» — mübtedâ.", segments=wa("الْقِسْمُ", "qism", "noun")),
  tok("الثَّانِي", "thani", "noun", [K, NA, MQ], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«second» — a naʿt.", "«ikinci» — na't."),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the khabar.", "«… olan» — haber."),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MAW], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ — صِلَةٌ.", "«is» — the relative clause.", "«olan» — sıla."),
  tok("مَعْمُولًا", "mamul", "noun", [K, KN, IMF], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«governed»", "«ma'mûl»"),
  tok("دَائِمًا", "daiman", "noun", [K, MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ.", "«always»", "«dâimâ»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("اثْنَانِ", "ithnan", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two» — the khabar.", "«iki» — haber."),
  tok("أَيْضًا", "aydan", "noun", [K, MM], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ: آضَ أَيْضًا.", "«too» — the absolute object of a dropped verb.", "«da» — hazfedilmiş fiilin mef'ûl-i mutlakı.", punct=":"),
  awwal(),
  tok("الِاسْمُ", "ism", "noun", [K, MK, KK], "خَبَرٌ مَرْفُوعٌ.", "«the noun» — the khabar.", "«isim» — haber."),
  tok("مُطْلَقًا", "mutlaq", "noun", [K, HL, IMF], "حَالٌ مَنْصُوبٌ.", "«absolutely» — a ḥāl.", "«mutlak olarak» — hâl.", punct="،"),
 ]})
# ----------- s6 — so that even the noun-verbs were ruled to have a maḥall
S.append({"id": "s6", "translation": {"en": "So much so that it was ruled of the noun-verbs that they are in the place of rafʿ by the ibtidāʾ, their doer filling the place of the khabar — or in the place of naṣb as a maṣdar.", "tr": "Öyle ki isim fiiller hakkında, ibtidâ üzere mahallen merfû olup fâillerinin haberin yerini tuttuğuna — veya mastariyet üzere mahallen mansûb olduğuna — hükmedildi."},
 "tokens": [
  tok("حَتَّى", "hatta", "part", [K, "hatta-particle" if False else AT], "حَرْفُ ابْتِدَاءٍ — تَدْخُلُ عَلَى الْجُمْلَةِ لِلْغَايَةِ.", "«so much so that» — the ḥattā that opens a sentence.", "«öyle ki» — cümle başı hattâ."),
  tok("حُكِمَ", "hakama", "verb", [K, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«it was ruled»", "«hükmedildi»"),
  tok("عَلَى", "ala", "prep", [K, HJ, NF], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَائِبُ الْفَاعِلِ.", "«of» — the jarr phrase as the deputy doer.", "«hakkında» — câr-mecrûr nâib-i fâil."),
  tok("أَسْمَاءِ", "ism", "noun", [K, HJ, ID, JT, IFL], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«the nouns of»", "«isimleri»"),
  tok("الْأَفْعَالِ", "fil", "noun", [K, ID, JT, IFL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَسْمَاءُ الْأَفْعَالِ.", "«the verbs» — the noun-verbs.", "«fiiller» — isim fiiller."),
  tok("بِأَنَّهَا", "anna", "part", [K, HJ, IN], "الْبَاءُ حَرْفُ جَرٍّ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْبَاءِ.", "«that they» — the clause under the bāʾ.", "«… olduğuna» — bâ altındaki cümle.", segments=[seg("بِ", "bi", "prep"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  tok("مَرْفُوعَةُ", "marfua", "noun", [K, IN, ID, IMF, MH], "خَبَرُ أَنَّ مَرْفُوعٌ، مُضَافٌ — إِضَافَةٌ لَفْظِيَّةٌ.", "«raised of» — the khabar of anna, annexed.", "«merfû» — enne'nin haberi, muzâf."),
  tok("الْمَحَلِّ", "mahall", "noun", [K, ID, MH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْإِعْرَابُ الْمَحَلِّيُّ.", "«place» — the local iʿrāb.", "«mahal» — mahallî i'râb."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«by»", "«üzere»"),
  tok("الِابْتِدَاءِ", "ibtida-nahw", "noun", [K, HJ, MSD, MK, AQ], "مَجْرُورٌ بِعَلَى — الْعَامِلُ الْمَعْنَوِيُّ الرَّافِعُ لِلْمُبْتَدَإِ.", "«the ibtidāʾ» — the maʿnawī raiser of the mubtada.", "«ibtidâ» — mübtedâyı ref' eden mânevî âmil."),
  tok("وَفَاعِلُهَا", "fail-doer", "noun", [K, AT, MK, ID, FL], "الْوَاوُ لِلْحَالِ، وَفَاعِلُهَا مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their doer» — the mubtada of the ḥāl clause.", "«fâilleri» — hâl cümlesinin mübtedâsı.", segments=[seg("وَ", "wa", "conj"), seg("فَاعِلُ", "fail-doer", "noun"), pr3fs()]),
  tok("سَادٌّ", "sadd-filling", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلِ سَدَّ.", "«filling» — the khabar: the ism fāʿil of «to fill».", "«tutan» — haber: sedde'nin ism-i fâili."),
  tok("مَسَدَّ", "masadd", "noun", [K, MF, ID, MSD], "ظَرْفُ مَكَانٍ (مَصْدَرٌ مِيمِيٌّ) مَنْصُوبٌ، مُضَافٌ.", "«the place of» — the mīm-maṣdar as a ẓarf.", "«yerini» — zarf olarak mimli mastar."),
  tok("الْخَبَرِ", "khabar-predicate", "noun", [K, ID, MK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the khabar»", "«haberin»", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مَنْصُوبَةُ", "mansuba", "noun", [K, AT, ID, IMF, MH], "مَعْطُوفٌ عَلَى مَرْفُوعَةُ مَرْفُوعٌ، مُضَافٌ.", "«in naṣb of» — joined to «raised».", "«mansûb» — merfûa'ya ma'tûf."),
  tok("الْمَحَلِّ", "mahall", "noun", [K, ID, MH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«place»", "«mahal»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«as»", "«üzere»"),
  tok("الْمَصْدَرِيَّةِ", "masdariyya", "noun", [K, HJ, MSD, MM], "مَجْرُورٌ بِعَلَى — عَلَى أَنَّهَا مَصْدَرٌ نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ.", "«being a maṣdar» — as a maṣdar standing for the absolute object.", "«mastariyet» — mef'ûl-i mutlak yerine mastar olarak.", punct="،"),
 ]})
# ----------- s7 — though some said: no maḥall, for they carry a verb's sense
S.append({"id": "s7", "translation": {"en": "— even though some of them said: they have no place in the iʿrāb, because they carry the sense of the verb.", "tr": "— bazıları «fiil mânâsında olduklarından i'râbdan mahalleri yoktur» demiş olsa da."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, SH], "الْوَاوُ لِلْحَالِ، وَإِنْ وَصْلِيَّةٌ — بِمَعْنَى: وَلَوْ.", "«even though» — the concessive in.", "«… olsa da» — vasliyye in.", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("قَالَ", "qala", "verb", [K, FL, HV], "فِعْلٌ مَاضٍ.", "«said»", "«dedi»"),
  tok("بَعْضُهُمْ", "bad", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«some of them» — the doer.", "«bazıları» — fâil.", punct=":", segments=[seg("بَعْضُ", "bad", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  *mahall_la(),
  tok("لَهَا", "li", "prep", [K, HJ, LAJ, MK], "اللَّامُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرُ لَا.", "«for them» — the khabar of lā.", "«onlar için» — lâ'nın haberi.", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«in»", "«-dan»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, HJ, MH], "مَجْرُورٌ بِمِنْ.", "«the iʿrāb»", "«i'râbdan»"),
  tok("لِكَوْنِهَا", "kawn", "noun", [K, HJ, ID, MSD, MFL], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَكَوْنِهَا مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — اسْمُ الْمَصْدَرِ.", "«because of their being» — the lām of cause.", "«olmaları sebebiyle» — ta'lîl lâmı.", segments=[seg("لِ", "li", "prep"), seg("كَوْنِ", "kawn", "noun"), pr3fs()]),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MQ, KN], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — خَبَرُ كَوْنِهَا.", "«in the sense of» — the khabar of «being».", "«mânâsında» — kevn'in haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiil»", punct="."),
 ]})
# ----------- s8 — the ḍamīr al-faṣl ruled a particle
S.append({"id": "s8", "translation": {"en": "And [it was ruled] of the pronoun of separation — as in «Zayd was [he] the standing one» — that it is a particle, against some of them, who say it is a noun with no place in the iʿrāb.", "tr": "Fasıl zamiri hakkında da — «Zeyd, o, ayakta olandı» gibi — harf olduğuna hükmedildi; «o, i'râbdan mahalli olmayan bir isimdir» diyen bazılarının hilâfına."},
 "tokens": [
  tok("وَعَلَى", "ala", "prep", [K, AT, HJ, NF], "الْوَاوُ عَاطِفَةٌ، وَعَلَى حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى عَلَى أَسْمَاءِ الْأَفْعَالِ: حُكِمَ عَلَى.", "«and of» — joined to «of the noun-verbs».", "«ve … hakkında» — esmâi'l-ef'âl'e ma'tûf.", segments=wa("عَلَى", "ala", "prep")),
  tok("ضَمِيرِ", "damir", "noun", [K, HJ, ID, DF], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«the pronoun of»", "«zamiri»"),
  tok("الْفَصْلِ", "fasl", "noun", [K, ID, DF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — ضَمِيرُ الْفَصْلِ: يَفْصِلُ الْخَبَرَ عَنِ النَّعْتِ.", "«separation» — the pronoun that parts khabar from naʿt.", "«fasıl» — haberi na'ttan ayıran zamir.", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in»", "«… gibi»", punct=":"),
  tok("كَانَ", "kana", "verb", [K, KN, HV, DF], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ نَاقِصٌ.", "«was» — kāna.", "«idi» — kâne."),
  tok("زَيْدٌ", "zayd", "propn", [K, KN, DF], "اسْمُ كَانَ مَرْفُوعٌ.", "«Zayd» — the ism of kāna.", "«Zeyd» — kâne'nin ismi."),
  tok("هُوَ", "huwa", "pron", [K, DF], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ — حَرْفٌ عِنْدَ الْمُصَنِّفِ.", "«he» — the pronoun of separation: no maḥall; a particle for the author.", "«o» — fasıl zamiri: mahalli yok; müellife göre harf."),
  tok("الْقَائِمَ", "qaim", "noun", [K, KN, IFA, DF], "خَبَرُ كَانَ مَنْصُوبٌ.", "«the standing one» — the khabar of kāna.", "«ayakta olan» — kâne'nin haberi.", punct="،"),
  tok("بِكَوْنِهِ", "kawn", "noun", [K, HJ, ID, MSD, NF], "الْبَاءُ حَرْفُ جَرٍّ، وَكَوْنِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِحُكِمَ: حُكِمَ عَلَيْهِ بِكَوْنِهِ.", "«with its being» — what was ruled of it.", "«olması ile» — hakkında hükmedilen.", segments=[seg("بِ", "bi", "prep"), seg("كَوْنِ", "kawn", "noun"), pr3msi()]),
  tok("حَرْفًا", "harf", "noun", [K, KN, KK, DF], "خَبَرُ كَوْنِهِ مَنْصُوبٌ.", "«a particle» — the khabar of «being».", "«harf» — kevn'in haberi.", punct="،"),
  tok("خِلَافًا", "khilaf", "noun", [K, HL, MM], "حَالٌ (أَوْ مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ) مَنْصُوبٌ — مُخَالِفًا.", "«contrary» — a ḥāl: differing.", "«hilâfına» — hâl: muhalif olarak."),
  tok("لِبَعْضِهِمْ", "bad", "noun", [K, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَبَعْضِهِمْ مَجْرُورٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«to some of them»", "«bazılarına»", segments=[seg("لِ", "li", "prep"), seg("بَعْضِ", "bad", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("يَقُولُ", "qala", "verb", [K, NA, FL, HV, JS, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ نَعْتٌ لِبَعْضٍ (أَوْ حَالٌ).", "«who says» — the ṣifa clause of «some».", "«diyen» — ba'd'ın sıfat cümlesi.", punct=":"),
  tok("إِنَّهُ", "inna", "part", [K, IN], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا — مَكْسُورَةٌ بَعْدَ الْقَوْلِ.", "«that it» — inna with the kasra after «says».", "«ki o» — kavilden sonra meksûr inne.", segments=[seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("اسْمٌ", "ism", "noun", [K, IN, KK], "خَبَرُ إِنَّ مَرْفُوعٌ.", "«a noun» — the khabar of inna.", "«isim» — inne'nin haberi."),
  *mahall_la(),
  tok("لَهُ", "li", "prep", [K, HJ, LAJ, MK], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — خَبَرُ لَا.", "«for it» — the khabar of lā.", "«onun için» — lâ'nın haberi.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-dan»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, HJ, MH], "مَجْرُورٌ بِمِنْ.", "«the iʿrāb»", "«i'râbdan»", punct="."),
 ]})
# ----------- s9 — the lām on the participles: a particle for some, a relative noun for most
S.append({"id": "s9", "translation": {"en": "As for the lām that enters upon the participles, some of them said it is a particle like the others, and most of them said it is a relative noun with the sense of «he who» and «she who», whose iʿrāb was given to what follows it when it passed from being a verb to being a noun.", "tr": "Sıfatların başına gelen lâm'a gelince, bazıları «o da diğerleri gibi harftir» dedi; çoğu ise «ellezî ve elletî mânâsında bir ism-i mevsûldür; fiillikten isimliğe geçince i'râbı kendisinden sonrakine verilmiştir» dedi."},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT, SH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for» — the particle of detail.", "«… -e gelince» — tafsîl harfi.", segments=wa("أَمَّا", "amma", "part")),
  tok("اللَّامُ", "lam-letter", "noun", [K, MK, SH], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the lām» — the mubtada.", "«lâm» — mübtedâ."),
  tok("الدَّاخِلَةُ", "dakhil", "noun", [K, NA, IFA], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلِ دَخَلَ.", "«that enters» — a naʿt.", "«giren» — na't."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«upon»", "«-e»"),
  tok("الصِّفَاتِ", "sifa", "noun", [K, HJ, JMU, IFA], "مَجْرُورٌ بِعَلَى بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ: الصِّفَاتُ الْمُشْتَقَّةُ كَاسْمِ الْفَاعِلِ.", "«the participles» — the derived attributes such as the ism fāʿil.", "«sıfatlar» — ism-i fâil gibi müştak sıfatlar."),
  tok("فَقَالَ", "qala", "verb", [K, SH, FL, HV], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَقَالَ فِعْلٌ مَاضٍ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ.", "«said» — the fāʾ of ammā's answer; the khabar clause.", "«dedi» — emmâ'nın cevap fâsı; haber cümlesi.", segments=fa("قَالَ", "qala", "verb")),
  tok("بَعْضُهُمْ", "bad", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«some of them» — the doer.", "«bazıları» — fâil.", punct=":", segments=[seg("بَعْضُ", "bad", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("إِنَّهَا", "inna", "part", [K, IN], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«that it» — inna.", "«ki o» — inne.", segments=[seg("إِنَّ", "inna", "part"), pr3fs()]),
  tok("حَرْفٌ", "harf", "noun", [K, IN, KK], "خَبَرُ إِنَّ مَرْفُوعٌ.", "«a particle» — the khabar of inna.", "«harf» — inne'nin haberi."),
  tok("كَغَيْرِهَا", "ghayr", "noun", [K, HJ, ID], "الْكَافُ حَرْفُ جَرٍّ، وَغَيْرِهَا مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — كَسَائِرِ اللَّامَاتِ.", "«like the others» — like the other lāms.", "«diğerleri gibi» — diğer lâmlar gibi.", punct="،", segments=[seg("كَ", "ka", "prep"), seg("غَيْرِ", "ghayr", "noun"), pr3fs()]),
  tok("وَقَالَ", "qala", "verb", [K, AT, FL, HV], "الْوَاوُ عَاطِفَةٌ، وَقَالَ فِعْلٌ مَاضٍ.", "«and said»", "«ve dedi»", segments=wa("قَالَ", "qala", "verb")),
  tok("أَكْثَرُهُمْ", "akthar", "noun", [K, FL, ID, "ism-tafdil"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«most of them» — the doer.", "«çoğu» — fâil.", punct=":", segments=[seg("أَكْثَرُ", "akthar", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("هِيَ", "hiya", "pron", [K, MK], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — مَقُولُ الْقَوْلِ.", "«it» — the mubtada.", "«o» — mübtedâ."),
  tok("اسْمٌ", "ism", "noun", [K, MK, KK], "خَبَرٌ مَرْفُوعٌ.", "«a noun» — the khabar.", "«isim» — haber."),
  tok("مَوْصُولٌ", "mawsul", "noun", [K, NA, MAW, IMF], "نَعْتٌ مَرْفُوعٌ.", "«relative» — a naʿt.", "«mevsûl» — na't."),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«with the sense of»", "«mânâsında»", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("الَّذِي", "alladhi", "pron", [K, ID, MAW], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«he who»", "«ellezî»"),
  tok("وَالَّتِي", "allati", "pron", [K, AT, MAW], "الْوَاوُ عَاطِفَةٌ، وَالَّتِي مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«and she who»", "«ve elletî»", punct="،", segments=wa("الَّتِي", "allati", "pron")),
  tok("أُعْطِيَ", "aata", "verb", [K, NF, F4, MQ, JS], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِاسْمٌ (أَوْ حَالٌ).", "«was given» — a further ṣifa clause.", "«verilmiş» — ikinci sıfat cümlesi."),
  tok("إِعْرَابُهَا", "irab", "noun", [K, NF, ID], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its iʿrāb» — the deputy doer.", "«i'râbı» — nâib-i fâil.", segments=[seg("إِعْرَابُ", "irab", "noun"), pr3fs()]),
  tok("لِمَا", "ma-mawsula", "pron", [K, HJ, MAW], "اللَّامُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — الْمَفْعُولُ الثَّانِي لِأُعْطِيَ.", "«to what» — the second object of «was given».", "«… şeye» — u'tiye'nin ikinci mef'ûlü.", segments=[seg("لِ", "li", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("بَعْدَهَا", "bada", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«after it» — the relative clause.", "«ondan sonra» — sıla.", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  tok("لَمَّا", "lamma", "part", [K, MF], "ظَرْفٌ بِمَعْنَى حِينَ.", "«when»", "«-ince»"),
  tok("انْتَقَلَ", "intaqala", "verb", [K, FL, F8, MF], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْمَوْصُولُ مَعَ صِلَتِهِ.", "«it passed» — the relative with its clause.", "«geçti» — sılasıyla mevsûl."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("الْفِعْلِيَّةِ", "filiyya", "noun", [K, HJ, NSB], "مَجْرُورٌ بِمِنْ — كَوْنُ الصِّلَةِ فِعْلًا: ضَرَبَ.", "«verb-hood» — the clause's being a verb: ضَرَبَ.", "«fiillik» — sılanın fiil oluşu."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("الِاسْمِيَّةِ", "ismiyya", "noun", [K, HJ, NSB], "مَجْرُورٌ بِإِلَى — كَوْنُهَا اسْمًا: ضَارِب.", "«noun-hood» — its being a noun: ضَارِب.", "«isimlik» — isim oluşu.", punct="."),
 ]})
# ----------- s10 — the origin of جَاءَنِي الضَّارِبُ زَيْدًا
S.append({"id": "s10", "translation": {"en": "So the origin of «there came to me the striker of Zayd» is «there came to me he who struck Zayd»: the first is governed and the second is not governed.", "tr": "Böylece «câenî ed-dâribu Zeyden»in aslı «câenî ellezî darabe Zeyden»dir: ilki ma'mûl, ikincisi ma'mûl değildir."},
 "tokens": [
  tok("فَأَصْلُ", "asl", "noun", [K, AT, MK, ID], "الْفَاءُ لِلتَّفْرِيعِ، وَأَصْلُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«so the origin of» — the mubtada.", "«böylece aslı» — mübtedâ.", segments=fa("أَصْلُ", "asl", "noun")),
  tok("جَاءَنِي", "jaa", "verb", [K, ID, FL, HV, MB, MAW], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me» — the cited clause, annexed.", "«bana geldi» — hikâye edilen, muzâfun ileyh.", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("الضَّارِبُ", "darib", "noun", [K, FL, IFA, MAW], "فَاعِلٌ مَرْفُوعٌ — اللَّامُ فِيهِ مَوْصُولَةٌ وَالضَّارِبُ صِلَتُهَا عِنْدَ الْأَكْثَرِ.", "«the striker» — the doer; its lām the relative, the participle its clause.", "«vuran» — fâil; lâmı mevsûl, sıfat onun sılası."),
  tok("زَيْدًا", "zayd", "propn", [K, MB, IFA], "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ مَنْصُوبٌ.", "«Zayd» — the participle's object.", "«Zeyd» — ism-i fâilin mef'ûlü.", punct=":"),
  tok("جَاءَنِي", "jaa", "verb", [K, MK, HT, FL, HV, MB], "لَفْظٌ مَحْكِيٌّ: خَبَرُ الْمُبْتَدَإِ أَصْلُ فِي مَحَلِّ رَفْعٍ — فِعْلٌ مَاضٍ وَنُونُ الْوِقَايَةِ وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me» — the quoted sentence as the khabar.", "«bana geldi» — haber olan hikâye edilen cümle.", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("الَّذِي", "alladhi", "pron", [K, FL, MAW], "اسْمٌ مَوْصُولٌ فَاعِلٌ فِي مَحَلِّ رَفْعٍ.", "«he who» — the doer.", "«… olan» — fâil."),
  tok("ضَرَبَ", "daraba", "verb", [K, FL, MAW], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةُ الَّذِي.", "«struck» — the relative clause.", "«vurdu» — sıla."),
  tok("زَيْدًا", "zayd", "propn", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«Zayd» — the object.", "«Zeyd» — mef'ûl.", punct="،"),
  tok("فَالْأَوَّلُ", "awwal", "noun", [K, AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ — الَّذِي.", "«so the first» — «he who»: the mubtada.", "«ilki» — ellezî: mübtedâ.", segments=fa("الْأَوَّلُ", "awwal", "noun")),
  tok("مَعْمُولٌ", "mamul", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ — فَاعِلُ جَاءَ.", "«governed» — the khabar: the doer of «came».", "«ma'mûl» — haber: câe'nin fâili."),
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — ضَرَبَ.", "«and the second» — «struck»: the mubtada.", "«ikincisi» — darabe: mübtedâ.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("غَيْرُ", "ghayr", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«not» — the khabar, annexed.", "«değil» — haber, muzâf."),
  tok("مَعْمُولٍ", "mamul", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمَاضِي لَا يُعْمَلُ فِيهِ.", "«governed» — the māḍī is not governed.", "«ma'mûl» — mâzîde amel edilmez.", punct="."),
 ]})
# ----------- s11 — the ruling reversed, favouring the wording
S.append({"id": "s11", "translation": {"en": "Then when this speech was altered, the first came into the shape of a particle and the second into the shape of a noun, so the ruling was reversed — giving the side of the wording precedence over the side of the meaning in the iʿrāb, which is a ruling of the wording.", "tr": "Bu söz değiştirilince ilki harf sûretine, ikincisi isim sûretine girdi; böylece hüküm tersine döndü — lafzî bir hüküm olan i'râbda lafız cihetini mânâ cihetine tercih ederek."},
 "tokens": [
  tok("فَلَمَّا", "lamma", "part", [K, AT, MF], "الْفَاءُ لِلتَّفْرِيعِ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«then when»", "«-ince»", segments=fa("لَمَّا", "lamma", "part")),
  tok("غُيِّرَ", "ghayyara", "verb", [K, NF, "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«was altered»", "«değiştirildi»"),
  tok("هٰذَا", "hadha", "pron", [K, NF, ISH], "اسْمُ إِشَارَةٍ نَائِبُ فَاعِلٍ فِي مَحَلِّ رَفْعٍ.", "«this» — the deputy doer.", "«bu» — nâib-i fâil."),
  tok("الْكَلَامُ", "kalam", "noun", [K, BD, KK], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ — جَاءَنِي الَّذِي ضَرَبَ زَيْدًا.", "«speech» — a badal of the demonstrative.", "«söz» — ism-i işâretin bedeli."),
  tok("صَارَ", "sara", "verb", [K, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ — جَوَابُ لَمَّا.", "«came to be» — the answer of «when».", "«oldu» — lemmâ'nın cevabı."),
  tok("الْأَوَّلُ", "awwal", "noun", [K, KN], "اسْمُ صَارَ مَرْفُوعٌ — الَّذِي.", "«the first» — the ism of ṣāra.", "«ilki» — sâra'nın ismi."),
  tok("فِي", "fi", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ صَارَ.", "«in» — the khabar of ṣāra.", "«-de» — sâra'nın haberi."),
  tok("صُورَةِ", "sura", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the shape of»", "«sûretinde»"),
  tok("الْحَرْفِ", "harf", "noun", [K, ID, KK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اللَّامُ.", "«a particle» — the lām.", "«harf» — lâm."),
  tok("وَالثَّانِي", "thani", "noun", [K, AT, KN, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مَعْطُوفٌ عَلَى الْأَوَّلُ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — ضَرَبَ.", "«and the second» — «struck».", "«ve ikincisi» — darabe.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("فِي", "fi", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("صُورَةِ", "sura", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the shape of»", "«sûretinde»"),
  tok("الِاسْمِ", "ism", "noun", [K, ID, KK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — ضَارِب.", "«a noun» — ضَارِب.", "«isim» — dârib.", punct="،"),
  tok("فَانْعَكَسَ", "inakasa", "verb", [K, AT, FL, F7], "الْفَاءُ عَاطِفَةٌ، وَانْعَكَسَ فِعْلٌ مَاضٍ.", "«so was reversed»", "«böylece tersine döndü»", segments=fa("انْعَكَسَ", "inakasa", "verb")),
  tok("الْحُكْمُ", "hukm", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«the ruling» — the doer.", "«hüküm» — fâil."),
  tok("تَرْجِيحًا", "tarjih", "noun", [K, MFL, MSD, "form-ii-verbs"], "مَفْعُولٌ لَهُ مَنْصُوبٌ — مَصْدَرُ رَجَّحَ.", "«giving precedence» — the object of cause.", "«tercih ederek» — mef'ûlün leh."),
  tok("لِجَانِبِ", "janib", "noun", [K, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَجَانِبِ مَجْرُورٌ، مُضَافٌ.", "«to the side of»", "«cihetine»", segments=[seg("لِ", "li", "prep"), seg("جَانِبِ", "janib", "noun")]),
  tok("اللَّفْظِ", "lafz", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the wording»", "«lafzın»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«over»", "«-e»"),
  tok("جَانِبِ", "janib", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«the side of»", "«cihetine»"),
  tok("الْمَعْنَى", "mana", "noun", [K, ID, MQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the meaning»", "«mânânın»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the iʿrāb»", "«i'râbda»"),
  tok("الَّذِي", "alladhi", "pron", [K, NA, MAW], "اسْمٌ مَوْصُولٌ نَعْتٌ لِلْإِعْرَابِ فِي مَحَلِّ جَرٍّ.", "«which» — a naʿt.", "«ki o» — na't."),
  tok("هُوَ", "huwa", "pron", [K, MK, MAW], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — صِلَةٌ.", "«is» — the mubtada of the relative clause.", "«o» — sılanın mübtedâsı."),
  tok("حُكْمٌ", "hukm", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«a ruling» — the khabar.", "«bir hüküm» — haber."),
  tok("لَفْظِيٌّ", "lafzi", "noun", [K, NA, NSB], "نَعْتٌ مَرْفُوعٌ.", "«of the wording» — a naʿt.", "«lafzî» — na't.", punct="."),
 ]})
# ----------- s12 — the second always-governed: the muḍāriʿ
S.append({"id": "s12", "translation": {"en": "And the second is the muḍāriʿ verb.", "tr": "İkincisi muzâri fiildir."},
 "tokens": [
  thani_wa(),
  tok("الْفِعْلُ", "fil", "noun", [K, MK, MR], "خَبَرٌ مَرْفُوعٌ.", "«the verb» — the khabar.", "«fiil» — haber."),
  tok("الْمُضَارِعُ", "mudari", "noun", [K, NA, MR], "نَعْتٌ مَرْفُوعٌ.", "«muḍāriʿ» — a naʿt.", "«muzâri» — na't.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

NEW = {
 "mudaraa": G("mudaraa", "مُضَارَعَة", "ض ر ع", "noun", "resemblance — حَرْفُ الْمُضَارَعَةِ: the prefix letter of the muḍāriʿ (أ ن ي ت)", "muzâraat — harfü'l-muzâraa: muzârinin ön harfi (e n y t)", 4, form="III"),
 "mushabih": G("mushabih", "مُشَابِه", "ش ب ه", "noun", "resembling, similar (ism fāʿil of شَابَهَ)", "benzeyen, müşâbih (şâbehe'nin ism-i fâili)", 3),
 "araba": G("araba", "أَعْرَبَ", "ع ر ب", "verb", "to decline (a word), to give it iʿrāb; to express clearly", "i'râb vermek; açıkça ifade etmek", 3, form="IV"),
 "kufi": G("kufi", "كُوفِيّ", None, "noun", "Kufan — of Kufa; الْكُوفِيُّونَ the Kufan grammarians", "Kûfeli; el-Kûfiyyûn: Kûfe nahivcileri", 4),
 "majzum": G("majzum", "مَجْزُوم", "ج ز م", "noun", "in the jussive (majzūm)", "meczûm, cezimli", 2),
 "masadd": G("masadd", "مَسَدّ", "س د د", "noun", "the place filled — سَدَّ مَسَدَّهُ: to fill its place, stand in for it", "yeri — sedde meseddehu: yerini tutmak", 4),
 "sadd-filling": G("sadd-filling", "سَادّ", "س د د", "noun", "filling, standing in (ism fāʿil of سَدَّ) — سَادٌّ مَسَدَّ الْخَبَرِ", "yerini tutan (sedde'nin ism-i fâili) — sâddün meseddi'l-haber", 4),
 "mansuba": G("mansuba", "مَنْصُوبَة", "ن ص ب", "noun", "in the accusative (feminine of manṣūb) — مَنْصُوبَةُ الْمَحَلِّ", "mansûb (müennes) — mansûbetü'l-mahall", 3),
 "ibtida-nahw": G("ibtida-nahw", "الِابْتِدَاء", "ب د أ", "noun", "the ibtidāʾ — the maʿnawī governor that raises the mubtada", "ibtidâ — mübtedâyı ref' eden mânevî âmil", 4, form="VIII"),
 "inakasa": G("inakasa", "اِنْعَكَسَ", "ع ك س", "verb", "to be reversed, inverted", "tersine dönmek", 3, form="VII"),
 "tarjih": G("tarjih", "تَرْجِيح", "ر ج ح", "noun", "giving precedence, preferring (maṣdar of رَجَّحَ)", "tercih, üstün tutma (reccaha'nın mastarı)", 3, form="II"),
 "filiyya": G("filiyya", "الْفِعْلِيَّة", "ف ع ل", "noun", "verb-hood — being a verb (the nisba abstract)", "fiillik — fiil olma", 4),
 "ismiyya": G("ismiyya", "الِاسْمِيَّة", "س م و", "noun", "noun-hood — being a noun (the nisba abstract)", "isimlik — isim olma", 4),
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
put_morph(mo, "araba", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَعْرَب", "عْرِب", "أَعْرِب", "إِعْرَاب", "مُعْرِب", "مُعْرَب", "أُعْرِبَ", "يُعْرَبُ", "مُتَعَدٍّ: أَعْرَبَ الْكَلِمَةَ — أَعْطَاهَا إِعْرَابَهَا."))
put_morph(mo, "inakasa", _sg.derived(_sg.B7, _sg.W7, "َ", "اِنْعَكَس", "نْعَكِس", "اِنْعَكِس", "اِنْعِكَاس", "مُنْعَكِس", None, None, None, "لَازِمٌ: انْعَكَسَ الْحُكْمُ — صَارَ عَكْسَ مَا كَانَ."))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch18 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("alima", "waqaa", "kana", "hadhafa", "sara", "araba", "amila", "kharaja", "ada-return", "qala", "hakama", "aata", "intaqala", "jaa", "daraba", "ghayyara", "inakasa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَعْمُولُ وَأَقْسَامُهُ: مَا لَا يُعْمَلُ فِيهِ أَصْلًا وَمَا يُعْمَلُ فِيهِ دَائِمًا", "en": "The governed word and its divisions: what is never governed, what is always governed", "tr": "Ma'mûl ve kısımları: hiç amel edilmeyen, dâimâ amel edilen"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الباب الثاني في المعمول", "الكافية لابن الحاجب — الاسم المعرب والمبني", "الإنصاف في مسائل الخلاف للأنباري — إعراب فعل الأمر"],
 "amil": "الْمَعْمُول — the word a governor acts on: outside composition nothing governs or is governed; inside it, the particle and the lām-less imperative are never governed (the Basrans — the imperative lost the muḍāriʿ's letter and so its likeness to the noun; the Kufans — it is jazm'd by an estimated lām), the noun and the muḍāriʿ always are (even the noun-verbs have a maḥall, the ḍamīr al-faṣl is a particle, the lām of the participle a relative whose iʿrāb passed to what follows it)",
 "question": {
  "en": ["What is the second bāb about? The governed word (al-maʿmūl). A coined word outside composition is neither governed nor governing; in composition every word falls into one of three divisions.",
         "What is never governed? Two things: the particle, absolutely; and the imperative without the lām — according to the Basrans.",
         "Why do the Basrans say the imperative is not governed? Because the letter of the muḍāriʿ (أ ن ي ت) was what made the muḍāriʿ resemble the noun and so be declined and governed; once that letter is dropped the verb leaves the likeness and returns to its origin, the binaʾ.",
         "What do the Kufans say? That the imperative is declined — in jazm by an estimated lām: اضْرِبْ from لِتَضْرِبْ.",
         "What is always governed? Two things: the noun, absolutely, and the muḍāriʿ verb.",
         "How far does «the noun, absolutely» reach? To the noun-verbs: they were ruled to be in the place of rafʿ by the ibtidāʾ with their doer filling the khabar's place, or in the place of naṣb as a maṣdar — though some say they have no maḥall because they carry a verb's sense.",
         "And the pronoun of separation? كَانَ زَيْدٌ هُوَ الْقَائِمَ — هُوَ was ruled a particle, against those who call it a noun with no maḥall.",
         "And the lām on the participles? Some: a particle like the other lāms. Most: a relative noun meaning الَّذِي / الَّتِي whose iʿrāb was given to what follows it when the clause passed from verb to noun — the origin of جَاءَنِي الضَّارِبُ زَيْدًا is جَاءَنِي الَّذِي ضَرَبَ زَيْدًا, where the first word is governed and the second is not; altered, the first took a particle's shape and the second a noun's, and the ruling was reversed, the wording's side outweighing the meaning's in the iʿrāb, which is a ruling of the wording.",
         "What does the engine READ here? The DabtEngine keeps the particle and the bare imperative on their binaʾ, declines every noun and muḍāriʿ, gives the noun-verb's doer its rafʿ, leaves the pronoun of separation without a maḥall, and reads الضَّارِبُ زَيْدًا as a participle with its object."],
  "tr": ["İkinci bab neyi anlatır? Ma'mûlü. Vaz' edilmiş bir lafız terkip dışında ne ma'mûl ne âmildir; terkipte her kelime üç kısımdan birine girer.",
         "Hiç ma'mûl olmayan nedir? İki şey: mutlak olarak harf ve — Basralılara göre — lâmsız emir.",
         "Basralılar emrin ma'mûl olmadığını niçin söyler? Çünkü muzâraat harfi (e n y t) muzâriyi isme benzeten, bu yüzden i'râb aldıran ve kendisinde amel ettiren şeydi; o harf düşünce fiil benzerlikten çıkar ve aslına, binâya döner.",
         "Kûfeliler ne der? Emir mu'rebdir — takdîrî bir lâmla meczûmdur: idrib, li-tadrib'den.",
         "Dâimâ ma'mûl olan nedir? İki şey: mutlak olarak isim ve muzâri fiil.",
         "«Mutlak olarak isim» nereye kadar uzanır? İsim fiillere: ibtidâ üzere mahallen merfû olup fâilleri haberin yerini tutar, ya da mastariyet üzere mahallen mansûbdurlar — bazıları fiil mânâsı taşıdıkları için mahalleri olmadığını söylese de.",
         "Fasıl zamiri? Kâne Zeydün hüve'l-kâime — hüve harf sayıldı; onu mahalsiz bir isim sayanların hilâfına.",
         "Sıfatların başındaki lâm? Bazıları: diğer lâmlar gibi harf. Çoğu: ellezî / elletî mânâsında ism-i mevsûl; cümle fiilden isme geçince i'râbı kendisinden sonrakine verildi — câenî ed-dâribu Zeyden'in aslı câenî ellezî darabe Zeyden'dir; ilki ma'mûl, ikincisi değil; değişince ilki harf, ikincisi isim sûretine girdi ve hüküm tersine döndü; lafzî bir hüküm olan i'râbda lafız ciheti mânâ cihetine ağır bastı.",
         "Motor burada neyi OKUR? DabtEngine harfi ve yalın emri binâlarında tutar, her ismi ve muzâriyi çeker, isim fiilin fâiline ref'ini verir, fasıl zamirini mahalsiz bırakır ve ed-dâribu Zeyden'i mef'ûllü ism-i fâil olarak okur."],
 },
 "plain": {"en": "A word only gets a case when it sits in a sentence. Even then particles never take one, nor does a bare command like «strike!» (the Basrans: it lost the prefix that made verbs noun-like; the Kufans: a hidden lām governs it). Nouns and present-tense verbs always take one — even noun-verbs like «hush!» have a slot.",
           "tr": "Bir kelime ancak cümle içinde i'râb alır. O zaman bile harfler asla almaz; «vur!» gibi yalın emir de almaz (Basralılara göre onu isme benzeten ön eki kaybetti; Kûfelilere göre gizli bir lâm onu cezm eder). İsimler ve muzâri fiiller daima alır — müellife göre «sus!» gibi isim fiillerin bile bir mahalli vardır."},
 "explanation": {"en": "The second bāb of the Iẓhār turns from the governor to the governed. Coined words outside composition are neither governed nor governing; in composition they are of three divisions. The first is never governed at all: the particle absolutely, and the imperative without the lām according to the Basrans — when the letter of the muḍāriʿ, by which the muḍāriʿ resembled the noun and was therefore declined and governed, is dropped, the verb leaves the likeness and returns to its origin, the binaʾ; the Kufans hold it declined, in jazm by an estimated lām. The second is always governed: the noun absolutely — so that even the noun-verbs were ruled to have a maḥall (rafʿ by the ibtidāʾ with their doer filling the khabar's place, or naṣb as a maṣdar), though some deny them a maḥall for carrying a verb's sense; the pronoun of separation in كَانَ زَيْدٌ هُوَ الْقَائِمَ was ruled a particle against those who call it a noun with no maḥall; and the lām on the participles is for some a particle like the others, for most a relative noun meaning الَّذِي and الَّتِي whose iʿrāb was given to what follows it when the clause passed from verb to noun — the origin of جَاءَنِي الضَّارِبُ زَيْدًا being جَاءَنِي الَّذِي ضَرَبَ زَيْدًا, the first governed and the second not, until the altered shapes reversed the ruling, the wording's side outweighing the meaning's in the iʿrāb, a ruling of the wording — and the muḍāriʿ verb.",
                 "tr": "İzhâr'ın ikinci babı âmilden ma'mûle döner. Vaz' edilmiş lafızlar terkip dışında ne ma'mûl ne âmildir; terkipte üç kısımdır. İlki hiç ma'mûl olmaz: mutlak olarak harf ve Basralılara göre lâmsız emir — muzâriyi isme benzeten ve bu yüzden i'râb aldırıp amel ettiren muzâraat harfi düşünce fiil benzerlikten çıkar ve aslına, binâya döner; Kûfeliler onu takdîrî bir lâmla meczûm, mu'reb sayar. İkincisi dâimâ ma'mûldür: mutlak olarak isim — öyle ki isim fiillerin bile mahalli olduğuna hükmedildi (ibtidâ ile ref', fâilleri haberin yerini tutar; ya da mastariyetle nasb), bazıları fiil mânâsı taşıdıkları için mahallerini inkâr etse de; kâne Zeydün hüve'l-kâime'deki fasıl zamiri, onu mahalsiz bir isim sayanların hilâfına harf sayıldı; sıfatların başındaki lâm bazılarına göre diğerleri gibi harf, çoğuna göre ellezî ve elletî mânâsında ism-i mevsûldür; cümle fiilden isme geçince i'râbı sonrakine verildi — câenî ed-dâribu Zeyden'in aslı câenî ellezî darabe Zeyden'dir; ilki ma'mûl, ikincisi değil; değişen sûretler hükmü tersine çevirdi, lafzî bir hüküm olan i'râbda lafız ciheti ağır bastı — ve muzâri fiil."},
 "examples": [
  {"ar": "إِذَا لَمْ تَقَعْ فِي التَّرْكِيبِ لَمْ تَكُنْ مَعْمُولَةً كَمَا لَا تَكُونُ عَامِلَةً", "en": "no governing and no being governed outside composition", "tr": "terkip dışında ne amel ne ma'mûliyet", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "الْحَرْفُ مُطْلَقًا، وَالْأَمْرُ بِغَيْرِ اللَّامِ عِنْدَ الْبَصْرِيِّينَ", "en": "the two things never governed", "tr": "hiç ma'mûl olmayan iki şey", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "هُوَ مُعْرَبٌ مَجْزُومٌ بِلَامٍ مُقَدَّرَةٍ", "en": "the Kufans on the imperative", "tr": "Kûfelilerin emir görüşü", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "مَرْفُوعَةُ الْمَحَلِّ عَلَى الِابْتِدَاءِ وَفَاعِلُهَا سَادٌّ مَسَدَّ الْخَبَرِ", "en": "the noun-verbs' maḥall", "tr": "isim fiillerin mahalli", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "كَانَ زَيْدٌ هُوَ الْقَائِمَ", "en": "the pronoun of separation, ruled a particle", "tr": "harf sayılan fasıl zamiri", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
  {"ar": "جَاءَنِي الضَّارِبُ زَيْدًا — أَصْلُهُ جَاءَنِي الَّذِي ضَرَبَ زَيْدًا", "en": "the lām of the participle as a relative", "tr": "mevsûl olarak sıfat lâmı", "sourceStory": "izhar-al-asrar", "sentence": "s10"},
 ],
 "commonMistakes": [
  {"wrong": "اضْرِبُ", "right": "اضْرِبْ", "why": {"en": "the bare imperative is built on sukūn: no governor touches it", "tr": "yalın emir sükûn üzere mebnîdir: hiçbir âmil ona dokunmaz"}},
  {"wrong": "كَانَ زَيْدٌ هُوَ الْقَائِمُ", "right": "كَانَ زَيْدٌ هُوَ الْقَائِمَ", "why": {"en": "the pronoun of separation has no maḥall; the khabar of kāna stays in naṣb", "tr": "fasıl zamirinin mahalli yoktur; kâne'nin haberi mansûb kalır"}},
  {"wrong": "جَاءَنِي الضَّارِبُ زَيْدٌ", "right": "جَاءَنِي الضَّارِبُ زَيْدًا", "why": {"en": "the participle after the lām governs its object as its verb would", "tr": "lâmdan sonraki ism-i fâil mef'ûlünü fiili gibi nasb eder"}},
 ],
}
ADD_EN = (" Chapter 18 (print pp. 115-117): the second bāb, on the governed word — words outside composition neither governed nor governing, three divisions inside it (s1); the first division, never governed: the particle and the lām-less imperative (s2), the Basrans' reason (s3) and the Kufans' view (s4); the second division, always governed: the noun absolutely (s5) — the noun-verbs' maḥall (s6-s7), the pronoun of separation (s8), the lām on the participles as a relative (s9) with the origin of جَاءَنِي الضَّارِبُ زَيْدًا (s10) and the reversed ruling (s11) — and the muḍāriʿ (s12). The print's ثلثة is given standard.")
ADD_TR = (" On sekizinci bab (baskı s. 115-117): ikinci bab, ma'mûl — terkip dışındaki lafızlar ne ma'mûl ne âmil, terkipte üç kısım (s1); birinci kısım, hiç ma'mûl olmayan: harf ve lâmsız emir (s2), Basralıların gerekçesi (s3) ve Kûfelilerin görüşü (s4); ikinci kısım, dâimâ ma'mûl olan: mutlak olarak isim (s5) — isim fiillerin mahalli (s6-s7), fasıl zamiri (s8), mevsûl olarak sıfat lâmı (s9), câenî ed-dâribu Zeyden'in aslı (s10) ve tersine dönen hüküm (s11) — ve muzâri (s12). Baskının ثلثة'si standart imlâyla verildi.")
write_out(18, S, TITLE, ADD_EN, ADD_TR, "pp. 115-117", GLOSS_ADD, notes=(NOTE,),
          related=((AQ, [K]), (K17, [K]), (IFL, [K]), (DF, [K]), (MAW, [K]), (AMR, [K]), (MH, [K])))
report(18, S, GLOSS_ADD, (NOTE,))
