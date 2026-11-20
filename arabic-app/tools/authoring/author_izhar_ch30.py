# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 30: the FĀʾ in the KHABAR of the mubtadaʾ — obligatory after أَمَّا (أَمَّا زَيْدٌ فَمُنْطَلِقٌ)
# save for the poet's necessity (أَمَّا الْقِتَالُ لَا قِتَالَ لَدَيْكُمْ) or the hiding of the word «say» (فَأَمَّا الَّذِينَ اسْوَدَّتْ
# وُجُوهُهُمْ أَكَفَرْتُمْ, i.e. فَيُقَالُ لَهُمْ); allowed when the mubtadaʾ is a relative linked by a verb or an adverb, or a noun
# qualified by one, or a nakira so qualified, or a muḍāf to one of these, or كُلّ annexed to a nakira qualified by a single word
# or not qualified at all — and so when إِنَّ، أَنَّ، لٰكِنَّ enter upon it, unlike the other abrogators (الَّذِي يَأْتِينِي فَلَهُ
# دِرْهَمٌ، قُلْ إِنَّ الْمَوْتَ الَّذِي تَفِرُّونَ مِنْهُ فَإِنَّهُ مُلَاقِيكُمْ، كُلُّ رَجُلٍ فَلَهُ دِرْهَمٌ); elsewhere it is not allowed. Print pp. 130–131.
#   python3 author_izhar_ch30.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
FK = "fa-khabar-mubtada"; AMT = "amma-tafsiliyya"; MA = "ma-la-mushabbaha"; LNJ = "la-nafiya-lil-jins"; F9 = "augmented-babs"; IDH = "idha-shartiyya"; JS = "jumla-sifa"; PSV = "naib-al-fail"
K = "al-fa-fi-khabar-al-mubtada"
K29 = "khabar-al-mubtada-wa-ahkamuh"
TITLE = {"ar": "الْفَاءُ فِي خَبَرِ الْمُبْتَدَإِ: وُجُوبُهَا بَعْدَ أَمَّا وَجَوَازُهَا", "en": "The fāʾ in the khabar of the mubtadaʾ: obligatory after أَمَّا, and where it is allowed", "tr": "Mübtedânın haberinde fâ: emmâ'dan sonra vücûbu ve cevâzı"}

def nahw(punct=":", wa_=False):
    if wa_: return tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«and as in»", "«ve … gibi»", punct=punct, segments=wa("نَحْوُ", "nahw", "noun"))
    return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def falahu(): return tok("فَلَهُ", "li", "prep", [K, FK, HJ, MK], "الْفَاءُ دَاخِلَةٌ فِي الْخَبَرِ، وَاللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«then to him» — the fāʾ of the khabar; the fronted khabar.", "«ona … vardır» — haberin fâsı; öne alınmış haber.", segments=[seg("فَ", "fa", "conj"), seg("لَ", "li", "prep"), pr3ms()])
