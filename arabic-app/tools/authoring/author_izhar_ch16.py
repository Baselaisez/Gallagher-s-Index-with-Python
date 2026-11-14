# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 16: the ninth QIYĀSĪ governor — the SENSE OF THE VERB (مَعْنَى الْفِعْلِ): every utterance from which
# a verb's sense is understood. Of it: the NOUN-VERBS (asmāʾ al-afʿāl — with the sense of a command or of a past verb; they govern as
# their named verb does, their governed word never precedes them): هَا زَيْدًا أَيْ خُذْهُ، رُوَيْدَ، هَلُمَّ، هَاتِ، حَيَّهَلَ الثَّرِيدَ، بَلْهَ،
# عَلَيْكَ، دُونَكَ، تَرَاكِ — and هَيْهَاتَ الْأَمْرُ أَيْ بَعُدَ، شَتَّانَ زَيْدٌ وَعَمْرٌو، سَرْعَانَ، وَشْكَانَ; the SETTLED ẒARF (never governs the object;
# the manifest doer only when it leans on what was mentioned or on the relative: زَيْدٌ فِي الدَّارِ أَبُوهُ، مَا فِي الدَّارِ أَحَدٌ، جَاءَ الَّذِي
# فِي الدَّارِ أَبُوهُ; it may be a fronted khabar; when it raises no manifest doer its doer is a concealed pronoun moved from its dropped
# mutaʿallaq; the ḥāl and the ẓarf it governs without condition); the NISBA noun (works as the ism mafʿūl: مَرَرْتُ بِرَجُلٍ هَاشِمِيٍّ أَخُوهُ);
# the BORROWED noun (مَرَرْتُ بِرَجُلٍ أَسَدٍ غُلَامُهُ، أَسَدٌ عَلَيَّ أَيْ مُجْتَرِئٌ); every noun with a ṣifa's sense (لَفْظَةُ اللهِ in
# ﴿وَهُوَ اللهُ فِي السَّمٰوَاتِ﴾ = الْمَعْبُودُ فِيهَا); and the demonstrative, لَيْتَ, لَعَلَّ, the letters of calling, likening, alerting and
# negation — governing the ḥāl and the ẓarf, never the doer or the object. Print pp. 113–115.
#   python3 author_izhar_ch16.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "mana-al-fil-wa-asma-al-afal"
K15 = "al-ism-al-mubham-al-tamm"
TITLE = {"ar": "مَعْنَى الْفِعْلِ: أَسْمَاءُ الْأَفْعَالِ وَالظَّرْفُ الْمُسْتَقَرُّ وَالْمَنْسُوبُ وَالْمُسْتَعَارُ", "en": "The sense of the verb: the noun-verbs, the settled ẓarf, the nisba and the borrowed noun", "tr": "Mana-yı fiil: isim fiiller, zarf-ı müstakar, mensûb ve müsteâr isim"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; F8 = "form-viii-verbs"; MSD = "masdar"; LN = "la-nafiya"; IN = "inna-wa-akhawatuha"; BD = "badal"; JT = "jam-taksir"; JMS = "jam-mudhakkar-salim"; JMU = "jam-muannath-salim"; ISH = "asma-al-ishara"; MQ = "ism-maqsur-manqus"; ND = "vocative-munada"; MM = "maful-mutlaq"
IFL = "ism-fil"; MNF = "mana-al-fil"; ZM = "zarf-mustaqarr-wa-laghw"; NSB = "ism-mansub"; IST = "istiara"; AMR = "imperative-amr"; MJZ = "nawasib-wa-jawazim-al-mudari"; MAW = "ism-mawsul"; JS = "jumla-sifa"; QA = "al-iqtibas-wal-tadmin"; TNB = "huruf-tanbih"; ALK = "five-nouns"; MJH = "naib-al-fail"; MD = "idafa-definiteness"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«… gibi» — hazfedilmiş mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def ay(punct=None, kasra=False): return tok("أَيِ" if kasra else "أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ" + ("، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ" if kasra else "") + ".", "«that is» — the explaining particle.", "«yani» — tefsir harfi.", punct=punct)
def ismfil_amr(form, lex, en, tr, meaning, segments=None, punct=None, pos="noun", tags=()):
    return tok(form, lex, pos, [K, IFL, MNF, FL] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if segments else "") + "لَفْظٌ مَحْكِيٌّ: اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى " + meaning + "، مَبْنِيٌّ، وَفَاعِلُهُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", en, tr, punct=punct, segments=segments)
def ismfil_madi(form, lex, en, tr, meaning, segments=None, punct=None, pos="noun", tags=()):
    return tok(form, lex, pos, [K, IFL, MNF, FL] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if segments else "") + "لَفْظٌ مَحْكِيٌّ: اسْمُ فِعْلٍ مَاضٍ بِمَعْنَى " + meaning + "، مَبْنِيٌّ عَلَى الْفَتْحِ — يَرْفَعُ فَاعِلًا.", en, tr, punct=punct, segments=segments)
def mafismfil(form, lex, en, tr, punct=None, pos="propn", tags=()): return tok(form, lex, pos, [K, IFL, MB] + list(tags), "مَفْعُولٌ بِهِ مَنْصُوبٌ لِاسْمِ الْفِعْلِ قَبْلَهُ — يَعْمَلُ عَمَلَ مُسَمَّاهُ.", en, tr, punct=punct)
def failismfil(form, lex, en, tr, punct=None, pos="propn", tags=(), ar="فَاعِلٌ مَرْفُوعٌ لِاسْمِ الْفِعْلِ قَبْلَهُ — يَعْمَلُ عَمَلَ مُسَمَّاهُ.", segments=None): return tok(form, lex, pos, [K, IFL, FL] + list(tags), ar, en, tr, punct=punct, segments=segments)
def amr_h(form, stem, lex, en, tr, punct=None, tags=(), hi=False, extra=""):
    return tok(form, lex, "verb", [K, AMR, IFL, HT] + list(tags), "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ، وَالْهَاءُ مَفْعُولٌ بِهِ — تَفْسِيرٌ لِاسْمِ الْفِعْلِ قَبْلَهُ" + extra + ".", en, tr, punct=punct, segments=[seg(stem, lex, "verb"), pr3msi() if hi else pr3ms()])
