# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 34: the THIRD manṣūb, the mafʿūl fīh — the noun of what the governor's content was done in, of time or
# place; its naṣb in wording conditioned on the estimation of فِي (the condition of that estimation passed); fronted even before a
# «sense of the verb», dropped absolutely, its governor dropped on a clue — and the FOURTH, the mafʿūl lahu — the noun of what the
# governor's content was done for; its naṣb conditioned on the estimation of the lām; fronted, left, its governor dropped on a clue. Print p. 133.
#   python3 author_izhar_ch34.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
ML = "maful-lah"; ZM = "zarf-mustaqarr-wa-laghw"; HJR = "hadhf-al-jarr"
K = "al-maful-fih-wal-maful-lah"
K33 = "al-maful-bihi-wa-qismah"
TITLE = {"ar": "الْمَنْصُوبُ الثَّالِثُ وَالرَّابِعُ: الْمَفْعُولُ فِيهِ وَالْمَفْعُولُ لَهُ", "en": "The third and fourth manṣūb: the mafʿūl fīh and the mafʿūl lahu", "tr": "Üçüncü ve dördüncü mansûb: mef'ûl-i fîh ve mef'ûl-i leh"}

def wahuwa(): return tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron"))
def ismu(): return tok("اسْمُ", "ism", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the noun of» — the khabar.", "«ismi» — haber.")
def ma_(): return tok("مَا", "ma-mawsula", "pron", [K, ID, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«what»", "«şeyin»")
def fuila(): return tok("فُعِلَ", "faala", "verb", [K, MAW, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةُ الْمَوْصُولِ.", "«was done»", "«işlendiği»")
def madmun(): return tok("مَضْمُونُ", "madmun", "noun", [K, NF, ID, IMF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«the content of» — the deputy doer.", "«muhtevâsı» — nâib-i fâil.")
def amilihi(punct=None, gr=None): return tok("عَامِلِهِ", "amil", "noun", [K] + (gr or [ID, IFA]), "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", punct=punct, segments=[seg("عَامِلِ", "amil", "noun"), pr3msi()])
def washart(): return tok("وَشَرْطُ", "shart", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَشَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the condition of»", "«ve … şartı»", segments=wa("شَرْطُ", "shart", "noun"))
def nasbihi(): return tok("نَصْبِهِ", "nasb", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its naṣb»", "«nasbının»", segments=[seg("نَصْبِ", "nasb", "noun"), pr3msi()])
def lafzan(): return tok("لَفْظًا", "lafz", "noun", [K, TMZ], "تَمْيِيزٌ مَنْصُوبٌ — أَوْ حَالٌ.", "«in wording»", "«lafzan»")
def taqdiru(): return tok("تَقْدِيرُ", "taqdir", "noun", [K, MK, ID, MSD, F2], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the estimation of» — the khabar.", "«takdîri» — haber.")
def waqadmarra(): return [tok("وَقَدْ", "qad", "part", [K, AT, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and already»", "«ve … idi»", segments=wa("قَدْ", "qad", "part")),
                          tok("مَرَّ", "marra", "verb", [K, FL, "doubled-verbs"], "فِعْلٌ مَاضٍ.", "«has passed»", "«geçmişti»")]
def wayajuz(): return tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb"))
def taqdimuhu(): return tok("تَقْدِيمُهُ", "taqdim", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its fronting»", "«öne alınması»", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), pr3ms()])
def ala(): return tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»")
def wahadhfu(what): return tok("وَحَذْفُ", "hadhf", "noun", [K, AT, FL, ID, MSD, HT], "الْوَاوُ عَاطِفَةٌ، وَحَذْفُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and the dropping of»", "«ve … hazfi»", segments=wa("حَذْفُ", "hadhf", "noun"))
def liqarina(punct="."): return tok("لِقَرِينَةٍ", "qarina", "noun", [K, HJ, HT], "اللَّامُ حَرْفُ جَرٍّ، وَقَرِينَةٍ مَجْرُورٌ.", "«on a clue»", "«karîne ile»", punct=punct, segments=[seg("لِ", "li", "prep"), seg("قَرِينَةٍ", "qarina", "noun")])
TMZ = "tamyiz"

# ----------- s1 — the third: the mafʿūl fīh defined
S.append({"id": "s1", "translation": {"en": "And the third is the mafʿūl fīh, and it is the noun of what the content of its governor was done in, of time or of place;", "tr": "Üçüncüsü mef'ûl-i fîhtir: âmilinin muhtevâsının içinde işlendiği şeyin ismidir — zamandan ya da mekândan;"},
 "tokens": [
  tok("وَالثَّالِثُ", "thalith", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the third»", "«üçüncüsü»", segments=wa("الثَّالِثُ", "thalith", "noun")),
  tok("الْمَفْعُولُ", "maful-noun", "noun", [K, MK, IMF, MF], "خَبَرٌ مَرْفُوعٌ.", "«the mafʿūl» — the khabar.", "«mef'ûl» — haber."),
  tok("فِيهِ", "fi", "prep", [K, HJ, MF], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ.", "«fīh» — part of the term.", "«fîh» — terimin parçası.", punct="،", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  wahuwa(), ismu(), ma_(), fuila(),
  tok("فِيهِ", "fi", "prep", [K, HJ, MAW], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«in it» — the returner.", "«içinde» — âid.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  madmun(), amilihi(),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«of»", "«-dan»"),
  tok("زَمَانٍ", "zaman", "noun", [K, HJ, MF], "مَجْرُورٌ بِمِنْ.", "«time»", "«zaman»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مَكَانٍ", "makan", "noun", [K, AT, MF], "مَعْطُوفٌ مَجْرُورٌ.", "«place»", "«mekân»", punct="،"),
 ]})
# ----------- s2 — the condition of its naṣb: the estimation of فِي
S.append({"id": "s2", "translation": {"en": "and the condition of its naṣb in wording is the estimation of «in», and the condition of that estimation has passed;", "tr": "lafzan nasbının şartı fî'nin takdîridir; o takdîrin şartı da geçmişti;"},
 "tokens": [
  washart(), nasbihi(), lafzan(), taqdiru(),
  tok("فِي", "fi", "prep", [K, ID, MF, ZM], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ — حَرْفُ الظَّرْفِيَّةِ.", "«in» — the particle of containment.", "«fî» — zarfiyet harfi.", punct="،"),
  *waqadmarra(),
  tok("شَرْطُ", "shart", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the condition of»", "«… şartı»"),
  tok("تَقْدِيرِهِ", "taqdir", "noun", [K, ID, MSD, F2], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — فِي بَابِ الْمُضَافِ.", "«its estimation» — in the bāb of the vague nouns.", "«takdîrinin» — mübhem isimler bâbında.", punct="،", segments=[seg("تَقْدِيرِ", "taqdir", "noun"), pr3msi()]),
 ]})
# ----------- s3 — fronted even before a sense of the verb; dropped; its governor dropped
S.append({"id": "s3", "translation": {"en": "and its fronting before its governor is allowed even if that be a sense of the verb, and its dropping absolutely, and the dropping of its governor on a clue.", "tr": "âmilinin önüne alınması, âmil fiil mânâsında olsa bile câizdir; mutlak olarak hazfi de; karîne ile âmilinin hazfi de."},
 "tokens": [
  wayajuz(), taqdimuhu(), ala(),
  tok("عَامِلِهِ", "amil", "noun", [K, HJ, ID, IFA], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", segments=[seg("عَامِلِ", "amil", "noun"), pr3msi()]),
  tok("وَلَوْ", "law", "part", [K, AT, INS], "الْوَاوُ لِلْحَالِ، وَلَوْ وَصْلِيَّةٌ.", "«even if»", "«olsa bile»", segments=wa("لَوْ", "law", "part")),
  tok("كَانَ", "kana", "verb", [K, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْعَامِلُ.", "«it be» — the governor.", "«olsa» — âmil."),
  tok("مَعْنَى", "mana", "noun", [K, KN, ID, MQ, MNF], "خَبَرُ كَانَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«a sense of» — the khabar of kāna.", "«mânâsı» — kâne'nin haberi."),
  tok("فِعْلٍ", "fil", "noun", [K, ID, MNF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — كَأَسْمَاءِ الْأَفْعَالِ وَالظَّرْفِ الْمُسْتَقَرِّ.", "«the verb» — as the noun-verbs and the settled ẓarf.", "«fiil» — isim-fiiller ve zarf-ı müstekar gibi."),
  tok("وَحَذْفُهُ", "hadhf", "noun", [K, AT, FL, ID, MSD, HT], "الْوَاوُ عَاطِفَةٌ، وَحَذْفُهُ مَعْطُوفٌ عَلَى تَقْدِيمُهُ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its dropping»", "«ve hazfi»", segments=[seg("وَ", "wa", "conj"), seg("حَذْفُ", "hadhf", "noun"), pr3ms()]),
  tok("مُطْلَقًا", "mutlaq", "noun", [K, "hal"], "حَالٌ مَنْصُوبٌ.", "«absolutely»", "«mutlak olarak»", punct="،"),
  wahadhfu("amil"),
  tok("عَامِلِهِ", "amil", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", segments=[seg("عَامِلِ", "amil", "noun"), pr3msi()]),
  liqarina(),
 ]})
# ----------- s4 — the fourth: the mafʿūl lahu defined
S.append({"id": "s4", "translation": {"en": "And the fourth is the mafʿūl lahu, and it is the noun of what the content of its governor was done for;", "tr": "Dördüncüsü mef'ûl-i lehtir: âmilinin muhtevâsının uğruna işlendiği şeyin ismidir;"},
 "tokens": [
  tok("وَالرَّابِعُ", "rabi-fourth", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالرَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fourth»", "«dördüncüsü»", segments=wa("الرَّابِعُ", "rabi-fourth", "noun")),
  tok("الْمَفْعُولُ", "maful-noun", "noun", [K, MK, IMF, ML], "خَبَرٌ مَرْفُوعٌ.", "«the mafʿūl» — the khabar.", "«mef'ûl» — haber."),
  tok("لَهُ", "li", "prep", [K, HJ, ML], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ.", "«lahu» — part of the term.", "«leh» — terimin parçası.", punct="،", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  wahuwa(), ismu(), ma_(), fuila(),
  tok("لِأَجْلِهِ", "ajl", "noun", [K, HJ, ID, MAW], "اللَّامُ حَرْفُ جَرٍّ، وَأَجْلِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«for the sake of it» — the returner.", "«uğruna» — âid.", segments=[seg("لِ", "li", "prep"), seg("أَجْلِ", "ajl", "noun"), pr3msi()]),
  madmun(), amilihi("،"),
 ]})
# ----------- s5 — the condition of its naṣb: the lām
S.append({"id": "s5", "translation": {"en": "and the condition of its naṣb in wording is the estimation of the lām, and the condition of that estimation has passed;", "tr": "lafzan nasbının şartı lâm'ın takdîridir; o takdîrin şartı da geçmişti;"},
 "tokens": [
  washart(), nasbihi(), lafzan(), taqdiru(),
  tok("اللَّامِ", "lam-letter", "noun", [K, ID, ML], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَامُ التَّعْلِيلِ.", "«the lām» — of causation.", "«lâm» — ta'lîl lâmı.", punct="،"),
  *waqadmarra(),
  tok("شَرْطُ", "shart", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the condition of»", "«… şartı»"),
  tok("تَقْدِيرِهِ", "taqdir", "noun", [K, ID, MSD, F2], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — فِي بَابِ الْمُضَافِ.", "«its estimation»", "«takdîrinin»", punct="،", segments=[seg("تَقْدِيرِ", "taqdir", "noun"), pr3msi()]),
 ]})
# ----------- s6 — fronted; left; its governor dropped
S.append({"id": "s6", "translation": {"en": "and its fronting before the governor is allowed, and leaving it out, and the dropping of its governor on a clue.", "tr": "âmilin önüne alınması, terki ve karîne ile âmilinin hazfi câizdir."},
 "tokens": [
  wayajuz(), taqdimuhu(), ala(),
  tok("عَامِلٍ", "amil", "noun", [K, HJ, IFA], "مَجْرُورٌ بِعَلَى.", "«a governor»", "«âmilin»"),
  tok("وَتَرْكُهُ", "tark", "noun", [K, AT, FL, ID, MSD, HT], "الْوَاوُ عَاطِفَةٌ، وَتَرْكُهُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and leaving it out»", "«ve terki»", segments=[seg("وَ", "wa", "conj"), seg("تَرْكُ", "tark", "noun"), pr3ms()]),
  wahadhfu("amil"),
  tok("عَامِلِهِ", "amil", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", segments=[seg("عَامِلِ", "amil", "noun"), pr3msi()]),
  liqarina(),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "madmun": G("madmun", "مَضْمُون", "ض م ن", "noun", "content, what is contained — the meaning a governor carries", "muhtevâ, içerik — âmilin taşıdığı mânâ", 4),
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
print("izhar ch34 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "marra", "faala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَفْعُولُ فِيهِ وَالْمَفْعُولُ لَهُ: تَعْرِيفُهُمَا وَشَرْطُ نَصْبِهِمَا وَأَحْكَامُهُمَا", "en": "The mafʿūl fīh and the mafʿūl lahu: their definitions, the condition of their naṣb and their rules", "tr": "Mef'ûl-i fîh ve mef'ûl-i leh: tarifleri, nasb şartları ve hükümleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المنصوبات: المفعول فيه والمفعول له", "الكافية لابن الحاجب — المفعول فيه، المفعول له", "شرح قطر الندى لابن هشام — الظرف والمفعول لأجله"],
 "amil": "the third manṣūb is the mafʿūl fīh — the noun of what the governor's content was done in, of time or place (صُمْتُ يَوْمًا، جَلَسْتُ خَلْفَكَ); its naṣb in wording is conditioned on the estimation of فِي, whose condition (the vague place-noun, any time-noun) passed in the bāb of the muḍāf; it may be fronted before its governor even when that is a sense of the verb, dropped absolutely, and its governor dropped on a clue; the fourth is the mafʿūl lahu — the noun of what the governor's content was done for (ضَرَبْتُهُ تَأْدِيبًا); its naṣb conditioned on the estimation of the lām (a maṣdar of the heart, sharing the verb's time and doer); it may be fronted, left out, and its governor dropped on a clue",
 "question": {
  "en": ["What is the mafʿūl fīh? The noun of what the governor's content was done in — of time (صُمْتُ يَوْمًا) or of place (جَلَسْتُ خَلْفَكَ).",
         "What conditions its naṣb in wording? That فِي be estimated — and فِي may be estimated in every time-noun but only in the vague place-nouns, as the bāb of the muḍāf said.",
         "May it be fronted? Yes, before its governor — even when the governor is a sense of the verb, as the noun-verbs (عِنْدَكَ زَيْدٌ): the ẓarf is the freest of the objects.",
         "May it be dropped? Absolutely; and its governor may be dropped on a clue: يَوْمَ الْجُمُعَةِ to one who asked مَتَى تَأْتِي.",
         "What is the mafʿūl lahu? The noun of what the governor's content was done for: تَأْدِيبًا in ضَرَبْتُهُ تَأْدِيبًا.",
         "What conditions its naṣb? That the lām be estimated: the mafʿūl lahu must be a maṣdar of the heart sharing its governor's time and doer — else the lām is spoken (جِئْتُكَ لِلسَّمَنِ).",
         "What does the engine READ here? The DabtEngine reads the time- and place-nouns on the tanwīn fatḥ after a verb as ẓarfs, the maṣdar on the tanwīn fatḥ after a verb whose doer is bound as a mafʿūl lahu or muṭlaq by its sense, and the cited particles فِي and اللَّام as the author wrote them."],
  "tr": ["Mef'ûl-i fîh nedir? Âmilinin muhtevâsının içinde işlendiği şeyin ismi — zamandan (sumtü yevmen) ya da mekândan (celestü halfeke).",
         "Lafzan nasbının şartı nedir? Fî'nin takdîr edilmesi — fî her zaman isminde takdîr edilebilir, mekân isimlerinde ise yalnız mübhem olanlarda; muzâf bâbında geçtiği gibi.",
         "Öne alınabilir mi? Evet, âmilinin önüne — âmil fiil mânâsında olsa bile, isim-fiiller gibi (indeke Zeydün): zarf mef'ûllerin en serbestidir.",
         "Hazfedilebilir mi? Mutlak olarak; âmili de karîne ile hazfedilir: metâ te'tî diyene yevme'l-cumuati.",
         "Mef'ûl-i leh nedir? Âmilinin muhtevâsının uğruna işlendiği şeyin ismi: darabtühû te'dîben'deki te'dîben.",
         "Nasbının şartı nedir? Lâm'ın takdîr edilmesi: mef'ûl-i leh, âmiliyle zamanı ve fâili ortak bir kalp mastarı olmalıdır — yoksa lâm söylenir (ci'tüke li's-semeni).",
         "Motor burada neyi OKUR? DabtEngine fiilden sonraki tenvîn-fethalı zaman ve mekân isimlerini zarf okur; fâili bağlı fiilden sonraki tenvîn-fethalı mastarı mânâsına göre mef'ûl-i leh veya mutlak okur; alıntılanan fî ve lâm'ı yazarın yazdığı gibi okur."],
 },
 "plain": {"en": "The third accusative is the adverb of time or place: «I fasted a day», «I sat behind you». It takes the accusative only where «in» can be understood. It may come first or be left out. The fourth is the reason: «I struck him as discipline», a feeling-noun that could take «for», sharing the verb's time and doer.",
           "tr": "Üçüncü mansûb zaman veya mekân zarfıdır: «bir gün oruç tuttum», «arkanda oturdum». Ancak önünde «-de» anlaşılabildiğinde nasb alır. Öne gelebilir, atılabilir, tek başına durabilir. Dördüncüsü sebeptir: «onu terbiye için dövdüm» — fiille zamanı ve fâili ortak, önüne «için» gelebilen bir duygu ismi."},
 "explanation": {"en": "The third manṣūb, the mafʿūl fīh, is the noun of what the governor's content was done in — time (صُمْتُ يَوْمًا) or place (جَلَسْتُ خَلْفَكَ). Its naṣb in wording is conditioned on the estimation of فِي, and the condition of that estimation — every time-noun, only the vague place-nouns — passed in the bāb of the muḍāf (chapter 14). It may be fronted before its governor even when that governor is a mere sense of the verb (the noun-verbs, the settled ẓarf), dropped absolutely, and its governor dropped on a clue. The fourth, the mafʿūl lahu, is the noun of what the governor's content was done for (ضَرَبْتُهُ تَأْدِيبًا). Its naṣb in wording is conditioned on the estimation of the lām of causation, whose condition — a maṣdar of the heart sharing the governor's time and doer — likewise passed. It may be fronted before the governor, left out, and its governor dropped on a clue.",
                 "tr": "Üçüncü mansûb mef'ûl-i fîh, âmilinin muhtevâsının içinde işlendiği şeyin ismidir — zaman (sumtü yevmen) veya mekân (celestü halfeke). Lafzan nasbı fî'nin takdîrine bağlıdır; o takdîrin şartı — her zaman ismi, mekân isimlerinden yalnız mübhem olanlar — muzâf bâbında (14. bab) geçmişti. Âmil yalnız fiil mânâsında olsa bile (isim-fiiller, zarf-ı müstekar) âmilinin önüne alınabilir, mutlak olarak hazfedilebilir, âmili de karîne ile hazfedilir. Dördüncüsü mef'ûl-i leh, âmilinin muhtevâsının uğruna işlendiği şeyin ismidir (darabtühû te'dîben). Lafzan nasbı ta'lîl lâmının takdîrine bağlıdır; şartı — âmiliyle zamanı ve fâili ortak bir kalp mastarı — o da geçmişti. Âmilin önüne alınabilir, terkedilebilir, âmili karîne ile hazfedilir."},
 "examples": [
  {"ar": "اسْمُ مَا فُعِلَ فِيهِ مَضْمُونُ عَامِلِهِ مِنْ زَمَانٍ أَوْ مَكَانٍ", "en": "the mafʿūl fīh defined", "tr": "mef'ûl-i fîhin tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "وَشَرْطُ نَصْبِهِ لَفْظًا تَقْدِيرُ فِي", "en": "the estimation of fī", "tr": "fî'nin takdîri", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "وَيَجُوزُ تَقْدِيمُهُ عَلَى عَامِلِهِ وَلَوْ كَانَ مَعْنَى فِعْلٍ", "en": "fronted even before a sense of the verb", "tr": "fiil mânâsının bile önüne alınır", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "اسْمُ مَا فُعِلَ لِأَجْلِهِ مَضْمُونُ عَامِلِهِ", "en": "the mafʿūl lahu defined", "tr": "mef'ûl-i lehin tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "وَشَرْطُ نَصْبِهِ لَفْظًا تَقْدِيرُ اللَّامِ", "en": "the estimation of the lām", "tr": "lâm'ın takdîri", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "جَلَسْتُ الدَّارَ", "right": "جَلَسْتُ فِي الدَّارِ", "why": {"en": "a specific place-noun does not take فِي in estimation, so it takes no naṣb as a ẓarf", "tr": "muayyen mekân ismi fî'yi takdîren almaz; zarf olarak nasb almaz"}},
  {"wrong": "جِئْتُكَ السَّمَنَ", "right": "جِئْتُكَ لِلسَّمَنِ", "why": {"en": "the mafʿūl lahu must be a maṣdar of the heart; a concrete thing needs the spoken lām", "tr": "mef'ûl-i leh kalp mastarı olmalı; somut şey için lâm söylenir"}},
  {"wrong": "ضَرَبْتُهُ تَأْدِيبٌ", "right": "ضَرَبْتُهُ تَأْدِيبًا", "why": {"en": "the mafʿūl lahu is manṣūb by the verb once the lām is estimated", "tr": "lâm takdîr edilince mef'ûl-i leh fiille mansûbdur"}},
 ],
}
ADD_EN = (" Chapter 34 (print p. 133): the mafʿūl fīh defined (s1), the estimation of fī as the condition of its naṣb (s2), fronted even before a sense of the verb, dropped, its governor dropped (s3); the mafʿūl lahu defined (s4), the estimation of the lām (s5), fronted, left, its governor dropped (s6).")
ADD_TR = (" Otuz dördüncü bab (baskı s. 133): mef'ûl-i fîhin tarifi (s1), nasb şartı olarak fî'nin takdîri (s2), fiil mânâsının bile önüne alınması, hazfi, âmilinin hazfi (s3); mef'ûl-i lehin tarifi (s4), lâm'ın takdîri (s5), öne alınması, terki, âmilinin hazfi (s6).")
write_out(34, S, TITLE, ADD_EN, ADD_TR, "p. 133", GLOSS_ADD, notes=(NOTE,),
          related=((K33, [K]), (MF, [K]), (ML, [K]), (ZM, [K]), ("al-mudaf-wa-nawa-al-idafa", [K]), (HT, [K])))
report(34, S, GLOSS_ADD, (NOTE,))
