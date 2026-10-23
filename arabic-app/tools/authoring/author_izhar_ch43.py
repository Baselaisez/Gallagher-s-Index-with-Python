# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 43: the MAJZŪM — a muḍāriʿ entered by one of the jāzims mentioned before; since the words of requital demand a
# condition and a requital: both muḍāriʿ, or the first a muḍāriʿ without a fāʾ, jazm in the muḍāriʿ is obligatory; the first a māḍī and the second a
# muḍāriʿ, jazm and rafʿ are both allowed in the second; the requital a conjugable māḍī in the muḍāriʿ's sense, or a muḍāriʿ negated by لَمْ or لَمَّا,
# the fāʾ may not enter it (إِنْ ضَرَبْتَ ضَرَبْتُ أَوْ لَمْ أَضْرِبْ). Print pp. 139–140.
#   python3 author_izhar_ch43.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
AMT = "amma-tafsiliyya"; FK = "fa-khabar-mubtada"; JS = "jawab-al-talab"; LJ = "lam-jazim"
K = "al-majzum-wal-shart-wal-jaza"
K42 = "hadhf-al-mudaf-wal-mudaf-ilayh"
TITLE = {"ar": "الْمَجْزُومُ: الشَّرْطُ وَالْجَزَاءُ وَوُجُوبُ الْجَزْمِ وَجَوَازُهُ", "en": "The majzūm: the condition and the requital, the obligatory jazm and the allowed", "tr": "Meczûm: şart ve cezâ, vâcib ve câiz cezm"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def wain(): return tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part"))
def kana(gr=None): return tok("كَانَ", "kana", "verb", [K, KN, INS, HV] + (gr or []), "فِعْلٌ مَاضٍ نَاقِصٌ، فِعْلُ الشَّرْطِ.", "«is»", "«olursa»")
def mudarian(gr, punct=None): return tok("مُضَارِعًا", "mudari", "noun", [K, KN] + gr, "خَبَرُ كَانَ مَنْصُوبٌ.", "«a muḍāriʿ»", "«muzâri»", punct=punct)

# ----------- s1 — the majzūm defined
S.append({"id": "s1", "translation": {"en": "And as for the majzūm, it is a muḍāriʿ verb entered by one of the jāzims mentioned before;", "tr": "Meczûma gelince, o daha önce zikredilen câzimlerden birinin başına geldiği muzâri fiildir;"},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT, AMT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for»", "«… -a gelince»", segments=wa("أَمَّا", "amma", "part")),
  tok("الْمَجْزُومُ", "majzum", "noun", [K, MK, AMT, IMF, JZ], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the majzūm» — the mubtada.", "«meczûm» — mübtedâ."),
  tok("فَفِعْلٌ", "fil", "noun", [K, FK, MK], "الْفَاءُ وَاقِعَةٌ فِي الْخَبَرِ، وَفِعْلٌ خَبَرٌ مَرْفُوعٌ.", "«then a verb» — the khabar.", "«fiildir» — haber.", segments=fa("فِعْلٌ", "fil", "noun")),
  tok("مُضَارِعٌ", "mudari", "noun", [K, NA, JZ], "نَعْتٌ مَرْفُوعٌ.", "«muḍāriʿ»", "«muzâri»"),
  tok("دَخَلَهُ", "dakhala", "verb", [K, NA, FL, MB, JS], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ.", "«entered by» — the clause a second naʿt.", "«başına gelmiş» — cümle ikinci sıfat.", segments=[seg("دَخَلَ", "dakhala", "verb"), pr3ms()]),
  tok("أَحَدُ", "ahad", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«one of»", "«biri»"),
  tok("الْجَوَازِمِ", "jazim", "noun", [K, ID, JT, JZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the jāzims»", "«câzimlerden»"),
  tok("الْمَذْكُورَةِ", "madhkur", "noun", [K, NA, IMF], "نَعْتٌ مَجْرُورٌ.", "«mentioned»", "«zikredilen»"),
  tok("سَابِقًا", "sabiq", "noun", [K, MF, IFA], "ظَرْفٌ مَنْصُوبٌ — فِي بَابِ الْعَوَامِلِ.", "«before» — in the governors' bāb.", "«daha önce» — âmiller bâbında.", punct="،"),
 ]})
# ----------- s2 — both muḍāriʿ, or the first without a fāʾ: jazm obligatory
S.append({"id": "s2", "translation": {"en": "so since the words of requital demand a condition and a requital — if both are muḍāriʿ, or the first a muḍāriʿ with no fāʾ, the jazm in the muḍāriʿ is obligatory;", "tr": "mücâzât kelimeleri bir şart ve bir cezâ gerektirdiğinden — ikisi de muzâri ise ya da ilki fâsız muzâri ise muzâride cezm vâcibdir;"},
 "tokens": [
  tok("فَإِنْ", "in-shartiyya", "part", [K, AT, INS], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ.", "«so since»", "«o halde … -ğinden»", segments=fa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَتْ", "kana", "verb", [K, KN, INS, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«are»", "«olduğundan»"),
  tok("كَلِمُ", "kalim", "noun", [K, KN, ID], "اسْمُ كَانَتْ مَرْفُوعٌ، مُضَافٌ — جَمْعُ كَلِمَةٍ.", "«the words of»", "«kelimeleri»"),
  tok("الْمُجَازَاةِ", "mujazat", "noun", [K, ID, MSD, "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَدَوَاتُ الشَّرْطِ.", "«requital» — the conditional tools.", "«mücâzât» — şart edatları."),
  tok("تَقْتَضِي", "iqtada-require", "verb", [K, KN, MR, FL, "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ كَانَتْ.", "«demand» — the clause the khabar of kānat.", "«gerektirir» — cümle kânet'in haberi."),
  tok("شَرْطًا", "shart", "noun", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a condition»", "«bir şart»"),
  tok("وَجَزَاءً", "jaza-answer", "noun", [K, AT, MB], "الْوَاوُ عَاطِفَةٌ، وَجَزَاءً مَعْطُوفٌ مَنْصُوبٌ.", "«and a requital»", "«ve bir cezâ»", punct="،", segments=wa("جَزَاءً", "jaza-answer", "noun")),
  tok("فَإِنْ", "in-shartiyya", "part", [K, AT, INS], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ.", "«if»", "«eğer»", segments=fa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَا", "kana", "verb", [K, KN, INS, HV, MTH], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْأَلِفُ اسْمُهُ — الشَّرْطُ وَالْجَزَاءُ.", "«both are» — the condition and the requital.", "«ikisi … ise» — şart ve cezâ.", segments=[seg("كَانَ", "kana", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("مُضَارِعَيْنِ", "mudari", "noun", [K, KN, MTH], "خَبَرُ كَانَا مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two muḍāriʿs»", "«iki muzâri»"),
  aw(),
  tok("الْأَوَّلُ", "awwal", "noun", [K, AT, KN], "مُبْتَدَأٌ مَرْفُوعٌ — أَوْ كَانَ الْأَوَّلُ.", "«the first»", "«ilki»"),
  mudarian([]),
  tok("بِغَيْرِ", "ghayr", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ.", "«with no»", "«-sız»", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  tok("فَاءٍ", "fa-letter", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فِي الْجَزَاءِ.", "«fāʾ» — in the requital.", "«fâ» — cezâda."),
  tok("فَالْجَزْمُ", "jazm", "noun", [K, FK, MK, INS, MSD, JZ], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَالْجَزْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«then the jazm» — the answer's mubtada.", "«cezm» — cevâbın mübtedâsı.", segments=fa("الْجَزْمُ", "jazm", "noun")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْمُضَارِعِ", "mudari", "noun", [K, HJ, JZ], "مَجْرُورٌ بِفِي.", "«the muḍāriʿ»", "«muzâri»"),
  tok("وَاجِبٌ", "wajib", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«obligatory»", "«vâcibdir»", punct="،"),
 ]})
# ----------- s3 — the first a māḍī, the second a muḍāriʿ: jazm and rafʿ allowed
S.append({"id": "s3", "translation": {"en": "and if the first is a māḍī and the second a muḍāriʿ, jazm and rafʿ are both allowed in the second;", "tr": "ilki mâzî ikincisi muzâri ise ikincide cezm de ref' de câizdir;"},
 "tokens": [
  wain(), kana(),
  tok("الْأَوَّلُ", "awwal", "noun", [K, KN], "اسْمُ كَانَ مَرْفُوعٌ.", "«the first»", "«ilki»"),
  tok("مَاضِيًا", "madi", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a māḍī»", "«mâzî»"),
  tok("وَالثَّانِي", "thani", "noun", [K, AT, KN, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — أَوْ كَانَ الثَّانِي.", "«and the second»", "«ikincisi»", segments=wa("الثَّانِي", "thani", "noun")),
  mudarian([JZ]),
  tok("جَازَ", "jaaza", "verb", [K, FL, INS, HV], "فِعْلٌ مَاضٍ، جَوَابُ الشَّرْطِ.", "«it is allowed»", "«câiz olur»"),
  tok("الْجَزْمُ", "jazm", "noun", [K, FL, MSD, JZ], "فَاعِلٌ مَرْفُوعٌ.", "«the jazm»", "«cezm»"),
  tok("وَالرَّفْعُ", "raf", "noun", [K, AT, MSD, MR], "الْوَاوُ عَاطِفَةٌ، وَالرَّفْعُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the rafʿ»", "«ve ref'»", segments=wa("الرَّفْعُ", "raf", "noun")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الثَّانِي", "thani", "noun", [K, HJ, MQ], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«the second»", "«ikincide»", punct="،"),
 ]})
# ----------- s4 — no fāʾ in a conjugable māḍī of the muḍāriʿ's sense, nor in lam/lammā
S.append({"id": "s4", "translation": {"en": "and if the requital is a conjugable māḍī in the sense of the muḍāriʿ, or a muḍāriʿ negated by «lam» or «lammā», the entering of the fāʾ into it is not allowed — as in «if you strike, I strike» or «I have not struck».", "tr": "cezâ, muzâri mânâsında mutasarrıf bir mâzî ya da lem veya lemmâ ile menfî bir muzâri ise ona fâ'nın girmesi câiz değildir — «vurursan vururum» veya «vurmadım» gibi."},
 "tokens": [
  wain(), kana(),
  tok("الْجَزَاءُ", "jaza-answer", "noun", [K, KN], "اسْمُ كَانَ مَرْفُوعٌ.", "«the requital»", "«cezâ»"),
  tok("مَاضِيًا", "madi", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a māḍī»", "«mâzî»"),
  tok("مُتَصَرِّفًا", "mutasarrif", "noun", [K, NA, IFA, F5], "نَعْتٌ مَنْصُوبٌ — لَا كَلَيْسَ وَعَسَى.", "«conjugable» — not like laysa and ʿasā.", "«mutasarrıf» — leyse ve asâ gibi değil."),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«in the sense of»", "«mânâsında»", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("الْمُضَارِعِ", "mudari", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لِأَنَّ الشَّرْطَ يَقْلِبُهُ إِلَى الِاسْتِقْبَالِ.", "«the muḍāriʿ» — the condition turns it to the future.", "«muzâri» — şart onu geleceğe çevirir."),
  aw(),
  mudarian([AT, JZ]),
  tok("مَنْفِيًّا", "manfi", "noun", [K, NA, IMF], "نَعْتٌ مَنْصُوبٌ.", "«negated»", "«menfî»"),
  tok("بِلَمْ", "lam", "part", [K, HJ, LJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَمْ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«by lam»", "«lem ile»", segments=[seg("بِ", "bi", "prep"), seg("لَمْ", "lam", "part")]),
  aw(),
  tok("لَمَّا", "lamma", "part", [K, AT, LJ], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — لَمَّا الْجَازِمَةُ.", "«lammā»", "«lemmâ»"),
  tok("فَلَا", "la-nafiya", "part", [K, AT, LN, INS], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَلَا نَافِيَةٌ.", "«then not»", "«o zaman … değildir»", segments=fa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, LN, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it is allowed»", "«câiz»"),
  tok("دُخُولُ", "dukhul", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the entering of»", "«girmesi»"),
  tok("الْفَاءِ", "fa", "conj", [K, ID, FK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the fāʾ»", "«fâ'nın»"),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — فِي الْجَزَاءِ.", "«into it» — into the requital.", "«ona» — cezâya.", punct="،", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  nahw(),
  tok("إِنْ", "in-shartiyya", "part", [K, INS], "لَفْظٌ مَحْكِيٌّ: حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«-san»"),
  tok("ضَرَبْتَ", "daraba", "verb", [K, INS, FL], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ.", "«you strike» — the condition in the place of jazm.", "«vurursan» — cezm mahallinde şart.", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تَ", "pron-2ms", "pron")]),
  tok("ضَرَبْتُ", "daraba", "verb", [K, INS, FL], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، جَوَابُ الشَّرْطِ بِلَا فَاءٍ، وَالتَّاءُ فَاعِلٌ.", "«I strike» — the requital, no fāʾ.", "«vururum» — fâsız cezâ.", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  aw(),
  tok("لَمْ", "lam", "part", [K, LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not»", "«-medim»"),
  tok("أَضْرِبْ", "daraba", "verb", [K, LJ, FL, INS], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، جَوَابُ الشَّرْطِ بِلَا فَاءٍ.", "«I have struck» — the requital negated by lam, no fāʾ.", "«vurdum» — lem ile menfî cezâ, fâsız.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "iqtada-require": G("iqtada-require", "اقْتَضَى", "ق ض ي", "verb", "to require, demand (form VIII)", "gerektirmek, iktizâ etmek (VIII. bab)", 4, form="VIII"),
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
put_morph(mo, "iqtada-require", {"bab": "الْبَابُ الثَّامِنُ افْتَعَلَ — نَاقِصٌ", "wazn": "افْتَعَلَ يَفْتَعِلُ", "masdar": "اقْتِضَاء", "ismFail": "مُقْتَضٍ",
 "mazi": ["اقْتَضَى", "اقْتَضَيَا", "اقْتَضَوْا", "اقْتَضَتْ", "اقْتَضَتَا", "اقْتَضَيْنَ", "اقْتَضَيْتَ", "اقْتَضَيْتُمَا", "اقْتَضَيْتُمْ", "اقْتَضَيْتِ", "اقْتَضَيْتُمَا", "اقْتَضَيْتُنَّ", "اقْتَضَيْتُ", "اقْتَضَيْنَا"],
 "mudari": ["يَقْتَضِي", "يَقْتَضِيَانِ", "يَقْتَضُونَ", "تَقْتَضِي", "تَقْتَضِيَانِ", "يَقْتَضِينَ", "تَقْتَضِي", "تَقْتَضِيَانِ", "تَقْتَضُونَ", "تَقْتَضِينَ", "تَقْتَضِيَانِ", "تَقْتَضِينَ", "أَقْتَضِي", "نَقْتَضِي"],
 "amr": ["اقْتَضِ", "اقْتَضِيَا", "اقْتَضُوا", "اقْتَضِي", "اقْتَضِيَا", "اقْتَضِينَ"], "mansub": "يَقْتَضِيَ", "majzum": "يَقْتَضِ", "majzum2": "تَقْتَضِ",
 "note": "اقْتَضَى الْأَمْرُ كَذَا يَقْتَضِيهِ اقْتِضَاءً: اسْتَلْزَمَهُ وَطَلَبَهُ — مِنَ الْبَابِ الثَّامِنِ، نَاقِصٌ يَائِيٌّ، مُتَعَدٍّ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch43 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("kana", "dakhala", "jaaza", "daraba") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَجْزُومُ: الشَّرْطُ وَالْجَزَاءُ — وُجُوبُ الْجَزْمِ، وَجَوَازُ الْجَزْمِ وَالرَّفْعِ، وَمَنْعُ الْفَاءِ", "en": "The majzūm: condition and requital — jazm obligatory, jazm and rafʿ allowed, the fāʾ refused", "tr": "Meczûm: şart ve cezâ — vâcib cezm, câiz cezm ve ref', fâ'nın yasağı"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المجزوم", "الكافية لابن الحاجب — الجوازم", "مغني اللبيب لابن هشام — الفاء الرابطة للجواب"],
 "amil": "the majzūm is a muḍāriʿ entered by a jāzim; the words of requital demand a condition and a requital — both muḍāriʿ (إِنْ تَضْرِبْ أَضْرِبْ), or the first a muḍāriʿ with the second fāʾ-less, jazm is obligatory; the first a māḍī and the second a muḍāriʿ (إِنْ ضَرَبْتَ أَضْرِبْ / أَضْرِبُ), jazm and rafʿ both allowed; a conjugable māḍī requital in the muḍāriʿ's sense, or a muḍāriʿ negated by لَمْ or لَمَّا, takes no fāʾ (إِنْ ضَرَبْتَ ضَرَبْتُ، إِنْ ضَرَبْتَ لَمْ أَضْرِبْ)",
 "question": {
  "en": ["What is the majzūm? A muḍāriʿ verb entered by one of the jāzims — لَمْ، لَمَّا، لَامُ الْأَمْرِ، لَا النَّاهِيَةُ and the words of requital.",
         "What do the words of requital demand? A condition and a requital — two clauses, the second hanging on the first: إِنْ، مَنْ، مَا، مَهْمَا، مَتَى، أَيْنَ …",
         "When is jazm obligatory? When both verbs are muḍāriʿ (إِنْ تَضْرِبْ أَضْرِبْ), or the first is a muḍāriʿ and the requital stands without a fāʾ.",
         "When are jazm and rafʿ both allowed? When the condition is a māḍī and the requital a muḍāriʿ: إِنْ ضَرَبْتَ أَضْرِبْ or أَضْرِبُ — the māḍī has no jazm to show, so the requital may follow it as if free.",
         "When is the fāʾ refused in the requital? When the requital is a conjugable māḍī in the muḍāriʿ's sense (إِنْ ضَرَبْتَ ضَرَبْتُ — the condition turns it to the future), or a muḍāriʿ negated by لَمْ or لَمَّا (إِنْ ضَرَبْتَ لَمْ أَضْرِبْ).",
         "Why no fāʾ there? Because such a requital can itself carry the jazm — in wording or in place — and needs no binder; the fāʾ is for the requital that cannot be jazm'd.",
         "What does the engine READ here? The DabtEngine reads the muḍāriʿ after إِنْ on the author's sukūn as the jazm'd condition, the fāʾ-less muḍāriʿ after it as the jazm'd requital, the māḍī condition and its muḍāriʿ requital in jazm or rafʿ by the author's mark, and لَمْ أَضْرِبْ as the negated requital."],
  "tr": ["Meczûm nedir? Câzimlerden birinin başına geldiği muzâri fiil — lem, lemmâ, emir lâmı, nehiy lâ'sı ve mücâzât kelimeleri.",
         "Mücâzât kelimeleri neyi gerektirir? Bir şart ve bir cezâ — iki cümle, ikincisi ilkine bağlı: in, men, mâ, mehmâ, metâ, eyne …",
         "Cezm ne zaman vâcibdir? İki fiil de muzâri ise (in tadrib adrib) ya da ilki muzâri olup cezâ fâsız durursa.",
         "Cezm ve ref' ne zaman birlikte câizdir? Şart mâzî, cezâ muzâri ise: in darabte adrib veya adribu — mâzînin gösterecek cezmi yoktur, cezâ onu serbestçe izleyebilir.",
         "Cezâda fâ ne zaman yasaktır? Cezâ muzâri mânâsında mutasarrıf bir mâzî ise (in darabte darabtü — şart onu geleceğe çevirir) ya da lem veya lemmâ ile menfî muzâri ise (in darabte lem adrib).",
         "Orada neden fâ yok? Çünkü böyle bir cezâ cezmi — lafzan veya mahallen — kendisi taşıyabilir, bağlayıcıya ihtiyacı yoktur; fâ cezm edilemeyen cezâ içindir.",
         "Motor burada neyi OKUR? DabtEngine in'den sonraki muzâriyi yazarın sükûnuyla cezimli şart; ardındaki fâsız muzâriyi cezimli cezâ; mâzî şart ile muzâri cezâyı yazarın işaretine göre cezm veya ref'; lem adrib'i menfî cezâ okur."],
 },
 "plain": {"en": "A verb is «jazm'd» (ending cut short) after words like «not yet», «let», «do not», «if». An «if» needs a condition and a result. Two present-tense verbs are both cut short; after a past-tense condition the result may be cut short or not. The result takes no «then» when it is a plain past verb or a verb with «did not».",
           "tr": "Fiil «değil, henüz», «-sin», «-me» ve «eğer» gibi sözcüklerden sonra «meczûm» olur (sonu kesilir). «Eğer» bir şart ve bir sonuç ister. İki muzâri fiil de kesilir; mâzî şarttan sonra sonuç kesilebilir de kesilmeyebilir de. Sonuç düz bir mâzî ya da «-medi»li bir fiil ise «fe» almaz."},
 "explanation": {"en": "The majzūm is a muḍāriʿ verb entered by one of the jāzims mentioned under the governors. Since the words of requital demand a condition and a requital: when both are muḍāriʿ, or the first is a muḍāriʿ and the requital has no fāʾ, the jazm in the muḍāriʿ is obligatory; when the first is a māḍī and the second a muḍāriʿ, jazm and rafʿ are both allowed in the second. When the requital is a conjugable māḍī in the sense of the muḍāriʿ (the condition carries it to the future), or a muḍāriʿ negated by لَمْ or لَمَّا, the fāʾ may not enter it: إِنْ ضَرَبْتَ ضَرَبْتُ، إِنْ ضَرَبْتَ لَمْ أَضْرِبْ. The requitals that need the fāʾ follow in the next chapter.",
                 "tr": "Meczûm, âmiller bâbında zikredilen câzimlerden birinin başına geldiği muzâri fiildir. Mücâzât kelimeleri şart ve cezâ gerektirdiğinden: ikisi de muzâri ise ya da ilki muzâri olup cezâ fâsız ise muzâride cezm vâcibdir; ilki mâzî ikincisi muzâri ise ikincide cezm de ref' de câizdir. Cezâ muzâri mânâsında mutasarrıf bir mâzî (şart onu geleceğe taşır) ya da lem veya lemmâ ile menfî bir muzâri ise fâ ona giremez: in darabte darabtü, in darabte lem adrib. Fâ isteyen cezâlar sonraki bâbdadır."},
 "examples": [
  {"ar": "فِعْلٌ مُضَارِعٌ دَخَلَهُ أَحَدُ الْجَوَازِمِ", "en": "the majzūm defined", "tr": "meczûmun tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "فَإِنْ كَانَا مُضَارِعَيْنِ … فَالْجَزْمُ فِي الْمُضَارِعِ وَاجِبٌ", "en": "jazm obligatory", "tr": "vâcib cezm", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "وَإِنْ كَانَ الْأَوَّلُ مَاضِيًا وَالثَّانِي مُضَارِعًا جَازَ الْجَزْمُ وَالرَّفْعُ", "en": "jazm and rafʿ allowed", "tr": "câiz cezm ve ref'", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "إِنْ ضَرَبْتَ ضَرَبْتُ أَوْ لَمْ أَضْرِبْ", "en": "the requital without a fāʾ", "tr": "fâsız cezâ", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "إِنْ تَضْرِبْ أَضْرِبُ (rafʿ after a muḍāriʿ condition, no fāʾ)", "right": "إِنْ تَضْرِبْ أَضْرِبْ", "why": {"en": "with both verbs muḍāriʿ and no fāʾ the jazm is obligatory", "tr": "iki fiil de muzâri ve fâ yokken cezm vâcibdir"}},
  {"wrong": "إِنْ ضَرَبْتَ فَضَرَبْتُ", "right": "إِنْ ضَرَبْتَ ضَرَبْتُ", "why": {"en": "a conjugable māḍī requital in the muḍāriʿ's sense takes no fāʾ", "tr": "muzâri mânâsındaki mutasarrıf mâzî cezâ fâ almaz"}},
  {"wrong": "إِنْ ضَرَبْتَ فَلَمْ أَضْرِبْ", "right": "إِنْ ضَرَبْتَ لَمْ أَضْرِبْ", "why": {"en": "a requital negated by lam or lammā refuses the fāʾ", "tr": "lem veya lemmâ ile menfî cezâ fâ'yı reddeder"}},
 ],
}
ADD_EN = (" Chapter 43 (print pp. 139-140): the majzūm defined (s1), jazm obligatory with two muḍāriʿs or a fāʾ-less requital (s2), jazm and rafʿ allowed after a māḍī condition (s3), no fāʾ in a conjugable māḍī or a lam/lammā requital (s4).")
ADD_TR = (" Kırk üçüncü bab (baskı s. 139-140): meczûmun tarifi (s1), iki muzâri veya fâsız cezâ ile vâcib cezm (s2), mâzî şarttan sonra câiz cezm ve ref' (s3), mutasarrıf mâzî veya lem/lemmâ cezâsında fâ yok (s4).")
write_out(43, S, TITLE, ADD_EN, ADD_TR, "pp. 139-140", GLOSS_ADD, notes=(NOTE,),
          related=((K42, [K]), (JZ, [K]), (INS, [K]), (LJ, [K]), (FK, [K]), (JS, [K])))
report(43, S, GLOSS_ADD, (NOTE,))
