# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 33: the SECOND manṣūb, the mafʿūl bih — the noun of what the doer's act fell upon; two kinds, general
# (the noun in jarr by the particle) and particular (of the transitive, already passed); it may be fronted (زَيْدًا ضَرَبْتُ), dropped
# absolutely, and its verb dropped on a clue (زَيْدًا to one who asked مَنْ أَضْرِبُ). Print p. 132.
#   python3 author_izhar_ch33.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
LM = "al-lazim-wal-mutaaddi"; MJ = "mahall-al-majrur"; HM = "hadhf-al-maful"
K = "al-maful-bihi-wa-qismah"
K32 = "al-mansubat-al-maful-al-mutlaq"
TITLE = {"ar": "الْمَنْصُوبُ الثَّانِي: الْمَفْعُولُ بِهِ وَقِسْمَاهُ وَأَحْكَامُهُ", "en": "The second manṣūb: the mafʿūl bih, its two kinds and its rules", "tr": "İkinci mansûb: mef'ûl-i bih, iki kısmı ve hükümleri"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)

# ----------- s1 — the second defined
S.append({"id": "s1", "translation": {"en": "And the second is the mafʿūl bih, and it is the noun of what the doer's act fell upon;", "tr": "İkincisi mef'ûl-i bihtir: fâilin fiilinin üzerine düştüğü şeyin ismidir;"},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«and the second»", "«ikincisi»", segments=wa("الثَّانِي", "thani", "noun")),
  tok("الْمَفْعُولُ", "maful-noun", "noun", [K, MK, IMF, MB], "خَبَرٌ مَرْفُوعٌ.", "«the mafʿūl» — the khabar.", "«mef'ûl» — haber."),
  tok("بِهِ", "bi", "prep", [K, HJ, MB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ.", "«bih» — part of the term.", "«bih» — terimin parçası.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("اسْمُ", "ism", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the noun of» — the khabar.", "«ismi» — haber."),
  tok("مَا", "ma-mawsula", "pron", [K, ID, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«what»", "«şeyin»"),
  tok("وَقَعَ", "waqaa", "verb", [K, MAW, FL, "mithal-verbs"], "فِعْلٌ مَاضٍ — صِلَةُ الْمَوْصُولِ.", "«fell»", "«düştüğü»"),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ, MAW], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«upon it» — the returner.", "«üzerine» — âid.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("فِعْلُ", "fil", "noun", [K, FL, ID], "فَاعِلُ وَقَعَ مَرْفُوعٌ، مُضَافٌ.", "«the act of» — the doer of «fell».", "«fiili» — vaka'a'nın fâili."),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer»", "«fâilin»", punct="،"),
 ]})
# ----------- s2 — its two kinds
S.append({"id": "s2", "translation": {"en": "and it is of two kinds: general — and that is the noun in jarr by the particle — and particular to the transitive, and it has passed;", "tr": "ve iki kısımdır: umûmî — o, harfle mecrûr olandır — ve müteaddîye has olan; o da geçmişti;"},
 "tokens": [
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the phrase as khabar.", "«üzere» — câr-mecrûr haber."),
  tok("قِسْمَيْنِ", "qism", "noun", [K, HJ, MTH], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two kinds»", "«iki kısım»", punct=":"),
  tok("عَامٌّ", "amm", "noun", [K, MK, MJ], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا عَامٌّ.", "«general» — the khabar of a dropped «one of them».", "«umûmî» — hazfedilmiş «biri»nin haberi."),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that is»", "«o da»", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْمَجْرُورُ", "majrur", "noun", [K, MK, IMF, MJ], "خَبَرٌ مَرْفُوعٌ.", "«the noun in jarr» — the khabar.", "«mecrûr» — haber."),
  tok("بِالْحَرْفِ", "harf", "noun", [K, HJ, MJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَرْفِ مَجْرُورٌ.", "«by the particle»", "«harfle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْحَرْفِ", "harf", "noun")]),
  tok("وَخَاصٌّ", "khass", "noun", [K, AT, MK, LM], "الْوَاوُ عَاطِفَةٌ، وَخَاصٌّ مَعْطُوفٌ عَلَى عَامٌّ مَرْفُوعٌ.", "«and particular»", "«ve has»", segments=wa("خَاصٌّ", "khass", "noun")),
  tok("بِالْمُتَعَدِّي", "mutaaddi", "noun", [K, HJ, LM, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْمُتَعَدِّي مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«to the transitive»", "«müteaddîye»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْمُتَعَدِّي", "mutaaddi", "noun")]),
  tok("وَقَدْ", "qad", "part", [K, AT, "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and already»", "«ve … idi»", segments=wa("قَدْ", "qad", "part")),
  tok("مَرَّ", "marra", "verb", [K, FL, "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — بَيَانُهُ فِي بَابِ الْعَامِلِ.", "«it has passed» — in the governors' bāb.", "«geçmişti» — âmil bâbında.", punct="،"),
 ]})
# ----------- s3 — fronted; dropped absolutely
S.append({"id": "s3", "translation": {"en": "and its fronting before its governor is allowed — as in «Zayd I struck» — and its dropping absolutely,", "tr": "âmilinin önüne alınması câizdir — «Zeyd'i dövdüm» gibi — ve mutlak olarak hazfi de,"},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("تَقْدِيمُهُ", "taqdim", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its fronting»", "«öne alınması»", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), pr3ms()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»"),
  tok("عَامِلِهِ", "amil", "noun", [K, HJ, ID, IFA], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor»", "«âmilinin»", punct="،", segments=[seg("عَامِلِ", "amil", "noun"), pr3msi()]),
  nahw(),
  tok("زَيْدًا", "zayd", "propn", [K, MB], "لَفْظٌ مَحْكِيٌّ: مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ.", "«Zayd» — the fronted object.", "«Zeyd'i» — öne alınmış mef'ûl."),
  tok("ضَرَبْتُ", "daraba", "verb", [K, FL, MB], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck»", "«dövdüm»", punct="،", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("وَحَذْفُهُ", "hadhf", "noun", [K, AT, FL, ID, MSD, HM], "الْوَاوُ عَاطِفَةٌ، وَحَذْفُهُ مَعْطُوفٌ عَلَى تَقْدِيمُهُ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its dropping»", "«ve hazfi»", segments=[seg("وَ", "wa", "conj"), seg("حَذْفُ", "hadhf", "noun"), pr3ms()]),
  tok("مُطْلَقًا", "mutlaq", "noun", [K, "hal"], "حَالٌ مَنْصُوبٌ — بِقَرِينَةٍ وَبِغَيْرِهَا.", "«absolutely» — with a clue or without.", "«mutlak olarak» — karîneli veya karînesiz.", punct="،"),
 ]})
# ----------- s4 — its verb dropped on a clue
S.append({"id": "s4", "translation": {"en": "and the dropping of its verb where a clue stands — as in «Zayd» to one who asked «whom shall I strike?».", "tr": "karîne bulununca fiilinin hazfi de — «kimi döveyim?» diyene «Zeyd'i» gibi."},
 "tokens": [
  tok("وَحَذْفُ", "hadhf", "noun", [K, AT, FL, ID, MSD, HT], "الْوَاوُ عَاطِفَةٌ، وَحَذْفُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and the dropping of»", "«ve hazfi»", segments=wa("حَذْفُ", "hadhf", "noun")),
  tok("فِعْلِهِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its verb»", "«fiilinin»", segments=[seg("فِعْلِ", "fil", "noun"), pr3msi()]),
  tok("لِقِيَامِ", "qiyam", "noun", [K, HJ, ID, MSD], "اللَّامُ حَرْفُ جَرٍّ، وَقِيَامِ مَجْرُورٌ، مُضَافٌ.", "«where stands»", "«bulununca»", segments=[seg("لِ", "li", "prep"), seg("قِيَامِ", "qiyam", "noun")]),
  tok("قَرِينَةٍ", "qarina", "noun", [K, ID, HT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«bir karîne»", punct="،"),
  nahw(),
  tok("زَيْدًا", "zayd", "propn", [K, MB, HT], "لَفْظٌ مَحْكِيٌّ: مَفْعُولٌ بِهِ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ: اضْرِبْ زَيْدًا.", "«Zayd» — the object of a dropped «strike».", "«Zeyd'i» — hazfedilmiş «döv»ün mef'ûlü.", punct="،"),
  tok("لِمَنْ", "man", "pron", [K, HJ, MAW], "اللَّامُ حَرْفُ جَرٍّ، وَمَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«to one who»", "«… diyene»", segments=[seg("لِ", "li", "prep"), seg("مَنْ", "man", "pron")]),
  tok("قَالَ", "qala", "verb", [K, FL, HV, MAW], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةُ مَنْ.", "«asked»", "«diyen»", punct=":"),
  tok("مَنْ", "man-istifham", "pron", [K, IST, MB], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ، مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«whom» — the fronted object.", "«kimi» — öne alınmış mef'ûl."),
  tok("أَضْرِبُ", "daraba", "verb", [K, MR, FL, IST], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«shall I strike»", "«döveyim»", punct="؟"),
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
print("izhar ch33 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "waqaa", "marra", "daraba", "qala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَفْعُولُ بِهِ: تَعْرِيفُهُ وَقِسْمَاهُ وَتَقْدِيمُهُ وَحَذْفُهُ", "en": "The mafʿūl bih: its definition, its two kinds, its fronting and its dropping", "tr": "Mef'ûl-i bih: tarifi, iki kısmı, öne alınması ve hazfi"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المنصوبات: المفعول به", "الكافية لابن الحاجب — المفعول به", "شرح قطر الندى لابن هشام — المفعول به"],
 "amil": "the second manṣūb is the mafʿūl bih, the noun of what the doer's act fell upon; two kinds — general (the noun in jarr by the particle: مَرَرْتُ بِزَيْدٍ) and particular to the transitive verb (ضَرَبْتُ زَيْدًا, passed in the governors' bāb); it may be fronted before its governor (زَيْدًا ضَرَبْتُ), dropped absolutely, and its verb dropped on a clue (زَيْدًا to one who asked مَنْ أَضْرِبُ)",
 "question": {
  "en": ["What is the mafʿūl bih? The noun of what the doer's act fell upon: زَيْدًا in ضَرَبْتُ زَيْدًا.",
         "What are its two kinds? General — the noun in jarr by a particle (مَرَرْتُ بِزَيْدٍ: the act reaches it through the particle); particular — the object of the transitive verb, treated under the governors.",
         "May it be fronted? Yes: زَيْدًا ضَرَبْتُ — the naṣb stays.",
         "May it be dropped? Absolutely — with a clue or without: ضَرَبْتُ «I struck» stands alone.",
         "May its verb be dropped? On a clue: زَيْدًا answering مَنْ أَضْرِبُ — the dropped verb is اضْرِبْ.",
         "How does the mafʿūl bih differ from the mafʿūl muṭlaq? The muṭlaq names the act itself (ضَرْبًا); the bih names what the act fell upon (زَيْدًا).",
         "What does the engine READ here? The DabtEngine reads the fronted name on the tanwīn fatḥ before its verb as the object, the citation زَيْدًا alone as an object with a dropped verb, مَنْ before أَضْرِبُ as the fronted question-object, and وَقَدْ مَرَّ as the aside it is."],
  "tr": ["Mef'ûl-i bih nedir? Fâilin fiilinin üzerine düştüğü şeyin ismi: darabtü Zeyden'deki Zeyden.",
         "İki kısmı nedir? Umûmî — harfle mecrûr isim (merartü bi-Zeydin: fiil ona harfle ulaşır); has — müteaddî fiilin mef'ûlü, âmiller bâbında geçti.",
         "Öne alınabilir mi? Evet: Zeyden darabtü — nasb kalır.",
         "Hazfedilebilir mi? Mutlak olarak — karîneli veya karînesiz: darabtü «dövdüm» tek başına durur.",
         "Fiili hazfedilebilir mi? Karîne ile: men adribu sorusuna Zeyden — hazfedilen fiil idrib.",
         "Mef'ûl-i bih mef'ûl-i mutlaktan nasıl ayrılır? Mutlak fiilin kendisini adlandırır (darben); bih fiilin üzerine düştüğünü (Zeyden).",
         "Motor burada neyi OKUR? DabtEngine fiilinin önündeki tenvîn-fethalı ismi mef'ûl okur; tek başına Zeyden alıntısını fiili hazfedilmiş mef'ûl; adribu'dan önceki men'i öne alınmış soru mef'ûlü; ve-kad merre'yi ara söz olarak okur."],
 },
 "plain": {"en": "The second accusative is the direct object: what the action lands on, «Zayd» in «I struck Zayd». Broadly, a noun after a preposition is an object too. The object may precede its verb («Zayd I struck»), may be left out, and may stand alone when the verb is obvious: «Zayd!» answering «whom shall I strike?».",
           "tr": "İkinci mansûb, mef'ûl-i bih (nesne)dir: eylemin üzerine düştüğü şey, «Zeyd'i dövdüm»deki «Zeyd'i». Geniş anlamda edattan sonraki isim de nesnedir. Nesne fiilinin önüne geçebilir («Zeyd'i dövdüm»), atılabilir ve fiil belliyken tek başına durabilir: «kimi döveyim?» sorusuna «Zeyd'i!»."},
 "explanation": {"en": "The second manṣūb is the mafʿūl bih: the noun of what the doer's act fell upon. It is of two kinds: general — the noun in jarr by a particle, since the act reaches it through the particle (مَرَرْتُ بِزَيْدٍ) — and particular to the transitive verb, whose object takes naṣb directly (ضَرَبْتُ زَيْدًا), treated already under the governors. It may be fronted before its governor (زَيْدًا ضَرَبْتُ); it may be dropped absolutely, with or without a clue (ضَرَبْتُ); and its verb may be dropped where a clue stands — زَيْدًا in answer to مَنْ أَضْرِبُ, the dropped verb اضْرِبْ.",
                 "tr": "İkinci mansûb mef'ûl-i bihtir: fâilin fiilinin üzerine düştüğü şeyin ismi. İki kısımdır: umûmî — harfle mecrûr isim; çünkü fiil ona harfle ulaşır (merartü bi-Zeydin) — ve müteaddî fiile has olan; onun mef'ûlü doğrudan nasb alır (darabtü Zeyden) ve âmiller bâbında geçmişti. Âmilinin önüne alınabilir (Zeyden darabtü); karîneli veya karînesiz mutlak olarak hazfedilebilir (darabtü); fiili de karîne bulununca hazfedilir — men adribu sorusuna Zeyden; hazfedilen fiil idrib."},
 "examples": [
  {"ar": "اسْمُ مَا وَقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ", "en": "the mafʿūl bih defined", "tr": "mef'ûl-i bihin tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "عَامٌّ وَهُوَ الْمَجْرُورُ بِالْحَرْفِ، وَخَاصٌّ بِالْمُتَعَدِّي", "en": "its two kinds", "tr": "iki kısmı", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "زَيْدًا ضَرَبْتُ", "en": "the object fronted", "tr": "öne alınmış mef'ûl", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "زَيْدًا لِمَنْ قَالَ مَنْ أَضْرِبُ", "en": "the verb dropped on a clue", "tr": "karîne ile hazfedilen fiil", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "زَيْدٌ ضَرَبْتُ (meaning «Zayd I struck»)", "right": "زَيْدًا ضَرَبْتُ", "why": {"en": "the fronted object keeps its naṣb; rafʿ would make Zayd a mubtadaʾ whose khabar lacks a returner", "tr": "öne alınmış mef'ûl nasbını korur; ref' Zeyd'i âidsiz haberli bir mübtedâ yapardı"}},
  {"wrong": "زَيْدٌ (answering مَنْ أَضْرِبُ)", "right": "زَيْدًا", "why": {"en": "the answer is the object of a dropped اضْرِبْ and takes its case", "tr": "cevap hazfedilmiş idrib'in mef'ûlüdür ve onun hâlini alır"}},
  {"wrong": "بِزَيْدٍ counted as no object at all", "right": "بِزَيْدٍ is the general mafʿūl bih", "why": {"en": "the act reaches the noun through the particle — the general kind", "tr": "fiil isme harfle ulaşır — umûmî kısım"}},
 ],
}
ADD_EN = (" Chapter 33 (print p. 132): the mafʿūl bih defined (s1), its general and particular kinds (s2), fronted and dropped absolutely (s3), its verb dropped on a clue (s4).")
ADD_TR = (" Otuz üçüncü bab (baskı s. 132): mef'ûl-i bihin tarifi (s1), umûmî ve has kısımları (s2), öne alınması ve mutlak hazfi (s3), fiilinin karîne ile hazfi (s4).")
write_out(33, S, TITLE, ADD_EN, ADD_TR, "p. 132", GLOSS_ADD, notes=(NOTE,),
          related=((K32, [K]), (MB, [K]), (LM, [K]), (MJ, [K]), (HM, [K]), (HT, [K])))
report(33, S, GLOSS_ADD, (NOTE,))
