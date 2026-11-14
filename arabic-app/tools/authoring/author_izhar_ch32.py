# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 32: the MANṢŪBĀT opened — thirteen; the FIRST, the mafʿūl muṭlaq: the noun of what the doer of a governor
# mentioned in wording or in estimation did, in its sense (ضَرَبْتُ ضَرْبًا وَضَرْبَةً وَضَرْبَتَيْنِ); it may be of another wording (قَعَدْتُ جُلُوسًا);
# its verb may be dropped on a clue (أَيْضًا, i.e. آضَ أَيْضًا); it may be fronted before its governor and binds no governor. Print p. 132.
#   python3 author_izhar_ch32.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
MM = "maful-mutlaq"; AMT = "amma-tafsiliyya"; FK = "fa-khabar-mubtada"; LM = "al-lazim-wal-mutaaddi"; TMZ = "tamyiz"
K = "al-mansubat-al-maful-al-mutlaq"
K31 = "al-marfuat-al-khamis-ila-al-tasi"
TITLE = {"ar": "الْمَنْصُوبَاتُ ثَلَاثَةَ عَشَرَ: الْأَوَّلُ الْمَفْعُولُ الْمُطْلَقُ", "en": "The thirteen manṣūbāt: the first, the mafʿūl muṭlaq", "tr": "On üç mansûb: birincisi mef'ûl-i mutlak"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def waqad(): return tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part"))
def wayajuz(): return tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb"))
def darabtu(gr, punct=None): return tok("ضَرَبْتُ", "daraba", "verb", [K] + gr, "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck»", "«dövdüm»", punct=punct, segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")])

# ----------- s1 — the manṣūbāt are thirteen
S.append({"id": "s1", "translation": {"en": "And as for the manṣūb, it is thirteen:", "tr": "Mansûba gelince, o on üçtür:"},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT, AMT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for»", "«… -e gelince»", segments=wa("أَمَّا", "amma", "part")),
  tok("الْمَنْصُوبُ", "mansub", "noun", [K, MK, AMT, IMF], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the manṣūb» — the mubtada.", "«mansûb» — mübtedâ."),
  tok("فَثَلَاثَةَ", "thalatha", "noun", [K, FK, MK, TMZ], "الْفَاءُ وَاقِعَةٌ فِي الْخَبَرِ، وَثَلَاثَةَ عَشَرَ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ رَفْعٍ، خَبَرٌ.", "«then thirteen» — the compound number, the khabar.", "«on üçtür» — mürekkeb sayı, haber.", segments=fa("ثَلَاثَةَ", "thalatha", "noun")),
  tok("عَشَرَ", "ashar", "noun", [K, MK, TMZ], "جُزْءُ الْعَدَدِ الْمُرَكَّبِ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«-teen»", "«on üç»", punct=":"),
 ]})
# ----------- s2 — the first: the mafʿūl muṭlaq defined
S.append({"id": "s2", "translation": {"en": "The first is the mafʿūl muṭlaq, and it is the noun of what the doer of a governor — mentioned in wording or in estimation — did, in its sense; as in «I struck a striking», «one strike», «two strikes»;", "tr": "Birincisi mef'ûl-i mutlaktır: lafzan veya takdîren zikredilmiş bir âmilin fâilinin, onun mânâsında işlediği şeyin ismidir; «vurdum bir vuruş», «bir vuruşla», «iki vuruşla» gibi;"},
 "tokens": [
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first»", "«birincisi»"),
  tok("الْمَفْعُولُ", "maful-noun", "noun", [K, MK, IMF, MM], "خَبَرٌ مَرْفُوعٌ.", "«the mafʿūl» — the khabar.", "«mef'ûl» — haber."),
  tok("الْمُطْلَقُ", "mutlaq", "noun", [K, NA, IMF, MM], "نَعْتٌ مَرْفُوعٌ.", "«the absolute»", "«mutlak»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("اسْمُ", "ism", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the noun of» — the khabar.", "«ismi» — haber."),
  tok("مَا", "ma-mawsula", "pron", [K, ID, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«what»", "«şeyin»"),
  tok("فَعَلَهُ", "faala", "verb", [K, MAW, FL, MB], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْعَائِدُ؛ وَالْجُمْلَةُ صِلَةٌ.", "«did» — its object pronoun the returner.", "«işlediği» — zamiri âid.", segments=[seg("فَعَلَ", "faala", "verb"), pr3ms()]),
  tok("فَاعِلُ", "fail-doer", "noun", [K, FL, ID, IFA], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the doer of»", "«fâilinin»"),
  tok("عَامِلٍ", "amil", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a governor»", "«bir âmilin»"),
  tok("مَذْكُورٍ", "madhkur", "noun", [K, NA, IMF], "نَعْتٌ مَجْرُورٌ.", "«mentioned»", "«zikredilmiş»"),
  tok("لَفْظًا", "lafz", "noun", [K, TMZ], "تَمْيِيزٌ مَنْصُوبٌ — أَوْ حَالٌ.", "«in wording»", "«lafzan»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("تَقْدِيرًا", "taqdir", "noun", [K, AT, TMZ, F2], "مَعْطُوفٌ مَنْصُوبٌ.", "«in estimation»", "«takdîren»"),
  tok("بِمَعْنَاهُ", "mana", "noun", [K, HJ, ID, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَاهُ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِفَعَلَهُ.", "«in its sense» — what the doer did bears the governor's sense.", "«onun mânâsında»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  nahw(),
  darabtu([FL, MM]),
  tok("ضَرْبًا", "darb", "noun", [K, MM, MSD], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — لِلتَّأْكِيدِ.", "«a striking» — the maṣdar confirming.", "«bir vuruş» — te'kîd için."),
  tok("وَضَرْبَةً", "darba", "noun", [K, AT, MM, MSD], "الْوَاوُ عَاطِفَةٌ، وَضَرْبَةً مَعْطُوفٌ مَنْصُوبٌ — لِلْعَدَدِ.", "«and one strike» — the number.", "«ve bir vuruş» — sayı için.", segments=wa("ضَرْبَةً", "darba", "noun")),
  tok("وَضَرْبَتَيْنِ", "darba", "noun", [K, AT, MM, MTH], "الْوَاوُ عَاطِفَةٌ، وَضَرْبَتَيْنِ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«and two strikes» — the dual.", "«ve iki vuruş» — tesniye.", punct="،", segments=wa("ضَرْبَتَيْنِ", "darba", "noun")),
 ]})
# ----------- s3 — of another wording
S.append({"id": "s3", "translation": {"en": "and it may be of other than its wording — as in «I sat a sitting»;", "tr": "lafzının dışında da olabilir — «oturdum bir oturuş» gibi;"},
 "tokens": [
  waqad(),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْمَفْعُولُ الْمُطْلَقُ.", "«it is»", "«olur»"),
  tok("بِغَيْرِ", "ghayr", "noun", [K, HJ, ID, KN], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ — خَبَرُ يَكُونُ.", "«of other than» — the khabar of yakūnu.", "«dışında» — yekûnu'nun haberi.", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  tok("لَفْظِهِ", "lafz", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — لَفْظِ عَامِلِهِ.", "«its wording» — the governor's.", "«lafzının» — âmilinin.", punct="،", segments=[seg("لَفْظِ", "lafz", "noun"), pr3msi()]),
  nahw(),
  tok("قَعَدْتُ", "qaada", "verb", [K, FL, MM], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I sat»", "«oturdum»", segments=[seg("قَعَدْ", "qaada", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("جُلُوسًا", "julus", "noun", [K, MM, MSD], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — مَصْدَرٌ بِمَعْنَى الْقُعُودِ لَا بِلَفْظِهِ.", "«a sitting» — a maṣdar of the sense, not the wording.", "«bir oturuş» — mânâca mastar, lafızca değil.", punct="،"),
 ]})
# ----------- s4 — its verb dropped on a clue: أَيْضًا
S.append({"id": "s4", "translation": {"en": "and its verb may be dropped where a clue stands — as in «also», that is «he returned a returning»;", "tr": "karîne bulununca fiili hazfedilebilir — «eydan» gibi, yani «âda eydan: dönmek döndü»;"},
 "tokens": [
  waqad(),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, NF, MR, HT], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is dropped»", "«hazfedilir»"),
  tok("فِعْلُهُ", "fil", "noun", [K, NF, ID], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its verb» — the deputy doer.", "«fiili» — nâib-i fâil.", segments=[seg("فِعْلُ", "fil", "noun"), pr3ms()]),
  tok("لِقِيَامِ", "qiyam", "noun", [K, HJ, ID, MSD], "اللَّامُ حَرْفُ جَرٍّ، وَقِيَامِ مَجْرُورٌ، مُضَافٌ.", "«where stands»", "«bulununca»", segments=[seg("لِ", "li", "prep"), seg("قِيَامِ", "qiyam", "noun")]),
  tok("قَرِينَةٍ", "qarina", "noun", [K, ID, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«bir karîne»", punct="،"),
  nahw(),
  tok("أَيْضًا", "aydan", "noun", [K, MM, HT], "لَفْظٌ مَحْكِيٌّ: مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ.", "«also» — the maṣdar of a dropped verb.", "«eydan» — hazfedilmiş fiilin mastarı.", punct="،"),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»", punct=":"),
  tok("آضَ", "ada-become", "verb", [K, HT, FL, HV], "فِعْلٌ مَاضٍ مُقَدَّرٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — رَجَعَ.", "«he returned» — the restored verb.", "«döndü» — takdîr edilen fiil."),
  tok("أَيْضًا", "aydan", "noun", [K, MM, MSD], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — مَصْدَرُ آضَ.", "«a returning» — the maṣdar of āḍa.", "«dönüş» — âda'nın mastarı.", punct="،"),
 ]})
# ----------- s5 — fronted; binds no governor
S.append({"id": "s5", "translation": {"en": "and its fronting before its governor is allowed, and it is not bound to a governor.", "tr": "âmilinin önüne alınması câizdir ve bir âmile bağlı değildir."},
 "tokens": [
  wayajuz(),
  tok("تَقْدِيمُهُ", "taqdim", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its fronting»", "«öne alınması»", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), pr3ms()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»"),
  tok("عَامِلِهِ", "amil", "noun", [K, HJ, ID, IFA], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", punct="،", segments=[seg("عَامِلِ", "amil", "noun"), pr3msi()]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve … değildir»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَلْزَمُ", "lazima", "verb", [K, LN, MR, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«it is bound»", "«bağlı»"),
  tok("لِعَامِلٍ", "amil", "noun", [K, HJ, IFA], "اللَّامُ حَرْفُ جَرٍّ، وَعَامِلٍ مَجْرُورٌ — لَا يَخْتَصُّ بِعَامِلٍ بِعَيْنِهِ.", "«to a governor» — not tied to one governor.", "«bir âmile» — belirli bir âmile bağlı değil.", punct=".", segments=[seg("لِ", "li", "prep"), seg("عَامِلٍ", "amil", "noun")]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "darba": G("darba", "ضَرْبَة", "ض ر ب", "noun", "a strike, one blow — the maṣdar of a single occurrence", "bir vuruş — bir kerelik mastar (masdar-ı merre)", 3, plural="ضَرَبَات"),
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
print("izhar ch32 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "daraba", "qaada", "hadhafa", "lazima", "faala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَنْصُوبَاتُ ثَلَاثَةَ عَشَرَ: الْمَفْعُولُ الْمُطْلَقُ وَأَحْكَامُهُ", "en": "The thirteen manṣūbāt: the mafʿūl muṭlaq and its rules", "tr": "On üç mansûb: mef'ûl-i mutlak ve hükümleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المنصوبات: المفعول المطلق", "الكافية لابن الحاجب — المفعول المطلق", "شرح قطر الندى لابن هشام — المفعول المطلق"],
 "amil": "the manṣūbāt are thirteen; the first is the mafʿūl muṭlaq — the noun of what the doer of a governor mentioned in wording or estimation did, in that governor's sense (ضَرَبْتُ ضَرْبًا for confirmation, ضَرْبَةً for number, ضَرْبَتَيْنِ); it may be of another wording (قَعَدْتُ جُلُوسًا); its verb may be dropped on a clue (أَيْضًا = آضَ أَيْضًا); it may be fronted before its governor and is bound to no particular governor",
 "question": {
  "en": ["How many are the manṣūbāt? Thirteen — the mafʿūl muṭlaq opens them.",
         "What is the mafʿūl muṭlaq? The noun of what the doer of a governor — mentioned in wording or estimated — did, in the governor's own sense: ضَرْبًا in ضَرَبْتُ ضَرْبًا.",
         "What are its three uses? Confirmation (ضَرْبًا), kind (ضَرْبًا شَدِيدًا), number (ضَرْبَةً، ضَرْبَتَيْنِ).",
         "Must it share the governor's wording? No — قَعَدْتُ جُلُوسًا: the maṣdar of the sense, not of the letters.",
         "May its verb be dropped? Where a clue stands: أَيْضًا — the maṣdar of آضَ «he returned», its verb never spoken.",
         "May it be fronted? Yes — ضَرْبًا ضَرَبْتُ; and it is not bound to one governor, unlike the mafʿūl bih of the transitive.",
         "What does the engine READ here? The DabtEngine reads the tanwīn-fatḥ maṣdar after a verb with its doer bound as the mafʿūl muṭlaq, the أَوْ/وَ list of maṣdars by their written case, the dual by its yāʾ, the citation أَيْضًا as the author wrote it, and فَثَلَاثَةَ عَشَرَ as the compound number on the fatḥa."],
  "tr": ["Mansûblar kaç tanedir? On üç — ilki mef'ûl-i mutlaktır.",
         "Mef'ûl-i mutlak nedir? Lafzan veya takdîren zikredilmiş bir âmilin fâilinin, o âmilin mânâsında işlediği şeyin ismi: darabtü darben'deki darben.",
         "Üç kullanımı nedir? Te'kîd (darben), nev' (darben şedîden), aded (darbeten, darbeteyni).",
         "Âmilinin lafzını paylaşmak zorunda mı? Hayır — ka'adtü cülûsen: harflerin değil mânânın mastarı.",
         "Fiili hazfedilebilir mi? Karîne bulununca: eydan — âda «döndü» fiilinin mastarı; fiili hiç söylenmez.",
         "Öne alınabilir mi? Evet — darben darabtü; ve tek bir âmile bağlı değildir, müteaddînin mef'ûl-i bihinin aksine.",
         "Motor burada neyi OKUR? DabtEngine fâili bağlı bir fiilden sonraki tenvîn-fethalı mastarı mef'ûl-i mutlak okur; ev/ve ile sıralanan mastarları yazılı hâlleriyle, tesniyeyi yâ'sıyla okur; eydan alıntısını yazarın yazdığı gibi, fe-selâsete aşere'yi fetha üzere mürekkeb sayı okur."],
 },
 "plain": {"en": "Thirteen kinds of word take the accusative. The first is the «absolute object»: a verbal noun repeating its verb to stress it, name its kind or count it: «I struck a striking», «one strike», «two strikes». It may come from another word of the same meaning, stand alone when the verb is understood, or precede its verb.",
           "tr": "On üç tür kelime nasb alır. İlki «mef'ûl-i mutlak»tır: fiilini pekiştirmek, türünü söylemek veya saymak için fiilini tekrarlayan mastar: «vurdum bir vuruş», «bir vuruş», «iki vuruş». Aynı anlamda başka bir kelimeden gelebilir, fiili anlaşılınca tek başına kalabilir, fiilinin önüne de geçebilir."},
 "explanation": {"en": "The manṣūbāt are thirteen. The first, the mafʿūl muṭlaq, is the noun of what the doer of a governor — mentioned in wording or in estimation — did, in that governor's sense: ضَرَبْتُ ضَرْبًا (confirmation), ضَرْبَةً (number: once), ضَرْبَتَيْنِ (twice). It need not share the governor's wording (قَعَدْتُ جُلُوسًا — the maṣdar of the sense). Its verb may be dropped where a clue stands: أَيْضًا is the maṣdar of آضَ «he returned», whose verb is never spoken. It may be fronted before its governor (ضَرْبًا ضَرَبْتُ), and it is not bound to any one governor: every verb, participle and maṣdar may take its own maṣdar as a mafʿūl muṭlaq.",
                 "tr": "Mansûblar on üçtür. İlki, mef'ûl-i mutlak, lafzan veya takdîren zikredilmiş bir âmilin fâilinin o âmilin mânâsında işlediği şeyin ismidir: darabtü darben (te'kîd), darbeten (aded: bir kere), darbeteyni (iki kere). Âmilin lafzını paylaşması gerekmez (ka'adtü cülûsen — mânânın mastarı). Karîne bulununca fiili hazfedilir: eydan, âda «döndü» fiilinin mastarıdır; fiili hiç söylenmez. Âmilinin önüne alınabilir (darben darabtü) ve tek bir âmile bağlı değildir: her fiil, ism-i fâil ve mastar kendi mastarını mef'ûl-i mutlak olarak alabilir."},
 "examples": [
  {"ar": "وَأَمَّا الْمَنْصُوبُ فَثَلَاثَةَ عَشَرَ", "en": "the manṣūbāt counted", "tr": "mansûbların sayısı", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "ضَرَبْتُ ضَرْبًا وَضَرْبَةً وَضَرْبَتَيْنِ", "en": "the mafʿūl muṭlaq of confirmation and number", "tr": "te'kîd ve aded mef'ûl-i mutlakı", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "قَعَدْتُ جُلُوسًا", "en": "the maṣdar of the sense, not the wording", "tr": "lafzın değil mânânın mastarı", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "أَيْضًا، أَيْ آضَ أَيْضًا", "en": "the verb dropped on a clue", "tr": "karîne ile hazfedilen fiil", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "وَيَجُوزُ تَقْدِيمُهُ عَلَى عَامِلِهِ", "en": "fronted, bound to no governor", "tr": "öne alınır, âmile bağlı değildir", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "ضَرَبْتُ ضَرْبٌ", "right": "ضَرَبْتُ ضَرْبًا", "why": {"en": "the mafʿūl muṭlaq is manṣūb by its own verb", "tr": "mef'ûl-i mutlak kendi fiiliyle mansûbdur"}},
  {"wrong": "قَعَدْتُ قُعُودًا only — جُلُوسًا refused", "right": "قَعَدْتُ جُلُوسًا is also a mafʿūl muṭlaq", "why": {"en": "the maṣdar of the sense counts, not only the maṣdar of the wording", "tr": "mânânın mastarı da sayılır, yalnız lafzın mastarı değil"}},
  {"wrong": "أَيْضًا read as a ḥāl", "right": "أَيْضًا is the mafʿūl muṭlaq of a dropped آضَ", "why": {"en": "its verb is dropped on a clue and the maṣdar keeps its naṣb", "tr": "fiili karîne ile hazfedilmiş, mastar nasbını korur"}},
 ],
}
ADD_EN = (" Chapter 32 (print p. 132): the thirteen manṣūbāt opened (s1); the mafʿūl muṭlaq defined with confirmation and number (s2), of another wording (s3), its verb dropped on a clue (s4), fronted and bound to no governor (s5).")
ADD_TR = (" Otuz ikinci bab (baskı s. 132): on üç mansûb açılır (s1); mef'ûl-i mutlak te'kîd ve adediyle tarif edilir (s2), başka lafızdan (s3), fiili karîne ile hazfedilmiş (s4), öne alınan ve âmile bağlı olmayan (s5).")
write_out(32, S, TITLE, ADD_EN, ADD_TR, "p. 132", GLOSS_ADD, notes=(NOTE,),
          related=((K31, [K]), (MM, [K]), (MK, [K]), (HT, [K]), (TMZ, [K])))
report(32, S, GLOSS_ADD, (NOTE,))
