"""tabaqat_common — the shared kit of the shelf «مِنَ الطَّبَقَاتِ الْكُبْرَى» (v358-T): accounts from Ibn Saʿd's al-Ṭabaqāt al-kubrā.

Each package `tabaqat-<slug>` is a RECEIVED text from «الطبقات الكبرى» لابن سعد (ت ٢٣٠ هـ), ط دار الكتب العلمية، بيروت ١٩٩٠، تحقيق محمد
عبد القادر عطا (Shamela 1686; the cached book is research/sources/tabaqat-ibn-sad-src.txt, built by tools/authoring/tabaqat_src.py).
One long story (`tabaqat-al-hijra`, ONE package with many chapters) and short single-chapter accounts. The script
tools/authoring/author_<slug>.py is the package's source of truth; it writes the sentences and calls `finish()` here (the proverbs' and
the Khaṣāʾiṣ readings' finish, v348-A / v352-K, with the sibling prefix `tabaqat-`).

RULES (v333, carried): the e-text is UNVOWELLED, so every vowel is ours and the manifest says so; the text is never retold, re-ordered or
silently corrected — a correction is made only against a named witness and is listed; a vowel we cannot settle from the lexicon and the
grammar is LEFT UNWRITTEN and listed «for the hoca»; an isnād stays as the text has it (the Siyar's precedent); the exact passage is
saved first as research/sources/<slug>-src.txt; honorifics are tokens, exactly as the text writes them.

The token DSL below writes the house wordings of story_kit / amthal_common in a shorter call: NOUN(role, case, sign …), VERB(kind …),
PART(…), SALLA() (the four tokens of «صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ»), RASUL(role …) (رَسُولُ + اللهِ + SALLA).
"""
import inspect, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import khasais_common as _kc
from amthal_common import *        # noqa: F401,F403 — the kit (tok, seg, PRON, NOTE, finish's helpers …)
from amthal_common import ROOT, OUT_ROOT, N, PRE, SG
from khasais_common import X, SEN, NP, NN, NV, PF   # noqa: F401
import json, os, unicodedata, collections, re

# finish(): the Khaṣāʾiṣ shelf's finish verbatim, with the sibling prefix this shelf's (a key a sibling Ṭabaqāt package coined may be
# reused by its sibling for the same lemma; any other holder of a NEW key stops the write — a key is a global claim)
_src = inspect.getsource(_kc.finish).replace('"khasais-"', '"tabaqat-"').replace("Khaṣāʾiṣ reading", "Ṭabaqāt package")
_ns = dict(_kc.__dict__); exec(compile(_src, __file__ + ":finish", "exec"), _ns); finish = _ns["finish"]

SOURCE_AR = "«الطَّبَقَاتُ الْكُبْرَى» لِمُحَمَّدِ بْنِ سَعْدٍ (ت ٢٣٠ هـ)، بِتَحْقِيقِ مُحَمَّدٍ عَبْدِ الْقَادِرِ عَطَا، دَارُ الْكُتُبِ الْعِلْمِيَّةِ، بَيْرُوتُ ١٩٩٠ (الشَّامِلَةُ ١٦٨٦)"
SOURCE_EN = "«al-Ṭabaqāt al-kubrā» by Muḥammad ibn Saʿd (d. 230 AH), ed. Muḥammad ʿAbd al-Qādir ʿAṭā, Dār al-Kutub al-ʿIlmiyya, Beirut 1990 (Shamela book 1686)"
SOURCE_TR = "İbn Sa'd'ın (Muhammed b. Sa'd, ö. 230) «et-Tabakātü'l-kübrâ» adlı eseri (thk. Muhammed Abdülkādir Atâ, Dârü'l-Kütübi'l-İlmiyye, Beyrut 1990; Şâmile kitap 1686)"
LEVEL_NAME = {1: "Beginner", 2: "Elementary", 3: "Intermediate", 4: "Upper Intermediate", 5: "Advanced", 6: "Master"}
SECTION = {"sira": ("السِّيرَةُ النَّبَوِيَّةُ", "the Prophet's sīra", "Siyer-i Nebî"), "sahaba": ("طَبَقَاتُ الصَّحَابَةِ", "the Companions' classes", "sahâbe tabakaları"),
           "tabiun": ("طَبَقَاتُ التَّابِعِينَ", "the Successors' classes", "tâbiîn tabakaları"), "nisa": ("النِّسَاءُ", "the women's volume", "kadınlar cildi")}

