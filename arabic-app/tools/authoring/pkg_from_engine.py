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
DEM = {"هذا": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ", "هذه": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ", "ذلك": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "تلك": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "هؤلاء": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ", "اولئك": "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "الذي": "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ", "التي": "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ", "الذين": "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "من": "اسْمٌ مَوْصُولٌ (أَوْ شَرْطِيٌّ) مَبْنِيٌّ عَلَى السُّكُونِ", "ما": "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ"}
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

def person_of(h2, hb2, tense, rule, words, i):
    """The hidden doer by the verb's own shape, then by the nearest cue in the sentence: ـَتْ is «she»; the interrogative
    hamza before تَفْعَلُ is «you»; أَ «I», نَـ «we» (behind سَـ too); تَـ is «she» after a feminine subject or هِيَ/إِنَّهَا,
    «you» after أَنْتَ/ـكَ/ـتَ, the nearest cue winning; a feminine subject right after the verb (تَكُونُ شَرَائِطُهُ) is «she»."""
    h2s = re.sub(r"^سَ", "", h2); hb2s = bare(h2s)
    if tense == "mazi" or rule == "mazi":
        return "هِيَ" if re.search(r"َتْ$", h2) else "هُوَ"
    if tense == "amr" or rule == "amr": return "أَنْتَ"
    if re.match(r"^أَت[َُ](?!ّ)", h2s) and len(hb2s) >= 4: return "أَنْتَ"
    if hb2s.startswith("أ"): return "أَنَا"
    if hb2s.startswith("ن"): return "نَحْنُ"
    if not hb2s.startswith("ت"): return "هُوَ"
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
    if enc in ("ي", "ني") and pos != "verb": return "ya-mutakallim"
    if re.search(r"(?:[ء-ي])َ[ً-ٰ]*ا[ً-ٰ]*ن[ً-ٰ]*ِ?$", h) and not re.search(r"ان[ً-ٰ]*ٌ", h) and len(b) >= 5 and case == "raf" and re.search(r"َان", h): return "muthanna"
    if re.search(r"َيْن[ً-ٰ]*ِ?$", h) and len(b) >= 4: return "muthanna"
    if b in ("ابو", "اخو", "حمو", "فو", "ذو", "أبو", "أخو") or b in ("ابا", "اخا", "ذا", "أبا", "أخا") or b in ("ابي", "اخي", "ذي", "أبي", "أخي"): return "khamsa"
    if b in ("بنو", "بني") and case in ("raf", "nasb", "jarr"): return "jam-m"
    if re.search(r"ُّ?ون[ً-ٰ]*َ?$", h) and len(b) >= 5 and case == "raf": return "jam-m"
    if re.search(r"ِّ?ين[ً-ٰ]*َ?$", h) and len(b) >= 5 and case in ("nasb", "jarr"): return "jam-m"
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
    LX = json.load(open(a.lex, encoding="utf-8")) if a.lex and os.path.exists(a.lex) else {}
    TR = json.load(open(a.trans, encoding="utf-8")) if a.trans and os.path.exists(a.trans) else {}
    FX = json.load(open(a.fixes, encoding="utf-8")) if a.fixes and os.path.exists(a.fixes) else {}
    G, M = load_global()
    if a.morph:
        for k, e in json.load(open(a.morph, encoding='utf-8'))['verbs'].items(): M[k] = e
    GIDS = grammar_ids()
    out = Path(a.out); (out / "chapters").mkdir(parents=True, exist_ok=True)
    used = {}; morph = {}; report = {"nokey": [], "mismatch": [], "undecided": [], "fixed": 0}
    def take(key, where):
        if key in G: used.setdefault(key, G[key]); return True
        for b, e in LX.items():
            if e.get("key") == key: used.setdefault(key, {k: v for k, v in e.items() if k != "key"}); return True
        report["nokey"].append((where, key)); return False
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
        for cand in cands:
            if cand in LX: return LX[cand]["key"], (cand == b2)
            if FOLD(cand) in LXF: return LXF[FOLD(cand)]["key"], (cand == b2)
        return None, bool(b2)
    chapters_out = []
    for ch in E["chapters"]:
        sents = []
        for si, s in enumerate(ch["sentences"], start=1):
            sid = f"s{si}"; where0 = f"{ch['n']}:{sid}"
            words = s["words"]; toks = []
            src_words = [re.sub(r"[،:؛.؟!«»\"()]", "", x) for x in s["text"].split() if re.sub(r"[،:؛.؟!«»\"()]", "", x)]
            aligned = len(src_words) == len(words)
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
                if fx.get("pos") == "verb": kind = "verb"
                if fx.get("pos") == "noun": kind = "noun"
                prevb_ = bare(words[i - 1]["w"]) if i else ""; prevb_ = re.sub(r"^[وف]", "", prevb_) if len(prevb_) > 2 else prevb_
                if prevb_ in JAZM_GOV and re.match(r"^[يتأن]", core) and len(core) >= 3 and not fx.get("pos"):
                    kind = "verb"; k = "cell"; rule = "jazm" if prevb_ in ("لم", "لما") else "nasbVerb"
                    w = dict(w); w["cell"] = dict(w.get("cell") or {}); w["cell"]["tense"] = "mudari"
                if fx.get("enc") is not None: enc = fx["enc"]
                if key and pre and key in G and noal(bare(str(G[key].get("lemma", "")).split("(")[0].strip())) == noal(bh): is_pre = False   # the lexicon owns the whole word (وَلَد، فَقِير)
                segs = []; punct = None
                # ---- particles / pronouns / demonstratives (mabnī)
                pb = core.replace("أ", "ا").replace("إ", "ا") if core else b
                wajh = fx.get("wajh") or w.get("wajh") or ""
                sh0 = "ّ" in N(full)
                if pb == "لكن" and not sh0 and not enc and "لكن-sakina" in PART: pb = "لكن-sakina"
                if pb == "بان" and not enc:   # بِأَنَّ / بِأَنْ: the jarr letter and the particle it governs, by the shadda
                    if sh0: ar0, en0, tr0, lx, tg = ("الْبَاءُ حَرْفُ جَرٍّ، وَ«أَنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمَعْمُولَيْهَا فِي مَحَلِّ جَرٍّ بِالْبَاءِ.", "«that» after the ba of jarr: anna, a sister of inna; the clause it opens stands as a verbal noun in the place of jarr.", "cer bâ'sı + «enne» (inne'nin kardeşi): açtığı cümle masdar-ı müevvel olarak mahallen mecrûr.", ("anna" if "anna" in G else "inna"), "inna-wa-akhawatuha")
                    else: ar0, en0, tr0, lx, tg = ("الْبَاءُ حَرْفُ جَرٍّ، وَ«أَنْ» حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِالْبَاءِ.", "«to» after the ba of jarr: an, the verbal-noun particle that puts the verb in nasb; the clause stands in the place of jarr.", "cer bâ'sı + masdariyye «en»: fiili nasb eder, cümle mahallen mecrûr.", "an-masdariyya", "nawasib-wa-jawazim-al-mudari")
                    ar0 = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + ar0
                    if pre: take("wa" if pre == "و" else "fa", where)
                    take("bi", where); take(lx, where)
                    hpart = full[2:] if pre else full
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": lx, "pos": "part", "grammar": [t for t in ["huruf-jarr", tg] if t in GIDS], "irab": {"ar": ar0, "en": en0, "tr": tr0}, "segments": ([{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}] if pre else []) + [{"form": hpart[:2], "lex": "bi", "pos": "prep"}, {"form": hpart[2:], "lex": lx, "pos": "part"}]})
                    continue
                FACE_LA = {"nafiya": ("«لَا» حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«not» — the negation.", "«değil / -mez» — nefiy harfi.", "la-nafiya"),
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
                if pb == "من" and "\u0650" in N(host_of(full, enc))[:3]: kind = "particle"   # مِنَ the preposition, not مَنْ the relative
                if bare(host_of(full, "")).replace("ٰ", "") in ("لله", "فلله", "ولله") and not enc:
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": "allah", "pos": "propn", "grammar": [t for t in ["huruf-jarr"] + (["mubtada-khabar"] if rule in ("khabar",) else []) if t in GIDS], "irab": {"ar": ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ" + ("، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ." if rule == "khabar" else "."), "en": "«to God» — the lam of jarr on the Name" + ("; the phrase is the khabar." if rule == "khabar" else "."), "tr": "«Allah'a» — lafza-i celâl üzerinde cer lâmı" + ("; câr-mecrûr haberdir." if rule == "khabar" else ".")}, "segments": ([{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}] if pre else []) + [{"form": "لِ", "lex": "li", "pos": "prep"}, {"form": "اللّٰهِ", "lex": "allah", "pos": "propn"}]})
                    take("allah", where); take("li", where)
                    if pre: take("wa" if pre == "و" else "fa", where)
                    continue
                if (kind == "noun" and (pos or "").startswith("noun") and k == "keep" and rule in ("mabni", "keep") and pb not in PART and pb not in DEM and pb not in PRON and not enc): k = None; rule = None
                if pb == "لا" and not enc and wajh in FACE_LA:
                    ar0, en0, tr0, tg = FACE_LA[wajh]; ar0 = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + ar0
                    if pre: take("wa" if pre == "و" else "fa", where)
                    take("la-nafiya" if wajh != "nahiya" else ("la-nahiya" if "la-nahiya" in G else "la-nafiya"), where); lx = "la-nahiya" if (wajh == "nahiya" and "la-nahiya" in G) else "la-nafiya"
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": lx, "pos": "part", "grammar": [t for t in [tg] if t in GIDS], "irab": {"ar": ar0, "en": en0, "tr": tr0}, **({"segments": [{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}, {"form": full[2:], "lex": lx, "pos": "part"}]} if pre else {})})
                    continue
                if pb == "من" and not enc and "\u0650" not in N(host_of(full, enc))[:3] and wajh in FACE_MAN:
                    ar0, en0, tr0, tg = FACE_MAN[wajh]; ar0 = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else ("الْفَاءُ عَاطِفَةٌ، وَ" if pre == "ف" else "")) + "«مَنْ» " + ar0
                    if pre: take("wa" if pre == "و" else "fa", where)
                    take("man", where)
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": "man", "pos": "pron", "grammar": [t for t in [tg] if t in GIDS], "irab": {"ar": ar0, "en": en0, "tr": tr0}, **({"segments": [{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}, {"form": full[2:], "lex": "man", "pos": "pron"}]} if pre else {})})
                    continue
                if kind == "particle" or k == "keep" or rule in ("mabni", "jarrPron", "pron", "symbol", "keep"):
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
                    elif pb in DEM and not enc and (kind != "particle" or pb in ("ما", "من")) and not (pb == "من" and "\u0650" in N(host_of(full, enc))[:3]):
                        cs = CASE_OF_RULE.get(rule); ar = DEM[pb] + (f" فِي مَحَلِّ {CASE_AR[cs]}" if cs else "") + "."; en = ("a demonstrative" if pb not in ("الذي", "التي", "الذين", "ما", "من") else "a relative pronoun") + " — built (mabni)" + (f"; in the place of {cs}" if cs else "") + "."; tr = ("işaret ismi" if pb not in ("الذي", "التي", "الذين", "ما", "من") else "ism-i mevsûl") + " — mebnî" + (f"; mahallen {CASE_AR[cs]}" if cs else "") + "."
                        tags = ["asma-al-ishara-wa-sighuha"] if pb not in ("الذي", "التي", "الذين", "ما", "من") else ["ism-mawsul"]
                        if key: take(key, where)
                        else: report["nokey"].append((where, b))
                    elif pkey in PART:
                        a_, e_, t_, tg, pk = PART[pkey]; ar, en, tr, tags = a_, e_, t_, list(tg)
                        key = pk or key
                        if key: take(key, where)
                        else: report["nokey"].append((where, b))
                    else:
                        ar = "حَرْفٌ مَبْنِيٌّ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ."; en = "a particle — built, no place in the iʿrab."; tr = "harf — mebnî, i'râbda mahalli yok."
                        if key: take(key, where)
                        else: report["nokey"].append((where, b))
                    if pre and pb not in ("و", "ف"):
                        ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else "الْفَاءُ عَاطِفَةٌ، وَ") + ar; en = ("The waw conjoins; " if pre == "و" else "The fa conjoins; ") + en[:1].lower() + en[1:]; tr = ("«ve» + " if pre == "و" else "«bunun üzerine» + ") + tr[:1].lower() + tr[1:]
                        segs = [{"form": full[:2], "lex": "wa" if pre == "و" else "fa", "pos": "conj"}, {"form": full[2:], "lex": key, "pos": "part"}]; take("wa" if pre == "و" else "fa", where)
                    toks.append({"surface": {"full": full, "smart": full, "bare": b}, "lex": key or "?", "pos": "pron" if pb in PRON or pb in DEM else "part", **({"grammar": list(dict.fromkeys(t for t in tags if t in GIDS))} if tags else {}), "irab": {"ar": ar, "en": en, "tr": tr}, **({"segments": segs} if segs else {})})
                    continue
                # ---- verbs
                if kind == "verb" or k == "cell" or rule in ("mazi", "amr", "raf", "nasbVerb", "jazm") or (pos and "verb" in pos and rule in ("raf", "jazm", "nasbVerb", "mazi", "amr")):
                    h = N(host_of(full, enc)); h2 = h[2:] if pre else h; hb2 = bare(h2)
                    tense = (w.get("cell") or {}).get("tense") or rule
                    hidden = i not in doers and not any(words[j].get("rule") in ("fail", "naib") and not any((words[q].get("kind") == "verb" or words[q].get("k") == "cell") for q in range(i + 1, j)) for j in range(i + 1, min(len(words), i + 7)))
                    nxt = words[i + 1]["w"] if i + 1 < len(words) else ""
                    person = person_of(h2, hb2, tense, rule, words, i)
                    mk = {"jazm": "jazm", "nasb": "nasbVerb", "raf": "raf"}.get(k) if rule not in ("raf", "nasbVerb", "jazm") else rule   # the mood from the engine's case where the rule names the construction (shart, jawab)
                    if mk not in ("raf", "nasbVerb", "jazm"): mk = "raf"
                    h2ns = h2.replace("ّ", "")   # NFC seats the shadda after the vowel (بُّو): the suffix test reads the word without it
                    five = bool(re.search(r"(ُونَ|ِينَ|َانِ)(هُ|هَا|هُمْ|هُمَا|هُنَّ|كَ|كِ|كُمْ|كُمَا|كُنَّ|نِي|نَا)?$", h2ns)) and len(re.sub(r"(هم|هما|هن|ها|ه|كم|كما|كن|ك|نا|ني)$", "", hb2) if re.search(r"(ُونَ|ِينَ|َانِ)(هُ|هَا|هُمْ|هُمَا|هُنَّ|كَ|كِ|كُمْ|كُمَا|كُنَّ|نِي|نَا)$", h2ns) else hb2) - 3 >= 2
                    if not five and mk in ("nasbVerb", "jazm") and len(hb2) >= 4 and (re.search(r"(ُوا|ِي|َا)$", h2) or (enc and re.search(r"(ُو|ِي|َا)$", h2))): five = True
                    passive = bool(re.match(r"^[ء-ي]ِي[ء-ي]َ$", h2)) or bool(re.match(r"^[ء-ي]ُ", h2)) and (tense in ("mazi",) and bool(re.search(r"ِ[ء-ي][ً-ٰ]*(?:تْ|وا|ا|تُ|نَا)?$|ِ[ء-ي]َ$", h2)) or (tense not in ("mazi", "amr") and bool(re.search(r"َ[ء-ي][ً-ٰ]*$|َ[ء-ي][َُِ]?(?:ون|ان|ين)?[ً-ٰ]*$", h2)) and not re.search(r"ِ[ء-ي][ً-ٰ]*$", h2)))
                    doer_ar = f"، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ {person}" if hidden and not re.search(r"(وا|تُ|تَ|تِ|نَا|تُمْ|تُنَّ)$", h2) and not enc or (hidden and enc) else ""
                    if passive: doer_ar = doer_ar.replace("وَالْفَاعِلُ", "وَنَائِبُ الْفَاعِلِ")
                    if hb2 == "قيل": doer_ar = "، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ بَعْدَهُ"
                    if tense == "mazi" or rule == "mazi":
                        if re.search(r"ُوا$", h2): ar = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ"; en = "A past verb; the waw of the group is its doer"; tr = "Mâzî fiil; cemaat vâvı fâildir"
                        elif re.search(r"(تُ|تَ|تِ|تُمْ|تُنَّ|نَا)$", h2): ar = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ رَفْعٍ مُتَحَرِّكٍ، وَالضَّمِيرُ فِي مَحَلِّ رَفْعٍ فَاعِلٌ"; en = "A past verb with its subject pronoun suffix as doer"; tr = "Mâzî fiil; bitişik ref zamiri fâildir"
                        elif re.search(r"َتْ$", h2) or re.search(r"َت$", h2): ar = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ" + doer_ar; en = "A past verb (feminine)" + ("; its doer is a hidden pronoun" if hidden else ""); tr = "Mâzî fiil (müennes)" + ("; fâili gizli zamirdir" if hidden else "")
                        elif re.search(r"َا$", h2) and len(hb2) >= 4: ar = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ"; en = "A past verb; the alif of the dual is its doer"; tr = "Mâzî fiil; tesniye elifi fâildir"
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
                        elif rule == "jazm": sign = ("السُّكُونُ، وَحُرِّكَ آخِرُهُ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ لِأَنَّهُ مُضَاعَفٌ" if re.search(r"ّ[َ]?$", h2) else ("السُّكُونُ" if re.search(r"ْ$", h2) or enc else "حَذْفُ حَرْفِ الْعِلَّةِ"))
                        elif re.search(r"[ىا]$", hb2): sign = ("الْفَتْحَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ" if rule == "nasbVerb" else "الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ")
                        elif re.search(r"[يو]$", hb2) and rule == "raf": sign = "الضَّمَّةُ الْمُقَدَّرَةُ عَلَى " + ("الْيَاءِ" if hb2.endswith("ي") else "الْوَاوِ") + " لِلثِّقَلِ"
                        else: sign = "الضَّمَّةُ الظَّاهِرَةُ" if rule == "raf" else "الْفَتْحَةُ الظَّاهِرَةُ"
                        doer2 = "" if five else doer_ar
                        if five: doer2 = "، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" if re.search(r"ون|وا", hb2) else ("، وَالْأَلِفُ فَاعِلٌ" if re.search(r"ان|ا$", hb2) else "، وَالْيَاءُ فَاعِلٌ")
                        ar = f"فِعْلٌ مُضَارِعٌ {'مَبْنِيٌّ لِلْمَجْهُولِ ' if passive else ''}{mood[0]} {gov}، وَعَلَامَةُ {'رَفْعِهِ' if rule == 'raf' else ('نَصْبِهِ' if rule == 'nasbVerb' else 'جَزْمِهِ')} {sign}{doer2}".replace("  ", " ").replace(" ،", "،")
                        en = f"A present verb{' in the passive' if passive else ''}, {mood[1]}" + (f" after {gov.replace('بِـ', '')}" if gov else "") + ("; its doer is a hidden pronoun «" + person + "»" if hidden and not five and not enc else ""); tr = f"Muzâri fiil{' (meçhul)' if passive else ''}, {mood[2]}" + ("; fâili gizli zamir «" + person + "»" if hidden and not five and not enc else "")
                        tags = ["nawasib-wa-jawazim-al-mudari"] if rule in ("nasbVerb", "jazm") else (["afal-khamsa"] if five else [])
                    if enc:
                        ar += f"، وَ{ENC_AR.get(enc, 'الضَّمِيرُ')} ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ"; en += f"; the pronoun suffix {ENC_EN.get(enc, '')} is its object"; tr += f"; bitişik zamir {ENC_TR.get(enc, '')} mef'ûlün bihtir"; tags = tags + ["maful-bihi"]
                    if pre: ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if pre == "و" else "الْفَاءُ عَاطِفَةٌ، وَ") + ar; en = ("The waw conjoins; " if pre == "و" else "The fa conjoins; ") + en[:1].lower() + en[1:]; tr = ("«ve» + " if pre == "و" else "«bunun üzerine» + ") + tr[:1].lower() + tr[1:]
                    ar = ar.rstrip("،") + "."; en = en + "."; tr = tr + "."
                    if not key: report["nokey"].append((where, b))
                    else: take(key, where)
                    if key and key in M and (OWNER_G.get(key) == OWNER_M.get(key) or key not in OWNER_G): morph[key] = M[key]
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
                lem_b = noal(bare(str((lem_e or {}).get("lemma", "")).split("(")[0])) if lem_e else ""
                if rule == "jarr" and re.match(r"^[بل]ِ|^كَ", h2) and len(hb2) >= 3:
                    rest_b = noal(hb2[1:])
                    if (lem_b and rest_b == lem_b) or (lem_b and lem_b != noal(hb2) and len(hb2) >= 4) or (not lem_b and len(hb2) >= 4): jc = h2[0]
                cs = CASE_OF_RULE.get(rule) or ({"raf": "raf", "nasb": "nasb", "jarr": "jarr"}.get(k) if k in ("raf", "nasb", "jarr") else None)
                if rule == "kanaIsm" and re.search(r"ً[اى]?$", h2.replace("ّ", "")): rule = "kanaKhabar"; cs = "nasb"
                if rule == "innaKhabar" and re.search(r"ً[اى]?$", h2.replace("ّ", "")):
                    rule = "kanaKhabar" if any(re.sub(r"^[وف]", "", bare(x["w"])) in KANA_FAM for x in words[max(0, i - 3):i]) else "innaIsm"; cs = "nasb"
                r_ar, r_en, r_tr, tags = ROLE.get(rule, ("", "", "", []))
                if rule in ("atf", "nat", "badal", "tawkid") and cs: r_ar = r_ar + " " + {"raf": "مَرْفُوعٌ", "nasb": "مَنْصُوبٌ", "jarr": "مَجْرُورٌ"}[cs]
                if rule == "jarr" and i > 0 and not jc: r_ar = "مَجْرُورٌ بِـ«" + N(words[i - 1]["w"]) + "»"
                hostn = h2[2:] if jc else h2
                sh = shape(hostn, cs, enc, pos, "al" if bare(hostn).startswith("ال") else "")
                hn_b = noal(bare(hostn))
                lem_pl = lem_b and re.search(r"(ون|ين)$", lem_b) and hn_b in (lem_b, lem_b[:-2] + "ون", lem_b[:-2] + "ين")
                if sh in ("muthanna", "jam-m") and lem_b and not lem_pl and hn_b not in ("بنو", "بني") and not (hn_b in (lem_b + "ان", lem_b + "ين", lem_b + "ون", lem_b + "ي", lem_b + "و", lem_b + "ا") or (lem_b.endswith("ة") and hn_b in (lem_b[:-1] + "تان", lem_b[:-1] + "تين")) or (lem_b.endswith("ى") and hn_b in (lem_b[:-1] + "يان", lem_b[:-1] + "يين"))): sh = "sahih"
                if sh == "sahih" and lem_b and (hn_b in (lem_b + "ان", lem_b + "ين") or (lem_b.endswith("ة") and hn_b in (lem_b[:-1] + "تان", lem_b[:-1] + "تين"))) and re.search(r"(َانِ|َيْنِ)$", hostn): sh = "muthanna"
                if sh == "sahih" and lem_b and (hn_b in (lem_b + "ون", lem_b + "ين") or lem_pl) and re.search(r"(ُونَ|ِينَ)$", hostn): sh = "jam-m"
                la_jins = (not cs) and i > 0 and bare(words[i - 1]["w"]) == "لا" and not enc and not bare(h2).startswith("ال") and re.search(r"َ$", N(h2)) and not re.search(r"[ًٌٍ]", N(h2))
                if la_jins:
                    cs = "nasb"; ar = "اسْمُ «لَا» النَّافِيَةِ لِلْجِنْسِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ"; en = "the noun of «la» of absolute negation — built on fatha, in the place of nasb"; tr = "cinsini nefyeden «lâ»nın ismi — fetha üzere mebnî, mahallen mansûb"; sign_ar = sign_en = sign_tr = ""; tags = list(tags) + ["la-nafiya-lil-jins"]
                elif not cs: 
                    ar = "اسْمٌ"; en = "a noun"; tr = "isim"; sign_ar = sign_en = sign_tr = ""
                    if rule == "fail" and k is None: pass
                else:
                    sign_ar, sign_en, sign_tr = SIGN.get((cs, sh), SIGN[(cs, "sahih")])
                    ar = f"{r_ar} {sign_ar}"; en = f"{r_en}; the sign is {sign_en}"; tr = f"{r_tr}; alâmeti {sign_tr}"
                    tags = list(tags) + SHAPE_TAG.get(sh, [])
                if jc:
                    JN = {"ب": ("الْبَاءُ", "bi"), "ل": ("اللَّامُ", "li"), "ك": ("الْكَافُ", "ka")}[jc]
                    ar = f"{JN[0]} حَرْفُ جَرٍّ، وَ" + ar.replace("مَجْرُورٌ", "مَجْرُورٌ بِهِ", 1) if "مَجْرُورٌ" in ar else f"{JN[0]} حَرْفُ جَرٍّ، وَالِاسْمُ مَجْرُورٌ {sign_ar}"
                    en = "preposition + noun: " + en; tr = "harf-i cer + isim: " + tr; tags = tags + ["huruf-jarr"]
                if enc:
                    ar += f"، وَهُوَ مُضَافٌ، وَ{ENC_AR.get(enc, 'الضَّمِيرُ')} ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ"; en += f"; annexed, the pronoun {ENC_EN.get(enc, '')} is the mudaf ilayh"; tr += f"; muzâf, zamir {ENC_TR.get(enc, '')} muzâfun ileyh"; tags = tags + ["idafa-definiteness"]
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
        if k in M and k not in morph and (G.get(k) or {}).get("pos") == "verb" and OWNER_G.get(k) == OWNER_M.get(k): morph[k] = M[k]
    json.dump({"entries": dict(sorted(used.items()))}, open(out / "glossary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump({"verbs": dict(sorted(morph.items()))}, open(out / "morphology.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    nt = sum(len(s["tokens"]) for c in chapters_out for s in c["sentences"]); ns = sum(len(c["sentences"]) for c in chapters_out)
    if report.get("paradigmSkipped"): print("paradigm not copied (glossary holder differs from paradigm owner):", sorted(set(report["paradigmSkipped"])))
    print(f"package {meta['id']}: {len(chapters_out)} ch / {ns} s / {nt} t; glossary {len(used)}; verbs with paradigms {len(morph)}")
    print(f"REVIEW: no key {len(report['nokey'])}; engine≠written {len(report['mismatch'])}; undecided {len(report['undecided'])}")
    json.dump(report, open(out / "_review.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
if __name__ == "__main__": main()
