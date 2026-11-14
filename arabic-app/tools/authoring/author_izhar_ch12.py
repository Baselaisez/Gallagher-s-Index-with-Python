# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 12: the second, third and fourth QIYĀSĪ governors — the ISM FĀʿIL (works the work of its active
# verb) and the ISM MAFʿŪL (the work of its passive verb); the condition of their governing the detached doer and the object: not
# diminutives (ضُوَيْرِب، مُضَيْرِب), not described (جَاءَنِي ضَارِبٌ شَدِيدٌ) — a description AFTER the work does no harm (جَاءَنِي رَجُلٌ ضَارِبٌ
# غُلَامَهُ شَدِيدٌ); with the lām nothing more is required (الضَّارِبُ غُلَامُهُ عَمْرًا أَمْسِ عِنْدَنَا); bare of it they must LEAN on a mubtadaʾ,
# a described noun or the owner of a ḥāl (جَاءَنِي زَيْدٌ رَاكِبًا غُلَامُهُ), a question (أَقَائِمٌ الزَّيْدَانِ) or a negation (مَا قَائِمٌ الزَّيْدَانِ);
# their naṣb of the object needs the sense of the present or the future; their dual and plural are like their singular, and so the
# three forms of intensification فَعَّال، فَعُول، مِفْعَال — which need no sense of the present or future; and the fourth, the ṢIFA
# MUSHABBAHA, works the work of its verb under the ism fāʿil's conditions save that sense (زَيْدٌ حَسَنٌ وَجْهُهُ). Print pp. 107–109.
#   python3 author_izhar_ch12.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "shurut-amal-ism-al-fail"
K8 = "al-lazim-wal-mutaaddi"
TITLE = {"ar": "اسْمُ الْفَاعِلِ وَاسْمُ الْمَفْعُولِ وَالصِّفَةُ الْمُشَبَّهَةُ وَشُرُوطُ عَمَلِهَا", "en": "The ism fāʿil, the ism mafʿūl and the ṣifa mushabbaha, and the conditions of their governing", "tr": "İsm-i fâil, ism-i mef'ûl ve sıfat-ı müşebbehe, amellerinin şartları"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; AM = "an-masdariyya"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
MM = "maful-mutlaq"; HL = "hal"; MQ = "ism-maqsur-manqus"; BD = "badal"; HV = "hollow-verbs"; DV = "doubled-verbs"; F8 = "form-viii-verbs"; MSD = "masdar"; LN = "la-nafiya"; SH = "in-shartiyya"; IN = "inna-wa-akhawatuha"; SM = "sifa-mushabbaha"; MBL = "sighat-mubalagha"; JT = "jam-taksir"; TSG = "ism-fail"; LJ = "nawasib-wa-jawazim-al-mudari"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«… gibi» — hazfedilmiş mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def zayd(form, role_ar, en, tr, punct=None, tags=()): return tok(form, "zayd", "propn", [K] + list(tags), role_ar, en, tr, punct=punct)
def jaani(punct=None): return tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, "ya-al-mutakallim"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ — لَفْظٌ مَحْكِيٌّ فِي الْمِثَالِ.", "«came to me» — the quoted example's verb with its object pronoun.", "«bana geldi» — örnek cümlenin fiili, mef'ûl zamiriyle.", punct=punct, segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")])
def yushtarat(form="يُشْتَرَطُ", role_ar="فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ", en="«is required»", tr="«şart koşulur»", punct=None, tags=()):
    return tok(form, "ishtarata", "verb", [K, NF, F8] + list(tags), role_ar + ".", en, tr, punct=punct)