def manifest(SLUG, level, title, subtitle, section, where_en, where_tr, where_ar, span_en, span_tr, span_ar, corrections=(), witness_ar="",
             witness_en="", witness_tr="", kept=(), hoca=(), left_en="", left_tr="", left_ar="", isnad=True, extra_en="", extra_tr="", extra_ar="",
             published="2026-11-27"):
    """the manifest of a Ṭabaqāt account: the RECEIVED-text attribution in three languages — section, volume and printed page, the span,
    the isnād kept, the vowelling declared ours, corrections (with their witness) or none, what is kept as printed, what lies between or
    around the spans, and the points left for the hoca"""
    sec = SECTION[section]
    if corrections:
        lst = "؛ ".join(f"«{a}» ← «{b}»" for a, b in corrections)
        cor_ar = f"التَّصْحِيحُ: صُحِّحَ مَا يَلِي عَلَى شَاهِدٍ هُوَ {witness_ar}، وَلَمْ يُصَحَّحْ شَيْءٌ غَيْرُهُ: {lst}. "
        lst = "; ".join(f"«{a}» → «{b}»" for a, b in corrections)
        cor_en = f"CORRECTIONS (e-text → now), each made against a named witness and nothing else — {witness_en}: {lst}. "
        cor_tr = f"DÜZELTMELER (elektronik metin → şimdi); her biri yalnızca adı geçen bir şâhide dayanır — {witness_tr}: {lst}. "
    else:
        cor_ar, cor_en, cor_tr = "وَلَمْ يُصَحَّحْ فِي النَّصِّ شَيْءٌ. ", "NO correction was made to the text. ", "Metinde HİÇBİR düzeltme yapılmamıştır. "
    kept_ar = ("وَأُبْقِيَ كَمَا طُبِعَ: " + "؛ ".join(k[0] for k in kept) + ". ") if kept else ""
    kept_en = ("KEPT AS PRINTED: " + "; ".join(k[1] for k in kept) + ". ") if kept else ""
    kept_tr = ("BASKIDAKİ GİBİ BIRAKILANLAR: " + "; ".join(k[2] for k in kept) + ". ") if kept else ""
    is_ar = "وَالْإِسْنَادُ مَذْكُورٌ كَمَا هُوَ فِي الْكِتَابِ. " if isnad else ""
    is_en = "The isnād is kept as the book gives it. " if isnad else ""
    is_tr = "İsnad kitapta olduğu gibi korunmuştur. " if isnad else ""
    lf_ar = ("وَمَا تُرِكَ: " + left_ar + ". ") if left_ar else ""
    lf_en = ("LEFT OUT (between or around the spans): " + left_en + ". ") if left_en else ""
    lf_tr = ("ALINMAYANLAR (parçaların arasında veya çevresinde): " + left_tr + ". ") if left_tr else ""
    hz_en = "LEFT FOR THE SCHOLAR: " + "; ".join(h[0] for h in hoca) + ". " if hoca else ""
    hz_tr = "HOCAYA BIRAKILANLAR: " + "; ".join(h[1] for h in hoca) + ". " if hoca else ""
    hz_ar = "وَتُرِكَ لِلْعَالِمِ الْمُرَاجِعِ " + str(len(hoca)) + " مَوَاضِعَ مَذْكُورَةٌ فِي الْإِنْكِلِيزِيَّةِ وَالتُّرْكِيَّةِ. " if hoca else ""
    return {
     "id": SLUG, "storyGroup": SLUG, "title": title, "subtitle": subtitle,
     "level": level, "levelName": LEVEL_NAME[level], "version": "0.1.0", "published": published, "access": "free",
     "attribution": {
      "ar": "نَصٌّ مَنْقُولٌ بِلَفْظِهِ مِنْ " + SOURCE_AR + "، مِنْ قِسْمِ «" + sec[0] + "»، " + where_ar + ": " + span_ar + ". " + is_ar + VOWEL_AR + cor_ar + kept_ar
            + lf_ar + extra_ar + hz_ar + "وَالتَّرْجَمَتَانِ الْإِنْكِلِيزِيَّةُ وَالتُّرْكِيَّةُ وَالْإِعْرَابُ مِنْ عَمَلِنَا، وَالنَّصُّ كُلُّهُ يَنْتَظِرُ مُرَاجَعَةَ الْعَالِمِ.",
      "en": "The RECEIVED text, verbatim, from " + SOURCE_EN + ", " + sec[1] + ", " + where_en + ": " + span_en + ". The exact passage is in research/sources/" + SLUG
            + "-src.txt. " + is_en + VOWEL_EN + cor_en + kept_en + lf_en + extra_en + hz_en
            + "The English and Turkish translations and every iʿrāb line are ours; the whole awaits a scholar's review.",
      "tr": "LAFZIYLA AKTARILAN metin: " + SOURCE_TR + ", " + sec[2] + ", " + where_tr + ": " + span_tr + ". Pasajın aynısı research/sources/" + SLUG
            + "-src.txt dosyasındadır. " + is_tr + VOWEL_TR + cor_tr + kept_tr + lf_tr + extra_tr + hz_tr
            + "İngilizce ve Türkçe tercümeler ile bütün i'râb satırları bize aittir; metnin tamamı bir âlimin incelemesini beklemektedir.",
      "reviewStatus": REVIEW,
     },
    }

# ---- the token DSL ------------------------------------------------------------------------------------------------------
CASE = {"raf": ("مَرْفُوعٌ", "raf'", "merfû"), "nasb": ("مَنْصُوبٌ", "nasb", "mansûb"), "jarr": ("مَجْرُورٌ", "jarr", "mecrûr")}
SIGN = {  # sign key → per case (ar, en, tr)
 None: {"raf": ("بِالضَّمَّةِ", "", ""), "nasb": ("بِالْفَتْحَةِ", "", ""), "jarr": ("بِالْكَسْرَةِ", "", "")},
 "5": {"raf": ("بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", " by the waw (one of the five nouns)", " (vâv ile; beş isimden)"),
       "nasb": ("بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", " by the alif (one of the five nouns)", " (elif ile; beş isimden)"),
       "jarr": ("بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", " by the ya (one of the five nouns)", " (yâ ile; beş isimden)")},
 "smp": {"raf": ("بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", " by the waw (a sound masculine plural)", " (vâv ile; cem-i müzekker sâlim)"),
         "nasb": ("بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", " by the ya (a sound masculine plural)", " (yâ ile; cem-i müzekker sâlim)"),
         "jarr": ("بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", " by the ya (a sound masculine plural)", " (yâ ile; cem-i müzekker sâlim)")},
 "bn": {"raf": ("بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", " by the waw (treated as a sound masculine plural)", " (vâv ile; cem-i müzekker sâlime mülhak)"),
        "nasb": ("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", " by the ya (treated as a sound masculine plural)", " (yâ ile; cem-i müzekker sâlime mülhak)"),
        "jarr": ("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", " by the ya (treated as a sound masculine plural)", " (yâ ile; cem-i müzekker sâlime mülhak)")},
 "sfp": {"raf": ("بِالضَّمَّةِ", "", ""), "nasb": ("بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ", " by the kasra (a sound feminine plural)", " (kesre ile; cem-i müennes sâlim)"),
         "jarr": ("بِالْكَسْرَةِ", "", "")},
 "du": {"raf": ("بِالْأَلِفِ لِأَنَّهُ مُثَنًّى", " by the alif (a dual)", " (elif ile; tesniye)"), "nasb": ("بِالْيَاءِ لِأَنَّهُ مُثَنًّى", " by the ya (a dual)", " (yâ ile; tesniye)"),
        "jarr": ("بِالْيَاءِ لِأَنَّهُ مُثَنًّى", " by the ya (a dual)", " (yâ ile; tesniye)")},
 "maq": {k: ("بِ" + v + " الْمُقَدَّرَةِ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", " (the vowel estimated on the alif)", " (hareke elif üzerinde takdîrî)") for k, v in (("raf", "الضَّمَّةِ"), ("nasb", "الْفَتْحَةِ"), ("jarr", "الْكَسْرَةِ"))},
 "manq": {"raf": ("بِالضَّمَّةِ الْمُقَدَّرَةِ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِلثِّقَلِ", " (the vowel estimated on the dropped ya)", " (hareke düşen yâ üzerinde takdîrî)"),
          "nasb": ("بِالْفَتْحَةِ الظَّاهِرَةِ", "", ""),
          "jarr": ("بِالْكَسْرَةِ الْمُقَدَّرَةِ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِلثِّقَلِ", " (the vowel estimated on the dropped ya)", " (hareke düşen yâ üzerinde takdîrî)")},
 "ya": {k: ("بِ" + v + " الْمُقَدَّرَةِ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ", " (the vowel estimated before the ya of the speaker)", " (hareke mütekellim yâsından öncekinde takdîrî)") for k, v in (("raf", "الضَّمَّةِ"), ("nasb", "الْفَتْحَةِ"), ("jarr", "الْكَسْرَةِ"))},
}
DIPT_WHY = {"tanith": ("لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", "a feminine proper name", "alemiyet ve te'nîs"),
            "ujma": ("لِلْعَلَمِيَّةِ وَالْعُجْمَةِ", "a foreign proper name", "alemiyet ve ucmet"),
            "wazn": ("لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ", "a proper name on a verb's pattern", "alemiyet ve fiil vezni"),
            "adl": ("لِلْعَلَمِيَّةِ وَالْعَدْلِ", "a proper name turned from another form", "alemiyet ve adl"),
            "nun": ("لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ", "a proper name ending in added -ān", "alemiyet ve elif-nûn ziyâdesi"),
            "muntaha": ("لِأَنَّهُ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ", "the furthest plural pattern", "müntehe'l-cumû' sîgası"),
            "alif": ("لِأَنَّهُ مَخْتُومٌ بِأَلِفِ التَّأْنِيثِ", "it ends in the feminine alif", "te'nîs elifiyle biter"),
            "wasf": ("لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ", "an adjective on a verb's pattern", "vasfiyet ve fiil vezni")}
