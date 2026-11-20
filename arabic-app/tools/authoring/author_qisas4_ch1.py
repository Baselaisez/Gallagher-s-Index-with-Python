# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 1: «نَظْرَةٌ عَلَى الْقِصَصِ السَّابِقَةِ» — sections 1–2 of the story of Shuʿayb (print pp. 1–2):
a look back at the stories read so far, and why they are stories of a struggle between truth and falsehood (12:111).
The vowelling is the print's; the sentences are the print's clauses. python3 tools/authoring/author_qisas4_ch1.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "نَظْرَةٌ عَلَى الْقِصَصِ السَّابِقَةِ", "en": "A look back at the stories so far", "tr": "Önceki kıssalara bir bakış"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"

def qaratum(full="قَرَأْتُمْ", wa=False, punct=None):
    return tok(full, "qaraa", "verb", [FL] + ([AT] if wa else []), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ لِلْجَمْعِ.", Wen(wa) + "«you read» — a māḍī on sukūn before the doer's tāʾ; the tāʾ is the doer.", Wtr(wa) + "«okudunuz» — fâil tâsı sebebiyle sükûn üzere mebnî mâzî; tâ fâildir.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("قَرَأْ", "qaraa", "verb"), seg("تُمْ", "pron-2mp", "pron")])
def qissata(punct=None): return tok("قِصَّةَ", "qissa", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the story of» — the object, annexed.", "«kıssasını» — mef'ûl, muzâf.", punct=punct)
def sayyidina(full="سَيِّدِنَا", wa=False):
    return tok(full, "sayyid", "noun", [ID] + ([AT] if wa else []), W(wa) + "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", Wen(wa) + "«our master» — annexed, and itself annexed to «our».", Wtr(wa) + "«efendimiz» — muzâfun ileyh, kendisi de nâ'ya muzâf.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("سَيِّدِ", "sayyid", "noun"), seg("نَا", "pron-1p", "pron")])
def prophet(full, lex, en, tr, punct=None, mamnu=True):
    return tok(full, lex, "propn", [ID] + (["mamnu-min-sarf"] if mamnu else []), "مُضَافٌ إِلَيْهِ مَجْرُورٌ " + ("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ." if mamnu else "بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ."), en + (" — annexed; a foreign name, diptote: fatḥa for the kasra." if mamnu else " — annexed; a triptote name."), tr + (" — muzâfun ileyh; gayr-i munsarif yabancı alem: kesre yerine fetha." if mamnu else " — muzâfun ileyh; munsarif alem."), punct=punct)
def bi_masdar(full, lex, en, tr, punct=None, first=True, tags=()):
    """بِشَوْقٍ — the jarr phrase of manner; the later ones joined"""
    if first: return tok(full, lex, "noun", [HJ, "masdar"] + list(tags), "الْبَاءُ لِلْمُصَاحَبَةِ، وَالِاسْمُ مَجْرُورٌ بِالْكَسْرَةِ — حَالٌ فِي الْمَعْنَى.", en + " — the bāʾ of accompaniment: a ḥāl in sense.", tr + " — musâhabe bâsı: mânen hâl.", punct=punct, segments=[seg("بِ", "bi", "prep"), seg(full[2:], lex, "noun")])
    return tok(full, lex, "noun", [AT, HJ, "masdar"] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَالِاسْمُ مَعْطُوفٌ مَجْرُورٌ.", en, tr, punct=punct, segments=wa_(full[2:], lex, "noun"))
def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."):
    return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def atf_majrur(full, lex, en, tr, punct=None, tags=(), ar="مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ."):
    return tok(full, lex, "noun", [AT] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَالِاسْمُ " + ar, en, tr, punct=punct, segments=wa_(full[2:], lex, "noun"))
def wabayna(punct=None):
    return tok("وَبَيْنَ", "bayna", "noun", [AT, "maful-fih", ID], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ ظَرْفٌ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and between»", "«ve … ile»", punct=punct, segments=wa_("بَيْنَ", "bayna", "noun"))
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", [ID] + list(tags), "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", en, tr, punct=punct)
def innaha(full="وَإِنَّهَا", wa=True, pre_ar="الْوَاوُ عَاطِفَةٌ، وَ"):
    return tok(full, "inna", "part", [IW] + ([AT] if wa else []), pre_ar + "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«and indeed it» — inna; «it» its ism.", "«ve şüphesiz o» — inne; hâ ismi.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("إِنَّ", "inna", "part"), pr3fs_()])
def khabar_inna_mudaf(full, lex, en, tr):
    return tok(full, lex, "noun", [IW, ID], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", en + " — the khabar of inna, annexed.", tr + " — inne'nin haberi, muzâf.")

# ---------------------------------------------------------------- §1
sen("s1", "You read the story of our master Ibrāhīm and our master Yūsuf, and you read the story of our master Nūḥ, our master Hūd and our master Ṣāliḥ;",
        "Efendimiz İbrâhim'in ve efendimiz Yûsuf'un kıssasını okudunuz; efendimiz Nûh'un, efendimiz Hûd'un ve efendimiz Sâlih'in kıssasını okudunuz;", [
  qaratum(), qissata(), sayyidina(), prophet("إِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  sayyidina("وَسَيِّدِنَا", wa=True), prophet("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yûsuf»", punct="،"),
  qaratum("وَقَرَأْتُمْ", wa=True), qissata(), sayyidina(), prophet("نُوحٍ", "nuh", "«Nūḥ»", "«Nûh»", mamnu=False),
  sayyidina("وَسَيِّدِنَا", wa=True), prophet("هُودٍ", "hud", "«Hūd»", "«Hûd»", mamnu=False),
  sayyidina("وَسَيِّدِنَا", wa=True), prophet("صَالِحٍ", "salih-nabi", "«Ṣāliḥ»", "«Sâlih»", punct="،", mamnu=False),
])
sen("s2", "you read the story of our master Mūsā in some detail and at some length;", "efendimiz Mûsâ'nın kıssasını biraz tafsilli ve uzunca okudunuz;", [
  qaratum(), qissata(), sayyidina(), tok("مُوسَى", "musa", "propn", [ID, "mamnu-min-sarf", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — عَلَمٌ أَعْجَمِيٌّ مَقْصُورٌ.", "«Mūsā» — annexed; a foreign name ending in alif: the fatḥa is assumed.", "«Mûsâ» — muzâfun ileyh; maksûr yabancı alem: fetha takdîrî."),
  fi(), majrur("شَيْءٍ", "shay", "«something»", "«bir miktar»"),
  tok("مِنَ", "min", "prep", [HJ, NA], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِشَيْءٍ.", "«of» — the phrase qualifies «something».", "«-den» — câr-mecrûr «bir miktar»ın sıfatı."),
  majrur("التَّفْصِيلِ", "tafsil", "«detail»", "«tafsil»", tags=["masdar"]), atf_majrur("وَالتَّطْوِيلِ", "tatwil", "«and length»", "«ve uzunluk»", punct="،", tags=["masdar"]),
])
sen("s3", "you read all of that with longing and desire, with reverence and esteem,", "bütün bunları şevk ve istekle, saygı ve takdirle okudunuz;", [
  qaratum(), tok("كُلَّ", "kull", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«all of» — the object, annexed.", "«bütününü» — mef'ûl, muzâf."),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", ID], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that» — the demonstrative, annexed to.", "«bunları» — ism-i işâret, muzâfun ileyh."),
  bi_masdar("بِشَوْقٍ", "shawq", "«with longing»", "«şevkle»"), bi_masdar("وَرَغْبَةٍ", "raghba", "«and desire»", "«ve istekle»", first=False, punct="،"),
  bi_masdar("وَإِجْلَالٍ", "ijlal", "«and reverence»", "«ve saygıyla»", first=False), bi_masdar("وَتَقْدِيرٍ", "taqdir", "«and esteem»", "«ve takdirle»", first=False, punct="،"),
])
sen("s4", "and they settled in your souls and your hearts in the place of the beloved, favourite stories; your memory kept them, and your tongues carried them,",
        "ve nefislerinizde ve kalplerinizde sevgili, gözde kıssaların yerine yerleştiler; hafızanız onları sakladı, dilleriniz onları aktardı;", [
  tok("وَحَلَّتْ", "halla-settle", "verb", [AT, FL, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَحَلَّتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — الْقِصَصُ.", "«and they settled» — the stories, its doer concealed.", "«ve yerleştiler» — kıssalar, fâili müstetir.", segments=wa_("حَلَّتْ", "halla-settle", "verb")),
  fi(), tok("نُفُوسِكُمْ", "nafs", "noun", [HJ, ID, "jam-taksir"], "مَجْرُورٌ بِفِي، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your souls»", "«nefislerinizde»", segments=[seg("نُفُوسِ", "nafs", "noun"), pr2mp()]),
  tok("وَقُلُوبِكُمْ", "qalb", "noun", [AT, ID, "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَقُلُوبِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«and your hearts»", "«ve kalplerinizde»", segments=[seg("وَ", "wa", "conj"), seg("قُلُوبِ", "qalb", "noun"), pr2mp()]),
  tok("مَحَلَّ", "mahall", "noun", ["maful-fih", ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — أَيْ: فِي مَحَلِّ.", "«in the place of» — the ẓarf, annexed.", "«yerine» — zarf, muzâf."),
  mudaf_ilayh("الْقِصَصِ", "qasas", "«the stories»", "«kıssaların»", tags=["jam-taksir"]),
  tok("الْحَبِيبَةِ", "habib", "noun", [NA], "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "«beloved» — the naʿt.", "«sevgili» — sıfat."),
  tok("الْأَثِيرَةِ", "athir", "noun", [NA], "نَعْتٌ ثَانٍ مَجْرُورٌ.", "«favourite» — a second naʿt.", "«gözde» — ikinci sıfat.", punct="،"),
  tok("وَوَعَتْهَا", "waa", "verb", [AT, MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَوَعَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَهَا مَفْعُولٌ بِهِ.", "«and kept them» — the hā its object.", "«ve onları sakladı» — hâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("وَعَتْ", "waa", "verb"), pr3fs_()]),
  tok("ذَاكِرَتُكُمْ", "dhakira", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your memory» — the doer.", "«hafızanız» — fâil.", punct="،", segments=[seg("ذَاكِرَتُ", "dhakira", "noun"), pr2mp()]),
  tok("وَدَلَّتْ", "dalla", "verb", [AT, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَدَلَّتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and carried»", "«ve aktardı»", segments=wa_("دَلَّتْ", "dalla", "verb")),
  tok("بِهَا", "bi", "prep", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ.", "«them»", "«onları»", segments=[seg("بِ", "bi", "prep"), pr3fs_()]),
  tok("أَلْسِنَتُكُمْ", "lisan", "noun", [FL, ID, "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ — جَمْعُ لِسَانٍ.", "«your tongues» — the doer.", "«dilleriniz» — fâil.", punct="،", segments=[seg("أَلْسِنَتُ", "lisan", "noun"), pr2mp()]),
])
sen("s5", "and people have seen you telling them to your little brothers and repeating them to your parents and elder brothers, savouring them, and sometimes growing fervent in telling them.",
        "insanlar sizi, onları küçük kardeşlerinize anlatırken, anne-babanıza ve büyük kardeşlerinize tekrarlarken gördü; siz onların tadını alıyor, bazen anlatırken coşuyordunuz.", [
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ مَعَ الْمَاضِي.", "«and indeed» — qad of certainty with the māḍī.", "«ve gerçekten» — mâzîyle tahkik kad'ı.", segments=wa_("قَدْ", "qad", "part")),
  tok("رَآكُمُ", "raa", "verb", [MB, "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَكُمْ مَفْعُولٌ بِهِ، حُرِّكَتْ مِيمُهُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«saw you» — the kum its object.", "«sizi gördü» — küm mef'ûl.", segments=[seg("رَآ", "raa", "verb"), seg("كُمُ", "pron-2mp", "pron")]),
  nas_fail(),
  tok("تَحْكُونَهَا", "haka", "verb", ["hal", "afal-khamsa", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ حَالٌ مِنْ كُمْ.", "«telling them» — the clause is a ḥāl of «you».", "«onları anlatırken» — cümle, küm'ün hâli.", segments=[seg("تَحْكُونَ", "haka", "verb"), pr3fs_()]),
  tok("لِإِخْوَتِكُمُ", "akh", "noun", [HJ, ID, "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَإِخْوَةِ مَجْرُورٌ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ، حُرِّكَتْ مِيمُهُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«to your brothers»", "«kardeşlerinize»", segments=[seg("لِ", "li", "prep"), seg("إِخْوَتِ", "akh", "noun"), seg("كُمُ", "pron-2mp", "pron")]),
  tok("الصِّغَارِ", "saghir", "noun", [NA, "jam-taksir"], "نَعْتٌ مَجْرُورٌ — جَمْعُ صَغِيرٍ.", "«little» — the naʿt.", "«küçük» — sıfat.", punct="،"),
  tok("وَتُرَدِّدُونَهَا", "raddada", "verb", [AT, "afal-khamsa", MB, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتُرَدِّدُونَ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ.", "«and repeating them»", "«ve onları tekrarlarken»", segments=[seg("وَ", "wa", "conj"), seg("تُرَدِّدُونَ", "raddada", "verb"), pr3fs_()]),
  tok("لِلْأَبَوَيْنِ", "ab", "noun", [HJ, "al-muthanna"], "اللَّامُ حَرْفُ جَرٍّ، وَالْأَبَوَيْنِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — الْأَبُ وَالْأُمُّ تَغْلِيبًا.", "«to your parents» — a dual in jarr by the yāʾ: «the two fathers» for father and mother.", "«anne-babaya» — yâ ile mecrûr tesniye: tağlîben «iki baba».", segments=[seg("لِ", "li", "prep"), seg("الْأَبَوَيْنِ", "ab", "noun")]),
  tok("وَالْإِخْوَةِ", "akh", "noun", [AT, "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَالْإِخْوَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the brothers»", "«ve kardeşlere»", segments=wa_("الْإِخْوَةِ", "akh", "noun")),
  tok("الْكِبَارِ", "kabir", "noun", [NA, "jam-taksir"], "نَعْتٌ مَجْرُورٌ — جَمْعُ كَبِيرٍ.", "«elder» — the naʿt.", "«büyük» — sıfat.", punct="،"),
  tok("وَأَنْتُمْ", "antum", "pron", ["hal", MK], "الْوَاوُ لِلْحَالِ، وَأَنْتُمْ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«while you» — the wāw of the ḥāl; the mubtada.", "«siz … iken» — hâl vâvı; mübtedâ.", segments=wa_("أَنْتُمْ", "antum", "pron")),
  tok("تَتَذَوَّقُونَهَا", "tadhawwaqa", "verb", [MK, "afal-khamsa", MB, "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ.", "«savour them» — the khabar clause.", "«onların tadını alıyorsunuz» — haber cümlesi.", punct="،", segments=[seg("تَتَذَوَّقُونَ", "tadhawwaqa", "verb"), pr3fs_()]),
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ.", "«and sometimes» — qad of rarity with the muḍāriʿ.", "«ve bazen» — muzâriyle taklîl kad'ı.", segments=wa_("قَدْ", "qad", "part")),
  tok("تَتَحَمَّسُونَ", "tahammasa", "verb", ["afal-khamsa", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«grow fervent»", "«coşuyorsunuz»"),
  fi(), tok("حِكَايَتِهَا", "hikaya", "noun", [HJ, ID, "masdar"], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«telling them»", "«onları anlatırken»", punct=".", segments=[seg("حِكَايَتِ", "hikaya", "noun"), pr3fs_()]),
])
# ---------------------------------------------------------------- §2
sen("s6", "And no wonder: they are stories that draw and stir;", "Buna şaşmamalı: onlar çekici ve heyecan verici kıssalardır;", [
  tok("وَلَا", "la-nafiya-lil-jins", "part", [AT, "la-nafiya-lil-jins"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«and no» — lā of the genus.", "«ve hiç» — cins nefyi lâ'sı.", segments=wa_("لَا", "la-nafiya-lil-jins", "part")),
  tok("غَرَابَةَ", "gharaba", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا مَحْذُوفٌ: فِي ذٰلِكَ.", "«wonder» — the ism of lā, built on fatḥa; its khabar «in that» dropped.", "«şaşılacak şey» — lâ'nın ismi, fetha üzere mebnî; haberi mahzûf.", punct="؛"),
  tok("فَإِنَّهَا", "inna", "part", [IW], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهَا.", "«for they» — the fāʾ of the reason; inna with its ism.", "«zira onlar» — ta'lîl fâsı; inne ve ismi.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3fs_()]),
  khabar_inna("قِصَصٌ", "qasas", "«stories»", "«kıssalardır»", tags=["jam-taksir"]),
  tok("شَائِقَةٌ", "shaiq", "noun", [NA, "ism-fail"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«that draw» — the naʿt.", "«çekici» — sıfat."),
  tok("مُثِيرَةٌ", "muthir", "noun", [NA, "ism-fail", "form-iv-verbs"], "نَعْتٌ ثَانٍ مَرْفُوعٌ.", "«that stir» — a second naʿt.", "«heyecan verici» — ikinci sıfat.", punct="،"),
])
sen("s7", "and they are the story of a struggle between truth and falsehood, between knowledge and ignorance, between light and darkness, between humanity and savagery, between certainty and conviction and mere guessing and conjecture.",
        "ve hak ile bâtıl, ilim ile cehalet, nur ile karanlık, insanlık ile vahşet, kesinlik ve yakîn ile zan ve tahmin arasındaki bir mücadelenin kıssasıdır.", [
  innaha(), khabar_inna_mudaf("قِصَّةُ", "qissa", "«the story of»", "«kıssası»"),
  mudaf_ilayh("صِرَاعٍ", "sira-conflict", "«a struggle»", "«bir mücadelenin»", tags=["masdar"]),
  tok("بَيْنَ", "bayna", "noun", ["maful-fih", ID, NA], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ — صِفَةٌ لِصِرَاعٍ.", "«between» — the ẓarf, qualifying «a struggle».", "«arasında» — zarf, «mücadele»nin sıfatı."),
  mudaf_ilayh("الْحَقِّ", "haqq", "«truth»", "«hak»"), atf_majrur("وَالْبَاطِلِ", "batil", "«and falsehood»", "«ile bâtıl»", punct="،"),
  wabayna(), mudaf_ilayh("الْعِلْمِ", "ilm", "«knowledge»", "«ilim»"), atf_majrur("وَالْجَهْلِ", "jahl", "«and ignorance»", "«ile cehalet»", punct="،"),
  wabayna(), mudaf_ilayh("النُّورِ", "nur", "«light»", "«nur»"), atf_majrur("وَالظَّلَامِ", "zalam", "«and darkness»", "«ile karanlık»", punct="،"),
  wabayna(), mudaf_ilayh("الْإِنْسَانِيَّةِ", "insaniyya", "«humanity»", "«insanlık»", tags=["ism-mansub"]), atf_majrur("وَالْوَحْشِيَّةِ", "wahshiyya", "«and savagery»", "«ile vahşet»", punct="،", tags=["ism-mansub"]),
  wabayna(), mudaf_ilayh("الْجَزْمِ", "jazm", "«certainty»", "«kesinlik»", tags=["masdar"]), atf_majrur("وَالْيَقِينِ", "yaqin", "«and conviction»", "«ve yakîn»", punct="،"),
  atf_majrur("وَالظَّنِّ", "zann", "«and guessing»", "«ile zan»", tags=["masdar"]), atf_majrur("وَالتَّخْمِينِ", "takhmin", "«and conjecture»", "«ve tahmin»", punct=".", tags=["masdar"]),
])
sen("s8", "Then, they are the story of a victory of truth over falsehood, of knowledge over ignorance, of the weak over the strong, of the few over the many;",
        "Sonra onlar hakkın bâtıla, ilmin cehalete, zayıfın güçlüye, azın çoğa galip gelişinin kıssasıdır;", [
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then»", "«sonra»"),
  innaha("إِنَّهَا", wa=False, pre_ar=""), khabar_inna_mudaf("قِصَّةُ", "qissa", "«the story of»", "«kıssası»"),
  mudaf_ilayh("انْتِصَارٍ", "intisar", "«a victory»", "«galip gelişinin»", tags=["masdar", "form-viii-verbs"]),
  tok("لِلْحَقِّ", "haqq", "noun", [HJ, NA], "اللَّامُ حَرْفُ جَرٍّ، وَالْحَقِّ مَجْرُورٌ — مُتَعَلِّقٌ بِانْتِصَارٍ.", "«of truth» — hangs on «a victory».", "«hakkın» — «galip geliş»e bağlı.", segments=[seg("لِ", "li", "prep"), seg("الْحَقِّ", "haqq", "noun")]),
  tok("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«over»", "«-e»"), majrur("الْبَاطِلِ", "batil", "«falsehood»", "«bâtıla»", punct="،"),
  atf_majrur("وَالْعِلْمِ", "ilm", "«and of knowledge»", "«ve ilmin»", ar="مَعْطُوفٌ عَلَى الْحَقِّ مَجْرُورٌ."), tok("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«over»", "«-e»"), majrur("الْجَهْلِ", "jahl", "«ignorance»", "«cehalete»", punct="،"),
  atf_majrur("وَالضَّعِيفِ", "daif", "«and of the weak»", "«ve zayıfın»", ar="مَعْطُوفٌ مَجْرُورٌ."), tok("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«over»", "«-e»"), majrur("الْقَوِيِّ", "qawi", "«the strong»", "«güçlüye»", punct="،"),
  atf_majrur("وَالْقَلِيلِ", "qalil", "«and of the few»", "«ve azın»", ar="مَعْطُوفٌ مَجْرُورٌ."), tok("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«over»", "«-e»"), majrur("الْكَثِيرِ", "kathir", "«the many»", "«çoğa»", punct="،"),
])
sen("s9", "a story in which there is knowledge and wisdom, admonition and remembrance;", "içinde ilim ve hikmet, öğüt ve hatırlatma bulunan bir kıssa;", [
  tok("قِصَّةٌ", "qissa", "noun", [MK, "badal"], "بَدَلٌ مِنْ قِصَّةُ انْتِصَارٍ مَرْفُوعٌ — أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هِيَ قِصَّةٌ.", "«a story» — the badal, or the khabar of a dropped «it is».", "«bir kıssa» — bedel, ya da mahzûf «o»nun haberi."),
  tok("فِيهَا", "fi", "prep", [HJ, MK, NA], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ صِفَةٌ لِقِصَّةٌ.", "«in which there is» — the fronted khabar; the clause qualifies «a story».", "«içinde» — mukaddem haber; cümle «kıssa»nın sıfatı.", segments=[seg("فِي", "fi", "prep"), pr3fs_()]),
  tok("عِلْمٌ", "ilm", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«knowledge» — the delayed mubtada.", "«ilim» — muahhar mübtedâ."),
  tok("وَحِكْمَةٌ", "hikma", "noun", [AT], "الْوَاوُ عَاطِفَةٌ، وَحِكْمَةٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and wisdom»", "«ve hikmet»", punct="،", segments=wa_("حِكْمَةٌ", "hikma", "noun")),
  tok("وَمَوْعِظَةٌ", "mawiza", "noun", [AT], "الْوَاوُ عَاطِفَةٌ، وَمَوْعِظَةٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and admonition»", "«ve öğüt»", segments=wa_("مَوْعِظَةٌ", "mawiza", "noun")),
  tok("وَذِكْرَى", "dhikra", "noun", [AT, "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَذِكْرَى مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«and remembrance» — the ḍamma assumed on the alif.", "«ve hatırlatma» — elif üzerinde takdîrî damme.", punct="،", segments=wa_("ذِكْرَى", "dhikra", "noun")),
])
sen("s10", "and God the Mighty spoke truly: «In their stories there is surely a lesson for those of understanding. It was no invented tale, but a confirmation of what came before it, a detailing of everything, a guidance and a mercy for a people who believe» (12:111).",
         "Yüce Allah doğru söyledi: «Andolsun, onların kıssalarında akıl sahipleri için ibret vardır. Bu, uydurulmuş bir söz değildir; fakat kendinden öncekini doğrulayan, her şeyi açıklayan, inanan bir topluluk için bir hidayet ve rahmettir» (12:111).", [
  tok("وَصَدَقَ", "sadaqa-verb", "verb", [AT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَصَدَقَ فِعْلٌ مَاضٍ.", "«and spoke truly»", "«ve doğru söyledi»", segments=wa_("صَدَقَ", "sadaqa-verb", "verb")),
  allah_fail(), tok("الْعَظِيمُ", "azim", "noun", [NA], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Mighty» — the naʿt.", "«Yüce» — sıfat.", punct=":"),
  *quran([
  tok("لَقَدْ", "qad", "part", [IQ, "qad-harf", "tawkid"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مُقَدَّرٍ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«surely» — the lām of an unspoken oath, and qad of certainty.", "«andolsun» — mukadder kasemin cevabının lâmı ve tahkik kad'ı.", segments=[seg("لَ", "lam-qasam", "part"), seg("قَدْ", "qad", "part")]),
  tok("كَانَ", "kana", "verb", [IQ, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«there was» — kāna.", "«vardı» — kâne."),
  fi(), tok("قَصَصِهِمْ", "qasas", "noun", [IQ, HJ, ID, KN], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ.", "«their stories» — the phrase is kāna's fronted khabar.", "«onların kıssalarında» — câr-mecrûr kâne'nin mukaddem haberi.", segments=[seg("قَصَصِ", "qasas", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("عِبْرَةٌ", "ibra-lesson", "noun", [IQ, KN], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a lesson» — the delayed ism of kāna.", "«ibret» — kâne'nin muahhar ismi."),
  tok("لِأُولِي", "ulu", "noun", [IQ, HJ, ID, NA], "اللَّامُ حَرْفُ جَرٍّ، وَأُولِي مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، مُضَافٌ.", "«for those of» — in jarr by the yāʾ, as a sound-plural adjunct; annexed.", "«sahipleri için» — cem-i müzekker sâlime mülhak, yâ ile mecrûr; muzâf.", segments=[seg("لِ", "li", "prep"), seg("أُولِي", "ulu", "noun")]),
  mudaf_ilayh("الْأَلْبَابِ", "lubb", "«understanding»", "«akıl»", tags=["jam-taksir"], punct="،"),
  tok("مَا", "ma-nafiya", "part", [IQ, "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not»", "«değildir»"),
  tok("كَانَ", "kana", "verb", [IQ, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْقُرْآنُ.", "«it was» — kāna, its ism concealed: the Qur'an.", "«o idi» — kâne, ismi müstetir: Kur'an."),
  tok("حَدِيثًا", "hadith", "noun", [IQ, KN], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a tale» — the khabar of kāna.", "«bir söz» — kâne'nin haberi."),
  tok("يُفْتَرَى", "iftara", "verb", [IQ, NA, "naib-al-fail", "form-viii-verbs", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ صِفَةٌ لِحَدِيثًا.", "«invented» — the passive clause qualifies «a tale».", "«uydurulan» — meçhul cümle «söz»ün sıfatı."),
  tok("وَلٰكِنْ", "lakin", "part", [IQ, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا يَعْمَلُ.", "«but» — the lightened lākin, ungoverning.", "«fakat» — amel etmeyen tahfif edilmiş lâkin.", segments=wa_("لٰكِنْ", "lakin", "part")),
  tok("تَصْدِيقَ", "tasdiq", "noun", [IQ, KN, ID, "masdar"], "خَبَرٌ لِكَانَ مَحْذُوفَةٍ مَنْصُوبٌ: وَلٰكِنْ كَانَ تَصْدِيقَ — مُضَافٌ.", "«a confirmation of» — the khabar of a dropped kāna; annexed.", "«doğrulayan» — mahzûf kâne'nin haberi; muzâf."),
  tok("الَّذِي", "alladhi", "pron", [IQ, MW, ID], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — the relative, annexed to.", "«olanı» — ism-i mevsûl, muzâfun ileyh."),
  tok("بَيْنَ", "bayna", "noun", [IQ, "maful-fih", ID, MW], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — صِلَةُ الَّذِي.", "«before» — the ẓarf; the ṣila.", "«önünde» — zarf; sıla."),
  tok("يَدَيْهِ", "yad", "noun", [IQ, ID, "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its two hands» — a dual in jarr by the yāʾ: what came before it.", "«iki eli» — yâ ile mecrûr tesniye: kendinden önceki.", segments=[seg("يَدَيْ", "yad", "noun"), pr3msi()]),
  tok("وَتَفْصِيلَ", "tafsil", "noun", [IQ, AT, ID, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَتَفْصِيلَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and a detailing of»", "«ve açıklayan»", segments=wa_("تَفْصِيلَ", "tafsil", "noun")),
  tok("كُلِّ", "kull", "noun", [IQ, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«every»", "«her»"), mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şeyi»"),
  tok("وَهُدًى", "huda", "noun", [IQ, AT, "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَهُدًى مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«and a guidance» — the fatḥa assumed.", "«ve bir hidayet» — takdîrî fetha.", segments=wa_("هُدًى", "huda", "noun")),
  tok("وَرَحْمَةً", "rahma", "noun", [IQ, AT], "الْوَاوُ عَاطِفَةٌ، وَرَحْمَةً مَعْطُوفٌ مَنْصُوبٌ.", "«and a mercy»", "«ve rahmet»", segments=wa_("رَحْمَةً", "rahma", "noun")),
  tok("لِقَوْمٍ", "qawm", "noun", [IQ, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَقَوْمٍ مَجْرُورٌ.", "«for a people»", "«bir topluluk için»", segments=[seg("لِ", "li", "prep"), seg("قَوْمٍ", "qawm", "noun")]),
  tok("يُؤْمِنُونَ", "aamana", "verb", [IQ, NA, "afal-khamsa", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ صِفَةٌ لِقَوْمٍ.", "«who believe» — the clause qualifies «a people».", "«inanan» — cümle «topluluk»un sıfatı.", punct="."),
  ]),
])

CAND = {
 "qaraa": G("qaraa", "قَرَأَ", "ق ر أ", "verb", "to read", "okumak", 1),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa, hikâye", 1, plural="قِصَص"),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "master, lord; سَيِّدُنَا: our master (of a prophet)", "efendi; seyyidünâ: efendimiz (peygamber için)", 2),
 "ibrahim": G("ibrahim", "إِبْرَاهِيم", None, "propn", "Ibrāhīm (Abraham)", "İbrâhim", 1),
 "yusuf": G("yusuf", "يُوسُف", None, "propn", "Yūsuf (Joseph)", "Yûsuf", 1),
 "nuh": G("nuh", "نُوح", None, "propn", "Nūḥ (Noah) — a three-letter foreign name with a quiet middle: it declines in full", "Nûh — ortası sâkin üç harfli yabancı alem: munsarif", 1),
 "hud": G("hud", "هُود", None, "propn", "Hūd — the prophet of ʿĀd; a three-letter name that declines in full", "Hûd — Âd kavminin peygamberi; munsarif", 1),
 "salih-nabi": G("salih-nabi", "صَالِح", "ص ل ح", "propn", "Ṣāliḥ — the prophet of Thamūd", "Sâlih — Semûd kavminin peygamberi", 1),
 "musa": G("musa", "مُوسَى", None, "propn", "Mūsā (Moses)", "Mûsâ", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing; شَيْءٌ مِنْ: some", "şey; şey'ün min: biraz", 1),
 "tafsil": G("tafsil", "تَفْصِيل", "ف ص ل", "noun", "detail, detailing (masdar of فَصَّلَ)", "tafsil — ayrıntı", 3),
 "tatwil": G("tatwil", "تَطْوِيل", "ط و ل", "noun", "lengthening, going at length (masdar of طَوَّلَ)", "uzatma, uzun tutma", 4),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "each, every, all", "her, bütün", 1),
 "dhalika": G("dhalika", "ذَلِكَ", None, "pron", "that", "o, şu", 1),
 "shawq": G("shawq", "شَوْق", "ش و ق", "noun", "longing, eagerness", "şevk, özlem", 2),
 "raghba": G("raghba", "رَغْبَة", "ر غ ب", "noun", "desire, wish", "istek, rağbet", 2),
 "ijlal": G("ijlal", "إِجْلَال", "ج ل ل", "noun", "reverence, honouring (masdar of أَجَلَّ)", "saygı, yüceltme", 4),
 "taqdir": G("taqdir", "تَقْدِير", "ق د ر", "noun", "esteem, appreciation; (grammar) estimation", "takdir", 3),
 "halla-settle": G("halla-settle", "حَلَّ", "ح ل ل", "verb", "to settle, to alight (حَلَّ مَحَلَّ: to take the place of)", "yerleşmek, konmak (halle mahalle: yerine geçmek)", 3),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "soul, self", "nefis, can", 1, plural="نُفُوس"),
 "qalb": G("qalb", "قَلْب", "ق ل ب", "noun", "heart", "kalp", 1, plural="قُلُوب"),
 "mahall": G("mahall", "مَحَلّ", "ح ل ل", "noun", "place, position", "yer, mahal", 2),
 "qasas": G("qasas", "قَصَص", "ق ص ص", "noun", "stories (plural of قِصَّة); narration", "kıssalar; anlatım", 2),
 "habib": G("habib", "حَبِيب", "ح ب ب", "noun", "beloved", "sevgili", 1),
 "athir": G("athir", "أَثِير", "أ ث ر", "noun", "favoured, preferred, cherished", "gözde, tercih edilen", 4),
 "waa": G("waa", "وَعَى", "و ع ي", "verb", "to retain, to take in and keep (of memory)", "belleğinde tutmak, kavramak", 3),
 "dhakira": G("dhakira", "ذَاكِرَة", "ذ ك ر", "noun", "memory (the faculty)", "hafıza", 3),
 "dalla": G("dalla", "دَلَّ", "د ل ل", "verb", "to point to, to indicate; دَلَّتْ بِهَا أَلْسِنَتُكُمْ: your tongues carried them", "göstermek, delâlet etmek", 2),
 "lisan": G("lisan", "لِسَان", "ل س ن", "noun", "tongue; language", "dil", 1, plural="أَلْسِنَة"),
 "qad": G("qad", "قَدْ", None, "part", "qad — certainty with the māḍī, possibility with the muḍāriʿ", "kad — mâzîyle tahkik, muzâriyle ihtimal", 3),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "haka": G("haka", "حَكَى", "ح ك ي", "verb", "to tell, to relate", "anlatmak, hikâye etmek", 2),
 "akh": G("akh", "أَخ", "أ خ و", "noun", "brother", "kardeş", 1, plural="إِخْوَة"),
 "saghir": G("saghir", "صَغِير", "ص غ ر", "noun", "small, little, young", "küçük", 1, plural="صِغَار"),
 "raddada": G("raddada", "رَدَّدَ", "ر د د", "verb", "to repeat, to recite over (Form II)", "tekrarlamak (tef'îl)", 3),
 "ab": G("ab", "أَب", "أ ب و", "noun", "father; الْأَبَوَانِ: the parents", "baba; el-ebevân: anne-baba", 1, plural="آبَاء"),
 "kabir": G("kabir", "كَبِير", "ك ب ر", "noun", "big, great, elder", "büyük", 1, plural="كِبَار"),
 "antum": G("antum", "أَنْتُمْ", None, "pron", "you (plural)", "siz", 1),
 "tadhawwaqa": G("tadhawwaqa", "تَذَوَّقَ", "ذ و ق", "verb", "to taste, to savour (Form V)", "tadına varmak (tefa''ul)", 3),
 "tahammasa": G("tahammasa", "تَحَمَّسَ", "ح م س", "verb", "to grow fervent, enthusiastic (Form V)", "coşmak, heyecanlanmak (tefa''ul)", 4),
 "hikaya": G("hikaya", "حِكَايَة", "ح ك ي", "noun", "a telling, a tale", "hikâye, anlatma", 2),
 "la-nafiya-lil-jins": G("la-nafiya-lil-jins", "لَا (النَّافِيَةُ لِلْجِنْس)", None, "part", "lā of the absolute negation of the genus — governs like إِنَّ", "cins nefyi lâ'sı — inne gibi amel eder", 4),
 "gharaba": G("gharaba", "غَرَابَة", "غ ر ب", "noun", "strangeness; لَا غَرَابَةَ: no wonder", "gariplik; lâ garâbete: şaşılacak şey yok", 3),
 "inna": G("inna", "إِنَّ", None, "part", "indeed — puts its ism in naṣb and its khabar in rafʿ", "inne — şüphesiz; ismini nasb, haberini ref' eder", 1),
 "shaiq": G("shaiq", "شَائِق", "ش و ق", "noun", "drawing, attractive (ism fāʿil of شَاقَ)", "çekici, cazip", 4),
 "muthir": G("muthir", "مُثِير", "ث و ر", "noun", "stirring, exciting (ism fāʿil of أَثَارَ)", "heyecan verici", 4),
 "sira-conflict": G("sira-conflict", "صِرَاع", "ص ر ع", "noun", "a struggle, a conflict (masdar of صَارَعَ)", "mücadele, çatışma", 3),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between (a ẓarf)", "arasında (zarf)", 1),
 "haqq": G("haqq", "حَقّ", "ح ق ق", "noun", "truth, right", "hak", 1),
 "batil": G("batil", "بَاطِل", "ب ط ل", "noun", "falsehood, vanity", "bâtıl", 2),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge", "ilim", 1),
 "jahl": G("jahl", "جَهْل", "ج ه ل", "noun", "ignorance", "cehalet", 2),
 "nur": G("nur", "نُور", "ن و ر", "noun", "light", "nur, ışık", 1),
 "zalam": G("zalam", "ظَلَام", "ظ ل م", "noun", "darkness", "karanlık", 2),
 "insaniyya": G("insaniyya", "إِنْسَانِيَّة", "أ ن س", "noun", "humanity, humaneness (a nisba noun)", "insanlık", 3),
 "wahshiyya": G("wahshiyya", "وَحْشِيَّة", "و ح ش", "noun", "savagery, wildness (a nisba noun)", "vahşet", 3),
 "jazm": G("jazm", "جَزْم", "ج ز م", "noun", "firm resolve, certainty; (grammar) the jazm", "kesinlik, cezm", 3),
 "yaqin": G("yaqin", "يَقِين", "ي ق ن", "noun", "certainty, sure conviction", "yakîn", 2),
 "zann": G("zann", "ظَنّ", "ظ ن ن", "noun", "supposition, doubt — the opinion short of certainty", "zan — kesinliğe varmayan kanaat", 3),
 "takhmin": G("takhmin", "تَخْمِين", "خ م ن", "noun", "guessing, conjecture (masdar of خَمَّنَ)", "tahmin", 3),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then, moreover", "sonra", 1),
 "intisar": G("intisar", "اِنْتِصَار", "ن ص ر", "noun", "victory (masdar of انْتَصَرَ)", "zafer, galip gelme", 3),
 "daif": G("daif", "ضَعِيف", "ض ع ف", "noun", "weak", "zayıf", 1),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü", 1),
 "qalil": G("qalil", "قَلِيل", "ق ل ل", "noun", "few, little", "az", 1),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "hikma": G("hikma", "حِكْمَة", "ح ك م", "noun", "wisdom", "hikmet", 1),
 "mawiza": G("mawiza", "مَوْعِظَة", "و ع ظ", "noun", "an admonition, a sermon", "öğüt, vaaz", 2),
 "dhikra": G("dhikra", "ذِكْرَى", "ذ ك ر", "noun", "a remembrance, a reminder", "hatırlatma, zikrâ", 2),
 "sadaqa-verb": G("sadaqa-verb", "صَدَقَ", "ص د ق", "verb", "to speak truly, to be truthful", "doğru söylemek", 1),
 "allah": G("allah", "اللَّه", None, "propn", "God", "Allah", 1),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "mighty, great", "yüce, büyük", 1),
 "lam-qasam": G("lam-qasam", "لَ (لَامُ الْقَسَمِ)", None, "part", "the lām of the oath's answer", "kasem cevabının lâmı", 4),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be — raises its ism and puts its khabar in naṣb", "kâne — idi; ismini ref', haberini nasb eder", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "ibra-lesson": G("ibra-lesson", "عِبْرَة", "ع ب ر", "noun", "a lesson, an example to take to heart", "ibret", 2),
 "ulu": G("ulu", "أُولُو", None, "noun", "those of, possessors of (أُولُو الْأَلْبَابِ: people of understanding)", "sahipleri (ülü'l-elbâb: akıl sahipleri)", 3),
 "lubb": G("lubb", "لُبّ", "ل ب ب", "noun", "the core; the understanding (plural أَلْبَاب)", "öz; akıl (çoğulu elbâb)", 3, plural="أَلْبَاب"),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "the negating mā (with the māḍī: did not)", "nefy mâ'sı (mâzîyle: -medi)", 2),
 "hadith": G("hadith", "حَدِيث", "ح د ث", "noun", "a tale, a saying; a ḥadīth", "söz, hadis", 1),
 "iftara": G("iftara", "اِفْتَرَى", "ف ر ي", "verb", "to invent, to fabricate (Form VIII)", "uydurmak, iftira etmek (iftiâl)", 3),
 "lakin": G("lakin", "لٰكِنْ", None, "part", "but — the lightened لٰكِنَّ, which does not govern", "lâkin — amel etmeyen tahfif edilmiş lâkinne", 2),
 "tasdiq": G("tasdiq", "تَصْدِيق", "ص د ق", "noun", "confirmation, affirming as true", "tasdik", 3),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "who, which, that (masculine relative)", "ellezî — müzekker ism-i mevsûl", 2),
 "yad": G("yad", "يَد", "ي د ي", "noun", "hand; بَيْنَ يَدَيْهِ: before it", "el; beyne yedeyhi: önünde", 1),
 "huda": G("huda", "هُدًى", "ه د ي", "noun", "guidance", "hidayet", 1),
 "rahma": G("rahma", "رَحْمَة", "ر ح م", "noun", "mercy", "rahmet", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people, a folk", "kavim", 1),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV; آمَنَ بِ)", "iman etmek, inanmak (if'âl; âmene bi-)", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (masculine plural, attached)", "siz / sizin (bitişik)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us / our", "biz", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "she / it / her (attached)", "o / onun (bitişik)", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "he / him / his (attached)", "o / onun (bitişik)", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, then", "o hâlde, sonra", 1),
 "bi": G("bi", "بِ", None, "prep", "by, with", "ile", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, over", "üzerine, -e", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "aamana", _sg.derived(_sg.B4 + " — مَهْمُوزُ الْفَاءِ", _sg.W4, "ُ", "آمَن", "ؤْمِن", "آمِن", "إِيمَان", "مُؤْمِن", "مُؤْمَن", "أُومِنَ", "يُؤْمَنُ", "آمَنَ يُؤْمِنُ: صَدَّقَ — بَابُ الْإِفْعَالِ، مَهْمُوزُ الْفَاءِ: هَمْزَتَانِ فِي أَوَّلِهِ صَارَتَا آ"))
put_morph(mo, "halla-settle", _sg.entry(_sg.BABS["nasara"][0] + " — مُضَاعَفٌ", _sg.BABS["nasara"][1], "حُلُول", "حَالّ", _sg.mazi14("حَلّ", "حَلَل"), _sg.mudari14("َ", "حُلّ", "حْلُل"),
    ["حُلَّ", "حُلَّا", "حُلُّوا", "حُلِّي", "حُلَّا", "اُحْلُلْنَ"], "يَحُلَّ", "يَحُلَّ", "تَحُلَّ", None, None, None, "حَلَّ يَحُلُّ: نَزَلَ وَاسْتَقَرَّ — مُضَاعَفٌ مِنْ بَابِ نَصَرَ؛ الْإِدْغَامُ وَاجِبٌ مَعَ الضَّمِيرِ الْمُتَحَرِّكِ يَنْفَكُّ: حَلَلْتُ، يَحْلُلْنَ"))
put_morph(mo, "waa", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "وَعَ", "ع", "i", "ع", "وَعْي", "وَاعٍ", "مَوْعِيّ", "وُعِيَ", "يُوعَى", "وَعَى يَعِي: حَفِظَ وَفَهِمَ — مِثَالٌ نَاقِصٌ (لَفِيفٌ مَفْرُوقٌ)؛ الْأَمْرُ: عِ"))
put_morph(mo, "raddada", _sg.derived(_sg.B2, _sg.W2, "ُ", "رَدَّد", "رَدِّد", "رَدِّد", "تَرْدِيد", "مُرَدِّد", "مُرَدَّد", "رُدِّدَ", "يُرَدَّدُ", "رَدَّدَ يُرَدِّدُ: كَرَّرَ — بَابُ التَّفْعِيلِ"))
put_morph(mo, "tadhawwaqa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَذَوَّق", "تَذَوَّق", "تَذَوَّق", "تَذَوُّق", "مُتَذَوِّق", "مُتَذَوَّق", "تُذُوِّقَ", "يُتَذَوَّقُ", "تَذَوَّقَ يَتَذَوَّقُ: ذَاقَ شَيْئًا فَشَيْئًا — بَابُ التَّفَعُّلِ"))
put_morph(mo, "tahammasa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَحَمَّس", "تَحَمَّس", "تَحَمَّس", "تَحَمُّس", "مُتَحَمِّس", None, None, None, "تَحَمَّسَ يَتَحَمَّسُ: اشْتَدَّ شَوْقُهُ — بَابُ التَّفَعُّلِ، لَازِمٌ"))
put_morph(mo, "iftara", _sg.derived_naqis(_sg.B8 + " — نَاقِصٌ", _sg.W8, "َ", "اِفْتَرَ", "فْتَر", "i", "اِفْتَر", "اِفْتِرَاء", "مُفْتَرٍ", "مُفْتَرًى", "اُفْتُرِيَ", "يُفْتَرَى", "اِفْتَرَى يَفْتَرِي: اخْتَلَقَ الْكَذِبَ — نَاقِصٌ مِنَ الِافْتِعَالِ؛ يُفْتَرَى: مَبْنِيٌّ لِلْمَجْهُولِ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch1 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 1 (print pp. 1–2, sections 1–2): a look back at the stories read so far (s1–s5) and why they are stories of a struggle between truth and falsehood, with 12:111 (s6–s10). The print's رَأَاكُمُ is written رَآكُمُ."
ADD_TR = " Birinci bölüm (baskı s. 1–2, 1–2. kısımlar): şimdiye kadar okunan kıssalara bir bakış (s1–s5) ve bunların neden hak ile bâtıl arasındaki bir mücadelenin kıssası olduğu, 12:111 ile (s6–s10). Baskının رَأَاكُمُ imlâsı رَآكُمُ yazılmıştır."
write_out(1, S, TITLE, ADD_EN, ADD_TR, "sections 1–2", GLOSS_ADD, notes=(), related=())
report(1, S, GLOSS_ADD, ())