def dirham(punct="،"): return tok("دِرْهَمٌ", "dirham", "noun", [K, MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a dirham» — the delayed mubtada.", "«bir dirhem» — sona alınmış mübtedâ.", punct=punct)
def yatini(gr): return tok("يَأْتِينِي", "ata", "verb", [K] + gr + [MR, YM, MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«comes to me»", "«bana gelen»", segments=[seg("يَأْتِي", "ata", "verb"), seg("نِي", "pron-1s-obj", "pron")])
def fiddar(gr, punct=None): return [tok("فِي", "fi", "prep", [K] + gr + [HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"), tok("الدَّارِ", "dar", "noun", [K] + gr + [HJ], "مَجْرُورٌ بِفِي — الظَّرْفُ.", "«the house» — the adverbial phrase.", "«ev» — zarf.", punct=punct)]

# ----------- s1 — after أَمَّا the fāʾ is obligatory
S.append({"id": "s1", "translation": {"en": "And if the mubtadaʾ comes after «as for», the entering of the fāʾ into its khabar is obligatory — as in «as for Zayd, he is off» —", "tr": "Mübtedâ emmâ'dan sonra gelirse haberine fâ'nın girmesi vâcibdir — «Zeyd'e gelince, o gitmektedir» gibi —"},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, KN, INS, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، فِعْلُ الشَّرْطِ.", "«is»", "«olursa»"),
  tok("الْمُبْتَدَأُ", "mubtada", "noun", [K, KN], "اسْمُ كَانَ مَرْفُوعٌ.", "«the mubtadaʾ» — the ism of kāna.", "«mübtedâ» — kâne'nin ismi."),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID, KN], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — خَبَرُ كَانَ.", "«after» — the khabar of kāna.", "«sonra» — kâne'nin haberi."),
  tok("أَمَّا", "amma", "part", [K, ID, AMT], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ — حَرْفُ تَفْصِيلٍ.", "«as for» — the particle of detailing.", "«emmâ» — tafsîl harfi."),
  tok("وَجَبَ", "wajaba", "verb", [K, FL, INS], "فِعْلٌ مَاضٍ، جَوَابُ الشَّرْطِ.", "«it is obligatory» — the answer.", "«vâcib olur» — cevap."),
  tok("دُخُولُ", "dukhul", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the entering of»", "«girmesi»"),
  tok("الْفَاءِ", "fa", "conj", [K, ID, FK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the fāʾ»", "«fâ'nın»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«into»", "«-ne»"),
  tok("خَبَرِهِ", "khabar", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its khabar»", "«haberine»", punct="،", segments=[seg("خَبَرِ", "khabar", "noun"), pr3msi()]),
  nahw(),
  tok("أَمَّا", "amma", "part", [K, AMT, MK], "لَفْظٌ مَحْكِيٌّ: حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«… -e gelince»"),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, AMT], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  tok("فَمُنْطَلِقٌ", "muntaliq", "noun", [K, FK, MK, IFA], "الْفَاءُ وَاقِعَةٌ فِي الْخَبَرِ لِمَا فِي أَمَّا مِنْ مَعْنَى الشَّرْطِ، وَمُنْطَلِقٌ خَبَرٌ مَرْفُوعٌ.", "«then he is off» — the fāʾ of the khabar; the khabar.", "«o gitmektedir» — haberin fâsı; haber.", punct="،", segments=fa("مُنْطَلِقٌ", "muntaliq", "noun")),
 ]})
# ----------- s2 — save for the poet's necessity
S.append({"id": "s2", "translation": {"en": "save for the necessity of verse — as in his saying «as for fighting, there is no fighting with you» —", "tr": "şiir zarûreti hariç — şâirin «savaşa gelince, sizde savaş yok» sözündeki gibi —"},
 "tokens": [
  tok("إِلَّا", "illa", "part", [K, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«save»", "«ancak … hariç»"),
  tok("لِضَرُورَةِ", "darura", "noun", [K, HJ, ID, "istithna"], "اللَّامُ حَرْفُ جَرٍّ، وَضَرُورَةِ مَجْرُورٌ، مُضَافٌ — الْمُسْتَثْنَى.", "«for the necessity of»", "«zarûreti için»", segments=[seg("لِ", "li", "prep"), seg("ضَرُورَةِ", "darura", "noun")]),
  tok("الشِّعْرِ", "shir", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«verse»", "«şiir»", punct="،"),
  tok("كَقَوْلِهِ", "qawl", "noun", [K, HJ, ID, MSD], "الْكَافُ حَرْفُ جَرٍّ، وَقَوْلِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«as in his saying»", "«onun sözü gibi»", punct=":", segments=[seg("كَ", "ka", "prep"), seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("أَمَّا", "amma", "part", [K, AMT, MK], "لَفْظٌ مَحْكِيٌّ: حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«… -e gelince»"),
  tok("الْقِتَالُ", "qital", "noun", [K, MK, AMT, MSD], "مُبْتَدَأٌ مَرْفُوعٌ.", "«fighting» — the mubtada.", "«savaş» — mübtedâ."),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, LNJ, FK], "نَافِيَةٌ لِلْجِنْسِ — وَالْفَاءُ مَتْرُوكَةٌ لِلضَّرُورَةِ.", "«no» — the fāʾ dropped by necessity.", "«yok» — fâ zarûretle düşmüş."),
  tok("قِتَالَ", "qital", "noun", [K, LNJ, MSD], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«fighting» — the ism of lā.", "«savaş» — lâ'nın ismi."),
  tok("لَدَيْكُمْ", "lada", "noun", [K, MF, ID, LNJ, MK], "ظَرْفٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرُ لَا، وَالْجُمْلَةُ خَبَرُ الْقِتَالُ.", "«with you» — the khabar of lā; the clause the khabar of the mubtada.", "«sizde» — lâ'nın haberi; cümle mübtedânın haberi.", punct="،", segments=[seg("لَدَيْ", "lada", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
 ]})
# ----------- s3 — or for the hiding of «say»
S.append({"id": "s3", "translation": {"en": "or for the hiding of the word «say» — as in His saying, exalted be He: «as for those whose faces are blackened: did you disbelieve?», that is: «it is said to them: did you disbelieve?».", "tr": "ya da «kavl» gizlendiği için — Allah Teâlâ'nın «yüzleri kararanlara gelince: inkâr mı ettiniz?» sözündeki gibi; yani: «onlara denir: inkâr mı ettiniz?»."},
 "tokens": [
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("لِإِضْمَارِ", "idmar", "noun", [K, AT, HJ, ID, MSD, F4], "اللَّامُ حَرْفُ جَرٍّ، وَإِضْمَارِ مَجْرُورٌ، مَعْطُوفٌ عَلَى ضَرُورَةِ، مُضَافٌ.", "«for the hiding of»", "«gizlenmesi için»", segments=[seg("لِ", "li", "prep"), seg("إِضْمَارِ", "idmar", "noun")]),
  tok("الْقَوْلِ", "qawl", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the word say»", "«kavlin»", punct="،"),
  tok("كَقَوْلِهِ", "qawl", "noun", [K, HJ, ID, MSD], "الْكَافُ حَرْفُ جَرٍّ، وَقَوْلِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«as in His saying»", "«O'nun sözü gibi»", segments=[seg("كَ", "ka", "prep"), seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("تَعَالَى", "taala", "part", [K], "فِعْلٌ مَاضٍ لِلتَّعْظِيمِ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«exalted be He»", "«Teâlâ»", punct=":"),
  tok("فَأَمَّا", "amma", "part", [K, AMT, MK], "لَفْظٌ مَحْكِيٌّ: الْفَاءُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«… -e gelince»", segments=fa("أَمَّا", "amma", "part")),
  tok("الَّذِينَ", "alladhina", "pron", [K, MAW, MK, AMT], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ.", "«those who» — the mubtada.", "«… olanlar» — mübtedâ."),
  tok("اسْوَدَّتْ", "iswadda", "verb", [K, MAW, FL, F9], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — صِلَةُ الْمَوْصُولِ.", "«are blackened» — the relative clause.", "«karardı» — sıla."),
  tok("وُجُوهُهُمْ", "wajh", "noun", [K, FL, ID, JT], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«their faces» — the doer; the returner.", "«yüzleri» — fâil; âid.", segments=[seg("وُجُوهُ", "wajh", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("أَكَفَرْتُمْ", "kafara", "verb", [K, IST, FL, HT, FK], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَكَفَرْتُمْ فِعْلٌ وَفَاعِلٌ — مَقُولُ قَوْلٍ مَحْذُوفٍ، وَالْجُمْلَةُ الْمَحْذُوفَةُ خَبَرٌ، وَالْفَاءُ مَتْرُوكَةٌ مَعَ الْقَوْلِ.", "«did you disbelieve?» — the said of a hidden «it is said»; its fāʾ hidden with it.", "«inkâr mı ettiniz?» — gizli kavlin makûlü; fâ onunla gizlenmiş.", punct="،", segments=[seg("أَ", "a-istifham", "part"), seg("كَفَرْ", "kafara", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»", punct=":"),
  tok("فَيُقَالُ", "qala", "verb", [K, FK, HT, PSV, HV, MR], "الْفَاءُ دَاخِلَةٌ فِي الْخَبَرِ، وَيُقَالُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — الْقَوْلُ الْمُقَدَّرُ.", "«then it is said» — the restored saying with its fāʾ.", "«o zaman denir» — takdîr edilen kavl ve fâsı.", segments=fa("يُقَالُ", "qala", "verb")),
  tok("لَهُمْ", "li", "prep", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَهُمْ فِي مَحَلِّ جَرٍّ.", "«to them»", "«onlara»", segments=[seg("لَ", "li", "prep"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("أَكَفَرْتُمْ", "kafara", "verb", [K, IST, FL, PSV], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَكَفَرْتُمْ فِعْلٌ وَفَاعِلٌ — نَائِبُ فَاعِلِ يُقَالُ.", "«did you disbelieve?» — the deputy doer of «it is said».", "«inkâr mı ettiniz?» — yukâlu'nun nâib-i fâili.", punct="؟", segments=[seg("أَ", "a-istifham", "part"), seg("كَفَرْ", "kafara", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
 ]})
# ----------- s4 — where the fāʾ is allowed: the seven shapes of the mubtadaʾ
S.append({"id": "s4", "translation": {"en": "And if it is a relative noun linked by a verb or an adverb, or a noun qualified by one, or an indefinite qualified by one of the two, or annexed to one of them, or the word «every» annexed to an indefinite qualified by a single word or not qualified at all, the entering of the fāʾ into its khabar is allowed;", "tr": "Mübtedâ fiil veya zarfla sılalanmış ism-i mevsûl, ya da onunla vasıflanmış isim, ya da ikisinden biriyle vasıflanmış nekre, ya da bunlardan birine muzâf, ya da müfredle vasıflanmış veya hiç vasıflanmamış nekreye muzâf «küll» lafzı olursa haberine fâ'nın girmesi câizdir;"},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, KN, INS, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْمُبْتَدَأُ.", "«it is» — the mubtadaʾ.", "«olursa» — mübtedâ."),
  tok("اسْمًا", "ism", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a noun»", "«isim»"),
  tok("مَوْصُولًا", "mawsul", "noun", [K, NA, IMF, MAW], "نَعْتٌ مَنْصُوبٌ.", "«relative»", "«mevsûl»"),
  tok("بِفِعْلٍ", "fil", "noun", [K, HJ, JS], "الْبَاءُ حَرْفُ جَرٍّ، وَفِعْلٍ مَجْرُورٌ — صِلَتُهُ فِعْلٌ.", "«by a verb»", "«fiille»", segments=[seg("بِ", "bi", "prep"), seg("فِعْلٍ", "fil", "noun")]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("ظَرْفٍ", "zarf", "noun", [K, AT, MF], "مَعْطُوفٌ مَجْرُورٌ.", "«an adverb»", "«zarfla»", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مَوْصُوفًا", "mawsuf", "noun", [K, AT, IMF, NA], "مَعْطُوفٌ عَلَى مَوْصُولًا مَنْصُوبٌ.", "«qualified»", "«vasıflanmış»"),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — بِالْمَوْصُولِ.", "«by it» — by such a relative.", "«onunla» — o mevsûlle.", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("نَكِرَةً", "nakira", "noun", [K, AT, KN], "مَعْطُوفٌ مَنْصُوبٌ.", "«an indefinite»", "«nekre»"),
  tok("مَوْصُوفَةً", "mawsuf", "noun", [K, NA, IMF, JS], "نَعْتٌ مَنْصُوبٌ.", "«qualified»", "«vasıflanmış»"),
  tok("بِأَحَدِهِمَا", "ahad", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَأَحَدِ مَجْرُورٌ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ — الْفِعْلُ أَوِ الظَّرْفُ.", "«by one of the two» — the verb or the adverb.", "«ikisinden biriyle» — fiil ya da zarf.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("أَحَدِ", "ahad", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("مُضَافًا", "mudaf", "noun", [K, AT, IMF, ID], "مَعْطُوفٌ مَنْصُوبٌ.", "«annexed»", "«muzâf»"),
  tok("إِلَيْهَا", "ila", "prep", [K, HJ], "إِلَى حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — إِلَى الْمَذْكُورَاتِ.", "«to one of them» — to the aforesaid.", "«onlara» — sayılanlara.", punct="،", segments=[seg("إِلَيْ", "ila", "prep"), pr3fs()]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("لَفْظَ", "lafz", "noun", [K, AT, ID, KN], "مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«the word»", "«lafzı»"),
  tok("كُلٍّ", "kull", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«every»", "«küll»"),
  tok("مُضَافًا", "mudaf", "noun", [K, "hal", IMF, ID], "حَالٌ مَنْصُوبٌ.", "«annexed»", "«muzâf olarak»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("نَكِرَةٍ", "nakira", "noun", [K, HJ], "مَجْرُورٌ بِإِلَى.", "«an indefinite»", "«nekreye»"),
  tok("مَوْصُوفَةٍ", "mawsuf", "noun", [K, NA, IMF], "نَعْتٌ مَجْرُورٌ.", "«qualified»", "«vasıflanmış»"),
  tok("بِمُفْرَدٍ", "mufrad", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَمُفْرَدٍ مَجْرُورٌ.", "«by a single word»", "«müfredle»", segments=[seg("بِ", "bi", "prep"), seg("مُفْرَدٍ", "mufrad", "noun")]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("غَيْرِ", "ghayr", "noun", [K, AT, ID], "مَعْطُوفٌ عَلَى مَوْصُوفَةٍ مَجْرُورٌ، مُضَافٌ.", "«not»", "«olmayan»"),
  tok("مَوْصُوفَةٍ", "mawsuf", "noun", [K, ID, IMF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«qualified»", "«vasıflanmış»"),
  tok("أَصْلًا", "asl", "noun", [K, MF], "مَنْصُوبٌ عَلَى الظَّرْفِيَّةِ — الْبَتَّةَ.", "«at all»", "«hiç»", punct="،"),
  tok("جَازَ", "jaaza", "verb", [K, FL, INS, HV], "فِعْلٌ مَاضٍ، جَوَابُ الشَّرْطِ.", "«it is allowed» — the answer.", "«câiz olur» — cevap."),
  tok("دُخُولُ", "dukhul", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the entering of»", "«girmesi»"),
  tok("الْفَاءِ", "fa", "conj", [K, ID, FK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the fāʾ»", "«fâ'nın»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«into»", "«-ne»"),
  tok("خَبَرِهِ", "khabar", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its khabar»", "«haberine»", punct="،", segments=[seg("خَبَرِ", "khabar", "noun"), pr3msi()]),
 ]})
# ----------- s5 — and so after إِنَّ، أَنَّ، لٰكِنَّ, unlike the other abrogators
S.append({"id": "s5", "translation": {"en": "and so too when «inna», «anna» and «lākinna» enter upon it — unlike the other abrogators of the mubtadaʾ, be they particle or verb —", "tr": "inne, enne ve lâkinne onun üzerine girdiğinde de böyledir — mübtedânın diğer nâsihlerinin aksine, harf olsun fiil olsun —"},
 "tokens": [
  tok("وَكَذَا", "kadha", "part", [K, AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ حَرْفُ جَرٍّ، وَذَا فِي مَحَلِّ جَرٍّ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: الْحُكْمُ كَذَا.", "«and so too»", "«ve böyledir»", segments=wa("كَذَا", "kadha", "part")),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-diğinde»"),
  tok("دَخَلَ", "dakhala", "verb", [K, FL, IDH], "فِعْلٌ مَاضٍ، فِعْلُ الشَّرْطِ.", "«enters»", "«girdiğinde»"),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — عَلَى الْمُبْتَدَإِ.", "«upon it» — upon the mubtada.", "«onun üzerine» — mübtedânın.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("إِنَّ", "inna", "part", [K, FL, IN], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ، فَاعِلُ دَخَلَ.", "«inna» — the doer of «enters».", "«inne» — dehale'nin fâili."),
  tok("وَأَنَّ", "anna", "part", [K, AT, IN], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and anna»", "«ve enne»", segments=wa("أَنَّ", "anna", "part")),
  tok("وَلٰكِنَّ", "lakinna", "part", [K, AT, IN], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and lākinna»", "«ve lâkinne»", punct="،", segments=wa("لٰكِنَّ", "lakinna", "part")),
  tok("بِخِلَافِ", "khilaf", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَخِلَافِ مَجْرُورٌ، مُضَافٌ.", "«unlike»", "«aksine»", segments=[seg("بِ", "bi", "prep"), seg("خِلَافِ", "khilaf", "noun")]),
  tok("سَائِرِ", "sair-rest", "noun", [K, ID, IFA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the rest of»", "«diğer»"),
  tok("نَوَاسِخِ", "nasikh", "noun", [K, ID, JT, IFA, KN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — كَانَ وَأَخَوَاتُهَا وَظَنَّ وَأَخَوَاتُهَا وَمَا وَلَا.", "«the abrogators of» — kāna, ẓanna, mā, lā.", "«nâsihlerinin» — kâne, zanne, mâ, lâ."),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mubtadaʾ»", "«mübtedânın»", punct="،"),
  tok("حَرْفًا", "harf", "noun", [K, KN], "خَبَرُ كَانَ مُقَدَّمٌ مَنْصُوبٌ.", "«a particle» — the fronted khabar of kāna.", "«harf» — kâne'nin öne alınmış haberi."),
  tok("كَانَ", "kana", "verb", [K, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — النَّاسِخُ.", "«be it» — the abrogator.", "«olsun» — nâsih."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("فِعْلًا", "fil", "noun", [K, AT, KN], "مَعْطُوفٌ عَلَى حَرْفًا مَنْصُوبٌ.", "«a verb»", "«fiil»", punct="،"),
 ]})
# ----------- s6 — examples: the relative; the Qurʾānic إِنَّ
S.append({"id": "s6", "translation": {"en": "as in «he who comes to me, and (he who is) in the house: to him a dirham», and His saying, exalted be He: «say: the death from which you flee — it will surely meet you»,", "tr": "«bana gelen ve evde olan: ona bir dirhem vardır» gibi; ve Allah Teâlâ'nın «de ki: kaçtığınız ölüm, muhakkak o size kavuşacaktır» sözü gibi,"},
 "tokens": [
  nahw(),
  tok("الَّذِي", "alladhi", "pron", [K, MAW, MK, FK], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ — مَوْصُولٌ بِفِعْلٍ.", "«he who» — the mubtada, a relative linked by a verb.", "«… olan» — mübtedâ; fiille sılalanmış mevsûl."),
  yatini([MAW]),
  tok("وَفِي", "fi", "prep", [K, AT, HJ, MAW], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — صِلَةُ مَوْصُولٍ مُقَدَّرٍ: وَالَّذِي فِي الدَّارِ.", "«and (he who is) in» — the second relative's adverbial link.", "«ve … -de olan» — ikinci mevsûlün zarf sılası.", segments=wa("فِي", "fi", "prep")),
  tok("الدَّارِ", "dar", "noun", [K, HJ, MAW], "مَجْرُورٌ بِفِي — الظَّرْفُ.", "«the house»", "«ev»"),
  falahu(),
  dirham(),
  tok("وَقَوْلِهِ", "qawl", "noun", [K, AT, ID, MSD], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِهِ مَعْطُوفٌ عَلَى الْمَحْكِيِّ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and His saying»", "«ve O'nun sözü»", segments=[seg("وَ", "wa", "conj"), seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("تَعَالَى", "taala", "part", [K], "فِعْلٌ مَاضٍ لِلتَّعْظِيمِ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«exalted be He»", "«Teâlâ»", punct=":"),
  tok("قُلْ", "qala", "verb", [K, "imperative-amr", HV], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«say»", "«de ki»", punct=":"),
  tok("إِنَّ", "inna", "part", [K, IN, FK], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — دَاخِلٌ عَلَى الْمُبْتَدَإِ الْمَوْصُولِ.", "«surely» — entering upon the relative mubtada.", "«muhakkak» — mevsûl mübtedâya girmiş."),
  tok("الْمَوْتَ", "mawt", "noun", [K, IN, MSD], "اسْمُ إِنَّ مَنْصُوبٌ.", "«death» — the ism of inna.", "«ölüm» — inne'nin ismi."),
  tok("الَّذِي", "alladhi", "pron", [K, MAW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ، نَعْتٌ لِلْمَوْتِ.", "«which» — a relative qualifying «death».", "«… olan» — ölümün sıfatı mevsûl."),
  tok("تَفِرُّونَ", "farra", "verb", [K, MAW, FL, MR, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — صِلَةُ الْمَوْصُولِ.", "«you flee» — the relative clause.", "«kaçtığınız» — sıla.", segments=[seg("تَفِرُّ", "farra", "verb"), seg("ونَ", "pron-2mp", "pron")]),
  tok("مِنْهُ", "min", "prep", [K, HJ, MAW], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«from which» — the returner.", "«ondan» — âid.", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("فَإِنَّهُ", "inna", "part", [K, FK, IN, AT], "الْفَاءُ دَاخِلَةٌ فِي خَبَرِ إِنَّ لِكَوْنِ اسْمِهَا مَوْصُولًا، وَإِنَّ حَرْفُ تَوْكِيدٍ، وَالْهَاءُ اسْمُهَا.", "«then surely it» — the fāʾ in the khabar of inna; the second inna with its pronoun ism.", "«muhakkak o» — inne'nin haberine giren fâ; ikinci inne ve zamir ismi.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("مُلَاقِيكُمْ", "mulaqi", "noun", [K, IN, ID, IFA, "form-iii-verbs"], "خَبَرُ إِنَّ الثَّانِيَةِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وَجُمْلَةُ إِنَّ الثَّانِيَةِ خَبَرُ الْأُولَى.", "«will meet you» — the second inna's khabar; its clause the first's khabar.", "«size kavuşacaktır» — ikinci inne'nin haberi; cümlesi ilkinin haberi.", punct="،", segments=[seg("مُلَاقِي", "mulaqi", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
 ]})
# ----------- s7 — the indefinite, the muḍāf, كُلّ; elsewhere not allowed
S.append({"id": "s7", "translation": {"en": "and as in «a man who comes to me, and (one) in the house: to him a dirham», «the servant of a man who comes to me, or (who is) in the house: to him a dirham», «every learned man: to him a dirham» and «every man: to him a dirham»; and in other than these it is not allowed.", "tr": "«bana gelen ve evde olan bir adam: ona bir dirhem vardır», «bana gelen veya evde olan bir adamın kölesi: ona bir dirhem vardır», «her âlim adam: ona bir dirhem vardır» ve «her adam: ona bir dirhem vardır» gibi; bunların dışında câiz değildir."},
 "tokens": [
  nahw(wa_=True),
  tok("رَجُلٌ", "rajul", "noun", [K, MK, JS, FK], "مُبْتَدَأٌ مَرْفُوعٌ — نَكِرَةٌ مَوْصُوفَةٌ بِالْفِعْلِ.", "«a man» — the mubtada, an indefinite qualified by a verb.", "«bir adam» — mübtedâ; fiille vasıflanmış nekre."),
  yatini([JS, NA]),
  tok("وَفِي", "fi", "prep", [K, AT, HJ, JS], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — الظَّرْفُ صِفَةٌ ثَانِيَةٌ.", "«and in» — the adverb as a second qualifier.", "«ve … -de» — ikinci sıfat olan zarf.", segments=wa("فِي", "fi", "prep")),
  tok("الدَّارِ", "dar", "noun", [K, HJ, JS], "مَجْرُورٌ بِفِي.", "«the house»", "«ev»"),
  falahu(),
  dirham(),
  tok("وَغُلَامُ", "ghulam", "noun", [K, AT, MK, ID, FK], "الْوَاوُ عَاطِفَةٌ، وَغُلَامُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — مُضَافٌ إِلَى النَّكِرَةِ الْمَوْصُوفَةِ.", "«and the servant of» — the mubtada, annexed to the qualified indefinite.", "«ve … kölesi» — mübtedâ; vasıflanmış nekreye muzâf.", segments=wa("غُلَامُ", "ghulam", "noun")),
  tok("رَجُلٍ", "rajul", "noun", [K, ID, JS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نَكِرَةٌ مَوْصُوفَةٌ.", "«a man»", "«bir adamın»"),
  yatini([JS, NA]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  *fiddar([JS, AT]),
  falahu(),
  dirham(),
  tok("وَكُلُّ", "kull", "noun", [K, AT, MK, ID, FK], "الْوَاوُ عَاطِفَةٌ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and every» — the mubtada.", "«ve her» — mübtedâ.", segments=wa("كُلُّ", "kull", "noun")),
  tok("رَجُلٍ", "rajul", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نَكِرَةٌ.", "«man»", "«adam»"),
  tok("عَالِمٍ", "alim-scholar", "noun", [K, NA, IFA], "نَعْتٌ مَجْرُورٌ — الْمُفْرَدُ.", "«learned» — the single-word qualifier.", "«âlim» — müfred sıfat."),
  falahu(),
  dirham(),
  tok("وَكُلُّ", "kull", "noun", [K, AT, MK, ID, FK], "الْوَاوُ عَاطِفَةٌ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and every» — the mubtada.", "«ve her» — mübtedâ.", segments=wa("كُلُّ", "kull", "noun")),
  tok("رَجُلٍ", "rajul", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نَكِرَةٌ غَيْرُ مَوْصُوفَةٍ.", "«man» — an unqualified indefinite.", "«adam» — vasıfsız nekre."),
  falahu(),
  dirham(),
  tok("وَفِي", "fi", "prep", [K, AT, HJ], "الْوَاوُ لِلِاسْتِئْنَافِ، وَفِي حَرْفُ جَرٍّ.", "«and in»", "«ve … -de»", segments=wa("فِي", "fi", "prep")),
  tok("غَيْرِهَا", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — غَيْرِ هٰذِهِ الْمَوَاضِعِ.", "«other than these»", "«bunların dışında»", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3fs()]),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«değildir»"),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV, MR, LN], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الدُّخُولُ.", "«it is allowed» — the entering.", "«câiz» — giriş.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "darura": G("darura", "ضَرُورَة", "ض ر ر", "noun", "necessity — the poet's licence", "zarûret — şiir zarûreti", 3, plural="ضَرُورَات"),
 "iswadda": G("iswadda", "اِسْوَدَّ", "س و د", "verb", "to turn black, be blackened (form IX)", "kararmak, siyahlaşmak (IX. bab)", 4, form="IX"),
 "nasikh": G("nasikh", "نَاسِخ", "ن س خ", "noun", "an abrogator — a governor that cancels the mubtadaʾ–khabar nexus (kāna, inna, ẓanna …)", "nâsih — mübtedâ-haber bağını bozan âmil (kâne, inne, zanne …)", 4, plural="نَوَاسِخ"),
 "mulaqi": G("mulaqi", "مُلَاقٍ", "ل ق ي", "noun", "meeting, one who meets (active participle of form III)", "kavuşan, karşılaşan (III. babın ism-i fâili)", 3),
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
put_morph(mo, "iswadda", {"bab": "الْبَابُ التَّاسِعُ اِفْعَلَّ — مُضَاعَفٌ", "wazn": "اِفْعَلَّ يَفْعَلُّ", "masdar": "اِسْوِدَاد", "ismFail": "مُسْوَدّ",
 "mazi": ["اِسْوَدَّ", "اِسْوَدَّا", "اِسْوَدُّوا", "اِسْوَدَّتْ", "اِسْوَدَّتَا", "اِسْوَدَدْنَ", "اِسْوَدَدْتَ", "اِسْوَدَدْتُمَا", "اِسْوَدَدْتُمْ", "اِسْوَدَدْتِ", "اِسْوَدَدْتُمَا", "اِسْوَدَدْتُنَّ", "اِسْوَدَدْتُ", "اِسْوَدَدْنَا"],
 "mudari": ["يَسْوَدُّ", "يَسْوَدَّانِ", "يَسْوَدُّونَ", "تَسْوَدُّ", "تَسْوَدَّانِ", "يَسْوَدِدْنَ", "تَسْوَدُّ", "تَسْوَدَّانِ", "تَسْوَدُّونَ", "تَسْوَدِّينَ", "تَسْوَدَّانِ", "تَسْوَدِدْنَ", "أَسْوَدُّ", "نَسْوَدُّ"],
 "amr": ["اِسْوَدَّ", "اِسْوَدَّا", "اِسْوَدُّوا", "اِسْوَدِّي", "اِسْوَدَّا", "اِسْوَدِدْنَ"], "mansub": "يَسْوَدَّ", "majzum": "يَسْوَدَّ", "majzum2": "تَسْوَدَّ",
 "note": "اِسْوَدَّ يَسْوَدُّ اِسْوِدَادًا: صَارَ أَسْوَدَ — مِنَ الْبَابِ التَّاسِعِ لِلْأَلْوَانِ وَالْعُيُوبِ، لَازِمٌ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch30 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "ata", "farra", "qala", "kafara", "wajaba", "dakhala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْفَاءُ فِي خَبَرِ الْمُبْتَدَإِ: وُجُوبُهَا بَعْدَ أَمَّا وَمَوَاضِعُ جَوَازِهَا", "en": "The fāʾ in the khabar of the mubtadaʾ: obligatory after أَمَّا, and the places where it is allowed", "tr": "Mübtedânın haberinde fâ: emmâ'dan sonra vücûbu ve cevâz yerleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المرفوعات: خبر المبتدأ والفاء فيه", "الكافية لابن الحاجب — الخبر بعد أمّا", "مغني اللبيب لابن هشام — أمّا والفاء"],
 "amil": "after أَمَّا the fāʾ must enter the khabar (أَمَّا زَيْدٌ فَمُنْطَلِقٌ) — dropped only by the poet's necessity (أَمَّا الْقِتَالُ لَا قِتَالَ لَدَيْكُمْ) or because the word «say» is hidden with it (فَأَمَّا الَّذِينَ اسْوَدَّتْ وُجُوهُهُمْ أَكَفَرْتُمْ, i.e. فَيُقَالُ لَهُمْ); the fāʾ MAY enter when the mubtadaʾ is a relative linked by a verb or an adverb, a noun qualified by such a relative, a nakira qualified by a verb or an adverb, a muḍāf to one of these, or كُلّ annexed to a nakira qualified by a single word or unqualified — and still when إِنَّ، أَنَّ، لٰكِنَّ enter upon it, not after kāna, ẓanna, mā or lā (الَّذِي يَأْتِينِي فَلَهُ دِرْهَمٌ، قُلْ إِنَّ الْمَوْتَ الَّذِي تَفِرُّونَ مِنْهُ فَإِنَّهُ مُلَاقِيكُمْ، كُلُّ رَجُلٍ فَلَهُ دِرْهَمٌ); elsewhere it is not allowed",
 "question": {
  "en": ["When must the fāʾ enter the khabar? When the mubtadaʾ follows أَمَّا: أَمَّا زَيْدٌ فَمُنْطَلِقٌ — the fāʾ answers the condition folded into أَمَّا.",
         "When is it dropped after أَمَّا? For the poet's necessity (أَمَّا الْقِتَالُ لَا قِتَالَ لَدَيْكُمْ), or because the word «say» is hidden together with it: فَأَمَّا الَّذِينَ اسْوَدَّتْ وُجُوهُهُمْ أَكَفَرْتُمْ, that is فَيُقَالُ لَهُمْ أَكَفَرْتُمْ.",
         "Where MAY the fāʾ enter? When the mubtadaʾ is general and its qualifier verb-like, so that it resembles a condition: a relative linked by a verb or an adverb (الَّذِي يَأْتِينِي، الَّذِي فِي الدَّارِ), a noun qualified by such a relative, a nakira qualified by a verb or an adverb (رَجُلٌ يَأْتِينِي), a muḍāf to one of these (غُلَامُ رَجُلٍ يَأْتِينِي), or كُلّ annexed to a nakira qualified by a single word or not at all (كُلُّ رَجُلٍ عَالِمٍ، كُلُّ رَجُلٍ).",
         "Does an abrogator cancel this licence? Not إِنَّ، أَنَّ، لٰكِنَّ (قُلْ إِنَّ الْمَوْتَ الَّذِي تَفِرُّونَ مِنْهُ فَإِنَّهُ مُلَاقِيكُمْ); but after the other abrogators, particle (مَا، لَا) or verb (كَانَ، ظَنَّ), the fāʾ may not enter.",
         "And elsewhere? Not allowed: زَيْدٌ فَمُنْطَلِقٌ is wrong — the fāʾ needs the condition-like mubtadaʾ or أَمَّا.",
         "What does the engine READ here? The DabtEngine raises the noun after أَمَّا as the mubtadaʾ and reads the fāʾ-initial word after it as its khabar, keeps the inert quoted particles (أَمَّا، إِنَّ، أَنَّ، لٰكِنَّ) at the author's form, reads فَلَهُ دِرْهَمٌ as a fronted khabar with a delayed mubtadaʾ, and reads the Qurʾānic citation as the source prints it."],
  "tr": ["Fâ habere ne zaman girmek zorundadır? Mübtedâ emmâ'dan sonra gelince: emmâ Zeydün fe-muntalikun — fâ, emmâ'daki şart mânâsının cevâbıdır.",
         "Emmâ'dan sonra ne zaman düşer? Şiir zarûretiyle (emmâ'l-kıtâlü lâ kıtâle ledeykum) ya da «kavl» onunla birlikte gizlendiği için: fe-emme'llezîne'svedded vucûhuhum e-kefertum, yani fe-yukâlu lehum e-kefertum.",
         "Fâ nerede girEBİLİR? Mübtedâ umûmî ve sıfatı fiil gibi olup şarta benzediğinde: fiil veya zarfla sılalanmış mevsûl (ellezî ye'tînî, ellezî fi'd-dâr), böyle bir mevsûlle vasıflanmış isim, fiil veya zarfla vasıflanmış nekre (racülün ye'tînî), bunlardan birine muzâf (gulâmu racülin ye'tînî) ya da müfredle vasıflanmış veya vasıfsız nekreye muzâf küll (küllü racülin âlimin, küllü racülin).",
         "Nâsih bu cevâzı kaldırır mı? İnne, enne, lâkinne kaldırmaz (kul inne'l-mevte'llezî tefirrûne minhu fe-innehû mülâkîkum); ama diğer nâsihlerden — harf (mâ, lâ) veya fiil (kâne, zanne) — sonra fâ giremez.",
         "Başka yerde? Câiz değildir: Zeydün fe-muntalikun yanlıştır — fâ, şarta benzeyen mübtedâyı veya emmâ'yı ister.",
         "Motor burada neyi OKUR? DabtEngine emmâ'dan sonraki ismi mübtedâ olarak ref' eder, ardındaki fâ ile başlayan kelimeyi haberi okur; alıntılanan âtıl edatları (emmâ, inne, enne, lâkinne) yazarın şeklinde tutar; fe-lehû dirhemün'ü sona alınmış mübtedâlı öne alınmış haber okur; Kur'ân alıntısını kaynağın bastığı gibi okur."],
 },
 "plain": {"en": "After «as for» the predicate must start with «then» (fa): «as for Zayd, then he is off». Poets may drop it, and it hides when «it is said» is left out. It may also start the predicate when the subject is a general «he who…», «a man who…», or «every man…», even under «inna», but not under other verbs or particles.",
           "tr": "«-e gelince» (emmâ) den sonra yüklem «fe» ile başlamalıdır: «Zeyd'e gelince, o gitmektedir». Şair bunu düşürebilir; «denir» gizlenince fe de gizlenir. Özne «… olan kimse», «… bir adam», «her adam» gibi genel olunca da fe gelebilir; inne altında bile, ama başka fiil ve edatlar altında gelmez."},
 "explanation": {"en": "When the mubtadaʾ follows أَمَّا, the fāʾ must enter its khabar (أَمَّا زَيْدٌ فَمُنْطَلِقٌ), because أَمَّا holds the sense of a condition and the fāʾ is the answer's mark. It is left out only for the poet's necessity (أَمَّا الْقِتَالُ لَا قِتَالَ لَدَيْكُمْ) or because the word «say» is hidden and the fāʾ goes with it (فَأَمَّا الَّذِينَ اسْوَدَّتْ وُجُوهُهُمْ أَكَفَرْتُمْ, i.e. فَيُقَالُ لَهُمْ). The fāʾ MAY enter the khabar when the mubtadaʾ is a relative noun linked by a verb or an adverb, a noun qualified by such a relative, a nakira qualified by a verb or an adverb, a muḍāf to any of these, or كُلّ annexed to a nakira qualified by a single word or unqualified — the mubtadaʾ is then general and its qualifier resembles a condition. This licence survives إِنَّ، أَنَّ، لٰكِنَّ (قُلْ إِنَّ الْمَوْتَ الَّذِي تَفِرُّونَ مِنْهُ فَإِنَّهُ مُلَاقِيكُمْ) but not the other abrogators, particle or verb. Examples: الَّذِي يَأْتِينِي وَفِي الدَّارِ فَلَهُ دِرْهَمٌ، رَجُلٌ يَأْتِينِي فَلَهُ دِرْهَمٌ، غُلَامُ رَجُلٍ يَأْتِينِي فَلَهُ دِرْهَمٌ، كُلُّ رَجُلٍ عَالِمٍ فَلَهُ دِرْهَمٌ، كُلُّ رَجُلٍ فَلَهُ دِرْهَمٌ. Elsewhere the fāʾ is not allowed.",
                 "tr": "Mübtedâ emmâ'dan sonra gelince haberine fâ girmek zorundadır (emmâ Zeydün fe-muntalikun); çünkü emmâ şart mânâsı taşır, fâ da cevâbın alâmetidir. Yalnız şiir zarûretiyle (emmâ'l-kıtâlü lâ kıtâle ledeykum) ya da «kavl» gizlenip fâ onunla gittiği için düşer (fe-emme'llezîne'svedded vucûhuhum e-kefertum, yani fe-yukâlu lehum). Mübtedâ fiil veya zarfla sılalanmış mevsûl, böyle bir mevsûlle vasıflanmış isim, fiil veya zarfla vasıflanmış nekre, bunlardan birine muzâf, ya da müfredle vasıflanmış veya vasıfsız nekreye muzâf küll olunca fâ habere girEBİLİR — mübtedâ o zaman umûmîdir, sıfatı şarta benzer. Bu cevâz inne, enne, lâkinne ile sürer (kul inne'l-mevte'llezî tefirrûne minhu fe-innehû mülâkîkum), harf veya fiil olan diğer nâsihlerle sürmez. Örnekler: ellezî ye'tînî ve fi'd-dâri fe-lehû dirhemün, racülün ye'tînî fe-lehû dirhemün, gulâmu racülin ye'tînî fe-lehû dirhemün, küllü racülin âlimin fe-lehû dirhemün, küllü racülin fe-lehû dirhemün. Başka yerde fâ câiz değildir."},
 "examples": [
  {"ar": "أَمَّا زَيْدٌ فَمُنْطَلِقٌ", "en": "the obligatory fāʾ after أَمَّا", "tr": "emmâ'dan sonra vâcib fâ", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "أَمَّا الْقِتَالُ لَا قِتَالَ لَدَيْكُمْ", "en": "the fāʾ dropped by the poet's necessity", "tr": "şiir zarûretiyle düşen fâ", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "فَأَمَّا الَّذِينَ اسْوَدَّتْ وُجُوهُهُمْ أَكَفَرْتُمْ، أَيْ فَيُقَالُ لَهُمْ", "en": "the fāʾ hidden with the word «say»", "tr": "kavl ile gizlenen fâ", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "الَّذِي يَأْتِينِي وَفِي الدَّارِ فَلَهُ دِرْهَمٌ", "en": "the fāʾ allowed after the relative", "tr": "mevsûlden sonra câiz fâ", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "قُلْ إِنَّ الْمَوْتَ الَّذِي تَفِرُّونَ مِنْهُ فَإِنَّهُ مُلَاقِيكُمْ", "en": "the licence surviving إِنَّ", "tr": "inne ile süren cevâz", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "كُلُّ رَجُلٍ عَالِمٍ فَلَهُ دِرْهَمٌ، كُلُّ رَجُلٍ فَلَهُ دِرْهَمٌ", "en": "كُلّ annexed to a nakira", "tr": "nekreye muzâf küll", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
 ],
 "commonMistakes": [
  {"wrong": "أَمَّا زَيْدٌ مُنْطَلِقٌ", "right": "أَمَّا زَيْدٌ فَمُنْطَلِقٌ", "why": {"en": "after أَمَّا the fāʾ in the khabar is obligatory save in verse or when «say» is hidden", "tr": "emmâ'dan sonra haberde fâ vâcibdir; şiir ve gizli kavl hariç"}},
  {"wrong": "زَيْدٌ فَمُنْطَلِقٌ", "right": "زَيْدٌ مُنْطَلِقٌ", "why": {"en": "a particular mubtadaʾ does not resemble a condition, so the fāʾ may not enter its khabar", "tr": "hâs mübtedâ şarta benzemez; haberine fâ giremez"}},
  {"wrong": "كَانَ الَّذِي يَأْتِينِي فَلَهُ دِرْهَمٌ", "right": "إِنَّ الَّذِي يَأْتِينِي فَلَهُ دِرْهَمٌ", "why": {"en": "the licence survives only إِنَّ، أَنَّ، لٰكِنَّ — not kāna, ẓanna, mā or lā", "tr": "cevâz yalnız inne, enne, lâkinne ile sürer; kâne, zanne, mâ, lâ ile sürmez"}},
 ],
}
ADD_EN = (" Chapter 30 (print pp. 130-131): the fāʾ in the khabar — obligatory after أَمَّا (s1), dropped by the poet's necessity (s2) or with a hidden «say» (s3), allowed after the condition-like mubtadaʾ (s4) and under إِنَّ، أَنَّ، لٰكِنَّ (s5), with the examples (s6-s7).")
ADD_TR = (" Otuzuncu bab (baskı s. 130-131): haberde fâ — emmâ'dan sonra vâcib (s1), şiir zarûretiyle (s2) veya gizli kavl ile düşen (s3), şarta benzer mübtedâdan sonra (s4) ve inne, enne, lâkinne altında câiz (s5), örnekleriyle (s6-s7).")
write_out(30, S, TITLE, ADD_EN, ADD_TR, "pp. 130-131", GLOSS_ADD, notes=(NOTE,),
          related=((K29, [K]), (FK, [K]), (AMT, [K]), (MK, [K]), (IN, [K]), (MAW, [K])))
report(30, S, GLOSS_ADD, (NOTE,))