ROLE = {  # role → (ar head, en head, tr head, grammar, default case)
 "fail": ("فَاعِلٌ", "The doer (fāʿil)", "Fâil", ["fail"], "raf"),
 "naib": ("نَائِبُ فَاعِلٍ", "The deputy doer", "Nâib-i fâil", ["naib-al-fail"], "raf"),
 "maful": ("مَفْعُولٌ بِهِ", "The object", "Mef'ûlün bih", ["maful-bihi"], "nasb"),
 "maful2": ("مَفْعُولٌ بِهِ ثَانٍ", "The second object", "İkinci mef'ûlün bih", ["maful-bihi", "mafulayn"], "nasb"),
 "mi": ("مُضَافٌ إِلَيْهِ", "The second term of the iḍāfa", "Muzâfun ileyh", ["idafa-definiteness"], "jarr"),
 "majr": ("اسْمٌ", "A noun", "İsim", ["huruf-jarr"], "jarr"),
 "mubt": ("مُبْتَدَأٌ", "The mubtadaʾ", "Mübtedâ", ["mubtada-khabar"], "raf"),
 "mubtm": ("مُبْتَدَأٌ مُؤَخَّرٌ", "The mubtadaʾ, placed after its khabar", "Sonraya bırakılmış mübtedâ", ["mubtada-khabar"], "raf"),
 "khabar": ("خَبَرٌ", "The khabar", "Haber", ["mubtada-khabar"], "raf"),
 "khmh": ("خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ", "The khabar of an omitted mubtadaʾ", "Mahzûf mübtedânın haberi", ["mubtada-khabar", "hadhf-wa-taqdir"], "raf"),
 "atf": ("مَعْطُوفٌ", "Conjoined to the word before", "Ma'tûf", ["atf-nasaq"], None),
 "naat": ("نَعْتٌ", "An adjective (naʿt)", "Na't", ["naat-sifa"], None),
 "badal": ("بَدَلٌ", "A substitute (badal)", "Bedel", ["badal"], None),
 "tawkid": ("تَوْكِيدٌ", "An emphasis (tawkīd)", "Te'kîd", ["al-tawkid-al-lafzi-wal-manawi"], None),
 "hal": ("حَالٌ", "A ḥāl (state)", "Hâl", ["hal"], "nasb"),
 "ismk": ("اسْمُ كَانَ", "The noun of kāna", "Kâne'nin ismi", ["kana-wa-akhawatuha"], "raf"),
 "khk": ("خَبَرُ كَانَ", "The predicate of kāna", "Kâne'nin haberi", ["kana-wa-akhawatuha"], "nasb"),
 "isminna": ("اسْمُ إِنَّ", "The noun of inna", "İnne'nin ismi", ["inna-wa-akhawatuha"], "nasb"),
 "isminnam": ("اسْمُ إِنَّ مُؤَخَّرٌ", "The noun of inna, placed after its predicate", "Sonraya bırakılmış inne'nin ismi", ["inna-wa-akhawatuha"], "nasb"),
 "khinna": ("خَبَرُ إِنَّ", "The predicate of inna", "İnne'nin haberi", ["inna-wa-akhawatuha"], "raf"),
 "tamyiz": ("تَمْيِيزٌ", "A specifier (tamyīz)", "Temyîz", ["al-tamyiz-wa-ahkamuh"], "nasb"),
 "zarf": ("ظَرْفٌ", "An adverbial (ẓarf)", "Zarf", ["maful-fih"], "nasb"),
 "mm": ("مَفْعُولٌ مُطْلَقٌ", "The absolute object (mafʿūl muṭlaq)", "Mef'ûl-i mutlak", ["maful-mutlaq"], "nasb"),
 "nmm": ("نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ", "Standing for the absolute object", "Mef'ûl-i mutlakın nâibi", ["maful-mutlaq"], "nasb"),
 "maflah": ("مَفْعُولٌ لِأَجْلِهِ", "The object of purpose", "Mef'ûlün leh", ["maful-lah"], "nasb"),
 "munada": ("مُنَادًى", "Called (munādā)", "Münâdâ", ["al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada"], "nasb"),
}
PRE_TXT = {  # a fused prefix's opening of the line
 "wa": ("الْوَاوُ عَاطِفَةٌ، وَ", "The waw conjoins; ", "«ve» + "), "fa": ("الْفَاءُ عَاطِفَةٌ، وَ", "The fa conjoins; ", "«bunun üzerine» + "),
 "wa-isti": ("الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ", "The waw resumes; ", "Vâv isti'nâf içindir; "), "fa-isti": ("الْفَاءُ اسْتِئْنَافِيَّةٌ، وَ", "The fa resumes; ", "Fâ isti'nâf içindir; "),
 "wa-hal": ("الْوَاوُ حَالِيَّةٌ، وَ", "The waw of the ḥāl; ", "Hâl vâvı; "), "fa-sabab": ("الْفَاءُ سَبَبِيَّةٌ عَاطِفَةٌ، وَ", "The fa of consequence conjoins; ", "Sebebiyye fâsı atfeder; "),
 "bi": ("الْبَاءُ حَرْفُ جَرٍّ، وَ", "The ba is a jarr letter; ", "Bâ cer harfi; "), "li": ("اللَّامُ حَرْفُ جَرٍّ، وَ", "The lam is a jarr letter; ", "Lâm cer harfi; "),
 "ka": ("الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ", "The kaf «like» is a jarr letter; ", "Kâf teşbih için cer harfi; "),
 "la": ("اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَ", "The lam answers the oath; ", "Lâm kasemin cevabındadır; "),
}
def _segs(full, pre, enc, lex, pos, s, spos):
    if not pre and not enc: return None
    rest, segs = N(full), []
    for k in pre:
        k0 = k.split("-")[0]; f = PF[k0][0]
        if k0 == "li" and rest.startswith("لِلْ"): segs.append(seg(*PF[k0])); rest = "الْ" + rest[4:]; continue
        assert rest.startswith(f), (full, k); segs.append(seg(*PF[k0])); rest = rest[len(f):]
    tail = None
    if enc:
        assert rest.endswith(enc), (full, enc); rest = rest[:-len(enc)]; tail = seg(enc, PRON[enc], "pron")
    segs.append(seg(rest, s or lex, spos or pos))
    if tail: segs.append(tail)
    return segs
