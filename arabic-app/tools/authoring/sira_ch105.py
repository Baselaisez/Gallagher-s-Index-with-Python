"""al-Nadwī, al-Sīra al-Nabawiyya — chapter 105: «ولادته الكريمة ونسبه الزكيّ» (4), Shamela p. 152, printed p. 160: the paragraph
«وهكذا فعلت حليمة» to «وحسدتها صواحبها.» — Ḥalīma takes the orphan, and the blessing in her camp."""
from sira_common import *

N_ = 105
TITLE = {"ar": "وِلَادَتُهُ الْكَرِيمَةُ وَنَسَبُهُ الزَّكِيُّ (٤)", "en": "His Noble Birth and Pure Lineage (4)", "tr": "Mübarek Doğumu ve Temiz Nesebi (4)"}
META = {"pages": "160", "en": "Ḥalīma turns away, comes back and takes him; the blessing in her camp and her companions' envy (s1–s6)",
        "tr": "Halîme önce döner, sonra geri gelip onu alır; çadırındaki bereket ve arkadaşlarının kıskançlığı (s1–s6)"}
J = lambda s: "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ " + s
HOCA = [("ch. 105 s2: «وَأَخْذَهُ» read as a masdar conjoined to «حُبَّهُ» (Allah inspired her with love of him and with taking him) — no feminine verb stands there", "Bölüm 105 s2: «ve ahzehû» «hubbehû»ya ma'tûf masdar okundu (Allah ona onu sevmeyi ve almayı ilham etti) — orada müennes bir fiil yoktur")]
HE = lambda who_ar, who_en, who_tr: ("، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى " + who_ar, " with «him» (" + who_en + ")", "; zamir (" + who_tr + ") mahallen mecrûr")
def JP(full, lex, enc, hang, who, en, tr, p=None):
    """a jarr letter with an attached pronoun, hanging on a verb"""
    return T(full, lex, "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "حَرْفُ جَرٍّ، وَ" + PRON_AR.get(enc, enc) + " ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى " + who[0] + J("بِـ«" + hang[0] + "»") + ".",
             "A jarr letter with «" + who[1] + "» — the phrase hangs on «" + hang[1] + "»: «" + en + "».", "Cer harfi; zamir (" + who[2] + ") mahallen mecrûr — câr-mecrûr «" + hang[2] + "»e müteallik: «" + tr + "».", p=p, enc=enc)
def FEM_V(full, lex, g, gloss, p=None, pre=None, obj=None, note=("", "", "")):
    """a past verb with the ta of the feminine and the hidden «she» (Ḥalīma), an attached object if any"""
    a0 = {"wa": "الْوَاوُ عَاطِفَةٌ، وَ", "fa": "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَ", None: ""}[pre]
    e0 = {"wa": "The waw conjoins; ", "fa": "The fa conjoins and marks what follows at once; ", None: ""}[pre]
    t0 = {"wa": "Vâv atıf; ", "fa": "Fâ ta'kîb ile atıf içindir; ", None: ""}[pre]
    ob = ("، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى النَّبِيِّ", "; «him» (the Prophet) is its object", "; zamir (Peygamber) mef'ûlün bih") if obj else ("", "", "")
    segs = None
    if obj or pre:
        stem = N(full)[2:] if pre else N(full)
        if obj: stem = stem[:-len(obj)]
        segs = ([({"wa": "وَ", "fa": "فَ"}[pre], pre, "conj")] if pre else []) + [(stem, lex, "verb")] + ([(obj, "pron-3ms", "pron")] if obj else [])
    return T(full, lex, "verb", g, a0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ" + ob[0] + "، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، يَعُودُ عَلَى حَلِيمَةَ" + note[0] + ".",
             e0 + "«" + gloss[0] + "» is a past verb built on fatha, the ta of the feminine" + ob[1] + "; its doer is the hidden «she» (Ḥalīma)" + note[1] + ".",
             t0 + "«" + gloss[1] + "» fetha üzere mebnî mâzî, tâ te'nîs için" + ob[2] + "; fâili gizli «hiye» (Halîme)" + note[2] + ".", p=p, segs=segs)
