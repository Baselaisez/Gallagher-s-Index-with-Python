# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 54: the THIRD locus (vowels with dropping) is only complete, in two kinds since what is dropped is a vowel or a
# letter: the sound muḍāriʿ with no pronoun at its end (يَضْرِبُ، لَنْ يَضْرِبَ، لَمْ يَضْرِبْ) and the same muḍāriʿ ending in a weak letter (يَغْزُو، لَنْ يَغْزُوَ، لَمْ يَغْزُ);
# the FOURTH (letters with dropping) is only deficient: the muḍāriʿ with a rafʿ pronoun other than the nūn at its end — rafʿ by the nūn, naṣb and jazm by
# dropping it (يَضْرِبَانِ، لَنْ يَضْرِبَا، لَمْ يَضْرِبَا) — nine in all. The munṣarif: what jarr and tanwīn enter (زَيْدٍ); the ghayr munṣarif: a noun declined by vowels that
# jarr and tanwīn do not enter, of two sorts — samāʿī: أُحَادَ وَمَوْحَدَ … وَأُخَرَ as adjectives, جُمَعَ وَكُتَعَ وَبُصَعَ وَبُتَعَ as plurals, عُمَرَ وَزُفَرَ وَزُحَلَ وَقُزَحَ as names.
# Print pp. 149–150. The print writes رَفْعُهُ بِالضَّمِّ for the first kind and بِالضَّمَّةِ for the second — kept as printed. The Ottoman commentary
# (izhar-full-corrected l. 1649 ff.) is followed for the readings of the samāʿī list.
#   python3 author_izhar_ch54.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F8 = "form-viii-verbs"; MMS = "mamnu-min-sarf"; LJ = "lam-jazim"; NQV = "naqis-verbs"; TQ = "taqsim"; MST = "al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"; AJ = "ajma"
K = "al-murab-bil-hadhf-wal-munsarif-wa-ghayruh-al-samai"
K53 = "naqis-al-irab-bil-harakat-wal-murab-bil-huruf"
TITLE = {"ar": "الْمُعْرَبُ بِالْحَذْفِ: الثَّالِثُ وَالرَّابِعُ، وَالتِّسْعَةُ، وَتَعْرِيفُ الْمُنْصَرِفِ وَغَيْرِهِ، وَالسَّمَاعِيُّ مِنْهُ", "en": "The iʿrāb with dropping: the third and fourth loci, the nine; the munṣarif and the ghayr munṣarif defined, and the samāʿī kind", "tr": "Hazf ile i'râb: üçüncü ve dördüncü mahal, dokuz; munsarif ve gayr-ı munsarifin tarifi ve semâî olanı"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def lan(): return tok("وَلَنْ", "lan", "part", [K, AT, JZ], "الْوَاوُ عَاطِفَةٌ، وَلَنْ حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", "«and … will not»", "«ve … -meyecek»", segments=wa("لَنْ", "lan", "part"))
def wlam(): return tok("وَلَمْ", "lam", "part", [K, AT, LJ, JZ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … did not»", "«ve … -medi»", segments=wa("لَمْ", "lam", "part"))
def la_yakunu(): return [tok("لَا", "la", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-maz»"), tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR, LN], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«is»", "«olur»"), tok("إِلَّا", "illa", "part", [K, MST], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ — الْقَصْرُ.", "«except» — restriction.", "«ancak» — kasr.")]
def rafuhu(form="فَرَفْعُهُ", f=True): return tok(form, "raf", "noun", [K, AT, MK, ID, MSD, IRB], ("الْفَاءُ لِلتَّفْرِيعِ" if f else "الْوَاوُ عَاطِفَةٌ") + "، وَرَفْعُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«so its rafʿ»" if f else "«and its rafʿ»", "«ref'i»", segments=[seg("فَ" if f else "وَ", "fa" if f else "wa", "conj"), seg("رَفْعُ", "raf", "noun"), pr3ms()])
def wanasbuhu(): return tok("وَنَصْبُهُ", "nasb", "noun", [K, AT, MK, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَنَصْبُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its naṣb»", "«nasbı»", segments=[seg("وَ", "wa", "conj"), seg("نَصْبُ", "nasb", "noun"), pr3ms()])
def wajazmuhu(): return tok("وَجَزْمُهُ", "jazm", "noun", [K, AT, MK, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَجَزْمُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its jazm»", "«cezmi»", segments=[seg("وَ", "wa", "conj"), seg("جَزْمُ", "jazm", "noun"), pr3ms()])
def bi_(form, lex, en, tr, punct=None, extra=()): return tok(form, lex, "noun", [K, HJ, MK, IRB] + list(extra), "الْبَاءُ حَرْفُ جَرٍّ، وَ" + form[2:] + " مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", en, tr, punct=punct, segments=[seg("بِ", "bi", "prep"), seg(form[2:], lex, "noun")])
def bihadhfi(): return tok("بِحَذْفِ", "hadhf", "noun", [K, HJ, MK, ID, MSD, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَحَذْفِ مَجْرُورٌ، مُضَافٌ — خَبَرٌ.", "«by dropping»", "«hazfi ile»", segments=[seg("بِ", "bi", "prep"), seg("حَذْفِ", "hadhf", "noun")])
def sam(form, lex, en, tr, first=False, punct=None):
    return tok(form, lex, "noun", [K, AT, MMS, HT] + ([] if first else []), ("خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — لَفْظٌ مَحْكِيٌّ، غَيْرُ مُنْصَرِفٍ." if first else "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " مَعْطُوفٌ — لَفْظٌ مَحْكِيٌّ، غَيْرُ مُنْصَرِفٍ."), en, tr, punct=punct, segments=None if first else wa(form[2:], lex, "noun"))

# ----------- s1 — the third locus: only complete; two kinds
S.append({"id": "s1", "translation": {"en": "And the third is only complete in iʿrāb, and it is two kinds, because what is dropped is either a vowel or a letter.", "tr": "Üçüncüsü ancak i'râbı tam olur; iki kısımdır, çünkü hazfedilen ya harekedir ya harf."},
 "tokens": [
  tok("وَالثَّالِثُ", "thalith", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ — الْمُعْرَبُ بِالْحَرَكَاتِ مَعَ الْحَذْفِ.", "«and the third» — declined by vowels with dropping.", "«üçüncüsü» — hazf ile harekelerle mu'reb.", segments=wa("الثَّالِثُ", "thalith", "noun")),
  *la_yakunu(),
  tok("تَامَّ", "tamm", "noun", [K, KN, ID, MST, "doubled-verbs"], "خَبَرُ يَكُونُ مَنْصُوبٌ، مُضَافٌ.", "«complete in» — yakūnu's khabar.", "«tam» — yekûnü'nün haberi."),
  tok("الْإِعْرَابِ", "irab", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb»", "«i'râbı»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("قِسْمَانِ", "qism", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds»", "«iki kısımdır»"),
  tok("لِأَنَّ", "anna", "part", [K, HJ, IN], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because»", "«çünkü»", segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part")]),
  tok("الْمَحْذُوفَ", "mahdhuf", "noun", [K, IN, IMF, IRB], "اسْمُ أَنَّ مَنْصُوبٌ.", "«what is dropped» — anna's ism.", "«hazfedilen» — enne'nin ismi."),
  tok("إِمَّا", "imma", "part", [K, AT, TQ], "حَرْفُ تَفْصِيلٍ.", "«either»", "«ya»"),
  tok("حَرَكَةٌ", "haraka", "noun", [K, IN, IRB], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«a vowel» — anna's khabar.", "«hareke» — enne'nin haberi."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya»"),
  tok("حَرْفٌ", "harf", "noun", [K, AT, IRB], "مَعْطُوفٌ مَرْفُوعٌ.", "«a letter»", "«harf»", punct="،"),
 ]})
# ----------- s2 — the first: the sound muḍāriʿ without a pronoun
S.append({"id": "s2", "translation": {"en": "So the first is the muḍāriʿ verb to whose end no pronoun is attached, and it is sound: its rafʿ is by the ḍamm, its naṣb by the fatḥa and its jazm by dropping the vowel — as in «he strikes», «he will not strike», «he did not strike»;", "tr": "Birincisi, sonuna zamir bitişmemiş ve sahih olan muzâri fiildir: ref'i damme, nasbı fetha, cezmi harekenin hazfi iledir — «döver», «dövmeyecek», «dövmedi» gibi;"},
 "tokens": [
  tok("فَالْأَوَّلُ", "awwal", "noun", [K, AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the first»", "«birincisi»", segments=fa("الْأَوَّلُ", "awwal", "noun")),
  tok("الْفِعْلُ", "fil", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the verb»", "«fiil»"),
  tok("الْمُضَارِعُ", "mudari", "noun", [K, NA, IFA, MR], "نَعْتٌ مَرْفُوعٌ.", "«muḍāriʿ»", "«muzâri»"),
  tok("الَّذِي", "alladhi", "pron", [K, NA, MAW], "اسْمٌ مَوْصُولٌ نَعْتٌ ثَانٍ فِي مَحَلِّ رَفْعٍ.", "«which»", "«ki»"),
  tok("لَمْ", "lam", "part", [K, LJ, JZ, MAW], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — وَالْجُمْلَةُ صِلَةٌ.", "«not» — the clause is the ṣila.", "«-memiş» — cümle sıla."),
  tok("يَتَّصِلْ", "ittasala", "verb", [K, LJ, JZ, F8, MAW], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ بِالسُّكُونِ.", "«is attached» — jazm by lam.", "«bitişmemiş» — lem ile meczûm."),
  tok("بِآخِرِهِ", "akhir", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَآخِرِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«to its end» — the returning pronoun.", "«sonuna» — âid zamir.", segments=[seg("بِ", "bi", "prep"), seg("آخِرِ", "akhir", "noun"), pr3msi()]),
  tok("ضَمِيرٌ", "damir", "noun", [K, FL, BM], "فَاعِلُ يَتَّصِلْ مَرْفُوعٌ.", "«a pronoun» — the doer.", "«bir zamir» — fâil."),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK, "hal"], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is» — the wāw of ḥāl.", "«o da» — hâl vâvı.", segments=wa("هُوَ", "huwa", "pron")),
  tok("صَحِيحٌ", "sahih", "noun", [K, MK, "hal"], "خَبَرٌ مَرْفُوعٌ — صَحِيحُ الْآخِرِ، لَا حَرْفَ عِلَّةٍ فِيهِ.", "«sound» — its last letter is not weak.", "«sahih» — sonu illet harfi değil.", punct="،"),
  rafuhu(),
  bi_("بِالضَّمِّ", "damm", "«by the ḍamm» — as printed.", "«damme ile» — baskıdaki gibi."),
  wanasbuhu(),
  bi_("بِالْفَتْحَةِ", "fatha", "«by the fatḥa»", "«fetha ile»"),
  wajazmuhu(),
  bihadhfi(),
  tok("الْحَرَكَةِ", "haraka", "noun", [K, ID, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the vowel»", "«harekenin»", punct="،"),
  nahw(),
  tok("يَضْرِبُ", "daraba", "verb", [K, MR, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«he strikes» — rafʿ by ḍamma.", "«döver» — damme ile merfû."),
  lan(),
  tok("يَضْرِبَ", "daraba", "verb", [K, JZ, IRB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ بِالْفَتْحَةِ.", "«strike» — naṣb by fatḥa.", "«dövmeyecek» — fetha ile mansûb."),
  wlam(),
  tok("يَضْرِبْ", "daraba", "verb", [K, LJ, JZ, IRB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ بِحَذْفِ الْحَرَكَةِ.", "«strike» — jazm by dropping the vowel.", "«dövmedi» — hareke hazfi ile meczûm.", punct="،"),
 ]})
# ----------- s3 — the second: the muḍāriʿ ending in a weak letter
S.append({"id": "s3", "translation": {"en": "and the second is the mentioned muḍāriʿ if its last letter is a weak letter: its rafʿ is by the ḍamma, its naṣb by the fatḥa and its jazm by dropping the last letter — as in «he raids», «he will not raid», «he did not raid».", "tr": "ikincisi, sonu illet harfi olan sözü geçen muzâridir: ref'i damme, nasbı fetha, cezmi sonun hazfi iledir — «gazâ eder», «gazâ etmeyecek», «gazâ etmedi» gibi."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second»", "«ikincisi»", segments=wa("الثَّانِي", "thani", "noun")),
  tok("الْمُضَارِعُ", "mudari", "noun", [K, MK, IFA, MR], "خَبَرٌ مَرْفُوعٌ.", "«the muḍāriʿ»", "«muzâri»"),
  tok("الْمَذْكُورُ", "madhkur", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ — الَّذِي لَمْ يَتَّصِلْ بِآخِرِهِ ضَمِيرٌ.", "«mentioned» — the one without a pronoun at its end.", "«sözü geçen» — sonuna zamir bitişmemiş olan."),
  tok("إِنْ", "in-shartiyya", "part", [K, INS, JZ], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ.", "«is»", "«olursa»"),
  tok("آخِرُهُ", "akhir", "noun", [K, KN, ID], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its last letter»", "«sonu»", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  tok("حَرْفَ", "harf", "noun", [K, KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«a letter of»", "«harfi»"),
  tok("عِلَّةٍ", "illa-cause", "noun", [K, ID, NQV], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْوَاوُ أَوِ الْأَلِفُ أَوِ الْيَاءُ.", "«weakness» — wāw, alif or yāʾ.", "«illet» — vâv, elif ya da yâ.", punct="،"),
  rafuhu(),
  bi_("بِالضَّمَّةِ", "damma", "«by the ḍamma»", "«damme ile»"),
  wanasbuhu(),
  bi_("بِالْفَتْحَةِ", "fatha", "«by the fatḥa»", "«fetha ile»"),
  wajazmuhu(),
  bihadhfi(),
  tok("الْآخِرِ", "akhir", "noun", [K, ID, IRB, NQV], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — حَرْفِ الْعِلَّةِ.", "«the last letter»", "«sonun»", punct="،"),
  nahw(),
  tok("يَغْزُو", "ghaza", "verb", [K, MR, NQV, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ.", "«he raids» — rafʿ by an implied ḍamma.", "«gazâ eder» — takdîrî damme ile merfû."),
  lan(),
  tok("يَغْزُوَ", "ghaza", "verb", [K, JZ, NQV, IRB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ بِالْفَتْحَةِ الظَّاهِرَةِ.", "«raid» — naṣb by a visible fatḥa.", "«gazâ etmeyecek» — zâhir fetha ile mansûb."),
  wlam(),
  tok("يَغْزُ", "ghaza", "verb", [K, LJ, JZ, NQV, IRB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ بِحَذْفِ الْآخِرِ.", "«raid» — jazm by dropping the last letter.", "«gazâ etmedi» — sonun hazfi ile meczûm.", punct="."),
 ]})
# ----------- s4 — the fourth locus: only deficient; the nine
S.append({"id": "s4", "translation": {"en": "And the fourth is only deficient in iʿrāb, and it is the muḍāriʿ verb to whose end a rafʿ pronoun other than the nūn is attached: its rafʿ is by the nūn, and its naṣb and its jazm by dropping it — as in «the two strike», «the two will not strike», «the two did not strike»; so the total is nine.", "tr": "Dördüncüsü ancak i'râbı nâkıs olur; o, sonuna nûn dışında bir merfû zamir bitişmiş muzâri fiildir: ref'i nûn ile, nasbı ve cezmi onun hazfi iledir — «ikisi döver», «ikisi dövmeyecek», «ikisi dövmedi» gibi; böylece toplam dokuzdur."},
 "tokens": [
  tok("وَالرَّابِعُ", "rabi-fourth", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالرَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ — الْمُعْرَبُ بِالْحُرُوفِ مَعَ الْحَذْفِ.", "«and the fourth» — declined by letters with dropping.", "«dördüncüsü» — hazf ile harflerle mu'reb.", segments=wa("الرَّابِعُ", "rabi-fourth", "noun")),
  *la_yakunu(),
  tok("نَاقِصَ", "naqis", "noun", [K, KN, ID, MST, IFA], "خَبَرُ يَكُونُ مَنْصُوبٌ، مُضَافٌ.", "«deficient in»", "«nâkıs»"),
  tok("الْإِعْرَابِ", "irab", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb»", "«i'râbı»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْفِعْلُ", "fil", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the verb»", "«fiil»"),
  tok("الْمُضَارِعُ", "mudari", "noun", [K, NA, IFA, MR], "نَعْتٌ مَرْفُوعٌ.", "«muḍāriʿ»", "«muzâri»"),
  tok("الَّذِي", "alladhi", "pron", [K, NA, MAW], "اسْمٌ مَوْصُولٌ نَعْتٌ ثَانٍ فِي مَحَلِّ رَفْعٍ.", "«which»", "«ki»"),
  tok("اتَّصَلَ", "ittasala", "verb", [K, MAW, F8], "فِعْلٌ مَاضٍ — صِلَةُ الَّذِي.", "«is attached» — the ṣila.", "«bitişmiş» — sıla."),
  tok("بِآخِرِهِ", "akhir", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَآخِرِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«to its end»", "«sonuna»", segments=[seg("بِ", "bi", "prep"), seg("آخِرِ", "akhir", "noun"), pr3msi()]),
  tok("ضَمِيرٌ", "damir", "noun", [K, FL, BM], "فَاعِلُ اتَّصَلَ مَرْفُوعٌ.", "«a pronoun»", "«bir zamir»"),
  tok("مَرْفُوعٌ", "marfu", "noun", [K, NA, IMF, BM], "نَعْتٌ مَرْفُوعٌ — أَلِفُ الِاثْنَيْنِ، وَاوُ الْجَمْعِ، يَاءُ الْمُخَاطَبَةِ.", "«in rafʿ» — the dual alif, the plural wāw, the feminine yāʾ.", "«merfû» — tesniye elifi, cemi vâvı, muhâtaba yâsı."),
  tok("غَيْرُ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ ثَانٍ مَرْفُوعٌ، مُضَافٌ.", "«other than»", "«dışında»"),
  tok("النُّونِ", "nun-letter", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نُونِ جَمَاعَةِ الْمُؤَنَّثِ، فَإِنَّهُ مَبْنِيٌّ مَعَهَا.", "«the nūn» — the feminine-plural nūn, with which the verb is indeclinable.", "«nûn» — nisve nûnu; onunla fiil mebnîdir.", punct="،"),
  rafuhu(),
  bi_("بِالنُّونِ", "nun-letter", "«by the nūn»", "«nûn ile»"),
  wanasbuhu(),
  wajazmuhu(),
  tok("بِحَذْفِهِ", "hadhf", "noun", [K, HJ, MK, ID, MSD, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَحَذْفِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ عَنِ النَّصْبِ وَالْجَزْمِ.", "«by dropping it» — the khabar of both.", "«onun hazfi ile» — ikisinin haberi.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("حَذْفِ", "hadhf", "noun"), pr3msi()]),
  nahw(),
  tok("يَضْرِبَانِ", "daraba", "verb", [K, MR, MTH, FL, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«the two strike»", "«ikisi döver»", segments=[seg("يَضْرِبَ", "daraba", "verb"), seg("ا", "pron-3d", "pron"), seg("نِ", "nun-letter", "part")]),
  lan(),
  tok("يَضْرِبَا", "daraba", "verb", [K, JZ, MTH, FL, IRB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ بِحَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«the two strike» — naṣb by dropping the nūn.", "«ikisi dövmeyecek» — nûn hazfi ile mansûb.", segments=[seg("يَضْرِبَ", "daraba", "verb"), seg("ا", "pron-3d", "pron")]),
  wlam(),
  tok("يَضْرِبَا", "daraba", "verb", [K, LJ, JZ, MTH, FL, IRB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ بِحَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«the two strike» — jazm by dropping the nūn.", "«ikisi dövmedi» — nûn hazfi ile meczûm.", punct="،", segments=[seg("يَضْرِبَ", "daraba", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("فَالْمَجْمُوعُ", "majmu", "noun", [K, AT, MK, IMF], "الْفَاءُ لِلتَّفْرِيعِ، وَالْمَجْمُوعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the total»", "«böylece toplam»", segments=fa("الْمَجْمُوعُ", "majmu", "noun")),
  tok("تِسْعَةٌ", "tisa", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ — ثَلَاثَةٌ بِالْحَرَكَاتِ الْمَحْضَةِ، ثَلَاثَةٌ بِالْحُرُوفِ، اثْنَانِ بِالْحَرَكَاتِ مَعَ الْحَذْفِ، وَاحِدٌ بِالْحُرُوفِ مَعَ الْحَذْفِ.", "«nine» — 3 + 3 + 2 + 1.", "«dokuzdur» — 3 + 3 + 2 + 1.", punct="."),
 ]})
# ----------- s5 — the munṣarif and the ghayr munṣarif defined
S.append({"id": "s5", "translation": {"en": "And what is meant by the munṣarif is that which jarr and tanwīn enter, as in «Zayd-in»; and by the ghayr munṣarif, a noun declined by vowel that jarr and tanwīn do not enter; and it is of two sorts:", "tr": "Munsariften kasıt, cer ve tenvinin girdiğidir — «Zeydin» gibi; gayr-ı munsariften kasıt, hareke ile mu'reb olup cer ve tenvinin girmediği isimdir; o da iki türlüdür:"},
 "tokens": [
  tok("وَالْمُرَادُ", "murad", "noun", [K, AT, MK, IMF, F4], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمُرَادُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and what is meant»", "«kasıt»", segments=wa("الْمُرَادُ", "murad", "noun")),
  tok("بِالْمُنْصَرِفِ", "munsarif", "noun", [K, HJ, IFA, MMS], "الْبَاءُ حَرْفُ جَرٍّ، وَالْمُنْصَرِفِ مَجْرُورٌ — مُتَعَلِّقٌ بِالْمُرَادِ.", "«by the munṣarif»", "«munsariften»", segments=[seg("بِ", "bi", "prep"), seg("الْمُنْصَرِفِ", "munsarif", "noun")]),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«that which» — the khabar.", "«-dığı şey» — haber."),
  tok("دَخَلَهُ", "dakhala", "verb", [K, MAW, FL, MB], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةُ مَا.", "«enters» — the ṣila.", "«girer» — sıla.", segments=[seg("دَخَلَ", "dakhala", "verb"), pr3ms()]),
  tok("الْجَرُّ", "jarr", "noun", [K, FL, MSD, MMS], "فَاعِلٌ مَرْفُوعٌ — الْكَسْرَةُ.", "«jarr» — the kasra.", "«cer» — kesre."),
  tok("وَالتَّنْوِينُ", "tanwin", "noun", [K, AT, FL, MSD, F2, MMS], "الْوَاوُ عَاطِفَةٌ، وَالتَّنْوِينُ مَعْطُوفٌ مَرْفُوعٌ.", "«and tanwīn»", "«ve tenvin»", segments=wa("التَّنْوِينُ", "tanwin", "noun")),
  nahw(punct=None),
  tok("زَيْدٍ", "zayd", "propn", [K, ID, MMS, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ مَعَ التَّنْوِينِ — لَفْظٌ مَحْكِيٌّ.", "«Zayd-in» — kasra and tanwīn together.", "«Zeydin» — kesre ve tenvin birlikte.", punct="،"),
  tok("وَبِغَيْرِ", "ghayr", "noun", [K, AT, HJ, ID, MMS], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ — مَعْطُوفٌ عَلَى بِالْمُنْصَرِفِ.", "«and by the non-»", "«gayr-ı … -ten»", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  tok("الْمُنْصَرِفِ", "munsarif", "noun", [K, ID, IFA, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«munṣarif»", "«munsarif»"),
  tok("اسْمٌ", "ism", "noun", [K, MK, HT], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: الْمُرَادُ بِهِ اسْمٌ.", "«a noun»", "«isimdir»"),
  tok("مُعْرَبٌ", "murab", "noun", [K, NA, IMF, F4, IRB], "نَعْتٌ مَرْفُوعٌ.", "«declined»", "«mu'reb»"),
  tok("بِالْحَرَكَةِ", "haraka", "noun", [K, HJ, IRB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَرَكَةِ مَجْرُورٌ — فَخَرَجَ الْمُعْرَبُ بِالْحُرُوفِ وَالْمَبْنِيُّ.", "«by vowel» — excluding letter-iʿrāb and the indeclinable.", "«hareke ile» — harfle mu'reb ve mebnî dışarıda.", segments=[seg("بِ", "bi", "prep"), seg("الْحَرَكَةِ", "haraka", "noun")]),
  tok("لَا", "la", "part", [K, LN, NA], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ.", "«not» — the clause is a second description.", "«-mez» — cümle ikinci sıfat."),
  tok("يَدْخُلُهُ", "dakhala", "verb", [K, MR, LN, MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«enter it»", "«ona girmez»", segments=[seg("يَدْخُلُ", "dakhala", "verb"), pr3ms()]),
  tok("الْجَرُّ", "jarr", "noun", [K, FL, MSD, MMS], "فَاعِلٌ مَرْفُوعٌ.", "«jarr»", "«cer»"),
  tok("وَالتَّنْوِينُ", "tanwin", "noun", [K, AT, FL, MSD, MMS], "الْوَاوُ عَاطِفَةٌ، وَالتَّنْوِينُ مَعْطُوفٌ مَرْفُوعٌ.", "«and tanwīn»", "«ve tenvin»", punct="،", segments=wa("التَّنْوِينُ", "tanwin", "noun")),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«o da»", segments=wa("هُوَ", "huwa", "pron")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of»", "«üzere»"),
  tok("نَوْعَيْنِ", "naw", "noun", [K, HJ, MTH], "مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«two sorts»", "«iki tür»", punct=":"),
 ]})
# ----------- s6 — the samāʿī sort
S.append({"id": "s6", "translation": {"en": "samāʿī — as in uḥāda, mawḥada, thunāʾa, mathnā, thulātha, mathlatha, rubāʿa, marbaʿa and ukhara as adjectives; jumaʿa, kutaʿa, buṣaʿa and butaʿa as plurals; and ʿUmara, Zufara, Zuḥala and Quzaḥa as proper names;", "tr": "semâî — sıfat olarak uhâde, mevhade, sünâe, mesnâ, sülâse, meslese, rubâa, merbaa ve uhare; cemi olarak cümea, kütea, busaa ve bütea; alem olarak Umere, Züfere, Zühale ve Kuzaha gibi;"},
 "tokens": [
  tok("سَمَاعِيٌّ", "samai", "noun", [K, MK, HT, NSB, MMS], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا سَمَاعِيٌّ — مَا سُمِعَ مِنَ الْعَرَبِ وَلَا يُقَاسُ عَلَيْهِ.", "«samāʿī» — heard from the Arabs, not extended by analogy.", "«semâî» — Araplardan işitilen, kıyas edilmeyen."),
  nahw(punct=None),
  sam("أُحَادَ", "uhad", "«uḥāda» — «one by one»", "«uhâde» — «birer»", first=True),
  sam("وَمَوْحَدَ", "mawhad", "«and mawḥada» — «one by one»", "«ve mevhade» — «birer»"),
  sam("وَثُنَاءَ", "thuna", "«and thunāʾa» — «two by two»", "«ve sünâe» — «ikişer»"),
  sam("وَمَثْنَى", "mathna", "«and mathnā» — «two by two»", "«ve mesnâ» — «ikişer»"),
  sam("وَثُلَاثَ", "thulath", "«and thulātha» — «three by three»", "«ve sülâse» — «üçer»"),
  sam("وَمَثْلَثَ", "mathlath", "«and mathlatha» — «three by three»", "«ve meslese» — «üçer»"),
  sam("وَرُبَاعَ", "ruba", "«and rubāʿa» — «four by four»", "«ve rubâa» — «dörder»"),
  sam("وَمَرْبَعَ", "marba", "«and marbaʿa» — «four by four»", "«ve merbaa» — «dörder»"),
  sam("وَأُخَرَ", "ukhar", "«and ukhara» — «others» (fem. pl.)", "«ve uhare» — «diğerleri»"),
  tok("صِفَاتٍ", "sifa", "noun", [K, "hal", "jam-muannath-salim"], "حَالٌ مِنَ الْمَعْدُودَاتِ مَنْصُوبٌ بِالْكَسْرَةِ — حَالَ كَوْنِهَا صِفَاتٍ.", "«as adjectives» — a ḥāl: being adjectives.", "«sıfat olarak» — hâl.", punct="،"),
  sam("وَجُمَعَ", "juma-all", "«and jumaʿa» — «all» (fem. pl.)", "«ve cümea» — «hepsi»"),
  sam("وَكُتَعَ", "kuta", "«and kutaʿa»", "«ve kütea»"),
  sam("وَبُصَعَ", "busa", "«and buṣaʿa»", "«ve busaa»"),
  sam("وَبُتَعَ", "buta", "«and butaʿa»", "«ve bütea»"),
  tok("جُمُوعًا", "jumu", "noun", [K, "hal", JT], "حَالٌ مَنْصُوبٌ — حَالَ كَوْنِهَا جُمُوعًا لِجَمْعَاءَ وَكَتْعَاءَ وَبَصْعَاءَ وَبَتْعَاءَ.", "«as plurals» — of jamʿāʾ, katʿāʾ, baṣʿāʾ, batʿāʾ.", "«cemi olarak» — cem'â, ket'â, bas'â, bet'â'nın cemileri.", punct="،"),
  sam("وَعُمَرَ", "umar", "«and ʿUmara»", "«ve Umere»"),
  sam("وَزُفَرَ", "zufar", "«and Zufara»", "«ve Züfere»"),
  sam("وَزُحَلَ", "zuhal", "«and Zuḥala» — Saturn", "«ve Zühale» — Satürn"),
  sam("وَقُزَحَ", "quzah", "«and Quzaḥa» — of qaws quzaḥ, the rainbow", "«ve Kuzaha» — kavs-i kuzah'taki"),
  tok("أَعْلَامًا", "alam-name", "noun", [K, "hal", JT], "حَالٌ مَنْصُوبٌ — حَالَ كَوْنِهَا أَعْلَامًا؛ كُلُّهَا عَلَى فُعَلَ مَعْدُولَةً.", "«as proper names» — all on the pattern fuʿal, by deflection.", "«alem olarak» — hepsi fual vezninde, ma'dûl.", punct="؛"),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "illa-cause": G("illa-cause", "عِلَّة", "ع ل ل", "noun", "weakness, defect; ḥarf al-ʿilla = a weak letter (wāw, alif, yāʾ)", "illet; harf-i illet = illet harfi (vâv, elif, yâ)", 3, plural="عِلَل"),
 "uhad": G("uhad", "أُحَادَ", "أ ح د", "noun", "uḥāda — «one by one», a deflected numeral (diptote)", "uhâde — «birer», ma'dûl sayı (gayr-ı munsarif)", 5),
 "mawhad": G("mawhad", "مَوْحَدَ", "و ح د", "noun", "mawḥada — «one by one», a deflected numeral (diptote)", "mevhade — «birer», ma'dûl sayı (gayr-ı munsarif)", 5),
 "thuna": G("thuna", "ثُنَاءَ", "ث ن ي", "noun", "thunāʾa — «two by two», a deflected numeral (diptote)", "sünâe — «ikişer», ma'dûl sayı (gayr-ı munsarif)", 5),
 "mathna": G("mathna", "مَثْنَى", "ث ن ي", "noun", "mathnā — «two by two», a deflected numeral (diptote)", "mesnâ — «ikişer», ma'dûl sayı (gayr-ı munsarif)", 5),
 "thulath": G("thulath", "ثُلَاثَ", "ث ل ث", "noun", "thulātha — «three by three», a deflected numeral (diptote)", "sülâse — «üçer», ma'dûl sayı (gayr-ı munsarif)", 5),
 "mathlath": G("mathlath", "مَثْلَثَ", "ث ل ث", "noun", "mathlatha — «three by three», a deflected numeral (diptote)", "meslese — «üçer», ma'dûl sayı (gayr-ı munsarif)", 5),
 "ruba": G("ruba", "رُبَاعَ", "ر ب ع", "noun", "rubāʿa — «four by four», a deflected numeral (diptote)", "rubâa — «dörder», ma'dûl sayı (gayr-ı munsarif)", 5),
 "marba": G("marba", "مَرْبَعَ", "ر ب ع", "noun", "marbaʿa — «four by four», a deflected numeral (diptote)", "merbaa — «dörder», ma'dûl sayı (gayr-ı munsarif)", 5),
 "ukhar": G("ukhar", "أُخَرَ", "أ خ ر", "noun", "ukhara — «others», feminine plural of ukhrā, deflected (diptote)", "uhare — «diğerleri», uhrâ'nın çoğulu, ma'dûl (gayr-ı munsarif)", 5),
 "juma-all": G("juma-all", "جُمَعَ", "ج م ع", "noun", "jumaʿa — «all», plural of jamʿāʾ, a tawkīd word (diptote)", "cümea — «hepsi», cem'â'nın çoğulu, te'kîd lafzı (gayr-ı munsarif)", 5),
 "kuta": G("kuta", "كُتَعَ", "ك ت ع", "noun", "kutaʿa — plural of katʿāʾ, follower of jumaʿa (diptote)", "kütea — ket'â'nın çoğulu, cümea'nın tâbii (gayr-ı munsarif)", 5),
 "busa": G("busa", "بُصَعَ", "ب ص ع", "noun", "buṣaʿa — plural of baṣʿāʾ, follower of jumaʿa (diptote)", "busaa — bas'â'nın çoğulu, cümea'nın tâbii (gayr-ı munsarif)", 5),
 "buta": G("buta", "بُتَعَ", "ب ت ع", "noun", "butaʿa — plural of batʿāʾ, follower of jumaʿa (diptote)", "bütea — bet'â'nın çoğulu, cümea'nın tâbii (gayr-ı munsarif)", 5),
 "zufar": G("zufar", "زُفَرُ", "ز ف ر", "propn", "Zufar — a man's name on the pattern fuʿal (diptote)", "Züfer — fual vezninde erkek adı (gayr-ı munsarif)", 5),
 "zuhal": G("zuhal", "زُحَلُ", "ز ح ل", "propn", "Zuḥal — Saturn (diptote)", "Zühal — Satürn (gayr-ı munsarif)", 5),
 "quzah": G("quzah", "قُزَحُ", "ق ز ح", "propn", "Quzaḥ — the name in qaws Quzaḥ, the rainbow (diptote)", "Kuzah — kavs-i Kuzah'taki ad, gökkuşağı (gayr-ı munsarif)", 5),
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
print("izhar ch54 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("ittasala", "dakhala", "daraba", "ghaza", "kana") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمُعْرَبُ بِالْحَذْفِ: الْمُضَارِعُ الصَّحِيحُ وَالْمُعْتَلُّ وَمَا اتَّصَلَ بِهِ ضَمِيرٌ، وَالتِّسْعَةُ؛ الْمُنْصَرِفُ وَغَيْرُهُ، وَالسَّمَاعِيُّ مِنْ غَيْرِ الْمُنْصَرِفِ", "en": "Iʿrāb with dropping: the sound, the weak and the pronoun-bearing muḍāriʿ, the nine; the munṣarif and the ghayr munṣarif, and the samāʿī diptotes", "tr": "Hazf ile i'râb: sahih, mu'tel ve zamirli muzâri, dokuz; munsarif ve gayr-ı munsarif, semâî gayr-ı munsarifler"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الإعراب: التقسيم بحسب المحل، غير المنصرف", "الكافية لابن الحاجب — غير المنصرف", "شرح قطر الندى لابن هشام — الممنوع من الصرف"],
 "amil": "the third locus (vowels with dropping) is only complete: the sound muḍāriʿ without a pronoun (يَضْرِبُ، لَنْ يَضْرِبَ، لَمْ يَضْرِبْ) and the weak-ending one (يَغْزُو، لَنْ يَغْزُوَ، لَمْ يَغْزُ); the fourth (letters with dropping) is only deficient: the muḍāriʿ with a rafʿ pronoun other than the nūn — rafʿ by the nūn, naṣb and jazm by dropping it (يَضْرِبَانِ، لَنْ يَضْرِبَا، لَمْ يَضْرِبَا); nine in all. The munṣarif takes jarr and tanwīn (زَيْدٍ); the ghayr munṣarif is a vowel-declined noun that takes neither — samāʿī (the deflected numerals, the plurals جُمَعَ كُتَعَ بُصَعَ بُتَعَ, the names عُمَرَ زُفَرَ زُحَلَ قُزَحَ) or qiyāsī.",
 "question": {
  "en": ["Why is the third locus only complete? Because the sound and the weak-ending muḍāriʿ each show all three states — ḍamma, fatḥa, and a dropping for jazm (of the vowel: لَمْ يَضْرِبْ; of the last letter: لَمْ يَغْزُ).",
         "What does the print say for the first kind's rafʿ? رَفْعُهُ بِالضَّمِّ — and for the second بِالضَّمَّةِ; the chapter keeps both as printed.",
         "Why is the fourth locus only deficient? Because the muḍāriʿ with the dual alif, plural wāw or feminine yāʾ shows two states only: the nūn in rafʿ, and its dropping for both naṣb and jazm (لَنْ يَضْرِبَا، لَمْ يَضْرِبَا).",
         "Why «other than the nūn»? With the feminine-plural nūn (يَضْرِبْنَ) the muḍāriʿ is indeclinable, so it is not a muʿrab at all.",
         "How do the nine add up? Three by pure vowels, three by pure letters, two by vowels with dropping, one by letters with dropping.",
         "What is the munṣarif? A noun that jarr and tanwīn enter — زَيْدٍ; the ghayr munṣarif is a vowel-declined noun that neither enters — so the letter-declined and the indeclinable are outside the definition.",
         "What is the samāʿī diptote? Forms heard from the Arabs and not extended: the deflected numerals أُحَادَ to مَرْبَعَ and أُخَرَ as adjectives, the plurals جُمَعَ كُتَعَ بُصَعَ بُتَعَ, the names عُمَرَ زُفَرَ زُحَلَ قُزَحَ — all on fuʿal or mafʿal by deflection.",
         "What does the engine READ here? The DabtEngine reads يَضْرِبُ/يَضْرِبَ/يَضْرِبْ by vowel and sukūn, يَغْزُو/يَغْزُوَ/يَغْزُ with the implied ḍamma, the visible fatḥa and the dropped wāw, يَضْرِبَانِ/يَضْرِبَا by the nūn and its dropping, زَيْدٍ as munṣarif, and the cited list as diptotes at their printed fatḥa."],
  "tr": ["Üçüncü mahal neden ancak tamdır? Çünkü sahih ve sonu illetli muzâri üç hâli de gösterir — damme, fetha ve cezm için hazf (harekenin: lem yadrib; sonun: lem yağzü).",
         "Baskı birinci kısmın ref'i için ne der? Ref'uhû bi'd-dammi — ikincisi için bi'd-dammeti; bab ikisini de basıldığı gibi korur.",
         "Dördüncü mahal neden ancak nâkıstır? Çünkü tesniye elifi, cemi vâvı ya da muhâtaba yâsı taşıyan muzâri yalnız iki hâl gösterir: ref'te nûn, nasb ve cezmde onun hazfi (len yadribâ, lem yadribâ).",
         "Neden «nûn dışında»? Nisve nûnuyla (yadribne) muzâri mebnîdir, dolayısıyla mu'reb değildir.",
         "Dokuz nasıl toplanır? Sırf hareke ile üç, sırf harf ile üç, hazf ile hareke iki, hazf ile harf bir.",
         "Munsarif nedir? Cer ve tenvinin girdiği isim — Zeydin; gayr-ı munsarif, hareke ile mu'reb olup ikisinin girmediği isimdir — harfle mu'reb ve mebnî tarifin dışındadır.",
         "Semâî gayr-ı munsarif nedir? Araplardan işitilip kıyas edilmeyen şekiller: sıfat olarak uhâde'den merbaa'ya ma'dûl sayılar ve uhare, cemi olarak cümea kütea busaa bütea, alem olarak Umere Züfere Zühale Kuzaha — hepsi udûl ile fual ya da mef'al vezninde.",
         "Motor burada neyi OKUR? DabtEngine yadribü/yadribe/yadrib'i hareke ve sükûnla, yağzû/yağzüve/yağzü'yü takdîrî damme, zâhir fetha ve düşen vâvla, yadribâni/yadribâ'yı nûn ve hazfiyle, Zeydin'i munsarif, alıntı listeyi basılı fethasıyla gayr-ı munsarif olarak okur."],
 },
 "plain": {"en": "Present-tense verbs mark case by a vowel and lose it for jazm: «yaḍribu, yaḍriba, yaḍrib»; weak-ending ones drop the last letter: «yaghzū, yaghzuwa, yaghzu». With a dual or plural pronoun they use a nūn and drop it: «yaḍribāni, yaḍribā». Nine patterns in all. A diptote never takes kasra or tanwīn.",
           "tr": "Muzâri fiiller i'râbını harekeyle gösterir, cezmde kaybeder: «yadribü, yadribe, yadrib»; sonu illetli olanlar son harfi düşürür: «yağzû, yağzüve, yağzü». Tesniye ya da cemi zamiriyle nûn kullanır ve düşürür: «yadribâni, yadribâ». Toplam dokuz kalıp. Gayr-ı munsarif hiç kesre ve tenvin almaz."},
 "explanation": {"en": "The third locus, vowels together with dropping, is only complete in iʿrāb, and it is of two kinds, since what is dropped is a vowel or a letter. The first is the muḍāriʿ verb to whose end no pronoun is attached, being sound: its rafʿ by the ḍamm (so the print), its naṣb by the fatḥa, its jazm by dropping the vowel — يَضْرِبُ، لَنْ يَضْرِبَ، لَمْ يَضْرِبْ. The second is the same muḍāriʿ when its last letter is weak: rafʿ by the ḍamma, naṣb by the fatḥa, jazm by dropping the last letter — يَغْزُو، لَنْ يَغْزُوَ، لَمْ يَغْزُ. The fourth locus, letters together with dropping, is only deficient: the muḍāriʿ to whose end a rafʿ pronoun other than the nūn is attached — rafʿ by the nūn, naṣb and jazm by dropping it: يَضْرِبَانِ، لَنْ يَضْرِبَا، لَمْ يَضْرِبَا. The total of the loci is nine. By the munṣarif is meant what jarr and tanwīn enter, as زَيْدٍ; by the ghayr munṣarif a noun declined by vowel that jarr and tanwīn do not enter. It is of two sorts. The samāʿī: أُحَادَ وَمَوْحَدَ وَثُنَاءَ وَمَثْنَى وَثُلَاثَ وَمَثْلَثَ وَرُبَاعَ وَمَرْبَعَ وَأُخَرَ as adjectives, جُمَعَ وَكُتَعَ وَبُصَعَ وَبُتَعَ as plurals, عُمَرَ وَزُفَرَ وَزُحَلَ وَقُزَحَ as proper names. The qiyāsī sort follows in the next chapter.",
                 "tr": "Üçüncü mahal, hazf ile birlikte harekeler, ancak i'râbı tam olur ve iki kısımdır; çünkü hazfedilen ya hareke ya harftir. Birincisi sonuna zamir bitişmemiş, sahih muzâri fiildir: ref'i damm ile (baskı böyle), nasbı fetha, cezmi harekenin hazfi ile — yadribü, len yadribe, lem yadrib. İkincisi sonu illetli aynı muzâridir: ref'i damme, nasbı fetha, cezmi sonun hazfi ile — yağzû, len yağzüve, lem yağzü. Dördüncü mahal, hazf ile birlikte harfler, ancak nâkıs olur: sonuna nûn dışında merfû zamir bitişen muzâri — ref'i nûn ile, nasbı ve cezmi onun hazfi ile: yadribâni, len yadribâ, lem yadribâ. Mahallerin toplamı dokuzdur. Munsariften kasıt cer ve tenvinin girdiğidir, Zeydin gibi; gayr-ı munsariften kasıt hareke ile mu'reb olup cer ve tenvinin girmediği isimdir. İki türlüdür. Semâî: sıfat olarak uhâde ve mevhade ve sünâe ve mesnâ ve sülâse ve meslese ve rubâa ve merbaa ve uhare, cemi olarak cümea ve kütea ve busaa ve bütea, alem olarak Umere ve Züfere ve Zühale ve Kuzaha. Kıyâsî tür sonraki babda gelir."},
 "examples": [
  {"ar": "يَضْرِبُ وَلَنْ يَضْرِبَ وَلَمْ يَضْرِبْ", "en": "the sound muḍāriʿ: jazm by dropping the vowel", "tr": "sahih muzâri: hareke hazfi ile cezm", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "يَغْزُو وَلَنْ يَغْزُوَ وَلَمْ يَغْزُ", "en": "the weak-ending muḍāriʿ: jazm by dropping the last letter", "tr": "sonu illetli muzâri: sonun hazfi ile cezm", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "يَضْرِبَانِ وَلَنْ يَضْرِبَا وَلَمْ يَضْرِبَا، فَالْمَجْمُوعُ تِسْعَةٌ", "en": "the nūn and its dropping; the nine", "tr": "nûn ve hazfi; dokuz", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "الْمُرَادُ بِالْمُنْصَرِفِ مَا دَخَلَهُ الْجَرُّ وَالتَّنْوِينُ", "en": "the munṣarif defined", "tr": "munsarifin tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "أُحَادَ وَمَوْحَدَ … وَعُمَرَ وَزُفَرَ وَزُحَلَ وَقُزَحَ", "en": "the samāʿī diptotes", "tr": "semâî gayr-ı munsarifler", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "لَنْ يَضْرِبَانِ", "right": "لَنْ يَضْرِبَا", "why": {"en": "after a rafʿ pronoun the naṣb, like the jazm, is by dropping the nūn", "tr": "merfû zamirden sonra nasb da cezm gibi nûnun hazfi iledir"}},
  {"wrong": "لَنْ يَغْزُ", "right": "لَنْ يَغْزُوَ", "why": {"en": "the weak-ending muḍāriʿ takes a visible fatḥa in naṣb; only jazm drops the letter", "tr": "sonu illetli muzâri nasbda zâhir fetha alır; yalnız cezm harfi düşürür"}},
  {"wrong": "لَمْ يَضْرِبْنَ (counted as a muʿrab)", "right": "يَضْرِبْنَ is indeclinable with the feminine nūn", "why": {"en": "the rule excludes the nūn: with it the muḍāriʿ is mabnī", "tr": "kural nûnu dışarıda bırakır: onunla muzâri mebnîdir"}},
  {"wrong": "مَرَرْتُ بِعُمَرٍ", "right": "مَرَرْتُ بِعُمَرَ", "why": {"en": "ʿUmar is a samāʿī diptote: no kasra, no tanwīn", "tr": "Ömer semâî gayr-ı munsariftir: kesre yok, tenvin yok"}},
 ],
}
ADD_EN = (" Chapter 54 (print pp. 149-150): the third locus only complete, two kinds (s1) — the sound muḍāriʿ (s2) and the weak-ending one (s3); the fourth only deficient, by the nūn and its dropping, nine in all (s4); the munṣarif and the ghayr munṣarif defined (s5); the samāʿī diptotes (s6).")
ADD_TR = (" Elli dördüncü bab (baskı s. 149-150): üçüncü mahal ancak tam, iki kısım (s1) — sahih muzâri (s2) ve sonu illetli olan (s3); dördüncüsü ancak nâkıs, nûn ve hazfi ile, toplam dokuz (s4); munsarif ve gayr-ı munsarifin tarifi (s5); semâî gayr-ı munsarifler (s6).")
write_out(54, S, TITLE, ADD_EN, ADD_TR, "pp. 149-150", GLOSS_ADD, notes=(NOTE,),
          related=((K53, [K]), (MMS, [K]), (NQV, [K]), (LJ, [K]), (JZ, [K]), (IRB, [K])))
report(54, S, GLOSS_ADD, (NOTE,))