def _pre_txt(pre, full=None, enc=None):
    """the opening of a line for a fused وَ / فَ (with the stem named, as the house writes «الْفَاءُ عَاطِفَةٌ، وَيَنْطِقَ فِعْلٌ …»)"""
    a = e = t = ""
    for k in pre:
        if k in PRE_TXT and not k.startswith(("bi", "li", "ka")): x = PRE_TXT[k]; a, e, t = a + x[0], e + x[1], t + x[2]
    if a and full is not None and not [k for k in pre if k in ("bi", "li", "ka")]:
        a += _stem_show(full, pre, enc) + " "
    return a, e, t
def _lc(pe, e): return pe + (e[:1].lower() + e[1:] if pe else e)
ENC_SEAT = {"jarr": ("فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "in the seat of jarr, the second term", "mahallen mecrûr muzâfun ileyh"),
            "nasb": ("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "in the seat of nasb, the object", "mahallen mansûb mef'ûlün bih"),
            "jarr-prep": ("فِي مَحَلِّ جَرٍّ بِالْحَرْفِ", "in the seat of jarr after the letter", "harfle mahallen mecrûr")}
def ENC_TXT(enc, seat="jarr", ref=None):
    nm = PRON_AR.get(enc, enc)
    r = ref or ("", "", "")
    return ("، وَ" + nm + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ " + ENC_SEAT[seat][0] + (("، يَعُودُ عَلَى " + r[0]) if r[0] else ""),
            "; the attached pronoun is " + ENC_SEAT[seat][1] + ((" (" + r[1] + ")") if r[1] else ""),
            "; bitişik zamir " + ENC_SEAT[seat][2] + ((" (" + r[2] + ")") if r[2] else ""))

def NOUN(full, lex, role, case=None, pos="noun", sign=None, mudaf=False, dipt=None, note=("", "", ""), p=None, pre=(), enc=None, ref=None,
         s=None, spos=None, g=(), by=None, of=None):
    """a noun in its seat: `role` (ROLE), `case` (raf/nasb/jarr; the role's default otherwise), `sign` (SIGN key), `dipt` (DIPT_WHY key:
    barred from tanwin — in jarr the fatḥa stands for the kasra), `mudaf` (annexed), `by` (the jarr letter's name for a majrūr), `of` (the
    word a naʿt / badal / ʿaṭf follows, as (ar, en, tr)), `enc` (attached pronoun; its seat follows the role), `pre` (fused prefixes)."""
    ra, re_, rt, gr, dc = ROLE[role]
    case = case or dc
    sg = SIGN[sign][case]
    sa = sg[0]
    dp = ("", "", "")
    if dipt:
        w = DIPT_WHY[dipt]
        if case == "jarr": sa = "بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ"
        dp = ("، مَمْنُوعٌ مِنَ الصَّرْفِ " + w[0], " — barred from tanwin (" + w[1] + ")", " — gayr-i munsarif (" + w[2] + ")")
    head_ar = ra + ("" if not of else " لِـ«" + of[0] + "»") + (" بِـ«" + by + "»" if by else "")
    a = head_ar + " " + CASE[case][0] + " " + sa + dp[0]
    e = re_ + ((" «" + of[1] + "»") if of and role in ("naat", "badal", "tawkid") else (" to «" + of[1] + "»" if of else "")) + ((" after «" + by + "»") if by else "") + ", in " + CASE[case][1] + sg[1] + dp[1]
    t = rt + ((" («" + of[2] + "»)") if of else "") + ", " + CASE[case][2] + sg[2] + dp[2]
    if mudaf or enc: a, e, t = a + "، مُضَافٌ", e + ", annexed", t + ", muzâf"
    if enc:
        x = ENC_TXT(enc, "jarr", ref); a, e, t = a + x[0], e + x[1], t + x[2]
    a, e, t = a + note[0], e + note[1], t + note[2]
    pa, pe, pt = _pre_txt(pre, full, enc)
    jarr_pre = [k for k in pre if k in ("bi", "li", "ka")]
    G = list(dict.fromkeys(gr + list(g)))
    if jarr_pre:
        j = PRE_TXT[jarr_pre[0]]
        if a.startswith("اسْمٌ "): a = a[len("اسْمٌ "):]
        a2 = j[0] + _stem_show(full, pre, enc) + " " + a
        return X(full, jarr_pre[0], "prep", list(dict.fromkeys(["huruf-jarr"] + G)), pa + a2 + ".", _lc(pe + j[1], e) + ".", pt + j[2] + t + ".", p=p, pre=_pf(pre), enc=enc, s=lex, spos=pos)
    return X(full, lex, pos, G, pa + a + ".", _lc(pe, e) + ".", pt + t + ".", p=p, pre=_pf(pre), enc=enc)
def _pf(pre): return tuple(k.split("-")[0] for k in pre)
def _stem_show(full, pre, enc):
    rest = N(full)
    for k in pre:
        f = PF[k.split("-")[0]][0]
        if k == "li" and rest.startswith("لِلْ"): rest = "الْ" + rest[4:]; continue
        rest = rest[len(f):]
    if enc: rest = rest[:-len(enc)]
    return rest

VK = {  # verb kind → (ar, en, tr)
 "m": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "A past verb built on fatḥa", "Fetha üzere mebnî mâzî"),
 "ma": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الْمُقَدَّرِ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "A past verb built on a fatḥa estimated on the alif", "Elif üzerinde takdîrî fetha üzere mebnî mâzî"),
 "mt": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ تَاءُ التَّأْنِيثِ السَّاكِنَةُ", "A past verb built on fatḥa; the ta marks the feminine", "Fetha üzere mebnî mâzî; tâ te'nîs tâsıdır"),
 "mw": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
        "A past verb built on ḍamma because the waw of the group is attached; the waw is its doer, in the seat of raf'",
        "Cemaat vâvı bitiştiği için damme üzere mebnî mâzî; vâv fâildir, mahallen merfû"),
 "mwa": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ الْمُقَدَّرِ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
         "A past verb built on a ḍamma estimated on the alif dropped before the waw; the waw is its doer, in the seat of raf'",
         "İki sâkin karşılaştığı için düşen elif üzerinde takdîrî damme üzere mebnî mâzî; vâv fâildir"),
 "mA": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
        "A past verb built on fatḥa; the alif of the two is its doer, in the seat of raf'", "Fetha üzere mebnî mâzî; tesniye elifi fâildir, mahallen merfû"),
 "mn": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
        "A past verb built on sukūn because the nūn of the women is attached; the nūn is its doer", "Nûn-i nisve bitiştiği için sükûn üzere mebnî mâzî; nûn fâildir"),
 "mtu": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
         "A past verb built on sukūn because the doer's ta is attached; the ta («I») is its doer, in the seat of raf'",
         "Fâil tâsı bitiştiği için sükûn üzere mebnî mâzî; tâ (ben) fâildir, mahallen merfû"),
 "mta": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
         "A past verb built on sukūn because the doer's ta is attached; the ta («you») is its doer, in the seat of raf'",
         "Fâil tâsı bitiştiği için sükûn üzere mebnî mâzî; tâ (sen) fâildir, mahallen merfû"),
 "mna": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا» الْفَاعِلِينَ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
         "A past verb built on sukūn because «nā» of the doers is attached; «nā» («we») is its doer, in the seat of raf'",
         "Fâiller «nâ»sı bitiştiği için sükûn üzere mebnî mâzî; «nâ» (biz) fâildir, mahallen merfû"),
 "mtum": ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ الْمُتَحَرِّكِ، وَتُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
          "A past verb built on sukūn because a moving raf' pronoun is attached; تُمْ («you all») is its doer, in the seat of raf'",
          "Harekeli ref zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» (siz) fâildir, mahallen merfû"),
 "p": ("فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ", "A past verb in the passive, built on fatḥa", "Meçhul mâzî, fetha üzere mebnî"),
 "pt": ("فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ تَاءُ التَّأْنِيثِ السَّاكِنَةُ", "A past verb in the passive, built on fatḥa; the ta marks the feminine", "Meçhul mâzî, fetha üzere mebnî; tâ te'nîs tâsıdır"),
 "u": ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالْجَازِمِ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ", "A present verb in raf' (nothing puts it in nasb or jazm), by the ḍamma", "Nâsıb ve câzimden boş olduğu için merfû muzâri, damme ile"),
 "uy": ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالْجَازِمِ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ", "A present verb in raf', the ḍamma estimated on the ya", "Merfû muzâri; damme yâ üzerinde takdîrî"),
 "uw": ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالْجَازِمِ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْوَاوِ لِلثِّقَلِ", "A present verb in raf', the ḍamma estimated on the waw", "Merfû muzâri; damme vâv üzerinde takdîrî"),
 "ua": ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالْجَازِمِ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "A present verb in raf', the ḍamma estimated on the alif", "Merfû muzâri; damme elif üzerinde takdîrî"),
 "u5": ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ ثُبُوتُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
        "A present verb in raf' by the nūn that stays (one of the five verbs); the waw is its doer, in the seat of raf'",
        "Nûnun sübûtuyla merfû muzâri (ef'âl-i hamse); vâv fâildir, mahallen merfû"),
 "us": ("فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ", "A present verb in nasb after أَنْ, by the fatḥa", "«En» ile mansûb muzâri, fetha ile"),
 "usatf": ("فِعْلٌ مُضَارِعٌ مَعْطُوفٌ عَلَى الْمَنْصُوبِ قَبْلَهُ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ", "A present verb conjoined to the one in nasb before it, in nasb by the fatḥa", "Önceki mansûba ma'tûf, mansûb muzâri, fetha ile"),
 "uj": ("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ", "A present verb in jazm after لَمْ, by the sukūn", "«Lem» ile meczûm muzâri, sükûn ile"),
 "amr": ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ", "An imperative built on sukūn; its doer is the hidden «you», necessarily", "Sükûn üzere mebnî emir; fâili vücûben gizli «ente»"),
 "amrw": ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "An imperative built on dropping the nūn; the waw («you all») is its doer", "Nûnun hazfi üzere mebnî emir; vâv fâildir"),
 "amr-ilal": ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ", "An imperative built on dropping the weak letter; its doer is the hidden «you»", "İllet harfinin hazfi üzere mebnî emir; fâili gizli «ente»"),
}
HID_NAME = {"هُوَ": ("he", "hüve"), "هِيَ": ("she", "hiye"), "هُمْ": ("they", "hüm"), "هُمَا": ("they two", "hümâ"), "نَحْنُ": ("we", "nahnü"),
            "أَنَا": ("I", "ene"), "أَنْتَ": ("you", "ente"), "أَنْتُمْ": ("you all", "entüm")}