PROPHET = ("النَّبِيِّ", "him", "Peygamber")

S = [
 SEN(1, "Ḥalīma did the same: she turned away from him the first time;",
     "Halîme de böyle yaptı; ilk seferinde ondan yüz çevirdi;",
 [T("وَهٰكَذَا", "hakadha", "pron", ["huruf-jarr", "asma-al-ishara-wa-sighuha", "maful-mutlaq"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْهَاءُ لِلتَّنْبِيهِ، وَالْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَائِبٍ عَنِ الْمَفْعُولِ الْمُطْلَقِ، أَيْ: فِعْلًا مِثْلَ ذٰلِكَ.",
    "The waw resumes; هَا calls attention, the kaf of likeness is a jarr letter, and ذَا «this» is a demonstrative in the seat of jarr — the phrase stands for an absolute object («a doing like that»).", "Vâv isti'nâf içindir; «hâ» tenbih, kâf teşbih için cer harfi, «zâ» ism-i işaret, mahallen mecrûr — câr-mecrûr mef'ûl-i mutlaka nâib mahzûfa müteallik («bunun gibi bir yapış»).",
    segs=[("وَ", "wa", "conj"), ("هٰكَذَا", "hakadha", "pron")]),
  T("فَعَلَتْ", "faala", "verb", ["thulathi-mujarrad-babs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ بَعْدَهُ.", "A past verb «did», the ta of the feminine; its doer follows.", "Mâzî «yaptı», tâ te'nîs için; fâili sonra gelir."),
  T("حَلِيمَةُ", "halima-sadiyya", "propn", ["fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَلَمْ يُنَوَّنْ لِأَنَّهُ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.", "The doer, in raf' — a feminine name, barred from tanwin.", "Fâil, merfû — müennes alem, gayr-i munsarif.", p="،"),
  FEM_V("فَانْصَرَفَتْ", "insarafa", ["atf-nasaq", "form-vii-verbs"], ("turned away", "yüz çevirdi"), pre="fa"),
  JP("عَنْهُ", "an", "هُ", ("انْصَرَفَتْ", "turned away", "insarafet"), PROPHET, "from him", "ondan"),
  T("أَوَّلَ", "awwal", "noun", ["maful-fih", "idafa-definiteness"], "نَائِبٌ عَنْ ظَرْفِ الزَّمَانِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، مُتَعَلِّقٌ بِـ«انْصَرَفَتْ».", "Standing for an adverb of time, in nasb, annexed — it hangs on «turned away»: «the first (time)».", "Zaman zarfına nâib, mansûb, muzâf — «insarafet»e müteallik: «ilk (sefer)»."),
  T("مَرَّةٍ", "marra-once", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The second term of the idafa, in jarr: «time».", "Muzâfun ileyh, mecrûr: «sefer».", p="،")]),
 SEN(2, "then her heart inclined to him, and Allah inspired her with love for him and with taking him;",
     "sonra kalbi ona meyletti; Allah ona onu sevmeyi ve almayı ilham etti;",
 [T("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ وَالتَّرَاخِيَ مَبْنِيٌّ عَلَى الْفَتْحِ.", "ثُمَّ «then», a conjunction of order with an interval.", "«Sümme» tertîb ve terâhî bildiren atıf harfi."),
  T("انْعَطَفَ", "inatafa", "verb", ["form-vii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ بَعْدَهُ — وَانْعَطَفَ عَلَيْهِ: مَالَ إِلَيْهِ وَرَقَّ لَهُ.", "A past verb «inclined», built on fatha; its doer follows — انْعَطَفَ عَلَيْهِ: to lean towards someone in tenderness.", "Fetha üzere mebnî mâzî «meyletti»; fâili sonra gelir — in'atafa aleyhi: ona şefkatle meyletti."),
  T("قَلْبُهَا", "qalb", "noun", ["fail", "al-bariz-al-muttasil"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى حَلِيمَةَ.", "The doer, in raf', annexed to «her» (Ḥalīma): «her heart».", "Fâil, merfû, muzâf; zamir (Halîme) muzâfun ileyh: «kalbi».", enc="هَا"),
  JP("عَلَيْهِ", "ala", "هِ", ("انْعَطَفَ", "inclined", "in'atafa"), PROPHET, "to him", "ona", p="،"),
  T("وَأَلْهَمَهَا", "alhama", "verb", ["atf-nasaq", "form-iv-verbs", "mafulayn", "al-bariz-al-muttasil"], "الْوَاوُ عَاطِفَةٌ، وَأَلْهَمَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ يَعُودُ عَلَى حَلِيمَةَ، وَالْفَاعِلُ بَعْدَهُ.",
    "The waw conjoins; «inspired» is a past verb built on fatha; «her» (Ḥalīma) is its first object; its doer follows.", "Vâv atıf; «elheme» fetha üzere mebnî mâzî; zamir (Halîme) birinci mef'ûl; fâili sonra gelir.", pre=("wa",), enc="هَا"),
  T("اللهُ", "allah", "propn", ["fail"], "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The name of Allah, the doer, in raf'.", "Lafza-i celâl, fâil, merfû."),
  T("حُبَّهُ", "hubb", "noun", ["maful-bihi", "masdar", "al-bariz-al-muttasil"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى النَّبِيِّ — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ.",
    "The second object, in nasb, annexed to «him» (the Prophet) — a masdar annexed to its object: «love for him».", "İkinci mef'ûl, mansûb, muzâf; zamir (Peygamber) muzâfun ileyh — masdarın mef'ûlüne izâfeti: «onu sevmek».", p="،", enc="هُ"),
  T("وَأَخْذَهُ", "akhdh", "noun", ["atf-nasaq", "masdar", "al-bariz-al-muttasil"], "الْوَاوُ عَاطِفَةٌ، وَأَخْذَ مَعْطُوفٌ عَلَى «حُبَّهُ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ.",
    "The waw conjoins; «and taking (him)» is a masdar conjoined to «love», in nasb, annexed to its object «him».", "Vâv atıf; «ahz» (almak) «hubb»a ma'tûf masdar, mansûb, muzâf; zamir mef'ûlü olarak muzâfun ileyh.", p="،", pre=("wa",), enc="هُ")]),
 SEN(3, "and she had found no other; so she went back to him, took him, and went with him to her camp;",
     "ondan başkasını da bulamamıştı; ona döndü, onu aldı ve onunla konak yerine gitti;",
 [T("وَلَمْ", "lam", "part", ["jawazim-al-mudari-wal-amr-fil-kafiya", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "The waw of the hal; لَمْ negates, puts the present verb in jazm and turns it to the past.", "Vâv hâliyye; «lem» nefy, cezm ve kalb harfi.", pre=("wa",)),
  T("تَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "jawazim-al-mudari-wal-amr-fil-kafiya"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "A defective present verb in jazm after لَمْ (its waw dropped where two sukuns met); its noun is the hidden «she» — the clause is a hal.", "«lem» ile meczûm nâkıs muzâri (iki sâkin karşılaştığı için vâvı düştü); ismi gizli «hiye» — cümle hâldir."),
  FEM_V("وَجَدَتْ", "wajada", ["mithal-verbs", "kana-wa-akhawatuha"], ("found", "buldu"), note=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «تَكُنْ»", " — the clause is the predicate of «be» («she had not found»)", " — cümle «tekun»un haberi olarak mahallen mansûb")),
  T("غَيْرَهُ", "ghayr", "noun", ["maful-bihi", "al-bariz-al-muttasil"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى النَّبِيِّ.", "The object, in nasb, annexed to «him»: «(any) other than him».", "Mef'ûlün bih, mansûb, muzâf; zamir (Peygamber) muzâfun ileyh: «ondan başkasını».", p="،", enc="هُ"),
  FEM_V("فَرَجَعَتْ", "rajaa", ["atf-nasaq", "thulathi-mujarrad-babs"], ("went back", "döndü"), pre="fa"),
  JP("إِلَيْهِ", "ila", "هِ", ("رَجَعَتْ", "went back", "racaat"), PROPHET, "to him", "ona", p="،"),
  FEM_V("فَأَخَذَتْهُ", "akhadha", ["atf-nasaq", "mahmuz-verbs", "al-bariz-al-muttasil"], ("took", "aldı"), pre="fa", obj="هُ", p="،"),
  FEM_V("وَذَهَبَتْ", "dhahaba", ["atf-nasaq", "thulathi-mujarrad-babs"], ("went", "gitti"), pre="wa"),
  T("بِهِ", "bi", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ لِلتَّعْدِيَةِ وَالْمُصَاحَبَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى النَّبِيِّ" + J("بِـ«ذَهَبَتْ»") + ".", "The ba (taking along), a jarr letter, with «him» — the phrase hangs on «went»: «with him».", "Bâ (beraber götürme) cer harfi; zamir (Peygamber) — câr-mecrûr «zehebet»e müteallik: «onunla».", enc="هِ"),
  T("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "A jarr letter: «to».", "Cer harfi: «-e»."),
  T("رَحْلِهَا", "rahl", "noun", ["huruf-jarr", "al-bariz-al-muttasil"], "مَجْرُورٌ بِـ«إِلَى» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + J("بِـ«ذَهَبَتْ»") + " — وَالرَّحْلُ: مَنْزِلُ الْمُسَافِرِ وَمَتَاعُهُ.",
    "In jarr after إِلَى, annexed to «her» — the phrase hangs on «went» — رَحْل: a traveller's lodging and gear: «her camp».", "«ilâ» ile mecrûr, muzâf; zamir muzâfun ileyh — câr-mecrûr «zehebet»e müteallik — rahl: yolcunun konağı ve eşyası.", p="،", enc="هَا")]),
 SEN(4, "and she touched the blessing with her own hand: everything in her camp had a new air about it;",
     "bereketi eliyle dokunur gibi gördü: konak yerindeki her şeyin başka bir hâli oldu;",
 [FEM_V("وَلَمَسَتِ", "lamasa", ["atf-nasaq", "thulathi-mujarrad-babs"], ("touched", "dokundu"), pre="wa", note=("، وَحُرِّكَتِ التَّاءُ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "; the ta is voweled with kasra before the article", "; tâ iki sâkin karşılaştığı için kesre aldı")),
  T("الْبَرَكَةَ", "baraka-blessing", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The object, in nasb: «the blessing».", "Mef'ûlün bih, mansûb: «bereket»."),
  T("بِيَدِهَا", "bi", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ لِلِاسْتِعَانَةِ، وَيَدِ مَجْرُورٌ بِالْبَاءِ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + J("بِـ«لَمَسَتِ»") + ".",
    "The ba of the means, a jarr letter; «hand» is in jarr, annexed to «her» — the phrase hangs on «touched».", "İsti'âne bâsı, cer harfi; «yed» mecrûr, muzâf; zamir muzâfun ileyh — câr-mecrûr «lemeset»e müteallik.", p="،", pre=("bi",), enc="هَا", s="yad", spos="noun"),
  T("فَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ لِلتَّفْصِيلِ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ «شَأْنٌ» مُؤَخَّرٌ.", "The fa conjoins and spells out what came before; كَانَ is the defective past verb; its noun «an air» comes later.", "Fâ tafsîl ile atıf içindir; «kâne» nâkıs mâzî; ismi «şe'n» sonra gelir.", pre=("fa",)),
  T("لِكُلِّ", "li", "prep", ["huruf-jarr", "kana-wa-akhawatuha", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ بِاللَّامِ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ" + J("بِمَحْذُوفٍ خَبَرِ «كَانَ» مُقَدَّمٌ") + ".",
    "The lam, a jarr letter; «every» is in jarr, annexed — the phrase is the fronted predicate of كَانَ: «everything had».", "Lâm cer harfi; «kull» mecrûr, muzâf — câr-mecrûr kâne'nin öne alınmış haberine müteallik.", pre=("li",), s="kull", spos="noun"),
  T("شَيْءٍ", "shay", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The second term of the idafa, in jarr: «thing».", "Muzâfun ileyh, mecrûr: «şey»."),
  T("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "A jarr letter: «in».", "Cer harfi: «-de»."),
  T("رَحْلِهَا", "rahl", "noun", ["huruf-jarr", "al-bariz-al-muttasil"], "مَجْرُورٌ بِـ«فِي» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + J("بِمَحْذُوفٍ نَعْتٍ لِـ«شَيْءٍ»") + ".",
    "In jarr after فِي, annexed to «her» — the phrase hangs on an omitted adjective of «thing».", "«fî» ile mecrûr, muzâf; zamir muzâfun ileyh — câr-mecrûr «şey»in mahzûf na'tına müteallik.", enc="هَا"),
  T("شَأْنٌ", "shan", "noun", ["kana-wa-akhawatuha"], "اسْمُ «كَانَ» مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of كَانَ, placed after its predicate, in raf': «a state, an air».", "Kâne'nin sonraya bırakılmış ismi, merfû: «hâl»."),
  T("غَيْرُ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِـ«شَأْنٌ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "An adjective of «an air», in raf', annexed: «other than».", "«Şe'n»in na'tı, merfû, muzâf: «… den başka»."),
  T("الشَّأْنِ", "shan", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — أَيْ: غَيْرُ مَا كَانَ عَلَيْهِ.", "The second term of the idafa, in jarr — «other than (its former) state».", "Muzâfun ileyh, mecrûr — yani önceki hâlinden başka.", p="،")]),
 SEN(5, "she saw the blessing in her own milk and in the milk of her beasts, in the old she-camel and in the she-donkey;",
     "bereketi kendi sütünde ve hayvanların sütünde, yaşlı dişi devede ve dişi eşekte gördü;",
 [T("وَرَأَتِ", "raa", "verb", ["atf-nasaq", "mahmuz-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَرَأَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الْمُقَدَّرِ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، يَعُودُ عَلَى حَلِيمَةَ.",
    "The waw conjoins; «saw» is a past verb built on a fatha estimated on the alif that dropped before the ta; the ta of the feminine is voweled with kasra before the article; its doer is the hidden «she» (Ḥalīma).", "Vâv atıf; «raet» iki sâkin karşılaşınca düşen elif üzerinde takdîrî fetha ile mebnî mâzî; te'nîs tâsı kesre aldı; fâili gizli «hiye» (Halîme).", pre=("wa",)),
  T("الْبَرَكَةَ", "baraka-blessing", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The object, in nasb: «the blessing».", "Mef'ûlün bih, mansûb: «bereket»."),
  T("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "A jarr letter: «in».", "Cer harfi: «-de»."),
  T("اللِّبَانِ", "liban-nursing", "noun", ["huruf-jarr"], "مَجْرُورٌ بِـ«فِي» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ" + J("بِـ«رَأَتِ»") + " — وَاللِّبَانُ: لَبَنُ الْمُرْضِعِ وَرَضَاعُهَا.", "In jarr after فِي — the phrase hangs on «saw» — لِبَان: the nurse's own milk.", "«fî» ile mecrûr — câr-mecrûr «raet»e müteallik — libân: sütannenin kendi sütü."),
  T("وَالْأَلْبَانِ", "laban", "noun", ["atf-nasaq", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَالْأَلْبَانِ مَعْطُوفٌ عَلَى «اللِّبَانِ» مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ «لَبَنٍ»: أَلْبَانُ الْمَاشِيَةِ.", "The waw conjoins; «and the milks» is conjoined, in jarr — the plural of لَبَن: the milk of the herd.", "Vâv atıf; «el-elbân» ma'tûf, mecrûr — «leben»in cemi: hayvanların sütü.", p="،", pre=("wa",)),
  T("وَالشَّارِفِ", "sharif-camel", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالشَّارِفِ مَعْطُوفٌ عَلَى «اللِّبَانِ» مَجْرُورٌ بِالْكَسْرَةِ — وَالشَّارِفُ: النَّاقَةُ الْمُسِنَّةُ.", "The waw conjoins; «and the old she-camel» is conjoined, in jarr.", "Vâv atıf; «eş-şârif» ma'tûf, mecrûr — yaşlı dişi deve.", pre=("wa",)),
  T("وَالْأَتَانِ", "atan", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْأَتَانِ مَعْطُوفٌ عَلَى «الشَّارِفِ» مَجْرُورٌ بِالْكَسْرَةِ — وَالْأَتَانُ: أُنْثَى الْحِمَارِ.", "The waw conjoins; «and the she-donkey» is conjoined, in jarr.", "Vâv atıf; «el-etân» ma'tûf, mecrûr — dişi eşek.", p="،", pre=("wa",))]),
 SEN(6, "and everyone was saying: You have taken, Ḥalīma, a blessed soul! — and her companions envied her.",
     "herkes: «Ey Halîme, mübarek bir can aldın!» diyordu; arkadaşları da onu kıskandılar.",
 [T("وَكُلٌّ", "kull", "noun", ["mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَكُلٌّ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالتَّنْوِينُ عِوَضٌ عَنِ الْمُضَافِ إِلَيْهِ، أَيْ: كُلُّ أَحَدٍ؛ وَجَازَ الِابْتِدَاءُ بِهِ لِذٰلِكَ.",
    "The waw conjoins; «everyone» is the mubtada, in raf' — its tanwin stands for the omitted second term («every one»), which lets it open the clause.", "Vâv atıf; «kullun» mübtedâ, merfû — tenvini mahzûf muzâfun ileyhe bedeldir («herkes»); bu yüzden mübtedâ olabildi.", pre=("wa",)),
  T("يَقُولُ", "qala", "verb", ["hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى «كُلٌّ» — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
    "A present verb in raf' «says»; its doer is the hidden «he» (everyone) — the clause is the predicate, in the seat of raf'.", "Merfû muzâri «der»; fâili gizli «hüve» («kull») — cümle haber olarak mahallen merfû.", p=":"),
  T("لَقَدْ", "qad", "part", ["qad-harf", "al-qasam-wal-shart-fil-kafiya"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مُقَدَّرٍ، وَقَدْ حَرْفُ تَحْقِيقٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "The lam answering an understood oath, and قَدْ «indeed» confirming the past verb.", "Lâm takdîrî bir kasemin cevabındadır; «kad» tahkîk harfi.", segs=[("لَ", "lam-jawab", "part"), ("قَدْ", "qad", "part")]),
  T("أَخَذْتِ", "akhadha", "verb", ["mahmuz-verbs", "al-bariz-al-muttasil"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا، وَهِيَ فِي مَوْضِعِ مَقُولِ الْقَوْلِ.",
    "A past verb built on sukun before the doer's ta, which (with kasra: «you», a woman) is its doer — the clause answers the oath; together they are what was said.", "Fâil tâsı bitiştiği için sükûn üzere mebnî mâzî; kesreli tâ («sen», kadın) fâildir — cümle kasemin cevabıdır; hepsi mekūlü'l-kavldir.",
    segs=[("أَخَذْ", "akhadha", "verb"), ("تِ", "pron-2fs", "pron")]),
  T("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ مَبْنِيٌّ عَلَى السُّكُونِ — وَالنِّدَاءُ مُعْتَرِضٌ بَيْنَ الْفِعْلِ وَمَفْعُولِهِ.", "يَا, the particle of calling — the call is set between the verb and its object.", "«Yâ» nidâ harfi — nidâ fiil ile mef'ûlü arasına girmiştir."),
  T("حَلِيمَةُ", "halima-sadiyya", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The one called, a single proper name, built on damma, in the seat of nasb.", "Münâdâ müfred alem, damme üzere mebnî, mahallen mansûb.", p="!"),
  T("نَسَمَةً", "nasama", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ لِـ«أَخَذْتِ» مَنْصُوبٌ بِالْفَتْحَةِ — وَالنَّسَمَةُ: النَّفْسُ وَالرُّوحُ.", "The object of «you have taken», in nasb — نَسَمَة «a soul, a living being».", "«Ehazti»nin mef'ûlü, mansûb — neseme: can, ruh."),
  T("مُبَارَكَةً", "mubarak", "noun", ["naat-sifa", "ism-maful"], "نَعْتٌ لِـ«نَسَمَةً» مَنْصُوبٌ بِالْفَتْحَةِ.", "An adjective of «soul», in nasb: «blessed».", "«Neseme»nin na'tı, mansûb: «mübarek».", p="،"),
  T("وَحَسَدَتْهَا", "hasada", "verb", ["atf-nasaq", "thulathi-mujarrad-babs", "al-bariz-al-muttasil"], "الْوَاوُ عَاطِفَةٌ، وَحَسَدَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى حَلِيمَةَ، وَالْفَاعِلُ بَعْدَهُ.",
    "The waw conjoins; «envied» is a past verb, the ta of the feminine; «her» (Ḥalīma) its object; its doer follows.", "Vâv atıf; «hasedet» mâzî, tâ te'nîs için; zamir (Halîme) mef'ûlün bih; fâili sonra gelir.", segs=[("وَ", "wa", "conj"), ("حَسَدَتْ", "hasada", "verb"), ("هَا", "pron-3fs", "pron")]),
  T("صَوَاحِبُهَا", "sahiba-companion", "noun", ["fail", "jam-taksir", "al-bariz-al-muttasil"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ «صَاحِبَةٍ» عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ.",
    "The doer, in raf', annexed to «her» — the plural of صَاحِبَة «a (woman) companion», on the farthest plural pattern.", "Fâil, merfû, muzâf; zamir muzâfun ileyh — «sâhibe»nin müntehe'l-cumû' vezninde cemi.", p=".", enc="هَا")]),
]
NEW = {
 "inatafa": NV("اِنْعَطَفَ", "ع ط ف", "VII", "to incline, to lean (towards) in tenderness", "meyletmek, şefkatle yönelmek", level=5),
 "liban-nursing": NN("لِبَان", "ل ب ن", "suckling; a woman's own milk", "emzirme; kadının kendi sütü", level=6),
 "atan": NN("أَتَان", "أ ت ن", "a she-donkey", "dişi eşek", level=5),
 "sahiba-companion": NN("صَاحِبَة", "ص ح ب", "a (woman) companion (pl. صَوَاحِب)", "kadın arkadaş (cemi: savâhib)", level=4),
}
GLOSS_HERE = {"insarafa": ("to turn away, to go off", "yüz çevirip gitmek")}
V = {"inatafa": SG.derived(SG.B7, SG.W7, "َ", "اِنْعَطَف", "نْعَطِف", "اِنْعَطِف", "اِنْعِطَاف", "مُنْعَطِف", None, None, None, "اِنْعَطَفَ عَلَيْهِ يَنْعَطِفُ: مَالَ إِلَيْهِ.")}
