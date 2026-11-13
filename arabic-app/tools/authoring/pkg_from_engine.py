import sys
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pkg_from_engine.py — a Qissa content package from the engines' reading of a transcribed text.

    python3 pkg_from_engine.py <engine.json> <meta.json> <out-pkg-dir> [--lex lex_extra.json] [--trans trans.json] [--fixes fixes.json]

engine.json   the output of tools/authoring/engine_author.js (the ḍabṭ engine's ending / rule / head per word, the lexicon's key)
meta.json     {"id", "storyGroup", "title":{ar,en,tr}, "subtitle":{…}, "level", "levelName", "access", "published", "version",
               "chapterTitles": {"1": {"en":…, "tr":…}, …}, "attribution": {ar,en,tr,reviewStatus}}
lex_extra     {"<bare host>": {"key":…, "lemma":…, "pos":…, "gloss":{en,tr}, "level":…, "root"?, "plural"?}} — the words no shipped glossary knows
trans         {"<ch>:<sId>": {"en":…, "tr":…}} — the sentence translations (the author's)
fixes         {"<ch>:<sId>:<i>": {"key"?:…, "rule"?:…, "k"?:…, "note"?: {ar,en,tr}}} — the author's corrections of the engine's reading

Every iʿrāb line is TEMPLATED FROM THE RULE the engine chose and the written shape of the word (the sign: ḍamma / fatḥa /
kasra, the letters of the dual and the sound plural, the taqdīrī sign of the maqṣūr / manqūṣ, the nūn of the five forms).
The author reviews the report this script prints (the words the engine and the transcription disagree on, the rows left
undecided) and corrects by the fixes file; nothing is invented by a model.
"""
import json, sys, re, unicodedata, glob, os, argparse, datetime
from pathlib import Path
ROOT = Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
N = lambda s: unicodedata.normalize("NFC", s or "")
DIA = re.compile("[ً-ْٰـ]")
bare = lambda s: DIA.sub("", N(s))
ENC = {"ه": "pron-3ms", "ها": "pron-3fs", "هم": "pron-3mp", "هن": "pron-3fp", "هما": "pron-3d", "ك": "pron-2ms", "كم": "pron-2mp", "كن": "pron-2fp", "كما": "pron-2d", "نا": "pron-1p", "ي": "pron-1s", "ني": "pron-1s"}
ENC_AR = {"ه": "الْهَاءُ", "ها": "الْهَاءُ", "هم": "الْهَاءُ", "هن": "الْهَاءُ", "هما": "الْهَاءُ", "ك": "الْكَافُ", "كم": "الْكَافُ", "كن": "الْكَافُ", "كما": "الْكَافُ", "نا": "«نَا»", "ي": "الْيَاءُ", "ني": "الْيَاءُ"}
ENC_EN = {"ه": "«his/its»", "ها": "«her/its»", "هم": "«their»", "هن": "«their (f.)»", "هما": "«their (dual)»", "ك": "«your»", "كم": "«your (pl.)»", "كن": "«your (f. pl.)»", "كما": "«your (dual)»", "نا": "«our»", "ي": "«my»", "ني": "«me»"}
ENC_TR = {"ه": "«onun»", "ها": "«onun (dişil)»", "هم": "«onların»", "هن": "«onların (dişil)»", "هما": "«ikisinin»", "ك": "«senin»", "كم": "«sizin»", "كن": "«sizin (dişil)»", "كما": "«ikinizin»", "نا": "«bizim»", "ي": "«benim»", "ني": "«beni»"}
# ---- the particles the matn uses (bare → ar/en/tr/grammar tags/key) ---------------------------------------------------
PART = {
 "و": ("الْوَاوُ حَرْفُ عَطْفٍ مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "«and» — the conjunction.", "«ve» — atıf harfi.", ["atf-nasaq"], "wa"),
 "ف": ("الْفَاءُ حَرْفُ عَطْفٍ (أَوِ اسْتِئْنَافٍ) مَبْنِيٌّ عَلَى الْفَتْحِ.", "«so / then» — the fa.", "«bunun üzerine» — fâ.", ["atf-nasaq"], "fa"),
 "ثم": ("حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي، مَبْنِيٌّ عَلَى الْفَتْحِ.", "«then» — the conjunction of sequence.", "«sonra» — tertip bildiren atıf harfi.", ["atf-nasaq"], "thumma"),
 "او": ("حَرْفُ عَطْفٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«or».", "«veya».", ["atf-nasaq"], "aw"),
 "بل": ("حَرْفُ إِضْرَابٍ وَعَطْفٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«rather» — the particle of correction.", "«bilakis» — idrâb harfi.", ["atf-nasaq"], "bal"),
 "لا": ("«لَا» حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«not» — the negation.", "«değil / -mez» — nefiy harfi.", [], "la-nafiya"),
 "لم": ("حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«did not» — the jussive negator.", "«-medi» — cezm eden nefiy harfi.", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], "lam-jazima"),
 "لن": ("حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«will not» — the subjunctive negator.", "«asla -meyecek» — nasb eden nefiy harfi.", ["nawasib-wa-jawazim-al-mudari"], "lan"),
 "ان": ("حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "the particle.", "harf.", [], None),
 "إن": ("«إِنْ» حَرْفُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "«if» — the conditional particle.", "«eğer» — şart harfi.", ["al-majzum-wal-shart-wal-jaza", "in-shartiyya"], "in-shartiyya"),
 "أن": ("«أَنْ» حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "«that / to» — the masdar particle.", "«-mesi» — masdariyye en.", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "an-masdariyya"),
 "إنّ": ("«إِنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "«indeed» — it puts its noun in nasb and its predicate in raf'.", "«şüphesiz» — ismini nasb, haberini ref eder.", ["inna-wa-akhawatuha"], "inna"),
 "أنّ": ("«أَنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "«that» — enne: it puts its noun in nasb and its predicate in raf'.", "«-diği» — enne: ismini nasb, haberini ref eder.", ["inna-wa-akhawatuha"], "anna"),
 "لان": ("اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَ«أَنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because» — the lam of cause with enne.", "«çünkü» — ta'lîl lâmı + enne.", ["inna-wa-akhawatuha", "huruf-jarr"], "lianna"),
  "لكن": ("«لٰكِنَّ» حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "«but» — the particle of amendment, a sister of inna: it puts its noun in nasb and its predicate in raf'.", "«fakat» — istidrâk harfi, inne'nin kardeşlerinden: ismini nasb, haberini ref eder.", ["inna-wa-akhawatuha"], "lakinna"),
  "لكن-sakina": ("«لٰكِنْ» حَرْفُ اسْتِدْرَاكٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "«but» — the light particle of amendment, built, no place in the i'rab.", "«fakat» — sükûn üzere mebnî istidrâk harfi.", [], "lakinna"),
 "لعل": ("«لَعَلَّ» حَرْفُ تَرَجٍّ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ.", "«perhaps» — a sister of inna.", "«umulur ki» — inne'nin kardeşlerinden.", ["inna-wa-akhawatuha"], "laalla"),
 "كان": ("«كَأَنَّ» حَرْفُ تَشْبِيهٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ.", "«as if» — a sister of inna.", "«sanki» — inne'nin kardeşlerinden.", ["inna-wa-akhawatuha"], "kaanna"),
 "ما": ("«مَا» حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«not» — the negation.", "«değil» — nefiy harfi.", [], "ma-nafiya"),
 "قد": ("حَرْفُ تَحْقِيقٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«indeed / already» — qad.", "«muhakkak» — tahkik harfi kad.", [], "qad"),
 "هل": ("حَرْفُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "the question particle «?».", "soru edatı «mı?».", ["al-istifham"], "hal"),
 "أ": ("هَمْزَةُ الِاسْتِفْهَامِ حَرْفٌ مَبْنِيٌّ عَلَى الْفَتْحِ.", "the question hamza «?».", "soru hemzesi.", ["al-istifham"], "hamza-istifham"),
 "يا": ("حَرْفُ نِدَاءٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«O» — the vocative particle.", "«ey» — nidâ harfi.", ["vocative-munada"], "ya-nida"),
 "الا": ("«إِلَّا» أَدَاةُ اسْتِثْنَاءٍ مَبْنِيَّةٌ عَلَى السُّكُونِ.", "«except» — illa.", "«-den başka» — istisnâ edatı.", ["istithna"], "illa"),
 "اذا": ("«إِذَا» ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ.", "«when» — the conditional time adverb.", "«-diğinde» — şart manası taşıyan zarf.", ["al-majzum-wal-shart-wal-jaza"], "idha"),
 "لو": ("«لَوْ» حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«if» — the counterfactual conditional.", "«eğer / -saydı» — cezmetmeyen şart harfi.", ["al-majzum-wal-shart-wal-jaza"], "law"),
 "لولا": ("«لَوْلَا» حَرْفُ امْتِنَاعٍ لِوُجُودٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«were it not for».", "«olmasaydı».", [], "lawla"),
 "كما": ("الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَ«مَا» مَصْدَرِيَّةٌ.", "«just as».", "«nitekim / gibi».", ["huruf-jarr"], "kama"),
 "حتى": ("«حَتَّى» حَرْفُ غَايَةٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«until / so that».", "«-e kadar / tâ ki».", [], "hatta"),
 "اما": ("«أَمَّا» حَرْفُ شَرْطٍ وَتَفْصِيلٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«as for».", "«-e gelince».", ["amma-tafsiliyya"], "amma"),
 "ام": ("«أَمْ» حَرْفُ عَطْفٍ لِلِاسْتِفْهَامِ.", "«or» (in a question).", "«yoksa».", ["atf-nasaq"], "am"),
 "سوف": ("حَرْفُ اسْتِقْبَالٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«will» — the future particle.", "«-ecek» — istikbal harfi.", [], "sawfa"),
 "كي": ("«كَيْ» حَرْفُ نَصْبٍ وَمَصْدَرٍ.", "«so that».", "«-mek için».", ["nawasib-wa-jawazim-al-mudari"], "kay"),
 "لكي": ("اللَّامُ حَرْفُ جَرٍّ، وَ«كَيْ» حَرْفُ نَصْبٍ وَمَصْدَرٍ.", "«in order that».", "«-mek için».", ["nawasib-wa-jawazim-al-mudari"], "li-kay"),
 "لمن": ("اللَّامُ حَرْفُ جَرٍّ، وَ«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.", "«for whoever» — the lam of jarr + the relative.", "«kim … ise ona» — cer lâmı + ism-i mevsûl.", ["huruf-jarr", "ism-mawsul"], "man"),
 "بما": ("الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.", "«by what» — the ba + the relative.", "«… şey ile» — bâ + ism-i mevsûl.", ["huruf-jarr", "ism-mawsul"], "ma-mawsula"),
 "فيما": ("«فِي» حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«in what».", "«… şeyde».", ["huruf-jarr", "ism-mawsul"], "ma-mawsula"),
 "فيمن": ("«فِي» حَرْفُ جَرٍّ، وَ«مَنْ» اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«in whoever».", "«… kimsede».", ["huruf-jarr", "ism-mawsul"], "man"),
 "كمن": ("الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَ«مَنْ» اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«like one who».", "«… kimse gibi».", ["huruf-jarr", "ism-mawsul"], "man"),
 "ممن": ("«مِنْ» حَرْفُ جَرٍّ، وَ«مَنْ» اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«from whoever».", "«… kimseden».", ["huruf-jarr", "ism-mawsul"], "man"),
 "انما": ("«إِنَّمَا» أَدَاةُ حَصْرٍ، كَافَّةٌ وَمَكْفُوفَةٌ.", "«only» — the particle of restriction.", "«ancak» — hasr edatı.", [], "innama"),
 "كلما": ("«كُلَّمَا» ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«whenever».", "«her ne zaman».", [], "kullama"),
 "ايها": ("«أَيُّهَا» مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَ«هَا» لِلتَّنْبِيهِ.", "«O …» — the vocative ayyuha.", "«ey …» — nidâ edatı eyyühâ.", ["vocative-munada"], "ayyuha"),
 "هلا": ("«هَلَّا» حَرْفُ تَحْضِيضٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«why not…?» — the particle of urging.", "«… değil mi?» — tahzîz harfi.", [], "halla"),
 "في": ("«فِي» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ.", "«in» — a preposition.", "«-de, içinde» — harf-i cer.", ["huruf-jarr"], "fi"),
 "على": ("«عَلَى» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ.", "«on, upon» — a preposition.", "«üzerine» — harf-i cer.", ["huruf-jarr"], "ala"),
 "الى": ("«إِلَى» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ.", "«to» — a preposition.", "«-e, -e doğru» — harf-i cer.", ["huruf-jarr"], "ila"),
 "من": ("«مِنْ» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ.", "«from, of» — a preposition.", "«-den» — harf-i cer.", ["huruf-jarr"], "min"),
 "عن": ("«عَنْ» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ.", "«from, about» — a preposition.", "«-den, hakkında» — harf-i cer.", ["huruf-jarr"], "an"),
 "مع": ("«مَعَ» ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«with» — an adverb (zarf) in nasb, annexed.", "«ile, beraber» — mansûb zarf, muzâf.", ["maful-fih"], "maa"),
 "عند": ("«عِنْدَ» ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«at, with» — an adverb of place in nasb, annexed.", "«yanında, katında» — mansûb mekân zarfı, muzâf.", ["maful-fih"], "inda"),
 "بعد": ("«بَعْدُ» ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ لِقَطْعِهِ عَنِ الْإِضَافَةِ، فِي مَحَلِّ نَصْبٍ.", "«afterwards» — the adverb cut from annexation, built on the damma.", "«sonra» — izâfetten kesildiği için damme üzere mebnî zarf.", ["maful-fih", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya"], "bada"),
 "قبل": ("«قَبْلُ» ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ لِقَطْعِهِ عَنِ الْإِضَافَةِ.", "«before» — the adverb cut from annexation.", "«önce» — izâfetten kesilmiş zarf.", ["maful-fih"], "qabla"),
 "بين": ("«بَيْنَ» ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«between» — an adverb of place in nasb, annexed.", "«arasında» — mansûb mekân zarfı, muzâf.", ["maful-fih"], "bayna"),
 "دون": ("«دُونَ» ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«without, below» — an adverb in nasb, annexed.", "«-sız, altında» — mansûb zarf, muzâf.", ["maful-fih"], "duna"),
 "بلى": ("حَرْفُ جَوَابٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«yes indeed».", "«evet, bilakis».", [], "bala-yes"),
 "نعم": ("حَرْفُ جَوَابٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«yes».", "«evet».", [], "naam"),
}
PRON = {"هو": ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "«he / it»", "«o»", "huwa"), "هي": ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "«she / it»", "«o (dişil)»", "hiya"), "هم": ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ", "«they»", "«onlar»", "hum"), "هن": ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "«they (f.)»", "«onlar (dişil)»", "hunna"), "هما": ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ", "«they two»", "«o ikisi»", "huma"), "انت": ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "«you»", "«sen»", "anta"), "انتم": ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ", "«you (pl.)»", "«siz»", "antum"), "انا": ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ", "«I»", "«ben»", "ana"), "نحن": ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ", "«we»", "«biz»", "nahnu")}
DEM = {"ذا": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ", "هذا": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ", "هذه": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ", "ذلك": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "تلك": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "هؤلاء": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ", "اولئك": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "الذي": "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ", "التي": "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ", "الذين": "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "من": "اسْمٌ مَوْصُولٌ (أَوْ شَرْطِيٌّ) مَبْنِيٌّ عَلَى السُّكُونِ", "ما": "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ"}
CASE_AR = {"raf": "رَفْعٍ", "nasb": "نَصْبٍ", "jarr": "جَرٍّ", "jazm": "جَزْمٍ"}
KANA_FAM = {"كان", "يكون", "تكون", "اكون", "نكون", "كانت", "كانوا", "كنت", "كنتم", "ليس", "ليست", "صار", "يصير", "اصبح", "يصبح", "امسى", "ظل", "بات", "مازال", "لايزال", "لازال"}
JAZM_GOV = {"لم", "لما", "لن", "ان", "كي", "لكي", "حتى", "لئلا", "الا"}   # the governors after which a يـ/تـ/أـ/نـ word is the verb they govern
ROLE = {  # rule → (ar role with its case word, en, tr, grammar tags)
 "mubtada": ("مُبْتَدَأٌ مَرْفُوعٌ", "The mubtada (subject of the nominal sentence), in raf'", "Mübtedâ, merfû", ["mubtada-khabar"]),
 "khabar": ("خَبَرٌ مَرْفُوعٌ", "The khabar (predicate), in raf'", "Haber, merfû", ["mubtada-khabar"]),
 "fail": ("فَاعِلٌ مَرْفُوعٌ", "The doer (fa'il), in raf'", "Fâil, merfû", ["fail"]),
 "naib": ("نَائِبُ فَاعِلٍ مَرْفُوعٌ", "The deputy doer (na'ib al-fa'il), in raf'", "Nâib-i fâil, merfû", ["naib-al-fail"]),
 "maful": ("مَفْعُولٌ بِهِ مَنْصُوبٌ", "The object (maf'ul bihi), in nasb", "Mef'ûlün bih, mansûb", ["maful-bihi"]),
 "maful2": ("مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ", "The second object, in nasb", "İkinci mef'ûlün bih, mansûb", ["maful-bihi"]),
 "mudafIlayh": ("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "The annexed noun (mudaf ilayh), in jarr", "Muzâfun ileyh, mecrûr", ["idafa-definiteness"]),
 "jarr": ("مَجْرُورٌ", "In jarr after the preposition", "Mecrûr", ["huruf-jarr"]),
 "atf": ("مَعْطُوفٌ", "Joined by the conjunction to the word before it; the same case", "Ma'tûf; aynı i'râb", ["atf-nasaq"]),
 "nat": ("نَعْتٌ", "An adjective (na't) agreeing with its noun in case", "Sıfat (na't); mevsûfuna uyar", ["naat-sifa"]),
 "hal": ("حَالٌ مَنْصُوبٌ", "The circumstantial (hal), in nasb", "Hâl, mansûb", ["hal"]),
 "tamyiz": ("تَمْيِيزٌ مَنْصُوبٌ", "The specifier (tamyiz), in nasb", "Temyiz, mansûb", ["tamyiz"]),
 "zarf": ("ظَرْفٌ مَنْصُوبٌ", "An adverb of time or place (zarf), in nasb", "Zarf, mansûb", ["maful-fih"]),
 "mafulMutlaq": ("مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ", "The absolute object (maf'ul mutlaq), in nasb", "Mef'ûl-i mutlak, mansûb", ["maful-mutlaq"]),
 "mafulLah": ("مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ", "The object of purpose, in nasb", "Mef'ûlün lieclih, mansûb", ["maful-lah"]),
 "badal": ("بَدَلٌ", "A substitute (badal); the same case as its head", "Bedel; aynı i'râb", ["badal"]),
 "kanaIsm": ("اسْمُ كَانَ مَرْفُوعٌ", "The noun of kana, in raf'", "Kâne'nin ismi, merfû", ["kana-wa-akhawatuha"]),
 "kanaKhabar": ("خَبَرُ كَانَ مَنْصُوبٌ", "The predicate of kana, in nasb", "Kâne'nin haberi, mansûb", ["kana-wa-akhawatuha"]),
 "innaIsm": ("اسْمُ إِنَّ مَنْصُوبٌ", "The noun of inna, in nasb", "İnne'nin ismi, mansûb", ["inna-wa-akhawatuha"]),
 "innaKhabar": ("خَبَرُ إِنَّ مَرْفُوعٌ", "The predicate of inna, in raf'", "İnne'nin haberi, merfû", ["inna-wa-akhawatuha"]),
 "mustathna": ("مُسْتَثْنًى مَنْصُوبٌ", "The excepted noun, in nasb", "Müstesnâ, mansûb", ["istithna"]),
 "munada": ("مُنَادًى", "The called noun (munada)", "Münâdâ", ["vocative-munada"]),
 "tawkid": ("تَوْكِيدٌ", "An emphasis (tawkid); the same case as its head", "Te'kîd; aynı i'râb", ["tawkid"]),
 "laIsm": ("اسْمُ لَا النَّافِيَةِ لِلْجِنْسِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ", "The noun of the genus-denying la", "Cinsi nefyeden lâ'nın ismi", ["la-nafiya-lil-jins"]),
}
CASE_OF_RULE = {"mubtada": "raf", "khabar": "raf", "fail": "raf", "naib": "raf", "kanaIsm": "raf", "innaKhabar": "raf", "maful": "nasb", "maful2": "nasb", "hal": "nasb", "tamyiz": "nasb", "zarf": "nasb", "mafulMutlaq": "nasb", "mafulLah": "nasb", "kanaKhabar": "nasb", "innaIsm": "nasb", "mustathna": "nasb", "mudafIlayh": "jarr", "jarr": "jarr"}
SIGN = {  # (case, shape) → (ar, en, tr)
 ("raf", "sahih"): ("بِالضَّمَّةِ", "the damma", "damme ile"), ("nasb", "sahih"): ("بِالْفَتْحَةِ", "the fatha", "fetha ile"), ("jarr", "sahih"): ("بِالْكَسْرَةِ", "the kasra", "kesre ile"),
 ("raf", "muthanna"): ("بِالْأَلِفِ لِأَنَّهُ مُثَنًّى", "the alif — it is a dual", "elif ile — tesniyedir"), ("nasb", "muthanna"): ("بِالْيَاءِ لِأَنَّهُ مُثَنًّى", "the ya — it is a dual", "yâ ile — tesniyedir"), ("jarr", "muthanna"): ("بِالْيَاءِ لِأَنَّهُ مُثَنًّى", "the ya — it is a dual", "yâ ile — tesniyedir"),
 ("raf", "jam-m"): ("بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", "the waw — a sound masculine plural", "vâv ile — cem'-i müzekker sâlim"), ("nasb", "jam-m"): ("بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", "the ya — a sound masculine plural", "yâ ile — cem'-i müzekker sâlim"), ("jarr", "jam-m"): ("بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", "the ya — a sound masculine plural", "yâ ile — cem'-i müzekker sâlim"),
 ("raf", "jam-f"): ("بِالضَّمَّةِ", "the damma", "damme ile"), ("nasb", "jam-f"): ("بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ", "the kasra in place of the fatha — a sound feminine plural", "fetha yerine kesre ile — cem'-i müennes sâlim"), ("jarr", "jam-f"): ("بِالْكَسْرَةِ", "the kasra", "kesre ile"),
 ("raf", "maqsur"): ("بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "an implied damma on the alif", "elif üzerinde takdîrî damme ile"), ("nasb", "maqsur"): ("بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "an implied fatha on the alif", "elif üzerinde takdîrî fetha ile"), ("jarr", "maqsur"): ("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "an implied kasra on the alif", "elif üzerinde takdîrî kesre ile"),
 ("raf", "manqus"): ("بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "an implied damma on the ya", "yâ üzerinde takdîrî damme ile"), ("nasb", "manqus"): ("بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ", "the fatha on the ya", "yâ üzerinde fetha ile"), ("jarr", "manqus"): ("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "an implied kasra on the ya", "yâ üzerinde takdîrî kesre ile"),
 ("raf", "ya-mutakallim"): ("بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ يَاءِ الْمُتَكَلِّمِ", "an implied damma — the speaker's ya takes the seat", "mütekellim yâsı sebebiyle takdîrî damme ile"), ("nasb", "ya-mutakallim"): ("بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ يَاءِ الْمُتَكَلِّمِ", "an implied fatha — the speaker's ya takes the seat", "mütekellim yâsı sebebiyle takdîrî fetha ile"), ("jarr", "ya-mutakallim"): ("بِكَسْرَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ يَاءِ الْمُتَكَلِّمِ", "an implied kasra — the speaker's ya takes the seat", "mütekellim yâsı sebebiyle takdîrî kesre ile"),
 ("raf", "khamsa"): ("بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "the waw — one of the five nouns", "vâv ile — esmâ-i hamseden"), ("nasb", "khamsa"): ("بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "the alif — one of the five nouns", "elif ile — esmâ-i hamseden"), ("jarr", "khamsa"): ("بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "the ya — one of the five nouns", "yâ ile — esmâ-i hamseden"),
 ("jarr", "mamnu"): ("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ", "the fatha in place of the kasra — a diptote", "kesre yerine fetha ile — gayr-i munsarif"),
}
SHAPE_TAG = {"muthanna": ["al-muthanna"], "jam-m": ["jam-mudhakkar-salim"], "jam-f": ["jam-muannath-salim"], "maqsur": ["ism-maqsur-manqus"], "manqus": ["ism-maqsur-manqus"], "ya-mutakallim": ["al-taqdiri-al-thani-wal-thalith-al-mudaf-ila-al-ya-wal-mahki"], "khamsa": ["al-asma-al-khamsa"], "mamnu": ["ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"]}

def host_of(w, enc):
    """the written word without its enclitic pronoun"""
    w = N(w)
    if enc:
        b = bare(w)
        if b.endswith(enc):
            # drop the enclitic's letters from the END, diacritics included
            n = len(enc); out = w; k = 0
            while k < n and out:
                ch = out[-1]; out = out[:-1]
                if not DIA.match(ch): k += 1
            return out
    return w

def pre_of(w):
    b = bare(w)
    if len(b) >= 3 and b[0] in "وف" and N(w)[1:2] == "َ": return b[0]
    return ""

PREPS = {"من", "الى", "على", "في", "عن", "حتى", "منذ", "مذ", "رب", "خلا", "عدا", "حاشا", "لدى", "لدن", "ب", "ل", "ك"}
MABNI_ZARF = {"قط": "ظَرْفٌ لِاسْتِغْرَاقِ الزَّمَانِ الْمَاضِي", "بعد": "ظَرْفُ زَمَانٍ", "قبل": "ظَرْفُ زَمَانٍ", "فوق": "ظَرْفُ مَكَانٍ", "تحت": "ظَرْفُ مَكَانٍ", "دون": "ظَرْفُ مَكَانٍ", "حسب": "اسْمٌ بِمَعْنَى كَافٍ"}
def written_case(hn, enc, cs, lem_b=None, lem_full=None, propn=False, prev_wc=None):
    """the case the written ending of a noun host shows — None where the ending is silent or ambiguous (maqṣūr, manqūṣ, the ـَات plural's kasra, the speaker's yāʾ, a dual/plural known from the lemma in ـِينَ/ـَيْنِ, a diptote's jarr fatḥa, the five nouns' letters)"""
    h = N(hn).replace("ّ", ""); hb = bare(hn); hb_ = noal(hb)
    if len(hb) < 2 or enc in ("ي", "ني", "يَ"): return None
    if re.search(r"ات$", hb) and not re.search(r"[ًٌَُ]$", h): return None
    du = lem_b is not None and (hb_ in (lem_b + "ان", lem_b + "ين") or (lem_b.endswith("ة") and hb_ in (lem_b[:-1] + "تان", lem_b[:-1] + "تين")))
    pl = lem_b is not None and (hb_ in (lem_b + "ون", lem_b + "ين") or (re.search(r"(ون|ين)$", lem_b) and hb_ in (lem_b, lem_b[:-2] + "ون", lem_b[:-2] + "ين")))
    lf0 = N(str(lem_full or "").split("(")[0].strip()).replace("ٰ", "")
    plural_lemma = lem_b is not None and bool(re.search(r"(ين|ون)$", lem_b)) and len(lem_b) >= 5
    if hb_.startswith("ل") and lem_b and hb_ != lem_b and hb_[1:] in (lem_b, lem_b + "ون", lem_b + "ين", lem_b + "ان", lem_b[:-1] + "ت" if lem_b.endswith("ة") else lem_b + "ات"): hb_ = hb_[1:]   # لَكَاذِبُونَ: the lām al-muzaḥlaqa before the noun
    own = lem_b is not None and hb_ == lem_b and not plural_lemma and not re.search(r"(َانِ|َيْنِ)$", lf0.replace("ّ", ""))   # the lemma itself ends in these letters (دِين، عَيْن، إِيمَان): read its last vowel
    if lem_b is not None and hb_ == lem_b and plural_lemma: pl = True
    if re.search(r"ُونَ$", h) and len(hb) >= 4 and not own: return "raf"   # the sound plural's wāw is rafʿ whatever the lemma says
    if re.search(r"^(كلا|كلتا)$", hb) and enc: return "raf"
    if re.search(r"^(كلي|كلتي)$", hb) and enc: return None
    if re.search(r"َيْ$", h) and len(hb) >= 3 and not own and not enc and not re.search(r"^(ال|لل)", hb): return "nasb-jarr"
    if re.search(r"َانِ$", h) and not own: return "raf" if du else None
    if re.search(r"ِينَ$", h) and len(hb) >= 4 and not own: return None
    if re.search(r"َيْنِ$", h) and not own: return "nasb-jarr" if du else None   # (patch 32) the lemma's dual in ـَيْنِ is nasb or jarr
    lf = lf0
    manqus = bool(lf) and (bool(re.search(r"ٍ$", lf)) or (bare(lf).endswith("ي") and hb_ == noal(bare(lf))[:-1]))
    if manqus and re.search(r"[ٍِ]$", h) and not enc and not hb.startswith("ال"): return None   # بَاقٍ / صَالِ: the manqūṣ hides its rafʿ and jarr
    m = re.search(r"([ًٌٍَُِْ])([اى])?$", h)
    if not m: return None
    v, al = m.group(1), m.group(2)
    if (al and v != "ً") or v == "ْ": return None
    if v in "ٌُ": return "raf"
    if v in "ٍِ": return "jarr"
    if v == "ً": return "nasb"
    if not (hb.startswith("ال") or enc or hb.startswith("لل")):   # a bare fatḥa on an undetermined noun may be a diptote's jarr (عَلْقَمَةَ، هُرَيْرَةَ، نُعْمَانَ بْنِ ثَابِتٍ)
        if propn: return "jarr" if prev_wc == "jarr" else ("nasb" if prev_wc == "verb" else None)
        if cs == "jarr": return None if diptote_like(hb_, lf0) else "nasb"
    return "nasb"
def host_written(words, q):
    """the written host of word q (the source token with its last vowel), without its وَ/فَ prefix and its enclitic"""
    wj = words[q]; enc = wj.get("enc") or ""
    raw = raw_at(words, q); wr = N(re.sub(r"[،:؛.؟!«»\"()]", "", raw)) if raw else N(wj["w"])
    h = N(host_of(wr, enc)); return h[2:] if pre_of(wr) else h
def enc_of(wj): return wj.get("enc") or ""
def is_verb_w(wj): return wj.get("kind") == "verb" or wj.get("k") == "cell" or wj.get("rule") in ("mazi", "amr", "raf", "nasbVerb", "jazm", "shart", "jawab")
def is_noun_w(wj): return wj.get("kind") == "noun" and wj.get("k") not in ("keep", "cell") and not is_verb_w(wj)
def wc_word(words, q, depth=1):
    """the written case of word q by its ending and lemma; a diptote name's fatḥa is read from the word before it (one step)"""
    wj = words[q]; lemj = str(wj.get("lemma") or "").split("(")[0].strip()
    prev_wc = wc_word(words, q - 1, 0) if depth and q > 0 and is_noun_w(words[q - 1]) else None
    pb_ = bare(words[q - 1]["w"]).replace("أ", "ا").replace("إ", "ا") if q > 0 else ""
    return written_case(host_written(words, q), wj.get("enc") or "", None, noal(bare(lemj)) if lemj else None, lemj or None, propn=(wj.get("pos") == "propn"), prev_wc=("jarr" if (prev_wc == "jarr" or pb_ in PREPS) else ("verb" if q > 0 and is_verb_w(words[q - 1]) else None)))
KANA_RE = re.compile(r"^(كان|كانت|كانا|كانوا|كن|كنت|كنتم|كنتما|كنتن|كنا|نك|نكن|نكون|يك|يكن|يكون|يكونا|يكونوا|يكونون|تك|تكن|تكون|تكونوا|تكونون|اك|اكن|اكون|ليس|ليست|ليسا|ليسوا|لست|لستم|لستما|لسنا|لسن|اصبح|اصبحت|اصبحوا|اصبحنا|يصبح|صار|صارت|صاروا|يصير|امسى|اضحى|ظل|بات|زال|يزال|يزل|يزالون|تزال|نزال|فتئ|برح|دام|يدوم|يدم)$")
FIVE = {"ابي": "jarr", "اخي": "jarr", "ذي": "jarr", "ابو": "raf", "اخو": "raf", "ذو": "raf", "ابا": "nasb", "اخا": "nasb", "حمي": "jarr", "حمو": "raf", "حما": "nasb"}
EXTRA_PART = {   # bare → (ar, en, tr, lex, tags)
 "اي": ("«أَيْ» حَرْفُ تَفْسِيرٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "«that is, i.e.» — the explanatory particle, built on sukūn.", "«yani» — tefsir harfi, sükûn üzere mebnî.", "ay", ["huruf-al-maani"]),
 "ايها": ("«أَيُّ» مُنَادَى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَ«هَا» لِلتَّنْبِيهِ، وَمَا بَعْدَهَا نَعْتٌ لَهَا (أَوْ بَدَلٌ) مَرْفُوعٌ.", "«O …»: «ayyu» a vocative built on ḍamma in the seat of naṣb, «hā» of alerting; the noun after it is its naʿt (or badal) in rafʿ.", "«ey …»: «eyyü» zamme üzere mebnî münâdâ, nasb mahallinde; «hâ» tenbih için; sonrası sıfatı (yahut bedeli), merfû.", "ayyuha", ["al-munada"]),
 "ماذا": ("«مَا» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ (أَوْ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ)، وَ«ذَا» اسْمُ إِشَارَةٍ أَوْ زَائِدَةٌ.", "«what?»: «mā» an interrogative noun built on sukūn, subject (or a fronted object); «dhā» a demonstrative or extra.", "«ne?»: «mâ» sükûn üzere mebnî istifhâm ismi, mübtedâ (yahut öne alınmış mef'ûl); «zâ» işaret ismi yahut zâid.", "madha", ["al-istifham"]),
 "اين": ("اسْمُ اسْتِفْهَامٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ (خَبَرٌ مُقَدَّمٌ).", "«where?»: an interrogative noun of place built on fatḥa, in the seat of naṣb as an adverb of place (a fronted predicate).", "«nerede?»: fetha üzere mebnî mekân istifhâm ismi, nasb mahallinde mekân zarfı (öne alınmış haber).", "ayna", ["al-istifham"]),
 "متى": ("اسْمُ اسْتِفْهَامٍ لِلزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ ظَرْفُ زَمَانٍ.", "«when?»: an interrogative noun of time built on sukūn, in the seat of naṣb as an adverb of time.", "«ne zaman?»: sükûn üzere mebnî zaman istifhâm ismi, nasb mahallinde zaman zarfı.", "mata", ["al-istifham"]),
 "كذا": ("الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَ«ذَا» اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ (لِمَا بَعْدَهُ).", "«likewise»: the kāf a jarr letter of likeness, «dhā» a demonstrative built on sukūn in the seat of jarr; the phrase is a fronted predicate.", "«keza, böylece»: kâf teşbih için harf-i cer, «zâ» sükûn üzere mebnî işaret ismi, cer mahallinde; câr-mecrûr öne alınmış haber.", "kadha", ["asma-al-ishara-wa-sighuha", "huruf-jarr"]),
 "هكذا": ("«هَا» لِلتَّنْبِيهِ، وَالْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَ«ذَا» اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«thus»: «hā» of alerting, the kāf a jarr letter of likeness, «dhā» a demonstrative in the seat of jarr.", "«böyle»: «hâ» tenbih, kâf teşbih için harf-i cer, «zâ» cer mahallinde mebnî işaret ismi.", "hakadha", ["asma-al-ishara-wa-sighuha"]),
 "اجل": ("«أَجَلْ» حَرْفُ جَوَابٍ وَتَصْدِيقٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "«yes, indeed»: a particle of answer and affirmation, built on sukūn.", "«evet, elbette»: sükûn üzere mebnî cevap ve tasdik harfi.", "ajal", []),
 "لما": ("«لَمَّا» ظَرْفٌ بِمَعْنَى «حِينَ» مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ.", "«when» — an adverb meaning «at the time that», carrying a conditional sense, built on sukūn in the seat of naṣb.", "«… -dığında» — «hîne» anlamında şart manası taşıyan zarf, sükûn üzere mebnî, nasb mahallinde (muzâriden önce nefiy ve cezm harfidir).", "lamma", ["al-shart"]),
 "بلا": ("الْبَاءُ حَرْفُ جَرٍّ، وَ«لَا» نَافِيَةٌ مُعْتَرِضَةٌ بَيْنَ الْجَارِّ وَالْمَجْرُورِ (بِمَعْنَى غَيْرِ)، وَالِاسْمُ بَعْدَهَا يَأْخُذُ الْكَسْرَةَ بِالْبَاءِ.", "«without»: the bāʾ a jarr letter, «lā» a negation set between the jarr letter and its noun (meaning «other than»); the following noun is in jarr by the bāʾ.", "«-sız, -sız olarak»: bâ harf-i cer, «lâ» câr ile mecrûr arasına giren nefiy (gayr anlamında); sonraki isim bâ ile mecrûr.", "bi", ["huruf-jarr", "la-nafiya"]),
 "مما": ("«مَا» اسْمٌ مَوْصُولٌ (أَوْ مَصْدَرِيَّةٌ) مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِـ«مِنْ» حَرْفِ الْجَرِّ قَبْلَهَا.", "«of what / because of what»: «min» a jarr letter, «mā» a relative (or maṣdar) noun built on sukūn in the seat of jarr.", "«…-den, …-den dolayı»: «min» harf-i cer, «mâ» sükûn üzere mebnî ism-i mevsûl (yahut masdariye), cer mahallinde.", "min", ["huruf-jarr", "ism-mawsul"]),
 "عما": ("«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِـ«عَنْ» حَرْفِ الْجَرِّ قَبْلَهَا.", "«about what»: «ʿan» a jarr letter, «mā» a relative noun built on sukūn in the seat of jarr.", "«…-den, hakkında»: «an» harf-i cer, «mâ» sükûn üzere mebnî ism-i mevsûl, cer mahallinde.", "an", ["huruf-jarr", "ism-mawsul"]),
 "بمن": ("«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِالْبَاءِ حَرْفِ الْجَرِّ قَبْلَهَا.", "«by / with one who»: the bāʾ a jarr letter, «man» a relative noun built on sukūn in the seat of jarr.", "«… kimse ile»: bâ harf-i cer, «men» sükûn üzere mebnî ism-i mevsûl, cer mahallinde.", "bi", ["huruf-jarr", "ism-mawsul"]),
 "رب": ("«رُبَّ» حَرْفُ جَرٍّ شَبِيهٌ بِالزَّائِدِ لِلتَّقْلِيلِ أَوِ التَّكْثِيرِ، مَبْنِيٌّ عَلَى الْفَتْحِ.", "«many a / seldom a …»: a jarr letter resembling the extra one, of fewness or muchness, built on fatḥa.", "«nice … / az …»: azlık yahut çokluk için zâide benzer harf-i cer, fetha üzere mebnî.", "rubba", ["huruf-jarr"]),
 "الم": ("الْهَمْزَةُ لِلِاسْتِفْهَامِ (الْإِنْكَارِيِّ أَوِ التَّقْرِيرِيِّ)، وَ«لَمْ» حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«did … not?»: the hamza asks (in denial or affirmation), «lam» the negating, jussive, time-turning particle built on sukūn.", "«… değil mi?»: hemze istifhâm (inkârî yahut takrîrî), «lem» nefiy, cezm ve kalb harfi, sükûn üzere mebnî.", "lam", ["al-istifham", "nawasib-wa-jawazim-al-mudari"]),
 "اولم": ("الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَالْوَاوُ عَاطِفَةٌ، وَ«لَمْ» حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and did … not?»: the hamza asks, the wāw conjoins, «lam» negates and puts the verb in jazm.", "«ve … değil mi?»: hemze istifhâm, vâv atıf, «lem» nefiy ve cezm harfi.", "lam", ["al-istifham", "nawasib-wa-jawazim-al-mudari"]),
 "لفي": ("اللَّامُ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَ«فِي» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ.", "«surely in»: the displaced lām of emphasis, «fī» a jarr letter built on sukūn.", "«muhakkak … içinde»: tekid için müzahlaka lâmı, «fî» sükûn üzere mebnî harf-i cer.", "fi", ["huruf-jarr"]),
 "افي": ("الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَ«فِي» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ.", "«is … in?»: the hamza asks, «fī» a jarr letter built on sukūn.", "«… içinde mi?»: hemze istifhâm, «fî» sükûn üzere mebnî harf-i cer.", "fi", ["al-istifham", "huruf-jarr"]),
 "لانا": ("اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَ«أَنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَ«نَا» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«because we»: the lām a jarr letter of cause, «anna» the emphasising particle, «nā» the attached pronoun as its noun.", "«çünkü biz»: lâm ta'lil için harf-i cer, «enne» tekid ve nasb harfi, «nâ» ismi olan bitişik zamir.", "anna", ["inna-wa-akhawatuha"]),
 "ايا": ("«إِيَّا» ضَمِيرُ نَصْبٍ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَمَا لَحِقَهُ حَرْفٌ دَالٌّ عَلَى الْمُخَاطَبِ أَوِ الْغَائِبِ.", "«iyyā» — the detached object pronoun in the seat of naṣb; the letter after it marks the addressee or the absent.", "«iyyâ» — nasb mahallinde munfasıl nasb zamiri; ardındaki harf muhatap yahut gaibi gösterir.", "iyya", ["al-damair"]),
 "خلا": ("«خَلَا» حَرْفُ اسْتِثْنَاءٍ وَجَرٍّ (أَوْ فِعْلٌ مَاضٍ وَمَا بَعْدَهُ مَفْعُولُهُ) مَبْنِيٌّ عَلَى السُّكُونِ الْمُقَدَّرِ.", "«except» — a particle of exception and jarr (or a past verb whose object follows).", "«hariç» — istisnâ ve cer harfi (yahut mef'ûlü ardından gelen mâzî fiil).", "khala", ["al-istithna"]),
 "لذا": ("اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَ«ذَا» اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.", "«therefore»: the lām a jarr letter of cause, «dhā» a demonstrative built on sukūn in the seat of jarr.", "«bu yüzden»: lâm ta'lil için harf-i cer, «zâ» sükûn üzere mebnî işaret ismi, cer mahallinde.", "dha", ["asma-al-ishara-wa-sighuha", "huruf-jarr"]),
 "اهي": ("الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَ«هِيَ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«is she / it …?»: the hamza asks, «hiya» a detached pronoun built on fatḥa in the seat of rafʿ as subject.", "«o mu …?»: hemze istifhâm, «hiye» fetha üzere mebnî munfasıl zamir, ref mahallinde mübtedâ.", "hiya", ["al-istifham", "al-damair"]),
 "اهم": ("الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَ«هُمْ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«are they …?»: the hamza asks, «hum» a detached pronoun built on sukūn in the seat of rafʿ as subject.", "«onlar mı …?»: hemze istifhâm, «hüm» sükûn üzere mebnî munfasıl zamir, ref mahallinde mübtedâ.", "hum", ["al-istifham", "al-damair"]),
 "لئن": ("اللَّامُ مُوَطِّئَةٌ لِلْقَسَمِ، وَ«إِنْ» حَرْفُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "«surely if»: the lām that prepares the oath's answer, «in» the jussive conditional particle built on sukūn.", "«andolsun eğer»: kasem için muvattıa lâmı, «in» sükûn üzere mebnî câzim şart harfi.", "in", ["al-shart", "al-qasam"]),
 "ربما": ("«رُبَّ» حَرْفُ تَقْلِيلٍ أَوْ تَكْثِيرٍ كُفَّ بِ«مَا» الْكَافَّةِ عَنْ عَمَلِ الْجَرِّ فَدَخَلَ عَلَى الْجُمْلَةِ.", "«perhaps / often»: «rubba» hindered by the restraining «mā» from governing, so it enters upon a clause.", "«belki / çok kere»: «rubbe» kâffe «mâ» ile cer amelinden alıkonmuş, cümleye dâhil olur.", "rubba", ["huruf-jarr"]),
 "لكنا": ("«لٰكِنَّ» حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، وَ«نَا» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«but we»: «lākinna» the corrective sister of inna, «nā» the attached pronoun as its noun.", "«fakat biz»: «lâkinne» istidrâk ve nasb harfi (inne'nin kardeşlerinden), «nâ» ismi olan bitişik zamir.", "lakinna", ["inna-wa-akhawatuha"]),
 "كانما": ("«كَأَنَّ» حَرْفُ تَشْبِيهٍ مِنْ أَخَوَاتِ إِنَّ كُفَّ بِ«مَا» الْكَافَّةِ عَنِ الْعَمَلِ، فَدَخَلَ عَلَى الْجُمْلَةِ.", "«as though»: «ka-anna» hindered by the restraining «mā», so it enters upon a clause without governing.", "«sanki»: «ke-enne» kâffe «mâ» ile amelden alıkonmuş, cümleye dâhil olur.", "kaanna", ["inna-wa-akhawatuha"]),
 "حاش": ("«حَاشَ» (أَصْلُهَا حَاشَا) لِلتَّنْزِيهِ: حَرْفُ جَرٍّ عِنْدَ قَوْمٍ، وَفِعْلٌ مَاضٍ جَامِدٌ عِنْدَ آخَرِينَ، وَلَفْظُ الْجَلَالَةِ بَعْدَهَا مَجْرُورٌ.", "«ḥāsha» (for ḥāshā) of exoneration — a jarr letter for some grammarians, a frozen past verb for others; «Allāh» after it is in jarr.", "«hâşe» (aslı hâşâ) tenzih için — kimine göre harf-i cer, kimine göre câmid mâzî fiil; lafza-i celâl ondan sonra mecrûr.", "hasha", ["al-istithna"]),
 "اياه": ("ضَمِيرُ نَصْبٍ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«him / it» — a detached object pronoun, built, in the seat of naṣb as the object.", "«onu» — munfasıl nasb zamiri, mebnî, nasb mahallinde mef'ûlün bih.", "iyya", ["al-damair"]),
 "اياك": ("ضَمِيرُ نَصْبٍ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ (مُقَدَّمٌ).", "«you» — a detached object pronoun, built, in the seat of naṣb as the (fronted) object.", "«seni» — munfasıl nasb zamiri, nasb mahallinde (öne alınmış) mef'ûlün bih.", "iyya", ["al-damair"]),
 "اياي": ("ضَمِيرُ نَصْبٍ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«me» — a detached object pronoun, in the seat of naṣb as the fronted object.", "«beni» — munfasıl nasb zamiri, nasb mahallinde öne alınmış mef'ûlün bih.", "iyya", ["al-damair"]),
 "اياهم": ("ضَمِيرُ نَصْبٍ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«them» — a detached object pronoun, in the seat of naṣb as the object.", "«onları» — munfasıl nasb zamiri, nasb mahallinde mef'ûlün bih.", "iyya", ["al-damair"]),
 "ايانا": ("ضَمِيرُ نَصْبٍ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«us» — a detached object pronoun, in the seat of naṣb as the object.", "«bizi» — munfasıl nasb zamiri, nasb mahallinde mef'ûlün bih.", "iyya", ["al-damair"]),
}
def verb_key_for(h2):
    """the verb whose lemma owns a written verb form — the engine's bare-letter key may name a homograph noun (قَالَ ≠ قَالٍ, سَلَّمَ ≠ سَلَام, رَضِيَ ≠ رَضِيّ).
    1. the lemma itself (or its stem with another last vowel); 2. a māḍī with a person suffix: the stem before the suffix against the lemma, one weak letter free;
    3. a muḍāriʿ / amr: the letters after the يـ/تـ/أـ/نـ prefix and before the ending against the lemma's letters (the augmented bābs' alif dropped), scored by the shadda and the inner alif the two share and by the prefix vowel"""
    h = N(h2).replace("ٰ", ""); hs = h.replace("ّ", ""); hb = bare(h2)
    STEM = lambda x: re.sub(r"[ًٌٍَُِْ]$", "", x.replace("ّ", ""))
    hit = VERB_BY_LEMMA.get(h) or (VERB_BY_STEM.get(STEM(h)) if not re.search(r"ُ$", hs) else None)
    if hit: return hit[0]
    FOLD = lambda x: x.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ٱ", "ا").replace("ى", "ي")
    def letters_ok(s, L):   # s: written stem letters; L: lemma letters (both folded, no shadda)
        if s == L: return 2
        if len(s) == len(L):
            d = [(x, y) for x, y in zip(s, L) if x != y]
            if len(d) == 1 and d[0][0] in "واي" and d[0][1] in "واي": return 1
        if len(L) == len(s) + 1:   # the hollow verb's dropped middle (قُلْتُ ← قَالَ), the defective's dropped last (دَعَوْا ← دَعَا), the assimilated verb's first و (يَصِلُ ← وَصَلَ)
            for k in range(0, len(L)):
                if L[k] in "واي" and L[:k] + L[k + 1:] == s: return 1
        return 0
    def cands(s, pref_v, shadda, inner_alif):
        best = None
        for lm, (kk, ee) in VERB_BY_LEMMA.items():
            L = FOLD(bare(lm)); Lsh = "ّ" in lm; Lalif = bool(re.search(r"^.ا", L)) and len(L) >= 4
            sc = letters_ok(s, L); aug = False
            if not sc and L.startswith("ا") and len(L) >= 4: sc = letters_ok(s, L[1:]); aug = bool(sc)
            if not sc: continue
            sc *= 3
            sc += 2 if shadda == Lsh else -2
            sc += 1 if inner_alif == (Lalif and not aug) else -1
            if pref_v == "ُ": sc += 1 if (aug or Lsh or Lalif) else -1
            elif pref_v == "َ": sc += 1 if not (aug or Lsh) else -1
            if best is None or sc > best[0]: best = (sc, kk)
        return best[1] if best and best[0] >= 3 else None
    if re.match(r"^لَ[ء-ي]", h) and len(hb) >= 4 and not VERB_BY_LEMMA.get(h):   # لَآمَنَ، لَجَعَلَ: the lām of the oath's answer before the verb
        r_ = verb_key_for(h[2:])
        if r_: return r_
    if re.search(r"َا$", h) and 3 <= len(hb) <= 5 and VERB_BY_LEMMA.get(h[:-1] + "ى"): return VERB_BY_LEMMA[h[:-1] + "ى"][0]   # عَصَاهُ، أَرْضَانَا: the defective māḍī writes its ى as ا before an enclitic
    m = re.search(r"[ّْ](تُ|تَ|تِ|نَا|تُمْ|تُنَّ)$|نَّا$|نَّ$", h)   # a person suffix after a sukūn is the māḍī whatever the first letter (تَعَجَّبْنَا، كُنَّ)
    base = h
    if not m:
        base = hs   # the shadda sits between the vowel and the wāw (اسْتَحَبُّوا): match on the shadda-less form
        m = re.search(r"(ُوا|َتْ|َتِ|َتَا|ْنَ)$", hs) or (re.search(r"ُو$", hs) if len(hb) >= 4 else None) or (re.search(r"َا$", hs) if len(hb) >= 4 and not re.match(r"^[يتأن][َُ]", hs) else None)   # فَعَلُو(هُ): the plural wāw drops its alif before an enclitic
        if m and re.match(r"^[يتن][َُ]", hs): m = None
    if m:
        stem = base[:m.start()] + ("ن" if m.group(0) in ("نَّا", "نَّ") else "")
        s = FOLD(bare(stem))
        return cands(s, None, "ّ" in h[:len(h) - (len(base) - m.start()) + 2] and m.group(0) not in ("نَّا", "نَّ"), bool(re.search(r"^.ا", s)) and len(s) >= 4)
    mp = re.match(r"^([يتأن])([َُ])", hs)
    if mp or re.match(r"^ا[^ً-ٰ]", hs):
        rest = h[2:] if mp else h[1:]
        rest = re.sub(r"(ُونَ|َوْنَ|ِينَ|َانِ|ُوا|َوْا|ْنَ|ِي|َا|ُو)$", "", rest) if re.search(r"(ُونَ|َوْنَ|ِينَ|َانِ|ُوا|َوْا|ْنَ)$", rest) or (re.search(r"(ِي|َا|ُو)$", rest) and len(bare(rest)) >= 4) else rest
        s = FOLD(bare(rest))
        if len(s) >= 2: return cands(s, mp.group(2) if mp else None, "ّ" in rest, bool(re.search(r"^.ا", s)) and len(s) >= 4)
    if re.match(r"^[ء-ي]ِي[ء-ي]َ$", hs) or re.match(r"^[ء-ي]ُ[ء-ي]ِ[ء-ي]َ$", hs):   # the passive māḍī (قِيلَ، كُتِبَ)
        return cands(FOLD(bare(h)), None, "ّ" in h, False)
    if re.match(r"^[اأ]ُ?[ء-ي]ْ?[ء-ي]ُ[ء-ي]ِ[ء-ي]َ$", hs) or re.match(r"^[اأ]ُ?[ء-ي]ْ[ء-ي]ُ[ء-ي]ْ?[ء-ي]ِ[ء-ي]َ$", hs):   # the augmented passive māḍī (افْتُرِضَ، اسْتُخْرِجَ)
        return cands(FOLD(bare(h)), None, "ّ" in h, False)
    if re.match(r"^[أا]ْ", h): return cands(FOLD(bare(h[2:])), None, "ّ" in h, False)   # وَأْمُرْ: the amr whose hamza carries a sukūn
    if re.search(r"[ِْ]$", hs) and not re.match(r"^[يتأن][َُ]", hs) and len(hb) <= 4: return cands(FOLD(bare(h)), None, "ّ" in h, bool(re.search(r"^.ا", FOLD(bare(h)))))   # صَلِّ، قُلْ: the amr of a bare stem
    if re.search(r"َ$", hs) and len(hb) <= 3: return cands(FOLD(bare(h)), None, "ّ" in h, False)   # رُدَّ، مَدَّ: short doubled / hollow forms
    return None
def diptote_like(hb_, lf0=""):
    """may this undetermined noun be a diptote (so that its fatḥa could be jarr)? the elative / أَفْعَل shape, the فَعْلَاء and فُعَلَاء endings, the broken plurals with an alif third (مَسَاجِد، مَفَاتِيح، فَوَاعِل), a lemma ending in alif-hamza"""
    b = hb_.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    if re.search(r"اء$", b) and len(b) >= 4: return True
    if b.startswith("ا") and len(b) == 4: return True
    if len(b) >= 5 and b[2] == "ا" and not b.endswith("ة") and not b.endswith("ات"): return True
    if re.search(r"ان$", b) and len(b) >= 5 and not re.search(r"[اوي]ان$", b): return True   # فَعْلَان (عَطْشَان، سَلْمَان)
    lb = bare(N(lf0 or "")).replace("أ", "ا")
    if lb and (re.search(r"اء$", lb) or (lb.startswith("ا") and len(lb) == 4)): return True
    return False
def gov_before(words, i, span=2):
    """the nearest nāṣib / jāzim of the muḍāriʿ within `span` words before i"""
    for q in range(i - 1, max(-1, i - 1 - span), -1):
        qb = bare(words[q]["w"]).replace("أ", "ا").replace("إ", "ا"); qb = re.sub(r"^[وف]", "", qb) if len(qb) > 2 else qb
        qw = N(words[q]["w"])
        if qb == "لما" and "ّ" not in qw: continue   # لِمَا (li + mā) is no jāzim
        if qb in ("لم", "لما", "لا", "ل"): return "jazm"
        if qb in ("ان", "لن", "كي", "لكي", "حتى", "اذن", "لئلا", "الا"): return "nasb"
    return None
def verb_shape(h2, lem, words, i):
    """tense and mood of a verb the engine read as a noun, from its written shape — the sukūn/waṣl ending is the amr (or the jussive after its governor), the lemma's own form is the māḍī, a يـ/تـ/أـ/نـ prefix is the muḍāriʿ with its mood from the last vowel and the governor"""
    h = N(h2).replace("ّ", ""); hb = bare(h2)
    lemN = N(str(lem).split("(")[0].strip()).replace("ٰ", "") if lem else ""
    lb = noal(bare(lemN)) if lemN else ""
    if not lb: return None, None
    gov = gov_before(words, i)
    pref = bool(re.match(r"^[يتأن][َُ]", h)) and len(hb) >= 3
    def stem_ok(a, b):   # the written stem letters against the lemma's, one weak letter (و ا ي ى) free
        a = a.replace("ى", "ي"); b = b.replace("ى", "ي")
        if a == b: return True
        if len(a) != len(b): return False
        d = [(x, y) for x, y in zip(a, b) if x != y]
        return len(d) == 1 and d[0][0] in "واي" and d[0][1] in "واي"
    lstem = re.sub(r"^[اأإ]", "", lb) if len(lb) >= 4 else lb
    exact = lemN.replace("ّ", "") == h or lemN == N(h2).replace("ٰ", "") or (h.endswith("َا") and lemN.replace("ّ", "") == h[:-1] + "ى")
    if re.match(r"^[ء-ي]ُ[ء-ي]ِ[ء-ي]َ$", h) or re.match(r"^[ء-ي]ِي[ء-ي]َ$", h) or re.match(r"^[اأ]ُ?[ء-ي]ْ?[ء-ي]ُ[ء-ي]ِ[ء-ي]َ$", h) or re.match(r"^[اأ]ُ?[ء-ي]ْ[ء-ي]ُ[ء-ي]ْ?[ء-ي]ِ[ء-ي]َ$", h) or re.match(r"^[ء-ي]ُ[ء-ي]ِّ?[ء-ي]َ$", N(h2).replace("ٰ", "")):   # the passive māḍī (قِيلَ، كُتِبَ، افْتُرِضَ، عُلِّمَ)
        if stem_ok(noal(hb), lb) or (len(lb) >= 4 and lb.startswith("ا") and stem_ok(noal(hb), lb) ) or stem_ok(noal(hb), lb.replace("ى", "ي")): return "mazi", "mazi"
    if re.search(r"ْ$", h) or (re.search(r"ِ$", h) and i + 1 < len(words) and bare(words[i + 1]["w"]).startswith("ال") and noal(hb) == lb):
        if not (stem_ok(noal(hb), lb) or (pref and stem_ok(noal(hb)[1:], lstem))): return None, None
        return ("mudari", "jazm") if (pref and gov == "jazm") else ("amr", "amr")
    m_ = re.search(r"(َتْ|َتِ|ْتُ|ْتَ|ْتِ|ْنَا|ْتُمْ|ْتُنَّ|ُوا)$", h)
    if m_ and not pref:
        stem = h[:m_.start()]; lstem_v = re.sub(r"[َُِ]$", "", lemN.replace("ّ", ""))
        if stem in (lstem_v, lstem_v[:-1] + "ْ" if lstem_v.endswith("ْ") else lstem_v) or stem_ok(noal(bare(stem)), lb) and re.sub(r"[ًٌٍَُِْ]", "", stem)[-1:] == lb[-1:] or stem_ok(noal(bare(stem)), lb[:-1] + "ي"): return "mazi", "mazi"
        return None, None
    if exact and not (pref and gov): return "mazi", "mazi"
    hstem = re.sub(r"(ون|ين|ان|وا|ن)$", "", noal(hb)[1:]) if re.search(r"(ُونَ|َوْنَ|ِينَ|َيْنَ|َانِ|ُوا|َوْا|ْنَ)$", h) else noal(hb)[1:]
    weak_ok = lambda a, b: stem_ok(a, b) or (b[-1:] in "ويى" and a == b[:-1])   # the defective verb drops its last radical before the plural ending (تُنْهَوْنَ ← نَهَى)
    if pref and (weak_ok(hstem, lstem) or (len(lb) <= 3 and weak_ok(hstem, lb))):
        if re.search(r"ُونَ$|َوْنَ$|َانِ$|ِينَ$", h): return "mudari", "raf"
        if re.search(r"(ُوا|ِي|َا)$", h) and len(hb) >= 4: return "mudari", {"jazm": "jazm", "nasb": "nasbVerb"}.get(gov, "nasbVerb")
        if gov == "jazm": return "mudari", "jazm"
        if re.search(r"ُ$", h): return "mudari", "raf"
        if re.search(r"َ$", h): return "mudari", "nasbVerb"
        if re.search(r"[وي]$", hb): return "mudari", ("nasbVerb" if gov == "nasb" else "raf")
        return "mudari", "raf"
    return None, None
def reconcile(rule, cs, wc, words, i, pauses, hn, pre):
    """the written ending wins: an agreeing word keeps its rule in the written case; otherwise the rule is re-read from the clause before the word (kāna's family, inna's family, a verb, a relative/interrogative, an earlier mubtadaʾ, a preposition, an earlier noun in the same written case for ʿaṭf)"""
    is_verb = is_verb_w; is_noun = is_noun_w
    def wc_of(wj, q=None): return wc_word(words, q) if q is not None else None
    prev = words[i - 1] if i else None
    if rule in ("atf", "nat", "badal", "tawkid") and prev is not None and is_noun(prev) and wc_of(prev, i - 1) == wc: return rule, wc
    if rule in ("atf", "nat", "badal", "tawkid") and prev is not None and not is_verb(prev) and not is_noun(prev) and i >= 2 and is_noun(words[i - 2]) and wc_of(words[i - 2], i - 2) == wc: return rule, wc
    nxt = words[i + 1] if i + 1 < len(words) else None
    prevb = bare(words[i - 1]["w"]) if i else ""; prevb0 = re.sub(r"^[وف]", "", prevb) if len(prevb) > 2 else prevb
    prevb0 = prevb0.replace("أ", "ا").replace("إ", "ا")
    verb = kana = inna = man = mubt = False; same = False; ma = False; between = False
    if pre in ("و", "ف"):   # ʿaṭf: an earlier noun in the same written case, across commas but not across a colon / full stop
        for q in range(i - 1, max(-1, i - 13), -1):
            if pauses[q] and not re.search(r"،$", raw_at(words, q)): break
            if is_noun(words[q]) and wc_of(words[q], q) == wc: same = True; break
    if same: return "atf", wc
    j = i - 1
    while j >= 0 and i - j <= 8:
        if pauses[j]: break
        wj = words[j]; bj = bare(wj["w"]); bj0 = re.sub(r"^[وف]", "", bj) if len(bj) > 2 else bj; bj0 = bj0.replace("أ", "ا").replace("إ", "ا")
        if bj0 in KANA_FAM: kana = True; break
        if (bj0 in ("ان", "لكن", "كان", "لعل", "ليت") or re.sub(r"(ه|ها|هم|هن|هما|ك|كم|كما|كن|ي|نا|ني)$", "", re.sub(r"^[لب](?=ان)", "", bj0)) in ("ان", "لكن", "كان", "لعل", "ليت")) and "ّ" in N(wj["w"]): inna = True; break   # (patch 32) لِأَنَّ، إِنَّهُ
        if bj0 in ("ما", "لا"): ma = True; break
        if bj0 in ("من", "الذي", "التي", "الذين", "اذا", "لو", "هل", "كيف", "اين", "لما", "حتى", "لئن", "مهما", "اما"): man = True; break
        if is_verb(wj): verb = True; break
        if wj.get("rule") == "mubtada" and wc == "raf": mubt = True; break   # the nearer mubtadaʾ owns this rafʿ word as its khabar
        if wj.get("rule") == "mubtada": mubt = True
        if is_noun(wj) or wj.get("rule") in ("jarr", "jarrPron"): between = True
        j -= 1
    nak = bool(re.search(r"ً[اى]?$", N(hn).replace("ّ", ""))) and not bare(hn).startswith("ال")
    if wc == "jarr":
        if prevb0 in PREPS: return "jarr", "jarr"
        for q in range(i - 1, max(-1, i - 4), -1):   # an earlier jarr noun that cannot annex further (ال / tanwīn / a pronoun) takes this word as its naʿt or badal
            wq = words[q]
            if is_noun(wq) and wc_of(wq, q) == "jarr":
                hq = host_written(words, q)
                if wq.get("enc") or bare(hq).startswith("ال") or re.search(r"ٍ$", hq.replace("ّ", "")):
                    return ("nat" if (bare(hn).startswith("ال") or re.search(r"ٍ$", N(hn).replace("ّ", ""))) else "badal"), "jarr"
                break
            if q < i - 1 or not (wq.get("rule") == "jarrPron"): break
        return "mudafIlayh", "jarr"
    if wc == "nasb":
        if inna: return "innaIsm", "nasb"
        if kana: return "kanaKhabar", "nasb"
        if nak and (between or not verb): return "hal", "nasb"
        if verb: return ("maful2" if rule == "maful2" else "maful"), "nasb"
        return "maful", "nasb"
    if kana: return "kanaIsm", "raf"
    if inna: return "innaKhabar", "raf"
    if mubt and not verb: return "khabar", "raf"
    if nxt is not None and is_verb(nxt) and bare(nxt["w"]) not in ("تعالى", "سبحانه", "عز", "جل", "صلى", "رضي") and (pre or (i and pauses[i - 1])): return "mubtada", "raf"   # وَالتُّهْمَةُ دَخَلَتْ: the noun before its own verb opens a clause
    if verb: return ("naib" if rule in ("naib", "naibFail") else "fail"), "raf"
    if ma: return "mubtada", "raf"
    if man: return "khabar", "raf"
    return ("khabar" if mubt else "mubtada"), "raf"
def _nd(x): return re.sub(r"[ً-ْٰ]", "", N(str(x or "")))
def name_sila(toks, raw, report):
    """(patch 32) the relative noun is never left without its ṣila: the line names the clause after it and its returning pronoun."""
    n = len(toks)
    lines = [_nd((t.get("irab") or {}).get("ar", "")) for t in toks]
    full = lambda k: toks[k]["surface"]["full"]
    def pause(k): return bool(raw) and k < len(raw) and bool(re.search(r"[،:؛.؟!]$", raw[k]))
    for i in range(n):
        L = lines[i]
        if not re.search(r"اسم موصول|موصول (مبني|في محل)", L) or "صلة" in L or "محكي" in L: continue
        if any("صلة" in lines[j] for j in range(i + 1, min(n, i + 10))): continue
        if i + 1 >= n: continue
        z = i + 1
        while z < n - 1 and not pause(z) and z - i < 8: z += 1
        span = range(i + 1, z + 1)
        aid = any(re.search(r"ضمير متصل|مستتر|ضمير منفصل", lines[k]) for k in span)
        head = lines[i + 1]; X = full(i + 1)
        if "حرف جر" in head or ("مجرور" in head and "فعل" not in head):
            X2 = X + (" " + full(i + 2) if i + 2 < n and "حرف جر" in head and "مجرور" not in head and "مجرور" in lines[i + 2] else "")
            ar_add = f"، وَصِلَتُهُ الْجَارُّ وَالْمَجْرُورُ «{X2}»"; en_add = f"; its relative clause is the prepositional phrase «{X2}»"; tr_add = f"; sılası câr-mecrûr «{X2}»"
        elif "ظرف" in head:
            ar_add = f"، وَصِلَتُهُ الظَّرْفُ «{X}»"; en_add = f"; its relative clause is the adverbial «{X}»"; tr_add = f"; sılası zarf «{X}»"
        elif re.search(r"فعل (ماض|مضارع)", head) or (i + 2 < n and re.search(r"فعل (ماض|مضارع)", lines[i + 2]) and re.search(r"^(لا|لم|لن|ما|قد|س|سوف|لما) ", _nd(X) + " ")):
            ar_add = f"، وَصِلَتُهُ جُمْلَةُ «{X} …» الْفِعْلِيَّةُ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ"; en_add = f"; its relative clause is the verbal clause «{X} …», with no place in the iʿrāb"; tr_add = f"; sılası «{X} …» fiil cümlesidir, i'râbdan mahalli yoktur"
        else:
            ar_add = f"، وَصِلَتُهُ الْجُمْلَةُ بَعْدَهُ «{X} …»"; en_add = f"; its relative clause is the clause after it «{X} …»"; tr_add = f"; sılası sonraki cümledir «{X} …»"
        if aid: ar_add += "، وَالْعَائِدُ الضَّمِيرُ فِيهَا"; en_add += "; the returning pronoun stands inside it"; tr_add += "; âid zamiri içindedir"
        t = toks[i]["irab"]; toks[i]["irab"] = {"ar": t["ar"].rstrip(".") + ar_add + ".", "en": t["en"].rstrip(".") + en_add + ".", "tr": t["tr"].rstrip(".") + tr_add + "."}
        lines[i] = _nd(toks[i]["irab"]["ar"]); report["sila_named"] = report.get("sila_named", 0) + 1

def name_khabar(toks, raw, report):
    """(patch 32) a mubtadaʾ is never left without its khabar: the line points at it — after it (a rafʿ noun, a maṣdar clause,
    a jarr phrase, a verb clause), before it (the fronted jarr phrase / ẕarf) or in the answer of أَمَّا."""
    n = len(toks)
    if not n: return
    lines = [_nd((t.get("irab") or {}).get("ar", "")) for t in toks]
    full = lambda k: toks[k]["surface"]["full"]
    bare_ = lambda k: re.sub(r"^[وف]", "", toks[k]["surface"]["bare"]) if toks[k]["surface"]["bare"] not in ("و", "ف") else toks[k]["surface"]["bare"]
    def stop(k, at=None):
        if not raw or k >= len(raw): return False
        p = re.search(r"([،:؛.؟!]+)$", raw[k])
        if not p: return False
        if k == at and ":" in p.group(1): return False      # فَأَوَّلُهَا: الْإِيمَانُ — the colon introduces the khabar
        return bool(re.search(r"[:؛.؟!]", p.group(1)))
    MUBT = re.compile(r"^(?:[^.]{0,40}، )?«?[^.]{0,12}»?\s*مبتدأ")
    PRAISE = ("تعالى", "سبحانه", "عز", "جل", "صلى", "وسلم", "رضي")
    jarrish = lambda k: ("حرف جر" in lines[k] or "مجرور" in lines[k]) and "فعل" not in lines[k]
    zarfish = lambda k: "ظرف" in lines[k]
    tail_ = lambda k: re.match(r"^(?:(?:الواو|الفاء) عاطفة، و)?(?:«[^»]*» )?(مضاف إليه|نعت|بدل|توكيد|معطوف مرفوع|صفة)", lines[k]) and not MUBT.match(lines[k])
    DUA = ("السلام", "الصلاة", "الرحمة", "اللعنة", "الرضوان", "رضوان", "رحمة", "سلام", "صلاة")
    dua_ = lambda k: k > 0 and bare_(k) in DUA and toks[k - 1]["surface"]["bare"].startswith("علي")
    def relabel(kk):
        t = toks[kk]["irab"]; toks[kk]["irab"] = {"ar": t["ar"].replace("مُبْتَدَأٌ", "خَبَرٌ", 1), "en": t["en"].replace("The mubtada (subject of the nominal sentence)", "The khabar (predicate)"), "tr": t["tr"].replace("Mübtedâ", "Haber")}
        lines[kk] = _nd(toks[kk]["irab"]["ar"]); report["khabar_named"] = report.get("khabar_named", 0) + 1
    for i in range(n):
        L = lines[i]
        if not MUBT.match(L) or "خبر" in L: continue
        a = i
        while a > 0 and not stop(a - 1): a -= 1
        z = i
        while z < n - 1 and not stop(z, at=i): z += 1
        z2 = next((k for k in range(i, z + 1) if raw and k < len(raw) and raw[k].endswith("،")), z)   # the khabar stands before the first comma
        if any("خبر" in lines[k] for k in range(a, z2 + 1) if k != i): continue
        pref_ = L.startswith(("الواو", "الفاء"))
        colon_prev = raw is not None and i > 0 and i - 1 < len(raw) and raw[i - 1].endswith(":")
        pv = i - 1
        while pv > a and (re.match(r"^(?:(?:الواو|الفاء) عاطفة، و)?توكيد", lines[pv]) or tail_(pv)): pv -= 1
        # the khabar of إِنَّ: لِأَنَّ الرَّعْدَ وَالسَّحَابَ سَبَبُ الْمَطَرِ
        if not pref_ and any(re.search(r"اسم (إن|أن|لكن|كأن|لعل|ليت)", lines[k]) for k in range(a, i)) and not any("خبر" in lines[k] for k in range(a, i)):
            t = toks[i]["irab"]; toks[i]["irab"] = {"ar": t["ar"].replace("مُبْتَدَأٌ", "خَبَرُ إِنَّ", 1), "en": t["en"].replace("The mubtada (subject of the nominal sentence)", "The predicate of inna"), "tr": t["tr"].replace("Mübtedâ", "İnne'nin haberi")}
            lines[i] = _nd(toks[i]["irab"]["ar"]); report["khabar_named"] = report.get("khabar_named", 0) + 1; continue
        # the second khabar: فَهُوَ مُتَمَنٍّ مُتَحَسِّرٌ
        if not pref_ and i > 0 and "خبر" in lines[i - 1] and "خبر إن" not in lines[i - 1] and re.search(r"[ًٌٍ]", N(full(i))) and (i - 1 >= a or colon_prev):
            t = toks[i]["irab"]; toks[i]["irab"] = {"ar": t["ar"].replace("مُبْتَدَأٌ", "خَبَرٌ ثَانٍ", 1), "en": t["en"].replace("The mubtada (subject of the nominal sentence)", "A second khabar"), "tr": t["tr"].replace("Mübtedâ", "İkinci haber")}
            lines[i] = _nd(toks[i]["irab"]["ar"]); report["khabar_named"] = report.get("khabar_named", 0) + 1; continue
        # the rafʿ nominal / detached pronoun right before it is the mubtadaʾ: وَصِفَاتُهُ كُلُّهَا خِلَافُ، وَهِيَ: الْحَيَاةُ، وَرِضَاهُ ثَوَابُهُ
        if not pref_ and i > 0 and (pv >= a or colon_prev) and (re.match(r"^(?:(?:الواو|الفاء) عاطفة، و)?(?:«[^»]*» )?(معطوف مرفوع|مبتدأ|بدل مرفوع)", lines[pv]) or ("ضمير منفصل" in lines[pv] and "رفع" in lines[pv])) and not re.search(r"فعل (ماض|مضارع)", lines[pv]):
            relabel(i); continue
        ar0 = (toks[i].get("irab") or {}).get("ar", ""); en0 = (toks[i].get("irab") or {}).get("en", ""); tr0 = (toks[i].get("irab") or {}).get("tr", "")
        def put(ar_add, en_add, tr_add, muakhkhar=False):
            ar = ar0.rstrip(".")
            if muakhkhar and "مُؤَخَّرٌ" not in ar: ar = ar.replace("مُبْتَدَأٌ", "مُبْتَدَأٌ مُؤَخَّرٌ", 1)
            toks[i]["irab"] = {"ar": ar + ar_add + ".", "en": en0.rstrip(".") + en_add + ".", "tr": tr0.rstrip(".") + tr_add + "."}
            lines[i] = _nd(toks[i]["irab"]["ar"])
            report["khabar_named"] = report.get("khabar_named", 0) + 1
        # (b) the fronted khabar: only a jarr phrase / ẕarf stands before the mubtadaʾ in its clause (عَلَيْهِ السَّلَامُ، فِيهِ أَرْبَعَةُ)
        if dua_(i): put(f"، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ الْمُتَقَدِّمُ «{full(i - 1)}» — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ", f"; its khabar is the fronted phrase «{full(i - 1)}» — a parenthetical prayer", f"; haberi öne alınmış «{full(i - 1)}» — mu'teriza duâ cümlesi", True); continue
        if bare_(i) in ("قوله", "قول", "قولهم", "قولها") and i + 1 <= z and bare_(i + 1) in ("تعالى", "سبحانه") and all(bare_(k) in PRAISE for k in range(i + 1, z + 1)):
            put("، وَخَبَرُهُ الْكَلَامُ الْمَحْكِيُّ بَعْدَهُ", "; its khabar is the quoted words that follow", "; haberi sonraki nakledilen sözdür"); continue
        if i > 0 and i - 1 >= a and ("ظرف" in lines[i - 1] or "استفهام" in lines[i - 1]) and not re.search(r"فعل (ماض|مضارع)", lines[i - 1]) and not lines[i - 1].startswith(("الواو", "الفاء")):
            put(f"، وَخَبَرُهُ الظَّرْفُ الْمُتَقَدِّمُ «{full(i - 1)}»", f"; its khabar is the fronted adverbial «{full(i - 1)}»", f"; haberi öne alınmış zarf «{full(i - 1)}»", True); continue
        if i > 0 and i - 1 >= a and jarrish(i - 1) and re.fullmatch(r"[وف]?(في|ل|له|لها|لهم|لهن|لهما|عليه|عليها|عليهم|عليك|عليكم|منه|منها|منهم|منكم|عنده|عندها|عندهم|لدينا|لديه|معه|معها|معهم|بينهم|فيه|فيها|فيهم|لنا|لكم|لي|لك|به|بها|بهم|عنه|عنها|عنهم|اليه|إليه|اليها|إليها)", toks[i - 1]["surface"]["bare"]):
            put(f"، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ الْمُتَقَدِّمُ «{full(i - 1)}»", f"; its khabar is the fronted prepositional phrase «{full(i - 1)}»", f"; haberi öne alınmış câr-mecrûr «{full(i - 1)}»", True); continue
        pre_ = [k for k in range(a, i) if bare_(k) not in ("اما", "أما", "انما", "إنما", "قد", "و", "ف", "ثم", "بل", "لكن", "لٰكن", "هل", "أ", "ا", "ثم")]
        if pre_ and all(jarrish(k) or zarfish(k) for k in pre_):
            X = " ".join(full(k) for k in pre_)
            if all(zarfish(k) for k in pre_): put(f"، وَخَبَرُهُ الظَّرْفُ الْمُتَقَدِّمُ «{X}»", f"; its khabar is the fronted adverbial «{X}»", f"; haberi öne alınmış zarf «{X}»", True)
            else: put(f"، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ الْمُتَقَدِّمُ «{X}»", f"; its khabar is the fronted prepositional phrase «{X}»", f"; haberi öne alınmış câr-mecrûr «{X}»", True)
            continue
        # the end of the mubtadaʾ phrase: its muḍāf ilayh, naʿt, badal, tawkīd, joined rafʿ nouns
        j = i + 1
        while j <= z and tail_(j): j += 1
        mawsul = j <= z and ("اسم موصول" in lines[j] or "موصول" in lines[j])
        amma = any(bare_(k) in ("اما", "أما") for k in range(a, i))
        fa_ = next((k for k in range(j, z + 1) if toks[k]["surface"]["bare"].startswith("ف") and lines[k].startswith("الفاء")), None)
        if amma and (j > z or mawsul):
            if fa_ is not None: put(f"، وَخَبَرُهُ الْجُمْلَةُ الْوَاقِعَةُ بَعْدَ فَاءِ «أَمَّا»: «{full(fa_)} …»", "; its khabar is the clause after the fāʾ of ammā", "; haberi emmâ'nın fâ'sından sonraki cümledir")
            else: put("، وَخَبَرُهُ جُمْلَةُ جَوَابِ «أَمَّا» الَّتِي تَلِي الْفَاءَ", "; its khabar is the answer-clause of ammā that follows the fāʾ", "; haberi emmâ'nın fâ'dan sonra gelen cevap cümlesidir")
            continue
        if mawsul:
            kk = next((k for k in range(j + 1, z + 1) if MUBT.match(lines[k]) and not lines[k].startswith(("الواو", "الفاء"))), None)
            if kk is not None: relabel(kk); continue
            kc = next((k for k in range(j + 1, z + 1) if jarrish(k) and toks[k]["surface"]["bare"].startswith("ك")), None)
            if kc is not None: put(f"، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ «{full(kc)}»", f"; its khabar is the prepositional phrase «{full(kc)}»", f"; haberi câr-mecrûr «{full(kc)}»"); continue
            put("، وَخَبَرُهُ مَا بَعْدَ تَمَامِ الصِّلَةِ", "; its khabar comes after the relative clause is complete", "; haberi sıla tamamlandıktan sonra gelir"); continue
        if j > z:
            report.setdefault("khabar_open", []).append((full(i), " ".join(full(k) for k in range(a, z + 1))[:90])); continue
        kk = None
        for k in range(j, z2 + 1):
            if re.search(r"فعل (ماض|مضارع|أمر)", lines[k]) and "اسم فعل" not in lines[k] and bare_(k) not in PRAISE: break
            if dua_(k) or (k > 0 and dua_(k - 1) and lines[k].startswith("الواو")): continue
            if MUBT.match(lines[k]) and not lines[k].startswith(("الواو", "الفاء")): kk = k; break
        if kk is not None: relabel(kk); continue
        Lj = lines[j]; bj = toks[j]["surface"]["bare"]
        # (d) the rafʿ noun right after the phrase, with no joining letter: إِحْدَاهَا الشَّرِيعَةُ، قَلْبُ الْمُؤْمِنِ عَرْشُ اللهِ
        # (e) the maṣdar clause: الْإِيمَانُ أَنْ تُؤْمِنَ
        if re.match(r"^(?:[وف]َ)?أَن[َّْ]", N(full(j))) or "مصدرية" in Lj:
            put(f"، وَخَبَرُهُ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «{full(j)}» وَمَا بَعْدَهَا", f"; its khabar is the maṣdar clause opened by «{full(j)}»", f"; haberi «{full(j)}» ile başlayan masdar-ı müevveldir"); continue
        # (f) the verb clause: فَاللهُ تَعَالَى عَفَا عَنْهُ
        jv = j
        while jv <= z2 and (bare_(jv) in PRAISE or bare_(jv) in ("لم", "لا", "ما", "لن", "قد", "لما", "سوف", "س", "ليس", "لمّا")): jv += 1
        if jv <= z2 and re.search(r"فعل (ماض|مضارع|أمر)", lines[jv]) and "اسم فعل" not in lines[jv]:
            put(f"، وَجُمْلَةُ «{full(jv)}» الْفِعْلِيَّةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", f"; the verbal clause «{full(jv)}» stands in the place of rafʿ as its khabar", f"; «{full(jv)}» fiil cümlesi ref mahallinde haberidir"); continue
        # (g) the jarr phrase / ẕarf after it: الْحَمْدُ لِلّٰهِ، عَشَرَةٌ مِنْهَا فِي الشَّرِيعَةِ
        cands = [k for k in range(j, z2 + 1) if (jarrish(k) and not (k > j and jarrish(k - 1) and "حرف جر" in lines[k - 1] and "مجرور" in lines[k] and "حرف جر" not in lines[k])) or zarfish(k)]
        if len(cands) >= 2 and re.fullmatch(r"من(ها|هم|هن|كم|نا|ه|ك|ي)", toks[cands[0]]["surface"]["bare"]): cands = cands[1:]
        if len(cands) == 1:
            k = cands[0]; X = full(k) + (" " + full(k + 1) if "حرف جر" in lines[k] and "مجرور" not in lines[k] and k + 1 <= z and "مجرور" in lines[k + 1] else "")
            if zarfish(k): put(f"، وَخَبَرُهُ الظَّرْفُ «{X}»", f"; its khabar is the adverbial «{X}»", f"; haberi zarf «{X}»")
            else: put(f"، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ «{X}»", f"; its khabar is the prepositional phrase «{X}»", f"; haberi câr-mecrûr «{X}»")
            continue
        if len(cands) >= 2:
            put("، وَخَبَرُهُ جَارٌّ وَمَجْرُورٌ مِمَّا بَعْدَهُ", "; its khabar is one of the prepositional phrases that follow", "; haberi sonraki câr-mecrûrlardan biridir"); continue   # (no «مُتَعَلِّقٌ بِـ»: the TaalluqEngine grades that wording on jarr tokens only)
        report.setdefault("khabar_open", []).append((full(i), " ".join(full(k) for k in range(a, z + 1))[:90]))

def raw_at(words, q):
    """the raw source token of word q (set per sentence by the caller)"""
    return RAW.get(id(words), [""] * len(words))[q] if q < len(RAW.get(id(words), [])) else ""
RAW = {}

DIDACTIC = {"on": False}   # set from the meta flag cellLines (a ṣarf matn)

def person_of(h2, hb2, tense, rule, words, i):
    """The hidden doer by the verb's own shape, then by the nearest cue in the sentence: ـَتْ is «she»; the interrogative
    hamza before تَفْعَلُ is «you»; أَ «I», نَـ «we» (behind سَـ too); تَـ is «she» after a feminine subject or هِيَ/إِنَّهَا,
    «you» after أَنْتَ/ـكَ/ـتَ, the nearest cue winning; a feminine subject right after the verb (تَكُونُ شَرَائِطُهُ) is «she»."""
    h2s = re.sub(r"^سَ", "", h2); hb2s = bare(h2s)
    if tense == "mazi" or rule == "mazi":
        return "هِيَ" if re.search(r"َتْ$", h2) else "هُوَ"
    if tense == "amr" or rule == "amr": return "أَنْتَ"
    if re.match(r"^ل[َِ][يتنأ]", N(h2s)) and len(hb2s) >= 5: h2s = N(h2s)[2:]; hb2s = bare(h2s)   # لِتَفْصِلَ، لَتَفْعَلَنَّ: the lām of purpose / of the oath stands before the prefix
    if re.match(r"^أَت[َُ](?!ّ)", h2s) and len(hb2s) >= 4: return "أَنْتَ"
    if hb2s.startswith("أ"): return "أَنَا"
    if hb2s.startswith("ن"): return "نَحْنُ"
    if not hb2s.startswith("ت"): return "هُوَ"
    if DIDACTIC["on"]:   # a ṣarf matn: its letters are the subjects — «تُحْذَفُ، تُقْلَبُ، تَثْبُتُ، تَسْقُطُ» speak of the wāw, the yāʾ, the nūn (she); the reader is addressed by what he DOES (تَقُولُ، تَضُمُّ، تُدْخِلُ)
        pb_ = bare(words[i - 1]["w"]) if i > 0 else ""
        addressed_ = bool(re.search(r"^[وف]?(انت|انك)$", pb_))
        hn_ = N(h2s)
        passive_ = bool(re.match(r"^تُ", hn_)) and bool(re.search(r"َا?[ء-ي]ّ?[َُِْ]?$|َّ?[ىا]$", hn_))
        state_ = bool(re.match(r"^تَ", hn_)) and re.sub(r"^[وف]", "", hb2s) in ("تثبت", "تسقط", "تسلم", "تكون", "تعود", "تنقلب", "تصير", "تبقى", "تقع")
        if (passive_ or state_) and not addressed_: return "هِيَ"
        if re.sub(r"^[وف]", "", hb2s) == "تقول" and re.search(r"تَقُولُ$", hn_): return "أَنْتَ"   # «فَتَقُولُ»: the author hands the reader the form to say
    def fem(x):
        xb = re.sub(r"(هم|هما|هن|ها|ه|كم|كما|كن|ك|نا|ني)$", "", bare(x["w"])) if x.get("enc") else bare(x["w"])
        return bool(re.search(r"(ة|ات)$", xb)) and x.get("rule") in ("mubtada", "fail", "kanaIsm", "innaIsm", "naib")
    for x in reversed(words[:i]):
        xb = bare(x["w"]); xw = N(x["w"]); xb2 = re.sub(r"^[وف]", "", xb) if len(xb) > 2 else xb
        if xb2 in ("انت", "انك", "لكنك", "لعلك", "كانك", "لانك", "يا", "ايها") or re.search(r"ْتَ$", xw) or (re.search(r"كَ$", xw) and xb2 not in ("ذلك", "تلك", "ذاك", "كذلك", "هناك")): return "أَنْتَ"
        if xb2 in ("هي", "انها", "لانها", "لكنها", "كانها", "لعلها", "هذه", "تلك", "التي") or fem(x) or re.search(r"َتْ$", xw): return "هِيَ"
    for x in words[i + 1:i + 3]:
        if fem(x): return "هِيَ"
    return "أَنْتَ"

def noal(x):
    """strip a LEADING article only (the ا-ل inside عَالَم is no article)"""
    return re.sub(r"^ال", "", x)

def shape(w, case, enc, pos, pre_jarr):
    """the written shape of a noun host, for its sign"""
    h = N(w); b = bare(h)
    if re.match(r"^[لأ]َ[ء-ي]", h) and len(b) >= 6 and re.search(r"(ُّ?ونَ?|ِّ?ينَ?|َانِ|َيْنِ)$", h) and not b.startswith("لل"): h = h[2:]; b = b[1:]
    if enc in ("ي", "ني") and pos != "verb": return "ya-mutakallim"
    if re.search(r"(?:[ء-ي])َ[ً-ٰ]*ا[ً-ٰ]*نِ?$", h) and not re.search(r"ان[ً-ٰ]*ٌ", h) and len(b) >= 5 and case == "raf" and re.search(r"َان", h): return "muthanna"   # ثَوْبَانُ (a name, ḍamma on the nūn) is no dual
    if re.search(r"َّ?يْن[ً-ٰ]*ِ?$", h) and len(b) >= 4: return "muthanna"
    if b in ("ابو", "اخو", "حمو", "فو", "ذو", "أبو", "أخو") or b in ("ابا", "اخا", "ذا", "أبا", "أخا") or b in ("ابي", "اخي", "ذي", "أبي", "أخي"): return "khamsa"
    if b in ("كلا", "كلتا", "كلي", "كلتي") and enc: return "muthanna"
    if b in ("بنو", "بني") and case in ("raf", "nasb", "jarr"): return "jam-m"
    stem3 = len(re.sub(r"^(ال|لل)", "", b)) - 2 >= 3   # الدِّينِ، الْجَنِينِ: one or two letters before ـين make no plural
    if re.search(r"ُّ?ونَ?$", h) and len(b) >= 5 and case == "raf" and stem3: return "jam-m"
    if re.search(r"ِّ?ينَ?$", h) and len(b) >= 5 and case in ("nasb", "jarr") and stem3: return "jam-m"
    if re.search(r"َيْ$", h) and len(b) >= 3 and case in ("nasb", "jarr") and enc == "": return "muthanna"
    if re.search(r"َات[ً-ٰ]*$", h) and len(b) >= 4: return "jam-f"
    if re.search(r"[َ]?[اى]$", b) and not re.search(r"[ًٌٍَُِ]$", h) and len(b) >= 3 and case and b[-1] in "اى" and not b.startswith("ال") and re.search(r"[َ][اى]$|ى$", h): return "maqsur"
    if re.search(r"ِي$", h) and len(b) >= 3 and case in ("raf", "jarr") and not enc: return "manqus"
    if b in ("ابو", "اخو", "حمو", "فو", "ذو", "أبو", "أخو") or b in ("ابا", "اخا", "ذا", "أبا", "أخا") or b in ("ابي", "اخي", "ذي", "أبي", "أخي"): return "khamsa"
    if case == "jarr" and re.search(r"َ$", h) and not b.startswith("ال") and not pre_jarr == "al" and not re.search(r"[ًٌٍ]", h): return "mamnu"
    return "sahih"

OWNER_G, OWNER_M = {}, {}
def load_global():
    G, M = {}, {}
    for f in sorted(glob.glob(str(ROOT / "content/samples/*/glossary.json"))):
        for k, e in json.load(open(f, encoding="utf-8")).get("entries", {}).items():
            if k not in G: G[k] = e; OWNER_G[k] = Path(f).parent.name
    for f in sorted(glob.glob(str(ROOT / "content/samples/*/morphology.json"))):
        for k, e in json.load(open(f, encoding="utf-8")).get("verbs", {}).items():
            if k not in M: M[k] = e; OWNER_M[k] = Path(f).parent.name
    return G, M

def grammar_ids():
    return {p.stem for p in (ROOT / "content/grammar").glob("*.json")}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("engine"); ap.add_argument("meta"); ap.add_argument("out"); ap.add_argument("--morph", default=None)
    ap.add_argument("--lex", default=None); ap.add_argument("--trans", default=None); ap.add_argument("--fixes", default=None)
    a = ap.parse_args()
    E = json.load(open(a.engine, encoding="utf-8")); meta = json.load(open(a.meta, encoding="utf-8"))
    DIDACTIC["on"] = bool(meta.get("cellLines"))
    LX = json.load(open(a.lex, encoding="utf-8")) if a.lex and os.path.exists(a.lex) else {}
    TR = json.load(open(a.trans, encoding="utf-8")) if a.trans and os.path.exists(a.trans) else {}
    FX = json.load(open(a.fixes, encoding="utf-8")) if a.fixes and os.path.exists(a.fixes) else {}
    G, M = load_global()
    global LXF_, VERB_BY_LEMMA, VERB_BY_STEM
    LXF_ = {k.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ٱ", "ا"): v for k, v in LX.items()}
    VERB_BY_LEMMA = {}; VERB_BY_STEM = {}
    for kk, ee in list(G.items()) + [(v.get("key"), v) for v in LX.values()]:
        if ee.get("pos") == "verb" and ee.get("lemma") and kk:
            lm_ = N(str(ee["lemma"]).split("(")[0].strip()).replace("ٰ", "")
            VERB_BY_LEMMA.setdefault(lm_, (kk, ee)); VERB_BY_STEM.setdefault(re.sub(r"[ًٌٍَُِْ]$", "", lm_.replace("ّ", "")), (kk, ee))
    MX = set()
    if a.morph:
        for k, e in json.load(open(a.morph, encoding='utf-8'))['verbs'].items(): M[k] = e; MX.add(k)
    GIDS = grammar_ids()
    out = Path(a.out); (out / "chapters").mkdir(parents=True, exist_ok=True)
    used = {}; morph = {}; report = {"nokey": [], "mismatch": [], "undecided": [], "fixed": 0, "reconciled": 0, "promoted": 0, "rekeyed": 0}
    def take(key, where):
        if key in G: used.setdefault(key, G[key]); return True
        for b, e in LX.items():
            if e.get("key") == key: used.setdefault(key, {k: v for k, v in e.items() if k not in ("key", "cite")}); return True
        report["nokey"].append((where, key)); return False
    CITE = set()   # (wave 165) tokens whose lexicon row is a QUOTED PATTERN-WORD (فَعَلَ، يَفْعُلُ، اِفْعَنْلَلَ …): keyed by the author, never re-keyed, and given the quoted-word line
    def hit(row, where):
        if row.get("cite") and FX.get(where, {}).get("cite") is not False: CITE.add(where)
        return row["key"]
    def key_for(w, enc, where):
        """the lex key of a written word: fixes → global lexicon via the engine → lex_extra by bare host (with or without a وَ/فَ prefix)"""
        cands = []
        for base in ([N(host_of(w, enc)), N(w)] if enc else [N(w)]):
            variants = [base]
            if re.search(r"\u064b\u0627$|\u0627\u064b$", base): variants.append(re.sub(r"\u064b\u0627$|\u0627\u064b$", "", base))   # the tanwīn alif
            for h in variants:
                b = bare(h); b2 = b[1:] if pre_of(h) else None
                cands += [b] + ([b2] if b2 else [])
                for x, hx in ((b, h), (b2, h[2:] if b2 else None)):
                    if x and hx and re.match(r"^[بل]\u0650|^ك\u064e", hx) and len(x) >= 4: cands.append(x[1:])
        b2 = bare(N(w))[1:] if pre_of(N(w)) else None
        FOLD = lambda x: x.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ٱ", "ا")
        LXF = {FOLD(k): v for k, v in LX.items()}
        # (wave 165) a lexicon key may be VOCALISED — «فَعِل» and «فَعُل» are two measures on the same letters; the ending's own vowel is dropped
        def VS(h):   # the ending's own marks off; a final shadda stays (NFC puts the vowel BEFORE the shadda)
            h = re.sub(r"\u064b(\u0651?)\u0627$|\u0627\u064b$", lambda m_: m_.group(1) or "", N(h)); m = re.search(r"[\u064b-\u0652]*$", h)
            return h[:m.start()] + ("\u0651" if "\u0651" in m.group(0) else "")
        LXV = {VS(k): v for k, v in LX.items() if DIA.search(k)}
        if LXV:
            for base in ([N(host_of(w, enc)), N(w)] if enc else [N(w)]):
                v0 = VS(base); v1 = re.sub(r"^[وف]\u064e", "", v0) if pre_of(base) else v0
                for v, stripped in ((v0, False), (v1, v1 != v0), (re.sub(r"^(?:[بل]\u0650|ك\u064e)", "", v0), False), (re.sub(r"^(?:[بل]\u0650|ك\u064e)", "", v1), v1 != v0)):
                    if v in LXV: return hit(LXV[v], where), stripped
        for cand in cands:
            if cand in LX: return hit(LX[cand], where), (cand == b2)
            if FOLD(cand) in LXF: return hit(LXF[FOLD(cand)], where), (cand == b2)
        return None, bool(b2)
    chapters_out = []
    for ch in E["chapters"]:
        sents = []
        for si, s in enumerate(ch["sentences"], start=1):
            sid = f"s{si}"; where0 = f"{ch['n']}:{sid}"
            words = s["words"]; toks = []
            src_words = [re.sub(r"[،:؛.؟!«»\"()]", "", x) for x in s["text"].split() if re.sub(r"[،:؛.؟!«»\"()]", "", x)]
            aligned = len(src_words) == len(words)
            raw_toks = [x for x in s["text"].split() if re.sub(r"[،:؛.؟!«»\"()]", "", x)]
            pauses = [bool(re.search(r"[،:؛.؟!]$", x)) for x in raw_toks] if aligned else [False] * len(words)
            RAW[id(words)] = raw_toks if aligned else [""] * len(words)
            if not aligned: report.setdefault("misaligned", []).append((where0, len(src_words), len(words)))
            doers = {w["head"] for w in words if w.get("rule") in ("fail", "naib") and isinstance(w.get("head"), int)}
            for i, w in enumerate(words):
                where = f"{where0}:{i}"; fx = FX.get(where, {})
                full = N(src_words[i]) if aligned else N(w["w"]); rule = fx.get("rule", w.get("rule")); k = fx.get("k", w.get("k")); enc = w.get("enc") or ""
                kind = w.get("kind") or ""; pos = w.get("pos") or ""
                if aligned and w.get("out") and bare(w["out"]) == bare(full) and N(w["out"]) != full and k not in ("keep", "cell", None): report["mismatch"].append((where, full, w["out"], rule))
                if rule in (None, "", "fail") and k is None: report["undecided"].append((where, full))
                b = bare(full); pre = pre_of(full); bh = bare(host_of(full, enc)); core = bh[1:] if pre else bh
                # ---- the lex key
                k2, is_pre2 = key_for(full, enc, where)
                key = fx.get("key") or k2 or w.get("key"); is_pre = bool(pre)
                if key and pos == "propn" and (G.get(key) or {}).get("pos") == "noun": pos = "noun"
                if fx.get("pos") == "verb": kind = "verb"
                if fx.get("pos") == "noun": kind = "noun"; k = fx.get("k", None if k in ("cell", "keep") else k); rule = fx.get("rule", rule if rule in ROLE else None)
                prevb_ = bare(words[i - 1]["w"]) if i else ""; prevb_ = re.sub(r"^[وف]", "", prevb_) if len(prevb_) > 2 else prevb_
                if prevb_ in JAZM_GOV and re.match(r"^[يتأن]", core) and len(core) >= 3 and not fx.get("pos"):
                    kind = "verb"; k = "cell"; rule = "jazm" if prevb_ in ("لم", "لما") else "nasbVerb"
                    w = dict(w); w["cell"] = dict(w.get("cell") or {}); w["cell"]["tense"] = "mudari"
                if fx.get("enc") is not None: enc = fx["enc"]
                if key and pre and key in G and noal(bare(str(G[key].get("lemma", "")).split("(")[0].strip())) == noal(bh): is_pre = False   # the lexicon owns the whole word (وَلَد، فَقِير)
                if pre and key and not fx.get("pre"):
                    le0_ = G.get(key) or next((v for v in LX.values() if v.get("key") == key and v.get("lemma")), None)
                    lb0_ = noal(bare(str((le0_ or {}).get("lemma", "")).split("(")[0].strip())) if le0_ else ""
                    fb_ = noal(bh); rb_ = noal(bh[1:])
                    rb0_ = bh[1:].replace("أ", "ا").replace("إ", "ا").replace("ٰ", "")
                    if lb0_ and lb0_[0] == bh[0] and (fb_ == lb0_ or (fb_.startswith(lb0_) and len(fb_) - len(lb0_) <= 3) or (lb0_.endswith("ة") and fb_.startswith(lb0_[:-1]) and len(fb_) - len(lb0_) <= 3)) and not (rb_ == lb0_ or rb_.startswith(lb0_)) and (rb0_ not in PART or bh[1:2] == "ا") and rb0_ not in PRON and rb0_ not in DEM and rb0_ not in EXTRA_PART and not KANA_RE.match(rb0_):
                        pre = ""; is_pre = False; core = bh   # وَارِدُونَ، فَضِيلَتَانِ، وَلَدٌ: the lemma begins with that letter — no prefix
                segs = []; punct = None
                # ---- particles / pronouns / demonstratives (mabnī)
                pb = core.replace("أ", "ا").replace("إ", "ا") if core else b
                wajh = fx.get("wajh") or w.get("wajh") or ""
                sh0 = "ّ" in N(full)
                if pb == "لكن" and not sh0 and not enc and "لكن-sakina" in PART: pb = "لكن-sakina"
                if pb == "بان" and enc and sh0:   # بِأَنَّهُ، بِأَنَّهُمْ: the jarr letter, أَنَّ and its pronoun noun
                    ar0 = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + f"الْبَاءُ حَرْفُ جَرٍّ، وَ«أَنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، وَ{ENC_AR.get(enc, 'الضَّمِيرُ')} ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِالْبَاءِ."
                    en0 = "the bāʾ (a jarr letter) + «anna» (the emphasising particle) + its attached pronoun as its noun; the clause stands in the seat of jarr."; tr0 = "bâ (harf-i cer) + «enne» (tekid harfi) + ismi olan bitişik zamir; masdar-ı müevvel cer mahallinde."
                    if pre: take("wa" if pre == "و" else "fa", where)
                    take("bi", where); take("anna", where); take(ENC.get(enc, "?"), where)
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": "anna", "pos": "part", "grammar": [t for t in ["huruf-jarr", "inna-wa-akhawatuha"] if t in GIDS], "irab": {"ar": ar0, "en": en0, "tr": tr0}, "segments": ([{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}] if pre else []) + [{"form": "بِ", "lex": "bi", "pos": "prep"}, {"form": "أَنَّ", "lex": "anna", "pos": "part"}, {"form": full[len(N(host_of(full, enc))):], "lex": ENC.get(enc, "?"), "pos": "pron"}]})
                    continue
                if pb == "بان" and not enc:   # بِأَنَّ / بِأَنْ: the jarr letter and the particle it governs, by the shadda
                    if sh0: ar0, en0, tr0, lx, tg = ("الْبَاءُ حَرْفُ جَرٍّ، وَ«أَنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمَعْمُولَيْهَا فِي مَحَلِّ جَرٍّ بِالْبَاءِ.", "«that» after the ba of jarr: anna, a sister of inna; the clause it opens stands as a verbal noun in the place of jarr.", "cer bâ'sı + «enne» (inne'nin kardeşi): açtığı cümle masdar-ı müevvel olarak mahallen mecrûr.", ("anna" if "anna" in G else "inna"), "inna-wa-akhawatuha")
                    else: ar0, en0, tr0, lx, tg = ("الْبَاءُ حَرْفُ جَرٍّ، وَ«أَنْ» حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِالْبَاءِ.", "«to» after the ba of jarr: an, the verbal-noun particle that puts the verb in nasb; the clause stands in the place of jarr.", "cer bâ'sı + masdariyye «en»: fiili nasb eder, cümle mahallen mecrûr.", "an-masdariyya", "nawasib-wa-jawazim-al-mudari")
                    ar0 = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + ar0
                    if pre: take("wa" if pre == "و" else "fa", where)
                    take("bi", where); take(lx, where)
                    hpart = full[2:] if pre else full
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": lx, "pos": "part", "grammar": [t for t in ["huruf-jarr", tg] if t in GIDS], "irab": {"ar": ar0, "en": en0, "tr": tr0}, "segments": ([{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}] if pre else []) + [{"form": hpart[:2], "lex": "bi", "pos": "prep"}, {"form": hpart[2:], "lex": lx, "pos": "part"}]})
                    continue
                FACE_LA = {"jawab": ("«لَا» حَرْفُ جَوَابٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ.", "«no» — the answer particle, standing for the whole denied clause.", "«hayır» — cevap harfi, nefyedilen cümlenin yerine geçer.", "la-nafiya"), "nafiya": ("«لَا» حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«not» — the negation.", "«değil / -mez» — nefiy harfi.", "la-nafiya"),
                           "nahiya": ("«لَا» النَّاهِيَةُ: حَرْفُ نَهْيٍ وَجَزْمٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«do not» — the prohibitive la, it puts the verb in jazm.", "«-me» — nehiy lâ'sı, fiili cezmeder.", "la-nahiya"),
                           "jins": ("«لَا» النَّافِيَةُ لِلْجِنْسِ، تَعْمَلُ عَمَلَ إِنَّ، مَبْنِيَّةٌ عَلَى السُّكُونِ.", "«no …» — the la of absolute negation, it works like inna.", "cinsini nefyeden «lâ» — inne gibi amel eder.", "la-nafiya-lil-jins"),
                           "atifa": ("«لَا» حَرْفُ عَطْفٍ مَبْنِيٌّ عَلَى السُّكُونِ، تَنْفِي عَنِ الْمَعْطُوفِ مَا ثَبَتَ لِلْمَعْطُوفِ عَلَيْهِ.", "«not» — the conjoining la: denies of the second what the first was given.", "«değil» — atıf lâ'sı.", "la-nafiya"),
                           "zaida": ("«لَا» زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ، مَبْنِيَّةٌ عَلَى السُّكُونِ.", "«la» — redundant, strengthening the negation.", "«lâ» — nefyi pekiştiren zâid.", "la-nafiya"),
                           "jawab": ("«لَا» حَرْفُ جَوَابٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«no» — the answering la.", "«hayır» — cevap harfi.", "la-nafiya")}
                FACE_MAN = {"shart": ("اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«whoever» — a conditional noun, it puts two verbs in jazm; built, in the place of raf' as the mubtada'.", "«kim … -se» — cezmeden şart ismi; mebnî, mahallen merfû mübtedâ.", "al-majzum-wal-shart-wal-jaza"),
                            "mawsul": ("اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "«the one who» — a relative pronoun, built.", "«kimse ki» — ism-i mevsûl, mebnî.", "asma-al-ishara-wal-mawsulat"),
                            "istifham": ("اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«who?» — an interrogative noun, built.", "«kim?» — istifhâm ismi, mebnî.", "al-istifham"),
                            "mawsufa": ("نَكِرَةٌ مَوْصُوفَةٌ بِمَعْنَى شَخْصٍ، مَبْنِيَّةٌ عَلَى السُّكُونِ.", "«someone» — an indefinite noun described by what follows, built.", "«bir kimse» — mevsûf nekre, mebnî.", "asma-al-ishara-wal-mawsulat")}
                shadda = "ّ" in N(host_of(full, enc))
                ar = en = tr = ""; tags = []
                if pb in ("لمن", "بما", "فيما", "فيمن", "كمن", "ممن", "انما", "كلما", "ايها", "هلا", "اذا", "كما", "لو", "لولا", "اما", "حتى") and not enc: kind = "particle"
                if kind == "particle" and rule in ROLE and (pos or "").startswith("noun") and pb not in PART and pb not in DEM and pb not in PRON: kind = "noun"
                if pb == "من" and "\u0650" in N(host_of(full, enc))[(2 if pre else 0):][:3]: kind = "particle"   # مِنَ the preposition, not مَنْ the relative
                if bare(host_of(full, "")).replace("ٰ", "") in ("لله", "فلله", "ولله") and not enc:
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": "allah", "pos": "propn", "grammar": [t for t in ["huruf-jarr"] + (["mubtada-khabar"] if rule in ("khabar",) else []) if t in GIDS], "irab": {"ar": ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ" + ("، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ." if rule == "khabar" else "."), "en": "«to God» — the lam of jarr on the Name" + ("; the phrase is the khabar." if rule == "khabar" else "."), "tr": "«Allah'a» — lafza-i celâl üzerinde cer lâmı" + ("; câr-mecrûr haberdir." if rule == "khabar" else ".")}, "segments": ([{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}] if pre else []) + [{"form": "لِ", "lex": "li", "pos": "prep"}, {"form": "اللّٰهِ", "lex": "allah", "pos": "propn"}]})
                    take("allah", where); take("li", where)
                    if pre: take("wa" if pre == "و" else "fa", where)
                    continue
                if (kind == "noun" and (pos or "").startswith("noun") and k == "keep" and rule in ("mabni", "keep") and pb not in PART and pb not in DEM and pb not in PRON and not enc): k = None; rule = None
                if pb == "لا" and not enc and i + 1 < len(words) and not fx.get("wajh"):   # the face from the written context, not the authoring-time guess
                    nw_ = host_written(words, i + 1); nxt_ = words[i + 1]
                    rawn_ = N(re.sub(r"[،:؛.؟!«»\"()]", "", raw_at(words, i + 1) or "")); rawn_ = rawn_[2:] if pre_of(rawn_) else rawn_
                    if enc_of(nxt_) and rawn_ and (bare(rawn_) in LX or (nxt_.get("key") and G.get(nxt_["key"]) and noal(bare(N(str(G[nxt_["key"]].get("lemma") or "").split("(")[0]))) == noal(bare(rawn_)))): nw_ = rawn_   # شَرِيكَ: the engine's «enclitic» is the lemma's own last letter
                    nws_ = nw_.replace("ّ", ""); nb_ = bare(nw_)
                    nv_ = nxt_.get("kind") == "verb" or nxt_.get("k") == "cell" or (re.match(r"^[يتأن][َُ]", nws_) and len(nb_) >= 3 and verb_key_for(nw_) is not None)
                    neg_before_ = any(re.sub(r"^[وف]", "", bare(words[q]["w"])) in ("لا", "ليس", "ليست", "لم", "ما", "لن", "غير", "بلا", "لست", "لسنا", "ليسوا") and not any(pauses[r_] and not re.search(r"،$", raw_at(words, r_) or "") for r_ in range(q, i)) for q in range(max(0, i - 6), i))
                    jins_before_ = i >= 2 and re.sub(r"^[وف]", "", bare(words[i - 2]["w"])) == "لا" and re.search(r"َ$", host_written(words, i - 1).replace("ّ", "")) and not re.search(r"[ًٌٍ]", host_written(words, i - 1)) and words[i - 1].get("kind") == "noun" and not enc_of(words[i - 1]) and not bare(words[i - 1]["w"]).startswith("ال") and words[i - 1].get("pos") != "propn"
                    if nv_ and nxt_.get("kind") != "verb" and nxt_.get("k") != "cell": nv_ = not re.search(r"[ًٌٍ]", nw_) and bool(re.search(r"([َُْ]|ُوا|ُونَ|ِينَ|َانِ|ِي|َا)$", nws_))
                    if nv_ and (re.search(r"[ًٌٍ]", nw_) or nb_.startswith("ال")): nv_ = False
                    nasib_before_ = any(re.sub(r"^[وف]", "", bare(words[q]["w"])).replace("أ", "ا") in ("ان", "لن", "كي", "حتى", "اذن", "لكي") and not any(pauses[r_] for r_ in range(q, i)) for q in range(max(0, i - 5), i))
                    prev_say_la_ = i > 0 and re.sub(r"^[وف]", "", bare(words[i - 1]["w"])) in ("قال", "قالت", "قالوا", "يقول", "فيقول", "قلت", "قلنا", "اجاب", "فقال", "قالا", "تقول", "يقولون")
                    pron_next_ = nb_ in ("هو", "هي", "هم", "هما", "هن", "انت", "انتم", "انا", "نحن", "ذلك", "هذا", "هذه", "ذاك", "تلك", "اولئك", "هؤلاء", "غير", "غيره", "غيرها", "غيرهم")
                    if os.environ.get("PKG_DEBUG") and where in os.environ["PKG_DEBUG"].split(","): print("LA?", where, full, "nw_", nw_, "nws_", nws_, "nb_", nb_, "kind", nxt_.get("kind"), "pos", nxt_.get("pos"), "key", nxt_.get("key"), "enc", repr(enc_of(nxt_)), "nv_", nv_, "neg", neg_before_, "jb", jins_before_, "pron", pron_next_, "wajh0", wajh)
                    if prev_say_la_ and not pre and (pauses[i] or nb_ in ("الا", "إلا") or (re.match(r"^[بلك]ِ", nws_) or nb_ in ("في", "على", "الى", "إلى", "من", "عن")) and not nv_): wajh = "jawab"
                    elif nv_: wajh = "nahiya" if (re.match(r"^ت[َُ]", nws_) and not nasib_before_ and (re.search(r"ْ$", nws_) or (re.search(r"(ُوا|َا)$", nws_) and len(nb_) >= 4) or re.search(r"َنّ$", host_written(words, i + 1)) or (enc_of(words[i + 1]) and re.search(r"(ُو|َا)$", nws_))) and not re.search(r"(ُونَ|ِينَ|َانِ|ُ)$", nws_)) else "nafiya"
                    elif jins_before_ and pre in ("و", "ف") and re.search(r"َ$", nws_) and not re.search(r"[ًٌٍ]", nw_) and not nb_.startswith("ال") and nxt_.get("kind") == "noun" and not enc_of(nxt_) and not pron_next_: wajh = "jins"
                    elif re.search(r"َ$", nws_) and not re.search(r"[ًٌٍ]", nw_) and not nb_.startswith("ال") and nxt_.get("kind") == "noun" and not pron_next_ and not re.search(r"(ِينَ|ُونَ|َانِ)$", nws_) and not re.match(r"^[يتأن][َُ]", nws_) and nxt_.get("pos") not in ("pron", "part", "propn") and (G.get(nxt_.get("key") or "") or {}).get("pos") != "propn" and not (enc_of(nxt_) and nw_ == host_written(words, i + 1)) and not (pre in ("و", "ف") and neg_before_ and (G.get(nxt_.get("key") or "") or {}).get("pos") == "propn"): wajh = "jins"
                    elif pre in ("و", "ف") and neg_before_: wajh = "zaida"
                    elif not pre and i > 0 and not neg_before_ and (is_noun_w(words[i - 1]) or enc_of(words[i - 1])) and "قول" not in bare(words[i - 1]["w"]) and "قال" not in bare(words[i - 1]["w"]) and nxt_.get("kind") == "noun" and not re.match(r"^[يتأن][َُ]", nws_) and (re.search(r"[ٌٍ]", nw_) or re.search(r"(ِينَ|ُونَ)$", nws_) or enc_of(nxt_) or (i + 2 >= len(words) or pauses[i + 1])) and not pron_next_: wajh = "atifa"
                    else: wajh = "nafiya"
                if pb == "لا" and not enc and wajh in FACE_LA:
                    ar0, en0, tr0, tg = FACE_LA[wajh]; ar0 = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + ar0
                    if pre: take("wa" if pre == "و" else "fa", where)
                    take("la-nafiya" if wajh != "nahiya" else ("la-nahiya" if "la-nahiya" in G else "la-nafiya"), where); lx = "la-nahiya" if (wajh == "nahiya" and "la-nahiya" in G) else "la-nafiya"
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": lx, "pos": "part", "grammar": [t for t in [tg] if t in GIDS], "irab": {"ar": ar0, "en": en0, "tr": tr0}, **({"segments": [{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}, {"form": full[2:], "lex": lx, "pos": "part"}]} if pre else {})})
                    continue
                if pb == "من" and not enc and "\u0650" not in N(host_of(full, enc))[(2 if pre else 0):][:3] and wajh in ("shart", "mawsul", "istifham"):
                    nxk_ = words[i + 1] if i + 1 < len(words) else None
                    nxh_ = host_written(words, i + 1) if nxk_ is not None else ""; nxb2_ = bare(nxh_).replace("أ", "ا").replace("إ", "ا")
                    nx_verb_ = nxk_ is not None and (nxk_.get("kind") == "verb" or nxk_.get("k") == "cell" or nxb2_ in ("كان", "كانت", "كانوا", "ليس", "لم", "لا", "ما", "لن") or (verb_key_for(nxh_) is not None and not re.search(r"[ًٌٍ]", nxh_) and not nxb2_.startswith("ال") and re.search(r"[َُْ]$|ُوا$|ُونَ$|َتْ$", nxh_.replace("ّ", ""))))
                    nx_madi_ = nx_verb_ and nxk_ is not None and (nxb2_ in ("كان", "كانت", "كانوا") or (not re.match(r"^[يتأن][َُ]", nxh_.replace("ّ", "")) and nxb2_ not in ("لم", "لا", "ما", "لن", "ليس")))
                    fa_after_ = any(pre_of(N(words[q]["w"])) == "ف" and not any(pauses[r_] and not re.search(r"،$", raw_at(words, r_) or "") for r_ in range(i, q)) for q in range(i + 2, min(len(words), i + 12)))
                    madi2_ = any((is_verb_w(words[q]) or verb_key_for(host_written(words, q)) is not None) and not re.match(r"^[وف]?[يتأن][َُ]", host_written(words, q).replace("ّ", "")) and pre_of(N(words[q]["w"])) != "و" and not any(pauses[r_] and not re.search(r"،$", raw_at(words, r_) or "") for r_ in range(i, q)) for q in range(i + 2, min(len(words), i + 6)))
                    question_ = any("؟" in str(raw_at(words, q) or "") for q in range(i, min(len(words), i + 10)))
                    prev_b_ = re.sub(r"^[وف]", "", bare(words[i - 1]["w"])).replace("إ", "ا").replace("أ", "ا") if i else ""
                    prev_pause_ = i == 0 or (pauses[i - 1] and not re.search(r"،$", raw_at(words, i - 1) or ""))
                    prev_noun_ = i > 0 and not prev_pause_ and is_noun_w(words[i - 1]) and not enc_of(words[i - 1]) and not re.search(r"[ًٌٍ]", host_written(words, i - 1)) and not bare(words[i - 1]["w"]).startswith("ال") and prev_b_ not in ("تعالى", "وجل", "وسلم")
                    prev_say_ = prev_b_ in ("قال", "قالت", "قالوا", "يقول", "فيقول", "قلت", "قلنا", "تقول", "يقولون", "قيل")
                    prev_ask_ = prev_b_.startswith("سال") or prev_b_.startswith("سئل") or prev_b_.startswith("يسال") or prev_b_.startswith("تسال") or prev_b_ in ("سل", "سلوا", "سلهم")
                    prev_verb_ = i > 0 and not prev_pause_ and is_verb_w(words[i - 1]) and not prev_say_ and prev_b_ not in ("تعالى", "كان", "كانت", "كانوا", "ليس")
                    prev_jarr_ = i > 0 and not prev_pause_ and (prev_b_ in ("من", "عن", "الى", "على", "في", "ب", "ل", "ك", "مع", "عند", "لدى", "بين", "كل", "بعض", "مثل", "غير", "سوى", "الا", "اما", "جميع", "سائر", "احد", "اول", "اكثر") or re.match(r"^[بلك]ِ", host_written(words, i - 1)) or words[i - 1].get("rule") in ("jarr", "jarrPron"))
                    jussive_next_ = nx_verb_ and bool(re.search(r"ْ$", nxh_.replace("ّ", ""))) and nxb2_ not in ("لم", "لن", "لا", "ما") and bool(re.match(r"^[يتأن][َُ]", nxh_.replace("ّ", ""))) and not re.search(r"(َتْ|ْتُ|ْتَ|ْنَا)$", nxh_.replace("ّ", ""))
                    prev_jarr_ = prev_jarr_ and not re.match(r"^(لان|لانه|لانها|لانهم|لعل|لكن|ليت|لو|لولا|لئن|لما|لم|لن)$", prev_b_)
                    if question_: wajh = "istifham"
                    elif prev_ask_: wajh = "istifham"
                    elif prev_say_ and not nx_verb_ and not re.match(r"^[بلك]ِ", nxh_) and nxb2_ not in ("في", "على", "الى", "من", "عن"): wajh = "istifham"
                    elif pre in ("ف", "و") and nx_verb_ and (fa_after_ or jussive_next_ or (nx_madi_ and madi2_)) and not (prev_b_ in ("اما", "فاما", "واما")): wajh = "shart"
                    elif jussive_next_: wajh = "shart"
                    elif prev_jarr_ or prev_noun_: wajh = "mawsul"
                    elif prev_verb_ and nx_verb_ and not pre: wajh = "mawsul"
                    elif nx_verb_ and pre == "ف" and nx_madi_ and madi2_: wajh = "shart"
                    elif nx_verb_ and fa_after_: wajh = "shart"
                    elif nx_verb_ and prev_pause_: wajh = "shart"
                    elif nx_verb_: wajh = "mawsul"
                    elif not nx_verb_ and not prev_pause_: wajh = "mawsul"
                    elif wajh not in ("shart", "mawsul", "istifham"): wajh = "istifham"
                if pb == "من" and not enc and "\u0650" not in N(host_of(full, enc))[(2 if pre else 0):][:3] and wajh in FACE_MAN:
                    ar0, en0, tr0, tg = FACE_MAN[wajh]; ar0 = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + "«مَنْ» " + ar0
                    if pre: take("wa" if pre == "و" else "fa", where)
                    take("man", where)
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": "man", "pos": "pron", "grammar": [t for t in [tg] if t in GIDS], "irab": {"ar": ar0, "en": en0, "tr": tr0}, **({"segments": [{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}, {"form": full[2:], "lex": "man", "pos": "pron"}]} if pre else {})})
                    continue
                pb = pb.replace("ٰ", "")   # the dagger alif of ذٰلِكَ / هٰذَا never hides the word
                if os.environ.get("PKG_DEBUG") and where in os.environ["PKG_DEBUG"].split(","):
                    _hk = N(host_of(full, enc)); _hk = _hk[2:] if pre else _hk; _vk = verb_key_for(_hk); _lm = str(((G.get(_vk) or next((v for v in LX.values() if v.get("key") == _vk and v.get("lemma")), None) or {}).get("lemma")) or "") if _vk else ""
                    print("DIV?", where, full, "kind", kind, "k", k, "rule", rule, "pb", pb, "enc", repr(enc), "key", key, "hk", _hk, "vk", _vk, "lem", _lm, "shape", verb_shape(_hk, _lm, words, i) if _vk else None)
                hk_ = N(host_of(full, enc)); hk_ = hk_[2:] if pre else hk_; hks_ = hk_.replace("ّ", "")
                wb_ = bare(full).replace("ٰ", ""); wb_ = wb_[1:] if pre else wb_; wb_ = wb_.replace("أ", "ا").replace("إ", "ا")
                if enc and (wb_ in DEM or wb_ in EXTRA_PART or (len(wb_) >= 4 and wb_[0] in "كلب" and wb_[1:] in DEM)) and (kind == "particle" or k == "keep" or rule in ("mabni", "keep") or kind == "pron"):
                    enc = ""; pb = wb_; core = bare(host_of(full, "")); core = core[1:] if pre else core; hk_ = N(host_of(full, "")); hk_ = hk_[2:] if pre else hk_; hks_ = hk_.replace("ّ", "")
                    if wb_ in DEM: kind = "pron"; k = "keep"; rule = "mabni"
                if (kind == "particle" or k == "keep" or rule in ("mabni", "keep")) and not fx.get("pos") and not fx.get("irab"):
                    if KANA_RE.match(pb) and not enc:   # كَانَ، لَيْسَ، كُنْتُمْ، يَكُونُونَ: kāna's family is a verb, never a particle
                        kind = "verb"; k = "cell"; w = dict(w); w["cell"] = dict(w.get("cell") or {})
                        if re.match(r"^[يتأن][َُ]", hks_) and not re.search(r"(ْتُ|ْتَ|ْنَا|ْتُمْ|َتْ|ُوا)$", hks_): w["cell"]["tense"] = "mudari"; rule = "jazm" if gov_before(words, i) == "jazm" else ("nasbVerb" if gov_before(words, i) == "nasb" else "raf")
                        else: w["cell"]["tense"] = "mazi"; rule = "mazi"
                        key = verb_key_for(hk_) or key
                    elif pb in FIVE and not enc and i + 1 < len(words) and (words[i + 1].get("kind") == "noun" or words[i + 1].get("pos") in ("propn", "noun")):   # أَبِي حَنِيفَةَ: the five nouns before their annexed noun
                        kind = "noun"; k = None; rule = None
                    elif pb in ("اي",) and re.search(r"[ُِ]$", hks_) and not enc:   # أَيُّ / أَيِّ with a case vowel is the noun, not the explanatory أَيْ
                        kind = "noun"; k = None; rule = None
                    elif pb in ("الله",) and re.search(r"[ُ]$", hks_) and not enc: kind = "noun"; k = None; rule = None; key = "allah"   # وَاللهُ عَلَى الْعَرْشِ: the name with its ḍamma opens a clause
                    elif pb in ("الله",) and re.search(r"[ِ]$", hks_) and not enc and pre == "و" and not fx.get("irab"):   # وَاللهِ: the oath
                        fx = dict(fx); fx["irab"] = {"ar": "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مُقْسَمٌ بِهِ مَجْرُورٌ بِالْكَسْرَةِ.", "en": "The wāw is the oath's wāw (a jarr letter); «Allāh» is the sworn-by noun in jarr by the kasra.", "tr": "Vâv kasem vâvı (harf-i cer); lafza-i celâl muksem-bih, kesre ile mecrûr."}; fx["tags"] = ["huruf-jarr", "al-qasam"]; fx["key"] = "allah"; fx["pos"] = "noun"; fx["rule"] = "jarr"; fx["k"] = "jarr"; kind = "noun"; k = "jarr"; rule = "jarr"; key = "allah"
                    elif (pb in ("اهم",) and not re.search(r"ْ$", hks_)) or pb in ("كفو", "الان", "اثنتين", "اثنين", "الاثنين", "الاثنتين") or (enc and pb in ("معنا", "بعد", "قبل", "يد", "يدي", "يدا")):
                        kind = "noun"; k = None; rule = None
                    elif pb not in PART and pb not in DEM and pb not in PRON and pb not in EXTRA_PART and len(bare(hk_)) >= 3 and (re.search(r"[َ]$|ُوا$|[ّْ](تُ|تَ|تِ|نَا|تُمْ)$|َتْ$|َتِ$", hks_) or (enc and re.search(r"َا$", hks_)) or re.match(r"^[يتأن][َُ]", hks_)) and verb_key_for(hk_):   # كَلَّمَ، بَنَاهُ، فَاسْتَحَبُّوا: a verb the engine left as a built word
                        vk_ = verb_key_for(hk_); lem__ = str(((G.get(vk_) or next((v for v in LX.values() if v.get("key") == vk_ and v.get("lemma")), None) or {}).get("lemma")) or "")
                        vt_, vm_ = verb_shape(hk_, lem__, words, i)
                        if vt_: kind = "verb"; k = "cell"; rule = vm_; key = vk_; w = dict(w); w["cell"] = dict(w.get("cell") or {}); w["cell"]["tense"] = vt_; words[i] = w
                    elif pb in PART and pb not in ("منذ", "مذ", "حيث", "قط", "ايها", "بعد", "قبل", "عن", "من", "في", "ب", "ل", "ك", "الى", "على", "حتى", "كي", "لكي", "اي", "ثم", "ان", "لكن") and not enc and (re.search(r"[ٌٍُ]$", hks_) or (re.search(r"ِ$", hks_) and not (i + 1 < len(words) and re.match(r"^(ال|ا[^ً-ٰ])", bare(words[i + 1]["w"]))))) and len(bare(hk_)) >= 2:   # أُمُّ، أَيُّ: a case vowel on the end is a noun, not the homograph particle (never the waṣl kasra of عَنِ / إِنِ before ال)
                        kind = "noun"; k = None; rule = None
                    elif pb in ("يديه", "معناه", "يدي", "يدا") or (enc and pb in ("يد",)):
                        kind = "noun"; k = None; rule = None
                if kind == "verb" and not fx.get("pos") and not enc and (re.match(r"^[أا]َ[ء-ي]ْ[ء-ي]َ[ء-ي]ُ$", hks_) or re.match(r"^[أا]َ[ء-ي]َ[ء-ي]ُ$", hks_)) and i + 1 < len(words) and bare(words[i + 1]["w"]).replace("إ", "ا") in ("الي", "اليك", "اليه", "اليهم", "الينا", "من", "منه", "منك", "منهم", "عند", "عندك", "عنده"):   # أَحَبُّ إِلَيَّ، أَكْثَرُ مِنْ: the elative before its مِنْ / إِلَى is a noun, not a verb
                    kind = "noun"; k = None; rule = None
                if kind == "particle" or k == "keep" or rule in ("mabni", "jarrPron", "pron", "symbol", "keep") or (pb.startswith("لل") and ("ال" + pb[2:]) in DEM and not enc):
                    pkey = pb
                    if pb in ("ان", "إن", "أن") and not shadda: pkey = "إن" if full.replace("وَ", "").replace("فَ", "").startswith("إِ") else "أن"
                    if pb == "ان" and shadda: pkey = "إنّ" if full.replace("وَ", "").replace("فَ", "").startswith("إِ") else "أنّ"
                    if pb == "لان" and shadda: pkey = "لان"
                    if not enc and shadda:
                        m_ = re.match(r"^(ان|لكن|لعل|كان|لان)(هما|كما|هم|هن|كم|كن|نا|ها|ني|ه|ك|ي)$", pb)
                        if m_: enc = m_.group(2); pb = m_.group(1)
                    if enc and pb in ("ان", "لكن", "لعل", "كان", "لان") and shadda:
                        base = {"ان": ("إِنَّ" if full.replace("وَ", "").replace("فَ", "").startswith("إِ") else "أَنَّ"), "لكن": "لٰكِنَّ", "لعل": "لَعَلَّ", "كان": "كَأَنَّ", "لان": "لِأَنَّ"}[pb]
                        bk = {"إِنَّ": "inna", "أَنَّ": "anna", "لٰكِنَّ": "lakinna", "لَعَلَّ": "laalla", "كَأَنَّ": "kana", "لِأَنَّ": "lianna"}[base]
                        ar = f"«{base}» حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَ{ENC_AR.get(enc, 'الضَّمِيرُ')} ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا."; en = f"{base} + the pronoun {ENC_EN.get(enc, '')}: the pronoun is its noun, in the place of nasb."; tr = f"{base} + zamir {ENC_TR.get(enc, '')}: zamir onun ismidir, mahallen mansûb."; tags = ["inna-wa-akhawatuha"]
                        key = bk; take(bk, where); take(ENC.get(enc, "?"), where)
                        hf = N(host_of(full, enc)); hf = hf[2:] if pre else hf
                        segs = ([{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}] if pre else []) + [{"form": hf, "lex": bk, "pos": "part"}, {"form": full[len(N(host_of(full, enc))):], "lex": ENC.get(enc, "?"), "pos": "pron"}]
                        if pre: take("wa" if pre == "و" else "fa", where)
                        toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": key, "pos": "part", "grammar": tags, "irab": {"ar": ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + ar, "en": en, "tr": tr}, "segments": segs})
                        continue
                    if not enc:
                        m_ = re.match(r"^(علي|الي|لدي|في|من|عن|مع|عند|بين|ب|ل|ك)(هما|كما|هم|هن|كم|كن|نا|ها|ني|ه|ك|ي)$", pb)
                        if m_ and (rule == "jarrPron" or kind == "particle") and pb not in PART and pb not in ("لكن", "لعل", "كان", "ان", "لان", "كأن", "ليت"): enc = m_.group(2); pb = m_.group(1)
                        if pb == "من" and full.replace("وَ", "").replace("فَ", "") in ("مِنِّي",): enc = "ي"
                    if rule == "jarrPron" or (enc and pb in ("ل", "ب", "ك", "في", "على", "علي", "الى", "الي", "عن", "من", "مع", "لدى", "لدي", "عند", "بين")):
                        hb = pb
                        PREP = {"ل": ("li", "اللَّامُ"), "ب": ("bi", "الْبَاءُ"), "ك": ("ka", "الْكَافُ"), "في": ("fi", "«فِي»"), "على": ("ala", "«عَلَى»"), "علي": ("ala", "«عَلَى»"), "الى": ("ila", "«إِلَى»"), "الي": ("ila", "«إِلَى»"), "عن": ("an", "«عَنْ»"), "من": ("min", "«مِنْ»"), "مع": ("maa", "«مَعَ»"), "عند": ("inda", "«عِنْدَ»"), "لدى": ("lada", "«لَدَى»")}
                        pk, pn = PREP.get(hb, (None, "«" + hb + "»"))
                        ar = f"{pn} حَرْفُ جَرٍّ، وَ{ENC_AR.get(enc, 'الضَّمِيرُ')} ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ." if hb not in ("مع", "عند", "لدى") else f"{pn} ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَ{ENC_AR.get(enc, 'الضَّمِيرُ')} مُضَافٌ إِلَيْهِ."
                        en = f"preposition + pronoun {ENC_EN.get(enc, '')}: the pronoun is in jarr."; tr = f"harf-i cer + zamir {ENC_TR.get(enc, '')}: zamir mecrûr."
                        tags = ["huruf-jarr", "al-mabni-wal-mudmar"]
                        if pk and ENC.get(enc) and pk in G and ENC[enc] in G:
                            key = pk; take(pk, where); take(ENC[enc], where)
                        elif key: take(key, where)
                        else: key = pk or key; take(key, where) if key else None
                    elif pb in PRON and not enc:
                        a_, e_, t_, pk = PRON[pb]; ar = a_ + " فِي مَحَلِّ رَفْعٍ."; en = e_ + " — a detached pronoun; in the place of raf'."; tr = t_ + " — munfasıl zamir, mahallen merfû."; tags = ["al-mabni-wal-mudmar"]
                        key = key or pk; take(key, where)
                    elif (pb in DEM or (pb.startswith("لل") and ("ال" + pb[2:]) in DEM)) and not enc and (kind != "particle" or pb in ("ما", "من") or pb not in ("ما", "من")) and not (pb == "من" and "\u0650" in N(host_of(full, enc))[(2 if pre else 0):][:3]):
                        cs = CASE_OF_RULE.get(rule)
                        ma_face_ = None
                        if pb == "ما" and not enc and "\u0650" not in N(host_of(full, enc))[(2 if pre else 0):][:3] and i + 1 < len(words):
                            # (wave 157) مَا by its written clause: ظرفية before لَمْ; استفهام before a noun at a clause head or after a saying verb; حجازية when a بِ-phrase or a manṣūb answers that noun; نافية at a clause head before a verb (or with إِلَّا later, or مَا لَهُ … مِنْ); موصولة after a noun, a jarr letter, a demonstrative or a transitive verb
                            nxm_ = host_written(words, i + 1); nxmb_ = bare(nxm_).replace("أ", "ا").replace("إ", "ا"); nxk2_ = words[i + 1]
                            nxv_ = nxk2_.get("kind") == "verb" or nxk2_.get("k") == "cell" or nxmb_ in ("كان", "كانت", "كانوا", "ليس") or (nxk2_.get("kind") != "noun" and not enc_of(nxk2_) and verb_key_for(nxm_) is not None and not re.search(r"[ًٌٍ]", nxm_) and not nxmb_.startswith("ال") and re.search(r"[َُْ]$|ُوا$|ُونَ$|َتْ$|ْتُ$|ْنَا$", nxm_.replace("ّ", "")))
                            prevm_ = re.sub(r"^[وف]", "", bare(words[i - 1]["w"])).replace("إ", "ا").replace("أ", "ا") if i else ""
                            pausem_ = i == 0 or (pauses[i - 1] and not re.search(r"،$", raw_at(words, i - 1) or ""))
                            saym_ = prevm_ in ("قال", "قالت", "قالوا", "يقول", "فيقول", "قلت", "قلنا", "تقول", "يقولون", "قيل", "تعالى", "وجل", "وسلم") or (i >= 2 and bare(words[i - 1]["w"]) in ("تعالى", "وجل") and re.sub(r"^[وف]", "", bare(words[i - 2]["w"])) in ("قال", "قوله", "لقوله", "بقوله"))
                            illa_ = any(bare(words[q]["w"]).replace("إ", "ا") == "الا" and not any(pauses[r_] and not re.search(r"،$", raw_at(words, r_) or "") for r_ in range(i, q)) for q in range(i + 1, min(len(words), i + 9)))
                            prev_noun_m_ = i > 0 and not pausem_ and (is_noun_w(words[i - 1]) or prevm_ in ("هذا", "هذه", "ذلك", "تلك", "كل", "بعض", "غير", "مثل", "افضل", "اول", "اكثر", "جميع", "من", "عن", "الى", "على", "في", "ب", "ل", "ك", "مع", "عند", "بعد", "قبل", "بين", "حسب", "سوى", "الا", "حتى", "ان", "لان", "فان"))
                            prev_verb_m_ = i > 0 and not pausem_ and is_verb_w(words[i - 1]) and not saym_ and prevm_ not in ("كان", "كانت", "كانوا", "ليس")
                            if nxmb_ == "لم": ma_face_ = ("«مَا» مَصْدَرِيَّةٌ ظَرْفِيَّةٌ (مَا لَمْ = مُدَّةَ عَدَمِ …)، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "«as long as … not, unless» — the time-making maṣdar مَا before لَمْ.", "«… -medikçe» — lem'den önce zarfiyye masdariyye mâ.", ["ma-masdariyya"])
                            elif not nxv_ and re.match(r"^[لب]", nxmb_) and nxmb_ in ("له", "لها", "لهم", "لكم", "لك", "لنا", "لي", "لهما", "بهم", "بك", "به") and any(bare(words[q]["w"]) == "من" for q in range(i + 2, min(len(words), i + 5))): ma_face_ = ("«مَا» نَافِيَةٌ، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "«not» — the negation: «he has no …».", "«değil / yok» — nefiy mâsı.", ["ma-nafiya"])
                            elif not nxv_ and nxmb_ in ("له", "لها", "لهم", "لكم", "لك", "لنا", "لي", "لهما"): ma_face_ = ("«مَا» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ (مَا لَهُمْ … = أَيُّ شَيْءٍ لَهُمْ).", "«what is it with them …?» — the interrogative مَا as mubtadaʾ.", "«onlara ne oluyor …?» — istifhâm mâsı, mübtedâ.", ["ma-istifhamiyya"])
                            elif not nxv_ and (pausem_ or saym_ or any(bare(words[q]["w"]) in ("يا", "ايها") for q in range(max(0, i - 4), i)) or (pre == "ف" and (nxmb_.startswith("ال") or (words[i + 1].get("kind") == "noun" and i + 2 < len(words) and re.search(r"[ُ]$", nxm_.replace("ّ", "")) and not re.search(r"[ًٌٍ]", nxm_))))) and (nxmb_.startswith("ال") or enc_of(nxk2_) or nxk2_.get("pos") == "propn" or nxmb_ in ("هو", "هي", "هم", "انت", "انتم", "هذا", "ذلك", "هذه") or (pre == "ف" and words[i + 1].get("kind") == "noun" and not re.search(r"[ًٌٍ]", nxm_))):
                                hij_ = any(re.match(r"^بِ[أا]", N(words[q]["w"])) or (words[q].get("kind") == "noun" and re.search(r"ً$|َ$", host_written(words, q).replace("ّ", "")) and not re.search(r"[ٌٍ]", host_written(words, q))) for q in range(i + 2, min(len(words), i + 5)) if not (pauses[q - 1] and not re.search(r"،$", raw_at(words, q - 1) or "")))
                                ma_face_ = ("«مَا» الْحِجَازِيَّةُ النَّافِيَةُ تَعْمَلُ عَمَلَ لَيْسَ، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "«not» — the Ḥijāzī مَا that works like لَيْسَ: its noun in rafʿ, its predicate in naṣb or after بِ.", "«değil» — leyse gibi amel eden Hicâzî mâ.", ["ma-nafiya"]) if hij_ and nxmb_ not in ("هذا", "ذلك", "هذه") else ("«مَا» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَمَا بَعْدَهُ خَبَرٌ.", "«what is …?» — the interrogative مَا as mubtadaʾ, the noun after it its predicate.", "«… nedir?» — istifhâm mâsı mübtedâ, sonraki isim haber.", ["ma-istifhamiyya"])
                            elif nxv_ and saym_ and re.match(r"^[وف]?تَ", nxm_) and not illa_: ma_face_ = ("«مَا» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«what do you …?» — the interrogative مَا as the fronted object.", "«ne …?» — istifhâm mâsı, öne alınmış mef'ûl.", ["ma-istifhamiyya"])
                            elif nxv_ and (prev_noun_m_ or prev_verb_m_): ma_face_ = None
                            elif nxv_ and (pausem_ or saym_ or illa_ or (pre in ("و", "ف") and i > 0 and not is_noun_w(words[i - 1]))): ma_face_ = ("«مَا» نَافِيَةٌ، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "«not» — the negation before a verb.", "«değil / -madı» — fiilden önce nefiy mâsı.", ["ma-nafiya"])
                        if ma_face_:
                            ar, en, tr, tags = ma_face_; cs = None
                            if key: take(key, where)
                            continue_ma_ = True
                        else: continue_ma_ = False
                        if continue_ma_: pass
                        elif pb not in DEM and pb.startswith("لل"): cs = "jarr"; pb = "ال" + pb[2:]; ar = "اللَّامُ حَرْفُ جَرٍّ، وَ" + DEM[pb] + " فِي مَحَلِّ جَرٍّ."
                        else: ar = DEM[pb] + (f" فِي مَحَلِّ {CASE_AR[cs]}" if cs else "") + "."
                        if not continue_ma_: en = ("a demonstrative" if pb not in ("الذي", "التي", "الذين", "ما", "من") else "a relative pronoun") + " — built (mabni)" + (f"; in the place of {cs}" if cs else "") + "."; tr = ("işaret ismi" if pb not in ("الذي", "التي", "الذين", "ما", "من") else "ism-i mevsûl") + " — mebnî" + (f"; mahallen {CASE_AR[cs]}" if cs else "") + "."
                        if not continue_ma_: tags = ["asma-al-ishara-wa-sighuha"] if pb not in ("الذي", "التي", "الذين", "ما", "من") else ["ism-mawsul"]
                        if continue_ma_: pass
                        elif key: take(key, where)
                        else: report["nokey"].append((where, b))
                    elif pkey in PART:
                        a_, e_, t_, tg, pk = PART[pkey]; ar, en, tr, tags = a_, e_, t_, list(tg)
                        if pkey == "اما" and re.search(r"إِمَّا$", N(full)) and "imma" in G:   # إِمَّا is not أَمَّا: the hamza's kasra decides
                            a_, e_, t_, tg, pk = ("«إِمَّا» حَرْفُ تَفْصِيلٍ مَبْنِيٌّ عَلَى السُّكُونِ، لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "«either … or» — the letter of detailing; it never comes alone.", "«ya … ya» — tafsîl harfi; asla yalnız gelmez.", ["aw-imma-am-la-bal-lakin-fil-kafiya"], "imma"); ar, en, tr, tags = a_, e_, t_, list(tg)
                        nxw_ = N(words[i + 1]["w"]) if i + 1 < len(words) else ""; nxb_ = bare(nxw_).replace("أ", "ا").replace("إ", "ا")
                        nxww_ = host_written(words, i + 1).replace("ّ", "") if i + 1 < len(words) else ""
                        nx_mudari_ = bool(re.match(r"^[يتأن][َُ][ء-ي]", nxww_)) and len(bare(nxww_)) >= 3 and (words[i + 1].get("kind") == "verb" or verb_key_for(nxww_) is not None) and not re.search(r"(َتْ|ْتُ|ْتَ|ْنَا|ْتُمْ)$", nxww_) and not VERB_BY_LEMMA.get(N(host_written(words, i + 1))) and re.search(r"([َُْ]|ُونَ|ُوا|ِينَ|َانِ|ْنَ|ِي|ُو)$", nxww_) and not re.search(r"[اى]$", bare(nxww_)) and not (words[i + 1].get("kind") == "verb" and words[i + 1].get("cell") and "mazi" in str(words[i + 1].get("cell")))
                        if pkey == "قد" and nx_mudari_: ar = "«قَدْ» حَرْفٌ لِلتَّقْلِيلِ (أَوِ التَّكْثِيرِ) قَبْلَ الْمُضَارِعِ، مَبْنِيٌّ عَلَى السُّكُونِ."; en = "«qad» of rarity (or frequency) before a present verb — «sometimes»."; tr = "«kad» muzâriden önce taklîl (yahut teksîr) için — «bazen»."
                        lam_jawab_ = False
                        for q_ in range(i + 1, min(len(words), i + 7)):
                            wq_ = host_written(words, q_); bq_ = bare(wq_)
                            if q_ > i + 1 and pauses[q_ - 1]: break
                            if re.match(r"^لَ[ء-ي]", wq_) and len(bq_) >= 3 and bq_ not in ("لا", "لن", "لم", "لما", "لعل", "لكن", "ليس", "لدى", "لدن", "لو", "لولا", "ليت") and (words[q_].get("kind") == "verb" or re.match(r"^لَ(قد|كان|كانت|كانوا|كنت|كنا|ما|سوف|س)", bq_) or verb_key_for(wq_[2:]) is not None): lam_jawab_ = True; break
                        prev_q_ = re.sub(r"^[وف]", "", bare(words[i - 1]["w"])) if i else ""
                        law_wasl_ = pre == "و" and i > 0 and not (pauses[i - 1] and not re.search(r"،$", raw_at(words, i - 1) or "")) and not lam_jawab_ and prev_q_ not in ("قال", "قالت", "قالوا", "تعالى", "وجل", "وسلم", "قل")
                        if pkey == "لو" and pre == "و" and not law_wasl_: ar = "«لَوْ» حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ، حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ، مَبْنِيٌّ عَلَى السُّكُونِ."; en = "«had it been …» — the counterfactual conditional: the answer failed because the condition failed."; tr = "«… olsaydı» — cezmetmeyen şart harfi: şartı gerçekleşmediği için cevabı da gerçekleşmeyen imtinâ harfi."
                        if pkey == "لو" and law_wasl_: ar = "«لَوْ» الْوَصْلِيَّةُ لِلتَّقْلِيلِ وَالْمُبَالَغَةِ (= وَإِنْ)، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ."; en = "«even if» — the concessive law after the wāw, with no answer of its own."; tr = "«… olsa bile» — vâvdan sonra vasliyye lev, kendine ait cevabı yok."
                        if pkey == "لما" and nx_mudari_: ar = "«لَمَّا» جَازِمَةٌ نَافِيَةٌ: حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ مَبْنِيٌّ عَلَى السُّكُونِ («لَمْ … بَعْدُ»)."; en = "«not yet» — the negating, jussive lammā before a present verb."; tr = "«henüz … -medi» — muzâriden önce nefiy ve cezm lemmâ'sı."
                        nx2w_ = host_written(words, i + 2).replace("ّ", "") if i + 2 < len(words) else ""
                        nx2v_ = i + 2 < len(words) and (words[i + 2].get("kind") == "verb" or words[i + 2].get("k") == "cell" or (re.match(r"^[يتأن][َُ][ء-ي]", nx2w_) and len(bare(nx2w_)) >= 3 and re.search(r"[َُْ]$|ُوا$|ُونَ$", nx2w_) and (len(bare(nx2w_)) >= 4 or verb_key_for(host_written(words, i + 2)) is not None)))
                        if pkey == "إن" and not shadda and nxw_ and words[i + 1].get("kind") != "verb" and not re.match(r"^[يتأن][َُ]", nxw_.replace("ّ", "")) and any(bare(words[q]["w"]).replace("إ", "ا") == "الا" and not any(pauses[r_] for r_ in range(i, q)) for q in range(i + 2, min(len(words), i + 7))):
                            ar = "«إِنْ» نَافِيَةٌ بِمَعْنَى «مَا»، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ (وَ«إِلَّا» بَعْدَهَا لِلِاسْتِثْنَاءِ الْمُفَرَّغِ)."; en = "«not» — the negating in (= مَا); the إِلَّا after it makes «nothing but …»."; tr = "«değil / ancak» — nefiy in'i (= mâ); sonraki illâ ile «… -den başka değil»."; tags = ["nafy"]
                        prev_say_ = any(re.sub(r"^[وف]", "", bare(words[q]["w"])).replace("أ", "ا") in ("نادى", "ناداه", "ناداهم", "اوحى", "اوحينا", "اشار", "كتب", "كتبنا", "اومى", "اوما") and not any(pauses[r_] for r_ in range(q, i)) for q in range(max(0, i - 3), i))
                        if pkey in ("أن", "ان") and not shadda and prev_say_:
                            ar = "«أَنْ» تَفْسِيرِيَّةٌ (بِمَعْنَى «أَيْ»)، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ."; en = "«that is …» — the explanatory an after a verb that means «say» without its letters (نَادَى، أَوْحَى)."; tr = "«yani» — «söylemek» anlamını taşıyan fakat harflerini taşımayan fiilden (nâdâ, evhâ) sonra tefsîriyye en."; tags = ["an-masdariyya"]
                        elif pkey in ("أن", "ان") and not shadda and ((nxb_ == "لا" and not nx2v_) or nxb_ in ("لم", "لن", "قد", "سوف", "لو", "ليس") or nxb_.startswith("س") and len(nxb_) >= 4 and re.match(r"^سَ[يتأن]", nxw_) or (nxw_ and not re.match(r"^[يتأن][َُ]", nxw_.replace("ّ", "")) and not re.search(r"َ$|ُوا$|ْتُ$|ْتَ$|ْنَا$|َتْ$", nxw_.replace("ّ", "")) and words[i + 1].get("kind") not in ("verb", "particle") and nxb_ != "لا")):
                            ar = "«أَنْ» مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ: حَرْفُ تَوْكِيدٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ الْمَحْذُوفُ، وَالْجُمْلَةُ بَعْدَهَا خَبَرُهَا."; en = "«an» lightened from the heavy «anna»: its noun is the omitted pronoun of the matter, the clause after it its predicate."; tr = "«en» sakîleden muhaffefe: ismi hazfedilmiş şe'n zamiri, sonraki cümle haberi."; tags = ["inna-wa-akhawatuha"]
                        key = pk or key
                        if key: take(key, where)
                        else: report["nokey"].append((where, b))
                    elif pb in EXTRA_PART or (pb == "علي" and shadda) or (pb == "الي" and shadda) or (pb + (enc or "")) in EXTRA_PART or (pb == "ايا" and enc):
                        if (pb + (enc or "")) in EXTRA_PART and pb not in EXTRA_PART: pb = pb + enc; enc = ""
                        if pb == "ايا" and enc: pb = "ايا"
                        if pb in ("علي", "الي"):
                            ar = ("«عَلَى»" if pb == "علي" else "«إِلَى»") + " حَرْفُ جَرٍّ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ."; en = "the preposition with the speaker's yāʾ («on me» / «to me»); the yāʾ is the attached pronoun in the seat of jarr."; tr = "harf-i cer ile mütekellim yâ'sı («bana / üzerime»); yâ, cer mahallinde bitişik zamir."; key = "ala" if pb == "علي" else "ila"; tags = ["huruf-jarr", "al-damair"]
                        else:
                            ar, en, tr, lx_, tg_ = EXTRA_PART[pb]; key = lx_ if lx_ in G else (key or lx_); tags = list(tg_)
                        if key: take(key, where)
                        else: report["nokey"].append((where, b))
                    elif len(pb) >= 4 and pb[0] in "كلب" and pb[1:] in DEM and pb[1:] not in ("ما", "من") and not enc:   # كَذٰلِكَ، لِذٰلِكَ، بِهٰذَا: a jarr letter before the demonstrative
                        JL = {"ك": ("الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ", "ka"), "ل": ("اللَّامُ حَرْفُ جَرٍّ", "li"), "ب": ("الْبَاءُ حَرْفُ جَرٍّ", "bi")}[pb[0]]
                        ar = JL[0] + "، وَ" + DEM[pb[1:]] + " فِي مَحَلِّ جَرٍّ."; en = "a jarr letter before a demonstrative, which stands in the seat of jarr."; tr = "işaret isminden önce harf-i cer; işaret ismi cer mahallinde."; tags = ["asma-al-ishara-wa-sighuha", "huruf-jarr"]
                        dk_ = {"ذلك": "dhalika", "هذا": "hadha", "هذه": "hadhihi", "تلك": "tilka", "هؤلاء": "haulai", "اولئك": "ulaika"}.get(pb[1:]); take(JL[1], where)
                        key = dk_ if dk_ and dk_ in G else (key or JL[1])
                        if key: take(key, where)
                        else: report["nokey"].append((where, b))
                    else:
                        ar = "حَرْفٌ مَبْنِيٌّ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ."; en = "a particle — built, no place in the iʿrab."; tr = "harf — mebnî, i'râbda mahalli yok."
                        report.setdefault("genericParticle", []).append((where, full))
                        if key: take(key, where)
                        else: report["nokey"].append((where, b))
                    if pre and pb not in ("و", "ف"):
                        ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else "الْفَاءُ عَاطِفَةٌ، وَ") + ar; en = ("The waw conjoins; " if pre == "و" else "The fa conjoins; ") + en[:1].lower() + en[1:]; tr = ("«ve» + " if pre == "و" else "«bunun üzerine» + ") + tr[:1].lower() + tr[1:]
                        segs = [{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}, {"form": full[2:], "lex": key, "pos": "part"}]; take("wa" if pre == "و" else "fa", where)
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": key or "?", "pos": "pron" if (pb in PRON or pb in DEM) and key != "min" else "part", **({"grammar": list(dict.fromkeys(t for t in tags if t in GIDS))} if tags else {}), "irab": {"ar": ar, "en": en, "tr": tr}, **({"segments": segs} if segs else {})})
                    continue
                # ---- a verb the engine read as a noun: the lexicon's part of speech wins, the shape gives tense and mood
                if kind == "noun" and not fx.get("pos") and (rule in ROLE or rule in (None, "", "laJins")) and k in ("raf", "nasb", "jarr", "fath", None):
                    hv_ = N(host_of(full, enc)); hv_ = hv_[2:] if pre else hv_
                    FOLD_ = lambda x: x.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ٱ", "ا")
                    lxe_ = next((LXF_[FOLD_(c)] for c in (core, bh, bare(host_of(full, enc))) if FOLD_(c) in LXF_), None)
                    if lxe_ and not lxe_.get("pos") and lxe_.get("key"): lxe_ = G.get(lxe_["key"]) or next((v for v in LX.values() if v.get("key") == lxe_["key"] and v.get("pos")), lxe_)   # a reference row points at the defining row
                    gpos_ = (G.get(key) or {}).get("pos") if key else None
                    STEM_ = lambda x: re.sub(r"[ًٌٍَُِْ]$", "", x.replace("ّ", "").replace("ٰ", ""))
                    own_ = N(str((G.get(key) or (lxe_ if lxe_ and lxe_.get("key") == key else None) or {}).get("lemma") or "").split("(")[0].strip())
                    owns_ = bool(own_) and STEM_(own_) == STEM_(hv_)   # the engine's noun owns the written form (أَشَدَّ the elative, حَقَّنَا the noun — not verbs)
                    vl_ = VERB_BY_LEMMA.get(hv_.replace("ٰ", "")) or VERB_BY_STEM.get(STEM_(hv_))   # the written host IS a verb's lemma (فَرَضَ beside the noun فَرْض), or its stem with another last vowel (تَعَلَّمِ the amr)
                    if not vl_ and pre and VERB_BY_LEMMA.get(N(host_of(full, enc)).replace("ٰ", "")) and not owns_: vl_ = VERB_BY_LEMMA.get(N(host_of(full, enc)).replace("ٰ", "")); hv_ = N(host_of(full, enc)); pre = ""; is_pre = False   # وَحَّدَ، فَرَضَ: the و / ف is the verb's own first letter
                    if vl_ and not owns_ and (not key or (G.get(key) or {}).get("pos") != "verb"): key = vl_[0]; lxe_ = vl_[1]; gpos_ = "verb"
                    if os.environ.get("PKG_DEBUG") and where in os.environ["PKG_DEBUG"].split(","): print("PROMO?", where, full, "hv", hv_, "key", key, "vl", bool(vl_), "owns", owns_, "lxe", (lxe_ or {}).get("pos"), "gpos", gpos_, "shape", verb_shape(hv_, str(((G.get(key) or {}).get("lemma")) or ((lxe_ or {}).get("lemma")) or ""), words, i))
                    epos_ = (G.get(key) or (lxe_ if lxe_ and lxe_.get("key") == key else None) or {}).get("pos")
                    if owns_ and epos_ != "verb": lxe_ = None; gpos_ = None
                    if not ((lxe_ and lxe_.get("pos") == "verb") or gpos_ == "verb") and not owns_ and epos_ != "propn" and (G.get(key) or {}).get("pos") != "propn" and len(bare(hv_)) >= 4 and not re.search(r"[ًٌٍ]", hv_) and (re.match(r"^[يتن][َُ][ء-ي]", hv_.replace("ّ", "")) or (not key and re.match(r"^أ[َُ][ء-ي]", hv_.replace("ّ", ""))) or re.search(r"[ّْ](تُ|تَ|تِ|نَا|تُمْ)$|ُوا$", hv_.replace("ّ", ""))) and not (i + 1 < len(words) and bare(words[i + 1]["w"]) in ("بن", "ابن")):
                        vk2_ = verb_key_for(hv_)   # يُطِيقُونَ، تَعْلَمُونَ: the shape and the lexicon's verb agree where the engine saw a noun
                        if vk2_: key = vk2_; lxe_ = G.get(vk2_) or next((v for v in LX.values() if v.get("key") == vk2_ and v.get("pos")), None); gpos_ = "verb"
                    if (lxe_ and lxe_.get("pos") == "verb") or gpos_ == "verb":
                        lem_ = str(((G.get(key) or {}).get("lemma")) or ((lxe_ or {}).get("lemma")) or "")
                        vt_, vm_ = verb_shape(hv_, lem_, words, i)
                        if vt_:
                            kind = "verb"; k = "cell"; rule = vm_; w = dict(w); w["cell"] = dict(w.get("cell") or {}); w["cell"]["tense"] = vt_; w["kind"] = "verb"; w["k"] = "cell"; w["rule"] = vm_; w["key"] = key; words[i] = w; report["promoted"] += 1
                # ---- verbs
                if kind == "verb" or k == "cell" or rule in ("mazi", "amr", "raf", "nasbVerb", "jazm") or (pos and "verb" in pos and rule in ("raf", "jazm", "nasbVerb", "mazi", "amr")):
                    h = N(host_of(full, enc)); h2 = h[2:] if pre else h; hb2 = bare(h2)
                    if not enc and not fx.get("enc"):   # the engine left the object pronoun on the verb (أَرْضَانَا): split it where the rest is a verb's lemma
                        for sfx_ in ("نَا", "هُمْ", "هَا", "هُ", "كُمْ", "نِي", "كَ"):
                            if h2.endswith(sfx_) and len(bare(h2)) - len(bare(sfx_)) >= 3:
                                rest_ = h2[:-len(sfx_)]
                                if VERB_BY_LEMMA.get(rest_.replace("ٰ", "")) or (rest_.endswith("َا") and VERB_BY_LEMMA.get(rest_[:-1] + "ى")):
                                    enc = {"نَا": "نا", "هُمْ": "هم", "هَا": "ها", "هُ": "ه", "كُمْ": "كم", "نِي": "ني", "كَ": "ك"}[sfx_]; h = N(host_of(full, enc)); h2 = h[2:] if pre else h; hb2 = bare(h2); break
                    kpos_ = (G.get(key) or next((v for v in LX.values() if v.get("key") == key and v.get("pos")), None) or {}).get("pos") if key else None
                    if not fx.get("key") and where not in CITE and (key is None or kpos_ not in ("verb", "part")):   # a verb keyed to a homograph noun (قَالَ → قَالٍ) or to nothing: the verb that owns the form
                        kv_ = verb_key_for(h2)
                        if not kv_ and pre and verb_key_for(h):
                            kv_ = verb_key_for(h); pre = ""; h2 = h; hb2 = bare(h2); is_pre = False   # the و / ف is the verb's first radical (وَصَفَ، وَلَدَ، فَعَلُوهُ)
                        if kv_: key = kv_; report["rekeyed"] += 1
                        elif key: report.setdefault("verbNounKey", []).append((where, full, key))
                    tense = (w.get("cell") or {}).get("tense") or rule
                    if tense not in ("mazi", "amr") and not fx.get("rule") and not enc and VERB_BY_LEMMA.get(h2.replace("ٰ", "")): tense = "mazi"; rule = "mazi"   # أَحْدَثَ، تَوَسَّطَ after مَنْ is the māḍī of the lexicon, not a muḍāriʿ
                    if tense not in ("mazi", "amr") and not fx.get("rule") and enc and re.search(r"َا$", h2) and VERB_BY_LEMMA.get(h2[:-1] + "ى") and not re.match(r"^[يتن][َُ]", h2): tense = "mazi"; rule = "mazi"   # أَتَانَا، عَصَاهُ: the defective māḍī writes its ى as ا before an enclitic
                    if tense not in ("mazi", "amr") and not fx.get("rule") and re.search(r"[ّْ](تُ|تَ|تِ|نَا|تُمْ|تُنَّ)$|نَّا$", h2.replace("ٰ", "")) and not re.match(r"^[يتن][َُ][ء-ي]+ْنَ$", h2.replace("ّ", "")): tense = "mazi"; rule = "mazi"   # أَظْمَأْتُ، كُنَّا: a person suffix after a sukūn is the māḍī
                    hidden = i not in doers and not any(words[j].get("rule") in ("fail", "naib") and not any((words[q].get("kind") == "verb" or words[q].get("k") == "cell") for q in range(i + 1, j)) for j in range(i + 1, min(len(words), i + 7)))
                    nxt = words[i + 1]["w"] if i + 1 < len(words) else ""
                    person = person_of(h2, hb2, tense, rule, words, i)
                    mk = {"jazm": "jazm", "nasb": "nasbVerb", "raf": "raf"}.get(k) if rule not in ("raf", "nasbVerb", "jazm") else rule   # the mood from the engine's case where the rule names the construction (shart, jawab)
                    if mk not in ("raf", "nasbVerb", "jazm"): mk = "raf"
                    h2ns = h2.replace("ّ", "")   # NFC seats the shadda after the vowel (بُّو): the suffix test reads the word without it
                    five = bool(re.search(r"(ُونَ|َوْنَ|ِينَ|َانِ)(هُ|هَا|هُمْ|هُمَا|هُنَّ|كَ|كِ|كُمْ|كُمَا|كُنَّ|نِي|نَا)?$", h2ns)) and len(re.sub(r"(هم|هما|هن|ها|ه|كم|كما|كن|ك|نا|ني)$", "", hb2) if re.search(r"(ُونَ|ِينَ|َانِ)(هُ|هَا|هُمْ|هُمَا|هُنَّ|كَ|كِ|كُمْ|كُمَا|كُنَّ|نِي|نَا)$", h2ns) else hb2) - 3 >= 2
                    if not five and mk in ("nasbVerb", "jazm") and len(hb2) >= 4 and (re.search(r"(ُوا|َا)$", h2) or (re.search(r"ِي$", h2) and re.match(r"^[وف]?تَ", h2)) or (enc and (re.search(r"(ُو|َا)$", h2) or (re.search(r"ِي$", h2) and re.match(r"^[وف]?تَ", h2))))): five = True
                    if not five and enc and re.search(r"ُّ?و$", h2) and len(hb2) >= 4 and re.match(r"^[وف]?[يتأن][َُ]", h2): five = True; mk = mk if mk in ("nasbVerb", "jazm") else ("nasbVerb" if any(bare(words[q]["w"]).replace("أ", "ا") in ("ان", "لن", "كي", "حتى", "وان", "فان", "ولن") for q in range(max(0, i - 3), i)) else "jazm")
                    lem_def_ = bool(re.search(r"[ىيا]$", bare(N(str((G.get(key) or {}).get("lemma") or "").split("(")[0]))) ) if key else False
                    if five and lem_def_ and not enc and re.search(r"[وي]$", hb2) and not re.search(r"(ُونَ|ِينَ|َانِ|َوْنَ)$", h2ns): five = False
                    gv_ = gov_before(words, i); gla_ = gv_ == "jazm" and i > 0 and re.sub(r"^[وف]", "", bare(words[i - 1]["w"])) == "لا"
                    if lem_def_ and not enc and not five and re.search(r"[وي]$", hb2) and not re.search(r"[َ]$", h2ns) and gla_ and mk == "jazm": mk = "raf"
                    if mk == "nasbVerb" and not enc and not five and pre == "و" and re.search(r"[وي]$", hb2) and not re.search(r"[َُ]$", h2ns) and tense not in ("mazi", "amr") and not fx.get("rule") and len(hb2) >= 4: mk = "raf"   # وَيَرْجُو: a weak ending with no fatḥa after a و opens its own clause
                    if tense not in ("mazi", "amr") and rule not in ("mazi", "amr") and not fx.get("rule") and not fx.get("k") and not re.search(r"ّ[َ]?$", h2) and (gv_ is None or (gla_ and (re.search(r"ُ$", h2ns) or five or (re.search(r"[وي]$", hb2) and re.match(r"^[وف]?[أن]", h2))))):   # the written mood wins over the engine's where no governor stands before the verb (a defective verb's jussive ends in its vowel: لَمْ يَبْقَ، لَمْ أَعْفُ); لَا before a marfūʿ verb is the plain negation, not the prohibitive
                        wm_ = ("raf" if (five and re.search(r"(ُونَ|َوْنَ|ِينَ|َانِ)", h2ns)) else None) if five else ("raf" if re.search(r"ُ$", h2ns) else ("nasbVerb" if re.search(r"َ$", h2ns) and not re.search(r"َا$", h2ns) else ("jazm" if re.search(r"ْ$", h2ns) else ("raf" if re.search(r"[وي]$", hb2) and (gv_ is None or (gla_ and re.match(r"^[وف]?[أن]", h2))) else None))))
                        if wm_ and wm_ != mk: mk = wm_; report["reconciled"] += 1
                    passive = bool(re.match(r"^[ء-ي]ِي[ء-ي]َ$", h2)) or bool(re.match(r"^[ء-ي]ُ", h2)) and (tense in ("mazi",) and bool(re.search(r"ِ[ء-ي][ً-ٰ]*(?:تْ|وا|ا|تُ|نَا)?$|ِ[ء-ي]َ$", h2)) or (tense not in ("mazi", "amr") and bool(re.search(r"َ[ء-ي][ً-ٰ]*$|َ[ء-ي][َُِ]?(?:ون|ان|ين)?[ً-ٰ]*$", h2)) and not re.search(r"ِ[ء-ي][ً-ٰ]*$", h2)))
                    doer_ar = f"، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ {person}" if hidden and not re.search(r"ُوا$|[ّْ](تُ|تَ|تِ|نَا|تُمْ|تُنَّ)$|نَّا$", h2) and not enc or (hidden and enc) else ""
                    if passive: doer_ar = doer_ar.replace("وَالْفَاعِلُ", "وَنَائِبُ الْفَاعِلِ")
                    if hb2 == "قيل": doer_ar = "، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ بَعْدَهُ"
                    if tense == "mazi" or rule == "mazi":
                        if re.search(r"ُوا$", h2ns) or (enc and re.search(r"ُو$", h2ns) and len(hb2) >= 4): ar = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ"; en = "A past verb; the waw of the group is its doer"; tr = "Mâzî fiil; cemaat vâvı fâildir"
                        elif re.search(r"[ّْ](تُ|تَ|تِ|تُمْ|تُنَّ|نَا)$|نَّا$", h2): ar = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ رَفْعٍ مُتَحَرِّكٍ، وَالضَّمِيرُ فِي مَحَلِّ رَفْعٍ فَاعِلٌ"; en = "A past verb with its subject pronoun suffix as doer"; tr = "Mâzî fiil; bitişik ref zamiri fâildir"
                        elif re.search(r"َتْ$", h2) or re.search(r"َت$", h2): ar = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ" + doer_ar; en = "A past verb (feminine)" + ("; its doer is a hidden pronoun" if hidden else ""); tr = "Mâzî fiil (müennes)" + ("; fâili gizli zamirdir" if hidden else "")
                        elif re.search(r"َا$", h2) and len(hb2) >= 4 and not VERB_BY_LEMMA.get(h2[:-1] + "ى") and not VERB_BY_LEMMA.get(h2): ar = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ"; en = "A past verb; the alif of the dual is its doer"; tr = "Mâzî fiil; tesniye elifi fâildir"
                        else: ar = ("فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ" if passive else "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (" الْمُقَدَّرِ عَلَى الْأَلِفِ" if re.search(r"[ىا]$", hb2) and not re.search(r"َ$", h2) else "")) + doer_ar; en = ("A past verb in the passive" if passive else "A past verb") + ("; its doer is a hidden pronoun «" + person + "»" if hidden and not enc else ""); tr = ("Meçhul mâzî fiil" if passive else "Mâzî fiil") + ("; fâili gizli zamirdir «" + person + "»" if hidden and not enc else "")
                        tags = ["hollow-verbs"] if re.search(r"^[ء-ي]َا[ء-ي]$", h2) else []
                    elif tense == "amr" or rule == "amr":
                        sign = "حَذْفِ النُّونِ" if re.search(r"(وا|ي|ا)$", hb2) and len(hb2) >= 4 else ("حَذْفِ حَرْفِ الْعِلَّةِ" if not re.search(r"ْ$", h2) and not enc else "السُّكُونِ")
                        ar = f"فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى {sign}" + ("، وَالْوَاوُ فَاعِلٌ" if re.search(r"وا$", hb2) else "، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ أَنْتَ"); en = "An imperative; its doer is «you»"; tr = "Emir fiili; fâili «sen»"; tags = ["al-amr-wa-wujuhuh"]
                    else:
                        rule = mk
                        mood = {"raf": ("مَرْفُوعٌ", "in raf'", "merfû"), "nasbVerb": ("مَنْصُوبٌ", "in nasb", "mansûb"), "jazm": ("مَجْزُومٌ", "in jazm", "meczûm")}.get(rule, ("مَرْفُوعٌ", "in raf'", "merfû"))
                        gov = ""
                        if rule in ("nasbVerb", "jazm"):
                            for q in range(i - 1, max(-1, i - 4), -1):
                                qb = bare(words[q]["w"]).replace("أ", "ا").replace("إ", "ا")
                                if qb in ("ان", "لن", "كي", "حتى", "اذن", "لم", "لا", "لما", "ان", "من", "مهما", "اذا", "لو", "ولا", "ولم", "فلا", "فلم", "ولن", "فلن", "وان", "فان", "ولما"): gov = "بِـ«" + N(words[q]["w"]).replace("وَ", "", 1).replace("فَ", "", 1) + "»"; break
                            if not gov and pre == "ف" and rule == "nasbVerb": gov = "بِأَنْ مُضْمَرَةٍ بَعْدَ فَاءِ السَّبَبِيَّةِ"
                            if not gov and re.match(r"^[وف]?لِ", N(host_of(full, enc))) and rule == "nasbVerb": gov = "بِأَنْ مُضْمَرَةٍ بَعْدَ لَامِ التَّعْلِيلِ"
                            if not gov and re.match(r"^[وف]?لْ", N(host_of(full, enc))) and rule == "jazm": gov = "بِلَامِ الْأَمْرِ"
                        if five: sign = {"raf": "ثُبُوتُ النُّونِ", "nasbVerb": "حَذْفُ النُّونِ", "jazm": "حَذْفُ النُّونِ"}.get(rule, "ثُبُوتُ النُّونِ")
                        elif rule == "jazm": sign = ("السُّكُونُ، وَحُرِّكَ آخِرُهُ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ لِأَنَّهُ مُضَاعَفٌ" if re.search(r"ّ[َ]?$", h2) else ("السُّكُونُ، وَحُرِّكَ آخِرُهُ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ" if (re.search(r"ِ$", h2ns) and i + 1 < len(words) and re.match(r"^(ال|ا)", bare(words[i + 1]["w"])) and not re.search(r"[وي]ِ$", h2ns)) else ("السُّكُونُ" if re.search(r"ْ$", h2) or enc else "حَذْفُ حَرْفِ الْعِلَّةِ")))
                        elif re.search(r"[ىا]$", hb2): sign = ("الْفَتْحَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ" if rule == "nasbVerb" else "الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ")
                        elif re.search(r"[يو]$", hb2) and rule == "raf": sign = "الضَّمَّةُ الْمُقَدَّرَةُ عَلَى " + ("الْيَاءِ" if hb2.endswith("ي") else "الْوَاوِ") + " لِلثِّقَلِ"
                        else: sign = "الضَّمَّةُ الظَّاهِرَةُ" if rule == "raf" else "الْفَتْحَةُ الظَّاهِرَةُ"
                        doer2 = "" if five else doer_ar
                        if five: doer2 = "، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" if re.search(r"ون|وا", hb2) else ("، وَالْأَلِفُ فَاعِلٌ" if re.search(r"ان|ا$", hb2) else "، وَالْيَاءُ فَاعِلٌ")
                        ar = f"فِعْلٌ مُضَارِعٌ {'مَبْنِيٌّ لِلْمَجْهُولِ ' if passive else ''}{mood[0]} {gov}، وَعَلَامَةُ {'رَفْعِهِ' if rule == 'raf' else ('نَصْبِهِ' if rule == 'nasbVerb' else 'جَزْمِهِ')} {sign}{doer2}".replace("  ", " ").replace(" ،", "،")
                        en = f"A present verb{' in the passive' if passive else ''}, {mood[1]}" + (f" after {gov.replace('بِـ', '')}" if gov else "") + ("; its doer is a hidden pronoun «" + person + "»" if hidden and not five and not enc else ""); tr = f"Muzâri fiil{' (meçhul)' if passive else ''}, {mood[2]}" + ("; fâili gizli zamir «" + person + "»" if hidden and not five and not enc else "")
                        tags = ["nawasib-wa-jawazim-al-mudari"] if rule in ("nasbVerb", "jazm") else (["afal-khamsa"] if five else [])
                    if tense not in ("mazi", "amr") and rule not in ("mazi", "amr") and re.search(r"[^وي]ْنَ$", h2ns) and len(hb2) >= 4 and not enc and not fx.get("irab"):   # يَتَفَطَّرْنَ: the nūn of women builds the muḍāriʿ
                        ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ"; en = "A present verb built on sukūn because the nūn of women is attached; the nūn is its doer."; tr = "Nûn-i nisve bitiştiği için sükûn üzere mebnî muzâri fiil; nûn fâilidir."; tags = ["mabni-wa-murab"]; pre = ""
                    if KANA_RE.match(re.sub(r"^[وف]", "", bare(h2)) if len(bare(h2)) > 3 else bare(h2)) or KANA_RE.match(bare(h2)):   # كَانَ، لَيْسَ، كُنْتُمْ، يَكُونُونَ: the defective verb takes a noun and a predicate, not a doer
                        jam_ = "جَامِدٌ " if bare(h2).startswith("ليس") or bare(h2).startswith("لس") else ""
                        ar = ar.replace("فِعْلٌ مَاضٍ", f"فِعْلٌ مَاضٍ نَاقِصٌ {jam_}مِنْ أَخَوَاتِ كَانَ", 1).replace("فِعْلٌ مُضَارِعٌ", "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ", 1).replace("وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ", "وَاسْمُهَا ضَمِيرٌ مُسْتَتِرٌ").replace("فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "فِي مَحَلِّ رَفْعٍ اسْمُهَا").replace("وَالْوَاوُ فَاعِلٌ", "وَالْوَاوُ اسْمُهَا").replace("وَالتَّاءُ لِلتَّأْنِيثِ", "وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا الْمَرْفُوعُ بَعْدَهَا")
                        en = en.rstrip(".") + " — one of kāna's sisters: it raises its noun and puts its predicate in naṣb."; tr = tr.rstrip(".") + " — kâne'nin kardeşlerinden: ismini ref, haberini nasb eder."; tags = list(tags) + ["kana-wa-akhawatuha", "nawasikh"]
                    if enc:
                        ar += f"، وَ{ENC_AR.get(enc, 'الضَّمِيرُ')} ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ"; en += f"; the pronoun suffix {ENC_EN.get(enc, '')} is its object"; tr += f"; bitişik zamir {ENC_TR.get(enc, '')} mef'ûlün bihtir"; tags = tags + ["maful-bihi"]
                    if pre: ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else "الْفَاءُ عَاطِفَةٌ، وَ") + ar; en = ("The waw conjoins; " if pre == "و" else "The fa conjoins; ") + en[:1].lower() + en[1:]; tr = ("«ve» + " if pre == "و" else "«bunun üzerine» + ") + tr[:1].lower() + tr[1:]
                    ar = ar.rstrip("،") + "."; en = en + "."; tr = tr + "."
                    if not key: report["nokey"].append((where, b))
                    else: take(key, where)
                    if key and key in M and (OWNER_G.get(key) == OWNER_M.get(key) or key not in OWNER_G or key in MX): morph[key] = M[key]
                    elif key and key in M: report.setdefault("paradigmSkipped", []).append(key)
                    if pre or enc:
                        segs = []
                        if pre: segs.append({"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}); take("wa" if pre == "و" else "fa", where)
                        hostf = N(host_of(full, enc)); hostf = hostf[2:] if pre else hostf
                        segs.append({"form": hostf, "lex": key or "?", "pos": "verb"})
                        if enc: segs.append({"form": full[len(N(host_of(full, enc))):], "lex": ENC.get(enc, "?"), "pos": "pron"}); take(ENC.get(enc, "?"), where)
                    if key == "taala": ar = ar.rstrip(".") + " — جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ."; en = en.rstrip(".") + " — a parenthetical clause of exaltation."; tr = tr.rstrip(".") + " — ta'zîm için mu'teriza cümlesi."   # as the Kāfiya's lines read it
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": key or "?", "pos": "verb", **({"grammar": list(dict.fromkeys(t for t in tags if t in GIDS))} if tags else {}), "irab": {"ar": ar, "en": en, "tr": tr}, **({"segments": segs} if segs else {})})
                    continue
                # ---- nouns
                h = N(host_of(full, enc)); h2 = h[2:] if pre else h; hb2 = bare(h2)
                jc = ""
                lem_e = G.get(key) or next((e for e in LX.values() if e.get("key") == key and e.get("lemma")), None)
                lem_b = noal(bare(str((lem_e or {}).get("lemma", "")).split("(")[0].strip())) if lem_e else ""
                if rule == "jarr" and re.match(r"^[بل]ِ|^كَ", h2) and len(hb2) >= 3:
                    rest_b = noal(hb2[1:])
                    if (lem_b and rest_b == lem_b) or (lem_b and lem_b != noal(hb2) and len(hb2) >= 4 and not re.search(r"ً", h2)) or (not lem_b and len(hb2) >= 4 and not re.search(r"ً", h2)): jc = h2[0]
                cs = CASE_OF_RULE.get(rule) or ({"raf": "raf", "nasb": "nasb", "jarr": "jarr"}.get(k) if k in ("raf", "nasb", "jarr") else None)
                if rule == "kanaIsm" and re.search(r"ً[اى]?$", h2.replace("ّ", "")): rule = "kanaKhabar"; cs = "nasb"
                if rule == "innaKhabar" and re.search(r"ً[اى]?$", h2.replace("ّ", "")):
                    rule = "kanaKhabar" if any(re.sub(r"^[وف]", "", bare(x["w"])) in KANA_FAM for x in words[max(0, i - 3):i]) else "innaIsm"; cs = "nasb"
                hostn0 = h2[2:] if jc else h2
                if bare(hostn0).replace("آ", "ا") == "الان" and not enc and not fx.get("irab"):   # الْآنَ: the time adverb built on fatḥ
                    fx = dict(fx); fx["irab"] = {"ar": "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "en": "«now» — a time adverb built on fatḥa, in the seat of naṣb.", "tr": "«şimdi» — fetha üzere mebnî zaman zarfı, nasb mahallinde."}; fx["tags"] = ["mabni-wa-murab"]; cs = None; rule = "zarf"
                elif bare(hostn0) == "قط" and re.search(r"ُّ$", N(hostn0)) and not enc and not fx.get("irab"):
                    fx = dict(fx); fx["irab"] = {"ar": "«قَطُّ» ظَرْفٌ لِاسْتِغْرَاقِ الزَّمَانِ الْمَاضِي مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "en": "«ever (in the past)» — an adverb covering the whole past, built on ḍamma, in the seat of naṣb.", "tr": "«asla / hiç» — geçmiş zamanın tamamını kaplayan zarf, zamme üzere mebnî, nasb mahallinde."}
                    fx["tags"] = ["mabni-wa-murab"]; cs = None; rule = "zarf"
                elif bare(hostn0) in MABNI_ZARF and re.search(r"ُ$", N(hostn0)) and not enc and not fx.get("irab") and not (i + 1 < len(words) and words[i + 1].get("rule") == "mudafIlayh"):   # أَمَّا بَعْدُ، فَحَسْبُ: cut from its annexation, built on ḍamm
                    zk_ = MABNI_ZARF[bare(hostn0)]; seat_ = "فِي مَحَلِّ رَفْعٍ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ" if bare(hostn0) == "حسب" else "فِي مَحَلِّ نَصْبٍ"
                    fx = dict(fx); fx["irab"] = {"ar": f"{zk_} مَبْنِيٌّ عَلَى الضَّمِّ لِقَطْعِهِ عَنِ الْإِضَافَةِ {seat_}.", "en": ("«enough» — built on ḍamma, cut from its annexation; in the seat of rafʿ as the predicate of an omitted subject." if bare(hostn0) == "حسب" else "An adverb built on ḍamma, cut from its annexation (its annexed noun is understood); in the seat of naṣb."), "tr": ("«yeter» — izâfetten kesildiği için zamme üzere mebnî; hazfedilmiş mübtedânın haberi olarak ref mahallinde." if bare(hostn0) == "حسب" else "İzâfetten kesildiği için zamme üzere mebnî zarf; nasb mahallinde.")}
                    fx["tags"] = ["mabni-wa-murab"]; cs = None; rule = "zarf"
                else:
                    pb1_ = bare(words[i - 1]["w"]).replace("أ", "ا").replace("إ", "ا") if i else ""; pb1_ = re.sub(r"^[وف]", "", pb1_) if len(pb1_) > 3 else pb1_
                    pwc_ = "jarr" if (pb1_ in PREPS or (i and is_noun_w(words[i - 1]) and wc_word(words, i - 1, 0) == "jarr")) else ("verb" if i and is_verb_w(words[i - 1]) else None)
                    wc = written_case(hostn0, enc, cs, lem_b if lem_b else None, (lem_e or {}).get("lemma") if lem_e else None, propn=(pos == "propn" or (lem_e or {}).get("pos") == "propn"), prev_wc=pwc_)
                    if wc == "nasb-jarr":
                        pvb_ = re.sub(r"^[وف]", "", bare(words[i - 1]["w"])).replace("إ", "ا") if i else ""
                        wc = "jarr" if (pvb_ in ("من", "عن", "الى", "على", "في", "ب", "ل", "ك", "مع", "حتى", "عند", "بعد", "قبل", "بين", "لدى", "منذ", "مذ") or (i and words[i - 1].get("kind") == "particle" and words[i - 1].get("rule") == "jarr")) else "nasb"
                        if wc == "nasb" and (lem_b in ("مائة", "الف", "مئة") or (re.fullmatch(r"(عشر|ثلاث|اربع|خمس|ست|سبع|ثمان|تسع)ين", noal(bare(hostn0))) and not (i and is_noun_w(words[i - 1]) and not bare(words[i - 1]["w"]).startswith("ال") and re.search(r"[َُِ]$", N(host_written(words, i - 1)).replace("ّ", ""))))) and i + 1 < len(words) and noal(bare(str(words[i + 1].get("lemma") or "").split("(")[0])) in ("سنة", "يوم", "عام", "شهر", "ليلة", "ساعة", "مرة", "حجة"): fx = dict(fx); fx["rule"] = "zarf"; rule = "zarf"; cs = "nasb"   # (patch 32) سَبْعِينَ سَنَةً: the decade before a time noun is a ẕarf like مائة
                    if wc == "jarr" and pb1_ in ("يا", "اي", "ايا", "هيا") and not enc and re.search(r"ِ$", N(hostn0).replace("ّ", "")) and not fx.get("irab"):   # يَا رَبِّ: the vocative annexed to the speaker's dropped yāʾ
                        fx = dict(fx); fx["irab"] = {"ar": "مُنَادَى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْكَسْرَةُ دَلِيلُ الْيَاءِ.", "en": "A vocative annexed to the speaker's dropped yāʾ («my Lord»); in naṣb by an understood fatḥa, the kasra standing for the yāʾ.", "tr": "Hazfedilmiş mütekellim yâ'sına muzâf münâdâ («Rabbim»); takdîrî fetha ile mansûb, kesre yâ'nın delili."}; fx["tags"] = ["al-munada"]; rule = "munada"; cs = "nasb"; wc = None
                    if wc and not fx.get("rule") and not fx.get("k") and (cs or rule in (None, "", "fail")) and wc != cs and not (not cs and bare(hostn0).replace("آ", "ا") in ("حيث", "اين", "كيف", "الان", "امس", "متى", "هنا", "هناك", "ثم", "منذ", "مذ")):
                        r0_ = rule; rule, cs = reconcile(rule, cs, wc, words, i, pauses, hostn0, pre); report["reconciled"] += 1
                        words[i] = dict(words[i], rule=rule, k=cs)
                        if os.environ.get("PKG_DEBUG") and where in os.environ["PKG_DEBUG"].split(","): print("DEBUG", where, full, "rule", r0_, "->", rule, "wc", wc, "pre", repr(pre), "lem_b", lem_b, "prev", [(words[q]["w"], words[q].get("kind"), words[q].get("rule")) for q in range(max(0, i - 4), i)], "pauses", pauses[max(0, i - 4):i])
                r_ar, r_en, r_tr, tags = ROLE.get(rule, ("", "", "", []))
                if rule in ("atf", "nat", "badal", "tawkid") and cs: r_ar = r_ar + " " + {"raf": "مَرْفُوعٌ", "nasb": "مَنْصُوبٌ", "jarr": "مَجْرُورٌ"}[cs]
                if rule == "jarr" and i > 0 and not jc: r_ar = "مَجْرُورٌ بِـ«" + N(words[i - 1]["w"]) + "»"
                hostn = h2[2:] if jc else h2
                if jc == "ل" and h2.startswith("لِلْ"): hostn = "ا" + hostn   # لِلْمُؤْمِنِينَ: the article's alif returns for the shape
                sh = shape(hostn, cs, enc, pos, "al" if bare(hostn).startswith("ال") else "")
                hn_b = noal(bare(hostn))
                lam_ib_ = bool(lem_b and rule in ("innaKhabar", "khabar") and N(hostn).startswith("لَ") and not lem_b.startswith("ل") and (hn_b[1:] == lem_b or hn_b[1:] in (lem_b + "ون", lem_b + "ين", lem_b + "ان", lem_b + "ي", lem_b + "و") or (lem_b.endswith("ة") and hn_b[1:] in (lem_b[:-1] + "ت", lem_b[:-1] + "ات", lem_b[:-1] + "تان", lem_b[:-1] + "تين"))))   # (patch 32) the muzaḥlaqa lām
                if lam_ib_ and hn_b[1:] == lem_b: hn_b = hn_b[1:]
                if lem_b and re.match(r"^[لأ]َ[ء-ي]", N(hostn)) and hn_b[1:] in (lem_b + "ون", lem_b + "ين", lem_b + "ان", lem_b + "ي", lem_b + "و") and len(hn_b) >= 6: hn_b = hn_b[1:]   # لَكَاذِبُونَ، أَمُرْسَلِينَ: the muzaḥlaqa lām / the question hamza
                if os.environ.get("PKG_DEBUG") and where in os.environ["PKG_DEBUG"].split(","): print("SHAPE?", where, full, "hostn", hostn, "sh", sh, "cs", cs, "lem_b", lem_b, "hn_b", hn_b, "pos", pos, "pre", repr(pre), "jc", repr(jc))
                lem_pl = lem_b and re.search(r"(ون|ين)$", lem_b) and hn_b in (lem_b, lem_b[:-2] + "ون", lem_b[:-2] + "ين") and not re.search(r"َيْن[ً-ْ]*$", N(str((lem_e or {}).get("lemma", "")).split("(")[0].strip()))   # عَيْن، غَيْن، بَيْن، دَيْن: the yāʾ and nūn are radicals, no plural's ending
                def _of_lemma(hb_, lb_):
                    """hb_ is a dual/plural form of the lemma lb_: the bare stem before ـان/ـين/ـون/ـي/ـو/ـا, allowing the feminine ـت and the manqūṣ ـي"""
                    if not lb_: return False
                    st_ = re.sub(r"(ان|ين|ون|ي|و|ا)$", "", hb_); lb0_ = lb_[:-1] if lb_.endswith("ة") else lb_
                    return st_ in (lb_, lb0_, lb0_ + "ت", lb_ + "ت", lb0_ + "يت", lb_ + "يت", lb_ + "ي") and len(st_) >= 2
                if lem_b and (lem_e or {}).get("lemma") and re.search(r"(َانِ|َيْنِ)$", N(str((lem_e or {}).get("lemma")).split("(")[0].strip())) and hn_b == lem_b and sh == "muthanna": lem_b = None   # اللَّذَانِ: a dual-shaped lemma keeps the dual's signs
                if sh in ("muthanna", "jam-m") and lem_b and not lem_pl and hn_b not in ("بنو", "بني", "كلا", "كلتا", "كلي", "كلتي") and not _of_lemma(hn_b, lem_b) and not (hn_b in (lem_b + "ان", lem_b + "ين", lem_b + "ون", lem_b + "ي", lem_b + "و", lem_b + "ا") or (lem_b.endswith("ة") and hn_b in (lem_b[:-1] + "تان", lem_b[:-1] + "تين", lem_b[:-1] + "تي", lem_b[:-1] + "تا")) or (lem_b.endswith("ى") and hn_b in (lem_b[:-1] + "يان", lem_b[:-1] + "يين"))): sh = "sahih"
                if sh == "sahih" and lem_b and (hn_b in (lem_b + "ان", lem_b + "ين") or (lem_b.endswith("ة") and hn_b in (lem_b[:-1] + "تان", lem_b[:-1] + "تين", lem_b[:-1] + "تي", lem_b[:-1] + "تا"))) and re.search(r"(َانِ|َيْنِ)$", hostn): sh = "muthanna"
                if sh == "sahih" and lem_b and (hn_b in (lem_b + "ون", lem_b + "ين") or lem_pl) and re.search(r"(ُونَ|ِينَ)$", hostn): sh = "jam-m"
                if os.environ.get("PKG_DEBUG") and where in os.environ["PKG_DEBUG"].split(","): print("LAJINS?", where, full, "cs", cs, "rule", rule, "prev", bare(words[i - 1]["w"]) if i else None, "enc", repr(enc))
                la_jins = (not cs or (cs == "nasb" and rule in ("maful", "hal", "zarf"))) and i > 0 and re.sub(r"^[وف]", "", bare(words[i - 1]["w"])) == "لا" and not enc and not bare(h2).startswith("ال") and re.search(r"َ$", N(h2).replace("ّ", "")) and not re.search(r"[ًٌٍ]", N(h2)) and not re.search(r"(ُونَ|ِينَ|َانِ|َوْنَ)$", N(h2).replace("ّ", "")) and not (re.match(r"^[يتأن][َُ]", N(h2).replace("ّ", "")) and len(bare(h2)) >= 4 and (G.get(key) or {}).get("pos") != "noun")
                if la_jins:
                    cs = "nasb"; ar = "اسْمُ «لَا» النَّافِيَةِ لِلْجِنْسِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ"; en = "the noun of «la» of absolute negation — built on fatha, in the place of nasb"; tr = "cinsini nefyeden «lâ»nın ismi — fetha üzere mebnî, mahallen mansûb"; sign_ar = sign_en = sign_tr = ""; tags = list(tags) + ["la-nafiya-lil-jins"]
                elif not cs and not enc and noal(bare(hostn)).replace("أ", "ا").replace("إ", "ا") in ("ابي", "اخي", "حمي", "اولو", "اولي", "حيث"):   # (patch 32) the five nouns and أُولُو read their case off the yāʾ/wāw and the word before; حَيْثُ is a mabnī ẕarf
                    hb5_ = noal(bare(hostn)).replace("أ", "ا").replace("إ", "ا"); pv5_ = re.sub(r"^[وف]", "", bare(words[i - 1]["w"])).replace("إ", "ا") if i else ""
                    pvj5_ = i > 0 and (pv5_ in ("من", "عن", "الى", "على", "في", "ب", "ل", "ك", "مع", "حتى", "عند", "بعد", "قبل", "بين", "لدى", "منذ", "مذ") or (words[i - 1].get("kind") == "particle" and words[i - 1].get("rule") == "jarr"))
                    pvn5_ = i > 0 and is_noun_w(words[i - 1]) and not bare(words[i - 1]["w"]).startswith("ال") and re.search(r"[َُِ]$", N(host_written(words, i - 1)).replace("ّ", "")) and not re.search(r"[ًٌٍ]", N(words[i - 1]["w"]))
                    sign_ar = sign_en = sign_tr = ""
                    if hb5_ == "حيث": cs = "nasb"; ar = "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ"; en = "an adverb of place built on the ḍamma, in the place of naṣb"; tr = "zamme üzere mebnî mekân zarfı, nasb mahallinde"
                    elif hb5_ in ("اولو",): cs = "raf"; rule = "fail" if (i and is_verb_w(words[i - 1])) else rule; ar = ("فَاعِلٌ " if rule == "fail" else "مُبْتَدَأٌ ") + "مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ"; en = ("The doer" if rule == "fail" else "The mubtada") + ", in raf' by the wāw — it follows the sound masculine plural"; tr = ("Fâil" if rule == "fail" else "Mübtedâ") + ", vâv ile merfû — cem-i müzekker sâlime mülhak"
                    elif hb5_ == "اولي": cs = "jarr" if pvj5_ or pvn5_ else "nasb"; ar = ("مَجْرُورٌ" if cs == "jarr" else "مَفْعُولٌ بِهِ مَنْصُوبٌ") + " بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ"; en = ("In jarr" if cs == "jarr" else "The object, in nasb") + " by the yāʾ — it follows the sound masculine plural"; tr = ("Mecrûr" if cs == "jarr" else "Mef'ûl, mansûb") + ", yâ ile — cem-i müzekker sâlime mülhak"
                    elif pvj5_: cs = "jarr"; rule = "jarr"; ar = "مَجْرُورٌ بِـ«" + N(words[i - 1]["w"]) + "» بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ"; en = "In jarr after the preposition, by the yāʾ — one of the five nouns"; tr = "Harf-i cerden sonra mecrûr, yâ ile — esmâ-i hamseden"
                    elif pvn5_ or (i and words[i - 1].get("rule") in ("mudafIlayh", "jarr", "nat", "badal", "atf") and not re.search(r"[ًٌٍ]", N(words[i - 1]["w"]))): cs = "jarr"; rule = "mudafIlayh"; ar = "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ"; en = "The annexed noun, in jarr by the yāʾ — one of the five nouns"; tr = "Muzâfun ileyh, yâ ile mecrûr — esmâ-i hamseden"
                    else: cs = "jarr"; ar = "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ"; en = "In jarr by the yāʾ — one of the five nouns"; tr = "Yâ ile mecrûr — esmâ-i hamseden"
                elif not cs: 
                    ar = "اسْمٌ"; en = "a noun"; tr = "isim"; sign_ar = sign_en = sign_tr = ""
                    if rule == "fail" and k is None: pass
                else:
                    sign_ar, sign_en, sign_tr = SIGN.get((cs, sh), SIGN[(cs, "sahih")])
                    ar = f"{r_ar} {sign_ar}"; en = f"{r_en}; the sign is {sign_en}"; tr = f"{r_tr}; alâmeti {sign_tr}"
                    if lam_ib_: ar = "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ إِلَى الْخَبَرِ، وَ" + ar; en = "the lām of emphasis displaced onto the khabar + " + en; tr = "habere kaydırılmış te'kîd lâmı + " + tr
                    tags = list(tags) + SHAPE_TAG.get(sh, [])
                if jc:
                    JN = {"ب": ("الْبَاءُ", "bi"), "ل": ("اللَّامُ", "li"), "ك": ("الْكَافُ", "ka")}[jc]
                    ar = f"{JN[0]} حَرْفُ جَرٍّ، وَ" + ar.replace("مَجْرُورٌ", "مَجْرُورٌ بِهِ", 1) if "مَجْرُورٌ" in ar else f"{JN[0]} حَرْفُ جَرٍّ، وَالِاسْمُ مَجْرُورٌ {sign_ar}"
                    en = "preposition + noun: " + en; tr = "harf-i cer + isim: " + tr; tags = tags + ["huruf-jarr"]
                if enc:
                    ar += f"، وَهُوَ مُضَافٌ، وَ{ENC_AR.get(enc, 'الضَّمِيرُ')} ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ"; en += f"; annexed, the pronoun {ENC_EN.get(enc, '')} is the mudaf ilayh"; tr += f"; muzâf, zamir {ENC_TR.get(enc, '')} muzâfun ileyh"; tags = tags + ["idafa-definiteness"]
                elif i + 1 < len(words) and re.match(r"^(?:[وف]َ)?أَن[َّْ]", N(words[i + 1]["w"])) and not enc and pos not in ("propn", "pron", "adv") and not bare(hostn).startswith("ال") and not re.search(r"[ًٌٍ]", h2) and re.search(r"[َُِ]$", N(hostn).replace("ّ", "")) and rule not in ("khabar", "mubtada", "innaIsm", "kanaIsm", "innaKhabar", "kanaKhabar", "fail", "naib", "hal", "tamyiz", "mafulMutlaq", "mafulLah"):
                    ar += "، مُضَافٌ إِلَى الْمَصْدَرِ الْمُؤَوَّلِ بَعْدَهُ"; en += "; annexed to the maṣdar clause that follows"; tr += "; sonraki masdar-ı müevvele muzâf"; tags = tags + ["idafa-definiteness"]   # (patch 32)
                elif i + 1 < len(words) and words[i + 1].get("rule") == "mudafIlayh" and words[i + 1].get("head") in (i, None) and not bare(h2).startswith("ال") and not re.search(r"[ًٌٍ]", h2):
                    ar += "، مُضَافٌ"; en += "; annexed (mudaf)"; tr += "; muzâf"; tags = tags + ["idafa-definiteness"]
                if pre: ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else "الْفَاءُ عَاطِفَةٌ، وَ") + ar; en = ("The waw conjoins; " if pre == "و" else "The fa conjoins; ") + en[:1].lower() + en[1:]; tr = ("«ve» + " if pre == "و" else "«bunun üzerine» + ") + tr[:1].lower() + tr[1:]
                ar = ar.rstrip("،") + "."; en = en + "."; tr = tr + "."
                if key: take(key, where)
                else: report["nokey"].append((where, b))
                if pre or enc or jc:
                    segs = []
                    if pre: segs.append({"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}); take("wa" if pre == "و" else "fa", where)
                    if jc: segs.append({"form": h2[:2], "lex": {"ب": "bi", "ل": "li", "ك": "ka"}[jc], "pos": "prep"}); take({"ب": "bi", "ل": "li", "ك": "ka"}[jc], where)
                    segs.append({"form": hostn, "lex": key or "?", "pos": pos or "noun"})
                    if enc: segs.append({"form": full[len(h):], "lex": ENC.get(enc, "?"), "pos": "pron"}); take(ENC.get(enc, "?"), where)
                if fx.get("irab"): ar, en, tr = fx["irab"]["ar"], fx["irab"]["en"], fx["irab"]["tr"]; tags = list(tags) + list(fx.get("tags", []))
                toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": key or "?", "pos": (pos if pos in ("noun", "propn", "adj", "pron", "adv") else "noun"), **({"grammar": list(dict.fromkeys(t for t in tags if t in GIDS))} if tags else {}), "irab": {"ar": ar, "en": en, "tr": tr}, **({"segments": segs} if segs else {})})
            for i, t in enumerate(toks):   # (wave 165) the quoted pattern-word: the Iẓhār's own wording for a word mentioned, by the seat the page shows
                if f"{where0}:{i}" not in CITE: continue
                fw = N(t["surface"]["full"]); pb = re.sub(r"^[وف]", "", bare(toks[i - 1]["surface"]["full"])) if i else ""
                waw = bool(re.match(r"^[وف]\u064e", fw)) and len(bare(fw)) > 3 and not re.match(r"^فَ[عا]", fw)
                core_ = fw[2:] if waw else fw; kaf = bool(re.match(r"^ك\u064e", core_)); ba = bool(re.match(r"^[بل]\u0650", core_))
                if waw: ar, en, tr = "الْوَاوُ عَاطِفَةٌ، وَالْمَعْطُوفُ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ.", "«and …» — the word itself is quoted, joined to what precedes.", "«ve …» — kelimenin kendisi kastedilmiştir (hikâye), öncekine atfedilmiştir."
                elif kaf: ar, en, tr = "الْكَافُ لِلتَّمْثِيلِ، وَمَا بَعْدَهَا لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ.", "«like …» — the word itself is quoted, in the place of jarr.", "«… gibi» — kelimenin kendisi kastedilmiştir (hikâye), cer mahallinde."
                elif ba: ar, en, tr = "حَرْفُ جَرٍّ، وَمَا بَعْدَهُ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ.", "a jarr letter, and after it the word itself is quoted, in the place of jarr.", "cer harfi; sonrasında kelimenin kendisi kastedilmiştir (hikâye), cer mahallinde."
                elif pb in ("وزن", "مثال", "نحو", "مثل", "بناء", "لفظ"): ar, en, tr = "مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ.", "the word itself is quoted; it sits in the place of jarr as mudaf ilayh.", "kelimenin kendisi kastedilmiştir (hikâye); muzâfun ileyh olarak cer mahallinde."
                elif pb in ("على", "من", "في", "الى", "إلى", "عن"): ar, en, tr = "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ.", "the word itself is quoted; it sits in the place of jarr.", "kelimenin kendisi kastedilmiştir (hikâye); cer mahallinde."
                else: ar, en, tr = "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ.", "the word itself is quoted.", "kelimenin kendisi kastedilmiştir (hikâye)."
                t["irab"] = {"ar": ar, "en": en, "tr": tr}; t["pos"] = "noun"; t.pop("grammar", None)
                if t.get("segments"):
                    for sg in t["segments"]:
                        if sg.get("lex") == t["lex"]: sg["pos"] = "noun"
            for ti_, t_ in enumerate(toks):   # (wave 165) a sister of kāna whose noun is written keeps no hidden one beside it; and no line ends on two full stops
                ir_ = t_.get("irab") or {}
                if "وَاسْمُهَا ضَمِيرٌ مُسْتَتِرٌ" in ir_.get("ar", "") and any("اسْمُ كَانَ" in (x_.get("irab") or {}).get("ar", "") for x_ in toks[ti_ + 1:ti_ + 4]):
                    ir_["ar"] = re.sub(r"، وَاسْمُهَا ضَمِيرٌ مُسْتَتِرٌ(?: وُجُوبًا| جَوَازًا)? تَقْدِيرُهُ [^،.]+", "", ir_["ar"])
                    if isinstance(ir_.get("en"), str): ir_["en"] = re.sub(r"; its (?:doer|noun) is a hidden pronoun «[^»]+»", "", ir_["en"])
                    if isinstance(ir_.get("tr"), str): ir_["tr"] = re.sub(r"; (?:fâili|ismi) gizli zamir(?:dir)? «[^»]+»", "", ir_["tr"])
                for k_ in ("ar", "en", "tr"):
                    if isinstance(ir_.get(k_), str) and ir_[k_].endswith(".."): ir_[k_] = ir_[k_][:-1]
            if meta.get("cellLines"):   # (wave 165) a recited paradigm row: each cell's line from its place in the stored paradigm (tools/authoring/cell_lines.py)
                import cell_lines as CL
                def vhost_(t):
                    f = N(t["surface"]["full"]); sg = t.get("segments") or []
                    if M.get(t.get("lex")) and CL.candidates(M[t["lex"]], f):
                        if sg and sg[0].get("lex") in ("wa", "fa"): t.pop("segments", None)
                    elif sg and sg[0].get("lex") in ("wa", "fa"): f = f[len(N(sg[0]["form"])):]
                    elif re.match(r"^و\u064e", f) and len(bare(f)) > 3 and not (M.get(t.get("lex")) and CL.candidates(M[t["lex"]], f)): f = f[2:]
                    return f
                PARTS_ = {"لم", "لن", "لا", "ما"}
                def mk_(t, key):
                    h = vhost_(t); e = M.get(key); gov = ""; cs = CL.candidates(e, h) if e else []
                    if e and not cs and re.match(r"^ل\u0650[يتنأ]", h):
                        cs = [c for c in CL.candidates(e, h[2:]) if c[0] == "mudari" and c[2] == "jazm"]
                        if cs or CL.tawkid_line(h[2:], "ل"): h = h[2:]; gov = "ل"
                    return {"h": h, "e": e, "cs": cs, "gov": gov, "key": key}
                def hosts_(f):
                    out = [f]
                    if re.match(r"^[وف]\u064e", f): out.append(f[2:])
                    for h in list(out):
                        if re.match(r"^س\u064e|^ل[\u064e\u0650]", h): out.append(h[2:])
                    return out
                for i, t in enumerate(toks):   # a verb cell filed under a homograph lemma (تَقُولُ under تَقَوَّلَ): exactly one other paradigm owns the written form
                    k0 = t.get("lex")
                    if t.get("pos") != "verb" or k0 not in M or f"{where0}:{i}" in CITE or FX.get(f"{where0}:{i}", {}).get("key"): continue
                    hs = hosts_(N(t["surface"]["full"]))
                    if any(CL.candidates(M[k0], h) for h in hs): continue
                    own = [k for k, e in M.items() if k != k0 and any(CL.candidates(e, h) for h in hs)]
                    if len(own) == 1 and take(own[0], f"{where0}:{i}"):
                        t["lex"] = own[0]
                        for sg in (t.get("segments") or []):
                            if sg.get("lex") == k0: sg["lex"] = own[0]
                        report.setdefault("cellRekey", []).append(f"{where0}:{i} {k0}->{own[0]}")
                info = []
                for i, t in enumerate(toks):
                    if f"{where0}:{i}" in CITE or FX.get(f"{where0}:{i}", {}).get("irab") or isinstance(FX.get(f"{where0}:{i}", {}).get("note"), dict): info.append(None); continue
                    info.append(mk_(t, t.get("lex")))
                def prev_part(i):
                    j = i - 1
                    if j >= 0 and re.sub(r"^[وف]", "", bare(toks[j]["surface"]["full"])) in PARTS_ | {"اما", "إما"}: return re.sub(r"^[وف]", "", bare(toks[j]["surface"]["full"])).replace("إ", "ا")
                    return ""
                i = 0
                while i < len(toks):
                    a_ = info[i]
                    if not a_ or not a_["e"]: i += 1; continue
                    run = [i]; j = i + 1
                    while j < len(toks):
                        if info[j] and info[j]["key"] == a_["key"]: run.append(j); j += 1
                        elif info[j] and len(run) >= 2 and mk_(toks[j], a_["key"])["cs"]:   # a cell of the SAME verb that a homograph lemma had claimed (تَنْصُرْ → نَصَرَ, not تَنَصَّرَ)
                            info[j] = mk_(toks[j], a_["key"]); old_ = toks[j].get("lex"); toks[j]["lex"] = a_["key"]; take(a_["key"], f"{where0}:{j}")
                            for sg in (toks[j].get("segments") or []):
                                if sg.get("lex") == old_: sg["lex"] = a_["key"]
                            report.setdefault("cellRekey", []).append(f"{where0}:{j} {old_}->{a_['key']}"); run.append(j); j += 1
                        elif re.sub(r"^[وف]", "", bare(toks[j]["surface"]["full"])) in PARTS_ and j + 1 < len(toks) and info[j + 1] and info[j + 1]["key"] == a_["key"]: j += 1
                        else: break
                    if len(run) >= 2:
                        prev = -1; ptense = None
                        la_jazm = any(prev_part(q) == "لا" and ((info[q]["cs"] and any(c[0] == "mudari" and c[2] == "jazm" for c in info[q]["cs"]) and not any(c[0] == "mudari" and c[2] == "raf" for c in info[q]["cs"])) or (not info[q]["cs"] and CL.tawkid_line(info[q]["h"], "لا"))) for q in run)   # one cell of the row is visibly forbidden (لَا يَنْصُرْ، لَا تُرِيَنَّ): the whole row is the prohibition
                        for q in run:
                            x = info[q]; pp = x["gov"] or prev_part(q); want = {"لم": "jazm", "ل": "jazm", "لن": "nasb", "اما": "jazm"}.get(pp) or ("jazm" if pp == "لا" and la_jazm else None)
                            if pp == "لا" and la_jazm and q > 0 and not FX.get(f"{where0}:{q - 1}", {}).get("irab"):
                                tl = toks[q - 1]; wl_ = bool(re.match(r"^و\u064e", N(tl["surface"]["full"])))
                                tl["irab"] = {"ar": ("الْوَاوُ عَاطِفَةٌ، وَ" if wl_ else "") + "«لَا» النَّاهِيَةُ: حَرْفُ نَهْيٍ وَجَزْمٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "en": ("«and» + " if wl_ else "") + "«do not» — the prohibitive la, it puts the verb in jazm.", "tr": ("«ve» + " if wl_ else "") + "«-me» — nehiy lâ'sı, fiili cezmeder."}
                                old_ = tl.get("lex"); tl["lex"] = "la-nahiya"; tl["grammar"] = ["la-nahiya"]; take("la-nahiya", f"{where0}:{q - 1}")
                                for sg in (tl.get("segments") or []):
                                    if sg.get("lex") == old_: sg["lex"] = "la-nahiya"
                            cs = x["cs"]; ln = None
                            if cs:
                                pool = [c for c in cs if (c[0] != "mudari" or (want and c[2] == want) or (not want and (c[2] == ("jazm" if pp == "لا" and any(k[2] == "jazm" and k[2] != "raf" for k in cs) and not any(k[2] == "raf" for k in cs) else "raf"))))] or cs
                                same = [c for c in pool if c[0] == ptense] or pool
                                nxt = [c for c in same if c[1] > prev] or same
                                c = min(nxt, key=lambda c: c[1]); prev, ptense = c[1], c[0]
                                gv = pp if (c[0] == "mudari" and c[2] in ("jazm", "nasb") and pp in ("لم", "لن", "لا", "ل", "اما")) else ""
                                ln = CL.line(x["e"], c[0], c[1], c[2], gv)
                            else:
                                ln = CL.tawkid_line(x["h"], pp if pp in ("لا", "ل", "اما") else "")
                                if not ln: ln = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ.", "the word itself is quoted.", "kelimenin kendisi kastedilmiştir (hikâye).")
                                else: prev, ptense = -1, None
                            t = toks[q]; pre_ = N(t["surface"]["full"])[:2] if N(t["surface"]["full"]) != x["h"] and re.match(r"^[وف]\u064e", N(t["surface"]["full"])) else ""
                            ar, en, tr = ln
                            if pre_: ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre_[0] == "و" else "الْفَاءُ عَاطِفَةٌ، وَ") + ar; en = ("The waw conjoins; " if pre_[0] == "و" else "The fa conjoins; ") + en[:1].lower() + en[1:]; tr = ("«ve» + " if pre_[0] == "و" else "«bunun üzerine» + ") + tr[:1].lower() + tr[1:]
                            if x["gov"] == "ل": ar = "اللَّامُ لَامُ الْأَمْرِ، وَ" + ar; en = "The lām is the lām of command; " + en[:1].lower() + en[1:]; tr = "Lâm emir lâmıdır; " + tr[:1].lower() + tr[1:]
                            quoted = "مَحْكِيٌّ" in ln[0]
                            t["irab"] = {"ar": ar, "en": en, "tr": tr}; t["pos"] = "noun" if quoted else "verb"; t.pop("grammar", None); report["cells"] = report.get("cells", 0) + 1
                            for sg in (t.get("segments") or []):
                                if sg.get("lex") == t["lex"]: sg["pos"] = t["pos"]
                    i = run[-1] + 1
                # a same-word row of nouns (نَاصِرٌ نَاصِرَانِ نَاصِرُونَ …): each is the word itself, quoted
                i = 0
                while i < len(toks):
                    j = i
                    while j + 1 < len(toks) and toks[j + 1].get("lex") == toks[i].get("lex") and toks[i].get("lex") not in M: j += 1
                    if j - i >= 2 and toks[i].get("pos") != "part":
                        for q in range(i, j + 1):
                            if f"{where0}:{q}" in CITE: continue
                            w_ = bool(re.match(r"^و\u064e", N(toks[q]["surface"]["full"]))) and bool(toks[q].get("segments"))
                            toks[q]["irab"] = ({"ar": "الْوَاوُ عَاطِفَةٌ، وَالْمَعْطُوفُ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ.", "en": "«and …» — the word itself is quoted, joined to what precedes.", "tr": "«ve …» — kelimenin kendisi kastedilmiştir (hikâye), öncekine atfedilmiştir."} if w_ else
                                               {"ar": "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ.", "en": "the word itself is quoted.", "tr": "kelimenin kendisi kastedilmiştir (hikâye)."})
                            toks[q].pop("grammar", None); report["cells"] = report.get("cells", 0) + 1
                    i = j + 1
            for i, t in enumerate(toks):
                nt = FX.get(f"{where0}:{i}", {}).get("note")
                if isinstance(nt, dict) and "ar" in nt: t["irab"] = {"ar": nt["ar"], "en": nt["en"], "tr": nt.get("tr", nt["en"])}; report["fixed"] += 1
            # punctuation from the source text
            src_words = [x for x in s["text"].split() if x]
            if len(src_words) == len(toks):
                for sw, t in zip(src_words, toks):
                    m = re.search(r"([،:؛.؟])$", sw)
                    if m: t["punctAfter"] = m.group(1)
            tr_ = TR.get(where0, {})
            # a fixes row's iʿrāb overrides whatever branch wrote the token's line (verbs and particles too)
            for i2, t in enumerate(toks):
                fx2 = FX.get(f"{where0}:{i2}", {}) if len(toks) == len(words) else {}
                if fx2.get("irab"): t["irab"] = {kk: fx2["irab"].get(kk, (t.get("irab") or {}).get(kk, "")) for kk in ("ar", "en", "tr")}
            name_khabar(toks, raw_toks if aligned else None, report)   # (patch 32)
            name_sila(toks, raw_toks if aligned else None, report)   # (patch 32)
            for t_ in toks:
                if (t_.get("pos") in ("noun", "propn")) and "مَمْنُوعٌ مِنَ الصَّرْفِ" in (t_.get("irab") or {}).get("ar", "") and "mamnu-min-sarf" in GIDS and "mamnu-min-sarf" not in t_.get("grammar", []): t_["grammar"] = list(t_.get("grammar", [])) + ["mamnu-min-sarf"]
            sents.append({"id": sid, **({"page": s.get("page")} if s.get("page") else {}), "translation": {"en": tr_.get("en", ""), "tr": tr_.get("tr", "")}, "tokens": toks})
        chapters_out.append({"n": ch["n"], "title_ar": ch["title"], "sentences": sents})
    # ---- write the package
    man = {"id": meta["id"], "storyGroup": meta.get("storyGroup", meta["id"]), "title": meta["title"], "subtitle": meta.get("subtitle", meta["title"]), "level": meta["level"], "levelName": meta.get("levelName", "Advanced"), "access": meta.get("access", "premium"), "published": meta.get("published", datetime.date.today().isoformat()), "version": meta.get("version", "0.1.0"),
           "chapters": [{"n": c["n"], "title": {"ar": c["title_ar"], **meta.get("chapterTitles", {}).get(str(c["n"]), {"en": c["title_ar"], "tr": c["title_ar"]})}} for c in chapters_out], "attribution": meta["attribution"]}
    json.dump(man, open(out / "manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for c in chapters_out: json.dump({"chapter": c["n"], "sentences": c["sentences"]}, open(out / "chapters" / f"{c['n']}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # prune glossary entries no token or segment references (an enclitic table entry taken but never written)
    ref = set()
    for ch in chapters_out:
        for sen in ch["sentences"]:
            for t in sen["tokens"]:
                ref.add(t.get("lex")); ref.update(sg.get("lex") for sg in t.get("segments", []))
    for k in [k for k in used if k not in ref]: used.pop(k)
    for k in used:
        if k in M and k not in morph and ((used.get(k) or G.get(k) or {}).get("pos") == "verb") and (OWNER_G.get(k) == OWNER_M.get(k) or OWNER_M.get(k) is None or k in MX): morph[k] = M[k]   # the package's own verbs (new keys) take their paradigms too
    for k in [k for k in morph if k not in used]: morph.pop(k)   # a paradigm whose verb every token left (re-keyed to the lemma that owns the cell)
    json.dump({"entries": dict(sorted(used.items()))}, open(out / "glossary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump({"verbs": dict(sorted(morph.items()))}, open(out / "morphology.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    nt = sum(len(s["tokens"]) for c in chapters_out for s in c["sentences"]); ns = sum(len(c["sentences"]) for c in chapters_out)
    if report.get("paradigmSkipped"): print("paradigm not copied (glossary holder differs from paradigm owner):", sorted(set(report["paradigmSkipped"])))
    print(f"package {meta['id']}: {len(chapters_out)} ch / {ns} s / {nt} t; glossary {len(used)}; verbs with paradigms {len(morph)}")
    print(f"REVIEW: no key {len(report['nokey'])}; engine≠written {len(report['mismatch'])}; undecided {len(report['undecided'])}; written ending won {report['reconciled']}; lex-verbs promoted {report['promoted']}; verbs re-keyed to their lemma {report['rekeyed']}; verbs still on a noun key {len(report.get('verbNounKey', []))}")
    print("sila named:", report.get("sila_named", 0))
    print("khabar named:", report.get("khabar_named", 0), "| open:", len(report.get("khabar_open", [])), report.get("khabar_open", [])[:40])
    json.dump(report, open(out / "_review.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
if __name__ == "__main__": main()