def VERB(full, lex, kind, g=(), hid=None, ref=None, doer_after=False, enc=None, encref=None, note=("", "", ""), cl=None, p=None, pre=(), form=None):
    """a verb: `kind` (VK), `hid` the hidden doer («هُوَ»/«هِيَ»/«هُمْ»/«نَحْنُ»/«أَنَا»), `ref` whom it names (ar, en, tr), `doer_after` (the doer is
    written after it), `enc` an attached object pronoun, `cl` the clause's seat (a tuple like SILA_, MAQUL …), `form` the bāb's grammar id"""
    a, e, t = VK[kind]
    if enc:
        x = ENC_TXT(enc, "nasb", encref); a, e, t = a + x[0], e + x[1], t + x[2]
    if hid:
        r = ref or ("", "", "")
        a += "، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: " + hid + (("، يَعُودُ عَلَى " + r[0]) if r[0] else "")
        if kind.startswith("p"): a = a.replace("وَالْفَاعِلُ ضَمِيرٌ", "وَنَائِبُ الْفَاعِلِ ضَمِيرٌ")
        he, ht = HID_NAME.get(hid, (hid, hid))
        e += ("; its deputy doer" if kind.startswith("p") else "; its doer") + " is the hidden «" + he + "»" + ((" (" + r[1] + ")") if r[1] else "")
        t += ("; nâib-i fâili" if kind.startswith("p") else "; fâili") + " gizli «" + ht + "»" + ((" (" + r[2] + ")") if r[2] else "")
    if doer_after:
        if kind.startswith("p"): a, e, t = a + "، وَنَائِبُ الْفَاعِلِ بَعْدَهُ", e + "; its deputy doer follows", t + "; nâib-i fâili sonra gelir"
        else: a, e, t = a + "، وَالْفَاعِلُ بَعْدَهُ", e + "; its doer follows", t + "; fâili sonra gelir"
    a, e, t = a + note[0], e + note[1], t + note[2]
    if cl: a, e, t = a + cl[0], e + cl[1], t + cl[2]
    pa, pe, pt = _pre_txt(pre, full, enc)
    gr = [form or "thulathi-mujarrad-babs"] + list(g)
    if enc: gr.append("al-bariz-al-muttasil")
    return X(full, lex, "verb", list(dict.fromkeys(gr)), pa + a + ".", _lc(pe, e) + ".", pt + t + ".", p=p, pre=_pf(pre), enc=enc)

