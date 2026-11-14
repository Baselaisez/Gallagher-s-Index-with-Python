# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 49: the SECOND follower, the ʿaṭf by particles — a follower between which and its followed word stands one of the
# ten particles: الْوَاوُ وَالْفَاءُ وَثُمَّ وَحَتَّى وَأَوْ وَإِمَّا وَأَمْ وَلَا وَبَلْ وَلٰكِنْ; joining to the attached rafʿ pronoun needs its confirmation by a detached one
# (ضَرَبْتُ أَنَا وَزَيْدٌ) unless a separation falls (ضَرَبْتُ الْيَوْمَ وَزَيْدٌ); joining to the jarr pronoun repeats the jarr-governor (مَرَرْتُ بِكَ وَبِزَيْدٍ،
# اللهُ بَيْنِي وَبَيْنَكَ); the joined word shares the rule of what it is joined to; two words may be joined by one particle to the two governed words of one
# governor (ضَرَبَ زَيْدٌ عَمْرًا وَبَكْرٌ خَالِدًا), not to those of two governors save, on one view, when the jarr-governor is fronted (فِي الدَّارِ زَيْدٌ وَالْحُجْرَةِ
# عَمْرٌو). Print pp. 144–145.
#   python3 author_izhar_ch49.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TW = "tawabi-al-musnad-ilayh"; AW = "anwa-al-waw"; FW = "al-fasl-wa-al-wasl"; TK = "tawkid"; IDH = "idha-shartiyya"; BM = "al-bariz-al-muttasil"
K = "al-atf-bil-huruf-wa-ahkamuh"
K48 = "al-mawsul-wal-muarraf-bil-lam-wal-mudaf"
TITLE = {"ar": "التَّابِعُ الثَّانِي: الْعَطْفُ بِالْحُرُوفِ الْعَشَرَةِ وَأَحْكَامُهُ", "en": "The second follower: the ʿaṭf by the ten particles and its rules", "tr": "İkinci tâbi: on harfle atıf ve hükümleri"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def H(form, lex, en, tr, punct=None, pos="part"): return tok(form, lex, pos, [K, AT], "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — حَرْفُ عَطْفٍ.", en, tr, punct=punct, segments=wa(form[2:], lex, pos))
def waidha(): return tok("وَإِذَا", "idha", "part", [K, AT, IDH, MF], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when»", "«ve … -ince»", segments=wa("إِذَا", "idha", "part"))
def utifa(): return tok("عُطِفَ", "atafa", "verb", [K, IDH, NF, AT], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، فِعْلُ الشَّرْطِ.", "«is joined»", "«atfedilince»")
def ala_damir(gr, punct=None): return [tok("عَلَى", "ala", "prep", [K, HJ, NF], "حَرْفُ جَرٍّ — نَائِبُ الْفَاعِلِ مَحَلًّا.", "«to»", "«-e»"), tok("الضَّمِيرِ", "damir", "noun", [K, HJ, BM], "مَجْرُورٌ بِعَلَى.", "«the pronoun»", "«zamire»")] + gr

# ----------- s1 — the second: the ʿaṭf and the ten particles
S.append({"id": "s1", "translation": {"en": "And the second is the ʿaṭf by particles, and it is a follower between which and its followed word one of the ten particles stands; and they are: the wāw, the fāʾ, «thumma», «ḥattā», «aw», «immā», «am», «lā», «bal» and «lākin»;", "tr": "İkincisi harflerle atıftır: kendisiyle metbûu arasına on harften biri giren tâbidir; onlar: vâv, fâ, sümme, hattâ, ev, immâ, em, lâ, bel ve lâkin;"},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second»", "«ikincisi»", segments=wa("الثَّانِي", "thani", "noun")),
  tok("الْعَطْفُ", "atf", "noun", [K, MK, MSD, TW], "خَبَرٌ مَرْفُوعٌ.", "«the ʿaṭf» — the khabar.", "«atıf» — haber."),
  tok("بِحُرُوفٍ", "harf", "noun", [K, HJ, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَحُرُوفٍ مَجْرُورٌ — لَا عَطْفُ الْبَيَانِ.", "«by particles» — not the ʿaṭf of exposition.", "«harflerle» — atf-ı beyân değil.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("حُرُوفٍ", "harf", "noun")]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("تَابِعٌ", "tabi", "noun", [K, MK, IFA, TW], "خَبَرٌ مَرْفُوعٌ.", "«a follower»", "«bir tâbi»"),
  tok("يَتَوَسَّطُ", "tawassata", "verb", [K, NA, MR, FL, F5, "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ نَعْتٌ.", "«stands» — the clause a naʿt.", "«girer» — cümle sıfat."),
  tok("بَيْنَهُ", "bayna", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«between it»", "«kendisiyle»", segments=[seg("بَيْنَ", "bayna", "noun"), pr3ms()]),
  tok("وَبَيْنَ", "bayna", "noun", [K, AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ ظَرْفٌ مَعْطُوفٌ، مُضَافٌ.", "«and»", "«ve»", segments=wa("بَيْنَ", "bayna", "noun")),
  tok("مَتْبُوعِهِ", "matbu", "noun", [K, ID, IMF, TW], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its followed word»", "«metbûu»", segments=[seg("مَتْبُوعِ", "matbu", "noun"), pr3msi()]),
  tok("أَحَدُ", "ahad", "noun", [K, FL, ID], "فَاعِلُ يَتَوَسَّطُ مَرْفُوعٌ، مُضَافٌ.", "«one of» — the doer.", "«biri» — fâil."),
  tok("الْحُرُوفِ", "harf", "noun", [K, ID, JT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the particles»", "«harflerden»"),
  tok("الْعَشَرَةِ", "ashara", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«ten»", "«on»", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and they are»", "«ve onlar»", punct=":", segments=wa("هِيَ", "hiya", "pron")),
  tok("الْوَاوُ", "waw-letter", "noun", [K, MK, AW], "لَفْظٌ مَحْكِيٌّ: خَبَرٌ مَرْفُوعٌ — لِمُطْلَقِ الْجَمْعِ.", "«the wāw» — for plain joining.", "«vâv» — mutlak cem' için."),
  H("وَالْفَاءُ", "fa-letter", "«and the fāʾ» — order without delay", "«ve fâ» — gecikmesiz sıra", pos="noun"),
  H("وَثُمَّ", "thumma", "«and thumma» — order with delay", "«ve sümme» — gecikmeli sıra"),
  H("وَحَتَّى", "hatta", "«and ḥattā» — the limit", "«ve hattâ» — gâye"),
  H("وَأَوْ", "aw", "«and aw» — one of two", "«ve ev» — ikisinden biri"),
  H("وَإِمَّا", "imma", "«and immā»", "«ve immâ»"),
  H("وَأَمْ", "am", "«and am» — in the question", "«ve em» — soruda"),
  H("وَلَا", "la-atifa", "«and lā» — the denial of the second", "«ve lâ» — ikincinin nefyi"),
  H("وَبَلْ", "bal", "«and bal» — the turning away", "«ve bel» — idrâb"),
  H("وَلٰكِنْ", "lakin", "«and lākin» — the correction", "«ve lâkin» — istidrâk", punct="،"),
 ]})
# ----------- s2 — joining to the attached rafʿ pronoun
S.append({"id": "s2", "translation": {"en": "and when something is joined to the attached rafʿ pronoun, its confirmation by a detached one is obligatory — as in «I struck, I and Zayd» — unless a separation falls, when leaving it is allowed — as in «I struck today, and Zayd»;", "tr": "muttasıl merfû zamire atıf yapılınca onun munfasıl bir zamirle te'kîdi vâcibdir — «ben ve Zeyd dövdüm» gibi — ancak bir fasıl girerse terki câizdir — «bugün dövdüm, ve Zeyd» gibi;"},
 "tokens": [
  waidha(), utifa(),
  *ala_damir([tok("الْمَرْفُوعِ", "marfu", "noun", [K, NA, IMF], "نَعْتٌ مَجْرُورٌ.", "«the rafʿ»", "«merfû»"), tok("الْمُتَّصِلِ", "muttasil", "noun", [K, NA, IFA, BM], "نَعْتٌ ثَانٍ مَجْرُورٌ.", "«attached»", "«muttasıl»")]),
  tok("يَجِبُ", "wajaba", "verb", [K, IDH, MR, FL, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، جَوَابُ الشَّرْطِ.", "«it is obligatory»", "«vâcibdir»"),
  tok("تَأْكِيدُهُ", "takid", "noun", [K, FL, ID, MSD, TK], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الضَّمِيرِ.", "«its confirmation» — the pronoun's.", "«te'kîdi» — zamirin.", segments=[seg("تَأْكِيدُ", "takid", "noun"), pr3ms()]),
  tok("بِمُنْفَصِلٍ", "munfasil", "noun", [K, HJ, IFA], "الْبَاءُ حَرْفُ جَرٍّ، وَمُنْفَصِلٍ مَجْرُورٌ — بِضَمِيرٍ مُنْفَصِلٍ.", "«by a detached one»", "«munfasıl ile»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("مُنْفَصِلٍ", "munfasil", "noun")]),
  nahw(),
  tok("ضَرَبْتُ", "daraba", "verb", [K, FL, AT], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْمَعْطُوفُ عَلَيْهِ.", "«I struck» — the tāʾ is what is joined to.", "«dövdüm» — tâ ma'tûfun aleyh.", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أَنَا", "ana", "pron", [K, TK], "تَوْكِيدٌ لِلتَّاءِ فِي مَحَلِّ رَفْعٍ.", "«I» — the confirming detached pronoun.", "«ben» — te'kîd eden munfasıl zamir."),
  tok("وَزَيْدٌ", "zayd", "propn", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَزَيْدٌ مَعْطُوفٌ عَلَى التَّاءِ مَرْفُوعٌ.", "«and Zayd» — joined to the tāʾ.", "«ve Zeyd» — tâ'ya ma'tûf.", punct="،", segments=wa("زَيْدٌ", "zayd", "propn")),
  tok("إِلَّا", "illa", "part", [K, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«unless»", "«ancak»"),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS], "حَرْفٌ مَصْدَرِيٌّ.", "«that»", "«-sa»"),
  tok("يَقَعَ", "waqaa", "verb", [K, AMS, FL, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ.", "«falls»", "«girerse»"),
  tok("فَصْلٌ", "fasl", "noun", [K, FL, MSD, FW], "فَاعِلٌ مَرْفُوعٌ.", "«a separation»", "«bir fasıl»"),
  tok("فَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْفَاءُ لِلتَّفْرِيعِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«then it is allowed»", "«o zaman câizdir»", segments=fa("يَجُوزُ", "jaaza", "verb")),
  tok("تَرْكُهُ", "tark", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — التَّأْكِيدِ.", "«leaving it» — the confirmation.", "«terki» — te'kîdin.", punct="،", segments=[seg("تَرْكُ", "tark", "noun"), pr3ms()]),
  nahw(),
  tok("ضَرَبْتُ", "daraba", "verb", [K, FL, AT], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck»", "«dövdüm»", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("الْيَوْمَ", "yawm", "noun", [K, MF, FW], "ظَرْفٌ مَنْصُوبٌ — الْفَاصِلُ.", "«today» — the separator.", "«bugün» — fâsıl."),
  tok("وَزَيْدٌ", "zayd", "propn", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَزَيْدٌ مَعْطُوفٌ عَلَى التَّاءِ مَرْفُوعٌ بِلَا تَأْكِيدٍ.", "«and Zayd» — joined without the confirmation.", "«ve Zeyd» — te'kîdsiz ma'tûf.", punct="،", segments=wa("زَيْدٌ", "zayd", "propn")),
 ]})
# ----------- s3 — joining to the jarr pronoun
S.append({"id": "s3", "translation": {"en": "and when something is joined to the jarr pronoun, the jarr-governor is repeated — as in «I passed by you and by Zayd», and «God is between me and between you»;", "tr": "mecrûr zamire atıf yapılınca hâfız tekrar edilir — «sana ve Zeyd'e uğradım» ve «Allah benimle senin aranda» gibi;"},
 "tokens": [
  waidha(), utifa(),
  *ala_damir([tok("الْمَجْرُورِ", "majrur", "noun", [K, NA, IMF], "نَعْتٌ مَجْرُورٌ.", "«the jarr»", "«mecrûr»")]),
  tok("أُعِيدَ", "aada", "verb", [K, IDH, NF, F4, HV], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، جَوَابُ الشَّرْطِ.", "«is repeated»", "«tekrar edilir»"),
  tok("الْخَافِضُ", "khafid", "noun", [K, NF, IFA], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — الْجَارُّ: الْحَرْفُ أَوِ الْمُضَافُ.", "«the jarr-governor» — the particle or the muḍāf.", "«hâfız» — câr: harf veya muzâf.", punct="،"),
  nahw(),
  tok("مَرَرْتُ", "marra", "verb", [K, FL, "doubled-verbs"], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مُضَاعَفٌ، وَالتَّاءُ فَاعِلٌ.", "«I passed»", "«uğradım»", segments=[seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("بِكَ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْكَافُ فِي مَحَلِّ جَرٍّ — الْمَعْطُوفُ عَلَيْهِ.", "«by you» — what is joined to.", "«sana» — ma'tûfun aleyh.", segments=[seg("بِ", "bi", "prep"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَبِزَيْدٍ", "zayd", "propn", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ مُعَادٌ، وَزَيْدٍ مَجْرُورٌ — الْمَعْطُوفُ.", "«and by Zayd» — the bāʾ repeated.", "«ve Zeyd'e» — bâ tekrar edilmiş.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("زَيْدٍ", "zayd", "propn")]),
  tok("وَاللهُ", "allah", "propn", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَاللهُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and God»", "«ve Allah»", segments=wa("اللهُ", "allah", "propn")),
  tok("بَيْنِي", "bayna", "noun", [K, MF, ID, MK, YM], "ظَرْفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«between me» — the khabar.", "«benimle» — haber.", segments=[seg("بَيْنِ", "bayna", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("وَبَيْنَكَ", "bayna", "noun", [K, AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ مُضَافٌ مُعَادٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — الْمَعْطُوفُ.", "«and between you» — the muḍāf repeated.", "«ve senin aranda» — muzâf tekrar edilmiş.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("بَيْنَ", "bayna", "noun"), seg("كَ", "pron-2ms", "pron")]),
 ]})
# ----------- s4 — the joined word shares the rule; two joined by one particle
S.append({"id": "s4", "translation": {"en": "and the joined word is in the rule of what it is joined to, in what is obligatory for it and what is refused to it; and joining two things by one particle to the two governed words of one governor is allowed by agreement — as in «Zayd struck ʿAmr, and Bakr Khālid»;", "tr": "ma'tûf, kendisine vâcib ve yasak olanlarda ma'tûfun aleyhin hükmündedir; iki şeyi bir harfle bir âmilin iki ma'mûlüne atfetmek ittifakla câizdir — «Zeyd Amr'ı dövdü, Bekir de Hâlid'i» gibi;"},
 "tokens": [
  tok("وَالْمَعْطُوفُ", "matuf", "noun", [K, AT, MK, IMF, TW], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمَعْطُوفُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the joined word»", "«ve ma'tûf»", segments=wa("الْمَعْطُوفُ", "matuf", "noun")),
  tok("فِي", "fi", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in» — the phrase as khabar.", "«-de» — câr-mecrûr haber."),
  tok("حُكْمِ", "hukm", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the rule of»", "«hükmünde»"),
  tok("الْمَعْطُوفِ", "matuf", "noun", [K, ID, IMF, TW], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«what is joined»", "«ma'tûfun»"),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ.", "«to» — part of the term.", "«aleyh» — terimin parçası.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("فِيمَا", "ma-mawsula", "pron", [K, HJ, MAW], "فِي حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«in what»", "«-de»", segments=[seg("فِي", "fi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("يَجِبُ", "wajaba", "verb", [K, MAW, MR, FL, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةُ مَا.", "«is obligatory»", "«vâcib olan»"),
  tok("لَهُ", "li", "prep", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — لِلْمَعْطُوفِ عَلَيْهِ.", "«for it»", "«ona»", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("وَيَمْتَنِعُ", "imtanaa", "verb", [K, AT, MR, FL, "form-viii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَمْتَنِعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is refused»", "«ve yasak olan»", segments=wa("يَمْتَنِعُ", "imtanaa", "verb")),
  tok("لَهُ", "li", "prep", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«to it»", "«ona»", punct="،", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ عَاطِفَةٌ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("عَطْفُ", "atf", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«joining»", "«atfetmek»"),
  tok("شَيْئَيْنِ", "shay", "noun", [K, ID, MTH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two things»", "«iki şeyi»"),
  tok("بِحَرْفٍ", "harf", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَحَرْفٍ مَجْرُورٌ.", "«by a particle»", "«bir harfle»", segments=[seg("بِ", "bi", "prep"), seg("حَرْفٍ", "harf", "noun")]),
  tok("وَاحِدٍ", "wahid", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«one»", "«tek»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَعْمُولَيْ", "mamul", "noun", [K, HJ, ID, MTH, IMF], "مَجْرُورٌ بِالْيَاءِ، مُثَنًّى حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "«the two governed words of»", "«iki ma'mûlüne»"),
  tok("عَامِلٍ", "amil", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a governor»", "«bir âmilin»"),
  tok("وَاحِدٍ", "wahid", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«one»", "«tek»"),
  tok("بِالِاتِّفَاقِ", "ittifaq", "noun", [K, HJ, MSD, "form-viii-verbs"], "الْبَاءُ حَرْفُ جَرٍّ، وَالِاتِّفَاقِ مَجْرُورٌ — بِاتِّفَاقِ النُّحَاةِ.", "«by agreement» — of the grammarians.", "«ittifakla» — nahivcilerin.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الِاتِّفَاقِ", "ittifaq", "noun")]),
  nahw(),
  tok("ضَرَبَ", "daraba", "verb", [K, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ — الْعَامِلُ الْوَاحِدُ.", "«struck» — the one governor.", "«dövdü» — tek âmil."),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd»", "«Zeyd»"),
  tok("عَمْرًا", "amr-name", "propn", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«ʿAmr»", "«Amr'ı»"),
  tok("وَبَكْرٌ", "bakr", "propn", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَبَكْرٌ مَعْطُوفٌ عَلَى زَيْدٌ مَرْفُوعٌ.", "«and Bakr» — joined to Zayd.", "«ve Bekir» — Zeyd'e ma'tûf.", segments=wa("بَكْرٌ", "bakr", "propn")),
  tok("خَالِدًا", "khalid", "propn", [K, AT, MB], "مَعْطُوفٌ عَلَى عَمْرًا مَنْصُوبٌ — بِالْوَاوِ نَفْسِهَا.", "«Khālid» — joined to ʿAmr by the same wāw.", "«Hâlid'i» — aynı vâv ile Amr'a ma'tûf.", punct="،"),
 ]})
# ----------- s5 — not to the governed words of two governors, save the fronted jarr
S.append({"id": "s5", "translation": {"en": "and it is not allowed to the two governed words of two governors, save — on one view — when the jarr-governor is fronted, as in «in the house is Zayd, and the room ʿAmr».", "tr": "iki âmilin iki ma'mûlüne câiz değildir; ancak — bir görüşe göre — câr öne alınmışsa, «evde Zeyd, odada Amr» gibi."},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve … değildir»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, LN, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الْعَطْفُ.", "«it is allowed» — the joining.", "«câiz» — atıf."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَعْمُولَيْ", "mamul", "noun", [K, HJ, ID, MTH, IMF], "مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«the two governed words of»", "«iki ma'mûlüne»"),
  tok("عَامِلَيْنِ", "amil", "noun", [K, ID, MTH, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two governors»", "«iki âmilin»"),
  tok("إِلَّا", "illa", "part", [K, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«save»", "«ancak»"),
  tok("عِنْدَ", "inda", "noun", [K, MF, ID, "istithna"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«when»", "«-ince»"),
  tok("تَقْدِيمِ", "taqdim", "noun", [K, ID, MSD, F2], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the fronting of»", "«öne alınması»"),
  tok("الْجَارِّ", "jarr-amil", "noun", [K, ID, IFA, "doubled-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — حَرْفُ الْجَرِّ.", "«the jarr-governor» — the particle of jarr.", "«cârrın» — cer harfi."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«göre»"),
  tok("رَأْيٍ", "ray", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى — رَأْيِ بَعْضِ النُّحَاةِ.", "«one view» — of some grammarians.", "«bir görüşe» — bazı nahivcilerin.", punct="،"),
  nahw(),
  tok("فِي", "fi", "prep", [K, HJ, MK], "لَفْظٌ مَحْكِيٌّ: حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«in» — the fronted khabar.", "«-de» — öne alınmış haber."),
  tok("الدَّارِ", "dar", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the house»", "«ev»"),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«Zayd» — the delayed mubtada.", "«Zeyd» — sona alınmış mübtedâ."),
  tok("وَالْحُجْرَةِ", "hujra", "noun", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَالْحُجْرَةِ مَعْطُوفٌ عَلَى الدَّارِ مَجْرُورٌ — مَعْمُولُ فِي.", "«and the room» — joined to «the house», governed by فِي.", "«ve odada» — ed-dâr'a ma'tûf, fî'nin ma'mûlü.", segments=wa("الْحُجْرَةِ", "hujra", "noun")),
  tok("عَمْرٌو", "amr-name", "propn", [K, AT, MK], "مَعْطُوفٌ عَلَى زَيْدٌ مَرْفُوعٌ — مَعْمُولُ الِابْتِدَاءِ، وَالْوَاوُ زَائِدَةٌ فِي الْخَطِّ.", "«ʿAmr» — joined to Zayd, governed by the mubtadaʾ's governor.", "«Amr» — Zeyd'e ma'tûf, ibtidânın ma'mûlü.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "khafid": G("khafid", "خَافِض", "خ ف ض", "noun", "the jarr-governor — the particle or muḍāf that lowers the noun (Kūfan term)", "hâfız — ismi mecrûr kılan harf veya muzâf (Kûfe terimi)", 4),
 "jarr-amil": G("jarr-amil", "جَارّ", "ج ر ر", "noun", "the jarr-governor — the particle of jarr as governor", "câr — cer harfi, cer âmili", 4),
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
print("izhar ch49 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("tawassata", "atafa", "wajaba", "waqaa", "jaaza", "aada", "marra", "imtanaa", "daraba") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْعَطْفُ بِالْحُرُوفِ الْعَشَرَةِ: التَّأْكِيدُ بِالْمُنْفَصِلِ، إِعَادَةُ الْخَافِضِ، حُكْمُ الْمَعْطُوفِ، وَالْعَطْفُ عَلَى مَعْمُولَيْ عَامِلٍ", "en": "The ʿaṭf by the ten particles: confirming by the detached pronoun, repeating the jarr-governor, the joined word's rule, and joining to two governed words", "tr": "On harfle atıf: munfasılla te'kîd, hâfızın tekrarı, ma'tûfun hükmü ve iki ma'mûle atıf"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — التوابع: العطف بالحروف", "الكافية لابن الحاجب — عطف النسق", "مغني اللبيب لابن هشام — حروف العطف"],
 "amil": "the ʿaṭf by particles is a follower between which and its followed word one of ten particles stands — الْوَاوُ وَالْفَاءُ وَثُمَّ وَحَتَّى وَأَوْ وَإِمَّا وَأَمْ وَلَا وَبَلْ وَلٰكِنْ; joining to the attached rafʿ pronoun needs a detached pronoun's confirmation (ضَرَبْتُ أَنَا وَزَيْدٌ) unless a separation falls (ضَرَبْتُ الْيَوْمَ وَزَيْدٌ); joining to the jarr pronoun repeats the jarr-governor (مَرَرْتُ بِكَ وَبِزَيْدٍ، اللهُ بَيْنِي وَبَيْنَكَ); the joined word shares the rule of what it is joined to; two words joined by one particle to the two governed words of one governor is agreed (ضَرَبَ زَيْدٌ عَمْرًا وَبَكْرٌ خَالِدًا), to those of two governors refused save, on one view, with the jarr-governor fronted (فِي الدَّارِ زَيْدٌ وَالْحُجْرَةِ عَمْرٌو)",
 "question": {
  "en": ["What is the ʿaṭf by particles? A follower with one of ten particles between it and its followed word: الْوَاوُ، الْفَاءُ، ثُمَّ، حَتَّى، أَوْ، إِمَّا، أَمْ، لَا، بَلْ، لٰكِنْ — it takes the followed word's iʿrāb.",
         "How is a word joined to the attached rafʿ pronoun? With a detached pronoun confirming it first: ضَرَبْتُ أَنَا وَزَيْدٌ — not ضَرَبْتُ وَزَيْدٌ; unless a separation falls: ضَرَبْتُ الْيَوْمَ وَزَيْدٌ.",
         "And to the jarr pronoun? The jarr-governor is repeated — the particle (مَرَرْتُ بِكَ وَبِزَيْدٍ) or the muḍāf (اللهُ بَيْنِي وَبَيْنَكَ); not مَرَرْتُ بِكَ وَزَيْدٍ.",
         "What is the joined word's rule? That of what it is joined to, in what is obligatory and what is refused for it.",
         "May one particle join two words to two governed words? Of one governor, yes, by agreement: ضَرَبَ زَيْدٌ عَمْرًا وَبَكْرٌ خَالِدًا — Bakr to Zayd, Khālid to ʿAmr, by one wāw.",
         "And to the governed words of two governors? Refused — save, on one view, when the jarr-governor is fronted: فِي الدَّارِ زَيْدٌ وَالْحُجْرَةِ عَمْرٌو, the room governed by فِي and ʿAmr by the mubtadaʾ's governor.",
         "What does the engine READ here? The DabtEngine reads the wāw-joined name after a bound-doer verb as joined to the doer in rafʿ, the repeated بِ before the joined name as its jarr-governor, the pair وَبَكْرٌ خَالِدًا by their written cases as joined to doer and object, and وَالْحُجْرَةِ عَمْرٌو as joined to the jarr noun and the mubtadaʾ."],
  "tr": ["Harflerle atıf nedir? Kendisiyle metbûu arasına on harften biri giren tâbi: vâv, fâ, sümme, hattâ, ev, immâ, em, lâ, bel, lâkin — metbûun i'râbını alır.",
         "Muttasıl merfû zamire nasıl atıf yapılır? Önce munfasıl bir zamirle te'kîd edilerek: darabtü ene ve Zeydün — darabtü ve Zeydün değil; ancak bir fasıl girerse: darabtü'l-yevme ve Zeydün.",
         "Mecrûr zamire? Hâfız tekrar edilir — harf (merartü bike ve bi-Zeydin) veya muzâf (Allâhu beynî ve beyneke); merartü bike ve Zeydin değil.",
         "Ma'tûfun hükmü nedir? Vâcib ve yasak olanlarda ma'tûfun aleyhin hükmü.",
         "Bir harf iki kelimeyi iki ma'mûle atfedebilir mi? Tek âmilin ma'mûllerine, evet, ittifakla: darabe Zeydün Amren ve Bekrun Hâliden — Bekir Zeyd'e, Hâlid Amr'a, tek vâv ile.",
         "İki âmilin ma'mûllerine? Yasak — ancak bir görüşe göre câr öne alınmışsa: fi'd-dâri Zeydün ve'l-hucrati Amrun; oda fî ile, Amr ibtidâ âmiliyle ma'mûl.",
         "Motor burada neyi OKUR? DabtEngine fâili bağlı fiilden sonra vâv ile bağlanan ismi fâile ma'tûf ref'; ma'tûf isimden önce tekrarlanan bi'yi hâfız; ve Bekrun Hâliden çiftini yazılı hâlleriyle fâile ve mef'ûle ma'tûf; ve'l-hucrati Amrun'u mecrûr isme ve mübtedâya ma'tûf okur."],
 },
 "plain": {"en": "«And»-type words (and, then, or, but, not …) link a second word to a first with the same case. If the first is a subject ending on the verb, say «I» first: «I struck, I and Zayd». If it is «you» after a preposition, repeat it: «by you and by Zayd». One «and» may link two pairs: «Zayd struck ʿAmr, and Bakr Khālid».",
           "tr": "«Ve» türü sözcükler (ve, sonra, veya, fakat, değil …) ikinci sözü ilkine bağlar ve aynı hâli verir. İlk söz fiildeki özne ekiyse önce «ben» de: «ben ve Zeyd dövdüm». Edattan sonraki «sen» ise edatı tekrarla: «sana ve Zeyd'e». Tek bir «ve» iki çifti birden bağlayabilir: «Zeyd Amr'ı dövdü, Bekir de Hâlid'i»."},
 "explanation": {"en": "The second follower is the ʿaṭf by particles: a follower between which and its followed word stands one of the ten particles — الْوَاوُ، الْفَاءُ، ثُمَّ، حَتَّى، أَوْ، إِمَّا، أَمْ، لَا، بَلْ، لٰكِنْ. When something is joined to the attached rafʿ pronoun, its confirmation by a detached pronoun is obligatory (ضَرَبْتُ أَنَا وَزَيْدٌ) unless a separation falls, when it may be left (ضَرَبْتُ الْيَوْمَ وَزَيْدٌ). When something is joined to the jarr pronoun, the jarr-governor is repeated (مَرَرْتُ بِكَ وَبِزَيْدٍ، اللهُ بَيْنِي وَبَيْنَكَ). The joined word is in the rule of what it is joined to, in what is obligatory for it and what is refused. Joining two things by one particle to the two governed words of one governor is allowed by agreement (ضَرَبَ زَيْدٌ عَمْرًا وَبَكْرٌ خَالِدًا); to the governed words of two governors it is not allowed, save — on one view — when the jarr-governor is fronted (فِي الدَّارِ زَيْدٌ وَالْحُجْرَةِ عَمْرٌو).",
                 "tr": "İkinci tâbi harflerle atıftır: kendisiyle metbûu arasına on harften biri giren tâbi — vâv, fâ, sümme, hattâ, ev, immâ, em, lâ, bel, lâkin. Muttasıl merfû zamire atıf yapılınca munfasıl bir zamirle te'kîdi vâcibdir (darabtü ene ve Zeydün); bir fasıl girerse terkedilebilir (darabtü'l-yevme ve Zeydün). Mecrûr zamire atıf yapılınca hâfız tekrar edilir (merartü bike ve bi-Zeydin, Allâhu beynî ve beyneke). Ma'tûf, vâcib ve yasak olanlarda ma'tûfun aleyhin hükmündedir. İki şeyi bir harfle bir âmilin iki ma'mûlüne atfetmek ittifakla câizdir (darabe Zeydün Amren ve Bekrun Hâliden); iki âmilin ma'mûllerine câiz değildir; ancak — bir görüşe göre — câr öne alınmışsa (fi'd-dâri Zeydün ve'l-hucrati Amrun)."},
 "examples": [
  {"ar": "الْوَاوُ وَالْفَاءُ وَثُمَّ وَحَتَّى وَأَوْ وَإِمَّا وَأَمْ وَلَا وَبَلْ وَلٰكِنْ", "en": "the ten particles of ʿaṭf", "tr": "on atıf harfi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "ضَرَبْتُ أَنَا وَزَيْدٌ؛ ضَرَبْتُ الْيَوْمَ وَزَيْدٌ", "en": "the detached confirmation and its omission after a separation", "tr": "munfasıl te'kîd ve fasıldan sonra terki", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "مَرَرْتُ بِكَ وَبِزَيْدٍ، وَاللهُ بَيْنِي وَبَيْنَكَ", "en": "the jarr-governor repeated", "tr": "hâfızın tekrarı", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "ضَرَبَ زَيْدٌ عَمْرًا وَبَكْرٌ خَالِدًا", "en": "two joined to one governor's two governed words", "tr": "tek âmilin iki ma'mûlüne iki ma'tûf", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "فِي الدَّارِ زَيْدٌ وَالْحُجْرَةِ عَمْرٌو", "en": "the fronted jarr-governor's exception", "tr": "öne alınmış cârrın istisnâsı", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "ضَرَبْتُ وَزَيْدٌ", "right": "ضَرَبْتُ أَنَا وَزَيْدٌ", "why": {"en": "joining to the attached rafʿ pronoun needs a detached pronoun first, unless something separates", "tr": "muttasıl merfû zamire atıf önce munfasıl zamir ister; fasıl yoksa"}},
  {"wrong": "مَرَرْتُ بِكَ وَزَيْدٍ", "right": "مَرَرْتُ بِكَ وَبِزَيْدٍ", "why": {"en": "joining to the jarr pronoun repeats the jarr-governor", "tr": "mecrûr zamire atıf hâfızı tekrarlar"}},
  {"wrong": "ضَرَبَ زَيْدٌ عَمْرًا وَبَكْرٌ خَالِدٌ", "right": "ضَرَبَ زَيْدٌ عَمْرًا وَبَكْرٌ خَالِدًا", "why": {"en": "each joined word takes the case of the governed word it is joined to", "tr": "her ma'tûf, atfedildiği ma'mûlün hâlini alır"}},
 ],
}
ADD_EN = (" Chapter 49 (print pp. 144-145): the ʿaṭf by the ten particles (s1), joining to the attached rafʿ pronoun with a detached confirmation or after a separation (s2), joining to the jarr pronoun with the jarr-governor repeated (s3), the joined word's rule and two joined to one governor's governed words (s4), not to two governors' save the fronted jarr (s5).")
ADD_TR = (" Kırk dokuzuncu bab (baskı s. 144-145): on harfle atıf (s1), munfasıl te'kîdle veya fasıldan sonra muttasıl merfû zamire atıf (s2), hâfız tekrarıyla mecrûr zamire atıf (s3), ma'tûfun hükmü ve tek âmilin ma'mûllerine iki ma'tûf (s4), iki âmilinkilere değil, öne alınmış câr hariç (s5).")
write_out(49, S, TITLE, ADD_EN, ADD_TR, "pp. 144-145", GLOSS_ADD, notes=(NOTE,),
          related=((K48, [K]), (AT, [K]), (AW, [K]), (TW, [K]), (TK, [K]), (FW, [K])))
report(49, S, GLOSS_ADD, (NOTE,))
