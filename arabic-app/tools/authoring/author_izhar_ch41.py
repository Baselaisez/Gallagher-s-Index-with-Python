# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 41: the MAJRŪR — two: by the particle of jarr (passed) and by annexation; neither the muḍāf ilayh nor its
# governed word is fronted before the muḍāf, save when the muḍāf is the word غَيْر, whose muḍāf ilayh's governed word may precede it
# (أَنَا زَيْدًا غَيْرُ ضَارِبٍ, since it means لَا أَضْرِبُ); no separation between the two in ordinary speech beyond what is heard (not to be
# reasoned from), nor in poetic necessity save by the ẓarf. Print pp. 137–138. The lithograph prints the example «أنا زيد غير ضارب»; the
# Ottoman commentary (izhar-full-corrected l. 1419) prints زَيْدًا, the object of ضَارِبٍ, which the text follows.
#   python3 author_izhar_ch41.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
MJ = "mahall-al-majrur"; MDF = "al-mudaf-wa-nawa-al-idafa"; IDL = "idafa-lafziyya"; SH = "shurut-amal-ism-al-fail"
K = "al-majrur-bil-harf-wa-bil-idafa"
K40 = "al-mansubat-al-tasi-ila-al-thalith-ashar"
TITLE = {"ar": "الْمَجْرُورُ اثْنَانِ: بِحَرْفِ الْجَرِّ وَبِالْإِضَافَةِ، وَمَا يَمْتَنِعُ فِي الْمُضَافِ إِلَيْهِ", "en": "The majrūr is two: by the particle of jarr and by annexation, and what is refused in the muḍāf ilayh", "tr": "Mecrûr ikidir: cer harfiyle ve izâfetle; muzâfun ileyhte neyin yasak olduğu"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wala(): return tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve … değildir»", segments=wa("لَا", "la-nafiya", "part"))
def almudaf(gr, punct=None): return tok("الْمُضَافِ", "mudaf", "noun", [K] + gr, "مَجْرُورٌ.", "«the muḍāf»", "«muzâfın»", punct=punct)

# ----------- s1 — the majrūr is two; the first by the particle
S.append({"id": "s1", "translation": {"en": "And as for the majrūr, it is two: the first is the majrūr by the particle of jarr, and its exposition has passed;", "tr": "Mecrûra gelince, o ikidir: birincisi cer harfiyle mecrûr olandır; açıklaması geçmişti;"},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT, "amma-tafsiliyya"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for»", "«… -a gelince»", segments=wa("أَمَّا", "amma", "part")),
  tok("الْمَجْرُورُ", "majrur-noun", "noun", [K, MK, IMF, MJ], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the majrūr» — the mubtada.", "«mecrûr» — mübtedâ."),
  tok("فَاثْنَانِ", "ithnan", "noun", [K, "fa-khabar-mubtada", MK, MTH], "الْفَاءُ وَاقِعَةٌ فِي الْخَبَرِ، وَاثْنَانِ خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«then two» — the khabar, a dual.", "«ikidir» — haber, tesniye.", punct=":", segments=fa("اثْنَانِ", "ithnan", "noun")),
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first»", "«birincisi»"),
  tok("الْمَجْرُورُ", "majrur-noun", "noun", [K, MK, IMF, MJ], "خَبَرٌ مَرْفُوعٌ.", "«the majrūr» — the khabar.", "«mecrûr» — haber."),
  tok("بِحَرْفِ", "harf", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَحَرْفِ مَجْرُورٌ، مُضَافٌ.", "«by the particle of»", "«harfiyle»", segments=[seg("بِ", "bi", "prep"), seg("حَرْفِ", "harf", "noun")]),
  tok("الْجَرِّ", "jarr", "noun", [K, ID, HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr»", "«cer»", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, AT, "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and already»", "«ve … idi»", segments=wa("قَدْ", "qad", "part")),
  tok("مَرَّ", "marra", "verb", [K, FL, "doubled-verbs"], "فِعْلٌ مَاضٍ.", "«has passed»", "«geçmişti»"),
  tok("بَيَانُهُ", "bayan", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — فِي حُرُوفِ الْجَرِّ.", "«its exposition» — under the particles of jarr.", "«açıklaması» — cer harflerinde.", punct="،", segments=[seg("بَيَانُ", "bayan", "noun"), pr3ms()]),
 ]})
# ----------- s2 — the second by annexation; no fronting
S.append({"id": "s2", "translation": {"en": "and the second is the majrūr by annexation, and neither its fronting nor its governed word's before the muḍāf is allowed,", "tr": "ikincisi izâfetle mecrûr olandır; ne kendisinin ne de ma'mûlünün muzâfın önüne alınması câizdir,"},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second»", "«ikincisi»", segments=wa("الثَّانِي", "thani", "noun")),
  tok("الْمَجْرُورُ", "majrur-noun", "noun", [K, MK, IMF, MDF], "خَبَرٌ مَرْفُوعٌ.", "«the majrūr» — the khabar.", "«mecrûr» — haber."),
  tok("بِالْإِضَافَةِ", "idafa", "noun", [K, HJ, MDF, F4], "الْبَاءُ حَرْفُ جَرٍّ، وَالْإِضَافَةِ مَجْرُورٌ.", "«by annexation»", "«izâfetle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْإِضَافَةِ", "idafa", "noun")]),
  wala(),
  tok("يَجُوزُ", "jaaza", "verb", [K, LN, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it is allowed»", "«câiz»"),
  tok("تَقْدِيمُهُ", "taqdim", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْمُضَافُ إِلَيْهِ.", "«its fronting» — the muḍāf ilayh's.", "«öne alınması» — muzâfun ileyhin.", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), pr3ms()]),
  wala(),
  tok("مَعْمُولِهِ", "mamul", "noun", [K, AT, ID, IMF], "مَعْطُوفٌ عَلَى الْهَاءِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَلَا تَقْدِيمُ مَعْمُولِهِ.", "«its governed word» — nor the fronting of its governed word.", "«ma'mûlünün» — ma'mûlünün öne alınması da.", segments=[seg("مَعْمُولِ", "mamul", "noun"), pr3msi()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»"),
  almudaf([HJ, MDF], "،"),
 ]})
# ----------- s3 — the exception: the muḍāf غَيْر
S.append({"id": "s3", "translation": {"en": "unless the muḍāf be the word «ghayr», for then the fronting of the muḍāf ilayh's governed word before it is allowed — as in «I, Zayd, am no striker of» — because it is in the sense of «I do not strike»;", "tr": "ancak muzâf «gayr» lafzı olursa muzâfun ileyhin ma'mûlünün onun önüne alınması câizdir — «ben Zeyd'i döven değilim» gibi — çünkü «dövmem» mânâsındadır;"},
 "tokens": [
  tok("إِلَّا", "illa", "part", [K, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«unless»", "«ancak»"),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS, "istithna"], "حَرْفٌ مَصْدَرِيٌّ.", "«that»", "«-ması»"),
  tok("يَكُونَ", "kana", "verb", [K, KN, AMS, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«it be»", "«olması»"),
  tok("الْمُضَافُ", "mudaf", "noun", [K, KN, MDF], "اسْمُ يَكُونَ مَرْفُوعٌ.", "«the muḍāf»", "«muzâf»"),
  tok("لَفْظَ", "lafz", "noun", [K, KN, ID], "خَبَرُ يَكُونَ مَنْصُوبٌ، مُضَافٌ.", "«the word»", "«lafzı»"),
  tok("غَيْرٍ", "ghayr", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَفْظٌ مَحْكِيٌّ.", "«ghayr»", "«gayr»", punct="،"),
  tok("فَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْفَاءُ لِلتَّفْرِيعِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«for then it is allowed»", "«o zaman câizdir»", segments=fa("يَجُوزُ", "jaaza", "verb")),
  tok("تَقْدِيمُ", "taqdim", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the fronting of»", "«öne alınması»"),
  tok("مَعْمُولِ", "mamul", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the governed word of»", "«ma'mûlünün»"),
  almudaf([ID, MDF]),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ, MDF], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ: الْمُضَافُ إِلَيْهِ.", "«ilayh» — part of the term.", "«ileyh» — terimin parçası.", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — عَلَى الْمُضَافِ.", "«before it» — before the muḍāf.", "«onun önüne» — muzâfın.", punct="،", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  nahw(),
  tok("أَنَا", "ana", "pron", [K, MK], "لَفْظٌ مَحْكِيٌّ: ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ.", "«I» — the mubtada.", "«ben» — mübtedâ."),
  tok("زَيْدًا", "zayd", "propn", [K, MB, SH], "مَفْعُولٌ بِهِ لِضَارِبٍ مُقَدَّمٌ مَنْصُوبٌ — مَعْمُولُ الْمُضَافِ إِلَيْهِ.", "«Zayd» — the object of ضَارِبٍ, fronted: the muḍāf ilayh's governed word.", "«Zeyd'i» — dâribin mef'ûlü, öne alınmış: muzâfun ileyhin ma'mûlü."),
  tok("غَيْرُ", "ghayr", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«no» — the khabar, the muḍāf.", "«değil» — haber, muzâf."),
  tok("ضَارِبٍ", "darib", "noun", [K, ID, IFA, SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ عَامِلٌ فِي زَيْدًا.", "«striker» — the participle governing زَيْدًا.", "«döven» — Zeyden'de âmil ism-i fâil.", punct="،"),
  tok("لِكَوْنِهِ", "kawn", "noun", [K, HJ, ID, MSD], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَكَوْنِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«because of its being»", "«olduğu için»", segments=[seg("لِ", "li", "prep"), seg("كَوْنِ", "kawn", "noun"), pr3msi()]),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى الْمَحْكِيِّ — خَبَرُ الْكَوْنِ.", "«in the sense of»", "«mânâsında»", punct=":", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-mem»"),
  tok("أَضْرِبُ", "daraba", "verb", [K, LN, MR, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — وَالْفِعْلُ يَتَقَدَّمُهُ مَعْمُولُهُ.", "«I strike» — a verb's object may precede it.", "«döverim» — fiilin mef'ûlü önüne geçebilir.", punct="،"),
 ]})
# ----------- s4 — no separation
S.append({"id": "s4", "translation": {"en": "nor is separation between the two by anything allowed in ordinary speech, beyond what has been heard — and it is not reasoned from — nor in poetic necessity, save by the ẓarf.", "tr": "ikisinin arasının genişlikte bir şeyle ayrılması da câiz değildir; işitilenin dışında — ona kıyas da edilmez — zarûrette de ancak zarfla."},
 "tokens": [
  wala(),
  tok("الْفَصْلُ", "fasl", "noun", [K, MK, MSD], "مُبْتَدَأٌ مَرْفُوعٌ — مَعْطُوفٌ عَلَى تَقْدِيمُهُ فِي الْحُكْمِ، وَخَبَرُهُ مَحْذُوفٌ: جَائِزٌ.", "«separation» — its khabar «allowed» understood.", "«ayırma» — «câiz» haberi mahzuf."),
  tok("بَيْنَهُمَا", "bayna", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ — بَيْنَ الْمُضَافِ وَالْمُضَافِ إِلَيْهِ.", "«between the two»", "«ikisinin arasında»", segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("بِشَيْءٍ", "shay", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَشَيْءٍ مَجْرُورٌ.", "«by anything»", "«bir şeyle»", segments=[seg("بِ", "bi", "prep"), seg("شَيْءٍ", "shay", "noun")]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-te»"),
  tok("السَّعَةِ", "saa", "noun", [K, HJ], "مَجْرُورٌ بِفِي — فِي الْكَلَامِ الْمُخْتَارِ غَيْرِ الْمُضْطَرِّ.", "«ordinary speech» — the unforced, chosen speech.", "«genişlikte» — zarûretsiz seçkin söz."),
  tok("غَيْرَ", "ghayr", "noun", [K, "istithna", ID], "مُسْتَثْنًى مَنْصُوبٌ، مُضَافٌ.", "«beyond»", "«dışında»"),
  tok("مَا", "ma-mawsula", "pron", [K, ID, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«what»", "«-en»"),
  tok("سُمِعَ", "samia", "verb", [K, MAW, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةُ مَا.", "«has been heard»", "«işitilen»", punct="،"),
  wala(),
  tok("يُقَاسُ", "qasa", "verb", [K, LN, NF, MR, HV], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«it is reasoned»", "«kıyas edilir»"),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ, NF], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — نَائِبُ الْفَاعِلِ.", "«from it» — the deputy doer.", "«ona» — nâib-i fâil.", punct="،", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  wala(),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-te»"),
  tok("الضَّرُورَةِ", "darura", "noun", [K, HJ], "مَجْرُورٌ بِفِي — ضَرُورَةِ الشِّعْرِ.", "«necessity» — the poet's.", "«zarûrette» — şiir zarûreti."),
  tok("إِلَّا", "illa", "part", [K, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«save»", "«ancak»"),
  tok("بِالظَّرْفِ", "zarf", "noun", [K, HJ, "istithna", MF], "الْبَاءُ حَرْفُ جَرٍّ، وَالظَّرْفِ مَجْرُورٌ — الْفَصْلُ بِالظَّرْفِ جَائِزٌ لِلضَّرُورَةِ.", "«by the ẓarf»", "«zarfla»", punct=".", segments=[seg("بِ", "bi", "prep"), seg("الظَّرْفِ", "zarf", "noun")]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {}
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
print("izhar ch41 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "marra", "samia", "qasa", "daraba") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَجْرُورُ بِالْحَرْفِ وَبِالْإِضَافَةِ: لَا تَقْدِيمَ وَلَا فَصْلَ إِلَّا مَا اسْتُثْنِيَ", "en": "The majrūr by the particle and by annexation: no fronting and no separation save what is excepted", "tr": "Harfle ve izâfetle mecrûr: istisnâ edilen dışında ne takdîm ne fasıl"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المجرورات", "الكافية لابن الحاجب — المضاف إليه", "شرح قطر الندى لابن هشام — الإضافة"],
 "amil": "the majrūr is two — by the particle of jarr (passed under the governors) and by annexation; the muḍāf ilayh is never fronted before its muḍāf, nor is its governed word, save when the muḍāf is غَيْر, whose muḍāf ilayh's object may precede it (أَنَا زَيْدًا غَيْرُ ضَارِبٍ = لَا أَضْرِبُ); nothing separates muḍāf and muḍāf ilayh in ordinary speech beyond what is heard (not a rule to reason from), nor in poetic necessity save the ẓarf",
 "question": {
  "en": ["How many are the majrūrāt? Two: the noun in jarr by a particle (مَرَرْتُ بِزَيْدٍ) and the noun in jarr by annexation (غُلَامُ زَيْدٍ).",
         "May the muḍāf ilayh be fronted before its muḍāf? Never — nor its governed word: not زَيْدٍ غُلَامُ.",
         "What is the one exception? When the muḍāf is غَيْر: the object of its muḍāf ilayh may precede, أَنَا زَيْدًا غَيْرُ ضَارِبٍ — because غَيْرُ ضَارِبٍ means لَا أَضْرِبُ, and a verb's object may precede the verb.",
         "May anything stand between muḍāf and muḍāf ilayh? In ordinary speech only what has been heard from the Arabs, and that is not a rule to reason from; in poetic necessity only the ẓarf.",
         "Why is the ẓarf allowed in necessity? Because the ẓarf is lax in its place and the annexation's bond survives it.",
         "What follows? The dropping of the muḍāf and of the muḍāf ilayh, and what compensates it — in the next chapter.",
         "What does the engine READ here? The DabtEngine reads the fronted name on the tanwīn fatḥ before غَيْرُ ضَارِبٍ as the participle's object, غَيْرُ as the khabar annexed to ضَارِبٍ, the cited particles as the author wrote them, and فَاثْنَانِ as the dual khabar."],
  "tr": ["Mecrûrlar kaç tanedir? İki: harfle mecrûr isim (merartü bi-Zeydin) ve izâfetle mecrûr isim (gulâmu Zeydin).",
         "Muzâfun ileyh muzâfının önüne alınabilir mi? Asla — ma'mûlü de: Zeydin gulâmu denmez.",
         "Tek istisnâ nedir? Muzâf gayr olunca: muzâfun ileyhinin mef'ûlü öne geçebilir, ene Zeyden gayru dâribin — çünkü gayru dâribin lâ adribu demektir, fiilin mef'ûlü de fiilin önüne geçebilir.",
         "Muzâf ile muzâfun ileyhin arasına bir şey girebilir mi? Genişlikte yalnız Araplardan işitilen; o da kıyas edilecek bir kural değildir; şiir zarûretinde yalnız zarf.",
         "Zarûrette zarf neden câizdir? Çünkü zarf yerinde gevşektir, izâfet bağı onu aşar.",
         "Sonra ne gelir? Muzâfın ve muzâfun ileyhin hazfi ve onun yerini tutan şey — sonraki bâbda.",
         "Motor burada neyi OKUR? DabtEngine gayru dâribin'den önceki tenvîn-fethalı ismi ism-i fâilin mef'ûlü; gayru'yu dâribin'e muzâf haber; alıntılanan edatları yazarın yazdığı gibi; fe'snâni'yi tesniye haber okur."],
 },
 "plain": {"en": "The genitive marks a noun after a preposition, and the second noun of a possessive pair («the servant of Zayd»). The second noun never moves in front of the first, and nothing comes between them. One exception: with «ghayr» («not a striker») the object may come first, as the phrase means «I do not strike».",
           "tr": "İki şey mecrûr olur: edattan sonraki isim ve izâfet çiftinin ikinci ismi («Zeyd'in kölesi»). İkinci isim ilkinin önüne geçmez, normal konuşmada araya bir şey girmez; şairler bir zarf sokabilir. Tek istisnâ: «gayr» ile («döven değil») nesne öne geçebilir, çünkü ifade «dövmem» demektir."},
 "explanation": {"en": "The majrūr is of two kinds: the noun in jarr by the particle of jarr, whose exposition passed under the governors, and the noun in jarr by annexation. The muḍāf ilayh may not be fronted before the muḍāf, nor may its governed word — unless the muḍāf is the word غَيْر, when the muḍāf ilayh's governed word may precede it: أَنَا زَيْدًا غَيْرُ ضَارِبٍ, because غَيْرُ ضَارِبٍ is in the sense of لَا أَضْرِبُ, and a verb's object may precede it. Nor may anything separate the muḍāf from the muḍāf ilayh in ordinary speech beyond what has been heard, which is not reasoned from; in poetic necessity only the ẓarf may stand between them. The lithograph prints the example as أنا زيد غير ضارب; the Ottoman commentary prints زَيْدًا, the fronted object of ضَارِبٍ, which the chapter follows.",
                 "tr": "Mecrûr iki türlüdür: cer harfiyle mecrûr isim — açıklaması âmillerde geçti — ve izâfetle mecrûr isim. Muzâfun ileyh muzâfın önüne alınamaz, ma'mûlü de — muzâf gayr lafzı olmadıkça; o zaman muzâfun ileyhin ma'mûlü öne geçebilir: ene Zeyden gayru dâribin; çünkü gayru dâribin lâ adribu mânâsındadır, fiilin mef'ûlü ise fiilin önüne geçebilir. Genişlikte muzâf ile muzâfun ileyhin arasına işitilenin dışında bir şey giremez, işitilene kıyas da edilmez; şiir zarûretinde yalnız zarf araya girebilir. Taşbaskı misâli ene Zeydün gayru dâribin diye basar; Osmanlıca şerh dâribin'in öne alınmış mef'ûlü olan Zeyden'i basar, bab onu izler."},
 "examples": [
  {"ar": "الْأَوَّلُ الْمَجْرُورُ بِحَرْفِ الْجَرِّ، وَالثَّانِي الْمَجْرُورُ بِالْإِضَافَةِ", "en": "the two majrūrs", "tr": "iki mecrûr", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "وَلَا يَجُوزُ تَقْدِيمُهُ وَلَا مَعْمُولِهِ عَلَى الْمُضَافِ", "en": "no fronting before the muḍāf", "tr": "muzâfın önüne takdîm yok", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "أَنَا زَيْدًا غَيْرُ ضَارِبٍ", "en": "the exception with ghayr", "tr": "gayr ile istisnâ", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "وَلَا الْفَصْلُ بَيْنَهُمَا بِشَيْءٍ فِي السَّعَةِ غَيْرَ مَا سُمِعَ", "en": "no separation save what is heard", "tr": "işitilen dışında fasıl yok", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "زَيْدٍ غُلَامُ", "right": "غُلَامُ زَيْدٍ", "why": {"en": "the muḍāf ilayh is never fronted before its muḍāf", "tr": "muzâfun ileyh muzâfının önüne alınmaz"}},
  {"wrong": "أَنَا زَيْدٌ غَيْرُ ضَارِبٍ (meaning «I do not strike Zayd»)", "right": "أَنَا زَيْدًا غَيْرُ ضَارِبٍ", "why": {"en": "Zayd is the fronted object of ضَارِبٍ and keeps its naṣb", "tr": "Zeyd, dâribin'in öne alınmış mef'ûlüdür; nasbını korur"}},
  {"wrong": "غُلَامُ الْيَوْمَ زَيْدٍ (in prose)", "right": "غُلَامُ زَيْدٍ الْيَوْمَ", "why": {"en": "the ẓarf may separate muḍāf and muḍāf ilayh only in poetic necessity", "tr": "zarf, muzâf ile muzâfun ileyhi ancak şiir zarûretinde ayırır"}},
 ],
}
ADD_EN = (" Chapter 41 (print pp. 137-138): the majrūr two — by the particle (s1) and by annexation with no fronting (s2), the exception of ghayr (s3), no separation save what is heard or the ẓarf in necessity (s4).")
ADD_TR = (" Kırk birinci bab (baskı s. 137-138): mecrûr iki — harfle (s1) ve takdîmsiz izâfetle (s2), gayr istisnâsı (s3), işitilen veya zarûrette zarf dışında fasıl yok (s4).")
write_out(41, S, TITLE, ADD_EN, ADD_TR, "pp. 137-138", GLOSS_ADD, notes=(NOTE,),
          related=((K40, [K]), (MJ, [K]), (MDF, [K]), (IDL, [K]), (SH, [K]), (HJ, [K])))
report(41, S, GLOSS_ADD, (NOTE,))