def PART(full, lex, ar, en, tr, g=(), p=None, pre=(), enc=None, pos="part", s=None, spos=None):
    pa, pe, pt = _pre_txt(pre, full, enc)
    return X(full, lex, pos, list(g), pa + ar, _lc(pe, en), pt + tr, p=p, pre=_pf(pre), enc=enc, s=s, spos=spos)
def PREPT(full, lex, hang=("", "", ""), role=("", "", ""), p=None, pre=()):
    """a free jarr letter; `hang` names what the phrase hangs on"""
    a = "حَرْفُ جَرٍّ" + role[0] + (("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ " + hang[0]) if hang[0] else "") + "."
    e = "A jarr letter" + role[1] + (("; the phrase hangs on " + hang[1]) if hang[1] else "") + "."
    t = "Cer harfi" + role[2] + (("; câr-mecrûr " + hang[2] + " müteallik") if hang[2] else "") + "."
    return PART(full, lex, a, e, t, ["huruf-jarr"], p=p, pre=pre, pos="prep")
def PRON_J(full, lex, enc, hang=("", "", ""), ref=None, p=None, pre=(), role=("", "", "")):
    """a jarr letter with its attached pronoun (عَلَيْهِ، لَهُمْ، بِهِ …)"""
    r = ref or ("", "", "")
    nm = PRON_AR.get(enc, enc)
    a = "حَرْفُ جَرٍّ" + role[0] + "، وَ" + nm + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ" + (("، يَعُودُ عَلَى " + r[0]) if r[0] else "") + (("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ " + hang[0]) if hang[0] else "") + "."
    e = "A jarr letter" + role[1] + " with an attached pronoun in the seat of jarr" + ((" (" + r[1] + ")") if r[1] else "") + (("; the phrase hangs on " + hang[1]) if hang[1] else "") + "."
    t = "Cer harfi" + role[2] + " ve bitişik zamir, mahallen mecrûr" + ((" (" + r[2] + ")") if r[2] else "") + (("; câr-mecrûr " + hang[2] + " müteallik") if hang[2] else "") + "."
    return PART(full, lex, a, e, t, ["huruf-jarr", "al-bariz-al-muttasil"], p=p, pre=pre, enc=enc, pos="prep")
def H(ar, en, tr):
    """what a jarr phrase / ẓarf hangs on: H("بِـ«خَرَجَ»", "«went out»", "«harece»ye")"""
    return (ar, en, tr)

def SALLA(p=None):
    """«صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ» as the text writes it after the Prophet's name: a supplication set between, with no seat"""
    return [
     tok("صَلَّى", "salla", "verb", ["naqis-verbs", "form-ii-verbs", "jumla-mutarida"],
         "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الْمُقَدَّرِ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
         "«(may He) bless» — a past verb built on a fatḥa estimated on the alif; the supplication is set in between and has no seat.",
         "«salât etsin» — elif üzerinde takdîrî fetha üzere mebnî mâzî; dua cümlesi araya girmiştir, mahalli yoktur."),
     tok("اللهُ", "allah", "propn", ["fail"], "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The name of God, the doer, in raf'.", "Lafza-i celâl, fâil, merfû."),
     tok("عَلَيْهِ", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
         "حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى النَّبِيِّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«صَلَّى».",
         "A jarr letter with «him» (the Prophet) in the seat of jarr; the phrase hangs on «bless».", "Cer harfi; zamir (Peygamber'e döner) mahallen mecrûr — câr-mecrûr «sallâ»ya müteallik.",
         segments=[seg("عَلَيْ", "ala", "prep"), seg("هِ", "pron-3ms", "pron")]),
     tok("وَسَلَّمَ", "sallama", "verb", ["atf-nasaq", "form-ii-verbs"],
         "الْوَاوُ عَاطِفَةٌ، وَسَلَّمَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى اللهِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «صَلَّى» الْمُعْتَرِضَةِ، فَهِيَ مِثْلُهَا مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
         "«and (may He) grant peace» — the waw conjoins; a past verb built on fatḥa, its doer the hidden «He» (God); conjoined to the parenthetic «bless», it too is set in between, with no seat.",
         "«ve selâm etsin» — vâv atıf; fetha üzere mebnî mâzî, fâili gizli «hüve» (Allah); araya giren «sallâ»ya ma'tûf olduğundan o da mu'teriza, mahalli yoktur.", punct=p,
         segments=[seg("وَ", "wa", "conj"), seg("سَلَّمَ", "sallama", "verb")])]
