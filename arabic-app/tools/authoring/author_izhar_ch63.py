# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 63: the lāzim mabnī continued — some of the kināyāt: كَمْ of the question, with its following word in naṣb as
# tamyīz (كَمْ رَجُلًا), and كَمْ of statement meaning «many», annexed to what follows (كَمْ رَجُلٍ); كَذَا for number, its following word in naṣb as tamyīz
# (عِنْدِي كَذَا دِرْهَمًا); كَيْتَ and ذَيْتَ for speech; the words holding the sense of إِنْ or of the question, other than أَيّ and أَيَّة; and some of the
# adverbs — أَمْسِ، قَطُّ، عَوْضُ، مُذْ، مُنْذُ، إِذَا، إِذْ، لَمَّا، مَتَى، أَنَّى، أَيَّانَ، كَيْفَ، حَيْثُ، لَدَى، لَدُنْ، لَدْ, and the nominal كَاف, عَلَى and عَنْ. Print p. 158.
# The Ottoman commentary (izhar-full-corrected l. 1912 ff.) is followed for the readings.
#   python3 author_izhar_ch63.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; IRB = "al-murab-wal-mabni-wal-irab"; JMS = "jam-muannath-salim"; MST = "al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"; KN2 = "kinaya"; ADW = "adawat-al-tasawwur"; IDH = "idha-shartiyya"
K = "al-mabni-al-lazim-al-kinayat-wal-mutadamminat-wal-zuruf"
K62 = "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"
TITLE = {"ar": "الْمَبْنِيُّ اللَّازِمُ: الْكِنَايَاتُ كَمْ وَكَذَا وَكَيْتَ وَذَيْتَ، وَالْمُتَضَمِّنَاتُ مَعْنَى إِنْ وَالِاسْتِفْهَامِ، وَبَعْضُ الظُّرُوفِ", "en": "The lāzim mabnī: the kināyāt kam, kadhā, kayta and dhayta; the words holding the sense of in and of the question; some of the adverbs", "tr": "Lâzım mebnî: kinâyeler kem, kezâ, keyte ve zeyte; in ve istifhâm manasını içeren kelimeler; bazı zarflar"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def zarf(form, lex, en, tr, first=False, punct=None, extra=(), ar=None):
    a = ar or (("لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — ظَرْفٌ مَبْنِيٌّ." if first else "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " مَعْطُوفٌ — ظَرْفٌ مَبْنِيٌّ."))
    return tok(form, lex, "noun", [K, MF, IRB] + ([ID] if first else [AT]) + list(extra), a, en, tr, punct=punct, segments=None if first else wa(form[2:], lex, "noun"))

# ----------- s1 — the kināyāt: kam
S.append({"id": "s1", "translation": {"en": "And some of the kināyāt — and that is kam: for the question, so that what follows it is put in naṣb as tamyīz — as in «how many men?»; and for statement, meaning «many», so that it is annexed to what follows it — as in «many a man»;", "tr": "Ve kinâyelerin bazısı — o da kem'dir: istifhâm için, ondan sonraki temyiz olarak nasbedilir — «kaç adam?» gibi; ve haber için, çokluk manasında, ondan sonrakine muzâf olur — «nice adam» gibi;"},
 "tokens": [
  tok("وَبَعْضُ", "bad", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَبَعْضُ مَعْطُوفٌ عَلَى مَا قَبْلَهُ مِنَ اللَّازِمِ مَرْفُوعٌ، مُضَافٌ.", "«and some of»", "«ve bazısı»", segments=wa("بَعْضُ", "bad", "noun")),
  tok("الْكِنَايَاتِ", "kinaya", "noun", [K, ID, JMS, KN2], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَا يُكْنَى بِهِ عَنِ الْعَدَدِ أَوِ الْحَدِيثِ.", "«the kināyāt» — what stands in for a number or a saying.", "«kinâyeler» — sayı ya da sözün yerini tutan.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that is»", "«o da»", segments=wa("هُوَ", "huwa", "pron")),
  tok("كَمْ", "kam", "noun", [K, MK, ADW, IST, IRB], "خَبَرٌ مَرْفُوعٌ تَقْدِيرًا — لَفْظٌ مَحْكِيٌّ مَبْنِيٌّ عَلَى السُّكُونِ.", "«kam» — the khabar; cited, built on sukūn.", "«kem» — haber; alıntı, sükûn üzere mebnî."),
  tok("لِلِاسْتِفْهَامِ", "istifham", "noun", [K, HJ, MSD, IST], "اللَّامُ حَرْفُ جَرٍّ، وَالِاسْتِفْهَامِ مَجْرُورٌ — حَالٌ: كَائِنًا لِلِاسْتِفْهَامِ.", "«for the question»", "«istifhâm için»", punct="،", segments=[seg("لِ", "li", "prep"), seg("الِاسْتِفْهَامِ", "istifham", "noun")]),
  tok("فَيُنْصَبُ", "nasaba-nahw", "verb", [K, AT, MR, NF], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيُنْصَبُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«so … is put in naṣb»", "«ve … nasbedilir»", segments=fa("يُنْصَبُ", "nasaba-nahw", "verb")),
  tok("مَا", "ma-mawsula", "pron", [K, NF, MAW], "اسْمٌ مَوْصُولٌ نَائِبُ فَاعِلٍ فِي مَحَلِّ رَفْعٍ.", "«what»", "«… olan»"),
  tok("بَعْدَهَا", "bada", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«follows it»", "«ondan sonraki»", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«as»", "«olarak»"),
  tok("التَّمْيِيزِ", "tamyiz-noun", "noun", [K, HJ, MSD, F2, TMZ], "مَجْرُورٌ بِعَلَى — عَلَى جِهَةِ التَّمْيِيزِ.", "«tamyīz»", "«temyiz»", punct="،"),
  nahw(punct=":"),
  tok("كَمْ", "kam", "noun", [K, MK, ADW, IST, IRB], "لَفْظٌ مَحْكِيٌّ: اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«how many»", "«kaç»"),
  tok("رَجُلًا", "rajul", "noun", [K, TMZ], "تَمْيِيزٌ مَنْصُوبٌ — مُفْرَدٌ بَعْدَ كَمِ الِاسْتِفْهَامِيَّةِ.", "«men» — a singular tamyīz after the question-kam.", "«adam» — istifhâm kem'inden sonra müfred temyiz.", punct="؟"),
  tok("وَلِلْخَبَرِيَّةِ", "khabariyya", "noun", [K, AT, HJ, NSB], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَالْخَبَرِيَّةِ مَجْرُورٌ — مَعْطُوفٌ عَلَى لِلِاسْتِفْهَامِ.", "«and for statement»", "«ve haber için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("الْخَبَرِيَّةِ", "khabariyya", "noun")]),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«in the sense of»", "«manasında»", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("التَّكْثِيرِ", "takthir", "noun", [K, ID, MSD, F2], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«making many»", "«çokluk»", punct="،"),
  tok("فَيُضَافُ", "adafa", "verb", [K, AT, MR, NF, F4, ID], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيُضَافُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — كَمْ.", "«so it is annexed»", "«ve muzâf olur»", segments=fa("يُضَافُ", "adafa", "verb")),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَا", "ma-mawsula", "pron", [K, HJ, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what»", "«… olan»"),
  tok("بَعْدَهُ", "bada", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«follows it»", "«ondan sonraki»", punct="،", segments=[seg("بَعْدَ", "bada", "noun"), pr3ms()]),
  nahw(punct=":"),
  tok("كَمْ", "kam", "noun", [K, MK, ADW, IRB, ID], "لَفْظٌ مَحْكِيٌّ: كَمِ الْخَبَرِيَّةُ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ، مُضَافٌ.", "«many a»", "«nice»"),
  tok("رَجُلٍ", "rajul", "noun", [K, ID, TMZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَمْيِيزُ كَمِ الْخَبَرِيَّةِ بِالْإِضَافَةِ.", "«man» — the tamyīz of the statement-kam, annexed.", "«adam» — haber kem'inin temyizi, izafetle.", punct="،"),
 ]})
# ----------- s2 — kadhā, kayta and dhayta
S.append({"id": "s2", "translation": {"en": "and kadhā for number, which puts what follows it in naṣb as tamyīz — as in «I have so-and-so many dirhams»; and kayta and dhayta for speech;", "tr": "ve sayı için kezâ, ondan sonrakini temyiz olarak nasbeder — «bende şu kadar dirhem var» gibi; ve söz için keyte ve zeyte;"},
 "tokens": [
  tok("وَكَذَا", "kadha", "part", [K, AT, MK, KN2, IRB], "الْوَاوُ عَاطِفَةٌ، وَكَذَا مَعْطُوفٌ عَلَى كَمْ فِي مَحَلِّ رَفْعٍ — لَفْظٌ مَحْكِيٌّ مَبْنِيٌّ.", "«and kadhā» — «so-and-so many».", "«ve kezâ» — «şu kadar».", segments=wa("كَذَا", "kadha", "part")),
  tok("لِلْعَدَدِ", "adad", "noun", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْعَدَدِ مَجْرُورٌ — حَالٌ: كَائِنًا لِلْعَدَدِ.", "«for number»", "«sayı için»", punct="،", segments=[seg("لِ", "li", "prep"), seg("الْعَدَدِ", "adad", "noun")]),
  tok("يَنْصِبُ", "nasaba-nahw", "verb", [K, MR, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — كَذَا.", "«it puts in naṣb»", "«nasbeder»"),
  tok("مَا", "ma-mawsula", "pron", [K, MB, MAW], "اسْمٌ مَوْصُولٌ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ.", "«what»", "«… olanı»"),
  tok("بَعْدَهُ", "bada", "noun", [K, MF, ID, MAW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«follows it»", "«ondan sonraki»", segments=[seg("بَعْدَ", "bada", "noun"), pr3ms()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«as»", "«olarak»"),
  tok("التَّمْيِيزِ", "tamyiz-noun", "noun", [K, HJ, MSD, F2, TMZ], "مَجْرُورٌ بِعَلَى.", "«tamyīz»", "«temyiz»", punct="،"),
  nahw(punct=":"),
  tok("عِنْدِي", "inda", "noun", [K, MF, ID, YM, MK], "لَفْظٌ مَحْكِيٌّ: ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«I have» — the fronted khabar.", "«bende var» — öne alınmış haber.", segments=[seg("عِنْدِ", "inda", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("كَذَا", "kadha", "part", [K, MK, KN2, IRB], "مُبْتَدَأٌ مُؤَخَّرٌ فِي مَحَلِّ رَفْعٍ — كِنَايَةٌ عَنِ الْعَدَدِ.", "«so-and-so many» — the mubtadaʾ, a kināya for the number.", "«şu kadar» — mübteda, sayının kinâyesi."),
  tok("دِرْهَمًا", "dirham", "noun", [K, TMZ], "تَمْيِيزٌ مَنْصُوبٌ.", "«dirhams»", "«dirhem»", punct="،"),
  tok("وَكَيْتَ", "kayta", "part", [K, AT, KN2, IRB], "الْوَاوُ عَاطِفَةٌ، وَكَيْتَ مَعْطُوفٌ عَلَى كَمْ — لَفْظٌ مَحْكِيٌّ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«and kayta» — «such-and-such»", "«ve keyte» — «şöyle»", segments=wa("كَيْتَ", "kayta", "part")),
  tok("وَذَيْتَ", "dhayta", "part", [K, AT, KN2, IRB], "الْوَاوُ عَاطِفَةٌ، وَذَيْتَ مَعْطُوفٌ — مَبْنِيٌّ عَلَى الْفَتْحِ.", "«and dhayta» — «such-and-such»", "«ve zeyte» — «böyle»", segments=wa("ذَيْتَ", "dhayta", "part")),
  tok("لِلْحَدِيثِ", "hadith", "noun", [K, HJ, KN2], "اللَّامُ حَرْفُ جَرٍّ، وَالْحَدِيثِ مَجْرُورٌ — كِنَايَةٌ عَنِ الْكَلَامِ: قَالَ كَيْتَ وَكَيْتَ.", "«for speech» — standing in for reported words.", "«söz için» — aktarılan sözün yerini tutar.", punct="،", segments=[seg("لِ", "li", "prep"), seg("الْحَدِيثِ", "hadith", "noun")]),
 ]})
# ----------- s3 — the words holding the sense of in or the question
S.append({"id": "s3", "translation": {"en": "and the words containing the sense of «in» or of the question, other than ayy and ayya;", "tr": "ve eyy ve eyye dışında in ya da istifhâm manasını içeren kelimeler;"},
 "tokens": [
  tok("وَالْكَلِمَاتُ", "kalima", "noun", [K, AT, JMS], "الْوَاوُ عَاطِفَةٌ، وَالْكَلِمَاتُ مَعْطُوفٌ عَلَى مَا قَبْلَهُ مَرْفُوعٌ.", "«and the words»", "«ve kelimeler»", segments=wa("الْكَلِمَاتُ", "kalima", "noun")),
  tok("الْمُتَضَمِّنَةُ", "mutadammin", "noun", [K, NA, IFA, F5], "نَعْتٌ مَرْفُوعٌ.", "«containing»", "«içeren»"),
  tok("لِمَعْنَى", "mana", "noun", [K, HJ, ID, MQ], "اللَّامُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — مَفْعُولُ الْمُتَضَمِّنَةِ بِاللَّامِ.", "«the sense of»", "«manasını»", segments=[seg("لِ", "li", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("إِنْ", "in-shartiyya", "part", [K, ID, INS], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — إِنِ الشَّرْطِيَّةُ: مَنْ وَمَا وَمَهْمَا.", "«in» — the conditional: man, mā, mahmā.", "«in» — şart in'i: men, mâ, mehmâ."),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«ya da»"),
  tok("الِاسْتِفْهَامِ", "istifham", "noun", [K, AT, MSD, IST], "مَعْطُوفٌ عَلَى إِنْ مَجْرُورٌ — مَنْ وَمَا وَكَمْ وَكَيْفَ.", "«the question» — man, mā, kam, kayfa.", "«istifhâm» — men, mâ, kem, keyfe."),
  tok("غَيْرَ", "ghayr", "noun", [K, MST, ID], "مُسْتَثْنًى بِغَيْرَ مَنْصُوبٌ، مُضَافٌ.", "«other than»", "«dışında»"),
  tok("أَيٍّ", "ayy", "pron", [K, ID, IST], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ayy»", "«eyy»"),
  tok("وَأَيَّةٍ", "ayya", "pron", [K, AT, IST], "الْوَاوُ عَاطِفَةٌ، وَأَيَّةٍ مَعْطُوفٌ مَجْرُورٌ — فَإِنَّهُمَا مُعْرَبَانِ لِلُزُومِ الْإِضَافَةِ.", "«and ayya» — both declined, being always annexed.", "«ve eyye» — ikisi de daima muzâf olduğundan mu'reb.", punct="،", segments=wa("أَيَّةٍ", "ayya", "pron")),
 ]})
# ----------- s4 — some of the adverbs
S.append({"id": "s4", "translation": {"en": "and some of the adverbs — as in amsi, qaṭṭu, ʿawḍu, mudh, mundhu, idhā, idh, lammā, matā, annā, ayyāna, kayfa, ḥaythu, ladā, ladun, lad, and the nominal kāf, ʿalā and ʿan.", "tr": "ve bazı zarflar — emsi, kattu, avdu, müz, münzü, izâ, iz, lemmâ, metâ, ennâ, eyyâne, keyfe, haysü, ledâ, ledün, led ve isim olan kâf, alâ ve an gibi."},
 "tokens": [
  tok("وَبَعْضُ", "bad", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَبَعْضُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and some of»", "«ve bazısı»", segments=wa("بَعْضُ", "bad", "noun")),
  tok("الظُّرُوفِ", "zarf", "noun", [K, ID, JT, MF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the adverbs»", "«zarfların»", punct="،"),
  nahw(punct=":"),
  zarf("أَمْسِ", "ams", "«amsi» — yesterday, on kasra", "«emsi» — dün, kesre üzere", first=True),
  zarf("وَقَطُّ", "qatt", "«qaṭṭu» — ever (of the past), on ḍamma", "«kattu» — asla (geçmiş için), damme üzere"),
  zarf("وَعَوْضُ", "awd-adverb", "«ʿawḍu» — ever (of the future), on ḍamma", "«avdu» — asla (gelecek için), damme üzere"),
  zarf("وَمُذْ", "mudh", "«mudh» — since", "«müz» — -den beri"),
  zarf("وَمُنْذُ", "mundhu", "«mundhu» — since", "«münzü» — -den beri"),
  zarf("وَإِذَا", "idha", "«idhā» — when", "«izâ» — -dığında", extra=(IDH,)),
  zarf("وَإِذْ", "idh", "«idh» — when (past)", "«iz» — o zaman ki"),
  zarf("وَلَمَّا", "lamma", "«lammā» — when", "«lemmâ» — -ınca"),
  zarf("وَمَتَى", "mata", "«matā» — when?", "«metâ» — ne zaman", extra=(ADW,)),
  zarf("وَأَنَّى", "anna-shartiyya", "«annā» — whence, however", "«ennâ» — nereden, nasıl", extra=(ADW,)),
  zarf("وَأَيَّانَ", "ayyana", "«ayyāna» — when?", "«eyyâne» — ne zaman", extra=(ADW,)),
  zarf("وَكَيْفَ", "kayfa", "«kayfa» — how?", "«keyfe» — nasıl", extra=(ADW,)),
  zarf("وَحَيْثُ", "haythu", "«ḥaythu» — where", "«haysü» — nerede"),
  zarf("وَلَدَى", "lada", "«ladā» — with, at", "«ledâ» — yanında"),
  zarf("وَلَدُنْ", "ladun", "«ladun» — from, at", "«ledün» — katında"),
  zarf("وَلَدْ", "lad", "«lad» — a form of ladun", "«led» — ledün'ün bir şekli"),
  tok("وَالْكَافِ", "kaf-letter", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَالْكَافِ مَعْطُوفٌ مَجْرُورٌ — الْكَافُ الِاسْمِيَّةُ بِمَعْنَى مِثْلٍ.", "«and the kāf» — the nominal kāf, «like».", "«ve kâf» — isim olan kâf, «gibi».", segments=wa("الْكَافِ", "kaf-letter", "noun")),
  tok("وَعَلَى", "ala", "prep", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَعَلَى مَعْطُوفٌ — الِاسْمِيَّةُ بِمَعْنَى فَوْقَ.", "«and ʿalā» — the nominal, «above».", "«ve alâ» — isim olanı, «üstü».", segments=wa("عَلَى", "ala", "prep")),
  tok("وَعَنِ", "an", "prep", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَعَنِ مَعْطُوفٌ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ — بِمَعْنَى جَانِبٍ.", "«and ʿan» — the nominal, «the side of».", "«ve an» — isim olanı, «yan».", segments=wa("عَنِ", "an", "prep")),
  tok("الِاسْمِيَّةِ", "ismiyya", "noun", [K, NA, NSB], "نَعْتٌ لِلْكَافِ وَعَلَى وَعَنْ مَجْرُورٌ — حِينَ تَكُونُ أَسْمَاءً بَعْدَ مِنْ: مِنْ عَلَيْهِ، مِنْ عَنْ يَمِينِهِ.", "«nominal» — when they are nouns, after min: min ʿalayhi, min ʿan yamīnihi.", "«isim olan» — min'den sonra isim olduklarında: min aleyhi, min an yemînihî.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "takthir": G("takthir", "تَكْثِير", "ك ث ر", "noun", "making many, multiplying — kam of statement means takthīr", "çoğaltma, teksîr — haber kem'i teksîr manasındadır", 3),
 "kayta": G("kayta", "كَيْتَ", "ك ي ت", "part", "kayta — «such-and-such», a kināya for reported speech, built on fatḥa", "keyte — «şöyle şöyle», aktarılan söz için kinâye, fetha üzere mebnî", 4),
 "dhayta": G("dhayta", "ذَيْتَ", "ذ ي ت", "part", "dhayta — «such-and-such», the companion of kayta, built on fatḥa", "zeyte — «böyle böyle», keyte'nin eşi, fetha üzere mebnî", 4),
 "qatt": G("qatt", "قَطُّ", "ق ط ط", "noun", "qaṭṭu — «ever» of the past (with a negative), built on ḍamma", "kattu — geçmiş için «asla» (olumsuzla), damme üzere mebnî", 3),
 "awd-adverb": G("awd-adverb", "عَوْضُ", "ع و ض", "noun", "ʿawḍu — «ever» of the future (with a negative), built on ḍamma", "avdu — gelecek için «asla» (olumsuzla), damme üzere mebnî", 4),
 "ayyana": G("ayyana", "أَيَّانَ", "أ ي ن", "noun", "ayyāna — «when?», an indeclinable adverb of question and condition", "eyyâne — «ne zaman?», mebnî istifhâm ve şart zarfı", 3),
 "lad": G("lad", "لَدْ", "ل د ن", "noun", "lad — a shortened form of ladun, «at, with»", "led — ledün'ün kısaltılmış şekli, «katında»", 4),
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
print("izhar ch63 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("nasaba-nahw", "adafa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَبْنِيُّ اللَّازِمُ: كَمِ الِاسْتِفْهَامِيَّةُ وَالْخَبَرِيَّةُ وَتَمْيِيزُهُمَا، وَكَذَا وَكَيْتَ وَذَيْتَ، وَمُتَضَمِّنَاتُ إِنْ وَالِاسْتِفْهَامِ، وَالظُّرُوفُ الْمَبْنِيَّةُ", "en": "The lāzim mabnī: kam of question and of statement with their tamyīz, kadhā, kayta and dhayta, the words holding in or the question, and the indeclinable adverbs", "tr": "Lâzım mebnî: temyizleriyle istifhâm ve haber kem'i, kezâ, keyte ve zeyte, in ve istifhâm içeren kelimeler ve mebnî zarflar"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المبني اللازم: الكنايات والظروف", "الكافية لابن الحاجب — الكنايات، الظروف المبنية", "شرح قطر الندى لابن هشام — كم وكأين وكذا"],
 "amil": "the lāzim mabnī continued: the kināyāt — kam of the question with its following word in naṣb as tamyīz (كَمْ رَجُلًا), kam of statement meaning «many», annexed (كَمْ رَجُلٍ); kadhā for number with naṣb tamyīz (عِنْدِي كَذَا دِرْهَمًا); kayta and dhayta for speech; the words holding the sense of in or of the question (ayy and ayya excepted); some adverbs — أَمْسِ، قَطُّ، عَوْضُ، مُذْ، مُنْذُ، إِذَا، إِذْ، لَمَّا، مَتَى، أَنَّى، أَيَّانَ، كَيْفَ، حَيْثُ، لَدَى، لَدُنْ، لَدْ and the nominal كَاف، عَلَى، عَنْ.",
 "question": {
  "en": ["What is a kināya here? A word that stands in for a number or a saying without naming it — kam, kadhā, kayta, dhayta — resembling the particle in its vagueness, so it is built.",
         "How do the two kams differ? Kam of the question takes its following word in naṣb as a singular tamyīz (كَمْ رَجُلًا؟); kam of statement means «many» and is annexed to what follows (كَمْ رَجُلٍ) — the tamyīz in jarr.",
         "What does kadhā do? It stands for a number and takes a naṣb tamyīz: عِنْدِي كَذَا دِرْهَمًا, «I have so-and-so many dirhams».",
         "What are kayta and dhayta? The kināyāt for a saying — قَالَ كَيْتَ وَكَيْتَ, «he said such-and-such» — built on fatḥa.",
         "Which words hold the sense of in or of the question? Man, mā, mahmā and the like for the condition; man, mā, kam, kayfa and the like for the question — all built, save ayy and ayya, which are always annexed and so declined.",
         "Which adverbs are indeclinable? Amsi (on kasra), qaṭṭu and ʿawḍu (on ḍamma, «ever» of the past and the future), mudh and mundhu, idhā, idh, lammā, matā, annā, ayyāna, kayfa, ḥaythu, ladā, ladun and lad — and the kāf, ʿalā and ʿan when they are nouns.",
         "When are the kāf, ʿalā and ʿan nouns? When min enters upon them — مِنْ عَلَيْهِ, مِنْ عَنْ يَمِينِهِ — or the kāf means mithl as a noun; a preposition cannot follow a preposition.",
         "What does the engine READ here? The DabtEngine reads كَمْ and كَذَا as built kināyāt, رَجُلًا and دِرْهَمًا as their naṣb tamyīz and رَجُلٍ as the annexed tamyīz of the statement-kam, the cited adverbs as built forms after نَحْوُ, and the three nominal particles with their describing الِاسْمِيَّةِ."],
  "tr": ["Burada kinâye nedir? Bir sayının ya da sözün adını vermeden yerini tutan kelime — kem, kezâ, keyte, zeyte — kapalılığıyla harfe benzer, bu yüzden mebnîdir.",
         "İki kem nasıl ayrılır? İstifhâm kem'i sonrakini müfred temyiz olarak nasbeder (kem racülen?); haber kem'i «nice» demektir ve sonrakine muzâf olur (kem racülin) — temyiz mecrûr.",
         "Kezâ ne yapar? Bir sayının yerini tutar ve mansûb temyiz alır: indî kezâ dirhemen, «bende şu kadar dirhem var».",
         "Keyte ve zeyte nedir? Bir sözün kinâyeleri — kâle keyte ve keyte, «şöyle şöyle dedi» — fetha üzere mebnî.",
         "Hangi kelimeler in ya da istifhâm manasını içerir? Şart için men, mâ, mehmâ ve benzerleri; istifhâm için men, mâ, kem, keyfe ve benzerleri — hepsi mebnî; daima muzâf olduklarından mu'reb olan eyy ve eyye hariç.",
         "Hangi zarflar mebnîdir? Emsi (kesre üzere), kattu ve avdu (damme üzere, geçmiş ve gelecek için «asla»), müz ve münzü, izâ, iz, lemmâ, metâ, ennâ, eyyâne, keyfe, haysü, ledâ, ledün ve led — ve isim olduklarında kâf, alâ ve an.",
         "Kâf, alâ ve an ne zaman isimdir? Min üzerlerine girince — min aleyhi, min an yemînihî — ya da kâf isim olarak misl manasına gelince; cer harfi cer harfini izleyemez.",
         "Motor burada neyi OKUR? DabtEngine kem ve kezâ'yı mebnî kinâye, racülen ve dirhemen'i mansûb temyizleri, racülin'i haber kem'inin muzâf temyizi, alıntı zarfları nahvü'den sonra mebnî şekiller, üç isimleşmiş harfi sıfatı el-ismiyyeti ile okur."],
 },
 "plain": {"en": "More frozen words: kam «how many / many a» (-an after it in a question, -in in a statement), kadhā «so-and-so many» (with -an), kayta wa-dhayta «such-and-such», the question and condition words (man, mā, kayfa), and adverbs like amsi, qaṭṭu, mundhu, idhā, matā, ḥaythu, ladā. Ayy is the exception: it still takes case.",
           "tr": "Başka donuk sözler: kem «kaç / nice» (soruda -en, haberde -in ile), kezâ «şu kadar» (-en ile), keyte ve zeyte «şöyle böyle», soru ve şart sözleri (men, mâ, keyfe…) ve emsi «dün», kattu «asla», münzü «-den beri», izâ, metâ, haysü, ledâ gibi zarflar. Eyy istisnadır: hâlâ i'râb alır."},
 "explanation": {"en": "The lāzim mabnī continues with some of the kināyāt. Kam for the question puts what follows it in naṣb as tamyīz — كَمْ رَجُلًا؟; kam for statement, meaning «many», is annexed to what follows — كَمْ رَجُلٍ. Kadhā for number puts what follows it in naṣb as tamyīz — عِنْدِي كَذَا دِرْهَمًا. Kayta and dhayta are for speech. Then the words containing the sense of «in» (the condition) or of the question, other than ayy and ayya, which are declined. Then some of the adverbs: أَمْسِ، قَطُّ، عَوْضُ، مُذْ، مُنْذُ، إِذَا، إِذْ، لَمَّا، مَتَى، أَنَّى، أَيَّانَ، كَيْفَ، حَيْثُ، لَدَى، لَدُنْ، لَدْ, and the kāf, ʿalā and ʿan when they are nouns. The non-lāzim mabnī follows.",
                 "tr": "Lâzım mebnî kinâyelerin bazısıyla sürer. İstifhâm için kem, sonrakini temyiz olarak nasbeder — kem racülen?; haber için kem, «nice» manasında, sonrakine muzâf olur — kem racülin. Sayı için kezâ sonrakini temyiz olarak nasbeder — indî kezâ dirhemen. Keyte ve zeyte söz içindir. Sonra «in» (şart) ya da istifhâm manasını içeren kelimeler — mu'reb olan eyy ve eyye hariç. Sonra bazı zarflar: emsi, kattu, avdu, müz, münzü, izâ, iz, lemmâ, metâ, ennâ, eyyâne, keyfe, haysü, ledâ, ledün, led ve isim olduklarında kâf, alâ ve an. Gayr-ı lâzım mebnî gelir."},
 "examples": [
  {"ar": "كَمْ رَجُلًا؟ — كَمْ رَجُلٍ", "en": "kam of question and of statement", "tr": "istifhâm ve haber kem'i", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "عِنْدِي كَذَا دِرْهَمًا، وَكَيْتَ وَذَيْتَ لِلْحَدِيثِ", "en": "kadhā, kayta and dhayta", "tr": "kezâ, keyte ve zeyte", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "الْكَلِمَاتُ الْمُتَضَمِّنَةُ لِمَعْنَى إِنْ أَوِ الِاسْتِفْهَامِ غَيْرَ أَيٍّ وَأَيَّةٍ", "en": "the condition and question words", "tr": "şart ve istifhâm kelimeleri", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "أَمْسِ وَقَطُّ وَعَوْضُ وَمُذْ وَمُنْذُ … وَالْكَافِ وَعَلَى وَعَنِ الِاسْمِيَّةِ", "en": "the indeclinable adverbs", "tr": "mebnî zarflar", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "كَمْ رَجُلٍ؟ (as a question)", "right": "كَمْ رَجُلًا؟", "why": {"en": "the question-kam takes a naṣb tamyīz; the jarr belongs to the statement-kam", "tr": "istifhâm kem'i mansûb temyiz alır; cer haber kem'ine aittir"}},
  {"wrong": "عِنْدِي كَذَا دِرْهَمٍ", "right": "عِنْدِي كَذَا دِرْهَمًا", "why": {"en": "kadhā's tamyīz is in naṣb", "tr": "kezâ'nın temyizi mansûbdur"}},
  {"wrong": "مَا فَعَلْتُهُ عَوْضُ (of the past)", "right": "مَا فَعَلْتُهُ قَطُّ", "why": {"en": "qaṭṭu is for the past, ʿawḍu for the future", "tr": "kattu geçmiş, avdu gelecek içindir"}},
  {"wrong": "جَاءَ أَيُّ (indeclinable)", "right": "أَيّ is declined: جَاءَ أَيُّهُمْ", "why": {"en": "ayy and ayya are excepted from the built words", "tr": "eyy ve eyye mebnîlerden istisnadır"}},
 ],
}
ADD_EN = (" Chapter 63 (print p. 158): the lāzim mabnī continued — kam of question and of statement with their tamyīz (s1); kadhā, kayta and dhayta (s2); the words holding the sense of in or of the question, ayy and ayya excepted (s3); the indeclinable adverbs and the nominal kāf, ʿalā and ʿan (s4).")
ADD_TR = (" Altmış üçüncü bab (baskı s. 158): lâzım mebnî devam — temyizleriyle istifhâm ve haber kem'i (s1); kezâ, keyte ve zeyte (s2); eyy ve eyye hariç in ya da istifhâm manasını içeren kelimeler (s3); mebnî zarflar ve isim olan kâf, alâ ve an (s4).")
write_out(63, S, TITLE, ADD_EN, ADD_TR, "p. 158", GLOSS_ADD, notes=(NOTE,),
          related=((K62, [K]), (IRB, [K]), (TMZ, [K]), (ADW, [K]), (IST, [K]), (MF, [K])))
report(63, S, GLOSS_ADD, (NOTE,))
