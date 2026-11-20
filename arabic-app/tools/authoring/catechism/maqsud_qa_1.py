# -*- coding: utf-8 -*-
# Catechism bank — al-Maqṣūd with its Ottoman lesson notes (research/sources/maqsud-sarf.txt): the six «س؛ … ج؛ …» pairs the
# notes themselves set. The book asks and answers in Ottoman Turkish, so q.tr / a.tr are the book's own sentences in today's
# letters, word for word; q.en / a.en translate them. `ar` is the vowelled Arabic the answer (or the line it comments on)
# carries in the source. `src` is the file and the lines. The same pairs stand in maksut-sarf-ottoman.txt (l. 88, 121, 345,
# 402, 1436, 1448).
SRC = "research/sources/maqsud-sarf.txt"
ITEMS = [
 {"n": 1, "q": {"tr": "Fiillerden az olan ile ne kastediliyor ve çoğalmasından murad nedir?",
                "en": "What is meant by «the few among the verbs», and what by their becoming many?"},
  "a": {"tr": "Az olan ile murad, fiillerin çıkış yeri olan masdardır. Çoğalmasından murad, masdardan müştak olan mâzî, muzâri, emir, nehiy gibi fiillerdir. Meselâ نَصْرًا masdardır ve bir kelimedir; bundan نَصَرَ، يَنْصُرُ، نَاصِرٌ، مَنْصُورٌ، لِيَنْصُرْ، اُنْصُرْ gibi birçok fiil müştak kılınmakla o bir kelime çoğalmıştır.",
        "en": "The few is the maṣdar, the place the verbs come out of. Their becoming many is the verbs derived from the maṣdar — the māḍī, the muḍāriʿ, the amr, the nahy. نَصْرًا, for instance, is a maṣdar and one word; by deriving نَصَرَ، يَنْصُرُ، نَاصِرٌ، مَنْصُورٌ، لِيَنْصُرْ، اُنْصُرْ and many more from it, that one word has become many."},
  "ar": ["نَصَرَ", "يَنْصُرُ", "نَاصِرٌ", "مَنْصُورٌ", "لِيَنْصُرْ", "اُنْصُرْ"], "notes": ["masdar"],
  "src": {"file": SRC, "lines": [71, 72, 73, 74, 75]}},
 {"n": 2, "q": {"tr": "Şâz, nâdir ve zayıf arasında ne fark vardır?",
                "en": "What is the difference between shādhdh, nādir and ḍaʿīf?"},
  "a": {"tr": "Şâz: her ne kadar çok olsa da kaideye muhalif olandır. Nâdir: kıyasa uygun olup az bulunandır. Zayıf: hükmü sâbit ve kat'î olmayandır.",
        "en": "Shādhdh: what goes against the rule, however frequent it is. Nādir: what agrees with the analogy but is rarely found. Ḍaʿīf: that whose ruling is not established and certain."},
  "ar": [], "notes": ["thulathi-mujarrad-babs"],
  "src": {"file": SRC, "lines": [102, 103, 104]}},
 {"n": 3, "q": {"tr": "İsm-i fâil ile sıfat-ı müşebbehe arasında ne fark vardır?",
                "en": "What is the difference between the ism fāʿil and the ṣifa mushabbaha?"},
  "a": {"tr": "İsm-i fâil hudûs, yani gelici geçicidir; meselâ آكِلٌ ve شَارِبٌ gibi. Sıfat-ı müşebbehe sübût mânâsınadır, yani gelici geçici değildir; meselâ حَسَنٌ ve قَبِيحٌ gibi.",
        "en": "The ism fāʿil is for occurrence — it comes and passes, like آكِلٌ and شَارِبٌ. The ṣifa mushabbaha is for permanence — it does not come and pass, like حَسَنٌ and قَبِيحٌ."},
  "ar": ["آكِلٌ", "شَارِبٌ", "حَسَنٌ", "قَبِيحٌ"], "notes": ["ism-fail", "sifa-mushabbaha"],
  "src": {"file": SRC, "lines": [297, 298, 299]}},
 {"n": 4, "q": {"tr": "فَلْيَفْعَلْ ne kelime olur?", "en": "What word is فَلْيَفْعَلْ?"},
  "a": {"tr": "Üçüncü bâbdan emr-i gâib müfred müzekker olur. Not: vâv, fâ ve ثُمَّ'den sonra gelen emr-i gâib lâmı cezm olur (sâkin kılınır).",
        "en": "A command to the absent, masculine singular, of the third bāb. Note: the lām of the command to the absent takes a sukūn after wāw, fāʾ and ثُمَّ."},
  "ar": ["فَلْيَفْعَلْ"], "notes": ["lam-amr", "imperative-amr"],
  "src": {"file": SRC, "lines": [341, 346, 347]}},
 {"n": 5, "q": {"tr": "رَأَى kelimesi aksâm-ı seb'adan ne olur?", "en": "Which of the seven classes is the word رَأَى?"},
  "a": {"tr": "Hem mehmûz hem de nâkıs olur.", "en": "It is both mahmūz and nāqiṣ."},
  "ar": ["رَأَى", "يَرَى"], "notes": ["naqis-verbs"],
  "src": {"file": SRC, "lines": [1073, 1074]}},
 {"n": 6, "q": {"tr": "أَتَى kelimesi aksâm-ı seb'adan ne olur?", "en": "Which of the seven classes is the word أَتَى?"},
  "a": {"tr": "Hem mehmûz hem de nâkıs olur.", "en": "It is both mahmūz and nāqiṣ."},
  "ar": ["أَتَى", "يَأْتِي"], "notes": ["naqis-verbs"],
  "src": {"file": SRC, "lines": [1085, 1086]}},
]