def ALLAH_MI(p=None):
    return tok("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The name of God, the second term of the iḍāfa, in jarr.", "Lafza-i celâl, muzâfun ileyh, mecrûr.", punct=p)
def RASUL(role, case=None, p=None, pre=(), by=None, of=None, note=("", "", ""), salla=True):
    """«رَسُولُ اللهِ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ» in a seat: the six tokens"""
    case = case or ROLE[role][4]
    full = {"raf": "رَسُولُ", "nasb": "رَسُولَ", "jarr": "رَسُولِ"}[case]
    for k in pre: full = PF[k.split("-")[0]][0] + full
    out = [NOUN(full, "rasul", role, case, mudaf=True, pre=pre, by=by, of=of, note=note), ALLAH_MI(None if salla else p)]
    return out + (SALLA(p) if salla else [])
def BN(case, of, alif=False, p=None):
    """«ibn» between two names: a naʿt, its alif dropped in writing (the Siyar's line); alif=True where the print writes it (ابْن)"""
    full = {"raf": "بْنُ", "nasb": "بْنَ", "jarr": "بْنِ"}[case]
    if alif:
        return tok("ا" + full, "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"],
            "نَعْتٌ لِـ«" + of[0] + "» " + CASE[case][0] + " " + SIGN[None][case][0] + "، مُضَافٌ — وَكُتِبَتْ أَلِفُهُ هُنَا كَمَا فِي النَّصِّ الْمَطْبُوعِ، وَالْقِيَاسُ حَذْفُهَا بَيْنَ عَلَمَيْنِ.",
            "An adjective (naʿt) of «" + of[1] + "», in " + CASE[case][1] + " and annexed — its alif is written here as the print has it, though between two names it is normally dropped.",
            "«" + of[2] + "» isminin na'tı, " + CASE[case][2] + ", muzâf — elifi burada baskıdaki gibi yazıldı; iki alem arasında kural olarak düşer.", punct=p)
    return tok(full, "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"],
        "نَعْتٌ لِـ«" + of[0] + "» " + CASE[case][0] + " " + SIGN[None][case][0] + "، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
        "An adjective (naʿt) of «" + of[1] + "», in " + CASE[case][1] + " and annexed — its alif is dropped in writing because it stands between two names.",
        "«" + of[2] + "» isminin na'tı, " + CASE[case][2] + ", muzâf — iki alem arasında geldiği için elifi yazıda düşer.", punct=p)
def BINT(case, of, p=None):
    full = {"raf": "بِنْتُ", "nasb": "بِنْتَ", "jarr": "بِنْتِ"}[case]
    return tok(full, "bint", "noun", ["naat-sifa", "idafa-definiteness"],
        "نَعْتٌ لِـ«" + of[0] + "» " + CASE[case][0] + " " + SIGN[None][case][0] + "، مُضَافٌ.",
        "An adjective (naʿt) of «" + of[1] + "», in " + CASE[case][1] + " and annexed: «daughter of».", "«" + of[2] + "» isminin na'tı, " + CASE[case][2] + ", muzâf: «kızı».", punct=p)
def AN(full="عَنْ", hang=("", "", ""), p=None):
    """the isnād's عَنْ"""
    k = "، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ" if full == "عَنِ" else ""
    a = "حَرْفُ جَرٍّ" + k + (("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ " + hang[0]) if hang[0] else "") + "."
    e = "A jarr letter «from»" + (", voweled with kasra before the following sukūn" if k else "") + (("; the phrase hangs on " + hang[1]) if hang[1] else "") + "."
    t = "«-den» — cer harfi" + ("; iki sâkin karşılaştığı için kesre ile harekelendi" if k else "") + (("; câr-mecrûr " + hang[2] + " müteallik") if hang[2] else "") + "."
    return tok(full, "an", "prep", ["huruf-jarr"], a, e, t, punct=p)
VERSE_END = "•"
def QURAN(toks):
    """a Qurʾān quotation as the text gives it (Ḥafṣ): the quote marks, and the first token tagged al-iqtibas-wal-tadmin"""
    toks[0]["quoteBefore"] = "«"; toks[-1]["quoteAfter"] = "»"
    toks[0].setdefault("grammar", []).insert(0, "al-iqtibas-wal-tadmin")
    return toks
def ISHARA_T(full, lex, seat_ar, seat_en, seat_tr, built="السُّكُونِ", p=None, g=(), pre=()):
    """a demonstrative in its seat"""
    return PART(full, lex, "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى " + built + " " + seat_ar + ".", "A demonstrative, built, " + seat_en + ".", "İşaret ismi, mebnî, " + seat_tr + ".",
                ["asma-al-ishara-wa-sighuha"] + list(g), p=p, pre=pre, pos="pron")
def WALLAHI0(p=None):
    return PART("وَاللهِ", "allah", "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مُقْسَمٌ بِهِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: أُقْسِمُ.",
        "The waw of the oath, a jarr letter; the name of God is sworn by, in jarr — the phrase hangs on an omitted «I swear».",
        "Kasem vâvı, cer harfi; lafza-i celâl kendisiyle yemin edilen, mecrûr — gizli «uksimu»ya müteallik.",
        ["huruf-al-qasam-fil-kafiya", "huruf-jarr"], p=p, pos="propn")
def _wallahi(p=None):
    t = WALLAHI0(p); t["segments"] = [seg("وَ", "wa-qasam", "part"), seg("اللهِ", "allah", "propn")]; return t
