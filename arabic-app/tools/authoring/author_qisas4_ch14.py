# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 14: «الْقُرْآنُ يَحْكِي قِصَّةَ سُلَيْمَانَ (٢)» — §14, 27:29–36: the queen reads the letter,
consults, sends the gift, and Sulaymān refuses it; print p. 23. The Qurʾānic text is given as the book prints it.
python3 tools/authoring/author_qisas4_ch14.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "الْقُرْآنُ يَحْكِي قِصَّةَ سُلَيْمَانَ (٢)", "en": "The Qurʾān tells Sulaymān's story (2)", "tr": "Kur'ân Süleyman'ın kıssasını anlatır (2)"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"; NT = "nun-tawkid"; TW = "tawkid"; IS = "al-istifham"; IDS = "idha-shartiyya"
def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=(), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [ID] + list(tags), ar, en, tr, punct=punct)
def naat(full, lex, en, tr, punct=None, tags=(), case="jarr"):
    C = {"jarr": "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
    return tok(full, lex, "noun", [NA] + list(tags), C, en + " — the naʿt.", tr + " — sıfat.", punct=punct)
def prep_pron(full, lex, pron_form, pron_lex, en, tr, punct=None, tags=(), extra_ar=""):
    pre = full[:len(full) - len(pron_form)]
    return tok(full, lex, "prep", [HJ] + list(tags), "حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra_ar + ".", en, tr, punct=punct, segments=[seg(pre, lex, "prep"), seg(pron_form, pron_lex, "pron")])
def maful_(full, lex, en, tr, punct=None, tags=(), ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [MB] + list(tags), ar, en, tr, punct=punct)
def noun_pron(full, lex, stem, pron_form, pron_lex, ar, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", list(tags), ar, en, tr, punct=punct, segments=[seg(stem, lex, "noun"), seg(pron_form, pron_lex, "pron")])
def atf(full, lex, en, tr, case="jarr", punct=None, tags=(), pos="noun", sign=None):
    C = {"jarr": "مَعْطُوفٌ مَجْرُورٌ " + (sign or "بِالْكَسْرَةِ"), "raf": "مَعْطُوفٌ مَرْفُوعٌ " + (sign or "بِالضَّمَّةِ"), "nasb": "مَعْطُوفٌ مَنْصُوبٌ " + (sign or "بِالْفَتْحَةِ")}[case]
    return tok(full, lex, pos, [AT] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " " + C + ".", "«and» + " + en + " — joined by the wāw.", "«ve» + " + tr + " — vâv ile atıf.", punct=punct, segments=wa_(full[2:], lex, pos))
def prep(full, lex, en, tr, punct=None, ar="حَرْفُ جَرٍّ."): return tok(full, lex, "prep", [HJ], ar, en, tr, punct=punct)
def li_pron(full, pron_form, pron_lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, "li", "prep", [HJ] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra + ".", en, tr, punct=punct, segments=[seg(full[:2], "li", "prep"), seg(pron_form, pron_lex, "pron")])
def ya_ayyuha():
    return [tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
            tok("أَيُّهَا", "ayyuha", "noun", ["vocative-munada", "huruf-tanbih"], "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ، وَهَا لِلتَّنْبِيهِ.", "«O you» — the munādā ayy with the hā of alerting.", "«ey» — münâdâ eyyü, tenbih hâ'sı.")]
def qalat(punct=None):
    return tok("قَالَتْ", "qala", "verb", [MB, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«she said»", "«dedi»", punct=punct)

sen("s1", "«She said: O chiefs, a noble letter has been delivered to me» (27:29).",
        "«Dedi ki: Ey ileri gelenler, bana değerli bir mektup bırakıldı» (27:29).", [
  *quran([
  qalat(),
  *ya_ayyuha(),
  tok("الْمَلَأُ", "mala-chiefs", "noun", ["vocative-munada", NA], "نَعْتٌ لِأَيٍّ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ.", "«chiefs» — the naʿt of ayy.", "«ileri gelenler» — eyyü'nün sıfatı."),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«indeed I»", "«şüphesiz ben»", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أُلْقِيَ", "alqa", "verb", [IW, NF, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«has been delivered» — a passive; the clause is inna's khabar.", "«bırakıldı» — meçhul; cümle inne'nin haberi."),
  prep_pron("إِلَيَّ", "ila", "يَّ", "pron-1s", "«to me»", "«bana»", extra_ar=" — وَالْيَاءُ مُشَدَّدَةٌ لِإِدْغَامِ يَاءِ إِلَى فِيهَا"),
  tok("كِتَابٌ", "kitab", "noun", [NF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "«a letter» — the deputy doer.", "«bir mektup» — nâib-i fâil."),
  naat("كَرِيمٌ", "karim", "«noble»", "«değerli»", case="raf", tags=["sifa-mushabbaha"], punct="."),
  ]),
])
sen("s2", "«It is from Sulaymān, and it is: In the name of God, the Most Gracious, the Most Merciful» (27:30).",
        "«O Süleyman'dandır ve şöyledir: Rahmân ve Rahîm olan Allah'ın adıyla» (27:30).", [
  *quran([
  tok("إِنَّهُ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا.", "«it is»", "«o»", segments=[seg("إِنَّ", "inna", "part"), pr3ms()]),
  prep("مِنْ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ."),
  tok("سُلَيْمَانَ", "sulayman", "propn", [HJ, IW, MM], "مَجْرُورٌ بِمِنْ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān»", "«Süleyman»"),
  tok("وَإِنَّهُ", "inna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا.", "«and it is»", "«ve o»", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("بِسْمِ", "bism", "noun", [HJ, ID, IW], "الْبَاءُ حَرْفُ جَرٍّ، وَاسْمِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ (أَيْ: مُفْتَتَحٌ بِبِسْمِ اللهِ).", "«in the name [of]» — the jarr phrase is inna's khabar.", "«… adıyla» — câr-mecrûr inne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("سْمِ", "bism", "noun")]),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  naat("الرَّحْمٰنِ", "rahman", "«the Most Gracious»", "«Rahmân»", tags=["sighat-mubalagha"]),
  naat("الرَّحِيمِ", "rahim", "«the Most Merciful»", "«Rahîm»", tags=["sighat-mubalagha"], punct="."),
  ]),
])
sen("s3", "«Do not exalt yourselves against me, but come to me in submission» (27:31).",
        "«Bana karşı büyüklük taslamayın ve bana Müslümanlar olarak gelin» (27:31).", [
  *quran([
  tok("أَلَّا", "an-masdariyya", "part", [AN, "la-nahiya"], "أَنْ تَفْسِيرِيَّةٌ (أَوْ مَصْدَرِيَّةٌ)، وَلَا نَاهِيَةٌ، أُدْغِمَتِ النُّونُ فِي اللَّامِ.", "«that … not» — the explaining an fused with the prohibiting lā.", "«… -mayın diye» — tefsîriyye en, nehiy lâ'sı ile birleşmiş.", segments=[seg("أَ", "an-masdariyya", "part"), seg("لَّا", "la-nahiya", "part")]),
  tok("تَعْلُوا", "ala-rise", "verb", ["la-nahiya", AK, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«exalt yourselves» — jazm by the dropped nūn; the wāw the doer.", "«büyüklük taslayın» — nûnun düşmesiyle meczum; vâv fâil."),
  prep_pron("عَلَيَّ", "ala", "يَّ", "pron-1s", "«against me»", "«bana karşı»"),
  tok("وَأْتُونِي", "ata", "verb", [AT, AM, MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأْتُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — سَقَطَتْ هَمْزَةُ الْوَصْلِ لِلْعَطْفِ.", "«and come to me» — an imperative on the dropped nūn; the nūn of protection; the yāʾ the object.", "«ve bana gelin» — nûnun düşmesi üzere mebnî emir; vikâye nûnu; yâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("أْتُو", "ata", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("مُسْلِمِينَ", "muslim", "noun", [HL, JS, "ism-fail", "form-iv-verbs"], "حَالٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«in submission» (lit. as Muslims) — a ḥāl, naṣb by the yāʾ.", "«Müslümanlar olarak» — hâl, yâ ile mansub.", punct="."),
  ]),
])
sen("s4", "«She said: O chiefs, advise me in my affair; I never decide a matter until you are present with me» (27:32).",
        "«Dedi ki: Ey ileri gelenler, işimde bana görüş bildirin; siz yanımda olmadıkça hiçbir işi kesip atmam» (27:32).", [
  *quran([
  qalat(),
  *ya_ayyuha(),
  tok("الْمَلَأُ", "mala-chiefs", "noun", ["vocative-munada", NA], "نَعْتٌ لِأَيٍّ مَرْفُوعٌ.", "«chiefs»", "«ileri gelenler»"),
  tok("أَفْتُونِي", "afta", "verb", [AM, MB, "naqis-verbs", "form-iv-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«advise me» — an imperative on the dropped nūn; the yāʾ the object.", "«bana görüş bildirin» — nûnun düşmesi üzere mebnî emir; yâ mef'ûl.", segments=[seg("أَفْتُو", "afta", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  fi(), noun_pron("أَمْرِي", "amr-noun", "أَمْرِ", "ي", "pron-1s", "مَجْرُورٌ بِفِي بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my affair»", "«işimde»", tags=[HJ, ID, "ya-al-mutakallim"]),
  tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا النَّافِيَةُ.", "«never» — the negating mā.", "«hiç … -mam» — nefiy mâ'sı."),
  tok("كُنْتُ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ اسْمُهُ.", "«I am» — kāna with the tāʾ as its ism.", "«ben … -im» — kâne; tâ ismi.", segments=[seg("كُنْ", "kana", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("قَاطِعَةً", "qati", "noun", [KN, "ism-fail", ID, "idafa-lafziyya"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ فَاعِلٍ يَعْمَلُ عَمَلَ فِعْلِهِ.", "«one who decides» — kāna's khabar; an active participle governing like its verb.", "«kesip atan» — kâne'nin haberi; fiili gibi amel eden ism-i fâil."),
  tok("أَمْرًا", "amr-noun", "noun", [MB], "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ مَنْصُوبٌ.", "«a matter» — the object of the participle.", "«bir işi» — ism-i fâilin mef'ûlü."),
  tok("حَتَّى", "hatta", "part", [HJ, AN], "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهَا مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "«until» — ḥattā; the muḍāriʿ after it takes naṣb by a hidden an.", "«… -dıkça» — hattâ; sonraki muzari gizli en ile mansub."),
  tok("تَشْهَدُونِ", "shahida", "verb", [AN, AK, MB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ حَتَّى وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ الْمَحْذُوفَةُ مَفْعُولٌ بِهِ.", "«you are present with me» — naṣb by the dropped nūn; the nūn of protection; the speaker's yāʾ dropped.", "«yanımda olursunuz» — nûnun düşmesiyle mansub; vikâye nûnu; mütekellim yâ'sı hazfedilmiş.", punct=".", segments=[seg("تَشْهَدُو", "shahida", "verb"), seg("نِ", "nun-wiqaya", "part")]),
  ]),
])
sen("s5", "«They said: We are men of strength and of great might; but the command is yours, so consider what you will command» (27:33).",
        "«Dediler ki: Biz güç sahibiyiz, çetin bir savaş gücüne sahibiz; buyruk senindir; ne buyuracağına bak» (27:33).", [
  *quran([
  qalu(punct=None),
  tok("نَحْنُ", "nahnu", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«we» — the mubtadaʾ.", "«biz» — mübtedâ."),
  tok("أُولُو", "ulu", "noun", [MK, ID, "five-nouns"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، مُضَافٌ.", "«possessors [of]» — the khabar, rafʿ by the wāw; annexed.", "«sahipleri» — haber, vâv ile merfû; muzâf."),
  mudaf_ilayh("قُوَّةٍ", "quwwa", "«strength»", "«güç»"),
  tok("وَأُولُو", "ulu", "noun", [AT, ID, "five-nouns"], "الْوَاوُ عَاطِفَةٌ، وَأُولُو مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ.", "«and possessors [of]»", "«ve sahipleri»", segments=wa_("أُولُو", "ulu", "noun")),
  mudaf_ilayh("بَأْسٍ", "bas", "«might»", "«savaş gücü»"),
  naat("شَدِيدٍ", "shadid", "«great»", "«çetin»", tags=["sifa-mushabbaha"]),
  tok("وَالْأَمْرُ", "amr-noun", "noun", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْأَمْرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the command» — the mubtadaʾ.", "«ve buyruk» — mübtedâ.", segments=wa_("الْأَمْرُ", "amr-noun", "noun")),
  prep_pron("إِلَيْكِ", "ila", "كِ", "pron-2fs", "«is yours» — the khabar.", "«senindir» — haber.", tags=[MK]),
  tok("فَانْظُرِي", "nazara", "verb", [AT, AM, MB], "الْفَاءُ لِلتَّفْرِيعِ، وَانْظُرِي فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ فَاعِلٌ.", "«so consider» — an imperative on the dropped nūn; the yāʾ of address is the doer.", "«bak» — nûnun düşmesi üzere mebnî emir; muhâtaba yâ'sı fâil.", segments=[seg("فَ", "fa", "conj"), seg("انْظُرِي", "nazara", "verb")]),
  tok("مَاذَا", "madha", "pron", [IS, MB], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ لِتَأْمُرِينَ — وَالْجُمْلَةُ مَفْعُولُ انْظُرِي.", "«what» — the fronted object of «command»; the clause is the object of «consider».", "«ne» — «buyurursun»un öne alınmış mef'ûlü; cümle «bak»ın mef'ûlü."),
  tok("تَأْمُرِينَ", "amara-v", "verb", [AK, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ فَاعِلٌ.", "«you will command» — one of the five verbs; the yāʾ of address is the doer.", "«buyurursun» — ef'âl-i hamseden; muhâtaba yâ'sı fâil.", punct="."),
  ]),
])
sen("s6", "«She said: Kings, when they enter a town, ruin it and make the mightiest of its people the lowest; and so they do» (27:34).",
        "«Dedi ki: Hükümdarlar bir kente girdiklerinde orayı harap eder, halkının ulularını zelil kılarlar; onlar böyle yaparlar» (27:34).", [
  *quran([
  qalat(),
  inna(),
  ism_inna("الْمُلُوكَ", "malik-king", "«kings»", "«hükümdarlar»", tags=[JT]),
  tok("إِذَا", "idha", "noun", [IDS, MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the conditional ẓarf.", "«… -ınca» — şart zarfı."),
  mazi_pl("دَخَلُوا", "dakhala", "«they enter»", "«girerler»", tags=[IDS, MB]),
  maful_("قَرْيَةً", "qarya", "«a town»", "«bir kent»"),
  tok("أَفْسَدُوهَا", "afsada", "verb", [IDS, MB, "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ — جَوَابُ إِذَا، وَالْجُمْلَةُ الشَّرْطِيَّةُ خَبَرُ إِنَّ.", "«they ruin it» — the answer of idhā; the whole is inna's khabar.", "«orayı harap ederler» — izâ'nın cevabı; şart cümlesi inne'nin haberi.", segments=[seg("أَفْسَدُو", "afsada", "verb"), seg("هَا", "pron-3fs", "pron")]),
  mazi_pl("وَجَعَلُوا", "jaala", "«and make»", "«ve kılarlar»", tags=[AT, MX], wa=True),
  tok("أَعِزَّةَ", "aziz", "noun", [MB, MX, ID, JT], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ، مُضَافٌ — جَمْعُ عَزِيزٍ.", "«the mightiest [of]» — the first object, annexed.", "«ulularını» — ilk mef'ûl, muzâf."),
  noun_pron("أَهْلِهَا", "ahl", "أَهْلِ", "هَا", "pron-3fs", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«of its people»", "«halkının»", tags=[ID]),
  tok("أَذِلَّةً", "dhalil", "noun", [MB, MX, JT], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — جَمْعُ ذَلِيلٍ.", "«the lowest» — the second object.", "«zelil» — ikinci mef'ûl."),
  tok("وَكَذٰلِكَ", "kadhalika", "part", [AT, HJ, "asma-al-ishara"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْكَافُ حَرْفُ جَرٍّ، وَذٰلِكَ فِي مَحَلِّ جَرٍّ — فِي مَحَلِّ نَصْبٍ مَفْعُولٌ مُطْلَقٌ (فِعْلًا مِثْلَ ذٰلِكَ).", "«and so» — the kāf with the demonstrative, standing for an absolute object.", "«ve böyle» — kâf ve ism-i işâret; mef'ûl-i mutlak yerinde.", segments=wa_("كَذٰلِكَ", "kadhalika", "part")),
  khamsa("يَفْعَلُونَ", "faala", "«they do»", "«yaparlar»", tags=[], punct="."),
  ]),
])
sen("s7", "«And I am sending them a gift, and shall see with what the envoys return» (27:35).",
        "«Ben onlara bir hediye göndereceğim ve elçilerin ne ile döneceğine bakacağım» (27:35).", [
  *quran([
  tok("وَإِنِّي", "inna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«and indeed I»", "«ve şüphesiz ben»", segments=[seg("وَ", "wa", "conj"), seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  khabar_inna("مُرْسِلَةٌ", "mursil", "«sending»", "«gönderecek olan»", tags=["ism-fail", "form-iv-verbs"]),
  prep_pron("إِلَيْهِمْ", "ila", "هِمْ", "pron-3mp", "«to them»", "«onlara»"),
  tok("بِهَدِيَّةٍ", "hadiyya", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَهَدِيَّةٍ مَجْرُورٌ — مُتَعَلِّقٌ بِمُرْسِلَةٌ.", "«a gift» — attached to the participle.", "«bir hediye» — ism-i fâile bağlı.", segments=[seg("بِ", "bi", "prep"), seg("هَدِيَّةٍ", "hadiyya", "noun")]),
  tok("فَنَاظِرَةٌ", "nazir-looking", "noun", [AT, IW, "ism-fail"], "الْفَاءُ عَاطِفَةٌ، وَنَاظِرَةٌ مَعْطُوفٌ عَلَى مُرْسِلَةٌ مَرْفُوعٌ — خَبَرٌ ثَانٍ.", "«and seeing» — joined to the first khabar.", "«ve bakacak olan» — ilk habere ma'tûf.", segments=[seg("فَ", "fa", "conj"), seg("نَاظِرَةٌ", "nazir-looking", "noun")]),
  tok("بِمَ", "bima", "part", [HJ, IS], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْتِفْهَامِيَّةٌ حُذِفَتْ أَلِفُهَا لِدُخُولِ الْجَارِّ عَلَيْهَا.", "«with what» — the question-mā, its alif dropped after the jarr letter.", "«ne ile» — soru mâ'sı; cer harfinden sonra elifi düşmüş.", segments=[seg("بِ", "bi", "prep"), seg("مَ", "ma-istifham", "pron")]),
  mudari("يَرْجِعُ", "rajaa", "«return»", "«döner»", tags=[], hidden=None),
  tok("الْمُرْسَلُونَ", "mursal", "noun", [FL, JS, "ism-maful"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the envoys» — the doer, rafʿ by the wāw.", "«elçiler» — fâil, vâv ile merfû.", punct="."),
  ]),
])
sen("s8", "«When [the envoy] came to Sulaymān he said: Do you offer me wealth? What God has given me is better than what He has given you; rather it is you who rejoice in your gift» (27:36).",
        "«[Elçi] Süleyman'a gelince, o dedi ki: Bana mal mı sunuyorsunuz? Allah'ın bana verdiği, size verdiğinden daha hayırlıdır; aksine hediyenizle sevinen sizsiniz» (27:36).", [
  *quran([
  tok("فَلَمَّا", "lamma", "part", [AT, MF, SH], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — lammā.", "«… -ınca» — lemmâ.", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi("جَاءَ", "jaa", "«came»", "«geldi»", tags=[SH, "hollow-verbs", MB], hidden="هُوَ (الرَّسُولُ)"),
  tok("سُلَيْمَانَ", "sulayman", "propn", [MB, MM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān» — the object; a diptote.", "«Süleyman'a» — mef'ûl; gayr-i munsarıf."),
  qala(hidden="هُوَ", punct=None, tags=[SH]),
  tok("أَتُمِدُّونَنِ", "amadda", "verb", [IS, AK, "mudari-marfu", MB, "doubled-verbs", "form-iv-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَتُمِدُّونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ الْمَحْذُوفَةُ مَفْعُولٌ بِهِ.", "«do you offer me» — the hamza of denial; the five-verb nūn kept; the nūn of protection; the speaker's yāʾ dropped.", "«bana … mı sunuyorsunuz» — inkâr hemzesi; ef'âl-i hamse nûnu; vikâye nûnu; mütekellim yâ'sı hazfedilmiş.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تُمِدُّونَ", "amadda", "verb"), seg("نِ", "nun-wiqaya", "part")]),
  tok("بِمَالٍ", "mal", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَالٍ مَجْرُورٌ.", "«wealth»", "«mal»", segments=[seg("بِ", "bi", "prep"), seg("مَالٍ", "mal", "noun")]),
  tok("فَمَا", "ma-mawsula", "pron", [AT, MK, MW], "الْفَاءُ لِلتَّعْلِيلِ (أَوِ الِاسْتِئْنَافِ)، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what» — the relative, the mubtadaʾ.", "«… -diği» — ism-i mevsûl, mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-mawsula", "pron")]),
  tok("آتَانِيَ", "aataa", "verb", [MW, MX, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ — صِلَةٌ.", "«has given me» — the ṣila; the nūn of protection; the yāʾ the first object.", "«bana verdi» — sıla; vikâye nûnu; yâ ilk mef'ûl.", segments=[seg("آتَا", "aataa", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("يَ", "pron-1s", "pron")]),
  allah_fail(),
  tok("خَيْرٌ", "khayr", "noun", [MK, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ.", "«is better» — the khabar; an elative.", "«daha hayırlıdır» — haber; ism-i tafdîl."),
  tok("مِمَّا", "ma-mawsula", "pron", [HJ, MW], "مِنْ حَرْفُ جَرٍّ أُدْغِمَتْ فِي مَا الْمَوْصُولَةِ.", "«than what»", "«… -den»", segments=[seg("مِ", "min", "prep"), seg("مَّا", "ma-mawsula", "pron")]),
  tok("آتَاكُمْ", "aataa", "verb", [MW, MX, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَكُمْ مَفْعُولٌ بِهِ أَوَّلُ — صِلَةٌ.", "«He has given you» — the ṣila.", "«size verdi» — sıla.", segments=[seg("آتَا", "aataa", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  tok("بَلْ", "bal", "part", [AT], "حَرْفُ إِضْرَابٍ.", "«rather»", "«aksine»"),
  tok("أَنْتُمْ", "antum", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«you» — the mubtadaʾ.", "«siz» — mübtedâ."),
  noun_pron("بِهَدِيَّتِكُمْ", "hadiyya", "بِهَدِيَّتِ", "كُمْ", "pron-2mp", "الْبَاءُ حَرْفُ جَرٍّ، وَهَدِيَّتِ مَجْرُورٌ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِتَفْرَحُونَ، قُدِّمَ لِلِاخْتِصَاصِ.", "«in your gift» — attached to «rejoice», fronted for emphasis.", "«hediyenizle» — «sevinirsiniz»e bağlı; tahsis için öne alınmış.", tags=[HJ, ID]),
  khamsa("تَفْرَحُونَ", "fariha", "«rejoice»", "«sevinirsiniz»", tags=[MK], extra_ar=" — وَالْجُمْلَةُ خَبَرٌ", punct="."),
  ]),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: ala-rise, bism, bima, qati, mursil, nazir-looking are the new keys)
CAND = {
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O — the vocative particle", "ey — nidâ harfi", 1),
 "ayyuha": G("ayyuha", "أَيُّ", None, "noun", "O you — the vocative ayy", "ey — nidâ eyyü", 2),
 "mala-chiefs": G("mala-chiefs", "مَلَأ", "م ل أ", "noun", "the chiefs", "ileri gelenler", 2),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "alqa": G("alqa", "أَلْقَى", "ل ق ي", "verb", "to deliver, to cast", "bırakmak, atmak", 2),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "a letter", "mektup", 1),
 "karim": G("karim", "كَرِيم", "ك ر م", "noun", "noble, generous", "değerli, kerim", 1),
 "sulayman": G("sulayman", "سُلَيْمَان", None, "propn", "Sulaymān", "Süleyman", 1),
 "bism": G("bism", "بِسْمِ", "س م و", "noun", "in the name of — the basmala's opening", "adıyla — besmelenin başı", 1),
 "rahman": G("rahman", "الرَّحْمٰن", "ر ح م", "propn", "the Most Gracious", "Rahmân", 1),
 "rahim": G("rahim", "الرَّحِيم", "ر ح م", "propn", "the Most Merciful", "Rahîm", 1),
 "la-nahiya": G("la-nahiya", "لَا (النَّاهِيَة)", None, "part", "the prohibiting lā", "nehiy lâ'sı", 1),
 "ala-rise": G("ala-rise", "عَلَا", "ع ل و", "verb", "to rise above, to exalt oneself (with ʿalā)", "üstüne çıkmak, büyüklük taslamak (alâ ile)", 2),
 "ata": G("ata", "أَتَى", "أ ت ي", "verb", "to come", "gelmek", 1),
 "nun-wiqaya": G("nun-wiqaya", "نِ (نُونُ الْوِقَايَةِ)", None, "part", "the nūn of protection", "vikâye nûnu", 2),
 "muslim": G("muslim", "مُسْلِم", "س ل م", "noun", "a Muslim, one who submits", "Müslüman, teslim olan", 1),
 "afta": G("afta", "أَفْتَى", "ف ت و", "verb", "to give counsel, a ruling (Form IV, defective)", "görüş bildirmek, fetvâ vermek (if'âl, nâkıs)", 3),
 "amr-noun": G("amr-noun", "أَمْر", "أ م ر", "noun", "an affair, a matter; a command", "iş; buyruk", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "the negating mā", "nefiy mâ'sı", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "qati": G("qati", "قَاطِع", "ق ط ع", "noun", "one who decides, cuts (an active participle)", "kesip atan, karar veren (ism-i fâil)", 2),
 "hatta": G("hatta", "حَتَّى", None, "part", "until", "… -e kadar", 1),
 "shahida": G("shahida", "شَهِدَ", "ش ه د", "verb", "to be present; to witness", "hazır bulunmak; şahit olmak", 1),
 "nahnu": G("nahnu", "نَحْنُ", None, "pron", "we", "biz", 1),
 "ulu": G("ulu", "أُولُو", None, "noun", "possessors of, men of (the plural of ذُو)", "sahipleri (zû'nun çoğulu)", 2),
 "quwwa": G("quwwa", "قُوَّة", "ق و ي", "noun", "strength", "güç", 1),
 "bas": G("bas", "بَأْس", "ب أ س", "noun", "might, valour", "savaş gücü", 2),
 "shadid": G("shadid", "شَدِيد", "ش د د", "noun", "great, severe", "çetin", 1),
 "pron-2fs": G("pron-2fs", "كِ", None, "pron", "you / your (fem. singular, attached)", "sen / senin (müennes, bitişik)", 1),
 "nazara": G("nazara", "نَظَرَ", "ن ظ ر", "verb", "to look, to consider", "bakmak", 1),
 "madha": G("madha", "مَاذَا", None, "pron", "what?", "ne?", 1),
 "amara-v": G("amara-v", "أَمَرَ", "أ م ر", "verb", "to command", "buyurmak", 1),
 "malik-king": G("malik-king", "مَلِك", "م ل ك", "noun", "a king", "hükümdar", 1, plural="مُلُوك"),
 "idha": G("idha", "إِذَا", None, "part", "when", "… -ınca", 1),
 "dakhala": G("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1),
 "qarya": G("qarya", "قَرْيَة", "ق ر ي", "noun", "a town", "kent, köy", 1),
 "afsada": G("afsada", "أَفْسَدَ", "ف س د", "verb", "to ruin", "harap etmek", 2),
 "jaala": G("jaala", "جَعَلَ", "ج ع ل", "verb", "to make", "kılmak", 1),
 "aziz": G("aziz", "عَزِيز", "ع ز ز", "noun", "mighty, honoured", "aziz, ulu", 1, plural="أَعِزَّة"),
 "ahl": G("ahl", "أَهْل", "أ ه ل", "noun", "people", "halk", 1),
 "dhalil": G("dhalil", "ذَلِيل", "ذ ل ل", "noun", "lowly, abased", "zelil", 2, plural="أَذِلَّة"),
 "kadhalika": G("kadhalika", "كَذٰلِكَ", None, "part", "so, likewise", "böyle", 1),
 "faala": G("faala", "فَعَلَ", "ف ع ل", "verb", "to do", "yapmak", 1),
 "mursil": G("mursil", "مُرْسِل", "ر س ل", "noun", "one who sends (the active participle of Form IV)", "gönderen (if'âl ism-i fâili)", 2),
 "hadiyya": G("hadiyya", "هَدِيَّة", "ه د ي", "noun", "a gift", "hediye", 1),
 "nazir-looking": G("nazir-looking", "نَاظِر", "ن ظ ر", "noun", "one who looks, waits to see (an active participle)", "bakan, bekleyen (ism-i fâil)", 2),
 "bima": G("bima", "بِمَ", None, "part", "with what? — bi with the question-mā, its alif dropped", "ne ile? — soru mâ'sı ile bâ, elifi düşmüş", 2),
 "ma-istifham": G("ma-istifham", "مَا (الِاسْتِفْهَامِيَّة)", None, "pron", "what?", "ne?", 1),
 "rajaa": G("rajaa", "رَجَعَ", "ر ج ع", "verb", "to return", "dönmek", 1),
 "mursal": G("mursal", "مُرْسَل", "ر س ل", "noun", "an envoy, one sent (a passive participle)", "elçi, gönderilen (ism-i mef'ûl)", 2),
 "lamma": G("lamma", "لَمَّا", None, "part", "when", "… -ınca", 2),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1),
 "amadda": G("amadda", "أَمَدَّ", "م د د", "verb", "to supply, to offer", "sunmak", 3),
 "hamza-istifham": G("hamza-istifham", "أَ (هَمْزَةُ الِاسْتِفْهَامِ)", None, "part", "the hamza of question", "soru hemzesi", 1),
 "mal": G("mal", "مَال", "م و ل", "noun", "wealth", "mal", 1),
 "aataa": G("aataa", "آتَى", "أ ت ي", "verb", "to give", "vermek", 2),
 "khayr": G("khayr", "خَيْر", "خ ي ر", "noun", "better", "daha hayırlı", 1),
 "bal": G("bal", "بَلْ", None, "part", "rather", "aksine", 2),
 "antum": G("antum", "أَنْتُمْ", None, "pron", "you", "siz", 1),
 "fariha": G("fariha", "فَرِحَ", "ف ر ح", "verb", "to rejoice", "sevinmek", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "I / me (attached)", "ben / beni (bitişik)", 1),
 "pron-2mp": G("pron-2mp", "كُمْ", None, "pron", "you (attached)", "siz (bitişik)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ala-rise", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "عَلَ", "عْل", "u", "اُعْل", "عُلُوّ", "عَالٍ (الْعَالِي)", None, None, None, "عَلَا يَعْلُو: ارْتَفَعَ؛ وَعَلَا عَلَيْهِ: تَكَبَّرَ — نَاقِصٌ وَاوِيٌّ مِنْ بَابِ نَصَرَ؛ لَمْ يَعْلُ، لَا تَعْلُوا."))
put_morph(mo, "afta", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَفْتَ", "فْت", "i", "أَفْت", "إِفْتَاء", "مُفْتٍ (الْمُفْتِي)", "مُفْتًى", "أُفْتِيَ", "يُفْتَى", "أَفْتَاهُ فِي الْأَمْرِ: بَيَّنَ لَهُ الْحُكْمَ وَأَشَارَ عَلَيْهِ."))
put_morph(mo, "shahida", _sg.sound1("samia", "شَهِد", "شْهَد", "اِشْهَد", "شُهُود", "شَاهِد", "مَشْهُود", "شُهِدَ", "يُشْهَدُ", "شَهِدَ الْأَمْرَ: حَضَرَهُ؛ وَشَهِدَ عَلَيْهِ: أَخْبَرَ بِمَا رَأَى."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch14 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 14 (print p. 23, §14 part 2): the Qurʾān's telling, 27:29–36 — the queen reads the letter, consults her chiefs, sends the gift, and Sulaymān refuses it (s1–s8)."
ADD_TR = " On dördüncü bölüm (baskı s. 23, 14. kısım 2. parça): Kur'ân'ın anlatımı, 27:29–36 — kraliçe mektubu okur, erkânına danışır, hediyeyi gönderir ve Süleyman onu reddeder (s1–s8)."
write_out(14, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §14 (27:29–36)", GLOSS_ADD, notes=(), related=())
report(14, S, GLOSS_ADD, ())
