# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 2: «وَإِلَى مَدْيَنَ أَخَاهُمْ شُعَيْبًا» — sections 3–4 of the story of Shuʿayb (print pp. 2–4):
the people of Madyan on the great trade road, their shirk and their cheating of the measure, Shuʿayb sent to them with
11:84–85, and his first appeal — what is left over after honest measure is better (5:100, 11:86).
The vowelling is the print's; the sentences are the print's clauses. python3 tools/authoring/author_qisas4_ch2.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "وَإِلَى مَدْيَنَ أَخَاهُمْ شُعَيْبًا", "en": "And to Madyan, their brother Shuʿayb", "tr": "Medyen'e de kardeşleri Şuayb'ı"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; NF = "naib-al-fail"

def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def atf_majrur(full, lex, en, tr, punct=None, tags=(), ar="مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ."):
    return tok(full, lex, "noun", [AT] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَالِاسْمُ " + ar, en, tr, punct=punct, segments=wa_(full[2:], lex, "noun"))
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=(), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [ID] + list(tags), ar, en, tr, punct=punct)
def naat(full, lex, en, tr, punct=None, tags=(), case="jarr"):
    C = {"jarr": "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
    return tok(full, lex, "noun", [NA] + list(tags), C, en + " — the naʿt.", tr + " — sıfat.", punct=punct)
def prep_pron(full, lex, pron_form, pron_lex, en, tr, punct=None, tags=(), extra_ar=""):
    pre = full[:len(full) - len(pron_form)]
    return tok(full, lex, "prep", [HJ] + list(tags), "حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra_ar + ".", en, tr, punct=punct, segments=[seg(pre, lex, "prep"), seg(pron_form, pron_lex, "pron")])
def khamsa_pl(full, lex, en, tr, tags=(), punct=None, wa=False, obj=None, extra=""):
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + ([seg(full[2:] if wa else full, lex, "verb")] if not obj else [seg((full[2:] if wa else full)[:-len(obj)], lex, "verb"), seg(obj, "pron-3fs" if obj == "هَا" else "pron-3mp", "pron")])
    return tok(full, lex, "verb", [AK, "mudari-marfu"] + list(tags) + ([AT] if wa else []) + ([MB] if obj else []), W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ" + ("، وَالضَّمِيرُ مَفْعُولٌ بِهِ" if obj else "") + extra + ".", Wen(wa) + en, Wtr(wa) + tr, punct=punct, segments=segs if (wa or obj) else None)
def maful_(full, lex, en, tr, punct=None, tags=(), ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [MB] + list(tags), ar, en, tr, punct=punct)
def atf_mansub(full, lex, en, tr, punct=None, tags=()): return tok(full, lex, "noun", [AT] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَالِاسْمُ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.", en, tr, punct=punct, segments=wa_(full[2:], lex, "noun"))
def la_nahiya_verb(full, lex, en, tr, punct=None, wa=True, tags=(), obj=None):
    base = full.split()[-1] if " " in full else (full[2:] if wa else full)   # (wave 32) the verb after «وَلَا » — the lā is its own token
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg("لَا", "la-nahiya", "part")]
    return [tok(("وَلَا" if wa else "لَا"), "la-nahiya", "part", ["la-nahiya"] + ([AT] if wa else []), W(wa) + "لَا نَاهِيَةٌ جَازِمَةٌ.", Wen(wa) + "«do not» — the prohibiting lā, which puts the verb in jazm.", Wtr(wa) + "«-mayın» — cezm eden nehiy lâ'sı.", segments=(wa_("لَا", "la-nahiya", "part") if wa else None)),
            tok(base, lex, "verb", ["la-nahiya", AK] + list(tags) + ([MB] if obj else []), "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا، وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ" + ("، وَالضَّمِيرُ مَفْعُولٌ بِهِ" if obj else "") + ".", en + " — majzūm by lā: the nūn dropped.", tr + " — lâ ile meczûm: nûn düşmüş.", punct=punct, segments=([seg(base[:-len(obj)], lex, "verb"), seg(obj, "pron-3mp", "pron")] if obj else None))]

# ---------------------------------------------------------------- §3
sen("s1", "And what we have told you of the stories of the prophets is not all that God has told of their stories and accounts in the Qur'an; in the Qur'an there are stories other than these.",
        "Size peygamberlerin kıssalarından anlattıklarımız, Allah'ın Kur'an'da onların kıssa ve hikâyelerinden anlattığının hepsi değildir; Kur'an'da bu kıssalardan başka kıssalar da vardır.", [
  tok("وَلَيْسَ", "laysa", "verb", [AT, "ma-la-mushabbaha", KN], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", "«and is not» — the frozen verb of negation.", "«ve değildir» — câmid nefy fiili.", segments=wa_("لَيْسَ", "laysa", "verb")),
  tok("مَا", "ma-mawsula", "pron", [MW, KN], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ اسْمُ لَيْسَ.", "«what» — the relative; the ism of laysa.", "«… şey» — ism-i mevsûl; leyse'nin ismi."),
  tok("حَكَيْنَاهُ", "haka", "verb", [MW, FL, MB, "naqis-verbs"], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةٌ.", "«we told» — nā the doer, the hā its object; the ṣila.", "«anlattığımız» — nâ fâil, hâ mef'ûl; sıla.", segments=[seg("حَكَيْ", "haka", "verb"), seg("نَا", "pron-1p", "pron"), pr3ms()]),
  prep_pron("لَكُمْ", "li", "كُمْ", "pron-2mp", "«to you»", "«size»"),
  tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«of»", "«-den»"), mudaf_ilayh("قِصَصِ", "qasas", "«the stories of»", "«kıssalarından»", tags=[HJ], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  tok("النَّبِيِّينَ", "nabi", "noun", [ID, "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the prophets» — in jarr by the yāʾ.", "«peygamberlerin» — yâ ile mecrûr.", punct="،"),
  tok("هُوَ", "huwa", "pron", ["damir-fasl", KN], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ — أَوْ مُبْتَدَأٌ وَمَا بَعْدَهُ خَبَرُهُ، وَالْجُمْلَةُ خَبَرُ لَيْسَ.", "«it» — the pronoun of separation.", "«o» — fasl zamiri."),
  tok("كُلَّ", "kull", "noun", [KN, ID], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«all of» — the khabar of laysa, annexed.", "«hepsi» — leyse'nin haberi, muzâf."),
  tok("مَا", "ma-mawsula", "pron", [MW, ID], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that which» — the relative, annexed to.", "«… şeyin» — ism-i mevsûl, muzâfun ileyh."),
  tok("حَكَاهُ", "haka", "verb", [MW, MB, "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«told» — the hā its object; the ṣila.", "«anlattığı» — hâ mef'ûl; sıla.", segments=[seg("حَكَا", "haka", "verb"), pr3ms()]),
  allah_fail(), fi(), tok("الْقُرْآنِ", "quran", "noun", [HJ], "مَجْرُورٌ بِفِي.", "«the Qur'an»", "«Kur'an'da»"),
  tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«of»", "«-den»"),
  tok("قِصَصِهِمْ", "qasas", "noun", [HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«their stories»", "«onların kıssalarından»", segments=[seg("قِصَصِ", "qasas", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("وَحِكَايَاتِهِمْ", "hikaya", "noun", [AT, ID, "jam-muannath-salim"], "الْوَاوُ عَاطِفَةٌ، وَحِكَايَاتِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ — مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«and their accounts»", "«ve hikâyelerinden»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("حِكَايَاتِ", "hikaya", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("فَفِي", "fi", "prep", [HJ, MK], "الْفَاءُ لِلتَّعْلِيلِ، وَفِي حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«for in» — the fronted khabar.", "«zira … -de» — mukaddem haber.", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep")]),
  tok("الْقُرْآنِ", "quran", "noun", [HJ], "مَجْرُورٌ بِفِي.", "«the Qur'an»", "«Kur'an»"),
  tok("قِصَصٌ", "qasas", "noun", [MK, "jam-taksir"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«stories» — the delayed mubtada.", "«kıssalar» — muahhar mübtedâ."),
  tok("غَيْرُ", "ghayr", "noun", [NA, ID], "نَعْتٌ مَرْفُوعٌ، مُضَافٌ.", "«other than» — the naʿt, annexed.", "«başka» — sıfat, muzâf."),
  tok("هٰذِهِ", "hadhihi", "pron", ["asma-al-ishara", ID], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«these»", "«bu»"),
  tok("الْقِصَصِ", "qasas", "noun", ["badal", "jam-taksir"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«stories» — the badal.", "«kıssalardan» — bedel.", punct="."),
])
sen("s2", "In it is the story of God's prophet Shuʿayb, whom God sent to Madyan and the people of the Thicket — folk of trade and merchandise;",
        "Onda, Allah'ın Medyen'e ve Eyke halkına gönderdiği, Allah'ın peygamberi Şuayb'ın kıssası vardır — onlar ticaret ve mal sahibi bir topluluktu;", [
  tok("فِيهِ", "fi", "prep", [HJ, MK], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«in it» — the fronted khabar.", "«onda» — mukaddem haber.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("قِصَّةُ", "qissa", "noun", [MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the story of» — the delayed mubtada, annexed.", "«kıssası» — muahhar mübtedâ, muzâf."),
  tok("نَبِيِّ", "nabi", "noun", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the prophet of»", "«peygamberi»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("شُعَيْبٍ", "shuayb", "propn", ["badal"], "بَدَلٌ مِنْ نَبِيِّ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ عَرَبِيٌّ مُنْصَرِفٌ.", "«Shuʿayb» — the badal; an Arabic name, it declines in full.", "«Şuayb» — bedel; munsarif Arapça alem."),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ لِشُعَيْبٍ.", "«whom» — the relative, qualifying Shuʿayb.", "«… -diği» — ism-i mevsûl, Şuayb'ın sıfatı."),
  tok("أَرْسَلَهُ", "arsala", "verb", [MW, MB, "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«sent him» — the ṣila.", "«onu gönderdi» — sıla.", segments=[seg("أَرْسَلَ", "arsala", "verb"), pr3ms()]),
  allah_fail(), tok("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَدْيَنَ", "madyan", "propn", [HJ, "mamnu-min-sarf"], "مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.", "«Madyan» — a diptote: fatḥa for the kasra.", "«Medyen» — gayr-i munsarif: kesre yerine fetha."),
  tok("وَأَصْحَابِ", "sahib", "noun", [AT, ID, "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَأَصْحَابِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the people of»", "«ve halkına»", segments=wa_("أَصْحَابِ", "sahib", "noun")),
  mudaf_ilayh("الْأَيْكَةِ", "ayka", "«the Thicket»", "«Eyke»", punct="،"),
  tok("وَهُمْ", "hum", "pron", ["hal", MK], "الْوَاوُ لِلْحَالِ، وَهُمْ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and they» — the wāw of the ḥāl; the mubtada.", "«ve onlar» — hâl vâvı; mübtedâ.", segments=wa_("هُمْ", "hum", "pron")),
  tok("أَصْحَابُ", "sahib", "noun", [MK, ID, "jam-taksir"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«folk of» — the khabar, annexed.", "«sahibi» — haber, muzâf."),
  mudaf_ilayh("تِجَارَةٍ", "tijara", "«trade»", "«ticaret»"), atf_majrur("وَسِلَعٍ", "sila-goods", "«and merchandise»", "«ve mal»", punct="،", tags=["jam-taksir"]),
])
sen("s3", "for they were on the great trade road between Yemen and Syria and between Iraq and Egypt, on the shore of the Red Sea.",
        "zira Yemen ile Şam ve Irak ile Mısır arasındaki büyük ticaret yolu üzerinde, Kızıldeniz kıyısında idiler.", [
  tok("فَقَدْ", "qad", "part", ["qad-harf"], "الْفَاءُ لِلتَّعْلِيلِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«for indeed»", "«zira gerçekten»", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("كَانُوا", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«they were» — kāna, the wāw its ism.", "«idiler» — kâne, vâv ismi."),
  tok("عَلَى", "ala", "prep", [HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«on» — the phrase is kāna's khabar.", "«üzerinde» — câr-mecrûr kâne'nin haberi."),
  majrur("الْجَادَّةِ", "jadda", "«the road»", "«yolu»"), naat("التِّجَارِيَّةِ", "tijari", "«trade»", "«ticaret»", tags=["ism-mansub"]), naat("الْكَبِيرَةِ", "kabir", "«great»", "«büyük»"),
  tok("بَيْنَ", "bayna", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«between»", "«arasında»"),
  mudaf_ilayh("الْيَمَنِ", "yaman", "«Yemen»", "«Yemen»"), atf_majrur("وَالشَّامِ", "sham", "«and Syria»", "«ile Şam»"),
  tok("وَبَيْنَ", "bayna", "noun", [AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ ظَرْفٌ مَعْطُوفٌ، مُضَافٌ.", "«and between»", "«ve … arasında»", segments=wa_("بَيْنَ", "bayna", "noun")),
  mudaf_ilayh("الْعِرَاقِ", "iraq", "«Iraq»", "«Irak»"),
  tok("وَمِصْرَ", "misr", "propn", [AT, "mamnu-min-sarf"], "الْوَاوُ عَاطِفَةٌ، وَمِصْرَ مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.", "«and Egypt» — a diptote.", "«ile Mısır» — gayr-i munsarif.", punct="،", segments=wa_("مِصْرَ", "misr", "propn")),
  tok("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«on»", "«-de»"), majrur("سَاحِلِ", "sahil", "«the shore of»", "«kıyısında»", tags=[ID], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  mudaf_ilayh("الْبَحْرِ", "bahr", "«the Sea»", "«deniz»"), naat("الْأَحْمَرِ", "ahmar", "«Red»", "«Kızıl»", punct=".", tags=["mamnu-min-sarf"]),
])
sen("s4", "They used to associate others with God, as the nations of the prophets did in every age;", "Her çağda peygamberlerin ümmetlerinin yaptığı gibi, Allah'a başkasını ortak koşuyorlardı;", [
  tok("كَانُوا", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«they used to» — kāna, the wāw its ism.", "«idiler» — kâne, vâv ismi."),
  khamsa_pl("يُشْرِكُونَ", "ashraka", "«associate» — the clause is kāna's khabar.", "«ortak koşuyorlardı» — cümle kâne'nin haberi.", tags=[KN, "form-iv-verbs"], extra=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  tok("بِاللهِ", "allah", "propn", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«with God»", "«Allah'a»", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  tok("غَيْرَهُ", "ghayr", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«others than Him» — the object.", "«O'ndan başkasını» — mef'ûl.", punct="،", segments=[seg("غَيْرَ", "ghayr", "noun"), pr3ms()]),
  tok("كَمَا", "kama", "part", [HJ, MW], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«as»", "«gibi»"),
  tok("كَانَتْ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«were» — kāna.", "«idi» — kâne."),
  tok("أُمَمُ", "umma", "noun", [KN, ID, "jam-taksir"], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ — وَخَبَرُهُ مَحْذُوفٌ: تُشْرِكُ.", "«the nations of» — the ism of kāna; its khabar «associating» dropped.", "«ümmetleri» — kâne'nin ismi; haberi mahzûf."),
  tok("الْأَنْبِيَاءِ", "nabi", "noun", [ID, "jam-taksir", "ism-mamdud"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ لِإِضَافَتِهِ — جَمْعُ نَبِيٍّ.", "«the prophets» — the plural, in jarr by the kasra because annexed.", "«peygamberlerin» — izâfetle kesreli cemi."),
  fi(), tok("كُلِّ", "kull", "noun", [HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«every»", "«her»"), mudaf_ilayh("عَصْرٍ", "asr", "«age»", "«çağda»", punct="،"),
])
sen("s5", "and — more than that — they used to give short measure and weight, skimp in the measuring, waylay the caravans, threaten and frighten them, and spread corruption in the land, as rich and powerful men do who hope for no reckoning and fear no punishment.",
        "ve — bundan da öte — ölçüyü ve tartıyı eksik tutuyor, ölçüde hile yapıyor, kervanların yolunu kesiyor, onları tehdit edip korkutuyor ve yeryüzünde bozgunculuk yapıyorlardı; hesap ummayan ve azaptan korkmayan zengin ve güçlü kimselerin yaptığı gibi.", [
  tok("وَكَانُوا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانُوا فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«and they used to»", "«ve idiler»", segments=wa_("كَانُوا", "kana", "verb")),
  tok("زِيَادَةً", "ziyada", "noun", ["maful-mutlaq", "jumla-mutarida"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ: يَزِيدُونَ زِيَادَةً — جُمْلَةٌ مُعْتَرِضَةٌ بَيْنَ كَانَ وَخَبَرِهَا.", "«more» — a parenthesis between kāna and its khabar.", "«daha da» — kâne ile haberi arasında mu'terize."),
  tok("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ.", "«than»", "«-e»"),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", HJ], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«that»", "«bu»"),
  khamsa_pl("يَنْقُصُونَ", "naqasa", "«give short» — the clause is kāna's khabar.", "«eksik tutuyorlardı» — kâne'nin haberi.", tags=[KN], extra=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  maful_("الْمِكْيَالَ", "mikyal", "«the measure»", "«ölçüyü»"), atf_mansub("وَالْمِيزَانَ", "mizan", "«and the weight»", "«ve tartıyı»", punct="،"),
  khamsa_pl("وَيُطَفِّفُونَ", "taffafa", "«and skimp»", "«ve hile yapıyorlardı»", wa=True, tags=["form-ii-verbs"]),
  fi(), majrur("الْكَيْلِ", "kayl", "«the measuring»", "«ölçüde»", punct="،", tags=["masdar"]),
  khamsa_pl("وَيَتَعَرَّضُونَ", "taarrada", "«and waylay»", "«ve yolunu kesiyorlardı»", wa=True, tags=["form-v-verbs"]),
  tok("لِلْقَوَافِلِ", "qafila", "noun", [HJ, "jam-taksir", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَالْقَوَافِلِ مَجْرُورٌ بِالْكَسْرَةِ لِدُخُولِ ال — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«the caravans» — an ultimate plural; the article gives the kasra back.", "«kervanlara» — münteha'l-cümû; harf-i tarif kesreyi geri verir.", punct="،", segments=[seg("لِ", "li", "prep"), seg("الْقَوَافِلِ", "qafila", "noun")]),
  tok("فَيَتَوَعَّدُونَهَا", "tawaada", "verb", [AT, AK, MB, "form-v-verbs"], "الْفَاءُ عَاطِفَةٌ، وَيَتَوَعَّدُونَ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ.", "«and threaten them»", "«ve onları tehdit ediyorlardı»", segments=[seg("فَ", "fa", "conj"), seg("يَتَوَعَّدُونَ", "tawaada", "verb"), pr3fs_()]),
  tok("وَيُخِيفُونَهَا", "akhafa", "verb", [AT, AK, MB, "form-iv-verbs", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُخِيفُونَ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ.", "«and frighten them»", "«ve onları korkutuyorlardı»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("يُخِيفُونَ", "akhafa", "verb"), pr3fs_()]),
  khamsa_pl("وَيَعِيثُونَ", "atha", "«and spread»", "«ve yapıyorlardı»", wa=True, tags=["hollow-verbs"]),
  fi(), majrur("الْأَرْضِ", "ard", "«the land»", "«yeryüzünde»"),
  tok("فَسَادًا", "fasad", "noun", ["tamyiz", "masdar"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — أَوْ مَفْعُولٌ مُطْلَقٌ.", "«corruption» — the tamyīz.", "«bozgunculuk» — temyiz.", punct="،"),
  tok("شَأْنَ", "shan", "noun", ["maful-mutlaq", ID], "مَفْعُولٌ مُطْلَقٌ نَائِبٌ عَنِ الْمَصْدَرِ مَنْصُوبٌ، مُضَافٌ — أَيْ: يَفْعَلُونَ فِعْلَ الْأَغْنِيَاءِ.", "«as … do» — the absolute object's deputy, annexed.", "«… gibi» — masdarın yerine mef'ûl-i mutlak, muzâf."),
  mudaf_ilayh("الْأَغْنِيَاءِ", "ghani", "«the rich»", "«zenginlerin»", tags=["jam-taksir", "ism-mamdud"]),
  naat("الْأَقْوِيَاءِ", "qawi", "«powerful»", "«güçlü»", punct="،", tags=["jam-taksir", "ism-mamdud"]),
  tok("الَّذِينَ", "alladhina", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ.", "«who» — the relative, a naʿt.", "«… olan» — ism-i mevsûl, sıfat."),
  la_nafiya(), khamsa_pl("يَرْجُونَ", "raja", "«hope for» — the ṣila.", "«ummayan» — sıla.", tags=[MW, "la-nafiya", "naqis-verbs"]),
  maful_("حِسَابًا", "hisab", "«a reckoning»", "«hesap»"),
  la_nafiya("وَلَا", wa=True), khamsa_pl("يَخْشَوْنَ", "khashiya", "«fear»", "«korkmayan»", tags=["la-nafiya", "naqis-verbs"]),
  maful_("عَذَابًا", "adhab", "«a punishment»", "«azap»", punct="."),
])
sen("s6", "God sent to them His messenger Shuʿayb, calling them and warning them, and saying to them:", "Allah onlara, kendilerini davet eden ve uyaran elçisi Şuayb'ı gönderdi; onlara diyordu ki:", [
  mazi("بَعَثَ", "baatha", "«sent»", "«gönderdi»", hidden=None), allah_fail(),
  prep_pron("إِلَيْهِمْ", "ila", "هِمْ", "pron-3mp", "«to them»", "«onlara»"),
  tok("رَسُولَهُ", "rasul", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His messenger» — the object.", "«elçisi» — mef'ûl.", segments=[seg("رَسُولَ", "rasul", "noun"), pr3ms()]),
  tok("شُعَيْبًا", "shuayb", "propn", ["badal"], "بَدَلٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Shuʿayb» — the badal.", "«Şuayb'ı» — bedel."),
  tok("يَدْعُوهُمْ", "daa", "verb", ["hal", MB, "naqis-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ حَالٌ.", "«calling them» — the clause is a ḥāl.", "«onları davet ederek» — cümle hâl.", segments=[seg("يَدْعُو", "daa", "verb"), pr3mp()]),
  tok("وَيُنْذِرُهُمْ", "andhara", "verb", [AT, MB, "form-iv-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيُنْذِرُ مُضَارِعٌ مَرْفُوعٌ، وَهُمْ مَفْعُولٌ بِهِ.", "«and warning them»", "«ve onları uyararak»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("يُنْذِرُ", "andhara", "verb"), pr3mp()]),
  tok("وَيَقُولُ", "qala", "verb", [AT, "hollow-verbs", "mudari-marfu", MB], "الْوَاوُ عَاطِفَةٌ، وَيَقُولُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«and saying» — what is said is its object.", "«ve diyerek» — söylenen söz mef'ûlü.", segments=wa_("يَقُولُ", "qala", "verb")),
  prep_pron("لَهُمْ", "li", "هُمْ", "pron-3mp", "«to them»", "«onlara»", punct=":"),
])
sen("s7", "«O my people, worship God; you have no god but Him. And do not give short measure and weight; I see you in prosperity, and I fear for you the punishment of an encompassing day» (11:84).",
        "«Ey kavmim, Allah'a kulluk edin; sizin O'ndan başka ilâhınız yoktur. Ölçüyü ve tartıyı eksik tutmayın; ben sizi bolluk içinde görüyorum ve sizin için kuşatıcı bir günün azabından korkuyorum» (11:84).", quran([
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("قَوْمِ", "qawm", "noun", ["vocative-munada", ID, "ya-al-mutakallim"], "مُنَادًى مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا.", "«my people» — the munādā, annexed to the dropped yāʾ of the speaker: the kasra marks it.", "«kavmim» — münâdâ, hazfedilmiş mütekellim yâsına muzâf: kesre ona delil."),
  tok("اعْبُدُوا", "abada", "verb", ["imperative-amr", MB], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«worship» — the command, built on the nūn's dropping.", "«kulluk edin» — nûnun hazfi üzere mebnî emir."),
  allah_ism("اللهَ", part="الْفِعْل") if False else tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«God» — the object.", "«Allah'a» — mef'ûl."),
  tok("مَا", "ma-nafiya", "part", ["anwa-ma", MK], "حَرْفُ نَفْيٍ.", "«not»", "«yoktur»"),
  prep_pron("لَكُمْ", "li", "كُمْ", "pron-2mp", "«for you» — the fronted khabar.", "«sizin» — mukaddem haber.", tags=[MK]),
  tok("مِنْ", "min", "prep", [HJ, "huruf-jarr-nawadir"], "حَرْفُ جَرٍّ زَائِدٌ لِتَأْكِيدِ النَّفْيِ.", "«any» — the added min that strengthens the negation.", "«hiç» — nefyi pekiştiren zâid min."),
  tok("إِلٰهٍ", "ilah", "noun", [MK, HJ], "مُبْتَدَأٌ مُؤَخَّرٌ مَجْرُورٌ لَفْظًا بِمِنْ الزَّائِدَةِ، مَرْفُوعٌ مَحَلًّا.", "«god» — the delayed mubtada, in jarr by the added min on the surface, in rafʿ by place.", "«ilâh» — muahhar mübtedâ; lafzan zâid min ile mecrûr, mahallen merfû."),
  tok("غَيْرُهُ", "ghayr", "noun", [NA, ID], "نَعْتٌ لِإِلٰهٍ عَلَى الْمَحَلِّ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَوْ بَدَلٌ.", "«but Him» — the naʿt on the place of «god», in rafʿ.", "«O'ndan başka» — mahallen sıfat, merfû.", segments=[seg("غَيْرُ", "ghayr", "noun"), pr3ms()]),
  *la_nahiya_verb("وَلَا تَنْقُصُوا", "naqasa", "«do not give short»", "«eksik tutmayın»"),
  maful_("الْمِكْيَالَ", "mikyal", "«the measure»", "«ölçüyü»"), atf_mansub("وَالْمِيزَانَ", "mizan", "«and the weight»", "«ve tartıyı»"),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«indeed I» — inna with the speaker's yāʾ as its ism.", "«şüphesiz ben» — inne, yâ ismi.", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أَرَاكُمْ", "raa", "verb", [IW, MB, "naqis-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَكُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I see you» — the khabar of inna.", "«sizi görüyorum» — inne'nin haberi.", segments=[seg("أَرَا", "raa", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  tok("بِخَيْرٍ", "khayr", "noun", [HJ, "hal"], "الْبَاءُ حَرْفُ جَرٍّ، وَخَيْرٍ مَجْرُورٌ — حَالٌ: فِي خَيْرٍ.", "«in prosperity» — a ḥāl.", "«bolluk içinde» — hâl.", segments=[seg("بِ", "bi", "prep"), seg("خَيْرٍ", "khayr", "noun")]),
  tok("وَإِنِّي", "inna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«and indeed I»", "«ve şüphesiz ben»", segments=[seg("وَ", "wa", "conj"), seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أَخَافُ", "khafa", "verb", [IW, "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — خَبَرُ إِنَّ.", "«I fear» — the khabar of inna.", "«korkuyorum» — inne'nin haberi."),
  prep_pron("عَلَيْكُمْ", "ala", "كُمْ", "pron-2mp", "«for you»", "«sizin için»"),
  tok("عَذَابَ", "adhab", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«the punishment of» — the object, annexed.", "«azabından» — mef'ûl, muzâf."),
  mudaf_ilayh("يَوْمٍ", "yawm", "«a day»", "«bir günün»"), naat("مُحِيطٍ", "muhit", "«encompassing»", "«kuşatıcı»", punct=".", tags=["ism-fail", "form-iv-verbs", "hollow-verbs"]),
]))
sen("s8", "«And O my people, give full measure and weight in justice, and do not deprive people of their things, and do not go about the land spreading corruption» (11:85).",
        "«Ey kavmim, ölçüyü ve tartıyı adaletle tam yapın; insanların eşyasını eksiltmeyin ve yeryüzünde bozgunculuk yaparak dolaşmayın» (11:85).", quran([
  tok("وَيَا", "ya-nida", "part", [AT, "vocative-munada"], "الْوَاوُ عَاطِفَةٌ، وَيَا حَرْفُ نِدَاءٍ.", "«and O»", "«ve ey»", segments=wa_("يَا", "ya-nida", "part")),
  tok("قَوْمِ", "qawm", "noun", ["vocative-munada", ID, "ya-al-mutakallim"], "مُنَادًى مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ.", "«my people» — the munādā.", "«kavmim» — münâdâ."),
  tok("أَوْفُوا", "awfa", "verb", ["imperative-amr", MB, "form-iv-verbs", "naqis-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«give full» — the command.", "«tam yapın» — emir."),
  maful_("الْمِكْيَالَ", "mikyal", "«the measure»", "«ölçüyü»"), atf_mansub("وَالْمِيزَانَ", "mizan", "«and the weight»", "«ve tartıyı»"),
  tok("بِالْقِسْطِ", "qist", "noun", [HJ, "hal"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْقِسْطِ مَجْرُورٌ — حَالٌ: عَادِلِينَ.", "«in justice» — a ḥāl.", "«adaletle» — hâl.", segments=[seg("بِ", "bi", "prep"), seg("الْقِسْطِ", "qist", "noun")]),
  *la_nahiya_verb("وَلَا تَبْخَسُوا", "bakhasa", "«do not deprive»", "«eksiltmeyin»"),
  maful_("النَّاسَ", "nas", "«people»", "«insanları»"),
  tok("أَشْيَاءَهُمْ", "shay", "noun", ["mafulayn", ID, "jam-taksir", "mamnu-min-sarf"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — أَشْيَاءُ مَمْنُوعَةٌ مِنَ الصَّرْفِ.", "«their things» — the second object; أَشْيَاء is a diptote.", "«eşyalarını» — ikinci mef'ûl; eşyâ gayr-i munsarif.", segments=[seg("أَشْيَاءَ", "shay", "noun"), pr3mp()]),
  *la_nahiya_verb("وَلَا تَعْثَوْا", "atha", "«do not go about»", "«dolaşmayın»", tags=["hollow-verbs"]),
  fi(), majrur("الْأَرْضِ", "ard", "«the land»", "«yeryüzünde»"),
  tok("مُفْسِدِينَ", "mufsid", "noun", ["hal", "jam-mudhakkar-salim", "ism-fail", "form-iv-verbs"], "حَالٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«spreading corruption» — the ḥāl, in naṣb by the yāʾ.", "«bozgunculuk yaparak» — hâl, yâ ile mansûb.", punct="."),
]))
# ---------------------------------------------------------------- §4
sen("s9", "And he speaks to them at length and unties a knot in their souls — the knot of love of wealth and of gain — and says:", "Onlara uzun uzun anlatır, içlerindeki bir düğümü çözer — mal ve kazanç sevgisi düğümünü — ve der ki:", [
  tok("وَيَبْسُطُ", "basata", "verb", [AT, "mudari-marfu"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَبْسُطُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and he speaks at length» — literally «spreads out».", "«ve uzun uzun anlatır» — «yayar».", segments=wa_("يَبْسُطُ", "basata", "verb")),
  prep_pron("لَهُمْ", "li", "هُمْ", "pron-3mp", "«to them»", "«onlara»"),
  fi(), majrur("الْكَلَامِ", "kalam", "«speech»", "«sözde»"),
  tok("وَيَحُلُّ", "halla-settle", "verb", [AT, "doubled-verbs", "mudari-marfu", MB], "الْوَاوُ عَاطِفَةٌ، وَيَحُلُّ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — حَلَّ الْعُقْدَةَ: فَكَّهَا.", "«and unties» — ḥalla here: to loosen.", "«ve çözer» — halle: çözmek.", segments=wa_("يَحُلُّ", "halla-settle", "verb")),
  maful_("عُقْدَةً", "uqda", "«a knot»", "«bir düğümü»"),
  fi(), tok("نُفُوسِهِمْ", "nafs", "noun", [HJ, ID, "jam-taksir"], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«their souls»", "«içlerinde»", punct="،", segments=[seg("نُفُوسِ", "nafs", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("وَهِيَ", "hiya", "pron", [MK, "jumla-mutarida"], "الْوَاوُ لِلِاعْتِرَاضِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is» — the mubtada of a parenthesis.", "«ve o» — mu'terize cümlenin mübtedâsı.", segments=wa_("هِيَ", "hiya", "pron")),
  tok("عُقْدَةُ", "uqda", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the knot of» — the khabar, annexed.", "«düğümü» — haber, muzâf."),
  mudaf_ilayh("حُبِّ", "hubb", "«love of»", "«sevgisi»", tags=["masdar"], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  mudaf_ilayh("الْمَالِ", "mal", "«wealth»", "«mal»"), atf_majrur("وَالزِّيَادَةِ", "ziyada", "«and of gain»", "«ve fazlalık»", punct="،"),
  tok("فَيَقُولُ", "qala", "verb", [AT, "hollow-verbs", "mudari-marfu", MB], "الْفَاءُ عَاطِفَةٌ، وَيَقُولُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَمَقُولُ الْقَوْلِ مَفْعُولُهُ.", "«and says»", "«ve der ki»", punct=":", segments=[seg("فَ", "fa", "conj"), seg("يَقُولُ", "qala", "verb")]),
])
sen("s10", "What remains to you of profit after giving full measure and weight is better for you than taking people's wealth by wrong and treachery;",
         "Ölçüyü ve tartıyı tam verdikten sonra size kalan kâr, insanların mallarını zulüm ve hıyanetle almaktan sizin için daha hayırlıdır;", [
  inna(), tok("مَا", "ma-mawsula", "pron", [MW, IW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«what» — the relative; the ism of inna.", "«… şey» — ism-i mevsûl; inne'nin ismi."),
  tok("يَفْضُلُ", "fadala", "verb", [MW, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةٌ.", "«remains over» — the ṣila.", "«artan» — sıla."),
  prep_pron("لَكُمْ", "li", "كُمْ", "pron-2mp", "«to you»", "«size»"),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"), majrur("الرِّبْحِ", "ribh", "«profit»", "«kâr»"),
  tok("بَعْدَ", "bada", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  mudaf_ilayh("وَفَاءِ", "wafa", "«giving full»", "«tam vermekten»", tags=["masdar", "ism-mamdud"], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  mudaf_ilayh("الْكَيْلِ", "kayl", "«the measure»", "«ölçüyü»"), atf_majrur("وَالْمِيزَانِ", "mizan", "«and the weight»", "«ve tartıyı»"),
  khabar_inna("خَيْرٌ", "khayr", "«better»", "«daha hayırlı»", tags=["ism-tafdil"]),
  prep_pron("لَكُمْ", "li", "كُمْ", "pron-2mp", "«for you»", "«sizin için»"),
  tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ — مِنْ التَّفْضِيلِيَّةُ.", "«than»", "«-den»"),
  majrur("أَخْذِ", "akhdh", "«taking»", "«almaktan»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("أَمْوَالِ", "mal", "«the wealth of»", "«mallarını»", tags=["jam-taksir"], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."), mudaf_ilayh("النَّاسِ", "nas", "«people»", "«insanların»"),
  tok("بِالظُّلْمِ", "zulm", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالظُّلْمِ مَجْرُورٌ.", "«by wrong»", "«zulümle»", segments=[seg("بِ", "bi", "prep"), seg("الظُّلْمِ", "zulm", "noun")]),
  atf_majrur("وَالْخِيَانَةِ", "khiyana", "«and treachery»", "«ve hıyanetle»", punct="،"),
])
sen("s11", "and if you look at your own lives and at the lives of those who grew rich and amassed wealth, you find that what they earned by skimping, cheating and treachery ended in ruin and loss, or in corruption and affliction —",
         "ve kendi hayatınıza ve zenginleşip mal yığanların hayatına bakarsanız, hile, eksiltme ve hıyanet yoluyla kazandıklarının sonunun telef ve zayi olmak, yahut fesat ve belâ olduğunu görürsünüz;", [
  tok("وَإِذَا", "idha", "part", [AT, "idha-shartiyya", MF], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the conditional ẓarf.", "«ve … -sanız» — şart mânâlı zarf.", segments=wa_("إِذَا", "idha", "part")),
  tok("نَظَرْتُمْ", "nazara", "verb", ["idha-shartiyya", FL], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — فِعْلُ الشَّرْطِ.", "«you look» — the condition's verb.", "«bakarsanız» — şart fiili.", segments=[seg("نَظَرْ", "nazara", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  fi(), tok("حَيَاتِكُمْ", "hayat", "noun", [HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your lives»", "«hayatınıza»", segments=[seg("حَيَاتِ", "hayat", "noun"), pr2mp()]),
  tok("وَفِي", "fi", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and at»", "«ve»", segments=wa_("فِي", "fi", "prep")),
  majrur("حَيَاةِ", "hayat", "«the lives of»", "«hayatına»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  tok("هٰؤُلَاءِ", "haulai", "pron", ["asma-al-ishara", ID], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«those»", "«şu»"),
  tok("الَّذِينَ", "alladhina", "pron", [MW, "badal"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ.", "«who» — the relative, the badal.", "«… olanların» — ism-i mevsûl, bedel."),
  tok("أَثْرَوْا", "athra", "verb", [MW, "form-iv-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ — صِلَةٌ.", "«grew rich» — the alif dropped before the group's wāw; the ṣila.", "«zenginleşen» — cemi vâvından önce elif düşmüş; sıla."),
  tok("وَجَمَعُوا", "jamaa-gather", "verb", [AT, MB], "الْوَاوُ عَاطِفَةٌ، وَجَمَعُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«and amassed»", "«ve yığan»", segments=wa_("جَمَعُوا", "jamaa-gather", "verb")),
  maful_("الْأَمْوَالَ", "mal", "«wealth»", "«malları»", punct="،", tags=["jam-taksir"]),
  tok("وَجَدْتُمْ", "wajada", "verb", ["idha-shartiyya", FL, "mafulayn", "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — جَوَابُ إِذَا، وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ سَدَّ مَسَدَّ مَفْعُولَيْهِ.", "«you find» — the answer; the clause after it stands for its two objects.", "«bulursunuz» — cevap; ardındaki cümle iki mef'ûlün yerini tutar.", segments=[seg("وَجَدْ", "wajada", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  anna(obj_of="وَجَدْتُمْ"), tok("مَا", "ma-mawsula", "pron", [MW, IW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«what» — the ism of anna.", "«… şey» — enne'nin ismi."),
  tok("اكْتَسَبُوهُ", "iktasaba", "verb", [MW, MB, "form-viii-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«they earned» — the ṣila.", "«kazandıkları» — sıla.", segments=[seg("اكْتَسَبُو", "iktasaba", "verb"), pr3ms()]),
  tok("عَنْ", "an", "prep", [HJ], "حَرْفُ جَرٍّ.", "«by»", "«yoluyla»"), majrur("طَرِيقِ", "tariq", "«way of»", "«yolu»", tags=[ID], ar="مَجْرُورٌ بِعَنْ، مُضَافٌ."),
  mudaf_ilayh("التَّطْفِيفِ", "tatfif", "«skimping»", "«hile»", tags=["masdar"]), atf_majrur("وَالْبَخْسِ", "bakhs", "«cheating»", "«eksiltme»", tags=["masdar"]), atf_majrur("وَالْخِيَانَةِ", "khiyana", "«and treachery»", "«ve hıyanet»", punct="،"),
  tok("كَانَ", "kana", "verb", [KN, IW, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«was» — the clause is the khabar of anna.", "«oldu» — cümle enne'nin haberi."),
  tok("مَصِيرُهُ", "masir-fate", "noun", [KN, ID], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end» — the ism of kāna.", "«sonu» — kâne'nin ismi.", segments=[seg("مَصِيرُ", "masir-fate", "noun"), pr3ms()]),
  tok("إِلَى", "ila", "prep", [HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«to» — the phrase is kāna's khabar.", "«-e» — câr-mecrûr kâne'nin haberi."),
  majrur("التَّلَفِ", "talaf", "«ruin»", "«telef»", tags=["masdar"]), atf_majrur("وَالضَّيَاعِ", "daya", "«and loss»", "«ve zayi olmak»", punct="،", tags=["masdar"]),
  tok("أَوِ", "aw", "part", [AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«yahut»"),
  majrur("الْفَسَادِ", "fasad", "«corruption»", "«fesat»", ar="مَعْطُوفٌ مَجْرُورٌ.", tags=[AT]), atf_majrur("وَالْبَلَاءِ", "bala", "«and affliction»", "«ve belâ»", punct="،", tags=["ism-mamdud"]),
])
sen("s12", "so it was stolen or plundered, or spent on what does not please God, or someone was set over it who destroyed it and played with it;",
         "o mal ya çalındı, ya yağmalandı, ya Allah'ın razı olmadığı yere harcandı, ya da üzerine onu telef eden ve onunla oynayan biri musallat edildi;", [
  tok("فَسُرِقَ", "saraqa", "verb", [AT, NF], "الْفَاءُ لِلتَّفْرِيعِ، وَسُرِقَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — الْمَالُ.", "«so it was stolen» — the passive; the deputy doer is the wealth.", "«çalındı» — meçhul; nâib-i fâil mal.", segments=[seg("فَ", "fa", "conj"), seg("سُرِقَ", "saraqa", "verb")]),
  tok("أَوْ", "aw", "part", [AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya»"), tok("نُهِبَ", "nahaba", "verb", [AT, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«plundered»", "«yağmalandı»", punct="،"),
  tok("أَوْ", "aw", "part", [AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya»"), tok("أُنْفِقَ", "anfaqa", "verb", [AT, NF, "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«spent»", "«harcandı»"),
  fi(), majrur("غَيْرِ", "ghayr", "«other than»", "«olmayan yere»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  tok("مَا", "ma-mawsula", "pron", [MW, ID], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what»", "«… şey»"),
  tok("يُرْضِي", "arda", "verb", [MW, MB, "form-iv-verbs", "naqis-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةٌ.", "«pleases» — the ṣila.", "«razı eden» — sıla."),
  tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«God» — the object.", "«Allah'ı» — mef'ûl.", punct="،"),
  tok("أَوْ", "aw", "part", [AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"), tok("سُلِّطَ", "sallata", "verb", [AT, NF, "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«was set»", "«musallat edildi»"),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«over it»", "«üzerine»"),
  tok("مَنْ", "man-mawsula", "pron", [MW, NF], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَائِبُ الْفَاعِلِ.", "«someone who» — the relative; the deputy doer.", "«biri ki» — ism-i mevsûl; nâib-i fâil."),
  tok("أَتْلَفَهُ", "atlafa", "verb", [MW, MB, "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«destroyed it» — the ṣila.", "«onu telef etti» — sıla.", segments=[seg("أَتْلَفَ", "atlafa", "verb"), pr3ms()]),
  tok("وَعَبَثَ", "abatha", "verb", [AT], "الْوَاوُ عَاطِفَةٌ، وَعَبَثَ فِعْلٌ مَاضٍ.", "«and played»", "«ve oynadı»", segments=wa_("عَبَثَ", "abatha", "verb")),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«with it»", "«onunla»", punct="،"),
])
sen("s13", "and the little that benefits is better than the much that does not: «Say: the foul and the good are not equal, though the abundance of the foul may please you» (5:100).",
         "ve faydalı olan az, faydasız çoktan hayırlıdır: «De ki: pis ile temiz bir olmaz; pisin çokluğu hoşuna gitse bile» (5:100).", [
  tok("وَالْقَلِيلُ", "qalil", "noun", [AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْقَلِيلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the little» — the mubtada.", "«ve az olan» — mübtedâ.", segments=wa_("الْقَلِيلُ", "qalil", "noun")),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ.", "«that» — the relative, a naʿt.", "«… olan» — sıfat."),
  tok("يَنْفَعُ", "nafaa", "verb", [MW, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«benefits» — the ṣila.", "«fayda veren» — sıla."),
  tok("خَيْرٌ", "khayr", "noun", [MK, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — أَفْعَلُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ.", "«better» — the khabar; an elative with its hamza dropped.", "«daha hayırlı» — haber; hemzesi düşmüş ism-i tafdîl."),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«than»", "«-den»"), majrur("الْكَثِيرِ", "kathir", "«the much»", "«çok olan»"),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ.", "«that»", "«… olan»"),
  la_nafiya(), tok("يَنْفَعُ", "nafaa", "verb", [MW, "la-nafiya", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ.", "«benefits»", "«fayda vermeyen»", punct=":"),
  *quran([
  tok("قُلْ", "qala", "verb", ["imperative-amr", "hollow-verbs", MB], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — وَمَقُولُ الْقَوْلِ مَفْعُولُهُ.", "«say» — the command.", "«de ki» — emir."),
  la_nafiya(), tok("يَسْتَوِي", "istawa", "verb", ["la-nafiya", "form-viii-verbs", "naqis-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«are equal» — the ḍamma assumed on the yāʾ.", "«bir olmaz» — yâ üzerinde takdîrî damme."),
  tok("الْخَبِيثُ", "khabith", "noun", [FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the foul» — the doer.", "«pis» — fâil."),
  tok("وَالطَّيِّبُ", "tayyib", "noun", [AT], "الْوَاوُ عَاطِفَةٌ، وَالطَّيِّبُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the good»", "«ile temiz»", segments=wa_("الطَّيِّبُ", "tayyib", "noun")),
  tok("وَلَوْ", "law", "part", [AT, "in-shartiyya"], "الْوَاوُ لِلْحَالِ، وَلَوْ وَصْلِيَّةٌ — شَرْطٌ جَوَابُهُ مَحْذُوفٌ.", "«even though» — the concessive law.", "«… bile» — vaslî lev.", segments=wa_("لَوْ", "law", "part")),
  tok("أَعْجَبَكَ", "aajaba", "verb", ["in-shartiyya", MB, "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«pleases you» — the kāf its object.", "«hoşuna gitse» — kâf mef'ûl.", segments=[seg("أَعْجَبَ", "aajaba", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("كَثْرَةُ", "kathra", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the abundance of» — the doer.", "«çokluğu» — fâil."),
  mudaf_ilayh("الْخَبِيثِ", "khabith", "«the foul»", "«pisin»", punct="."),
  ]),
])
sen("s14", "And my counsel to you is pure and sincere, and God alone is the Watcher over you.", "Size nasihatim hâlis ve samimidir; sizin üzerinizde gözetleyici yalnız Allah'tır.", [
  tok("وَنَصِيحَتِي", "nasiha", "noun", [AT, MK, ID, "ya-al-mutakallim"], "الْوَاوُ عَاطِفَةٌ، وَنَصِيحَةُ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«and my counsel» — the mubtada, annexed to the speaker's yāʾ.", "«ve nasihatim» — mübtedâ, mütekellim yâsına muzâf.", segments=[seg("وَ", "wa", "conj"), seg("نَصِيحَتِ", "nasiha", "noun"), seg("ي", "pron-1s", "pron")]),
  prep_pron("لَكُمْ", "li", "كُمْ", "pron-2mp", "«to you»", "«size»"),
  tok("خَالِصَةٌ", "khalis", "noun", [MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«pure» — the khabar.", "«hâlis» — haber."),
  tok("مُخْلِصَةٌ", "mukhlis", "noun", [MK, "ism-fail", "form-iv-verbs"], "خَبَرٌ ثَانٍ مَرْفُوعٌ.", "«sincere» — a second khabar.", "«samimi» — ikinci haber.", punct="،"),
  tok("وَاللهُ", "allah", "propn", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَلَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ.", "«and God» — the mubtada.", "«ve Allah» — mübtedâ.", segments=wa_("اللهُ", "allah", "propn")),
  tok("هُوَ", "huwa", "pron", ["damir-fasl", MK], "ضَمِيرُ فَصْلٍ.", "«He» — the pronoun of separation.", "«O» — fasl zamiri."),
  tok("الرَّقِيبُ", "raqib", "noun", [MK], "خَبَرٌ مَرْفُوعٌ.", "«the Watcher» — the khabar.", "«gözetleyici» — haber."),
  prep_pron("عَلَيْكُمْ", "ala", "كُمْ", "pron-2mp", "«over you»", "«üzerinizde»"),
  tok("وَحْدَهُ", "wahda", "noun", ["hal", ID], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ: مُنْفَرِدًا.", "«alone» — the ḥāl.", "«yalnız» — hâl.", punct=".", segments=[seg("وَحْدَ", "wahda", "noun"), pr3ms()]),
])
sen("s15", "He says, with gentleness and wisdom, knowledge and insight: «What God leaves you is better for you, if you are believers; and I am not a keeper over you» (11:86).",
         "Yumuşaklık ve hikmetle, ilim ve basiretle der ki: «Eğer mü'minlerseniz Allah'ın bıraktığı sizin için daha hayırlıdır; ben sizin üzerinize bir bekçi değilim» (11:86).", [
  tok("يَقُولُ", "qala", "verb", ["hollow-verbs", "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَمَقُولُ الْقَوْلِ مَفْعُولُهُ.", "«he says»", "«der ki»"),
  fi(), majrur("رِفْقٍ", "rifq", "«gentleness»", "«yumuşaklık»", tags=["masdar"]), atf_majrur("وَحِكْمَةٍ", "hikma", "«and wisdom»", "«ve hikmet»"),
  atf_majrur("وَعِلْمٍ", "ilm", "«knowledge»", "«ilim»"), atf_majrur("وَبَصِيرَةٍ", "basira", "«and insight»", "«ve basiretle»", punct=":"),
  *quran([
  tok("بَقِيَّتُ", "baqiyya", "noun", [MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«what … leaves» — the mubtada, annexed.", "«bıraktığı» — mübtedâ, muzâf."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("خَيْرٌ", "khayr", "noun", [MK, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«better» — the khabar.", "«daha hayırlı» — haber."),
  prep_pron("لَكُمْ", "li", "كُمْ", "pron-2mp", "«for you»", "«sizin için»"),
  tok("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ — جَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«if» — its answer is implied by what precedes.", "«eğer» — cevabı öncesinden anlaşılır."),
  tok("كُنْتُمْ", "kana", "verb", ["in-shartiyya", KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ اسْمُهُ.", "«you are» — the condition's verb; the tāʾ its ism.", "«iseniz» — şart fiili; tâ ismi.", segments=[seg("كُنْ", "kana", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  tok("مُؤْمِنِينَ", "mumin", "noun", [KN, "jam-mudhakkar-salim", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«believers» — kāna's khabar, in naṣb by the yāʾ.", "«mü'minler» — kâne'nin haberi, yâ ile mansûb."),
  tok("وَمَا", "ma-hijaziyya", "part", [AT, "ma-la-mushabbaha"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ تَعْمَلُ عَمَلَ لَيْسَ.", "«and not» — the Ḥijāzī mā, governing like laysa.", "«ve değil» — leyse gibi amel eden mâ.", segments=wa_("مَا", "ma-hijaziyya", "part")),
  tok("أَنَا", "ana", "pron", ["ma-la-mushabbaha"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ مَا.", "«I» — the ism of mā.", "«ben» — mâ'nın ismi."),
  prep_pron("عَلَيْكُمْ", "ala", "كُمْ", "pron-2mp", "«over you»", "«üzerinize»"),
  tok("بِحَفِيظٍ", "hafiz-keeper", "noun", [HJ, "ma-la-mushabbaha", "huruf-jarr-nawadir"], "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَحَفِيظٍ خَبَرُ مَا مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.", "«a keeper» — the khabar of mā after the added bāʾ: jarr on the surface, naṣb by place.", "«bekçi» — zâid bâ'dan sonra mâ'nın haberi: lafzan mecrûr, mahallen mansûb.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("حَفِيظٍ", "hafiz-keeper", "noun")]),
  ]),
])

CAND = {
 "laysa": G("laysa", "لَيْسَ", None, "verb", "is not — the frozen verb of negation", "leyse — değildir; câmid nefy fiili", 2),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "that which — the relative", "mâ-i mevsûle", 3),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber, nebî", 1, plural="أَنْبِيَاء"),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "quran": G("quran", "الْقُرْآن", "ق ر أ", "propn", "the Qur'an", "Kur'ân", 1),
 "ghayr": G("ghayr", "غَيْر", None, "noun", "other than; except", "başka, gayri", 2),
 "hadhihi": G("hadhihi", "هَذِهِ", None, "pron", "this (feminine)", "bu (müennes)", 1),
 "shuayb": G("shuayb", "شُعَيْب", None, "propn", "Shuʿayb — the prophet of Madyan", "Şuayb — Medyen'in peygamberi", 1),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "who, which, that (masculine relative)", "ellezî — müzekker ism-i mevsûl", 2),
 "arsala": G("arsala", "أَرْسَلَ", "ر س ل", "verb", "to send (Form IV)", "göndermek (if'âl)", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to, towards", "-e, -e doğru", 1),
 "madyan": G("madyan", "مَدْيَن", None, "propn", "Madyan — the town of Shuʿayb's people; a diptote", "Medyen — Şuayb kavminin şehri; gayr-i munsarif", 2),
 "sahib": G("sahib", "صَاحِب", "ص ح ب", "noun", "companion, owner; أَصْحَابُ: the people of", "sahip, arkadaş; ashâb: halkı", 1, plural="أَصْحَاب"),
 "ayka": G("ayka", "الْأَيْكَة", "أ ي ك", "noun", "the Thicket — أَصْحَابُ الْأَيْكَةِ, Shuʿayb's people", "Eyke — ashâbü'l-Eyke, Şuayb'ın kavmi", 3),
 "hum": G("hum", "هُمْ", None, "pron", "they (masculine plural)", "onlar", 1),
 "tijara": G("tijara", "تِجَارَة", "ت ج ر", "noun", "trade, commerce", "ticaret", 2),
 "sila-goods": G("sila-goods", "سِلْعَة", "س ل ع", "noun", "a commodity, goods", "mal, emtia", 3, plural="سِلَع"),
 "qad": G("qad", "قَدْ", None, "part", "qad — certainty with the māḍī, possibility with the muḍāriʿ", "kad — mâzîyle tahkik, muzâriyle ihtimal", 3),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be — raises its ism and puts its khabar in naṣb", "kâne — idi; ismini ref', haberini nasb eder", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, over", "üzerine, -e", 1),
 "jadda": G("jadda", "جَادَّة", "ج د د", "noun", "a main road, a highway", "ana yol, cadde", 3),
 "tijari": G("tijari", "تِجَارِيّ", "ت ج ر", "noun", "of trade, commercial (a nisba)", "ticarî", 3),
 "kabir": G("kabir", "كَبِير", "ك ب ر", "noun", "big, great, elder", "büyük", 1, plural="كِبَار"),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between (a ẓarf)", "arasında (zarf)", 1),
 "yaman": G("yaman", "الْيَمَن", None, "propn", "Yemen", "Yemen", 1),
 "sham": G("sham", "الشَّام", None, "propn", "Syria, the Levant", "Şam", 1),
 "iraq": G("iraq", "الْعِرَاق", None, "propn", "Iraq", "Irak", 1),
 "misr": G("misr", "مِصْر", None, "propn", "Egypt — a diptote (a proper name, feminine)", "Mısır — gayr-i munsarif", 1),
 "sahil": G("sahil", "سَاحِل", "س ح ل", "noun", "a shore, a coast", "sahil, kıyı", 2),
 "bahr": G("bahr", "بَحْر", "ب ح ر", "noun", "sea", "deniz", 1),
 "ahmar": G("ahmar", "أَحْمَر", "ح م ر", "noun", "red; الْبَحْرُ الْأَحْمَرُ: the Red Sea", "kızıl, kırmızı; Kızıldeniz", 1),
 "ashraka": G("ashraka", "أَشْرَكَ", "ش ر ك", "verb", "to associate (a partner with God), to commit shirk (Form IV)", "şirk koşmak (if'âl)", 2),
 "kama": G("kama", "كَمَا", None, "part", "as, just as", "gibi", 1),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation, a community", "ümmet", 1, plural="أُمَم"),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "each, every, all", "her, bütün", 1),
 "asr": G("asr", "عَصْر", "ع ص ر", "noun", "an age, an era", "çağ, asır", 2),
 "ziyada": G("ziyada", "زِيَادَة", "ز ي د", "noun", "increase, more; gain", "fazlalık, artış", 2),
 "dhalika": G("dhalika", "ذَلِكَ", None, "pron", "that", "o, şu", 1),
 "naqasa": G("naqasa", "نَقَصَ", "ن ق ص", "verb", "to lessen, to give short (measure)", "eksiltmek, eksik vermek", 2),
 "mikyal": G("mikyal", "مِكْيَال", "ك ي ل", "noun", "a measure (of capacity)", "ölçek, kile", 3),
 "mizan": G("mizan", "مِيزَان", "و ز ن", "noun", "a balance, scales; weight", "terazi, tartı", 2),
 "taffafa": G("taffafa", "طَفَّفَ", "ط ف ف", "verb", "to skimp in measuring, to give short measure (Form II)", "ölçüde hile yapmak, eksik tartmak (tef'îl)", 4),
 "kayl": G("kayl", "كَيْل", "ك ي ل", "noun", "measuring, measure (masdar of كَالَ)", "ölçme, ölçü", 3),
 "taarrada": G("taarrada", "تَعَرَّضَ", "ع ر ض", "verb", "to waylay, to set upon (تَعَرَّضَ لِ) (Form V)", "yolunu kesmek, saldırmak (tefa''ul)", 4),
 "qafila": G("qafila", "قَافِلَة", "ق ف ل", "noun", "a caravan", "kervan, kafile", 2, plural="قَوَافِل"),
 "tawaada": G("tawaada", "تَوَعَّدَ", "و ع د", "verb", "to threaten (Form V)", "tehdit etmek (tefa''ul)", 4),
 "akhafa": G("akhafa", "أَخَافَ", "خ و ف", "verb", "to frighten (Form IV)", "korkutmak (if'âl)", 3),
 "atha": G("atha", "عَاثَ", "ع ي ث", "verb", "to wreak havoc (عَاثَ فِي الْأَرْضِ فَسَادًا)", "bozgunculuk yapmak, kargaşa çıkarmak", 4),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "earth, land", "yer, arz", 1),
 "fasad": G("fasad", "فَسَاد", "ف س د", "noun", "corruption, mischief", "fesat, bozgunculuk", 2),
 "shan": G("shan", "شَأْن", "ش أ ن", "noun", "the matter, the way (of); شَأْنَ: as … do", "şan — durum, tarz; şâ'ne: … gibi", 3),
 "ghani": G("ghani", "غَنِيّ", "غ ن ي", "noun", "rich", "zengin", 1, plural="أَغْنِيَاء"),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü", 1, plural="أَقْوِيَاء"),
 "alladhina": G("alladhina", "الَّذِينَ", None, "pron", "who, those who (masculine plural relative)", "ellezîne — cemi müzekker ism-i mevsûl", 2),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "the negating lā", "nefy lâ'sı", 1),
 "raja": G("raja", "رَجَا", "ر ج و", "verb", "to hope for", "ummak", 2),
 "hisab": G("hisab", "حِسَاب", "ح س ب", "noun", "a reckoning, an account", "hesap", 2),
 "khashiya": G("khashiya", "خَشِيَ", "خ ش ي", "verb", "to fear, to dread", "korkmak, çekinmek", 2),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "punishment, torment", "azap", 1),
 "baatha": G("baatha", "بَعَثَ", "ب ع ث", "verb", "to send (a messenger); to raise", "göndermek; diriltmek", 2),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "a messenger", "elçi, resûl", 1),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call, to invite; to pray", "çağırmak, davet etmek; dua etmek", 1),
 "andhara": G("andhara", "أَنْذَرَ", "ن ذ ر", "verb", "to warn (Form IV)", "uyarmak (if'âl)", 2),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O — the calling particle", "yâ — nidâ harfi", 1),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "kulluk etmek, ibadet etmek", 1),
 "ilah": G("ilah", "إِلَه", "أ ل ه", "noun", "a god", "ilâh", 1),
 "la-nahiya": G("la-nahiya", "لَا (النَّاهِيَة)", None, "part", "the prohibiting lā — puts the muḍāriʿ in jazm", "nehiy lâ'sı — muzâriyi cezm eder", 2),
 "khayr": G("khayr", "خَيْر", "خ ي ر", "noun", "good; better (an elative without its hamza)", "hayır; daha hayırlı", 1),
 "khafa": G("khafa", "خَافَ", "خ و ف", "verb", "to fear", "korkmak", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1),
 "muhit": G("muhit", "مُحِيط", "ح و ط", "noun", "encompassing (ism fāʿil of أَحَاطَ)", "kuşatıcı", 3),
 "awfa": G("awfa", "أَوْفَى", "و ف ي", "verb", "to give in full, to fulfil (Form IV)", "tam vermek, yerine getirmek (if'âl)", 3),
 "qist": G("qist", "قِسْط", "ق س ط", "noun", "justice, fairness", "adalet, kıst", 3),
 "bakhasa": G("bakhasa", "بَخَسَ", "ب خ س", "verb", "to deprive, to give less than due (two objects)", "eksik vermek, hakkını yemek (iki mef'ûllü)", 4),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing; شَيْءٌ مِنْ: some", "şey; şey'ün min: biraz", 1, plural="أَشْيَاء"),
 "mufsid": G("mufsid", "مُفْسِد", "ف س د", "noun", "a corrupter, one who spreads mischief (ism fāʿil of أَفْسَدَ)", "bozguncu, müfsit", 2),
 "basata": G("basata", "بَسَطَ", "ب س ط", "verb", "to spread out; بَسَطَ فِي الْكَلَامِ: to speak at length", "yaymak; sözü uzatmak", 3),
 "kalam": G("kalam", "كَلَام", "ك ل م", "noun", "speech", "söz, kelâm", 2),
 "uqda": G("uqda", "عُقْدَة", "ع ق د", "noun", "a knot; a complex", "düğüm", 3),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "soul, self", "nefis, can", 1, plural="نُفُوس"),
 "hiya": G("hiya", "هِيَ", None, "pron", "she, it", "o", 1),
 "hubb": G("hubb", "حُبّ", "ح ب ب", "noun", "love", "sevgi", 1),
 "mal": G("mal", "مَال", "م و ل", "noun", "wealth, property", "mal", 1, plural="أَمْوَال"),
 "fadala": G("fadala", "فَضَلَ", "ف ض ل", "verb", "to remain over, to be left in surplus", "artmak, fazla kalmak", 3),
 "ribh": G("ribh", "رِبْح", "ر ب ح", "noun", "profit", "kâr, kazanç", 2),
 "bada": G("bada", "بَعْدَ", "ب ع د", "noun", "after (a ẓarf)", "sonra (zarf)", 1),
 "wafa": G("wafa", "وَفَاء", "و ف ي", "noun", "giving in full, fulfilment", "tam verme, vefa", 3),
 "akhdh": G("akhdh", "أَخْذ", "أ خ ذ", "noun", "taking (masdar of أَخَذَ)", "alma", 2),
 "zulm": G("zulm", "ظُلْم", "ظ ل م", "noun", "wrong, injustice", "zulüm", 1),
 "khiyana": G("khiyana", "خِيَانَة", "خ و ن", "noun", "treachery, betrayal", "hıyanet", 2),
 "idha": G("idha", "إِذَا", None, "part", "when, if — the conditional ẓarf of the future", "-dığı zaman, -sa — istikbal şart zarfı", 2),
 "nazara": G("nazara", "نَظَرَ", "ن ظ ر", "verb", "to look (نَظَرَ فِي / إِلَى)", "bakmak", 1),
 "hayat": G("hayat", "حَيَاة", "ح ي ي", "noun", "life", "hayat", 1),
 "haulai": G("haulai", "هَؤُلَاءِ", None, "pron", "these, those (plural demonstrative)", "bunlar, şunlar", 1),
 "athra": G("athra", "أَثْرَى", "ث ر و", "verb", "to grow rich (Form IV)", "zenginleşmek (if'âl)", 4),
 "jamaa-gather": G("jamaa-gather", "جَمَعَ", "ج م ع", "verb", "to gather, to amass", "toplamak, yığmak", 1),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find; (with two objects) to find that", "bulmak", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that — the sister of إِنَّ that makes its clause a maṣdar", "enne — ki; cümlesini masdar kılan inne kardeşi", 2),
 "iktasaba": G("iktasaba", "اِكْتَسَبَ", "ك س ب", "verb", "to earn, to acquire (Form VIII)", "kazanmak, edinmek (iftiâl)", 2),
 "an": G("an", "عَنْ", None, "prep", "from, about; by way of", "-den, hakkında", 1),
 "tariq": G("tariq", "طَرِيق", "ط ر ق", "noun", "a way, a road", "yol", 1),
 "tatfif": G("tatfif", "تَطْفِيف", "ط ف ف", "noun", "skimping in measure (masdar of طَفَّفَ)", "ölçüde hile", 4),
 "bakhs": G("bakhs", "بَخْس", "ب خ س", "noun", "cheating, giving less than due", "eksik verme, hak yeme", 4),
 "masir-fate": G("masir-fate", "مَصِير", "ص ي ر", "noun", "the end, the fate, where something ends up", "âkıbet, son", 2),
 "talaf": G("talaf", "تَلَف", "ت ل ف", "noun", "ruin, destruction", "telef, yok olma", 3),
 "daya": G("daya", "ضَيَاع", "ض ي ع", "noun", "loss, waste", "zayi olma, kayıp", 3),
 "aw": G("aw", "أَوْ", None, "part", "or", "yahut", 1),
 "bala": G("bala", "بَلَاء", "ب ل و", "noun", "affliction, trial", "belâ", 2),
 "saraqa": G("saraqa", "سَرَقَ", "س ر ق", "verb", "to steal", "çalmak", 1),
 "nahaba": G("nahaba", "نَهَبَ", "ن ه ب", "verb", "to plunder", "yağmalamak", 3),
 "anfaqa": G("anfaqa", "أَنْفَقَ", "ن ف ق", "verb", "to spend (Form IV)", "harcamak (if'âl)", 2),
 "arda": G("arda", "أَرْضَى", "ر ض و", "verb", "to please, to satisfy (Form IV)", "razı etmek, hoşnut etmek (if'âl)", 3),
 "sallata": G("sallata", "سَلَّطَ", "س ل ط", "verb", "to set (someone) over, to give power over (Form II)", "musallat etmek (tef'îl)", 3),
 "man-mawsula": G("man-mawsula", "مَنْ (الْمَوْصُولَة)", None, "pron", "he who, whoever — the relative", "men-i mevsûle — kim ki", 3),
 "atlafa": G("atlafa", "أَتْلَفَ", "ت ل ف", "verb", "to destroy, to waste (Form IV)", "telef etmek (if'âl)", 3),
 "abatha": G("abatha", "عَبِثَ", "ع ب ث", "verb", "to play with, to tamper with (عَبِثَ بِ)", "oynamak, kurcalamak", 3),
 "qalil": G("qalil", "قَلِيل", "ق ل ل", "noun", "few, little", "az", 1),
 "nafaa": G("nafaa", "نَفَعَ", "ن ف ع", "verb", "to benefit", "fayda vermek", 1),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "istawa": G("istawa", "اِسْتَوَى", "س و ي", "verb", "to be equal; to be level (Form VIII)", "eşit olmak; düz olmak (iftiâl)", 3),
 "khabith": G("khabith", "خَبِيث", "خ ب ث", "noun", "foul, evil", "pis, habis", 2),
 "tayyib": G("tayyib", "الطَّيِّب", "ط ي ب", "noun", "good, wholesome", "temiz, hoş", 1),
 "law": G("law", "لَوْ", None, "part", "if, had — the condition whose answer fails because its protasis fails", "lev — şartın gerçekleşmemesi yüzünden cevabın gerçekleşmediği şart", 3),
 "aajaba": G("aajaba", "أَعْجَبَ", "ع ج ب", "verb", "to please, to delight (Form IV)", "hoşuna gitmek (if'âl)", 2),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masculine singular, attached)", "sen / senin (bitişik)", 1),
 "kathra": G("kathra", "كَثْرَة", "ك ث ر", "noun", "abundance, multitude", "çokluk", 2),
 "nasiha": G("nasiha", "نَصِيحَة", "ن ص ح", "noun", "counsel, sincere advice", "nasihat", 2),
 "khalis": G("khalis", "خَالِص", "خ ل ص", "noun", "pure, unmixed", "hâlis", 2),
 "mukhlis": G("mukhlis", "مُخْلِص", "خ ل ص", "noun", "sincere (ism fāʿil of أَخْلَصَ)", "samimi, muhlis", 2),
 "raqib": G("raqib", "رَقِيب", "ر ق ب", "noun", "a watcher, an overseer", "gözetleyici, rakîb", 3),
 "wahda": G("wahda", "وَحْد", "و ح د", "noun", "alone (وَحْدَهُ: he alone)", "yalnız (vahdehû: tek başına)", 2),
 "rifq": G("rifq", "رِفْق", "ر ف ق", "noun", "gentleness", "yumuşaklık, rıfk", 3),
 "hikma": G("hikma", "حِكْمَة", "ح ك م", "noun", "wisdom", "hikmet", 1),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge", "ilim", 1),
 "basira": G("basira", "بَصِيرَة", "ب ص ر", "noun", "insight, discernment", "basiret", 3),
 "baqiyya": G("baqiyya", "بَقِيَّة", "ب ق ي", "noun", "what remains, the remainder; بَقِيَّتُ اللهِ: what God leaves you", "kalan; bakıyyetullah: Allah'ın bıraktığı", 3),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if — the conditional particle", "eğer — şart harfi", 1),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "a believer", "mü'min", 1, plural="مُؤْمِنُونَ"),
 "ma-hijaziyya": G("ma-hijaziyya", "مَا (الْحِجَازِيَّة)", None, "part", "the Ḥijāzī mā — the negating mā that governs like لَيْسَ", "Hicâzî mâ — leyse gibi amel eden nefy mâ'sı", 5),
 "ana": G("ana", "أَنَا", None, "pron", "I", "ben", 1),
 "hafiz-keeper": G("hafiz-keeper", "حَفِيظ", "ح ف ظ", "noun", "a keeper, a guardian", "koruyucu, bekçi", 3),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için", 1),
 "bi": G("bi", "بِ", None, "prep", "by, with", "ile", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, then", "o hâlde, sonra", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "he / him / his (attached)", "o / onun (bitişik)", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "I / me / my", "ben", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (masculine plural, attached)", "siz / sizin (bitişik)", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us / our", "biz", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "she / it / her (attached)", "o / onun (bitişik)", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed — puts its ism in naṣb and its khabar in rafʿ", "inne — şüphesiz; ismini nasb, haberini ref' eder", 1),
 "allah": G("allah", "اللَّه", None, "propn", "God", "Allah", 1),
 "qasas": G("qasas", "قَصَص", "ق ص ص", "noun", "stories (plural of قِصَّة); narration", "kıssalar; anlatım", 2),
 "haka": G("haka", "حَكَى", "ح ك ي", "verb", "to tell, to relate", "anlatmak, hikâye etmek", 2),
 "hikaya": G("hikaya", "حِكَايَة", "ح ك ي", "noun", "a telling, a tale", "hikâye, anlatma", 2, plural="حِكَايَات"),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa, hikâye", 1, plural="قِصَص"),
 "halla-settle": G("halla-settle", "حَلَّ", "ح ل ل", "verb", "to settle, to alight (حَلَّ مَحَلَّ: to take the place of); to untie", "yerleşmek; çözmek", 3),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "taffafa", _sg.derived(_sg.B2, _sg.W2, "ُ", "طَفَّف", "طَفِّف", "طَفِّف", "تَطْفِيف", "مُطَفِّف", "مُطَفَّف", "طُفِّفَ", "يُطَفَّفُ", "طَفَّفَ يُطَفِّفُ: نَقَصَ الْكَيْلَ — بَابُ التَّفْعِيلِ؛ وَيْلٌ لِلْمُطَفِّفِينَ"))
put_morph(mo, "taarrada", _sg.derived(_sg.B5, _sg.W5, "َ", "تَعَرَّض", "تَعَرَّض", "تَعَرَّض", "تَعَرُّض", "مُتَعَرِّض", None, None, None, "تَعَرَّضَ لَهُ يَتَعَرَّضُ: اعْتَرَضَ طَرِيقَهُ — بَابُ التَّفَعُّلِ"))
put_morph(mo, "tawaada", _sg.derived(_sg.B5, _sg.W5, "َ", "تَوَعَّد", "تَوَعَّد", "تَوَعَّد", "تَوَعُّد", "مُتَوَعِّد", "مُتَوَعَّد", "تُوُعِّدَ", "يُتَوَعَّدُ", "تَوَعَّدَ يَتَوَعَّدُ: هَدَّدَ — بَابُ التَّفَعُّلِ"))
put_morph(mo, "atha", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "عَاث", "عِث", "عِيث", "عِث", "عِيث", "عِث", "عَيْث", "عَائِث", None, None, None, "عَاثَ يَعِيثُ فِي الْأَرْضِ فَسَادًا: أَفْسَدَ — أَجْوَفُ يَائِيٌّ مِنْ بَابِ ضَرَبَ؛ لَا تَعْثَوْا: الْأَلِفُ مَحْذُوفَةٌ قَبْلَ الْوَاوِ"))
put_morph(mo, "andhara", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَنْذَر", "نْذِر", "أَنْذِر", "إِنْذَار", "مُنْذِر", "مُنْذَر", "أُنْذِرَ", "يُنْذَرُ", "أَنْذَرَ يُنْذِرُ: خَوَّفَ وَحَذَّرَ — بَابُ الْإِفْعَالِ"))
put_morph(mo, "awfa", _sg.derived_naqis(_sg.B4 + " — نَاقِصٌ", _sg.W4, "ُ", "أَوْفَ", "وْف", "i", "أَوْف", "إِيفَاء", "مُوفٍ", "مُوفًى", "أُوفِيَ", "يُوفَى", "أَوْفَى يُوفِي: أَتَمَّ — نَاقِصٌ مِنَ الْإِفْعَالِ؛ أَوْفُوا الْكَيْلَ"))
put_morph(mo, "bakhasa", _sg.sound1("fataha", "بَخَس", "بْخَس", "اِبْخَس", "بَخْس", "بَاخِس", "مَبْخُوس", "بُخِسَ", "يُبْخَسُ", "بَخَسَ يَبْخَسُ: نَقَصَ — بَابُ فَتَحَ، يَتَعَدَّى إِلَى مَفْعُولَيْنِ"))
put_morph(mo, "basata", _sg.sound1("nasara", "بَسَط", "بْسُط", "اُبْسُط", "بَسْط", "بَاسِط", "مَبْسُوط", "بُسِطَ", "يُبْسَطُ", "بَسَطَ يَبْسُطُ: مَدَّ وَنَشَرَ — بَابُ نَصَرَ"))
put_morph(mo, "fadala", _sg.sound1("nasara", "فَضَل", "فْضُل", "اُفْضُل", "فَضْل", "فَاضِل", None, None, None, "فَضَلَ يَفْضُلُ: زَادَ وَبَقِيَ — بَابُ نَصَرَ"))
put_morph(mo, "athra", _sg.derived_naqis(_sg.B4 + " — نَاقِصٌ", _sg.W4, "ُ", "أَثْرَ", "ثْر", "i", "أَثْر", "إِثْرَاء", "مُثْرٍ", None, None, None, "أَثْرَى يُثْرِي: كَثُرَ مَالُهُ — نَاقِصٌ مِنَ الْإِفْعَالِ"))
put_morph(mo, "nahaba", _sg.sound1("fataha", "نَهَب", "نْهَب", "اِنْهَب", "نَهْب", "نَاهِب", "مَنْهُوب", "نُهِبَ", "يُنْهَبُ", "نَهَبَ يَنْهَبُ: سَلَبَ — بَابُ فَتَحَ"))
put_morph(mo, "arda", _sg.derived_naqis(_sg.B4 + " — نَاقِصٌ", _sg.W4, "ُ", "أَرْضَ", "رْض", "i", "أَرْض", "إِرْضَاء", "مُرْضٍ", "مُرْضًى", "أُرْضِيَ", "يُرْضَى", "أَرْضَى يُرْضِي: جَعَلَهُ رَاضِيًا — نَاقِصٌ مِنَ الْإِفْعَالِ"))
put_morph(mo, "sallata", _sg.derived(_sg.B2, _sg.W2, "ُ", "سَلَّط", "سَلِّط", "سَلِّط", "تَسْلِيط", "مُسَلِّط", "مُسَلَّط", "سُلِّطَ", "يُسَلَّطُ", "سَلَّطَ يُسَلِّطُ: جَعَلَ لَهُ سُلْطَانًا عَلَيْهِ — بَابُ التَّفْعِيلِ"))
put_morph(mo, "atlafa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَتْلَف", "تْلِف", "أَتْلِف", "إِتْلَاف", "مُتْلِف", "مُتْلَف", "أُتْلِفَ", "يُتْلَفُ", "أَتْلَفَ يُتْلِفُ: أَهْلَكَ — بَابُ الْإِفْعَالِ"))
put_morph(mo, "abatha", _sg.sound1("samia", "عَبِث", "عْبَث", "اِعْبَث", "عَبَث", "عَابِث", None, None, None, "عَبِثَ بِهِ يَعْبَثُ: لَعِبَ بِهِ — بَابُ سَمِعَ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch2 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 2 (print pp. 2–4, sections 3–4): the people of Madyan on the trade road, their shirk and their cheating of the measure, Shuʿayb sent with 11:84–85 (s1–s8); his first appeal — what remains after honest measure is better, 5:100 and 11:86 (s9–s15)."
ADD_TR = " İkinci bölüm (baskı s. 2–4, 3–4. kısımlar): ticaret yolu üzerindeki Medyen halkı, şirkleri ve ölçüde hileleri, 11:84–85 ile gönderilen Şuayb (s1–s8); ilk çağrısı — dürüst ölçüden sonra kalan daha hayırlıdır, 5:100 ve 11:86 (s9–s15)."
write_out(2, S, TITLE, ADD_EN, ADD_TR, "sections 3–4", GLOSS_ADD, notes=(), related=())
report(2, S, GLOSS_ADD, ())
