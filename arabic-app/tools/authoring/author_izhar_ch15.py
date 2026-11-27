# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 15: the eighth QIYĀSĪ governor — the COMPLETE VAGUE NOUN (الِاسْمُ الْمُبْهَمُ التَّامُّ), which puts an
# indefinite noun in naṣb as a TAMYĪZ. Its completeness — its being in a state in which annexation is impossible — comes by one of
# five things: by itself (the vague pronoun: رُبَّهُ رَجُلًا، يَا لَهُ رَجُلًا، نِعْمَ رَجُلًا; the demonstrative: مَاذَا أَرَادَ اللهُ بِهٰذَا مَثَلًا);
# by the tanwīn — spoken (رِطْلٌ زَيْتًا) or estimated (مِثْقَالُ ذَهَبًا، أَحَدَ عَشَرَ رَجُلًا) — with the counted nouns' rules: three to ten
# take a plural in jarr (ثَلَاثَةُ رِجَالٍ) save three hundred to nine hundred, eleven to ninety-nine a singular in naṣb always, a hundred and
# a thousand with their dual and plural a singular in jarr (مِائَةُ رَجُلٍ، أَلْفُ دِرْهَمٍ); by the nūn of the dual (مَنَوَانِ سَمْنًا — and in
# some of these two kinds annexation is allowed: رِطْلُ زَيْتٍ، مَنَوَا سَمْنٍ); by the nūn resembling the plural's, twenty to ninety
# (عِشْرُونَ دِرْهَمًا); and by annexation (مِلْؤُهُ عَسَلًا). The governed word of the complete noun does not precede it. Print pp. 111–113.
#   python3 author_izhar_ch15.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-ism-al-mubham-al-tamm"
K14 = "al-mudaf-wa-nawa-al-idafa"
TITLE = {"ar": "الِاسْمُ الْمُبْهَمُ التَّامُّ وَالتَّمْيِيزُ", "en": "The complete vague noun and the tamyīz", "tr": "Mübhem tâm isim ve temyiz"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; AM = "an-masdariyya"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
TM = "tamyiz"; HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; MSD = "masdar"; LN = "la-nafiya"; IN = "inna-wa-akhawatuha"; BD = "badal"; JT = "jam-taksir"; JMS = "jam-mudhakkar-salim"; MST = "istithna"; ISH = "asma-al-ishara"; NM = "nima-verb-note" if False else "al-lazim-wal-mutaaddi"; MQ = "ism-maqsur-manqus"; RB = "huruf-jarr-nawadir"; ND = "vocative-munada"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«… gibi» — hazfedilmiş mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def tamyiz(form, lex, en, tr, punct=None, tags=(), pos="noun"): return tok(form, lex, pos, [K, TM] + list(tags), "تَمْيِيزٌ مَنْصُوبٌ — لِلِاسْمِ الْمُبْهَمِ التَّامِّ قَبْلَهُ.", en, tr, punct=punct)
def mumayyiz(form, lex, en, tr, punct=None, tags=(), role_ar="لَفْظٌ مَحْكِيٌّ: الِاسْمُ الْمُبْهَمُ التَّامُّ — مُبْتَدَأٌ مَرْفُوعٌ", segments=None, pos="noun"): return tok(form, lex, pos, [K, TM, HT] + list(tags), role_ar + ".", en, tr, punct=punct, segments=segments)
def wa_nun(form, lex, en, tr, punct=None): return tok(form, lex, "noun", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَ" + "بِ" + "… — الْبَاءُ حَرْفُ جَرٍّ، وَالِاسْمُ مَجْرُورٌ، مُضَافٌ — مَعْطُوفٌ عَلَى بِنَفْسِهِ.", en, tr, punct=punct)

# ----------- s1 — the eighth: the complete vague noun
S.append({"id": "s1", "translation": {"en": "And the eighth is the COMPLETE VAGUE NOUN, for it puts an indefinite noun in naṣb as a TAMYĪZ.", "tr": "Sekizincisi MÜBHEM TÂM İSİM'dir; çünkü nekre bir ismi TEMYİZ olarak nasb eder."},
 "tokens": [
  tok("وَالثَّامِنُ", "thamin-eighth", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّامِنُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the eighth» — the mubtada.", "«sekizincisi» — mübtedâ.", segments=wa("الثَّامِنُ", "thamin-eighth", "noun")),
  tok("الِاسْمُ", "ism", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the noun» — the khabar.", "«isim» — haber."),
  tok("الْمُبْهَمُ", "mubham", "noun", [K, NA, IMF, TM], "نَعْتٌ مَرْفُوعٌ — الْمُبْهَمُ: مَا احْتَاجَ إِلَى تَفْسِيرٍ.", "«vague» — a naʿt: what needs explaining.", "«mübhem» — na't: açıklamaya muhtaç olan."),
  tok("التَّامُّ", "tamm", "noun", [K, NA, TM], "نَعْتٌ ثَانٍ مَرْفُوعٌ — التَّامُّ: مَا امْتَنَعَتْ إِضَافَتُهُ.", "«complete» — a second naʿt: what cannot be annexed.", "«tâm» — ikinci na't: izâfeti mümkün olmayan.", punct="،"),
  tok("فَإِنَّهُ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«for it» — inna with its pronoun ism.", "«çünkü o» — inne, zamir ismi.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("يَنْصِبُ", "nasaba-nahw", "verb", [K, IN, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«puts in naṣb» — the khabar of inna.", "«nasb eder» — inne'nin haberi."),
  tok("اسْمًا", "ism", "noun", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a noun» — the object.", "«bir isim» — mef'ûl."),
  tok("نَكِرَةً", "nakira", "noun", [K, NA, TM], "نَعْتٌ مَنْصُوبٌ.", "«indefinite» — a naʿt.", "«nekre» — na't."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«as»", "«olarak»"),
  tok("التَّمْيِيزِ", "tamyiz-noun", "noun", [K, HJ, TM, MSD], "مَجْرُورٌ بِعَلَى — عَلَى أَنَّهُ تَمْيِيزٌ.", "«the tamyīz» — as a specifier.", "«temyiz» — temyiz olarak.", punct="."),
 ]})
# ----------- s2 — its completeness by one of five things; by itself: the pronoun and the demonstrative
S.append({"id": "s2", "translation": {"en": "And its completeness — that is, its being in a state in which its annexation is impossible — is by one of five things: by itself, and that is in the vague pronoun, as in «many a one — a man!», «what a man he is!», «how excellent a man!», and in the demonstrative, as in His word: «what did God intend by this as a likeness?».", "tr": "Tamlığı — yani izâfetinin mümkün olmadığı bir hâlde bulunması — beş şeyden biriyledir: kendisiyle, ki bu mübhem zamirdedir — «nice adam!», «ne adam o!», «ne iyi adam!» gibi — ve ism-i işârettedir — Allah'ın «Allah bununla misal olarak ne murâd etti?» sözündeki gibi."},
 "tokens": [
  tok("وَتَمَامُهُ", "tamam", "noun", [K, AT, MK, ID, MSD], "الْوَاوُ لِلِاسْتِئْنَافِ، وَتَمَامُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its completeness» — the mubtada.", "«ve tamlığı» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("تَمَامُ", "tamam", "noun"), pr3ms()]),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»"),
  tok("كَوْنُهُ", "kawn", "noun", [K, BD, ID, MSD], "بَدَلٌ مِنْ تَمَامُهُ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ كَانَ.", "«its being» — a badal of «its completeness».", "«olması» — tamâmühu'nun bedeli.", segments=[seg("كَوْنُ", "kawn", "noun"), pr3ms()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ — مُتَعَلِّقٌ بِكَوْنُهُ.", "«in»", "«-de»"),
  tok("حَالَةٍ", "hala-condition", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«a state»", "«bir hâlde»"),
  tok("يَمْتَنِعُ", "imtanaa", "verb", [K, NA, FL, "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ نَعْتٌ لِحَالَةٍ.", "«is impossible» — the ṣifa clause of «a state».", "«mümkün olmaz» — hâletin'in sıfat cümlesi."),
  tok("إِضَافَتُهُ", "idafa", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its annexation» — the doer.", "«izâfeti» — fâil.", segments=[seg("إِضَافَتُ", "idafa", "noun"), pr3ms()]),
  tok("مَعَهَا", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — مَعَ تِلْكَ الْحَالَةِ.", "«with it» — in that state.", "«onunla» — o hâlde.", segments=[seg("مَعَ", "maa", "noun"), pr3fs()]),
  tok("بِأَحَدِ", "ahad", "noun", [K, HJ, ID, MK], "الْبَاءُ حَرْفُ جَرٍّ، وَأَحَدِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ الْمُبْتَدَإِ.", "«by one of» — the khabar.", "«… biriyle» — haber.", segments=[seg("بِ", "bi", "prep"), seg("أَحَدِ", "ahad", "noun")]),
  tok("خَمْسَةِ", "khamsa", "noun", [K, ID, TM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«five»", "«beş»"),
  tok("أَشْيَاءَ", "shay", "noun", [K, ID, JT, "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — جَمْعُ شَيْءٍ.", "«things» — the diptote plural.", "«şey» — gayr-i munsarif çoğul.", punct=":"),
  tok("بِنَفْسِهِ", "nafs", "noun", [K, HJ, ID, BD], "الْبَاءُ حَرْفُ جَرٍّ، وَنَفْسِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — بَدَلُ تَفْصِيلٍ مِنْ بِأَحَدِ: الْأَوَّلُ.", "«by itself» — the first of the five.", "«kendisiyle» — beşin ilki.", segments=[seg("بِ", "bi", "prep"), seg("نَفْسِ", "nafs", "noun"), pr3msi()]),
  tok("وَذٰلِكَ", "dhalika", "pron", [K, AT, MK, ISH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that» — the mubtada.", "«ve bu» — mübtedâ.", segments=wa("ذٰلِكَ", "dhalika", "pron")),
  tok("فِي", "fi", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in» — the khabar.", "«-de» — haber."),
  tok("الضَّمِيرِ", "damir", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the pronoun»", "«zamirde»"),
  tok("الْمُبْهَمِ", "mubham", "noun", [K, NA, TM], "نَعْتٌ مَجْرُورٌ — ضَمِيرُ الْمَجْهُولِ الَّذِي يُفَسِّرُهُ التَّمْيِيزُ.", "«vague» — the pronoun the tamyīz explains.", "«mübhem» — temyizin açıkladığı zamir.", punct="،"),
  nahw(),
  mumayyiz("رُبَّهُ", "rubba", "«many a one» — rubba with its vague pronoun: the complete noun.", "«nice» — rubbe mübhem zamiriyle: tâm isim.", tags=[RB], role_ar="لَفْظٌ مَحْكِيٌّ: رُبَّ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُبْهَمٌ مَجْرُورٌ — وَهُوَ الِاسْمُ الْمُبْهَمُ التَّامُّ", segments=[seg("رُبَّ", "rubba", "part"), pr3ms()], pos="part"),
  tamyiz("رَجُلًا", "rajul", "«a man» — the tamyīz of the pronoun.", "«adam» — zamirin temyizi."),
  mumayyiz("وَيَا", "ya-nida", "«and O …» — the exclamation.", "«ve ey» — nidâ.", role_ar="الْوَاوُ عَاطِفَةٌ، وَيَا حَرْفُ نِدَاءٍ وَتَعَجُّبٍ — لَفْظٌ مَحْكِيٌّ", segments=wa("يَا", "ya-nida", "part"), pos="part", tags=[ND]),
  mumayyiz("لَهُ", "lahu", "«what a … he is» — the lām with the vague pronoun: the complete noun.", "«ne …dir o» — lâm mübhem zamirle: tâm isim.", role_ar="اللَّامُ حَرْفُ جَرٍّ لِلتَّعَجُّبِ، وَالْهَاءُ ضَمِيرٌ مُبْهَمٌ مَجْرُورٌ — الِاسْمُ الْمُبْهَمُ التَّامُّ", segments=[seg("لِ", "li", "prep"), pr3ms()], pos="part"),
  tamyiz("رَجُلًا", "rajul", "«a man» — the tamyīz.", "«adam» — temyiz."),
  mumayyiz("وَنِعْمَ", "nima-verb", "«and how excellent» — the praise verb with its concealed vague doer.", "«ve ne iyi» — gizli mübhem fâilli medih fiili.", role_ar="الْوَاوُ عَاطِفَةٌ، وَنِعْمَ فِعْلُ مَدْحٍ جَامِدٌ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ مُبْهَمٌ — الِاسْمُ الْمُبْهَمُ التَّامُّ", segments=wa("نِعْمَ", "nima-verb", "verb"), pos="verb", tags=[NM]),
  tamyiz("رَجُلًا", "rajul", "«a man» — the tamyīz of the concealed doer.", "«adam» — gizli fâilin temyizi."),
  tok("وَفِي", "fi", "prep", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى فِي الضَّمِيرِ.", "«and in»", "«ve … -de»", segments=wa("فِي", "fi", "prep")),
  tok("اسْمِ", "ism", "noun", [K, HJ, ID, ISH], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the noun of»", "«ism-i»"),
  tok("الْإِشَارَةِ", "ishara", "noun", [K, ID, ISH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْإِشَارَةِ.", "«pointing» — the demonstrative.", "«işâret» — ism-i işâret.", punct="،"),
  tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ.", "«as in»", "«… gibi»"),
  tok("قَوْلِهِ", "qawl", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His word»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("تَعَالَى", "taala", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.", "«Most High»", "«Teâlâ»", punct=":"),
  mumayyiz("مَاذَا", "madha", "«what» — the question noun, the object of «intended».", "«ne» — soru ismi, murâd etti'nin mef'ûlü.", role_ar="لَفْظٌ مَحْكِيٌّ (مِنَ الْقُرْآنِ، الْبَقَرَة ٢٦): اسْمُ اسْتِفْهَامٍ مَفْعُولٌ بِهِ مُقَدَّمٌ فِي مَحَلِّ نَصْبٍ", pos="pron", tags=["al-istifham", "al-iqtibas-wal-tadmin"]),
  tok("أَرَادَ", "arada", "verb", [K, FL, F4, HV, "al-iqtibas-wal-tadmin"], "فِعْلٌ مَاضٍ.", "«intended»", "«murâd etti»"),
  tok("اللهُ", "allah", "propn", [K, FL, "al-iqtibas-wal-tadmin"], "فَاعِلٌ مَرْفُوعٌ.", "«God» — the doer.", "«Allah» — fâil."),
  mumayyiz("بِهٰذَا", "hadha", "«by this» — the demonstrative: the complete vague noun.", "«bununla» — ism-i işâret: mübhem tâm isim.", role_ar="الْبَاءُ حَرْفُ جَرٍّ، وَهٰذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — الِاسْمُ الْمُبْهَمُ التَّامُّ", segments=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")], pos="pron", tags=[ISH, "al-iqtibas-wal-tadmin"]),
  tamyiz("مَثَلًا", "mathal", "«as a likeness» — the tamyīz of the demonstrative.", "«misal olarak» — ism-i işâretin temyizi.", punct=".", tags=["al-iqtibas-wal-tadmin"]),
 ]})
# ----------- s3 — by the tanwīn, spoken or estimated
S.append({"id": "s3", "translation": {"en": "And by the tanwīn — either spoken, as in «a pound of oil», or estimated, as in «a mithqāl of gold» and «eleven men».", "tr": "Ve tenvinle — ya lafzen, «bir rıtl zeytinyağı» gibi; ya takdiren, «bir miskal altın» ve «on bir adam» gibi."},
 "tokens": [
  tok("وَبِالتَّنْوِينِ", "tanwin", "noun", [K, AT, HJ, BD], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَالتَّنْوِينِ مَجْرُورٌ — مَعْطُوفٌ عَلَى بِنَفْسِهِ: الثَّانِي.", "«and by the tanwīn» — the second of the five.", "«ve tenvinle» — ikincisi.", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("التَّنْوِينِ", "tanwin", "noun")]),
  tok("إِمَّا", "imma", "part", [K, AT], "حَرْفُ تَفْصِيلٍ.", "«either»", "«ya»"),
  tok("لَفْظًا", "lafz", "noun", [K, HL], "حَالٌ مَنْصُوبٌ (أَوْ تَمْيِيزٌ) — مَلْفُوظًا.", "«spoken» — a ḥāl.", "«lafzen» — hâl."),
  nahw(),
  mumayyiz("رِطْلٌ", "ritl", "«a pound» — the measure with its spoken tanwīn: complete.", "«bir rıtl» — lafzî tenvinli ölçü: tâm.", role_ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ (أَوْ خَبَرٌ لِمَحْذُوفٍ) — تَنْوِينُهُ لَفْظِيٌّ، وَبِهِ تَمَامُهُ"),
  tamyiz("زَيْتًا", "zayt", "«of oil» — the tamyīz.", "«zeytinyağı» — temyiz."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("تَقْدِيرًا", "taqdir", "noun", [K, HL, AT], "مَعْطُوفٌ عَلَى لَفْظًا مَنْصُوبٌ — مُقَدَّرًا.", "«estimated»", "«takdiren»"),
  nahw(),
  mumayyiz("مِثْقَالُ", "mithqal", "«a mithqāl» — its tanwīn estimated (the print: مثقال ذهبا).", "«bir miskal» — tenvini takdirî.", role_ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ — تَنْوِينُهُ مُقَدَّرٌ عِنْدَ الْمُصَنِّفِ"),
  tamyiz("ذَهَبًا", "dhahab-gold", "«of gold» — the tamyīz.", "«altın» — temyiz."),
  mumayyiz("وَأَحَدَ", "ahada-ashar", "«and eleven» — the compound number built on the fatḥa, its tanwīn estimated.", "«ve on bir» — fetha üzere mebnî mürekkeb sayı, tenvini takdirî.", role_ar="الْوَاوُ عَاطِفَةٌ، وَأَحَدَ عَشَرَ لَفْظٌ مَحْكِيٌّ: مَعْطُوفٌ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ رَفْعٍ — تَنْوِينُهُ مُقَدَّرٌ", segments=wa("أَحَدَ", "ahada-ashar", "noun"), tags=["al-murab-wal-mabni-wal-irab"]),
  tok("عَشَرَ", "ashar", "noun", [K, TM, "al-murab-wal-mabni-wal-irab"], "الْجُزْءُ الثَّانِي مِنَ الْمُرَكَّبِ، مَبْنِيٌّ عَلَى الْفَتْحِ.", "«-teen» — the second half, built on the fatḥa.", "«on» — mürekkebin ikinci yarısı, fetha üzere mebnî."),
  tamyiz("رَجُلًا", "rajul", "«men» — the tamyīz of the number: a singular.", "«adam» — sayının temyizi: müfred.", punct="."),
 ]})
# ----------- s4 — the counted nouns' rules
S.append({"id": "s4", "translation": {"en": "And the specifier of three to ten is not put in naṣb; rather it is in jarr and plural, as in «three men» — except in three hundred to nine hundred; the specifier of eleven to ninety-nine is in naṣb and singular always; and the specifier of a hundred and a thousand, and their duals and plurals, is not put in naṣb; rather it is in jarr and singular, as in «a hundred men», «a thousand dirhams».", "tr": "Üçten ona kadarın temyizi nasb edilmez; mecrûr ve çoğuldur, «üç adam» gibi — üç yüzden dokuz yüze kadar hariç; on birden doksan dokuza kadarın temyizi daima mansûb ve müfreddir; yüz ve binin, tesniye ve cem'lerinin temyizi nasb edilmez; mecrûr ve müfreddir, «yüz adam», «bin dirhem» gibi."},
 "tokens": [
  tok("وَمُمَيِّزُ", "mumayyiz", "noun", [K, AT, MK, ID, TM], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمُمَيِّزُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — التَّمْيِيزُ.", "«and the specifier of» — the mubtada.", "«ve … temyizi» — mübtedâ.", segments=wa("مُمَيِّزُ", "mumayyiz", "noun")),
  tok("ثَلَاثَةٍ", "thalatha", "noun", [K, ID, HT, TM], "لَفْظٌ مَحْكِيٌّ: مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«three»", "«üç»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e kadar»"),
  tok("عَشَرَةٍ", "ashara", "noun", [K, HJ, HT, TM], "لَفْظٌ مَحْكِيٌّ: مَجْرُورٌ بِإِلَى.", "«ten»", "«on»"),
  tok("لَا", "la-nafiya", "part", [K, LN], "نَافِيَةٌ.", "«not»", "«-mez»"),
  tok("يُنْصَبُ", "nasaba-nahw", "verb", [K, MK, NF], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«is put in naṣb» — the khabar clause.", "«nasb edilir» — haber cümlesi."),
  tok("بَلْ", "bal", "part", [K, AT], "حَرْفُ إِضْرَابٍ.", "«rather»", "«bilakis»"),
  tok("هُوَ", "huwa", "pron", [K, MK], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«it» — the mubtada.", "«o» — mübtedâ."),
  tok("مَجْرُورٌ", "majrur", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«in jarr» — the khabar.", "«mecrûr» — haber."),
  tok("وَمَجْمُوعٌ", "majmu", "noun", [K, AT, IMF], "الْوَاوُ عَاطِفَةٌ، وَمَجْمُوعٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and plural»", "«ve çoğul»", punct="،", segments=wa("مَجْمُوعٌ", "majmu", "noun")),
  nahw(),
  mumayyiz("ثَلَاثَةُ", "thalatha", "«three» — annexed to its plural specifier.", "«üç» — çoğul temyizine muzâf.", role_ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ"),
  tok("رِجَالٍ", "rajul", "noun", [K, ID, TM, JT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعٌ: تَمْيِيزُ الثَّلَاثَةِ إِلَى الْعَشَرَةِ.", "«men» — the plural in jarr.", "«adam» — mecrûr çoğul."),
  tok("إِلَّا", "illa", "part", [K, MST], "أَدَاةُ اسْتِثْنَاءٍ.", "«except»", "«hariç»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("ثَلَاثِمِائَةٍ", "thalathumia", "noun", [K, HJ, HT, TM], "لَفْظٌ مَحْكِيٌّ: مَجْرُورٌ بِفِي — مُرَكَّبٌ إِضَافِيٌّ.", "«three hundred»", "«üç yüz»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e kadar»"),
  tok("تِسْعِمِائَةٍ", "tisumia", "noun", [K, HJ, HT, TM], "لَفْظٌ مَحْكِيٌّ: مَجْرُورٌ بِإِلَى.", "«nine hundred»", "«dokuz yüz»", punct="،"),
  tok("وَمُمَيِّزُ", "mumayyiz", "noun", [K, AT, MK, ID, TM], "الْوَاوُ عَاطِفَةٌ، وَمُمَيِّزُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the specifier of»", "«ve … temyizi»", segments=wa("مُمَيِّزُ", "mumayyiz", "noun")),
  tok("أَحَدَ", "ahada-ashar", "noun", [K, ID, HT, TM, "al-murab-wal-mabni-wal-irab"], "لَفْظٌ مَحْكِيٌّ: مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ جَرٍّ.", "«eleven»", "«on bir»"),
  tok("عَشَرَ", "ashar", "noun", [K, TM, "al-murab-wal-mabni-wal-irab"], "الْجُزْءُ الثَّانِي، مَبْنِيٌّ عَلَى الْفَتْحِ.", "«-teen»", "«on»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e kadar»"),
  tok("تِسْعٍ", "tis", "noun", [K, HJ, HT, TM], "لَفْظٌ مَحْكِيٌّ: مَجْرُورٌ بِإِلَى.", "«nine»", "«dokuz»"),
  tok("وَتِسْعِينَ", "tisun", "noun", [K, AT, HT, TM, JMS], "الْوَاوُ عَاطِفَةٌ، وَتِسْعِينَ مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«and ninety» — jarr by the yāʾ.", "«ve doksan» — yâ ile mecrûr.", segments=wa("تِسْعِينَ", "tisun", "noun")),
  tok("مَنْصُوبٌ", "mansub", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«in naṣb» — the khabar.", "«mansûb» — haber."),
  tok("مُفْرَدٌ", "mufrad", "noun", [K, MK], "خَبَرٌ ثَانٍ مَرْفُوعٌ.", "«singular»", "«müfred»"),
  tok("دَائِمًا", "daiman", "noun", [K, HL], "حَالٌ (أَوْ ظَرْفٌ) مَنْصُوبٌ.", "«always»", "«daima»", punct="،"),
  tok("وَمُمَيِّزُ", "mumayyiz", "noun", [K, AT, MK, ID, TM], "الْوَاوُ عَاطِفَةٌ، وَمُمَيِّزُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the specifier of»", "«ve … temyizi»", segments=wa("مُمَيِّزُ", "mumayyiz", "noun")),
  tok("مِائَةٍ", "mia", "noun", [K, ID, HT, TM], "لَفْظٌ مَحْكِيٌّ: مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a hundred»", "«yüz»"),
  tok("وَأَلْفٍ", "alf", "noun", [K, AT, HT, TM], "الْوَاوُ عَاطِفَةٌ، وَأَلْفٍ مَعْطُوفٌ مَجْرُورٌ.", "«and a thousand»", "«ve bin»", segments=wa("أَلْفٍ", "alf", "noun")),
  tok("وَتَثْنِيَتِهِمَا", "tathniya", "noun", [K, AT, ID, MTH], "الْوَاوُ عَاطِفَةٌ، وَتَثْنِيَتِهِمَا مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«and their duals»", "«ve tesniyeleri»", segments=[seg("وَ", "wa", "conj"), seg("تَثْنِيَتِ", "tathniya", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("وَجَمْعِهِمَا", "jam", "noun", [K, AT, ID, JT], "الْوَاوُ عَاطِفَةٌ، وَجَمْعِهِمَا مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«and their plurals»", "«ve cem'leri»", segments=[seg("وَ", "wa", "conj"), seg("جَمْعِ", "jam", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("لَا", "la-nafiya", "part", [K, LN], "نَافِيَةٌ.", "«not»", "«-mez»"),
  tok("يُنْصَبُ", "nasaba-nahw", "verb", [K, MK, NF], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرٌ.", "«is put in naṣb» — the khabar clause.", "«nasb edilir» — haber cümlesi."),
  tok("بَلْ", "bal", "part", [K, AT], "حَرْفُ إِضْرَابٍ.", "«rather»", "«bilakis»"),
  tok("هُوَ", "huwa", "pron", [K, MK], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«it»", "«o»"),
  tok("مَجْرُورٌ", "majrur", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«in jarr»", "«mecrûr»"),
  tok("مُفْرَدٌ", "mufrad", "noun", [K, MK], "خَبَرٌ ثَانٍ مَرْفُوعٌ.", "«singular»", "«müfred»", punct="،"),
  nahw(),
  mumayyiz("مِائَةُ", "mia", "«a hundred» — annexed to a singular.", "«yüz» — müfrede muzâf.", role_ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ"),
  tok("رَجُلٍ", "rajul", "noun", [K, ID, TM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مُفْرَدٌ.", "«men» — a singular in jarr.", "«adam» — mecrûr müfred."),
  mumayyiz("وَأَلْفُ", "alf", "«and a thousand»", "«ve bin»", role_ar="الْوَاوُ عَاطِفَةٌ، وَأَلْفُ لَفْظٌ مَحْكِيٌّ: مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ", segments=wa("أَلْفُ", "alf", "noun")),
  tok("دِرْهَمٍ", "dirham", "noun", [K, ID, TM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مُفْرَدٌ.", "«dirhams» — a singular in jarr.", "«dirhem» — mecrûr müfred.", punct="."),
 ]})
# ----------- s5 — by the nūn of the dual; annexation allowed in two kinds
S.append({"id": "s5", "translation": {"en": "And by the nūn of the dual, as in «two manns of clarified butter»; and in some of these two kinds annexation is allowed, as in «a pound of oil», «two manns of butter» — and it is not allowed in the others.", "tr": "Ve tesniye nûnuyla, «iki men sadeyağ» gibi; bu iki kısmın bazısında izâfet câizdir, «bir rıtl zeytinyağı», «iki men sadeyağ» gibi — başkalarında câiz değildir."},
 "tokens": [
  tok("وَبِنُونِ", "nun-letter", "noun", [K, AT, HJ, ID, BD, MTH], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَنُونِ مَجْرُورٌ، مُضَافٌ — مَعْطُوفٌ عَلَى بِنَفْسِهِ: الثَّالِثُ.", "«and by the nūn of» — the third of the five.", "«ve … nûnuyla» — üçüncüsü.", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("نُونِ", "nun-letter", "noun")]),
  tok("التَّثْنِيَةِ", "tathniya", "noun", [K, ID, MTH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the dual»", "«tesniye»", punct="،"),
  nahw(),
  mumayyiz("مَنَوَانِ", "mann", "«two manns» — the dual with its nūn: complete.", "«iki men» — nûnlu tesniye: tâm.", role_ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى — نُونُهُ تَمَامُهُ", tags=[MTH]),
  tamyiz("سَمْنًا", "samn", "«of clarified butter» — the tamyīz.", "«sadeyağ» — temyiz."),
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and … is allowed»", "«ve … câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("بَعْضِ", "bad", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«some of»", "«bazısında»"),
  tok("هٰذَيْنِ", "hadhayn", "pron", [K, ID, ISH, MTH], "اسْمُ إِشَارَةٍ لِلْمُثَنَّى مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«these two»", "«bu iki»"),
  tok("الْقِسْمَيْنِ", "qism", "noun", [K, BD, MTH], "بَدَلٌ مِنْ هٰذَيْنِ مَجْرُورٌ بِالْيَاءِ — قِسْمَيِ التَّنْوِينِ وَنُونِ التَّثْنِيَةِ.", "«kinds» — the tanwīn kind and the dual kind.", "«kısımda» — tenvin ve tesniye nûnu kısımları."),
  tok("الْإِضَافَةُ", "idafa", "noun", [K, FL, MSD, K14], "فَاعِلٌ مَرْفُوعٌ.", "«annexation» — the doer.", "«izâfet» — fâil.", punct="،"),
  nahw(),
  mumayyiz("رِطْلُ", "ritl", "«a pound of» — annexed to its specifier.", "«bir rıtl» — temyizine muzâf.", role_ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ"),
  tok("زَيْتٍ", "zayt", "noun", [K, ID, TM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — التَّمْيِيزُ بِالْإِضَافَةِ.", "«oil» — the specifier annexed.", "«zeytinyağı» — izâfetle temyiz."),
  mumayyiz("وَمَنَوَا", "mann", "«and two manns of» — the dual with its nūn dropped for the annexation.", "«ve iki men» — izâfet için nûnu düşmüş tesniye.", role_ar="الْوَاوُ عَاطِفَةٌ، وَمَنَوَا لَفْظٌ مَحْكِيٌّ: مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", segments=wa("مَنَوَا", "mann", "noun"), tags=[MTH]),
  tok("سَمْنٍ", "samn", "noun", [K, ID, TM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«butter»", "«sadeyağ»"),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … değildir»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (ذٰلِكَ).", "«is allowed»", "«câiz»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("غَيْرِهِمَا", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«the others»", "«o ikisinden başkasında»", punct=".", segments=[seg("غَيْرِ", "ghayr", "noun"), seg("هِمَا", "pron-3d", "pron")]),
 ]})
# ----------- s6 — by the nūn resembling the plural's, and by annexation; no fronting
S.append({"id": "s6", "translation": {"en": "And by the nūn that resembles the plural's — and that is twenty to ninety — as in «twenty dirhams»; and by annexation, as in «its fill of honey». And the governed word of the complete noun does not precede it.", "tr": "Ve cem'e benzeyen nûnla — ki yirmiden doksana kadardır — «yirmi dirhem» gibi; ve izâfetle, «bal dolusu» gibi. Tâm ismin ma'mûlü onun önüne geçmez."},
 "tokens": [
  tok("وَبِنُونِ", "nun-letter", "noun", [K, AT, HJ, ID, BD, JMS], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَنُونِ مَجْرُورٌ، مُضَافٌ — الرَّابِعُ.", "«and by the nūn of» — the fourth.", "«ve … nûnuyla» — dördüncüsü.", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("نُونِ", "nun-letter", "noun")]),
  tok("شِبْهِ", "shibh", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the like of»", "«benzeri»"),
  tok("الْجَمْعِ", "jam", "noun", [K, ID, JMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ الْمُذَكَّرِ السَّالِمُ.", "«the plural» — the sound masculine plural.", "«cem'» — cem'-i müzekker sâlim."),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that is» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("عِشْرُونَ", "ishrun", "noun", [K, MK, HT, TM, JMS], "لَفْظٌ مَحْكِيٌّ: خَبَرٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«twenty» — the khabar, rafʿ by the wāw.", "«yirmi» — haber, vâv ile merfû."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e kadar»"),
  tok("تِسْعِينَ", "tisun", "noun", [K, HJ, HT, TM, JMS], "لَفْظٌ مَحْكِيٌّ: مَجْرُورٌ بِالْيَاءِ.", "«ninety»", "«doksan»", punct="،"),
  nahw(),
  mumayyiz("عِشْرُونَ", "ishrun", "«twenty» — complete by its nūn.", "«yirmi» — nûnuyla tâm.", role_ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ — نُونُهُ تَمَامُهُ", tags=[JMS]),
  tamyiz("دِرْهَمًا", "dirham", "«dirhams» — the tamyīz: a singular in naṣb.", "«dirhem» — temyiz: mansûb müfred.", punct="،"),
  tok("وَبِالْإِضَافَةِ", "idafa", "noun", [K, AT, HJ, BD, K14], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَالْإِضَافَةِ مَجْرُورٌ — الْخَامِسُ.", "«and by annexation» — the fifth.", "«ve izâfetle» — beşincisi.", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("الْإِضَافَةِ", "idafa", "noun")]),
  nahw(),
  mumayyiz("مِلْؤُهُ", "mil", "«its fill» — complete by its annexation to the pronoun.", "«dolusu» — zamire izâfetiyle tâm.", role_ar="لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — إِضَافَتُهُ تَمَامُهُ", segments=[seg("مِلْءُ", "mil", "noun"), pr3ms()]),
  tamyiz("عَسَلًا", "asal", "«of honey» — the tamyīz.", "«bal» — temyiz.", punct="."),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَتَقَدَّمُ", "taqaddama", "verb", [K, FL, F5], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«precedes»", "«öne geçer»"),
  tok("مَعْمُولُ", "mamul", "noun", [K, FL, ID, IMF], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the governed word of» — the doer.", "«ma'mûlü» — fâil."),
  tok("الِاسْمِ", "ism", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the noun»", "«ismin»"),
  tok("التَّامِّ", "tamm", "noun", [K, NA, TM], "نَعْتٌ مَجْرُورٌ.", "«complete»", "«tâm»"),
  tok("عَلَيْهِ", "alayhi", "part", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«(before) it»", "«onun önüne»", punct=".", segments=[seg("عَلَى", "ala", "prep"), pr3msi()]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

CAND = {
 "thamin-eighth": G("thamin-eighth", "ثَامِن", "ث م ن", "noun", "eighth", "sekizinci", 2),
 "ism": G("ism", "اِسْم", "س م و", "noun", "noun; name", "isim", 1, plural="أَسْمَاء"),
 "mubham": G("mubham", "مُبْهَم", "ب ه م", "noun", "vague, obscure (needing a specifier)", "mübhem, kapalı (temyize muhtaç)", 3),
 "tamm": G("tamm", "تَامّ", "ت م م", "noun", "complete, tāmm", "tam", 2),
 "inna": G("inna", "إِنَّ", None, "part", "indeed, verily (puts its noun in naṣb)", "muhakkak, şüphesiz (ismini nasb eder)", 1),
 "nasaba-nahw": G("nasaba-nahw", "نَصَبَ", "ن ص ب", "verb", "to put in naṣb (the grammarians' verb)", "nasb etmek (nahivcilerin fiili)", 3),
 "nakira": G("nakira", "نَكِرَة", "ن ك ر", "noun", "an indefinite noun (nakira)", "nekre (belirsiz isim)", 2),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon", "üzerine, -e", 1),
 "tamyiz-noun": G("tamyiz-noun", "تَمْيِيز", "م ي ز", "noun", "the tamyīz — the specifying accusative", "temyiz", 2),
 "tamam": G("tamam", "تَمَام", "ت م م", "noun", "completeness", "tamlık, tamam", 2),
 "ay": G("ay", "أَيْ", None, "part", "that is, i.e. (the explaining particle)", "yani (tefsir harfi)", 2),
 "kawn": G("kawn", "كَوْن", "ك و ن", "noun", "being (the masdar of kāna)", "oluş, olma (kâne'nin mastarı)", 2),
 "hala-condition": G("hala-condition", "حَالَة", "ح و ل", "noun", "state, condition", "hâl, durum", 2),
 "imtanaa": G("imtanaa", "اِمْتَنَعَ", "م ن ع", "verb", "to refuse; to be impossible, to be barred", "imtina etmek; mümkün olmamak, yasak olmak", 3, form="VIII"),
 "idafa": G("idafa", "إِضَافَة", "ض ي ف", "noun", "annexation (iḍāfa, the construct)", "izâfet (isim tamlaması)", 2),
 "maa": G("maa", "مَعَ", None, "noun", "with (a ẓarf)", "ile, birlikte (zarf)", 1),
 "ahad": G("ahad", "أَحَد", "أ ح د", "noun", "one, one of; anyone", "biri, bir; hiç kimse", 1),
 "khamsa": G("khamsa", "خَمْسَة", "خ م س", "noun", "five", "beş", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "thing", "şey", 1, plural="أَشْيَاء"),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "self, soul", "nefis, kendi", 1, plural="أَنْفُس"),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "şu, o", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "damir": G("damir", "ضَمِير", "ض م ر", "noun", "pronoun", "zamir", 2),
 "nahw": G("nahw", "نَحْو", "ن ح و", "noun", "like, such as; grammar", "gibi; nahiv", 2),
 "rubba": G("rubba", "رُبَّ", None, "part", "many a …; sometimes (a jarr letter)", "nice …; bazen (cer harfi)", 3),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam", 1, plural="رِجَال"),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O (the vocative particle)", "ey (nidâ harfi)", 1),
 "lahu": G("lahu", "لَهُ", None, "part", "to him, for him; (in exclamation) what a … he is", "ona, onun için; (hayret) ne …dir o", 1),
 "nima-verb": G("nima-verb", "نِعْمَ", "ن ع م", "verb", "how excellent! (the verb of praise)", "ne iyi! (medih fiili)", 3),
 "ishara": G("ishara", "إِشَارَة", "ش و ر", "noun", "pointing, indication — اسْمُ الْإِشَارَةِ the demonstrative", "işâret — ism-i işâret", 2),
 "qawl": G("qawl", "قَوْل", "ق و ل", "noun", "saying, word", "söz, kavil", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "Most High (of God — «He is exalted»)", "Teâlâ (yücedir)", 1),
 "madha": G("madha", "مَاذَا", None, "pron", "what? (the question noun)", "ne? (soru ismi)", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to intend", "istemek, murâd etmek", 1, form="IV"),
 "allah": G("allah", "اللَّه", None, "propn", "God", "Allah", 1),
 "hadha": G("hadha", "هَذَا", None, "pron", "this", "bu", 1),
 "mathal": G("mathal", "مَثَل", "م ث ل", "noun", "likeness, example, parable", "misal, örnek, mesel", 2),
 "tanwin": G("tanwin", "تَنْوِين", "ن و ن", "noun", "tanwīn (nunation)", "tenvin", 2),
 "imma": G("imma", "إِمَّا", None, "part", "either … (or)", "ya … (ya da)", 2),
 "lafz": G("lafz", "لَفْظ", "ل ف ظ", "noun", "utterance, wording", "lafız", 2),
 "ritl": G("ritl", "رِطْل", "ر ط ل", "noun", "a pound (raṭl, a measure of weight)", "rıtl (bir ağırlık ölçüsü)", 3),
 "zayt": G("zayt", "زَيْت", "ز ي ت", "noun", "oil", "zeytinyağı, yağ", 2),
 "aw": G("aw", "أَوْ", None, "part", "or", "veya", 1),
 "taqdir": G("taqdir", "تَقْدِير", "ق د ر", "noun", "estimation; the supplied reading", "takdir; varsayılan okunuş", 3),
 "mithqal": G("mithqal", "مِثْقَال", "ث ق ل", "noun", "a mithqāl (a measure of weight)", "miskal (bir ağırlık ölçüsü)", 3),
 "dhahab-gold": G("dhahab-gold", "ذَهَب", "ذ ه ب", "noun", "gold", "altın", 1),
 "ahada-ashar": G("ahada-ashar", "أَحَدَ عَشَرَ", "أ ح د", "noun", "eleven (built on the fatḥa of both halves)", "on bir (iki yarısı da fetha üzere mebnî)", 2),
 "ashar": G("ashar", "عَشَرَ", "ع ش ر", "noun", "-teen (the second half of eleven to nineteen)", "on (on bir–on dokuzun ikinci yarısı)", 2),
 "mumayyiz": G("mumayyiz", "مُمَيِّز", "م ي ز", "noun", "the specifier — the word that is explained by a tamyīz; (also) the tamyīz itself in the Iẓhār's usage", "mümeyyiz — temyizle açıklanan; (Izhâr'da) temyizin kendisi", 3),
 "thalatha": G("thalatha", "ثَلَاثَة", "ث ل ث", "noun", "three", "üç", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e, -a", 1),
 "ashara": G("ashara", "عَشَرَة", "ع ش ر", "noun", "ten", "on", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not (negation)", "değil, -mez (nefiy)", 1),
 "bal": G("bal", "بَلْ", None, "part", "rather, nay", "bilakis, hayır", 2),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "majrur": G("majrur", "مَجْرُور", "ج ر ر", "noun", "in the genitive (majrūr)", "mecrûr", 2),
 "majmu": G("majmu", "مَجْمُوع", "ج م ع", "noun", "plural; collected", "cem' hâlinde, toplanmış", 3),
 "illa": G("illa", "إِلَّا", None, "part", "except", "-den başka, hariç", 1),
 "thalathumia": G("thalathumia", "ثَلَاثُمِائَة", "ث ل ث", "noun", "three hundred", "üç yüz", 3),
 "tisumia": G("tisumia", "تِسْعُمِائَة", "ت س ع", "noun", "nine hundred", "dokuz yüz", 3),
 "tis": G("tis", "تِسْع", "ت س ع", "noun", "nine", "dokuz", 2),
 "tisun": G("tisun", "تِسْعُونَ", "ت س ع", "noun", "ninety", "doksan", 2),
 "mansub": G("mansub", "مَنْصُوب", "ن ص ب", "noun", "in the accusative (manṣūb)", "mansûb", 2),
 "mufrad": G("mufrad", "مُفْرَد", "ف ر د", "noun", "singular", "müfred, tekil", 2),
 "daiman": G("daiman", "دَائِمًا", "د و م", "noun", "always", "daima", 1),
 "mia": G("mia", "مِائَة", "م أ ي", "noun", "a hundred", "yüz", 1),
 "alf": G("alf", "أَلْف", "أ ل ف", "noun", "a thousand", "bin", 1, plural="آلَاف"),
 "tathniya": G("tathniya", "تَثْنِيَة", "ث ن ي", "noun", "the dual (making dual)", "tesniye, ikil", 3),
 "jam": G("jam", "جَمْع", "ج م ع", "noun", "plural", "cem', çoğul", 2),
 "dirham": G("dirham", "دِرْهَم", "د ر ه م", "noun", "dirham (a silver coin)", "dirhem", 2, plural="دَرَاهِم"),
 "nun-letter": G("nun-letter", "نُون", None, "noun", "the letter nūn; the nūn (of the dual, of the sound plural)", "nûn harfi; nûn (tesniye, cem' nûnu)", 2),
 "mann": G("mann", "مَنّ", "م ن ن", "noun", "a mann (a measure of weight — two raṭls)", "men (bir ağırlık ölçüsü — iki rıtl)", 4),
 "samn": G("samn", "سَمْن", "س م ن", "noun", "clarified butter", "sadeyağ", 2),
 "jaaza": G("jaaza", "جَازَ", "ج و ز", "verb", "to be permitted", "câiz olmak", 2),
 "bad": G("bad", "بَعْض", "ب ع ض", "noun", "some, part of", "bazı, bir kısmı", 1),
 "hadhayn": G("hadhayn", "هٰذَيْنِ", None, "pron", "these two (the dual demonstrative in naṣb and jarr)", "bu ikisi (nasb ve cerde tesniye ism-i işâreti)", 2),
 "qism": G("qism", "قِسْم", "ق س م", "noun", "division, part", "kısım", 2, plural="أَقْسَام"),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not", "başka, gayr; değil", 1),
 "shibh": G("shibh", "شِبْه", "ش ب ه", "noun", "the like of, quasi-", "benzeri, şibh", 2),
 "ishrun": G("ishrun", "عِشْرُونَ", "ع ش ر", "noun", "twenty", "yirmi", 1),
 "mil": G("mil", "مِلْء", "م ل أ", "noun", "fill, fullness (as much as fills)", "dolusu", 3),
 "asal": G("asal", "عَسَل", "ع س ل", "noun", "honey", "bal", 1),
 "taqaddama": G("taqaddama", "تَقَدَّمَ", "ق د م", "verb", "to precede, to come first", "öne geçmek, önce gelmek", 2, form="V"),
 "mamul": G("mamul", "الْمَعْمُول", "ع م ل", "noun", "the governed word (maʿmūl)", "ma'mûl — amel edilen kelime", 3),
 "alayhi": G("alayhi", "عَلَيْهِ", None, "part", "on him, on it", "onun üzerine", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch15 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("nasaba-nahw", "imtanaa", "nima-verb", "taala", "arada", "jaaza", "taqaddama") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الِاسْمُ الْمُبْهَمُ التَّامُّ وَتَمْيِيزُهُ", "en": "The complete vague noun and its tamyīz", "tr": "Mübhem tâm isim ve temyizi"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العوامل القياسية: الاسم المبهم التام", "الكافية لابن الحاجب — التمييز", "قطر الندى لابن هشام — تمييز العدد"],
 "amil": "الِاسْمُ الْمُبْهَمُ التَّامُّ — a vague noun made complete (by itself, by its tanwīn, by the nūn of the dual, by the nūn of twenty to ninety, by annexation) puts the indefinite noun after it in naṣb as its tamyīz",
 "question": {
  "en": ["What is the eighth qiyāsī governor? The COMPLETE VAGUE NOUN — a noun whose meaning needs a specifier, in a state where it cannot be annexed; it puts that indefinite specifier in naṣb as a TAMYĪZ.",
         "What makes it complete? One of five things: itself, its tanwīn, the nūn of the dual, the nūn of twenty to ninety, or an annexation.",
         "Which nouns are complete by themselves? The vague pronoun — رُبَّهُ رَجُلًا، يَا لَهُ رَجُلًا، نِعْمَ رَجُلًا — and the demonstrative: مَاذَا أَرَادَ اللهُ بِهٰذَا مَثَلًا.",
         "How does the tanwīn complete a noun? Spoken (رِطْلٌ زَيْتًا) or estimated — in مِثْقَالُ ذَهَبًا and in the compound numbers أَحَدَ عَشَرَ رَجُلًا, whose binaʾ stands for it.",
         "What are the counted nouns' rules? Three to ten take a PLURAL in JARR (ثَلَاثَةُ رِجَالٍ) — save three hundred to nine hundred, where the hundred is singular; eleven to ninety-nine take a SINGULAR in NAṢB always (أَحَدَ عَشَرَ رَجُلًا، عِشْرُونَ دِرْهَمًا); a hundred and a thousand, their duals and plurals, take a SINGULAR in JARR (مِائَةُ رَجُلٍ، أَلْفُ دِرْهَمٍ).",
         "How does the nūn of the dual complete a noun? مَنَوَانِ سَمْنًا — and in the measures (the tanwīn kind and the dual kind) annexation is allowed too: رِطْلُ زَيْتٍ، مَنَوَا سَمْنٍ; not elsewhere.",
         "And the nūn resembling the plural's? Twenty to ninety: عِشْرُونَ دِرْهَمًا.",
         "And annexation? مِلْؤُهُ عَسَلًا — the annexed noun is complete by its annex and takes its tamyīz after it.",
         "May the tamyīz stand before its noun? No — the governed word of the complete noun never precedes it.",
         "What does the engine READ here? The DabtEngine puts the nakira after a measure, a number or a vague pronoun in naṣb as its tamyīz, annexes three to ten to a plural and a hundred or a thousand to a singular in jarr, keeps eleven to nineteen on their fatḥa, and declines twenty to ninety by the wāw and the yāʾ."],
  "tr": ["Sekizinci kıyâsî âmil nedir? MÜBHEM TÂM İSİM — mânâsı açıklayıcıya muhtaç olan, izâfet edilemeyecek hâldeki bir isim; o nekre açıklayıcıyı TEMYİZ olarak nasb eder.",
         "Onu tam kılan nedir? Beş şeyden biri: kendisi, tenvini, tesniye nûnu, yirmiden doksana kadarki nûn veya bir izâfet.",
         "Hangi isimler kendiliğinden tamdır? Mübhem zamir — rubbehu racülen, yâ lehu racülen, ni'me racülen — ve ism-i işâret: mâzâ erâda'llâhu bi-hâzâ meselen.",
         "Tenvin bir ismi nasıl tam kılar? Lafzen (rıtlün zeyten) veya takdiren — miskâlü zeheben'de ve binâsı tenvin yerine geçen mürekkeb sayılarda: ehade aşera racülen.",
         "Ma'dûdların kuralları nedir? Üçten ona kadar MECRÛR ÇOĞUL alır (selâsetü ricâlin) — yüzün müfred olduğu üç yüz–dokuz yüz hariç; on birden doksan dokuza kadar daima MANSÛB MÜFRED (ehade aşera racülen, işrûne dirhemen); yüz ve bin, tesniye ve cem'leri MECRÛR MÜFRED alır (mietü racülin, elfü dirhemin).",
         "Tesniye nûnu bir ismi nasıl tam kılar? Menevâni semnen — ölçülerde (tenvin kısmı ve tesniye kısmı) izâfet de câizdir: rıtlü zeytin, menevâ semnin; başka yerde değil.",
         "Cem'e benzeyen nûn? Yirmiden doksana: işrûne dirhemen.",
         "İzâfet? Mil'ühu aselen — muzâf isim muzâfun ileyhiyle tamdır ve temyizini ardına alır.",
         "Temyiz isminin önüne geçebilir mi? Hayır — tâm ismin ma'mûlü asla onun önüne geçmez.",
         "Motor burada neyi OKUR? DabtEngine ölçü, sayı veya mübhem zamirden sonraki nekreyi temyiz olarak nasb eder, üç–onu çoğula, yüz ve bini müfrede mecrûr olarak muzâf yapar, on bir–on dokuzu fethasında tutar, yirmi–doksanı vâv ve yâ ile çeker."],
 },
 "plain": {"en": "Some words leave a question hanging — «twenty», «a pound», «what a one!» — and Arabic answers with a bare noun in the -an ending: twenty dirhams, a pound of oil, a man. That noun is the tamyīz; the counted nouns keep fixed shapes: three men (plural, -in), eleven men (singular, -an), a hundred men (singular, -in).",
           "tr": "Bazı kelimeler bir soruyu askıda bırakır — «yirmi», «bir rıtl», «ne adam!» — Arapça bunu -en ekli yalın bir isimle cevaplar: yirmi dirhem, bir rıtl yağ, bir adam. O cevaplayan isim temyizdir; sayılanlar sabit şekillere uyar: üç adam (çoğul, -in), on bir adam (tekil, -en), yüz adam (tekil, -in)."},
 "explanation": {"en": "The eighth qiyāsī governor is the complete vague noun, which puts an indefinite noun in naṣb as a tamyīz. Its completeness — its being in a state in which annexation is impossible — comes by one of five things: by itself, in the vague pronoun (رُبَّهُ رَجُلًا، يَا لَهُ رَجُلًا، نِعْمَ رَجُلًا) and the demonstrative (مَاذَا أَرَادَ اللهُ بِهٰذَا مَثَلًا); by the tanwīn, spoken (رِطْلٌ زَيْتًا) or estimated (مِثْقَالُ ذَهَبًا، أَحَدَ عَشَرَ رَجُلًا) — the specifier of three to ten being plural in jarr (ثَلَاثَةُ رِجَالٍ) save in three hundred to nine hundred, that of eleven to ninety-nine singular in naṣb always, that of a hundred and a thousand with their duals and plurals singular in jarr (مِائَةُ رَجُلٍ، أَلْفُ دِرْهَمٍ); by the nūn of the dual (مَنَوَانِ سَمْنًا) — annexation being allowed in some of these two kinds (رِطْلُ زَيْتٍ، مَنَوَا سَمْنٍ) and not elsewhere; by the nūn resembling the plural's, twenty to ninety (عِشْرُونَ دِرْهَمًا); and by annexation (مِلْؤُهُ عَسَلًا). The governed word of the complete noun does not precede it.",
                 "tr": "Sekizinci kıyâsî âmil mübhem tâm isimdir; nekre bir ismi temyiz olarak nasb eder. Tamlığı — izâfetinin mümkün olmadığı bir hâlde bulunması — beş şeyden biriyledir: kendisiyle, mübhem zamirde (rubbehu racülen, yâ lehu racülen, ni'me racülen) ve ism-i işârette (mâzâ erâda'llâhu bi-hâzâ meselen); tenvinle, lafzen (rıtlün zeyten) veya takdiren (miskâlü zeheben, ehade aşera racülen) — üçten ona kadarın temyizi mecrûr çoğul (selâsetü ricâlin), üç yüzden dokuz yüze kadar hariç; on birden doksan dokuza kadarınki daima mansûb müfred; yüz ve binin, tesniye ve cem'lerinin temyizi mecrûr müfred (mietü racülin, elfü dirhemin); tesniye nûnuyla (menevâni semnen) — bu iki kısmın bazısında izâfet de câizdir (rıtlü zeytin, menevâ semnin), başkasında değil; cem'e benzeyen nûnla, yirmiden doksana (işrûne dirhemen); ve izâfetle (mil'ühu aselen). Tâm ismin ma'mûlü onun önüne geçmez."},
 "examples": [
  {"ar": "رُبَّهُ رَجُلًا، وَيَا لَهُ رَجُلًا، وَنِعْمَ رَجُلًا", "en": "complete by itself: the vague pronoun", "tr": "kendiliğinden tam: mübhem zamir", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "مَاذَا أَرَادَ اللهُ بِهٰذَا مَثَلًا", "en": "the demonstrative with its tamyīz (al-Baqara 26)", "tr": "temyiziyle ism-i işâret (Bakara 26)", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "رِطْلٌ زَيْتًا", "en": "complete by the spoken tanwīn", "tr": "lafzî tenvinle tam", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "أَحَدَ عَشَرَ رَجُلًا", "en": "the compound number: the tanwīn estimated, the specifier singular in naṣb", "tr": "mürekkeb sayı: tenvin takdirî, temyiz mansûb müfred", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "ثَلَاثَةُ رِجَالٍ", "en": "three to ten: a plural in jarr", "tr": "üçten ona: mecrûr çoğul", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "مِائَةُ رَجُلٍ وَأَلْفُ دِرْهَمٍ", "en": "a hundred and a thousand: a singular in jarr", "tr": "yüz ve bin: mecrûr müfred", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "مَنَوَانِ سَمْنًا", "en": "complete by the nūn of the dual", "tr": "tesniye nûnuyla tam", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "عِشْرُونَ دِرْهَمًا", "en": "complete by the nūn of twenty to ninety", "tr": "yirmi–doksan nûnuyla tam", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "مِلْؤُهُ عَسَلًا", "en": "complete by annexation", "tr": "izâfetle tam", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "ثَلَاثَةُ رَجُلٍ", "right": "ثَلَاثَةُ رِجَالٍ", "why": {"en": "three to ten take a plural in jarr", "tr": "üçten ona kadar mecrûr çoğul alır"}},
  {"wrong": "أَحَدَ عَشَرَ رِجَالًا", "right": "أَحَدَ عَشَرَ رَجُلًا", "why": {"en": "eleven to ninety-nine take a singular in naṣb always", "tr": "on birden doksan dokuza daima mansûb müfred"}},
  {"wrong": "مِائَةُ رِجَالٍ", "right": "مِائَةُ رَجُلٍ", "why": {"en": "a hundred and a thousand take a singular in jarr", "tr": "yüz ve bin mecrûr müfred alır"}},
  {"wrong": "عَسَلًا مِلْؤُهُ", "right": "مِلْؤُهُ عَسَلًا", "why": {"en": "the tamyīz never stands before its complete noun", "tr": "temyiz tâm isminin önüne geçmez"}},
 ],
}
ADD_EN = (" Chapter 15 (print pp. 111-113): the complete vague noun as the eighth governor (s1); its completeness by one of five things — by itself: the vague pronoun and the demonstrative, with al-Baqara 2:26 as the print sets it (s2); by the tanwīn, spoken or estimated (s3); "
          "the counted nouns' rules (s4); by the nūn of the dual and the annexation allowed in the measures (s5); by the nūn of twenty to ninety, by annexation, and no fronting (s6). The print's ثلثة / ثلثمائة are given standard.")
ADD_TR = (" On beşinci bab (baskı s. 111-113): sekizinci âmil olarak mübhem tâm isim (s1); beş şeyden biriyle tamlığı — kendisiyle: mübhem zamir ve ism-i işâret, baskının verdiği şekliyle Bakara 2:26 (s2); lafzî veya takdirî tenvinle (s3); "
          "ma'dûdların kuralları (s4); tesniye nûnuyla ve ölçülerde câiz olan izâfet (s5); yirmi–doksan nûnuyla, izâfetle ve öne geçmeme (s6). Baskının ثلثة / ثلثمائة'si standart imlâyla verildi.")
write_out(15, S, TITLE, ADD_EN, ADD_TR, "pp. 111-113", GLOSS_ADD, notes=(NOTE,),
          related=((TM, [K]), (K14, [K]), (MTH, [K]), (JMS, [K]), ("al-lazim-wal-mutaaddi", [K]), (ISH, [K])))
report(15, S, GLOSS_ADD, (NOTE,))