WALLAHI = _wallahi

# ---- the isnād and the saying verbs ---------------------------------------------------------------------------------------
IBN_SAD = ("ابْنِ سَعْدٍ (أَوْ رَاوِي الْكِتَابِ عَنْهُ)", "Ibn Saʿd, or the book's transmitter from him", "İbn Sa'd ya da kitabın ondan râvisi")
NT = (" — وَلَمْ يُنَوَّنْ لِأَنَّهُ عَلَمٌ مَوْصُوفٌ بِـ«ابْن» مُضَافًا إِلَى عَلَمٍ", " — no tanwin: a name described by «ibn» annexed to a name", " — tenvin almaz: aleme muzâf «ibn» ile vasfedilmiş alem")
QALA_W = (" — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "; what follows is what is said, in the seat of nasb", "; sonrası mekūlü'l-kavl, mahallen mansûb")
def _wf(pre): return {("fa",): "فَ", ("wa",): "وَ"}.get(tuple(pre), "")
def QALA_HID(ref, p=":", pre=(), hid="هُوَ"):
    """قَالَ with its hidden doer named; what follows is its maqūl"""
    return VERB(_wf(pre) + "قَالَ", "qala", "m", g=["hollow-verbs"], hid=hid, ref=ref, cl=QALA_W, p=p, pre=pre)
def QALAT_HID(ref, p=":", pre=()):
    return VERB(_wf(pre) + "قَالَتْ", "qala", "mt", g=["hollow-verbs"], hid="هِيَ", ref=ref, cl=QALA_W, p=p, pre=pre)
def QALA_AFTER(p=None, pre=(), fem=False):
    """قَالَ / قَالَتْ whose doer is written after it"""
    return VERB(_wf(pre) + ("قَالَتْ" if fem else "قَالَ"), "qala", "mt" if fem else "m", g=["hollow-verbs"], doer_after=True, p=p, pre=pre)
def QALU(ref, p=":", pre=()):
    return VERB(_wf(pre) + "قَالُوا", "qala", "mw", g=["hollow-verbs"], note=(("، يَعُودُ عَلَى " + ref[0]) if ref[0] else "", " (" + ref[1] + ")", " (" + ref[2] + ")"), cl=QALA_W, p=p, pre=pre)
def NAME(full, lex, role, case=None, dipt=None, note=("", "", ""), p=None, by=None, sign=None, mudaf=False, pre=(), of=None, enc=None, ref=None):
    return NOUN(full, lex, role, case, pos="propn", dipt=dipt, note=note, p=p, by=by, sign=sign, mudaf=mudaf, pre=pre, of=of, enc=enc, ref=ref)
def ISNAD_AKHBARANA(full="أَخْبَرَنَا", note=("", "", "")):
    """أَخْبَرَنَا of the isnād: «nā» its object, the doer after it (the Siyar's line)"""
    return VERB(full, "akhbara", "m", form="form-iv-verbs", enc="نَا", doer_after=True, note=note, cl=MAQUL if False else None)
def ISNAD_HADDATHANA(full="حَدَّثَنَا", pre=()):
    return VERB(full, "haddatha", "m", form="form-ii-verbs", enc="نَا", doer_after=True, pre=pre)
def HADDATHANI(pre=()):
    full = ("وَ" if pre else "") + "حَدَّثَنِي"
    segs = ([seg("وَ", "wa", "conj")] if pre else []) + [seg("حَدَّثَ", "haddatha", "verb"), seg("نِي", "pron-1s", "pron")]
    w = ("الْوَاوُ عَاطِفَةٌ، وَحَدَّثَ ", "The waw conjoins; a", "«ve» + ") if pre else ("", "A", "")
    return tok(full, "haddatha", "verb", ["form-ii-verbs", "ya-al-mutakallim", "al-bariz-al-muttasil", "maful-bihi"],
        w[0] + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ.",
        w[1] + " past verb built on fatḥa; the nūn guards it and the ya («me») is its object, in the seat of nasb; its doer follows.",
        w[2] + "Fetha üzere mebnî mâzî; nûn vikâye içindir, yâ (beni) mef'ûlün bih, mahallen mansûb; fâili sonra gelir.", segments=segs)
def YA(p=None):
    return PART("يَا", "ya-nida", "حَرْفُ نِدَاءٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "يَا, the particle of calling.", "«Yâ» nidâ harfi.", ["al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada"], p=p)
def QAD(p=None):
    return PART("قَدْ", "qad", "حَرْفُ تَحْقِيقٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "قَدْ, the particle of assurance.", "«Kad» tahkîk harfi.", ["qad-harf"], p=p)
def FROM_PARADIGM(key, letters, note=None):
    """a new verb's paradigm made from a stored one of the same bāb and class by putting its radicals in their seats
    (letters = {old radical: new radical}); the stored cell-for-cell paradigm is the model, as v352-K built اِحْتَجَّ from اِشْتَدَّ"""
    for f in sorted((ROOT / "content/samples").glob("*/morphology.json")):
        v = json.loads(f.read_text(encoding="utf-8")).get("verbs", {})
        if key in v:
            src = json.dumps(v[key], ensure_ascii=False)
            src = src.translate(str.maketrans(letters))
            out = json.loads(src)
            if note: out["note"] = note
            return out
    raise KeyError(key)
def ALLAH_FAIL(p=None):
    return tok("اللهُ", "allah", "propn", ["fail"], "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The name of God, the doer, in raf'.", "Lafza-i celâl, fâil, merfû.", punct=p)
PRON.update({"يَّ": "pron-1s", "نِي": "pron-1s", "كُمُ": "pron-2mp"}); PRON_AR.update({"يَّ": "الْيَاءُ", "نِي": "الْيَاءُ", "ي": "الْيَاءُ"})
PRE_TXT["la-muz"] = ("اللَّامُ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَ", "The emphatic lam (moved onto the predicate); ", "Haberin başına kaydırılmış te'kîd lâmı; ")
def ALLAH_MUBT(p=None):
    return tok("اللهُ", "allah", "propn", ["mubtada-khabar"], "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The name of God, the mubtadaʾ, in raf'.", "Lafza-i celâl, mübtedâ, merfû.", punct=p)