def amal(form, role_ar, en, tr, punct=None, segments=None, tags=()): return tok(form, "amal-governing", "noun", [K] + list(tags), role_ar, en, tr, punct=punct, segments=segments)
def fahuwa(): return tok("فَهُوَ", "huwa", "pron", [K, AT, MK], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«so it» — the mubtada of the explaining clause.", "«o da» — açıklayan cümlenin mübtedâsı.", segments=fa("هُوَ", "huwa", "pron"))
def yamalu(form="يَعْمَلُ", en="«works» — the khabar clause, its doer concealed", tr="«amel eder» — haber cümlesi, fâili gizli"): return tok(form, "amila", "verb", [K, MK, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.", en, tr)
def amala(): return amal("عَمَلَ", "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ لِبَيَانِ النَّوْعِ، مُضَافٌ.", "«the work of» — the absolute object of kind, annexed.", "«… ameli gibi» — nev' bildiren mef'ûl-i mutlak, muzâf.", tags=[MM, ID])
def filihi(form="فِعْلِهِ", pr=None):
    pr = pr or pr3msi()
    return tok(form, "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its verb»", "«fiilinin»", segments=[seg("فِعْلِ", "fil", "noun"), pr])

# ----------- s1 — the second: the ism fāʿil
S.append({"id": "s1", "translation": {"en": "And the second is the ISM FĀʿIL — it works the work of its active verb.", "tr": "İkincisi İSM-İ FÂİL'dir — ma'lûm fiilinin amelini yapar."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«and the second» — the mubtada.", "«ikincisi» — mübtedâ.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("اسْمُ", "ism", "noun", [K, MK, ID, IFA], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the noun of» — the khabar, annexed.", "«ismi» — haber, muzâf."),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْفَاعِلِ: الْعَامِلُ الثَّانِي مِنَ الْقِيَاسِيَّةِ.", "«the doer» — the ism fāʿil, the second qiyāsī governor.", "«fâil» — ism-i fâil, ikinci kıyâsî âmil.", punct="،"),
  fahuwa(), yamalu(), amala(), filihi(),
  tok("الْمَعْلُومِ", "malum", "noun", [K, NA, IMF], "نَعْتٌ لِفِعْلِهِ مَجْرُورٌ — الْفِعْلُ الْمَبْنِيُّ لِلْمَعْلُومِ.", "«active» — a naʿt of «its verb»: the verb built for the known.", "«ma'lûm» — fiilinin na'ti: ma'lûm fiil.", punct="."),
 ]})
# ----------- s2 — the third: the ism mafʿūl
S.append({"id": "s2", "translation": {"en": "And the third is the ISM MAFʿŪL — it works the work of its passive verb.", "tr": "Üçüncüsü İSM-İ MEF'ÛL'dür — meçhûl fiilinin amelini yapar."},
 "tokens": [
  tok("وَالثَّالِثُ", "thalith", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the third» — the mubtada.", "«üçüncüsü» — mübtedâ.", segments=wa("الثَّالِثُ", "thalith", "noun")),
  tok("اسْمُ", "ism", "noun", [K, MK, ID, IMF], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the noun of» — the khabar, annexed.", "«ismi» — haber, muzâf."),
  tok("الْمَفْعُولِ", "maful-object", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْمَفْعُولِ: الْعَامِلُ الثَّالِثُ.", "«the object» — the ism mafʿūl, the third governor.", "«mef'ûl» — ism-i mef'ûl, üçüncü âmil.", punct="،"),
  fahuwa(), yamalu(), amala(), filihi(),
  tok("الْمَجْهُولِ", "majhul", "noun", [K, NA, NF], "نَعْتٌ لِفِعْلِهِ مَجْرُورٌ — الْفِعْلُ الْمَبْنِيُّ لِلْمَجْهُولِ.", "«passive» — a naʿt: the verb built for the unknown.", "«meçhûl» — na't: meçhûl fiil.", punct="."),
 ]})
# ----------- s3 — the condition: no diminutive, no description (unless after the work)
S.append({"id": "s3", "translation": {"en": "And the condition of their governing the detached doer and the object is that they not be DIMINUTIVES — as in ḍuwayrib and muḍayrib — and not DESCRIBED — as in «a severe striker came to me»; and if they are described AFTER the work, their earlier work is not harmed — as in «a man came to me, striking his servant, severe».", "tr": "Munfasıl fâilde ve mef'ûlün bihte amel etmelerinin şartı, TASGÎR edilmiş olmamalarıdır — duvayrib ve mudayrib gibi — ve MEVSÛF olmamalarıdır — «bana şiddetli bir vurucu geldi» gibi; amelden SONRA vasıflanırlarsa önceki amelleri zarar görmez — «bana, kölesine vuran şiddetli bir adam geldi» gibi."},
 "tokens": [
  tok("وَشَرْطُ", "shart", "noun", [K, AT, MK, ID], "الْوَاوُ لِلِاسْتِئْنَافِ، وَشَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the condition of» — the mubtada, annexed.", "«ve şartı» — mübtedâ, muzâf.", segments=wa("شَرْطُ", "shart", "noun")),
  amal("عَمَلِهِمَا", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their (two) governing»", "«ikisinin ameli»", segments=[seg("عَمَلِ", "amal-governing", "noun"), seg("هِمَا", "pron-3d", "pron")], tags=[ID]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, HJ, FL], "مَجْرُورٌ بِفِي.", "«the doer»", "«fâilde»"),
  tok("الْمُنْفَصِلِ", "munfasil", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ — الْفَاعِلُ الظَّاهِرُ لَا الضَّمِيرُ الْمُسْتَتِرُ.", "«detached» — the overt doer, not the concealed pronoun.", "«munfasıl» — zâhir fâil, gizli zamir değil."),
  tok("وَالْمَفْعُولِ", "maful-object", "noun", [K, AT, MB], "الْوَاوُ عَاطِفَةٌ، وَالْمَفْعُولِ مَعْطُوفٌ عَلَى الْفَاعِلِ مَجْرُورٌ.", "«and the object»", "«ve mef'ûl»", segments=wa("الْمَفْعُولِ", "maful-object", "noun")),
  tok("بِهِ", "bi", "prep", [K, HJ, MB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْمَفْعُولُ بِهِ.", "«(by) it» — the mafʿūl bihi.", "«bih» — mef'ûlün bih.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, MK], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ شَرْطُ.", "«that» — the an-clause is the khabar.", "«-maları» — en'li cümle haber."),
  tok("لَا", "la-nafiya", "part", [K, LN], "نَافِيَةٌ.", "«not»", "«değil»"),
  tok("يَكُونَا", "kana", "verb", [K, KN, MTH, AM, "afal-khamsa"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ بِحَذْفِ النُّونِ، وَالْأَلِفُ اسْمُهُ — مِنَ الْأَفْعَالِ الْخَمْسَةِ.", "«they two be» — naṣb by the dropped nūn; the alif its ism.", "«ikisi olmasınlar» — nûnun hazfiyle mansûb; elif ismi.", segments=[seg("يَكُونَ", "kana", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("مُصَغَّرَيْنِ", "musaghghar", "noun", [K, KN, MTH, TSG], "خَبَرُ يَكُونَا مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«diminutives» — the khabar, dual in naṣb.", "«tasgîr edilmiş (iki)» — haber, tesniye mansûb.", punct="،"),
  nahw(),
  tok("ضُوَيْرِبٌ", "duwayrib", "noun", [K, MK, TSG, HT], "لَفْظٌ مَحْكِيٌّ: خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ — تَصْغِيرُ ضَارِبٍ.", "«ḍuwayrib» — a little striker: the diminutive of ḍārib.", "«duvayrib» — küçük vurucu: dâribin tasgîri."),
  tok("وَمُضَيْرِبٌ", "mudayrib", "noun", [K, AT, TSG, HT], "الْوَاوُ عَاطِفَةٌ، وَمُضَيْرِبٌ مَعْطُوفٌ مَرْفُوعٌ — تَصْغِيرُ مَضْرُوبٍ.", "«and muḍayrib» — the diminutive of maḍrūb.", "«ve mudayrib» — madrûbun tasgîri.", punct="،", segments=wa("مُضَيْرِبٌ", "mudayrib", "noun")),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«and not»", "«ve … değil»", segments=wa("لَا", "la-nafiya", "part")),
  tok("مَوْصُوفَيْنِ", "mawsuf", "noun", [K, AT, MTH, IMF], "مَعْطُوفٌ عَلَى مُصَغَّرَيْنِ مَنْصُوبٌ بِالْيَاءِ.", "«described» — joined to «diminutives».", "«mevsûf (iki)» — musaggarayn'e ma'tûf.", punct="،"),
  nahw(),
  jaani(),
  tok("ضَارِبٌ", "darib", "noun", [K, FL, IFA], "فَاعِلٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مَوْصُوفٌ، فَلَا يَعْمَلُ.", "«a striker» — the doer; described, so it governs nothing.", "«bir vurucu» — fâil; mevsûf olduğundan amel etmez."),
  tok("شَدِيدٌ", "shadid", "noun", [K, NA, SM], "نَعْتٌ مَرْفُوعٌ.", "«severe» — its naʿt.", "«şiddetli» — na'ti.", punct="،"),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ شَرْطِيَّةٌ جَازِمَةٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("وُصِفَا", "wasafa", "verb", [K, SH, NF, MTH], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَالْأَلِفُ نَائِبُ فَاعِلٍ.", "«they two are described» — the shart verb, the alif its deputy.", "«ikisi vasıflanırsa» — şart fiili, elif nâib-i fâil.", segments=[seg("وُصِفَ", "wasafa", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  amal("الْعَمَلِ", "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the work»", "«amelden»", tags=[ID]),
  tok("لَمْ", "lam-jazima", "part", [K, LJ, SH], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mez»"),
  tok("يَضُرَّ", "darra", "verb", [K, LJ, SH, DV], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَعَلَامَةُ جَزْمِهِ السُّكُونُ الْمُقَدَّرُ وَحُرِّكَ بِالْفَتْحِ لِلتَّخَلُّصِ مِنِ الْتِقَاءِ السَّاكِنَيْنِ — مُضَاعَفٌ؛ وَالْجُمْلَةُ جَوَابُ الشَّرْطِ.", "«is harmed» — jazm by lam, the geminate's fatḥa; the jawāb.", "«zarar görmez» — lem ile meczûm, muzâafın fethası; cevap."),
  amal("عَمَلُهُمَا", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their work» — the doer.", "«ikisinin ameli» — fâil.", segments=[seg("عَمَلُ", "amal-governing", "noun"), seg("هُمَا", "pron-3d", "pron")], tags=[FL, ID]),
  tok("السَّابِقُ", "sabiq", "noun", [K, NA, IFA], "نَعْتٌ مَرْفُوعٌ.", "«earlier» — a naʿt.", "«önceki» — na't.", punct="،"),
  nahw(),
  jaani(),
  tok("رَجُلٌ", "rajul", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«a man» — the doer.", "«bir adam» — fâil."),
  tok("ضَارِبٌ", "darib", "noun", [K, NA, IFA, K8], "نَعْتٌ لِرَجُلٍ مَرْفُوعٌ — اسْمُ فَاعِلٍ عَامِلٌ، وَصْفُهُ بِشَدِيدٍ بَعْدَ عَمَلِهِ.", "«striking» — a naʿt of «a man»; it governs, and is described only after its work.", "«vuran» — racülün na'ti; amel eder, şiddetle vasfı amelinden sonradır."),
  tok("غُلَامَهُ", "ghulam", "noun", [K, MB, ID, IFA], "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his servant» — the object of the ism fāʿil.", "«kölesine» — ism-i fâilin mef'ûlü.", segments=[seg("غُلَامَ", "ghulam", "noun"), pr3ms()]),
  tok("شَدِيدٌ", "shadid", "noun", [K, NA, SM], "نَعْتٌ ثَانٍ لِضَارِبٍ مَرْفُوعٌ — بَعْدَ الْعَمَلِ.", "«severe» — a second naʿt of «striking», after its work.", "«şiddetli» — dâribin ikinci na'ti, amelden sonra.", punct="."),
 ]})
# ----------- s4 — with the lām
S.append({"id": "s4", "translation": {"en": "Then, if the two carry the lām, nothing beyond what was mentioned is required for their governing — as in «the one who struck his servant, ʿAmr, yesterday, at our place».", "tr": "Sonra ikisi lâm ile olursa amel etmeleri için zikredilenden başkası şart koşulmaz — «dün bizim yanımızda kölesi Amr'a vuran» gibi."},
 "tokens": [
  tok("ثُمَّ", "thumma", "part", [K, AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ.", "«then»", "«sonra»"),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "شَرْطِيَّةٌ جَازِمَةٌ.", "«if»", "«eğer»"),
  tok("كَانَا", "kana", "verb", [K, KN, SH, MTH], "فِعْلٌ مَاضٍ نَاقِصٌ فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَالْأَلِفُ اسْمُهُ.", "«they two are» — the shart verb, the alif its ism.", "«ikisi … ise» — şart fiili, elif ismi.", segments=[seg("كَانَ", "kana", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("بِاللَّامِ", "lam-letter", "noun", [K, HJ, KN, "anwa-al-lam-al-tarif"], "الْبَاءُ حَرْفُ جَرٍّ، وَاللَّامِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَا: مُعَرَّفَيْنِ بِلَامِ التَّعْرِيفِ.", "«with the lām» — the khabar of kāna: made definite by the article.", "«lâm ile» — kâne'nin haberi: lâm-ı ta'rîf ile ma'rife.", segments=[seg("بِ", "bi", "prep"), seg("اللَّامِ", "lam-letter", "noun")]),
  tok("لَا", "la-nafiya", "part", [K, LN, SH], "نَافِيَةٌ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ.", "«not» — the jawāb.", "«-maz» — cevap."),
  yushtarat(role_ar="فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ (جَوَابُ الشَّرْطِ بِالرَّفْعِ لِكَوْنِ الشَّرْطِ مَاضِيًا)", en="«is required» — the jawāb kept in rafʿ after a māḍī shart", tr="«şart koşulmaz» — şart mâzî olduğundan cevap merfû"),
  amal("لِعَمَلِهِمَا", "اللَّامُ حَرْفُ جَرٍّ، وَعَمَلِهِمَا مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«for their governing»", "«amelleri için»", segments=[seg("لِ", "li", "prep"), seg("عَمَلِ", "amal-governing", "noun"), seg("هِمَا", "pron-3d", "pron")], tags=[HJ, ID]),
  tok("غَيْرُ", "ghayr", "noun", [K, NF, ID], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«other than» — the deputy, annexed.", "«-den başkası» — nâib-i fâil, muzâf."),
  tok("مَا", "ma-mawsula", "pron", [K, MW, ID], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«what»", "«… olan»"),
  tok("ذُكِرَ", "dhakara", "verb", [K, MW, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةٌ.", "«was mentioned» — the ṣila.", "«zikredildi» — sıla.", punct="،"),
  nahw(),
  tok("الضَّارِبُ", "darib", "noun", [K, MK, IFA, "anwa-al-lam-al-tarif"], "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ بِاللَّامِ عَامِلٌ، وَخَبَرُهُ عِنْدَنَا.", "«the striker» — the mubtada: the ism fāʿil with the article, governing.", "«vuran» — mübtedâ: lâmlı ism-i fâil, amel eder."),
  tok("غُلَامُهُ", "ghulam", "noun", [K, FL, ID, IFA], "فَاعِلٌ لِاسْمِ الْفَاعِلِ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his servant» — the doer of the ism fāʿil.", "«kölesi» — ism-i fâilin fâili.", segments=[seg("غُلَامُ", "ghulam", "noun"), pr3ms()]),
  tok("عَمْرًا", "amr-name", "propn", [K, MB, IFA], "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ مَنْصُوبٌ.", "«ʿAmr» — its object.", "«Amr'a» — mef'ûlü."),
  tok("أَمْسِ", "ams", "noun", [K, MF, "al-murab-wal-mabni-wal-irab"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ.", "«yesterday» — a ẓarf built on the kasra.", "«dün» — kesre üzere mebnî zarf."),
  tok("عِنْدَنَا", "inda", "noun", [K, MF, MK, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — خَبَرُ الْمُبْتَدَإِ.", "«at our place» — the khabar.", "«bizim yanımızda» — haber.", punct=".", segments=[seg("عِنْدَ", "inda", "noun"), seg("نَا", "pron-1p", "pron")]),
 ]})
# ----------- s5 — bare of the lām: the dependence
S.append({"id": "s5", "translation": {"en": "And if the two are bare of it, DEPENDENCE is required — on a mubtadaʾ, a described noun or the owner of a ḥāl, as in «Zayd came to me, his servant riding»; or on a question, as in «are the two Zayds standing?»; or on a negation, as in «the two Zayds are not standing».", "tr": "İkisi ondan yalın olursa İ'TİMÂD şart koşulur — mübtedâya, mevsûfa veya zilhâle, «Zeyd bana geldi, kölesi binmiş olarak» gibi; veya istifhâma, «iki Zeyd ayakta mı?» gibi; veya nefye, «iki Zeyd ayakta değil» gibi."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ شَرْطِيَّةٌ جَازِمَةٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَا", "kana", "verb", [K, KN, SH, MTH], "فِعْلٌ مَاضٍ نَاقِصٌ فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَالْأَلِفُ اسْمُهُ.", "«they two are» — the shart verb.", "«ikisi … ise» — şart fiili.", segments=[seg("كَانَ", "kana", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("مُجَرَّدَيْنِ", "mujarrad", "noun", [K, KN, MTH, IMF], "خَبَرُ كَانَا مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«bare» — the khabar, dual.", "«yalın (iki)» — haber, tesniye."),
  tok("مِنْهَا", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — مِنَ اللَّامِ.", "«of it» — of the lām.", "«ondan» — lâmdan.", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
  yushtarat(role_ar="فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — جَوَابُ الشَّرْطِ بِالرَّفْعِ", en="«is required» — the jawāb in rafʿ", tr="«şart koşulur» — cevap merfû"),
  tok("الِاعْتِمَادُ", "itimad", "noun", [K, NF, MSD, F8], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — مَصْدَرُ اعْتَمَدَ.", "«the dependence» — the deputy.", "«i'timâd» — nâib-i fâil."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-e»"),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, HJ, MK], "مَجْرُورٌ بِعَلَى.", "«the mubtada»", "«mübtedâya»"),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«veya»"),
  tok("الْمَوْصُوفِ", "mawsuf", "noun", [K, AT, NA], "مَعْطُوفٌ عَلَى الْمُبْتَدَإِ مَجْرُورٌ.", "«the described noun»", "«mevsûfa»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("ذِي", "dhu", "noun", [K, AT, ID, "five-nouns"], "مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«the owner of» — jarr by the yāʾ, one of the five nouns.", "«sâhibi» — yâ ile mecrûr, beş isimden."),
  tok("الْحَالِ", "hal", "noun", [K, ID, HL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the ḥāl»", "«hâlin»", punct="،"),
  nahw(),
  jaani(),
  zayd("زَيْدٌ", "فَاعِلٌ مَرْفُوعٌ — ذُو الْحَالِ.", "«Zayd» — the doer, the owner of the ḥāl.", "«Zeyd» — fâil, zilhâl.", tags=[FL]),
  tok("رَاكِبًا", "rakib", "noun", [K, HL, IFA], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ مُعْتَمِدٌ عَلَى ذِي الْحَالِ، عَامِلٌ.", "«riding» — the ḥāl: an ism fāʿil leaning on its owner, governing.", "«binmiş olarak» — hâl: zilhâle dayanan ism-i fâil, amel eder."),
  tok("غُلَامُهُ", "ghulam", "noun", [K, FL, ID, IFA], "فَاعِلٌ لِرَاكِبًا مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his servant» — the doer of «riding».", "«kölesi» — râkiben'in fâili.", punct="،", segments=[seg("غُلَامُ", "ghulam", "noun"), pr3ms()]),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«veya»"),
  tok("الِاسْتِفْهَامِ", "istifham", "noun", [K, AT, "al-istifham"], "مَعْطُوفٌ عَلَى الْمُبْتَدَإِ مَجْرُورٌ.", "«the question»", "«istifhâma»", punct="،"),
  nahw(),
  tok("أَقَائِمٌ", "qaim", "noun", [K, MK, IFA, "al-istifham"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَقَائِمٌ مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مُعْتَمِدٌ عَلَى الِاسْتِفْهَامِ، سَدَّ فَاعِلُهُ مَسَدَّ الْخَبَرِ.", "«are … standing?» — the question hamza; the ism fāʿil a mubtada whose doer stands for the khabar.", "«ayakta mı?» — istifhâm hemzesi; fâili haberin yerini tutan ism-i fâil mübtedâ.", segments=[seg("أَ", "hamza-istifham", "part"), seg("قَائِمٌ", "qaim", "noun")]),
  zayd("الزَّيْدَانِ", "فَاعِلٌ لِقَائِمٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، سَدَّ مَسَدَّ الْخَبَرِ.", "«the two Zayds» — the doer, standing for the khabar.", "«iki Zeyd» — fâil, haberin yerini tutar.", punct="،", tags=[FL, MTH]),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«veya»"),
  tok("النَّفْيِ", "nafy", "noun", [K, AT, LN], "مَعْطُوفٌ عَلَى الْمُبْتَدَإِ مَجْرُورٌ.", "«the negation»", "«nefye»", punct="،"),
  nahw(),
  tok("مَا", "ma-nafiya", "part", [K, LN, "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not»", "«değil»"),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, IFA], "مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مُعْتَمِدٌ عَلَى النَّفْيِ.", "«standing» — the mubtada leaning on the negation.", "«ayakta» — nefye dayanan mübtedâ."),
  zayd("الزَّيْدَانِ", "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ، سَدَّ مَسَدَّ الْخَبَرِ.", "«the two Zayds» — the doer standing for the khabar.", "«iki Zeyd» — haberin yerini tutan fâil.", punct=".", tags=[FL, MTH]),
 ]})
# ----------- s6 — the sense of present or future
S.append({"id": "s6", "translation": {"en": "And for their putting the object in naṣb, the indication of the present or the future is required.", "tr": "Mef'ûlün bihi nasb etmeleri için hâl veya istikbâle delâlet şart koşulur."},
 "tokens": [
  tok("وَيُشْتَرَطُ", "ishtarata", "verb", [K, AT, NF, F8], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيُشْتَرَطُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«and … is required»", "«ve … şart koşulur»", segments=wa("يُشْتَرَطُ", "ishtarata", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«for»", "«-de»"),
  tok("نَصْبِهِمَا", "nasb", "noun", [K, HJ, ID, MSD], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — مَصْدَرٌ مُضَافٌ إِلَى فَاعِلِهِ.", "«their putting in naṣb» — a maṣdar annexed to its doer.", "«ikisinin nasb etmesi» — fâiline muzâf mastar.", segments=[seg("نَصْبِ", "nasb", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("الْمَفْعُولَ", "maful-object", "noun", [K, MB, MSD], "مَفْعُولٌ بِهِ لِلْمَصْدَرِ مَنْصُوبٌ.", "«the object» — the object of the maṣdar.", "«mef'ûlü» — mastarın mef'ûlü."),
  tok("بِهِ", "bi", "prep", [K, HJ, MB], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«(by) it»", "«bih»", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("الدَّلَالَةُ", "dalala", "noun", [K, NF, MSD], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the indication» — the deputy.", "«delâlet» — nâib-i fâil."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-e»"),
  tok("الْحَالِ", "hal", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى — زَمَنُ الْحَالِ.", "«the present»", "«hâle (şimdiki zamana)»"),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«veya»"),
  tok("الِاسْتِقْبَالِ", "istiqbal", "noun", [K, AT, MSD], "مَعْطُوفٌ مَجْرُورٌ.", "«the future»", "«istikbâle»", punct="."),
 ]})
# ----------- s7 — dual, plural, the three forms of intensification
S.append({"id": "s7", "translation": {"en": "And their dual and their plural are like their singular, and so are the three patterns of the doer's intensification — faʿʿāl, faʿūl and mifʿāl — and the sense of the present and the future is not required for the governing of these three.", "tr": "Tesniyeleri ve cem'leri müfredleri gibidir; fâilin mübalağasının üç vezni — fa''âl, fa'ûl ve mif'âl — de öyledir, ve bu üçünün amelinde hâl ve istikbâl mânâsı şart koşulmaz."},
 "tokens": [
  tok("وَتَثْنِيَتُهُمَا", "tathniya", "noun", [K, AT, MK, ID, MTH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَتَثْنِيَتُهُمَا مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«and their dual» — the mubtada.", "«ve tesniyeleri» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("تَثْنِيَتُ", "tathniya", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("وَجَمْعُهُمَا", "jam", "noun", [K, AT, ID, JT], "الْوَاوُ عَاطِفَةٌ، وَجَمْعُهُمَا مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«and their plural»", "«ve cem'leri»", segments=[seg("وَ", "wa", "conj"), seg("جَمْعُ", "jam", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("كَمُفْرَدِهِمَا", "mufrad", "noun", [K, HJ, MK, ID], "الْكَافُ حَرْفُ جَرٍّ، وَمُفْرَدِهِمَا مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«like their singular» — the khabar.", "«müfredleri gibi» — haber.", punct="،", segments=[seg("كَ", "ka", "prep"), seg("مُفْرَدِ", "mufrad", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("وَكَذَا", "kadha", "part", [K, AT, HT], "الْوَاوُ عَاطِفَةٌ، وَكَذَا: الْكَافُ حَرْفُ جَرٍّ وَذَا اسْمُ إِشَارَةٍ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and likewise» — the fronted khabar.", "«ve böylece» — mukaddem haber.", segments=wa("كَذَا", "kadha", "part")),
  tok("ثَلَاثَةُ", "thalatha", "noun", [K, MK, ID, "tamyiz"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«three» — the delayed mubtada, annexed.", "«üç» — muahhar mübtedâ, muzâf."),
  tok("أَوْزَانٍ", "wazn", "noun", [K, ID, JT, "tamyiz"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ وَزْنٍ.", "«patterns»", "«vezin»"),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("مُبَالَغَةِ", "mubalagha", "noun", [K, HJ, ID, MBL], "مَجْرُورٌ بِمِنْ، مُضَافٌ — صِيَغُ الْمُبَالَغَةِ.", "«the intensification of» — the forms of intensity.", "«mübalağa» — mübalağa sîgaları."),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer»", "«fâilin»", punct=":"),
  tok("فَعَّالٌ", "faal", "noun", [K, MK, HT, MBL], "لَفْظٌ مَحْكِيٌّ: بَدَلُ تَفْصِيلٍ مِنْ ثَلَاثَةُ مَرْفُوعٌ، أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«faʿʿāl» — the first pattern, a badal of detail.", "«fa''âl» — ilk vezin, bedel-i tafsîl."),
  tok("وَفَعُولٌ", "faul-wazn", "noun", [K, AT, HT, MBL], "الْوَاوُ عَاطِفَةٌ، وَفَعُولٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and faʿūl»", "«ve fa'ûl»", segments=wa("فَعُولٌ", "faul-wazn", "noun")),
  tok("وَمِفْعَالٌ", "mifal-wazn", "noun", [K, AT, HT, MBL], "الْوَاوُ عَاطِفَةٌ، وَمِفْعَالٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and mifʿāl»", "«ve mif'âl»", punct="،", segments=wa("مِفْعَالٌ", "mifal-wazn", "noun")),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … -maz»", segments=wa("لَا", "la-nafiya", "part")),
  yushtarat(role_ar="فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ", en="«is required»", tr="«şart koşulur»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«for»", "«-de»"),
  amal("عَمَلِ", "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the governing of»", "«amelinde»", tags=[HJ, ID]),
  tok("هٰذِهِ", "hadhihi", "pron", [K, ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«these»", "«bu»"),
  tok("الثَّلَاثَةِ", "thalatha", "noun", [K, BD, "tamyiz"], "بَدَلٌ مِنْ هٰذِهِ مَجْرُورٌ.", "«three» — the badal of the demonstrative.", "«üçünün» — ism-i işâretin bedeli."),
  tok("مَعْنَى", "mana", "noun", [K, NF, ID, MQ], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the sense of» — the deputy.", "«mânâsı» — nâib-i fâil."),
  tok("الْحَالِ", "hal", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the present»", "«hâl»"),
  tok("وَالِاسْتِقْبَالِ", "istiqbal", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالِاسْتِقْبَالِ مَعْطُوفٌ مَجْرُورٌ.", "«and the future»", "«ve istikbâl»", punct=".", segments=wa("الِاسْتِقْبَالِ", "istiqbal", "noun")),
 ]})
# ----------- s8 — the fourth: the ṣifa mushabbaha
S.append({"id": "s8", "translation": {"en": "And the fourth is the ṢIFA MUSHABBAHA — it works the work of its verb under the conditions considered for the ism fāʿil, save the sense of the present and the future, for that is not required for its governing — as in «Zayd is handsome of face».", "tr": "Dördüncüsü SIFAT-I MÜŞEBBEHE'dir — ism-i fâilde mûteber olan şartlarla fiilinin amelini yapar, hâl ve istikbâl mânâsı hariç; çünkü o, amelinde şart koşulmaz — «Zeyd yüzü güzeldir» gibi."},
 "tokens": [
  tok("وَالرَّابِعُ", "rabi-fourth", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالرَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fourth» — the mubtada.", "«dördüncüsü» — mübtedâ.", segments=wa("الرَّابِعُ", "rabi-fourth", "noun")),
  tok("الصِّفَةُ", "sifa", "noun", [K, MK, SM], "خَبَرٌ مَرْفُوعٌ.", "«the adjective» — the khabar.", "«sıfat» — haber."),
  tok("الْمُشَبَّهَةُ", "mushabbaha", "noun", [K, NA, SM, IMF], "نَعْتٌ مَرْفُوعٌ — الصِّفَةُ الْمُشَبَّهَةُ بِاسْمِ الْفَاعِلِ.", "«resembling» — the ṣifa mushabbaha: likened to the ism fāʿil.", "«müşebbehe» — ism-i fâile benzeyen sıfat.", punct="،"),
  tok("فَهِيَ", "hiya", "pron", [K, AT, MK], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَهِيَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«so it» — the mubtada.", "«o da» — mübtedâ.", segments=fa("هِيَ", "hiya", "pron")),
  yamalu("تَعْمَلُ", "«works» — the khabar clause, its doer concealed (she)", "«amel eder» — haber cümlesi, fâili gizli (o)"),
  amala(),
  filihi("فِعْلِهَا", pr3fs()),
  tok("بِالشُّرُوطِ", "shart", "noun", [K, HJ, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَالشُّرُوطِ مَجْرُورٌ — جَمْعُ شَرْطٍ.", "«under the conditions»", "«şartlarla»", segments=[seg("بِ", "bi", "prep"), seg("الشُّرُوطِ", "shart", "noun")]),
  tok("الْمُعْتَبَرَةِ", "mutabar", "noun", [K, NA, IMF, F8], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنِ اعْتَبَرَ.", "«considered» — a naʿt: the ism mafʿūl of iʿtabara.", "«mûteber» — na't: i'tebera'nın ism-i mef'ûlü."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«for»", "«-de»"),
  tok("اسْمِ", "ism", "noun", [K, HJ, ID, IFA], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the noun of»", "«ism-i»"),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer»", "«fâil»"),
  tok("غَيْرَ", "ghayr", "noun", [K, "istithna", ID], "مُسْتَثْنًى بِغَيْرَ مَنْصُوبٌ، مُضَافٌ.", "«save» — the exception, annexed.", "«hariç» — müstesnâ, muzâf."),
  tok("مَعْنَى", "mana", "noun", [K, ID, MQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the sense of»", "«mânâsı»"),
  tok("الْحَالِ", "hal", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the present»", "«hâl»"),
  tok("وَالِاسْتِقْبَالِ", "istiqbal", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالِاسْتِقْبَالِ مَعْطُوفٌ مَجْرُورٌ.", "«and the future»", "«ve istikbâl»", punct="،", segments=wa("الِاسْتِقْبَالِ", "istiqbal", "noun")),
  tok("فَإِنَّهُ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«for it» — inna with its pronoun ism.", "«çünkü o» — inne, zamir ismi.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("لَا", "la-nafiya", "part", [K, LN], "نَافِيَةٌ.", "«not»", "«-maz»"),
  yushtarat(role_ar="فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ إِنَّ", en="«is required» — the khabar of inna", tr="«şart koşulmaz» — inne'nin haberi", tags=[IN]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«for»", "«-de»"),
  amal("عَمَلِهَا", "مَجْرُورٌ بِفِي، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its governing»", "«onun amelinde»", punct="،", segments=[seg("عَمَلِ", "amal-governing", "noun"), pr3fs()], tags=[HJ, ID]),
  nahw(),
  zayd("زَيْدٌ", "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ.", tags=[MK]),
  tok("حَسَنٌ", "hasan-adj", "noun", [K, MK, SM], "خَبَرٌ مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ عَامِلَةٌ.", "«handsome» — the khabar: a ṣifa mushabbaha that governs.", "«güzel» — haber: amel eden sıfat-ı müşebbehe."),
  tok("وَجْهُهُ", "wajh", "noun", [K, FL, ID, SM], "فَاعِلٌ لِلصِّفَةِ الْمُشَبَّهَةِ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his face» — the doer of the ṣifa mushabbaha.", "«yüzü» — sıfat-ı müşebbehenin fâili.", punct=".", segments=[seg("وَجْهُ", "wajh", "noun"), pr3ms()]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

CAND = {
 "thani": G("thani", "ثَانِي", "ث ن ي", "noun", "second", "ikinci", 1),
 "ism": G("ism", "اِسْم", "س م و", "noun", "noun; name", "isim", 1, plural="أَسْمَاء"),
 "fail-doer": G("fail-doer", "فَاعِل", "ف ع ل", "noun", "the doer (fāʿil); the active participle", "fâil; ism-i fâil", 2),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to work, to act; (of a governor) to govern", "çalışmak, yapmak; (âmil) amel etmek", 1),
 "amal-governing": G("amal-governing", "الْعَمَل", "ع م ل", "noun", "the governing (of a word in another's iʿrāb)", "amel (bir kelimenin başkasının i'râbına etkisi)", 3),
 "fil": G("fil", "فِعْل", "ف ع ل", "noun", "verb; act", "fiil", 1, plural="أَفْعَال"),
 "malum": G("malum", "مَعْلُوم", "ع ل م", "noun", "known; (a verb) active", "ma'lûm; (fiil) etken", 2),
 "thalith": G("thalith", "ثَالِث", "ث ل ث", "noun", "third", "üçüncü", 1),
 "maful-object": G("maful-object", "مَفْعُول", "ف ع ل", "noun", "object (mafʿūl); the passive participle", "mef'ûl; ism-i mef'ûl", 2, plural="مَفَاعِيل"),
 "majhul": G("majhul", "مَجْهُول", "ج ه ل", "noun", "unknown; (a verb) passive", "meçhûl; (fiil) edilgen", 2),
 "shart": G("shart", "شَرْط", "ش ر ط", "noun", "condition", "şart", 2, plural="شُرُوط"),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "munfasil": G("munfasil", "مُنْفَصِل", "ف ص ل", "noun", "detached, separate", "munfasıl, ayrı", 3),
 "bi": G("bi", "بِ", None, "prep", "with, by, in", "ile, -de", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "to, that (the masdar particle that puts the muḍāriʿ in naṣb)", "-mesi, -mek (muzâriyi nasb eden mastar harfi)", 2),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not (negation)", "değil, -mez (nefiy)", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak, idi", 1),
 "musaghghar": G("musaghghar", "مُصَغَّر", "ص غ ر", "noun", "diminutive (made small)", "tasgîr edilmiş, küçültülmüş", 4),
 "nahw": G("nahw", "نَحْو", "ن ح و", "noun", "like, such as; grammar", "gibi; nahiv", 2),
 "duwayrib": G("duwayrib", "ضُوَيْرِب", "ض ر ب", "noun", "a little striker — the diminutive of ḍārib (quoted as a word)", "küçük vurucu — dâribin tasgîri (lafız olarak)", 5),
 "mudayrib": G("mudayrib", "مُضَيْرِب", "ض ر ب", "noun", "a little struck one — the diminutive of maḍrūb (quoted as a word)", "küçük vurulmuş — madrûbun tasgîri (lafız olarak)", 5),
 "mawsuf": G("mawsuf", "مَوْصُوف", "و ص ف", "noun", "described; the noun an adjective qualifies", "mevsûf; sıfatın nitelediği isim", 3),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1),
 "darib": G("darib", "ضَارِب", "ض ر ب", "noun", "striking, a striker (ism fāʿil of ḍaraba)", "vuran, vurucu (darabe'nin ism-i fâili)", 2),
 "shadid": G("shadid", "شَدِيد", "ش د د", "noun", "severe, strong", "şiddetli, güçlü", 2),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if (the conditional particle)", "eğer (şart edatı)", 2),
 "wasafa": G("wasafa", "وَصَفَ", "و ص ف", "verb", "to describe", "vasıflamak, nitelemek", 2),
 "bada": G("bada", "بَعْدَ", "ب ع د", "noun", "after", "sonra", 1),
 "lam-jazima": G("lam-jazima", "لَمْ", None, "part", "did not (the jussive negation)", "-medi (cezm eden nefiy)", 1),
 "darra": G("darra", "ضَرَّ", "ض ر ر", "verb", "to harm", "zarar vermek", 2),
 "sabiq": G("sabiq", "سَابِق", "س ب ق", "noun", "preceding, earlier", "önceki, geçen", 2),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam", 1, plural="رِجَال"),
 "ghulam": G("ghulam", "غُلَام", "غ ل م", "noun", "boy, servant", "oğlan, köle", 1, plural="غِلْمَان"),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "lam-letter": G("lam-letter", "لَام", None, "noun", "the letter lām; the lām (the article, the lām of jarr…)", "lâm harfi; lâm (ta'rîf lâmı, cer lâmı…)", 3),
 "ishtarata": G("ishtarata", "اِشْتَرَطَ", "ش ر ط", "verb", "to stipulate, to require as a condition", "şart koşmak", 3, form="VIII"),
 "li": G("li", "لِ", None, "prep", "to, for", "-e, için", 1),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not", "başka, gayr; değil", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "that which, what (relative)", "… olan şey (ism-i mevsûl)", 2),
 "dhakara": G("dhakara", "ذَكَرَ", "ذ ك ر", "verb", "to mention", "zikretmek, anmak", 1),
 "amr-name": G("amr-name", "عَمْرو", None, "propn", "ʿAmr (the grammarians' second stock name)", "Amr (nahivcilerin ikinci örnek adı)", 1),
 "ams": G("ams", "أَمْسِ", None, "noun", "yesterday (built on the kasra)", "dün (kesre üzere mebnî)", 2),
 "inda": G("inda", "عِنْدَ", "ع ن د", "noun", "at, with (a ẓarf)", "yanında, -de (zarf)", 1),
 "mujarrad": G("mujarrad", "مُجَرَّد", "ج ر د", "noun", "bare, stripped of", "mücerred, yalın", 3),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "itimad": G("itimad", "اِعْتِمَاد", "ع م د", "noun", "dependence, leaning on (masdar of iʿtamada)", "i'timâd, dayanma (i'temede'nin mastarı)", 4),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon", "üzerine, -e", 1),
 "mubtada": G("mubtada", "الْمُبْتَدَأ", "ب د أ", "noun", "the mubtadaʾ — the subject of a nominal sentence", "mübtedâ — isim cümlesinin öznesi", 2),
 "aw": G("aw", "أَوْ", None, "part", "or", "veya", 1),
 "dhu": G("dhu", "ذُو", None, "noun", "owner of, possessor of (one of the five nouns)", "sâhibi (beş isimden)", 2),
 "hal": G("hal", "حَال", "ح و ل", "noun", "state, condition; the ḥāl (circumstantial accusative)", "hâl, durum; hâl (durum zarfı)", 2),
 "zayd": G("zayd", "زَيْد", None, "propn", "Zayd (the grammarians' stock name)", "Zeyd (nahivcilerin örnek adı)", 1),
 "rakib": G("rakib", "رَاكِب", "ر ك ب", "noun", "riding, a rider", "binen, binici", 2),
 "istifham": G("istifham", "اِسْتِفْهَام", "ف ه م", "noun", "question, interrogation", "istifhâm, soru", 3),
 "qaim": G("qaim", "قَائِم", "ق و م", "noun", "standing", "ayakta duran, kâim", 2),
 "nafy": G("nafy", "نَفْي", "ن ف ي", "noun", "negation", "nefiy, olumsuzluk", 3),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (the negating mā)", "değil (nefiy mâ'sı)", 2),
 "nasb": G("nasb", "نَصْب", "ن ص ب", "noun", "the accusative (naṣb); putting in naṣb", "nasb (-i hâli); nasb etme", 2),
 "dalala": G("dalala", "دَلَالَة", "د ل ل", "noun", "indication, signification", "delâlet", 3),
 "istiqbal": G("istiqbal", "الِاسْتِقْبَال", "ق ب ل", "noun", "the future", "istikbâl, gelecek", 3),
 "tathniya": G("tathniya", "تَثْنِيَة", "ث ن ي", "noun", "the dual (making dual)", "tesniye, ikil", 3),
 "jam": G("jam", "جَمْع", "ج م ع", "noun", "plural", "cem', çoğul", 2),
 "mufrad": G("mufrad", "مُفْرَد", "ف ر د", "noun", "singular", "müfred, tekil", 2),
 "kadha": G("kadha", "كَذَا", None, "part", "likewise, so (كَ + ذَا)", "böylece, keza (ke + zâ)", 2),
 "thalatha": G("thalatha", "ثَلَاثَة", "ث ل ث", "noun", "three", "üç", 1),
 "wazn": G("wazn", "وَزْن", "و ز ن", "noun", "pattern, measure (wazn)", "vezin", 2, plural="أَوْزَان"),
 "mubalagha": G("mubalagha", "مُبَالَغَة", "ب ل غ", "noun", "intensification, exaggeration (mubālagha)", "mübalağa", 3),
 "faal": G("faal", "فَعَّال", "ف ع ل", "noun", "the pattern faʿʿāl (an intensive form)", "fa''âl vezni (mübalağa sîgası)", 4),
 "faul-wazn": G("faul-wazn", "فَعُول", "ف ع ل", "noun", "the pattern faʿūl (an intensive form)", "fa'ûl vezni (mübalağa sîgası)", 4),
 "mifal-wazn": G("mifal-wazn", "مِفْعَال", "ف ع ل", "noun", "the pattern mifʿāl (an intensive form)", "mif'âl vezni (mübalağa sîgası)", 4),
 "hadhihi": G("hadhihi", "هَذِهِ", None, "pron", "this (f.)", "bu (diş.)", 1),
 "mana": G("mana", "مَعْنًى", "ع ن ي", "noun", "meaning, sense", "mânâ", 2, plural="مَعَانٍ"),
 "rabi-fourth": G("rabi-fourth", "رَابِع", "ر ب ع", "noun", "fourth", "dördüncü", 2),
 "sifa": G("sifa", "صِفَة", "و ص ف", "noun", "adjective, attribute (ṣifa)", "sıfat", 2),
 "mushabbaha": G("mushabbaha", "مُشَبَّهَة", "ش ب ه", "noun", "resembling, likened — الصِّفَةُ الْمُشَبَّهَةُ, the adjective likened to the ism fāʿil", "müşebbehe, benzetilmiş — sıfat-ı müşebbehe", 4),
 "hiya": G("hiya", "هِيَ", None, "pron", "she, it", "o (diş.)", 1),
 "mutabar": G("mutabar", "مُعْتَبَر", "ع ب ر", "noun", "considered, regarded (ism mafʿūl of iʿtabara)", "mûteber, itibar edilen (i'tebera'nın ism-i mef'ûlü)", 4),
 "inna": G("inna", "إِنَّ", None, "part", "indeed, verily (puts its noun in naṣb)", "muhakkak, şüphesiz (ismini nasb eder)", 1),
 "hasan-adj": G("hasan-adj", "حَسَن", "ح س ن", "noun", "handsome, good", "güzel, iyi", 1),
 "wajh": G("wajh", "وَجْه", "و ج ه", "noun", "face; way, manner", "yüz; vecih, tarz", 2, plural="وُجُوه"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch12 gloss+morph ok", len(GLOSS_ADD), "verbs:", [k for k in ("amila", "jaa", "wasafa", "darra", "ishtarata", "dhakara", "kana") if k in mo["verbs"]], "missing morph:", [k for k in ("amila", "jaa", "wasafa", "darra", "ishtarata", "dhakara") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "شُرُوطُ عَمَلِ اسْمِ الْفَاعِلِ وَاسْمِ الْمَفْعُولِ وَالصِّفَةِ الْمُشَبَّهَةِ", "en": "The conditions under which the ism fāʿil, the ism mafʿūl and the ṣifa mushabbaha govern", "tr": "İsm-i fâil, ism-i mef'ûl ve sıfat-ı müşebbehenin amel şartları"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العوامل القياسية: اسم الفاعل واسم المفعول والصفة المشبهة", "الكافية لابن الحاجب — اسم الفاعل", "قطر الندى لابن هشام — إعمال اسم الفاعل"],
 "amil": "اسْمُ الْفَاعِلِ — raises a doer and puts an object in naṣb like its active verb; اسْمُ الْمَفْعُولِ — like its passive verb; الصِّفَةُ الْمُشَبَّهَةُ — like its verb, under the same conditions save the sense of time",
 "question": {
  "en": ["What does the ism fāʿil govern? The work of its ACTIVE verb — it raises a doer and puts an object in naṣb: ضَارِبٌ غُلَامَهُ.",
         "And the ism mafʿūl? The work of its PASSIVE verb — it raises a deputy doer: مَضْرُوبٌ غُلَامُهُ.",
         "What is the first condition for governing a detached doer or an object? That the participle is not a DIMINUTIVE (ضُوَيْرِب، مُضَيْرِب) and not DESCRIBED before it works (جَاءَنِي ضَارِبٌ شَدِيدٌ — the adjective has closed it).",
         "What if the description comes after the work? It does no harm: جَاءَنِي رَجُلٌ ضَارِبٌ غُلَامَهُ شَدِيدٌ.",
         "What changes when the participle carries the article? Nothing more is required: الضَّارِبُ غُلَامُهُ عَمْرًا أَمْسِ عِنْدَنَا — it governs on its own.",
         "And when it is bare of the article? It must LEAN (اعْتِمَاد) on something: a mubtadaʾ, a described noun or the owner of a ḥāl (جَاءَنِي زَيْدٌ رَاكِبًا غُلَامُهُ), a question (أَقَائِمٌ الزَّيْدَانِ) or a negation (مَا قَائِمٌ الزَّيْدَانِ).",
         "What does its naṣb of the object need besides? The sense of the PRESENT or the FUTURE — a participle meaning the past does not take an object in naṣb (it annexes it instead).",
         "Do the dual, the plural and the intensive forms govern too? Yes — the dual and the plural like the singular, and فَعَّال، فَعُول، مِفْعَال as well, without even the condition of time.",
         "What is the fourth governor? The ṢIFA MUSHABBAHA — the adjective likened to the ism fāʿil — which works like its verb under the same conditions, time excepted: زَيْدٌ حَسَنٌ وَجْهُهُ (handsome of face — the face is its doer).",
         "What does the engine READ here? The DabtEngine raises the noun after a governing participle as its doer, puts the noun after a present-sense participle in naṣb as its object, annexes the one after a past-sense participle, and reads a bare participle after a question or a negation as a mubtadaʾ whose doer stands for the khabar."],
  "tr": ["İsm-i fâil neye amel eder? MA'LÛM fiilinin ameline — fâil ref eder ve mef'ûl nasb eder: dâribün gulâmehu.",
         "Ya ism-i mef'ûl? MEÇHÛL fiilinin ameline — nâib-i fâil ref eder: madrûbün gulâmühu.",
         "Munfasıl fâilde veya mef'ûlde amelin ilk şartı nedir? Sîganın TASGÎR edilmemiş (duvayrib, mudayrib) ve amelden önce VASIFLANMAMIŞ olması (câenî dâribün şedîdün — sıfat onu kapatmıştır).",
         "Vasıf amelden sonra gelirse? Zarar vermez: câenî racülün dâribün gulâmehu şedîdün.",
         "Sîga lâm (harf-i ta'rîf) taşıyınca ne değişir? Başka şart aranmaz: ed-dâribü gulâmühu Amren emsi indenâ — tek başına amel eder.",
         "Lâmdan yalın olunca? Bir şeye DAYANMALI (i'timâd): mübtedâya, mevsûfa veya zilhâle (câenî Zeydün râkiben gulâmühu), istifhâma (e kâimün ez-Zeydâni) veya nefye (mâ kâimün ez-Zeydâni).",
         "Mef'ûlü nasb etmesi için başka ne gerekir? HÂL veya İSTİKBÂL mânâsı — mâzî mânâsındaki sîga mef'ûlü nasb etmez (onu muzâf alır).",
         "Tesniye, cem' ve mübalağa sîgaları da amel eder mi? Evet — tesniye ve cem' müfred gibi; fa''âl, fa'ûl, mif'âl de öyle, hem de zaman şartı olmadan.",
         "Dördüncü âmil nedir? SIFAT-I MÜŞEBBEHE — ism-i fâile benzetilen sıfat — fiili gibi, aynı şartlarla amel eder, zaman hariç: Zeydün hasenün vechühu (yüzü güzel — yüz onun fâilidir).",
         "Motor burada neyi OKUR? DabtEngine amel eden sîgadan sonraki ismi fâili olarak ref eder, hâl mânâlı sîgadan sonrakini mef'ûl olarak nasb eder, mâzî mânâlıdan sonrakini muzâfun ileyh yapar, istifhâm veya nefiyden sonraki yalın sîgayı fâili haber yerine geçen mübtedâ okur."],
 },
 "plain": {"en": "A participle can act like its verb: «striking his servant» raises a doer and takes an object. It may do so only when it is not a pet-form, not already qualified by an adjective, and — without «the» — only when it leans on a subject, a described noun, a question or a «not». The likened adjective does the same.",
           "tr": "Bir sıfat fiili gibi iş görebilir: «kölesine vuran» fâil alır, mef'ûl alır. Bunu ancak küçültülmemişse, önceden bir sıfatla nitelenmemişse ve — başında «el-» yoksa — bir özneye, bir mevsûfa, bir soruya ya da bir «değil»e dayanıyorsa yapar. Benzetilmiş sıfat (yüzü güzel) da aynısını yapar."},
 "explanation": {"en": "The second qiyāsī governor is the ism fāʿil, which works the work of its active verb; the third is the ism mafʿūl, which works the work of its passive verb. The condition of their governing the detached doer and the object is that they not be diminutives (ضُوَيْرِب، مُضَيْرِب) nor described (جَاءَنِي ضَارِبٌ شَدِيدٌ); a description after the work does not harm the earlier work (جَاءَنِي رَجُلٌ ضَارِبٌ غُلَامَهُ شَدِيدٌ). With the article nothing more is required (الضَّارِبُ غُلَامُهُ عَمْرًا أَمْسِ عِنْدَنَا); bare of it they must lean on a mubtadaʾ, a described noun or the owner of a ḥāl (جَاءَنِي زَيْدٌ رَاكِبًا غُلَامُهُ), a question (أَقَائِمٌ الزَّيْدَانِ) or a negation (مَا قَائِمٌ الزَّيْدَانِ). Their naṣb of the object requires the indication of the present or the future. Their dual and plural are like their singular, and so are the three intensive patterns فَعَّال، فَعُول، مِفْعَال, whose governing needs no sense of the present or future. The fourth is the ṣifa mushabbaha, which works the work of its verb under the conditions considered for the ism fāʿil, save the sense of time (زَيْدٌ حَسَنٌ وَجْهُهُ).",
                 "tr": "İkinci kıyâsî âmil ism-i fâildir, ma'lûm fiilinin amelini yapar; üçüncüsü ism-i mef'ûldür, meçhûl fiilinin amelini yapar. Munfasıl fâilde ve mef'ûlde amel etmelerinin şartı tasgîr edilmemiş (duvayrib, mudayrib) ve vasıflanmamış olmalarıdır (câenî dâribün şedîdün); amelden sonraki vasıf önceki amele zarar vermez (câenî racülün dâribün gulâmehu şedîdün). Lâm ile başka şart aranmaz (ed-dâribü gulâmühu Amren emsi indenâ); lâmdan yalın iseler mübtedâya, mevsûfa veya zilhâle (câenî Zeydün râkiben gulâmühu), istifhâma (e kâimün ez-Zeydâni) veya nefye (mâ kâimün ez-Zeydâni) dayanmaları şarttır. Mef'ûlü nasb etmeleri hâl veya istikbâle delâleti gerektirir. Tesniye ve cem'leri müfredleri gibidir; fa''âl, fa'ûl, mif'âl mübalağa vezinleri de öyledir ve amellerinde hâl-istikbâl mânâsı şart değildir. Dördüncüsü sıfat-ı müşebbehedir; ism-i fâilde mûteber şartlarla, zaman mânâsı hariç, fiilinin amelini yapar (Zeydün hasenün vechühu)."},
 "examples": [
  {"ar": "جَاءَنِي رَجُلٌ ضَارِبٌ غُلَامَهُ شَدِيدٌ", "en": "the ism fāʿil governing its object, then described", "tr": "mef'ûlüne amel eden, sonra vasıflanan ism-i fâil", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "جَاءَنِي ضَارِبٌ شَدِيدٌ", "en": "described first — it governs nothing", "tr": "önce vasıflanmış — amel etmez", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "الضَّارِبُ غُلَامُهُ عَمْرًا أَمْسِ عِنْدَنَا", "en": "with the article: doer, object, two ẓarfs — no further condition", "tr": "lâm ile: fâil, mef'ûl, iki zarf — başka şart yok", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "جَاءَنِي زَيْدٌ رَاكِبًا غُلَامُهُ", "en": "leaning on the owner of the ḥāl", "tr": "zilhâle dayanarak", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "أَقَائِمٌ الزَّيْدَانِ", "en": "leaning on the question — the doer stands for the khabar", "tr": "istifhâma dayanarak — fâil haberin yerini tutar", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "مَا قَائِمٌ الزَّيْدَانِ", "en": "leaning on the negation", "tr": "nefye dayanarak", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "فَعَّالٌ وَفَعُولٌ وَمِفْعَالٌ", "en": "the intensive patterns govern without the condition of time", "tr": "mübalağa vezinleri zaman şartı olmadan amel eder", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "زَيْدٌ حَسَنٌ وَجْهُهُ", "en": "the ṣifa mushabbaha raising its doer", "tr": "fâilini ref eden sıfat-ı müşebbehe", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
 ],
 "commonMistakes": [
  {"wrong": "جَاءَنِي ضَارِبٌ شَدِيدٌ غُلَامَهُ", "right": "جَاءَنِي ضَارِبٌ غُلَامَهُ شَدِيدٌ", "why": {"en": "a participle described before it works governs nothing — the object must come before the adjective", "tr": "amelden önce vasıflanan sîga amel etmez — mef'ûl sıfattan önce gelmelidir"}},
  {"wrong": "ضَارِبٌ غُلَامَهُ أَمْسِ", "right": "ضَارِبُ غُلَامِهِ أَمْسِ", "why": {"en": "a participle meaning the past does not put its object in naṣb — it annexes it", "tr": "mâzî mânâsındaki sîga mef'ûlünü nasb etmez — ona muzâf olur"}},
  {"wrong": "قَائِمٌ الزَّيْدَانِ", "right": "أَقَائِمٌ الزَّيْدَانِ", "why": {"en": "a bare participle must lean on something — a question, a negation, a mubtadaʾ, a described noun or the owner of a ḥāl", "tr": "yalın sîga bir şeye dayanmalıdır — soru, nefiy, mübtedâ, mevsûf veya zilhâl"}},
  {"wrong": "زَيْدٌ حَسَنٌ وَجْهَهُ", "right": "زَيْدٌ حَسَنٌ وَجْهُهُ", "why": {"en": "the ṣifa mushabbaha raises its doer; the face is the doer, not an object", "tr": "sıfat-ı müşebbehe fâilini ref eder; yüz fâildir, mef'ûl değil"}},
 ],
}
ADD_EN = (" Chapter 12 (print pp. 107-109): the ism fāʿil (s1) and the ism mafʿūl (s2) as governors; the condition of their governing — no diminutive, no "
          "description before the work (s3); with the article nothing more (s4); bare of it, the dependence on a mubtadaʾ, a described noun, the owner of a ḥāl, "
          "a question or a negation (s5); the sense of the present or the future for the naṣb of the object (s6); the dual, the plural and the three intensive "
          "patterns (s7); the ṣifa mushabbaha (s8). The print's ثلثة is given standard as ثَلَاثَة.")
ADD_TR = (" On ikinci bab (baskı s. 107-109): âmil olarak ism-i fâil (s1) ve ism-i mef'ûl (s2); amel şartı — tasgîr yok, amelden önce vasıf yok (s3); lâm ile başka şart "
          "yok (s4); lâmsız iken mübtedâya, mevsûfa, zilhâle, istifhâma veya nefye i'timâd (s5); mef'ûlün nasbı için hâl veya istikbâl mânâsı (s6); tesniye, cem' ve üç "
          "mübalağa vezni (s7); sıfat-ı müşebbehe (s8). Baskının ثلثة'si standart imlâyla ثَلَاثَة verildi.")
write_out(12, S, TITLE, ADD_EN, ADD_TR, "pp. 107-109", GLOSS_ADD, notes=(NOTE,),
          related=((IFA, [K]), (IMF, [K]), (SM, [K]), (K8, [K]), ("al-istifham", [K]), (HL, [K])))
report(12, S, GLOSS_ADD, (NOTE,))