def minhu(punct=None, wa=True, fa=False):
    pre = "وَ" if wa else ("فَ" if fa else "")
    segs = ([seg("وَ", "wa", "conj")] if wa else ([seg("فَ", "fa", "conj")] if fa else [])) + [seg("مِنْ", "min", "prep"), pr3ms()]
    return tok(pre + "مِنْهُ", "min", "prep", [K, HJ, MK, AT], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ لِلتَّفْرِيعِ، وَ" if fa else "")) + "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ: مِنْ مَعْنَى الْفِعْلِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and of it» — the fronted khabar: of the sense of the verb.", "«ve ondan» — öne alınmış haber: mana-yı fiilden.", punct=punct, segments=segs)
def fi_zarf(en, tr, punct=None, tags=()): return tok("فِي", "fi", "prep", [K, HJ, ZM, MK] + list(tags), "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ ظَرْفٌ مُسْتَقَرٌّ: خَبَرٌ، مُتَعَلِّقُهُ مَحْذُوفٌ.", en, tr, punct=punct)
def aldar(punct=None): return tok("الدَّارِ", "dar", "noun", [K, HJ, ZM], "مَجْرُورٌ بِفِي.", "«the house»", "«evde»", punct=punct)
def abuhu(punct=None, ar="فَاعِلُ الظَّرْفِ الْمُسْتَقَرِّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الظَّرْفُ اعْتَمَدَ عَلَى الْمُبْتَدَإِ."):
    return tok("أَبُوهُ", "ab", "noun", [K, ZM, FL, ALK, ID], ar, "«his father» — the doer the settled ẓarf raises.", "«babası» — zarf-ı müstakarrın ref' ettiği fâil.", punct=punct, segments=[seg("أَبُو", "ab", "noun"), pr3ms()])

# ----------- s1 — the ninth: the sense of the verb
S.append({"id": "s1", "translation": {"en": "And the ninth is the SENSE OF THE VERB, and what is meant by it is every utterance from which the sense of a verb is understood.", "tr": "Dokuzuncusu MANA-YI FİİL'dir; bundan murâd, kendisinden bir fiil mânâsı anlaşılan her lafızdır."},
 "tokens": [
  tok("وَالتَّاسِعُ", "tasi", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالتَّاسِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the ninth» — the mubtada.", "«dokuzuncusu» — mübtedâ.", segments=wa("التَّاسِعُ", "tasi", "noun")),
  tok("مَعْنَى", "mana", "noun", [K, MK, ID, MQ, MNF], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ.", "«the sense of» — the khabar.", "«mânâsı» — haber."),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiil»", punct="،"),
  tok("وَالْمُرَادُ", "murad", "noun", [K, AT, MK, IMF], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمُرَادُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and what is meant» — the mubtada.", "«ve murâd olan» — mübtedâ.", segments=wa("الْمُرَادُ", "murad", "noun")),
  tok("مِنْهُ", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِالْمُرَادِ.", "«by it»", "«ondan»", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("كُلُّ", "kull", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«every» — the khabar.", "«her» — haber."),
  tok("لَفْظٍ", "lafz", "noun", [K, ID, JS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«utterance»", "«lafız»"),
  tok("يُفْهَمُ", "fahima", "verb", [K, NA, NF, MJH, JS], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَالْجُمْلَةُ نَعْتٌ لِلَفْظٍ.", "«is understood» — the ṣifa clause of «utterance».", "«anlaşılır» — lafzın sıfat cümlesi."),
  tok("مِنْهُ", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«from it» — the returning pronoun.", "«ondan» — âid zamir.", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("مَعْنَى", "mana", "noun", [K, NF, ID, MQ], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the sense of» — the deputy doer.", "«mânâsı» — nâib-i fâil."),
  tok("فِعْلٍ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb»", "«bir fiil»", punct="."),
 ]})
# ----------- s2 — of it, the noun-verbs: their definition and their two rules
S.append({"id": "s2", "translation": {"en": "Of it are the NOUN-VERBS — and that is what has the sense of a command or of a past verb; it governs as its named verb does, and its governed word does not precede it.", "tr": "Bundan İSİM FİİLLER'dir — ki o, emir veya mâzî mânâsında olandır; müsemmâsının ameli gibi amel eder ve ma'mûlü onun önüne geçmez."},
 "tokens": [
  minhu(wa=False, fa=True),
  tok("أَسْمَاءُ", "ism", "noun", [K, MK, ID, JT, IFL], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ — جَمْعُ اسْمٍ.", "«the nouns of» — the delayed mubtada.", "«isimleri» — sonraya bırakılmış mübtedâ."),
  tok("الْأَفْعَالِ", "fil", "noun", [K, ID, JT, IFL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ فِعْلٍ: أَسْمَاءُ الْأَفْعَالِ.", "«the verbs» — the noun-verbs.", "«fiiller» — isim fiiller.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the khabar.", "«… olan» — haber."),
  tok("كَانَ", "kana", "verb", [K, KN, HV, MAW], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةٌ.", "«is» — kāna, the relative clause.", "«olan» — kâne, sıla cümlesi."),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, KN, ID, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«in the sense of» — the khabar of kāna.", "«mânâsında» — kâne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("الْأَمْرِ", "amr", "noun", [K, ID, AMR], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فِعْلُ الْأَمْرِ.", "«the command»", "«emir»"),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«veya»"),
  tok("الْمَاضِي", "madi", "noun", [K, AT, MQ], "مَعْطُوفٌ عَلَى الْأَمْرِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«the past verb»", "«mâzî»", punct="،"),
  tok("وَيَعْمَلُ", "amila", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَيَعْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and it governs»", "«ve amel eder»", segments=wa("يَعْمَلُ", "amila", "verb")),
  tok("عَمَلَ", "amal-governing", "noun", [K, MM, ID], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ، مُضَافٌ — مُبَيِّنٌ لِلنَّوْعِ.", "«the governing of» — the absolute object.", "«… ameli gibi» — mef'ûl-i mutlak."),
  tok("مُسَمَّاهُ", "musamma", "noun", [K, ID, IMF, MQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْفِعْلُ الَّذِي سُمِّيَ بِهِ.", "«its named verb» — the verb it names.", "«müsemmâsı» — adını taşıdığı fiil.", punct="،", segments=[seg("مُسَمَّا", "musamma", "noun"), pr3ms()]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَتَقَدَّمُ", "taqaddama", "verb", [K, FL, F5], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«precedes»", "«öne geçer»"),
  tok("مَعْمُولُهُ", "mamul", "noun", [K, FL, ID, IMF], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governed word» — the doer.", "«ma'mûlü» — fâil.", segments=[seg("مَعْمُولُ", "mamul", "noun"), pr3ms()]),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَتَقَدَّمُ.", "«it»", "«onun önüne»", punct=".", segments=[seg("عَلَى", "ala", "prep"), pr3msi()]),
 ]})
# ----------- s3 — the first kind (command sense): هَا، رُوَيْدَ، هَلُمَّ، هَاتِ
S.append({"id": "s3", "translation": {"en": "The first is as in «hā Zayd!» — that is, take him; «ruwayda Zayd!» — that is, give him respite; «halumma Zayd!» — that is, bring him; «hāti a thing!» — that is, give it.", "tr": "İlki: «hâ Zeyd!» — yani onu al; «ruveyde Zeyd!» — yani ona mühlet ver; «helümme Zeyd!» — yani onu getir; «hâti bir şey!» — yani onu ver, gibidir."},
 "tokens": [
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK, IFL], "مُبْتَدَأٌ مَرْفُوعٌ — مَا كَانَ بِمَعْنَى الْأَمْرِ.", "«the first» — the command kind: the mubtada.", "«ilki» — emir mânâsındaki: mübtedâ."),
  tok("نَحْوُ", "nahw", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar.", "«… gibi» — haber.", punct=":"),
  ismfil_amr("هَا", "ha-ism-fil", "«hā!» — the noun-verb «take!».", "«hâ!» — «al!» isim fiili.", "خُذْ"),
  mafismfil("زَيْدًا", "zayd", "«Zayd» — its object.", "«Zeyd» — mef'ûlü."),
  ay(),
  amr_h("خُذْهُ", "خُذْ", "akhadha", "«take him» — the explaining imperative.", "«onu al» — açıklayan emir.", punct="،"),
  ismfil_amr("وَرُوَيْدَ", "ruwayd", "«and ruwayda!» — «give respite!».", "«ve ruveyde!» — «mühlet ver!».", "أَمْهِلْ", segments=wa("رُوَيْدَ", "ruwayd", "noun")),
  mafismfil("زَيْدًا", "zayd", "«Zayd» — its object.", "«Zeyd» — mef'ûlü."),
  ay(),
  amr_h("أَمْهِلْهُ", "أَمْهِلْ", "amhala", "«give him respite»", "«ona mühlet ver»", punct="،", tags=[F4]),
  ismfil_amr("وَهَلُمَّ", "halumma", "«and halumma!» — «bring!».", "«ve helümme!» — «getir!».", "أَحْضِرْ", segments=wa("هَلُمَّ", "halumma", "noun")),
  mafismfil("زَيْدًا", "zayd", "«Zayd» — its object.", "«Zeyd» — mef'ûlü."),
  ay(),
  amr_h("أَحْضِرْهُ", "أَحْضِرْ", "ahdara", "«bring him»", "«onu getir»", punct="،", tags=[F4]),
  ismfil_amr("وَهَاتِ", "hati", "«and hāti!» — «give!».", "«ve hâti!» — «ver!».", "أَعْطِ", segments=wa("هَاتِ", "hati", "noun")),
  mafismfil("شَيْئًا", "shay", "«a thing» — its object.", "«bir şey» — mef'ûlü.", pos="noun"),
  ay(),
  tok("أَعْطِهِ", "aata", "verb", [K, AMR, IFL, HT, F4, MQ], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالْهَاءُ مَفْعُولٌ بِهِ — تَفْسِيرٌ لِهَاتِ.", "«give it» — the explaining imperative, its final weak letter dropped.", "«onu ver» — illet harfi düşmüş emir.", punct=".", segments=[seg("أَعْطِ", "aata", "verb"), pr3msi()]),
 ]})
# ----------- s4 — the first kind continued: حَيَّهَلَ، بَلْهَ، عَلَيْكَ، دُونَكَ، تَرَاكِ
S.append({"id": "s4", "translation": {"en": "And «ḥayyahala the tharīd!» — that is, come to it; «balha Zayd!» — that is, leave him; «ʿalayka Zayd!» — that is, hold to him; «dūnaka ʿAmr!» — that is, take him; «tarāki Zayd!» — that is, leave him; and other than that.", "tr": "«Hayyehele's-serîd!» — yani ona gel; «belhe Zeyd!» — yani onu bırak; «aleyke Zeyd!» — yani ona sarıl; «dûneke Amr!» — yani onu al; «terâki Zeyd!» — yani onu terk et; ve bunlardan başkası."},
 "tokens": [
  ismfil_amr("وَحَيَّهَلَ", "hayyahal", "«and ḥayyahala!» — «come to!».", "«ve hayyehele!» — «gel!».", "ائْتِ", segments=wa("حَيَّهَلَ", "hayyahal", "noun")),
  mafismfil("الثَّرِيدَ", "thurayd", "«the tharīd» — the bread-and-broth dish: its object.", "«tirit» — ekmekli et suyu yemeği: mef'ûlü.", pos="noun"),
  ay(kasra=True),
  tok("ائْتِهِ", "ata", "verb", [K, AMR, IFL, HT, MQ], "فِعْلُ أَمْرٍ مِنْ أَتَى مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، هَمْزَتُهُ هَمْزَةُ وَصْلٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالْهَاءُ مَفْعُولٌ بِهِ — تَفْسِيرٌ لِحَيَّهَلَ.", "«come to it» — the imperative of «to come» with its joining hamza.", "«ona gel» — etâ'nın vasıl hemzeli emri.", punct="،", segments=[seg("ائْتِ", "ata", "verb"), pr3msi()]),
  ismfil_amr("وَبَلْهَ", "balha", "«and balha!» — «leave!».", "«ve belhe!» — «bırak!».", "دَعْ", segments=wa("بَلْهَ", "balha", "noun")),
  mafismfil("زَيْدًا", "zayd", "«Zayd» — its object.", "«Zeyd» — mef'ûlü."),
  ay(),
  amr_h("دَعْهُ", "دَعْ", "da-leave", "«leave him»", "«onu bırak»", punct="،"),
  ismfil_amr("وَعَلَيْكَ", "alayka", "«and ʿalayka!» — «hold to!».", "«ve aleyke!» — «sarıl!».", "الْزَمْ", segments=wa("عَلَيْكَ", "alayka", "part"), pos="part"),
  mafismfil("زَيْدًا", "zayd", "«Zayd» — its object.", "«Zeyd» — mef'ûlü."),
  ay(kasra=True),
  amr_h("الْزَمْهُ", "الْزَمْ", "lazima", "«hold to him»", "«ona sarıl»", punct="،", extra="، هَمْزَتُهُ هَمْزَةُ وَصْلٍ"),
  ismfil_amr("وَدُونَكَ", "dunaka", "«and dūnaka!» — «take!».", "«ve dûneke!» — «al!».", "خُذْ", segments=wa("دُونَكَ", "dunaka", "noun")),
  mafismfil("عَمْرًا", "amr-name", "«ʿAmr» — its object; the silent wāw is dropped in naṣb.", "«Amr» — mef'ûlü; nasbda sessiz vâv yazılmaz."),
  ay(),
  amr_h("خُذْهُ", "خُذْ", "akhadha", "«take him»", "«onu al»", punct="،"),
  ismfil_amr("وَتَرَاكِ", "taraki", "«and tarāki!» — «leave!» (built on the kasra, the فَعَالِ pattern).", "«ve terâki!» — «terk et!» (kesre üzere mebnî, feâli vezni).", "اتْرُكْ", segments=wa("تَرَاكِ", "taraki", "noun")),
  mafismfil("زَيْدًا", "zayd", "«Zayd» — its object.", "«Zeyd» — mef'ûlü."),
  ay(kasra=True),
  amr_h("اتْرُكْهُ", "اتْرُكْ", "taraka", "«leave him»", "«onu terk et»", punct="،", extra="، هَمْزَتُهُ هَمْزَةُ وَصْلٍ"),
  tok("وَغَيْرُ", "ghayr", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَغَيْرُ مَعْطُوفٌ عَلَى الْمَحْكِيِّ مَرْفُوعٌ، مُضَافٌ.", "«and other than» — joined to the cited list.", "«ve … başkası» — hikâye edilenlere ma'tûf.", segments=wa("غَيْرُ", "ghayr", "noun")),
  tok("ذٰلِكَ", "dhalika", "pron", [K, ID, ISH], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«that»", "«bu»", punct="."),
 ]})
# ----------- s5 — the second kind (past sense): هَيْهَاتَ، شَتَّانَ، سَرْعَانَ، وَشْكَانَ
S.append({"id": "s5", "translation": {"en": "And the second is as in «hayhāta the matter!» — that is, it is far; «shattāna Zayd and ʿAmr!» — that is, the two have parted; «sarʿāna Zayd!» and «washkāna ʿAmr!» — that is, the two are near; and other than that.", "tr": "İkincisi: «heyhâte'l-emr!» — yani uzaklaştı; «şettâne Zeyd ve Amr!» — yani ikisi ayrıldı; «ser'âne Zeyd!» ve «veşkâne Amr!» — yani ikisi yaklaştı; ve bunlardan başkası, gibidir."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, IFL, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — مَا كَانَ بِمَعْنَى الْمَاضِي.", "«and the second» — the past kind: the mubtada.", "«ikincisi» — mâzî mânâsındaki: mübtedâ.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("نَحْوُ", "nahw", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar.", "«… gibi» — haber.", punct=":"),
  ismfil_madi("هَيْهَاتَ", "hayhat", "«hayhāta!» — «it is far».", "«heyhâte!» — «uzaklaştı».", "بَعُدَ"),
  failismfil("الْأَمْرُ", "amr-noun", "«the matter» — its doer.", "«iş» — fâili.", pos="noun"),
  ay(),
  tok("بَعُدَ", "baada", "verb", [K, IFL, HT, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — تَفْسِيرٌ لِهَيْهَاتَ.", "«it is far» — the explaining past verb.", "«uzaklaştı» — açıklayan mâzî.", punct="،"),
  ismfil_madi("وَشَتَّانَ", "shattana", "«and shattāna!» — «the two have parted».", "«ve şettâne!» — «ikisi ayrıldı».", "افْتَرَقَ", segments=wa("شَتَّانَ", "shattana", "noun")),
  failismfil("زَيْدٌ", "zayd", "«Zayd» — its doer.", "«Zeyd» — fâili."),
  tok("وَعَمْرٌو", "amr-name", "propn", [K, AT, IFL], "الْوَاوُ عَاطِفَةٌ، وَعَمْرٌو مَعْطُوفٌ عَلَى زَيْدٌ مَرْفُوعٌ — وَاوُهُ صَامِتَةٌ.", "«and ʿAmr» — joined to Zayd; the silent wāw.", "«ve Amr» — Zeyd'e ma'tûf; sessiz vâv.", segments=wa("عَمْرٌو", "amr-name", "propn")),
  ay(kasra=True),
  tok("افْتَرَقَا", "iftaraqa", "verb", [K, IFL, HT, FL, F8, MTH], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، هَمْزَتُهُ هَمْزَةُ وَصْلٍ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ — تَفْسِيرٌ لِشَتَّانَ.", "«the two have parted» — the alif of the dual is its doer.", "«ikisi ayrıldı» — tesniye elifi fâil.", punct="،"),
  ismfil_madi("وَسَرْعَانَ", "saraana", "«and sarʿāna!» — «how quickly … is near».", "«ve ser'âne!» — «ne çabuk yaklaştı».", "قَرُبَ", segments=wa("سَرْعَانَ", "saraana", "noun")),
  failismfil("زَيْدٌ", "zayd", "«Zayd» — its doer.", "«Zeyd» — fâili."),
  ismfil_madi("وَوَشْكَانَ", "washkana", "«and washkāna!» — «how soon … is near».", "«ve veşkâne!» — «ne tez yaklaştı».", "قَرُبَ", segments=wa("وَشْكَانَ", "washkana", "noun")),
  failismfil("عَمْرٌو", "amr-name", "«ʿAmr» — its doer.", "«Amr» — fâili."),
  ay(),
  tok("قَرُبَا", "qaruba", "verb", [K, IFL, HT, FL, MTH], "فِعْلٌ مَاضٍ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ — تَفْسِيرٌ لِسَرْعَانَ وَوَشْكَانَ.", "«the two are near» — the explaining past verb.", "«ikisi yaklaştı» — açıklayan mâzî.", punct="،"),
  tok("وَغَيْرُ", "ghayr", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَغَيْرُ مَعْطُوفٌ عَلَى الْمَحْكِيِّ مَرْفُوعٌ، مُضَافٌ.", "«and other than»", "«ve … başkası»", segments=wa("غَيْرُ", "ghayr", "noun")),
  tok("ذٰلِكَ", "dhalika", "pron", [K, ID, ISH], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«that»", "«bu»", punct="."),
 ]})
# ----------- s6 — the settled ẓarf: no object; the manifest doer only on leaning
S.append({"id": "s6", "translation": {"en": "And of it is the SETTLED ẒARF — its explanation has passed — and it does not govern the direct object by agreement, nor the manifest doer except on condition of leaning on what was mentioned, or on the relative pronoun.", "tr": "Bundan ZARF-I MÜSTAKAR'dır — açıklaması geçti — ve o, ittifakla mef'ûlün bihte amel etmez; zâhir fâilde de ancak zikredilenlere veya mevsûle dayanmak şartıyla amel eder."},
 "tokens": [
  minhu(),
  tok("الظَّرْفُ", "zarf", "noun", [K, MK, ZM], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the ẓarf» — the delayed mubtada.", "«zarf» — sonraya bırakılmış mübtedâ."),
  tok("الْمُسْتَقَرُّ", "mustaqarr", "noun", [K, NA, ZM], "نَعْتٌ مَرْفُوعٌ — الظَّرْفُ الَّذِي مُتَعَلِّقُهُ عَامٌّ مَحْذُوفٌ.", "«settled» — the ẓarf whose general mutaʿallaq is dropped.", "«müstakar» — umûmî müteallakı hazfedilmiş zarf.", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ لِلِاعْتِرَاضِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed»", "«ve gerçekten»", segments=wa("قَدْ", "qad", "part")),
  tok("مَرَّ", "marra", "verb", [K, FL], "فِعْلٌ مَاضٍ.", "«has passed»", "«geçti»"),
  tok("تَفْسِيرُهُ", "tafsir", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its explanation» — the doer.", "«açıklaması» — fâil.", punct="،", segments=[seg("تَفْسِيرُ", "tafsir", "noun"), pr3ms()]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-mez»"),
  tok("يَعْمَلُ", "amila", "verb", [K, FL, MK], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«governs» — the khabar clause.", "«amel eder» — haber cümlesi."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْمَفْعُولِ", "maful-noun", "noun", [K, HJ, MB], "مَجْرُورٌ بِفِي.", "«the object»", "«mef'ûl»"),
  tok("بِهِ", "bi", "prep", [K, HJ, MB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْمَفْعُولُ بِهِ.", "«direct» — the mafʿūl bihi.", "«bih» — mef'ûlün bih.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("بِالِاتِّفَاقِ", "ittifaq", "noun", [K, HJ, MSD, F8], "الْبَاءُ حَرْفُ جَرٍّ، وَالِاتِّفَاقِ مَجْرُورٌ — بِاتِّفَاقِ النُّحَاةِ.", "«by agreement» — of the grammarians.", "«ittifakla» — nahivcilerin ittifakıyla.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الِاتِّفَاقِ", "ittifaq", "noun")]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ مُؤَكِّدَةٌ لِلنَّفْيِ.", "«nor»", "«ne de»", segments=wa("لَا", "la-nafiya", "part")),
  tok("فِي", "fi", "prep", [K, HJ, AT], "حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى فِي الْمَفْعُولِ.", "«in»", "«-de»"),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, HJ, FL], "مَجْرُورٌ بِفِي.", "«the doer»", "«fâil»"),
  tok("الظَّاهِرِ", "zahir", "noun", [K, NA, IFA], "نَعْتٌ مَجْرُورٌ — الِاسْمُ الظَّاهِرُ لَا الضَّمِيرُ.", "«manifest» — a noun, not a pronoun.", "«zâhir» — zamir değil, açık isim."),
  tok("إِلَّا", "illa", "part", [K, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ — الِاسْتِثْنَاءُ مُفَرَّغٌ.", "«except»", "«ancak»"),
  tok("بِشَرْطِ", "shart", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَشَرْطِ مَجْرُورٌ، مُضَافٌ.", "«on condition of»", "«şartıyla»", segments=[seg("بِ", "bi", "prep"), seg("شَرْطِ", "shart", "noun")]),
  tok("الِاعْتِمَادِ", "itimad", "noun", [K, ID, MSD, F8, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الِاعْتِمَادُ: شَرْطُ عَمَلِ اسْمِ الْفَاعِلِ.", "«leaning» — the ism fāʿil's condition.", "«i'timâd» — ism-i fâilin şartı."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ — مُتَعَلِّقٌ بِالِاعْتِمَادِ (قُرِئَ فِي الطَّبْعَةِ: إِلَّا).", "«on» — the lithograph transcription reads «except» here.", "«-e» — taşbaskı transkripsiyonunda «illâ» okunmuştur."),
  tok("مَا", "ma-mawsula", "pron", [K, HJ, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what»", "«… şey»"),
  tok("ذُكِرَ", "dhakara", "verb", [K, NF, MJH, MAW], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — صِلَةُ مَا: النَّفْيُ وَالِاسْتِفْهَامُ وَالْمَوْصُوفُ وَذُو الْحَالِ.", "«was mentioned» — the relative clause: negation, question, the described noun, the owner of the ḥāl.", "«zikredildi» — sıla: nefiy, istifhâm, mevsûf, zü'l-hâl."),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«veya»"),
  tok("الْمَوْصُولِ", "mawsul", "noun", [K, AT, MAW, IMF], "مَعْطُوفٌ عَلَى مَا مَجْرُورٌ — الِاسْمُ الْمَوْصُولُ.", "«the relative pronoun»", "«mevsûl»", punct="."),
 ]})
# ----------- s7 — the three examples of the settled ẓarf raising a manifest doer
S.append({"id": "s7", "translation": {"en": "As in «Zayd — in the house is his father», «there is not in the house anyone», and «there came he who — in the house is his father».", "tr": "«Zeyd — evde babası vardır», «evde hiç kimse yoktur» ve «evde babası olan geldi» gibi."},
 "tokens": [
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, ZM], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ — اعْتَمَدَ عَلَيْهِ الظَّرْفُ.", "«Zayd» — the mubtada the ẓarf leans on.", "«Zeyd» — zarfın dayandığı mübtedâ."),
  fi_zarf("«in» — the settled ẓarf, the khabar.", "«-de» — zarf-ı müstakar, haber."),
  aldar(),
  abuhu(punct="،"),
  tok("وَمَا", "ma-nafiya", "part", [K, AT, ZM], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ — اعْتَمَدَ عَلَيْهَا الظَّرْفُ.", "«and not» — the negation the ẓarf leans on.", "«ve yoktur» — zarfın dayandığı nefiy.", segments=wa("مَا", "ma-nafiya", "part")),
  fi_zarf("«in» — the settled ẓarf, the fronted khabar.", "«-de» — zarf-ı müstakar, öne alınmış haber."),
  aldar(),
  tok("أَحَدٌ", "ahad", "noun", [K, ZM, FL, MK], "فَاعِلُ الظَّرْفِ الْمُسْتَقَرِّ مَرْفُوعٌ (أَوْ مُبْتَدَأٌ مُؤَخَّرٌ) — الظَّرْفُ اعْتَمَدَ عَلَى النَّفْيِ.", "«anyone» — the doer the ẓarf raises after the negation.", "«hiç kimse» — nefiyden sonra zarfın ref' ettiği fâil.", punct="،"),
  tok("وَجَاءَ", "jaa", "verb", [K, AT, FL, HV], "الْوَاوُ عَاطِفَةٌ، وَجَاءَ فِعْلٌ مَاضٍ.", "«and there came»", "«ve geldi»", segments=wa("جَاءَ", "jaa", "verb")),
  tok("الَّذِي", "alladhi", "pron", [K, FL, MAW, ZM], "اسْمٌ مَوْصُولٌ فَاعِلٌ فِي مَحَلِّ رَفْعٍ — اعْتَمَدَ عَلَيْهِ الظَّرْفُ.", "«he who» — the doer; the relative the ẓarf leans on.", "«… olan» — fâil; zarfın dayandığı mevsûl."),
  fi_zarf("«in» — the settled ẓarf: the relative clause.", "«-de» — zarf-ı müstakar: sıla.", tags=[MAW]),
  aldar(),
  abuhu(punct=".", ar="فَاعِلُ الظَّرْفِ الْمُسْتَقَرِّ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَهُوَ الْعَائِدُ؛ الظَّرْفُ اعْتَمَدَ عَلَى الْمَوْصُولِ."),
 ]})
# ----------- s8 — the ẓarf as a fronted khabar; its concealed doer; the ḥāl and the ẓarf without condition
S.append({"id": "s8", "translation": {"en": "And the ẓarf may be a fronted khabar; and when it raises no manifest noun, its doer is a pronoun concealed in it, moved from its dropped mutaʿallaq; and it governs other than these two — such as the ḥāl and the ẓarf — without condition.", "tr": "Zarfın öne alınmış haber olması câizdir; zâhir bir ismi ref' etmediğinde fâili, hazfedilmiş müteallakından ona geçmiş gizli bir zamirdir; bu ikisinden başkasında — hâl ve zarf gibi — şartsız amel eder."},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("كَوْنُ", "kawn", "noun", [K, FL, ID, MSD, KN], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ كَانَ يَعْمَلُ عَمَلَهَا.", "«the being of» — the doer; kāna's maṣdar governs as kāna does.", "«olması» — fâil; kâne'nin mastarı onun gibi amel eder."),
  tok("الظَّرْفِ", "zarf", "noun", [K, ID, KN, ZM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ كَوْنُ فِي الْمَعْنَى.", "«the ẓarf» — the ism of «being».", "«zarfın» — kevn'in ismi."),
  tok("خَبَرًا", "khabar-predicate", "noun", [K, KN, MK], "خَبَرُ كَوْنُ مَنْصُوبٌ.", "«a khabar» — the khabar of «being».", "«haber» — kevn'in haberi."),
  tok("مُقَدَّمًا", "muqaddam", "noun", [K, NA, IMF, MK], "نَعْتٌ مَنْصُوبٌ — مُقَدَّمًا عَلَى الْمُبْتَدَإِ: فِي الدَّارِ زَيْدٌ.", "«fronted» — before the mubtada: فِي الدَّارِ زَيْدٌ.", "«öne alınmış» — mübtedâdan önce: fi'd-dâri Zeydün.", punct="،"),
  tok("وَإِذَا", "idha", "part", [K, AT, MF], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the conditional time-adverb.", "«ve … -diğinde» — şart mânâlı zaman zarfı.", segments=wa("إِذَا", "idha", "part")),
  tok("لَمْ", "lam-jazima", "part", [K, MJZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mez»"),
  tok("يَرْفَعْ", "rafaa", "verb", [K, MJZ, FL], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الظَّرْفُ.", "«it raises» — jussive after lam; the ẓarf is its doer.", "«ref' etmez» — lem ile meczûm; fâili zarf."),
  tok("ظَاهِرًا", "zahir", "noun", [K, MB, IFA], "مَفْعُولٌ بِهِ مَنْصُوبٌ — اسْمًا ظَاهِرًا.", "«a manifest noun» — the object.", "«zâhir bir isim» — mef'ûl."),
  tok("فَفَاعِلُهُ", "fail-doer", "noun", [K, MK, ID, FL], "الْفَاءُ رَابِطَةٌ لِجَوَابِ إِذَا، وَفَاعِلُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«then its doer» — the fāʾ of the apodosis; the mubtada.", "«o hâlde fâili» — cevap fâsı; mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("فَاعِلُ", "fail-doer", "noun"), pr3ms()]),
  tok("ضَمِيرٌ", "damir", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«a pronoun» — the khabar.", "«bir zamir» — haber."),
  tok("مُسْتَتِرٌ", "mustatir", "noun", [K, NA, IFA, "form-x-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلِ اسْتَتَرَ.", "«concealed» — a naʿt.", "«gizli» — na't."),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — فِي الظَّرْفِ.", "«in it» — in the ẓarf.", "«onda» — zarfta.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("مُنْتَقِلٌ", "muntaqil", "noun", [K, NA, IFA, F8], "نَعْتٌ ثَانٍ مَرْفُوعٌ — اسْمُ فَاعِلِ انْتَقَلَ.", "«moved» — a second naʿt.", "«geçmiş» — ikinci na't."),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("مُتَعَلَّقِهِ", "mutaallaq", "noun", [K, HJ, ID, IMF], "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَامِلُ الَّذِي يَتَعَلَّقُ بِهِ الظَّرْفُ.", "«its mutaʿallaq» — the governor the ẓarf hangs on.", "«müteallakından» — zarfın bağlandığı âmil.", segments=[seg("مُتَعَلَّقِ", "mutaallaq", "noun"), pr3msi()]),
  tok("الْمَحْذُوفِ", "mahdhuf", "noun", [K, NA, IMF, HT], "نَعْتٌ مَجْرُورٌ — كَائِنٌ أَوْ مُسْتَقِرٌّ.", "«dropped» — «existing» or «settled».", "«hazfedilmiş» — kâinün veya müstakırrun.", punct="،"),
  tok("وَيَعْمَلُ", "amila", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَيَعْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and it governs»", "«ve amel eder»", segments=wa("يَعْمَلُ", "amila", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("غَيْرِهَا", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — غَيْرِ الْفَاعِلِ وَالْمَفْعُولِ بِهِ.", "«other than these two» — the doer and the object.", "«bu ikisinden başkasında» — fâil ve mef'ûlün bih.", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3fs()]),
  tok("كَالْحَالِ", "hal", "noun", [K, HJ, HL], "الْكَافُ حَرْفُ جَرٍّ، وَالْحَالِ مَجْرُورٌ.", "«such as the ḥāl»", "«hâl gibi»", segments=[seg("كَ", "ka", "prep"), seg("الْحَالِ", "hal", "noun")]),
  tok("وَالظَّرْفِ", "zarf", "noun", [K, AT, MF], "الْوَاوُ عَاطِفَةٌ، وَالظَّرْفِ مَعْطُوفٌ مَجْرُورٌ.", "«and the ẓarf»", "«ve zarf»", segments=wa("الظَّرْفِ", "zarf", "noun")),
  tok("بِلَا", "bila", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَا زَائِدَةٌ لِلنَّفْيِ.", "«without»", "«-sız»"),
  tok("شَرْطٍ", "shart", "noun", [K, HJ], "مَجْرُورٌ بِالْبَاءِ.", "«condition»", "«şart»", punct="."),
 ]})
# ----------- s9 — the nisba noun governs as the ism mafʿūl does
S.append({"id": "s9", "translation": {"en": "And of it is the NISBA NOUN, for it governs as the ism mafʿūl governs, as in «I passed by a man Hashimite his brother», and what is stipulated for the ism mafʿūl's governing is stipulated for its governing.", "tr": "Bundan MENSÛB İSİM'dir; çünkü ism-i mef'ûlün ameli gibi amel eder, «kardeşi Hâşimî olan bir adama uğradım» gibi; ism-i mef'ûlün amelinde şart koşulan, bunun amelinde de şart koşulur."},
 "tokens": [
  minhu(),
  tok("الْمَنْسُوبُ", "mansub-nisba", "noun", [K, MK, NSB, IMF], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — الِاسْمُ الْمَنْسُوبُ بِيَاءِ النِّسْبَةِ.", "«the nisba noun» — the delayed mubtada.", "«mensûb isim» — sonraya bırakılmış mübtedâ.", punct="،"),
  tok("فَإِنَّهُ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«for it» — inna with its pronoun ism.", "«çünkü o» — inne, zamir ismi.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("يَعْمَلُ", "amila", "verb", [K, IN, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«governs» — the khabar of inna.", "«amel eder» — inne'nin haberi."),
  tok("كَعَمَلِ", "amal-governing", "noun", [K, HJ, ID, MM], "الْكَافُ حَرْفُ جَرٍّ، وَعَمَلِ مَجْرُورٌ، مُضَافٌ — نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ.", "«as the governing of» — standing for the absolute object.", "«… ameli gibi» — mef'ûl-i mutlak yerine."),
  tok("اسْمِ", "ism", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the noun of»", "«ism-i»"),
  tok("الْمَفْعُولِ", "maful-object", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْمَفْعُولِ.", "«the acted-upon» — the ism mafʿūl.", "«mef'ûl» — ism-i mef'ûl.", punct="،"),
  nahw(),
  tok("مَرَرْتُ", "marra", "verb", [K, FL, NSB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مُضَاعَفٌ فُكَّ إِدْغَامُهُ، وَالتَّاءُ فَاعِلٌ.", "«I passed» — the doubled verb opened before the tāʾ.", "«uğradım» — tâ'dan önce idgamı çözülmüş muzâaf fiil.", segments=[seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("بِرَجُلٍ", "rajul", "noun", [K, HJ, NSB], "الْبَاءُ حَرْفُ جَرٍّ، وَرَجُلٍ مَجْرُورٌ — الْمَوْصُوفُ.", "«by a man» — the described noun.", "«bir adama» — mevsûf.", segments=[seg("بِ", "bi", "prep"), seg("رَجُلٍ", "rajul", "noun")]),
  tok("هَاشِمِيٍّ", "hashimi", "noun", [K, NA, NSB, MNF], "نَعْتٌ مَجْرُورٌ — الْمَنْسُوبُ، بِمَعْنَى مَنْسُوبٍ إِلَى هَاشِمٍ: اعْتَمَدَ عَلَى الْمَوْصُوفِ فَرَفَعَ.", "«Hashimite» — the nisba noun: «related to Hāshim», leaning on the described noun, so it raises.", "«Hâşimî» — mensûb isim: «Hâşim'e nisbet edilen», mevsûfa dayanır ve ref' eder."),
  tok("أَخُوهُ", "akh", "noun", [K, NSB, FL, ALK, ID], "فَاعِلُ الْمَنْسُوبِ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — كَنَائِبِ فَاعِلِ اسْمِ الْمَفْعُولِ.", "«his brother» — the doer the nisba noun raises, as the ism mafʿūl raises its deputy doer.", "«kardeşi» — mensûbun ref' ettiği fâil; ism-i mef'ûlün nâib-i fâili gibi.", punct="،", segments=[seg("أَخُو", "akh", "noun"), pr3ms()]),
  tok("وَيُشْتَرَطُ", "ishtarata", "verb", [K, AT, NF, F8, MJH], "الْوَاوُ عَاطِفَةٌ، وَيُشْتَرَطُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«and is stipulated»", "«ve şart koşulur»", segments=wa("يُشْتَرَطُ", "ishtarata", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("عَمَلِهِ", "amal-governing", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَمَلِ الْمَنْسُوبِ.", "«its governing» — the nisba noun's.", "«amelinde» — mensûbun ameli.", segments=[seg("عَمَلِ", "amal-governing", "noun"), pr3msi()]),
  tok("مَا", "ma-mawsula", "pron", [K, NF, MAW], "اسْمٌ مَوْصُولٌ نَائِبُ فَاعِلٍ فِي مَحَلِّ رَفْعٍ.", "«what» — the deputy doer.", "«… şey» — nâib-i fâil."),
  tok("يُشْتَرَطُ", "ishtarata", "verb", [K, NF, F8, MJH, MAW], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — صِلَةُ مَا.", "«is stipulated» — the relative clause.", "«şart koşulur» — sıla."),
  tok("فِيهِ", "fi", "prep", [K, HJ, IMF], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — فِي اسْمِ الْمَفْعُولِ: الِاعْتِمَادُ.", "«for it» — for the ism mafʿūl: the leaning.", "«onda» — ism-i mef'ûlde: i'timâd.", punct=".", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
 ]})
# ----------- s10 — the borrowed noun: أَسَدٌ غُلَامُهُ، أَسَدٌ عَلَيَّ
S.append({"id": "s10", "translation": {"en": "And of it is the BORROWED NOUN, as in «lion» in your saying «I passed by a man, a lion his servant», and «a lion against me» — that is, bold — and that is why it governed «against».", "tr": "Bundan MÜSTEÂR İSİM'dir, «kölesi aslan olan bir adama uğradım» sözündeki «aslan» ve «bana karşı aslan» — yani cür'etkâr — gibi; bu yüzden «alâ»da amel etti."},
 "tokens": [
  minhu(),
  tok("الِاسْمُ", "ism", "noun", [K, MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the noun» — the delayed mubtada.", "«isim» — sonraya bırakılmış mübtedâ."),
  tok("الْمُسْتَعَارُ", "mustaar", "noun", [K, NA, IST, IMF], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ اسْتَعَارَ: الْمُسْتَعْمَلُ فِي غَيْرِ مَا وُضِعَ لَهُ لِعَلَاقَةِ الْمُشَابَهَةِ.", "«borrowed» — used for other than what it was coined for, by likeness.", "«müsteâr» — benzerlik alâkasıyla konulduğundan başka mânâda kullanılan.", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ.", "«as in»", "«… gibi»"),
  tok("أَسَدٌ", "asad", "noun", [K, ID, IST, HT], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ، مَرْفُوعٌ عَلَى الْحِكَايَةِ.", "«lion» — the cited word.", "«aslan» — hikâye edilen kelime."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("قَوْلِكَ", "qawl", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your saying»", "«sözün»", punct=":", segments=[seg("قَوْلِ", "qawl", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("مَرَرْتُ", "marra", "verb", [K, FL, IST], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I passed»", "«uğradım»", segments=[seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("بِرَجُلٍ", "rajul", "noun", [K, HJ, IST], "الْبَاءُ حَرْفُ جَرٍّ، وَرَجُلٍ مَجْرُورٌ — الْمَوْصُوفُ.", "«by a man» — the described noun.", "«bir adama» — mevsûf.", segments=[seg("بِ", "bi", "prep"), seg("رَجُلٍ", "rajul", "noun")]),
  tok("أَسَدٍ", "asad", "noun", [K, NA, IST, MNF], "نَعْتٌ مَجْرُورٌ — الِاسْمُ الْمُسْتَعَارُ لِلشُّجَاعِ: فُهِمَ مِنْهُ مَعْنَى الصِّفَةِ فَعَمِلَ.", "«a lion» — borrowed for «brave»: a ṣifa's sense is understood from it, so it governs.", "«aslan» — «cesur» için müsteâr: ondan sıfat mânâsı anlaşılır, o yüzden amel eder."),
  tok("غُلَامُهُ", "ghulam", "noun", [K, IST, FL, ID], "فَاعِلُ الِاسْمِ الْمُسْتَعَارِ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his servant» — the doer the borrowed noun raises.", "«kölesi» — müsteâr ismin ref' ettiği fâil.", punct="،", segments=[seg("غُلَامُ", "ghulam", "noun"), pr3ms()]),
  tok("وَأَسَدٌ", "asad", "noun", [K, AT, IST, MK, HT], "الْوَاوُ عَاطِفَةٌ، وَأَسَدٌ لَفْظٌ مَحْكِيٌّ: خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — هُوَ أَسَدٌ.", "«and a lion» — the khabar of a dropped «he».", "«ve aslan» — hazfedilmiş «o»nun haberi.", segments=wa("أَسَدٌ", "asad", "noun")),
  tok("عَلَيَّ", "ala", "prep", [K, HJ, IST, MNF], "عَلَى حَرْفُ جَرٍّ، وَالْيَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِأَسَدٌ لِمَا فِيهِ مِنْ مَعْنَى الْفِعْلِ.", "«against me» — hangs on «lion» for the verb's sense in it.", "«bana karşı» — içindeki fiil mânâsıyla «aslan»a bağlı.", segments=[seg("عَلَيْ", "ala", "prep"), seg("يَ", "pron-1s", "pron")]),
  ay(),
  tok("مُجْتَرِئٌ", "mujtari", "noun", [K, HT, IFA, F8], "تَفْسِيرٌ لِأَسَدٌ: خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ — اسْمُ فَاعِلِ اجْتَرَأَ.", "«bold» — the explanation: the ism fāʿil of «to dare».", "«cür'etkâr» — açıklama: icterae'nin ism-i fâili.", punct="،"),
  tok("فَلِذَا", "dha", "pron", [K, HJ, ISH], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«and that is why»", "«bu yüzden»", segments=[seg("فَ", "fa", "conj"), seg("لِ", "li", "prep"), seg("ذَا", "dha", "pron")]),
  tok("عَمِلَ", "amila", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — أَسَدٌ.", "«it governed» — the lion.", "«amel etti» — aslan."),
  tok("عَلَى", "ala", "prep", [K, MB, HT], "لَفْظٌ مَحْكِيٌّ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ — أَيْ عَمِلَ فِي الْجَارِّ وَالْمَجْرُورِ: عَلَيَّ.", "«against» — the cited word as the object: it governed the jarr phrase.", "«alâ» — mef'ûl olarak hikâye edilen kelime: câr-mecrûrda amel etti.", punct="."),
 ]})
# ----------- s11 — every noun from which a ṣifa's sense is understood: لَفْظَةُ اللهِ
S.append({"id": "s11", "translation": {"en": "And of it is every noun from which the sense of a ṣifa is understood, as the word «God» in His word, Most High: «and He is God in the heavens» — that is, the One worshipped in them.", "tr": "Bundan, kendisinden sıfat mânâsı anlaşılan her isimdir; Allah Teâlâ'nın «O, göklerde Allah'tır» sözündeki «Allah» lafzı gibi — yani onlarda ibadet edilen."},
 "tokens": [
  minhu(),
  tok("كُلُّ", "kull", "noun", [K, MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«every» — the delayed mubtada.", "«her» — sonraya bırakılmış mübtedâ."),
  tok("اسْمٍ", "ism", "noun", [K, ID, JS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«noun»", "«isim»"),
  tok("فُهِمَ", "fahima", "verb", [K, NA, NF, MJH, JS], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَالْجُمْلَةُ نَعْتٌ لِاسْمٍ.", "«is understood» — the ṣifa clause of «noun».", "«anlaşılır» — ismin sıfat cümlesi."),
  tok("مِنْهُ", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«from it»", "«ondan»", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("مَعْنَى", "mana", "noun", [K, NF, ID, MQ], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the sense of» — the deputy doer.", "«mânâsı» — nâib-i fâil."),
  tok("الصِّفَةِ", "sifa", "noun", [K, ID, NA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a ṣifa»", "«sıfat»", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ.", "«as»", "«… gibi»"),
  tok("لَفْظَةِ", "lafza", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the word»", "«lafzı»"),
  tok("اللهِ", "allah", "propn", [K, ID, MNF], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("قَوْلِهِ", "qawl", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His word»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("تَعَالَى", "taala", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.", "«Most High»", "«Teâlâ»", punct=":"),
  tok("وَهُوَ", "huwa", "pron", [K, MK, QA, MNF], "لَفْظٌ مَحْكِيٌّ (مِنَ الْقُرْآنِ، الْأَنْعَام ٣): الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and He» — the mubtada (al-Anʿām 3).", "«ve O» — mübtedâ (En'âm 3).", segments=wa("هُوَ", "huwa", "pron")),
  tok("اللهُ", "allah", "propn", [K, MK, QA, MNF], "لَفْظُ الْجَلَالَةِ خَبَرٌ مَرْفُوعٌ — فُهِمَ مِنْهُ مَعْنَى الْمَعْبُودِ فَعَمِلَ فِي الظَّرْفِ.", "«God» — the khabar; «the worshipped» is understood from it, so it governs the ẓarf.", "«Allah» — haber; ondan «ma'bûd» mânâsı anlaşılır, o yüzden zarfta amel eder."),
  tok("فِي", "fi", "prep", [K, HJ, QA, MF], "حَرْفُ جَرٍّ — مُتَعَلِّقٌ بِلَفْظِ اللهِ لِمَا فِيهِ مِنْ مَعْنَى الصِّفَةِ.", "«in» — hangs on the word «God».", "«-de» — Allah lafzına bağlı."),
  tok("السَّمٰوَاتِ", "sama", "noun", [K, HJ, QA, JMU], "مَجْرُورٌ بِفِي بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ (رَسْمُ الْمُصْحَفِ: السَّمٰوَات).", "«the heavens» — the sound feminine plural (the muṣḥaf's spelling).", "«gökler» — cem'-i müennes sâlim (mushaf imlâsı).", punct="،"),
  ay(kasra=True),
  tok("الْمَعْبُودُ", "mabud", "noun", [K, HT, IMF, MK], "تَفْسِيرٌ لِلَفْظِ اللهِ: خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ — اسْمُ مَفْعُولِ عَبَدَ.", "«the One worshipped» — the explanation: the ism mafʿūl of «to worship».", "«ma'bûd» — açıklama: abede'nin ism-i mef'ûlü."),
  tok("فِيهَا", "fi", "prep", [K, HJ, MF], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — فِي السَّمٰوَاتِ.", "«in them» — in the heavens.", "«onlarda» — göklerde.", punct=".", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
 ]})
# ----------- s12 — the demonstrative, لَيْتَ، لَعَلَّ, the letters of calling, likening, alerting, negation: the ḥāl and the ẓarf only
S.append({"id": "s12", "translation": {"en": "And of it are the demonstrative, «would that», «perhaps», the letter of calling, of likening, of alerting, of negation, and others — for they govern, among the verb's governed words, other than the doer and the direct object, such as the ḥāl and the ẓarf.", "tr": "Bundan ism-i işâret, leyte, lealle, nidâ, teşbîh, tenbîh ve nefiy harfleri ve başkalarıdır; çünkü bunlar fiilin ma'mûllerinden fâil ve mef'ûlün bih dışındakilerde — hâl ve zarf gibi — amel eder."},
 "tokens": [
  minhu(),
  tok("اسْمُ", "ism", "noun", [K, MK, ID, ISH], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the noun of» — the delayed mubtada.", "«ism-i» — sonraya bırakılmış mübtedâ."),
  tok("الْإِشَارَةِ", "ishara", "noun", [K, ID, ISH, MNF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْإِشَارَةِ: فِيهِ مَعْنَى أُشِيرُ.", "«pointing» — the demonstrative: «I point» is in it.", "«işâret» — ism-i işâret: içinde «işaret ederim» mânâsı var."),
  tok("وَلَيْتَ", "layta", "part", [K, AT, IN, MNF], "الْوَاوُ عَاطِفَةٌ، وَلَيْتَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ — فِيهِ مَعْنَى أَتَمَنَّى.", "«and would that» — «I wish» is in it.", "«ve leyte» — içinde «temenni ederim» mânâsı var.", segments=wa("لَيْتَ", "layta", "part")),
  tok("وَلَعَلَّ", "laalla", "part", [K, AT, IN, MNF], "الْوَاوُ عَاطِفَةٌ، وَلَعَلَّ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — فِيهِ مَعْنَى أَتَرَجَّى.", "«and perhaps» — «I hope» is in it.", "«ve lealle» — içinde «ümit ederim» mânâsı var.", segments=wa("لَعَلَّ", "laalla", "part")),
  tok("وَحَرْفُ", "harf", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَحَرْفُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and the letter of»", "«ve … harfi»", segments=wa("حَرْفُ", "harf", "noun")),
  tok("النِّدَاءِ", "nida", "noun", [K, ID, ND, MNF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — يَا: فِيهِ مَعْنَى أُنَادِي.", "«calling» — yā: «I call» is in it.", "«nidâ» — yâ: içinde «çağırırım» mânâsı var."),
  tok("وَالتَّشْبِيهِ", "tashbih", "noun", [K, AT, ID, MNF], "الْوَاوُ عَاطِفَةٌ، وَالتَّشْبِيهِ مَعْطُوفٌ عَلَى النِّدَاءِ مَجْرُورٌ — كَأَنَّ: فِيهِ مَعْنَى أُشَبِّهُ.", "«likening» — ka-anna: «I liken» is in it.", "«teşbîh» — keenne: içinde «benzetirim» mânâsı var.", segments=wa("التَّشْبِيهِ", "tashbih", "noun")),
  tok("وَالتَّنْبِيهِ", "tanbih", "noun", [K, AT, ID, TNB, MNF], "الْوَاوُ عَاطِفَةٌ، وَالتَّنْبِيهِ مَعْطُوفٌ مَجْرُورٌ — هَا: فِيهِ مَعْنَى أُنَبِّهُ.", "«alerting» — hā: «I alert» is in it.", "«tenbîh» — hâ: içinde «uyarırım» mânâsı var.", segments=wa("التَّنْبِيهِ", "tanbih", "noun")),
  tok("وَالنَّفْيِ", "nafy", "noun", [K, AT, ID, LN, MNF], "الْوَاوُ عَاطِفَةٌ، وَالنَّفْيِ مَعْطُوفٌ مَجْرُورٌ — مَا وَلَا: فِيهِ مَعْنَى أَنْفِي.", "«negation» — mā and lā: «I deny» is in it.", "«nefiy» — mâ ve lâ: içinde «nefyederim» mânâsı var.", segments=wa("النَّفْيِ", "nafy", "noun")),
  tok("وَغَيْرُهَا", "ghayr", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَغَيْرُ مَعْطُوفٌ عَلَى اسْمُ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and others»", "«ve başkaları»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("غَيْرُ", "ghayr", "noun"), pr3fs()]),
  tok("فَإِنَّهَا", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«for they» — inna with its pronoun ism.", "«çünkü bunlar» — inne, zamir ismi.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3fs()]),
  tok("تَعْمَلُ", "amila", "verb", [K, IN, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«govern» — the khabar of inna.", "«amel eder» — inne'nin haberi."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«other than»", "«… dışındakilerde»"),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, FL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer»", "«fâil»"),
  tok("وَالْمَفْعُولِ", "maful-object", "noun", [K, AT, MB], "الْوَاوُ عَاطِفَةٌ، وَالْمَفْعُولِ مَعْطُوفٌ مَجْرُورٌ.", "«and the object»", "«ve mef'ûl»", segments=wa("الْمَفْعُولِ", "maful-object", "noun")),
  tok("بِهِ", "bi", "prep", [K, HJ, MB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْمَفْعُولُ بِهِ.", "«direct»", "«bih»", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«among»", "«-den»"),
  tok("مَعْمُولَاتِ", "mamul", "noun", [K, HJ, ID, JMU, IMF], "مَجْرُورٌ بِمِنْ بِالْكَسْرَةِ، مُضَافٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the governed words of»", "«ma'mûlleri»"),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiilin»"),
  tok("كَالْحَالِ", "hal", "noun", [K, HJ, HL], "الْكَافُ حَرْفُ جَرٍّ، وَالْحَالِ مَجْرُورٌ.", "«such as the ḥāl»", "«hâl gibi»", segments=[seg("كَ", "ka", "prep"), seg("الْحَالِ", "hal", "noun")]),
  tok("وَالظَّرْفِ", "zarf", "noun", [K, AT, MF], "الْوَاوُ عَاطِفَةٌ، وَالظَّرْفِ مَعْطُوفٌ مَجْرُورٌ.", "«and the ẓarf»", "«ve zarf»", punct=".", segments=wa("الظَّرْفِ", "zarf", "noun")),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

NEW = {
 "tasi": G("tasi", "تَاسِع", "ت س ع", "noun", "ninth", "dokuzuncu", 2),
 "ha-ism-fil": G("ha-ism-fil", "هَا (اسْمُ فِعْلٍ)", None, "noun", "hā! — «take!» (a noun-verb of command: هَا زَيْدًا)", "hâ! — «al!» (emir isim fiili: hâ Zeyden)", 4),
 "halumma": G("halumma", "هَلُمَّ", None, "noun", "halumma! — «bring!», «come!» (a noun-verb of command)", "helümme! — «getir!», «gel!» (emir isim fiili)", 4),
 "hati": G("hati", "هَاتِ", None, "noun", "hāti! — «give!», «hand over!» (a noun-verb of command)", "hâti! — «ver!» (emir isim fiili)", 4),
 "hayyahal": G("hayyahal", "حَيَّهَلَ", None, "noun", "ḥayyahala! — «come to!», «hurry to!» (a compound noun-verb of command)", "hayyehele! — «gel!», «koş!» (mürekkeb emir isim fiili)", 5),
 "thurayd": G("thurayd", "ثَرِيد", "ث ر د", "noun", "tharīd — bread crumbled into broth", "tirit — et suyuna doğranmış ekmek", 4),
 "balha": G("balha", "بَلْهَ", None, "noun", "balha! — «leave!», «let alone» (a noun-verb of command)", "belhe! — «bırak!», «şöyle dursun» (emir isim fiili)", 5),
 "dunaka": G("dunaka", "دُونَكَ", None, "noun", "dūnaka! — «take!», «here, take it!» (a ẓarf turned noun-verb of command)", "dûneke! — «al!» (zarftan dönmüş emir isim fiili)", 4),
 "taraki": G("taraki", "تَرَاكِ", "ت ر ك", "noun", "tarāki! — «leave!» (a noun-verb of command on the فَعَالِ pattern)", "terâki! — «terk et!» (feâli vezninde emir isim fiili)", 5),
 "shattana": G("shattana", "شَتَّانَ", "ش ت ت", "noun", "shattāna! — «how different!», «the two have parted» (a noun-verb with a past sense)", "şettâne! — «ne kadar farklı!», «ikisi ayrıldı» (mâzî mânâlı isim fiil)", 4),
 "saraana": G("saraana", "سَرْعَانَ", "س ر ع", "noun", "sarʿāna! — «how quickly!» (a noun-verb with a past sense: it was quick, it drew near)", "ser'âne! — «ne çabuk!» (mâzî mânâlı isim fiil: çabuk oldu, yaklaştı)", 5),
 "washkana": G("washkana", "وَشْكَانَ", "و ش ك", "noun", "washkāna! — «how soon!» (a noun-verb with a past sense: it was soon, it drew near)", "veşkâne! — «ne tez!» (mâzî mânâlı isim fiil: tez oldu, yaklaştı)", 5),
 "iftaraqa": G("iftaraqa", "اِفْتَرَقَ", "ف ر ق", "verb", "to part, to separate from one another", "ayrılmak, birbirinden ayrılmak", 3, form="VIII"),
 "mawsul": G("mawsul", "مَوْصُول", "و ص ل", "noun", "the relative pronoun (al-ism al-mawṣūl); joined", "mevsûl (ism-i mevsûl); bağlanmış", 3),
 "muqaddam": G("muqaddam", "مُقَدَّم", "ق د م", "noun", "fronted, put first (ism mafʿūl of قَدَّمَ)", "öne alınmış, mukaddem (kaddeme'nin ism-i mef'ûlü)", 3),
 "mustatir": G("mustatir", "مُسْتَتِر", "س ت ر", "noun", "concealed (of a pronoun: ism fāʿil of اسْتَتَرَ)", "gizli, müstetir (zamir için: istetere'nin ism-i fâili)", 3),
 "muntaqil": G("muntaqil", "مُنْتَقِل", "ن ق ل", "noun", "moved over, transferred (ism fāʿil of انْتَقَلَ)", "geçmiş, intikal etmiş (intekale'nin ism-i fâili)", 3),
 "mansub-nisba": G("mansub-nisba", "مَنْسُوب", "ن س ب", "noun", "the nisba noun — related to (ism mafʿūl of نَسَبَ, the noun with the yāʾ of relation)", "mensûb — nisbet edilen (nesebe'nin ism-i mef'ûlü, nisbet yâlı isim)", 3),
 "lafza": G("lafza", "لَفْظَة", "ل ف ظ", "noun", "a word, a single utterance", "lafız, bir kelime", 2),
 "mabud": G("mabud", "مَعْبُود", "ع ب د", "noun", "worshipped, the object of worship (ism mafʿūl of عَبَدَ)", "ma'bûd, ibadet edilen (abede'nin ism-i mef'ûlü)", 3),
 "mujtari": G("mujtari", "مُجْتَرِئ", "ج ر أ", "noun", "bold, daring (ism fāʿil of اجْتَرَأَ)", "cür'etkâr, cesur (icterae'nin ism-i fâili)", 4),
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
put_morph(mo, "iftaraqa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِفْتَرَق", "فْتَرِق", "اِفْتَرِق", "اِفْتِرَاق", "مُفْتَرِق", None, None, None, "لَازِمٌ: افْتَرَقَ الرَّجُلَانِ — تَفَرَّقَا؛ لَا مَفْعُولَ لَهُ."))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch16 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("fahima", "amila", "taqaddama", "akhadha", "amhala", "ahdara", "aata", "ata", "da-leave", "lazima", "taraka", "baada", "iftaraqa", "qaruba", "marra", "dhakara", "jaa", "jaaza", "rafaa", "ishtarata", "kana", "taala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "مَعْنَى الْفِعْلِ: أَسْمَاءُ الْأَفْعَالِ وَالظَّرْفُ الْمُسْتَقَرُّ وَالْمَنْسُوبُ وَالْمُسْتَعَارُ", "en": "The sense of the verb as a governor: the noun-verbs, the settled ẓarf, the nisba and the borrowed noun", "tr": "Âmil olarak mana-yı fiil: isim fiiller, zarf-ı müstakar, mensûb ve müsteâr isim"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العوامل القياسية: معنى الفعل", "الكافية لابن الحاجب — أسماء الأفعال", "شرح قطر الندى لابن هشام — الظرف المستقر"],
 "amil": "مَعْنَى الْفِعْلِ — every utterance from which a verb's sense is understood (the noun-verbs, the settled ẓarf, the nisba noun, the borrowed noun, any noun with a ṣifa's sense, the demonstrative, لَيْتَ، لَعَلَّ and the letters of calling, likening, alerting and negation) governs as the verb it carries would — the last group only the ḥāl and the ẓarf",
 "question": {
  "en": ["What is the ninth qiyāsī governor? The SENSE OF THE VERB: every utterance from which a verb's meaning is understood, though it is not a verb.",
         "What are the noun-verbs? Words with the sense of a command (هَا = خُذْ، رُوَيْدَ = أَمْهِلْ، هَلُمَّ = أَحْضِرْ، هَاتِ = أَعْطِ، حَيَّهَلَ = ائْتِ، بَلْهَ = دَعْ، عَلَيْكَ = الْزَمْ، دُونَكَ = خُذْ، تَرَاكِ = اتْرُكْ) or of a past verb (هَيْهَاتَ = بَعُدَ، شَتَّانَ = افْتَرَقَا، سَرْعَانَ / وَشْكَانَ = قَرُبَ). They govern as the verb they name — هَا زَيْدًا puts Zayd in naṣb, هَيْهَاتَ الْأَمْرُ raises the matter — and their governed word never precedes them.",
         "What does the settled ẓarf govern? Never the direct object; the manifest doer only when it leans on what was mentioned (negation, question, the described noun, the owner of the ḥāl) or on the relative pronoun: زَيْدٌ فِي الدَّارِ أَبُوهُ، مَا فِي الدَّارِ أَحَدٌ، جَاءَ الَّذِي فِي الدَّارِ أَبُوهُ. It may be a fronted khabar (فِي الدَّارِ زَيْدٌ). When it raises no manifest noun its doer is a pronoun concealed in it, moved from the dropped mutaʿallaq. The ḥāl and the ẓarf it governs without any condition.",
         "Why does the lithograph read إلا before مَا ذُكِرَ? The transcription has إلا بشرط الاعتماد إلا ما ذكر; the standard text and the three examples require عَلَى مَا ذُكِرَ أَوِ الْمَوْصُولِ, which the reader prints and flags.",
         "How does the nisba noun govern? As the ism mafʿūl does: مَرَرْتُ بِرَجُلٍ هَاشِمِيٍّ أَخُوهُ — «related to Hāshim» raises «his brother» as the ism mafʿūl raises its deputy doer, under the same condition of leaning.",
         "And the borrowed noun? أَسَدٌ in مَرَرْتُ بِرَجُلٍ أَسَدٍ غُلَامُهُ raises «his servant», and أَسَدٌ عَلَيَّ means مُجْتَرِئٌ — bold — which is why it governs the jarr phrase عَلَيَّ.",
         "And any noun with a ṣifa's sense? لَفْظُ اللهِ in ﴿وَهُوَ اللهُ فِي السَّمٰوَاتِ﴾ (al-Anʿām 3) means الْمَعْبُودُ فِيهَا, so it governs the ẓarf فِي السَّمٰوَاتِ.",
         "And the demonstrative, لَيْتَ، لَعَلَّ, the letters of calling, likening, alerting and negation? They carry أُشِيرُ، أَتَمَنَّى، أَتَرَجَّى، أُنَادِي، أُشَبِّهُ، أُنَبِّهُ، أَنْفِي, so they govern the verb's governed words other than the doer and the object — the ḥāl and the ẓarf.",
         "What does the engine READ here? The DabtEngine keeps the noun-verbs on their binaʾ, puts the noun after a command noun-verb in naṣb as its object and raises the noun after a past-sense one as its doer, raises the noun after a settled ẓarf that leans on a mubtada, a negation or a relative, lets the nisba and the borrowed noun raise the pronoun-bearing noun after them, and reads the Qurʾānic ẓarf after لَفْظُ اللهِ as its governed word."],
  "tr": ["Dokuzuncu kıyâsî âmil nedir? MANA-YI FİİL: fiil olmadığı hâlde kendisinden bir fiil mânâsı anlaşılan her lafız.",
         "İsim fiiller nedir? Emir mânâsındaki (hâ = huz, ruveyde = emhil, helümme = ahdır, hâti = a'ti, hayyehele = i'ti, belhe = da', aleyke = ilzem, dûneke = huz, terâki = ütruk) veya mâzî mânâsındaki (heyhâte = baude, şettâne = ifterakâ, ser'âne / veşkâne = karube) kelimeler. Adını taşıdıkları fiil gibi amel ederler — hâ Zeyden Zeyd'i nasb eder, heyhâte'l-emru işi ref' eder — ve ma'mûlleri asla önlerine geçmez.",
         "Zarf-ı müstakar neyde amel eder? Mef'ûlün bihte asla; zâhir fâilde ancak zikredilenlere (nefiy, istifhâm, mevsûf, zü'l-hâl) veya mevsûle dayanınca: Zeydün fi'd-dâri ebûhu, mâ fi'd-dâri ehadün, câe'llezî fi'd-dâri ebûhu. Öne alınmış haber olabilir (fi'd-dâri Zeydün). Zâhir bir isim ref' etmediğinde fâili, hazfedilmiş müteallaktan ona geçmiş gizli bir zamirdir. Hâl ve zarfta şartsız amel eder.",
         "Taşbaskı mâ zükira'dan önce niçin illâ okunmuş? Transkripsiyonda illâ bi-şarti'l-i'timâdi illâ mâ zükira var; standart metin ve üç örnek alâ mâ zükira evi'l-mevsûl'ü gerektirir; okuyucu bunu basar ve işaretler.",
         "Mensûb isim nasıl amel eder? İsm-i mef'ûl gibi: merartü bi-racülin Hâşimiyyin ehûhu — «Hâşim'e nisbet edilen», ism-i mef'ûlün nâib-i fâilini ref' ettiği gibi «kardeşi»ni ref' eder; aynı i'timâd şartıyla.",
         "Müsteâr isim? merartü bi-racülin esedin gulâmuhu'daki esed «kölesi»ni ref' eder; esedün aleyye ise müctéri' — cür'etkâr — demektir; bu yüzden aleyye câr-mecrûrunda amel eder.",
         "Sıfat mânâsı anlaşılan her isim? ﴿ve hüve'llâhu fi's-semâvâti﴾ (En'âm 3) âyetindeki Allah lafzı el-ma'bûdü fîhâ demektir; o yüzden fi's-semâvât zarfında amel eder.",
         "İsm-i işâret, leyte, lealle, nidâ, teşbîh, tenbîh ve nefiy harfleri? İçlerinde üşîru, etemennâ, eteraccâ, ünâdî, üşebbihu, ünebbihu, enfî mânâsı vardır; bu yüzden fiilin ma'mûllerinden fâil ve mef'ûlün bih dışındakilerde — hâl ve zarfta — amel ederler.",
         "Motor burada neyi OKUR? DabtEngine isim fiilleri binâlarında tutar, emir isim fiilinden sonraki ismi mef'ûl olarak nasb eder ve mâzî mânâlı olandan sonrakini fâil olarak ref' eder; mübtedâya, nefye veya mevsûle dayanan zarf-ı müstakardan sonraki ismi ref' eder; mensûb ve müsteâr ismin ardındaki zamirli ismi ref' ettirir; Allah lafzından sonraki Kur'ânî zarfı onun ma'mûlü olarak okur."],
 },
 "plain": {"en": "Some words act like verbs without being verbs. «Hā!» means «take!», so the next word is an object: hā Zaydan. «Hayhāta!» means «it is far», so the next word is a doer. «In the house» hides an «is»; «Hashimite» and «a lion» (= brave) hide a quality. Each governs as the hidden verb would.",
           "tr": "Bazı kelimeler fiil olmadan fiil gibi davranır. «Hâ!» «al!» demektir, ardındaki mef'ûldür: hâ Zeyden. «Heyhâte!» «uzaklaştı» demektir, ardındaki fâildir. «Evde» içinde bir «vardır» saklar; «Hâşimî» ve «aslan» (= cesur) bir nitelik saklar. Her biri gizli fiilin amel edeceği gibi amel eder."},
 "explanation": {"en": "The ninth qiyāsī governor is the sense of the verb — every utterance from which a verb's meaning is understood. Of it are the noun-verbs, with the sense of a command (هَا، رُوَيْدَ، هَلُمَّ، هَاتِ، حَيَّهَلَ، بَلْهَ، عَلَيْكَ، دُونَكَ، تَرَاكِ) or of a past verb (هَيْهَاتَ، شَتَّانَ، سَرْعَانَ، وَشْكَانَ); they govern as their named verb does and their governed word never precedes them. Of it is the settled ẓarf, which never governs the direct object and raises a manifest doer only when it leans on what was mentioned or on the relative pronoun (زَيْدٌ فِي الدَّارِ أَبُوهُ، مَا فِي الدَّارِ أَحَدٌ، جَاءَ الَّذِي فِي الدَّارِ أَبُوهُ); it may be a fronted khabar; without a manifest doer its doer is a pronoun concealed in it and moved from its dropped mutaʿallaq; the ḥāl and the ẓarf it governs without condition. Of it is the nisba noun, governing as the ism mafʿūl does under its conditions (مَرَرْتُ بِرَجُلٍ هَاشِمِيٍّ أَخُوهُ); the borrowed noun (أَسَدٌ غُلَامُهُ; أَسَدٌ عَلَيَّ = مُجْتَرِئٌ, hence it governs عَلَى); every noun with a ṣifa's sense (لَفْظُ اللهِ in al-Anʿām 3 = الْمَعْبُودُ فِيهَا); and the demonstrative, لَيْتَ، لَعَلَّ and the letters of calling, likening, alerting and negation, which govern only the ḥāl and the ẓarf among the verb's governed words.",
                 "tr": "Dokuzuncu kıyâsî âmil mana-yı fiildir — kendisinden bir fiil mânâsı anlaşılan her lafız. Bundan isim fiillerdir: emir mânâlı (hâ, ruveyde, helümme, hâti, hayyehele, belhe, aleyke, dûneke, terâki) veya mâzî mânâlı (heyhâte, şettâne, ser'âne, veşkâne); müsemmâları gibi amel ederler ve ma'mûlleri asla önlerine geçmez. Bundan zarf-ı müstakardır: mef'ûlün bihte asla amel etmez, zâhir fâili ancak zikredilenlere veya mevsûle dayanınca ref' eder (Zeydün fi'd-dâri ebûhu, mâ fi'd-dâri ehadün, câe'llezî fi'd-dâri ebûhu); öne alınmış haber olabilir; zâhir fâili yoksa fâili, hazfedilmiş müteallaktan geçmiş gizli bir zamirdir; hâl ve zarfta şartsız amel eder. Bundan mensûb isimdir: ism-i mef'ûl gibi, onun şartlarıyla amel eder (merartü bi-racülin Hâşimiyyin ehûhu); müsteâr isimdir (esedün gulâmuhu; esedün aleyye = müctéri', bu yüzden alâ'da amel eder); sıfat mânâsı anlaşılan her isimdir (En'âm 3'teki Allah lafzı = el-ma'bûdü fîhâ); ve ism-i işâret, leyte, lealle ile nidâ, teşbîh, tenbîh ve nefiy harfleridir — fiilin ma'mûllerinden yalnız hâl ve zarfta amel ederler."},
 "examples": [
  {"ar": "هَا زَيْدًا أَيْ خُذْهُ", "en": "a command noun-verb with its object", "tr": "mef'ûlüyle emir isim fiili", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "حَيَّهَلَ الثَّرِيدَ أَيِ ائْتِهِ", "en": "the compound noun-verb", "tr": "mürekkeb isim fiil", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "هَيْهَاتَ الْأَمْرُ أَيْ بَعُدَ", "en": "a past-sense noun-verb with its doer", "tr": "fâiliyle mâzî mânâlı isim fiil", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "شَتَّانَ زَيْدٌ وَعَمْرٌو أَيِ افْتَرَقَا", "en": "shattāna with its two doers", "tr": "iki fâiliyle şettâne", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "زَيْدٌ فِي الدَّارِ أَبُوهُ", "en": "the settled ẓarf raises a manifest doer after leaning on the mubtada", "tr": "zarf-ı müstakar mübtedâya dayanıp zâhir fâil ref' eder", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "مَا فِي الدَّارِ أَحَدٌ", "en": "leaning on the negation", "tr": "nefye dayanarak", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "جَاءَ الَّذِي فِي الدَّارِ أَبُوهُ", "en": "leaning on the relative pronoun", "tr": "mevsûle dayanarak", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "مَرَرْتُ بِرَجُلٍ هَاشِمِيٍّ أَخُوهُ", "en": "the nisba noun raises «his brother» as the ism mafʿūl would", "tr": "mensûb isim «kardeşi»ni ism-i mef'ûl gibi ref' eder", "sourceStory": "izhar-al-asrar", "sentence": "s9"},
  {"ar": "مَرَرْتُ بِرَجُلٍ أَسَدٍ غُلَامُهُ", "en": "the borrowed noun raises «his servant»", "tr": "müsteâr isim «kölesi»ni ref' eder", "sourceStory": "izhar-al-asrar", "sentence": "s10"},
  {"ar": "وَهُوَ اللهُ فِي السَّمٰوَاتِ", "en": "the word «God» = «the worshipped», governing the ẓarf (al-Anʿām 3)", "tr": "Allah lafzı = «ma'bûd», zarfta amel eder (En'âm 3)", "sourceStory": "izhar-al-asrar", "sentence": "s11"},
 ],
 "commonMistakes": [
  {"wrong": "زَيْدًا هَا", "right": "هَا زَيْدًا", "why": {"en": "the governed word of a noun-verb never precedes it", "tr": "isim fiilin ma'mûlü asla onun önüne geçmez"}},
  {"wrong": "هَيْهَاتَ الْأَمْرَ", "right": "هَيْهَاتَ الْأَمْرُ", "why": {"en": "a past-sense noun-verb raises a doer; it takes no object", "tr": "mâzî mânâlı isim fiil fâil ref' eder; mef'ûl almaz"}},
  {"wrong": "زَيْدٌ فِي الدَّارِ أَبَاهُ", "right": "زَيْدٌ فِي الدَّارِ أَبُوهُ", "why": {"en": "the settled ẓarf raises a doer; it never governs an object", "tr": "zarf-ı müstakar fâil ref' eder; mef'ûlde asla amel etmez"}},
  {"wrong": "مَرَرْتُ بِرَجُلٍ هَاشِمِيٍّ أَخِيهِ", "right": "مَرَرْتُ بِرَجُلٍ هَاشِمِيٍّ أَخُوهُ", "why": {"en": "«his brother» is the doer the nisba noun raises, not a second majrūr", "tr": "«kardeşi» mensûbun ref' ettiği fâildir, ikinci bir mecrûr değil"}},
 ],
}
ADD_EN = (" Chapter 16 (print pp. 113-115): the ninth governor, the sense of the verb (s1); the noun-verbs, their definition and two rules (s2), the command kind (s3-s4) and the past kind (s5); the settled ẓarf — no object, the manifest doer only on leaning (s6) with its three examples (s7), the fronted khabar, the concealed doer, the ḥāl and the ẓarf without condition (s8); "
          "the nisba noun (s9), the borrowed noun (s10), every noun with a ṣifa's sense and al-Anʿām 6:3 as the print sets it (s11), the demonstrative, لَيْتَ، لَعَلَّ and the letters of calling, likening, alerting and negation (s12). The transcription's «إلا ما ذكر» (p. 114) is printed as the standard «على ما ذكر», which the three examples require, and flagged in the iʿrāb.")
ADD_TR = (" On altıncı bab (baskı s. 113-115): dokuzuncu âmil mana-yı fiil (s1); isim fiiller, tarifi ve iki kuralı (s2), emir kısmı (s3-s4) ve mâzî kısmı (s5); zarf-ı müstakar — mef'ûl yok, zâhir fâil ancak i'timâdla (s6), üç örneği (s7), öne alınmış haber, gizli fâil, şartsız hâl ve zarf (s8); "
          "mensûb isim (s9), müsteâr isim (s10), sıfat mânâlı her isim ve baskının verdiği şekliyle En'âm 6:3 (s11), ism-i işâret, leyte, lealle ile nidâ, teşbîh, tenbîh ve nefiy harfleri (s12). Transkripsiyonun «إلا ما ذكر»ı (s. 114) üç örneğin gerektirdiği standart «على ما ذكر» olarak basıldı ve i'râbda işaretlendi.")
write_out(16, S, TITLE, ADD_EN, ADD_TR, "pp. 113-115", GLOSS_ADD, notes=(NOTE,),
          related=((IFL, [K]), (MNF, [K]), (ZM, [K]), (NSB, [K]), (IST, [K]), (K15, [K]), (HL, [K]), (ISH, [K]), (TNB, [K])))
report(16, S, GLOSS_ADD, (NOTE,))
