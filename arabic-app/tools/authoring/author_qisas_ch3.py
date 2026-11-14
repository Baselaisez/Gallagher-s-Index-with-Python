# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 3: «نَارٌ بَارِدَةٌ» — sections 6–8 of «من كسر الأصنام؟» (print pp. 12–15): the cold fire,
«who is my Lord?» (the star, the moon, the sun) and «my Lord is Allah». s4 quotes al-Anbiyāʾ 21:68, s7 quotes 21:69 and s16 al-Anʿām 6:78
as the print sets them (marked). Every printed line is one sentence; the vowelling is the print's. python3 tools/authoring/author_qisas_ch3.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "نَارٌ بَارِدَةٌ", "en": "A cold fire", "tr": "Soğuk bir ateş"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def ibrahim_maful(punct=None): return maful_name("إِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm»", "«İbrâhim'i»", punct=punct)
def ibrahim_jarr(full, punct=None, pre_ar="", pre_en="", pre_tr="", segs=None):
    return tok(full, "ibrahim", "propn", ["huruf-jarr", "mamnu-min-sarf"], pre_ar + "إِبْرَاهِيمَ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", pre_en + "«Ibrāhīm» — in jarr shown by fatḥa: a diptote.", pre_tr + "«İbrâhim» — kesre yerine fetha ile mecrûr: gayr-i munsarıf.", punct=punct, segments=segs)
def hayy_la_yamut(wa=False, punct=".", part="إِنَّ"):
    return [khabar_inna("وَحَيٌّ" if wa else "حَيٌّ", "hayy", "«living»", "«diri»", part=part, tags=(["atf-nasaq"] if wa else []), extra=(" — مَعْطُوفٌ عَلَى الْخَبَرِ قَبْلَهُ" if wa else "")),
            la_nafiya(), neg_mudari("يَمُوتُ", "mata", "«dies»", "«ölür»", tags=["hollow-verbs", "jumla-sifa"], hidden="هُوَ", punct=punct, extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ ثَانٍ (أَوْ حَالٌ)")]
def baqin_la_yaghib(wa=False, punct=".", part="إِنَّ"):
    return [tok("وَبَاقٍ" if wa else "بَاقٍ", "baqi", "noun", ["inna-wa-akhawatuha", "ism-fail"] + (["atf-nasaq"] if wa else []), W(wa) + f"خَبَرُ {part} مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — اسْمٌ مَنْقُوصٌ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْيَاءِ.", Wen(wa) + "«ever-remaining» — the khabar in rafʿ by an estimated ḍamma on the dropped yāʾ: a manqūṣ noun, its tanwīn standing in for the yāʾ.", Wtr(wa) + "«bâkî» — düşen yâ üzerinde takdîrî damme ile merfû haber: mankûs isim; tenvin yânın ivazıdır.", segments=(wa_("بَاقٍ", "baqi", "noun") if wa else None)),
            la_nafiya(), neg_mudari("يَغِيبُ", "ghaba", "«vanishes»", "«kaybolur»", tags=["hollow-verbs", "jumla-sifa"], hidden="هُوَ", punct=punct, extra=" — وَالْجُمْلَةُ خَبَرٌ ثَانٍ")]
def qawi_la_yaghlib(wa=False, punct=".", part="إِنَّ"):
    return [tok("وَقَوِيٌّ" if wa else "قَوِيٌّ", "qawi", "noun", ["inna-wa-akhawatuha", "sifa-mushabbaha"] + (["atf-nasaq"] if wa else []), W(wa) + f"خَبَرُ {part} مَرْفُوعٌ بِالضَّمَّةِ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ.", Wen(wa) + "«strong» — the khabar, in rafʿ; a resembling adjective on faʿīl.", Wtr(wa) + "«güçlü» — haber, merfû; faîl vezninde sıfat-ı müşebbehe.", segments=(wa_("قَوِيٌّ", "qawi", "noun") if wa else None)),
            la_nafiya(),
            tok("يَغْلِبُهُ", "ghalaba", "verb", ["la-nafiya", "mudari-marfu", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَالْجُمْلَةُ خَبَرٌ ثَانٍ.", "«overcomes Him» — rafʿ after the negating lā; the pronoun «Him» is the object, placed before the doer.", "«ona galip gelir» — nefiy lâ'sından sonra merfû; «ona» zamiri öne alınmış mef'ûl.", segments=[seg("يَغْلِبُ", "ghalaba", "verb"), seg("هُ", "pron-3ms", "pron")]),
            fail("شَيْءٌ", "shay", "«anything»", "«hiçbir şey»", punct=punct, extra_ar=" مُؤَخَّرٌ")]
def daif_khabar(full, lex, en, tr, punct=None, fem=False):
    return tok(full, lex, "noun", ["mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — صِفَةٌ مُشَبَّهَةٌ" + (" مُؤَنَّثَةٌ بِالتَّاءِ" if fem else "") + ".", en + " — the khabar, in rafʿ; a resembling adjective.", tr + " — haber, merfû; sıfat-ı müşebbehe.", punct=punct)
def mubtada_al(full, lex, en, tr, wa=True, punct=None):
    return tok(full, lex, "noun", ["mubtada-khabar"] + (["atf-nasaq"] if wa else []), W(wa) + "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", Wen(wa) + en + " — the mubtadaʾ, in rafʿ.", Wtr(wa) + tr + " — mübtedâ, merfû.", punct=punct, segments=(wa_(full[2:], lex, "noun") if wa else None))
def yaghlibu_h(full, obj_pron, obj_lex, en, tr, punct=None, wa=False):
    base = full[2:] if wa else full
    verb = base[:-len(obj_pron)]
    return tok(full, "ghalaba", "verb", ["mudari-marfu", "jumla-sifa"] + (["atf-nasaq"] if wa else []), W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالضَّمِيرُ الْمُتَّصِلُ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ ثَانٍ.", Wen(wa) + en + " — a muḍāriʿ in rafʿ with its object pronoun first; the clause is a second khabar.", Wtr(wa) + tr + " — merfû muzari, mef'ûl zamiri önde; cümle ikinci haberdir.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(verb, "ghalaba", "verb"), seg(obj_pron, obj_lex, "pron")])
def la_yansuruni(full, lex, en, tr, wa=True, ta=False):
    verb = full
    return [la_nafiya("وَلَا" if wa else "لَا", wa=wa),
            tok(verb, lex, "verb", ["la-nafiya", "mudari-marfu", "ya-al-mutakallim"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", en + " — rafʿ after the negating lā; the nūn of protection and the speaker's yāʾ as the object.", tr + " — nefiy lâ'sından sonra merfû; vikâye nûnu ve mütekellim yâsı mef'ûldür.", segments=[seg(verb[:-3], lex, "verb"), seg("نِي", "pron-1s", "pron")])]
def li_annahu(full, pron_lex, en, tr, fem=False):
    return li_pron(full, pron_lex, "«because " + ("it (f.)" if fem else "it") + "» — the lām of cause on anna; the pronoun is its ism.", "«çünkü o» — ta'lil lâmı + enne; zamir ismidir.", "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالضَّمِيرُ الْمُتَّصِلُ فِي مَحَلِّ نَصْبٍ اسْمُهَا.")
def rabb_khabar(full, en, tr, punct=None, part="أَنَّ", extra_tags=()):
    return tok(full, "rabb", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"] + list(extra_tags), f"خَبَرُ {part} مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", en + " — the khabar of anna, in rafʿ; annexed.", tr + " — enne'nin haberi, merfû; muzâf.", punct=punct)
def mudaf_ilayh_al(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["idafa-definiteness"] + list(tags), "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", en + " — the annexed noun, in jarr.", tr + " — muzâfun ileyh, mecrûr.", punct=punct)

# ================================================================ §6 نار باردة (p. 12)
sen("s1", "The people gathered and said: What shall we do?", "İnsanlar toplandı ve dediler: Ne yapalım?", [
  mazi("اجْتَمَعَ", "ijtamaa", "«gathered»", "«toplandı»", tags=["form-viii-verbs"], hidden=None), nas_fail(),
  qalu("وَقَالُوا", wa=True),
  tok("مَاذَا", "madha", "pron", ["al-istifham", "maful-bihi"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«what» — the interrogative noun, built, in the place of naṣb: the object, placed first.", "«ne» — mebnî istifham ismi, mahallen mansub; öne alınmış mef'ûl."),
  tok("نَفْعَلُ", "faala", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ.", "«we do» — a muḍāriʿ in rafʿ; «we» is concealed by necessity.", "«yaparız» — merfû muzari; fâil zorunlu gizli «biz».", punct="؟")])
sen("s2", "Ibrāhīm has broken the idols and insulted the gods!", "İbrâhim putları kırdı ve ilâhları aşağıladı!", [
  inna(), tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — the ism of inna, in naṣb; a diptote name.", "«İbrâhim» — inne'nin ismi, mansub; gayr-i munsarıf."),
  mazi("كَسَرَ", "kasara", "«broke»", "«kırdı»", hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  maful("الْأَصْنَامَ", "sanam", "«the idols»", "«putları»", tags=["jam-taksir"]),
  tok("وَأَهَانَ", "ahana", "verb", ["atf-nasaq", "form-iv-verbs", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَهَانَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — مِنْ بَابِ الْإِفْعَالِ، أَجْوَفُ.", "«and insulted» — a Form IV hollow māḍī; the doer «he» is concealed.", "«ve aşağıladı» — if'âl bâbından ecvef mâzî; fâil gizli «o».", segments=[seg("وَ", "wa", "conj"), seg("أَهَانَ", "ahana", "verb")]),
  maful("الْآلِهَةَ", "ilah", "«the gods»", "«ilâhları»", tags=["jam-taksir"], punct="!", extra_ar=" — جَمْعُ إِلَهٍ")])
sen("s3", "And the people asked: What is Ibrāhīm's punishment? What is Ibrāhīm's due?", "Ve insanlar sordu: İbrâhim'in cezası ne? İbrâhim'in karşılığı ne?", [
  mazi("وَسَأَلَ", "saala", "«asked»", "«sordu»", hidden=None, wa=True), nas_fail(punct=":"),
  tok("مَا", "ma-istifham", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what» — the interrogative noun, the mubtadaʾ.", "«ne» — istifham ismi, mübtedâ."),
  tok("عِقَابُ", "iqab", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the punishment» — the khabar, in rafʿ; annexed.", "«cezası» — haber, merfû; muzâf."),
  tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«of Ibrāhīm» — the annexed noun, jarr by fatḥa: a diptote.", "«İbrâhim'in» — muzâfun ileyh, fetha ile mecrûr: gayr-i munsarıf.", punct="؟"),
  tok("مَا", "ma-istifham", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what» — the interrogative noun, the mubtadaʾ.", "«ne» — istifham ismi, mübtedâ."),
  tok("جَزَاءُ", "jaza-answer", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the due» — the khabar, in rafʿ; annexed.", "«karşılığı» — haber, merfû; muzâf."),
  tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«of Ibrāhīm» — the annexed noun, jarr by fatḥa.", "«İbrâhim'in» — muzâfun ileyh, fetha ile mecrûr.", punct="؟")])
sen("s4", "The answer was: «Burn him and help your gods!» (al-Anbiyāʾ 21:68)", "Cevap şu oldu: «Onu yakın ve ilâhlarınıza yardım edin!» (Enbiyâ 21:68)", [
  kana("كَانَ", wa=False), tok("الْجَوَابُ", "jawab", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — وَخَبَرُهَا الْجُمْلَةُ الْمَحْكِيَّةُ بَعْدَهُ.", "«the answer» — kāna's ism; its khabar is the quoted sentence.", "«cevap» — kâne'nin ismi; haberi sonraki nakledilen cümledir.", punct=":")] + quran([
  tok("حَرِّقُوهُ", "harraqa", "verb", ["imperative-amr", "form-ii-verbs", K], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«burn him» — an imperative built on the dropped nūn; the wāw is the doer, «him» the object; the clause is kāna's khabar.", "«onu yakın» — nûnun hazfi üzere mebnî emir; vâv fâil, «onu» mef'ûl; cümle kâne'nin haberidir.", segments=[seg("حَرِّقُوا", "harraqa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("وَانْصُرُوا", "nasara", "verb", ["atf-nasaq", "imperative-amr"], "الْوَاوُ عَاطِفَةٌ، وَانْصُرُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and help» — an imperative on the dropped nūn; the wāw is the doer.", "«ve yardım edin» — nûnun hazfi üzere mebnî emir; vâv fâil.", segments=[seg("وَ", "wa", "conj"), seg("انْصُرُوا", "nasara", "verb")]),
  tok("آلِهَتَكُمْ", "ilah", "noun", ["maful-bihi", "idafa-definiteness", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَكُمْ ضَمِيرٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«your gods» — the object; annexed to «your».", "«ilâhlarınızı» — mef'ûl; «siz»e muzâf.", punct=".", segments=[seg("آلِهَةَ", "ilah", "noun"), seg("كُمْ", "pron-2mp", "pron")])]))
sen("s5", "And so it was: they lit a fire and threw Ibrāhīm into it.", "Ve öyle oldu: bir ateş yaktılar ve İbrâhim'i içine attılar.", [
  tok("وَهٰكَذَا", "hakadha", "pron", ["mubtada-khabar", "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهٰكَذَا: الْكَافُ لِلتَّشْبِيهِ وَذَا اسْمُ إِشَارَةٍ — فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ (أَيْ: كَانَ الْأَمْرُ كَذٰلِكَ).", "«and so» — the kāf of likeness on a demonstrative; kāna's khabar, fronted («the matter was like this»).", "«ve öyle» — teşbih kâfı + ism-i işâret; kâne'nin öne alınmış haberi («durum böyle oldu»).", segments=[seg("وَ", "wa", "conj"), seg("هٰكَذَا", "hakadha", "pron")]),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — أَيِ الْأَمْرُ.", "«was» — kāna; its ism is concealed («the matter»).", "«oldu» — kâne; ismi gizli («durum»).", punct=":"),
  mazi_pl("أَوْقَدُوا", "awqada", "«they lit»", "«yaktılar»", tags=["form-iv-verbs", "mithal-verbs"]),
  maful("نَارًا", "nar", "«a fire»", "«bir ateş»"),
  tok("وَأَلْقَوْا", "alqa", "verb", ["atf-nasaq", "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَلْقَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ الْمُقَدَّرِ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ.", "«and threw» — a nāqiṣ māḍī built on an estimated ḍamma on the dropped alif; the wāw is the doer.", "«ve attılar» — düşen elif üzerinde takdîrî damme ile mebnî nâkıs mâzî; vâv fâil.", segments=[seg("وَ", "wa", "conj"), seg("أَلْقَوْا", "alqa", "verb")]),
  tok("فِيهَا", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَهَا ضَمِيرٌ فِي مَحَلِّ جَرٍّ.", "«into it» — the jarr letter on the pronoun.", "«içine» — cer harfi + zamir.", segments=[seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")]),
  ibrahim_maful(punct=".")])
sen("s6", "But Allah helped Ibrāhīm and said to the fire:", "Fakat Allah İbrâhim'e yardım etti ve ateşe dedi:", [
  tok("وَلٰكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "«but» — the heavy lākinna of correction: naṣb on its ism, rafʿ on its khabar.", "«fakat» — şeddeli istidrak harfi lâkinne: ismini nasb, haberini ref eder.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part")]),
  allah_ism("اللهَ", part="لٰكِنَّ"),
  mazi("نَصَرَ", "nasara", "«helped»", "«yardım etti»", hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"),
  ibrahim_maful(),
  qala("وَقَالَ", punct=None, wa=True, hidden="هُوَ"),
  tok("لِلنَّارِ", "nar", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالنَّارِ مَجْرُورٌ بِالْكَسْرَةِ.", "«to the fire» — the lām of jarr; in jarr.", "«ateşe» — cer lâmı; mecrûr.", punct=":", segments=[seg("لِ", "li", "prep"), seg("النَّارِ", "nar", "noun")])])
sen("s7", "«O fire, be coolness and safety for Ibrāhīm.» (al-Anbiyāʾ 21:69)", "«Ey ateş, İbrâhim'e serin ve selâmet ol.» (Enbiyâ 21:69)", quran([
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
  tok("نَارُ", "nar", "noun", ["vocative-munada"], "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«fire» — a specified-indefinite vocative, built on ḍamma in the place of naṣb.", "«ateş» — nekire-i maksûde münâdâ, zamme üzere mebnî, mahallen mansub."),
  tok("كُونِي", "kana", "verb", [K, "imperative-amr", "hollow-verbs"], "فِعْلُ أَمْرٍ نَاقِصٌ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا.", "«be» — the defective verb's imperative, built on the dropped nūn; the yāʾ of the addressed woman is its ism.", "«ol» — nâkıs fiilin emri, nûnun hazfi üzere mebnî; muhâtaba yâsı ismidir."),
  tok("بَرْدًا", "bard", "noun", [K], "خَبَرُ كُونِي مَنْصُوبٌ بِالْفَتْحَةِ.", "«coolness» — the khabar of «be», in naṣb.", "«serinlik» — «ol»un haberi, mansub."),
  tok("وَسَلَامًا", "salam", "noun", ["atf-nasaq", K], "الْوَاوُ عَاطِفَةٌ، وَسَلَامًا مَعْطُوفٌ عَلَى بَرْدًا مَنْصُوبٌ مِثْلُهُ.", "«and safety» — joined to «coolness», in the same naṣb.", "«ve selâmet» — berd'e ma'tûf, mansub.", segments=[seg("وَ", "wa", "conj"), seg("سَلَامًا", "salam", "noun")]),
  tok("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for» (upon).", "«üzerine»."),
  ibrahim_jarr("إِبْرَاهِيمَ", punct=".")]))
sen("s8", "And so it was: the fire was coolness and safety for Ibrāhīm.", "Ve öyle oldu: ateş İbrâhim'e serin ve selâmet oldu.", [
  tok("وَهٰكَذَا", "hakadha", "pron", ["mubtada-khabar", "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهٰكَذَا فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«and so» — kāna's khabar, fronted.", "«ve öyle» — kâne'nin öne alınmış haberi.", segments=[seg("وَ", "wa", "conj"), seg("هٰكَذَا", "hakadha", "pron")]),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — أَيِ الْأَمْرُ.", "«was» — kāna; its ism is concealed.", "«oldu» — kâne; ismi gizli.", punct="،"),
  tok("كَانَتِ", "kana", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَكُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«was» — kāna with the feminine tāʾ, its kasra for the meeting of two sukūns.", "«oldu» — kâne + te'nis tâsı; iki sâkinin karşılaşması için kesre."),
  tok("النَّارُ", "nar", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the fire» — kāna's ism, in rafʿ.", "«ateş» — kâne'nin ismi, merfû."),
  tok("بَرْدًا", "bard", "noun", [K], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«coolness» — kāna's khabar, in naṣb.", "«serinlik» — kâne'nin haberi, mansub."),
  tok("وَسَلَامًا", "salam", "noun", ["atf-nasaq", K], "الْوَاوُ عَاطِفَةٌ، وَسَلَامًا مَعْطُوفٌ عَلَى بَرْدًا مَنْصُوبٌ.", "«and safety» — joined to «coolness».", "«ve selâmet» — berd'e ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("سَلَامًا", "salam", "noun")]),
  tok("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«üzerine»."),
  ibrahim_jarr("إِبْرَاهِيمَ", punct=".")])
sen("s9", "And the people saw that the fire did not harm Ibrāhīm.", "Ve insanlar ateşin İbrâhim'e zarar vermediğini gördü.", [
  mazi("وَرَأَى", "raa", "«saw»", "«gördü»", tags=["naqis-verbs"], hidden=None, wa=True), nas_fail(),
  anna(obj_of="رَأَى"), ism_inna("النَّارَ", "nar", "«the fire»", "«ateşin»", part="أَنَّ"),
  la_nafiya(), neg_mudari("تَضُرُّ", "darra", "«harms»", "«zarar verir»", tags=["doubled-verbs"], extra=" — وَالْجُمْلَةُ خَبَرُ أَنَّ"),
  ibrahim_maful(punct=".")])
sen("s10", "And the people saw that Ibrāhīm was happy, and that Ibrāhīm was safe.", "Ve insanlar İbrâhim'in sevinçli ve sağ salim olduğunu gördü.", [
  mazi("وَرَأَى", "raa", "«saw»", "«gördü»", tags=["naqis-verbs"], hidden=None, wa=True), nas_fail(),
  anna(obj_of="رَأَى"), tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — the ism of anna; a diptote.", "«İbrâhim'in» — enne'nin ismi; gayr-i munsarıf."),
  khabar_inna("مَسْرُورٌ", "masrur", "«happy»", "«sevinçli»", part="أَنَّ", tags=["ism-maful"], punct="،", extra=" — اسْمُ مَفْعُولٍ"),
  anna(wa=True, obj_of="رَأَى"), tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Ibrāhīm» — the ism of anna.", "«İbrâhim'in» — enne'nin ismi."),
  khabar_inna("سَالِمٌ", "salim", "«safe»", "«sağ salim»", part="أَنَّ", tags=["ism-fail"], punct=".", extra=" — اسْمُ فَاعِلٍ")])
sen("s11", "And the people were amazed and bewildered.", "Ve insanlar hayrete düştü ve şaşkına döndü.", [
  mazi("وَدَهِشَ", "dahisha", "«were amazed»", "«hayrete düştü»", hidden=None, wa=True), nas_fail(),
  tok("وَتَحَيَّرُوا", "tahayyara", "verb", ["atf-nasaq", "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَحَيَّرُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ — مِنْ بَابِ التَّفَعُّلِ.", "«and were bewildered» — a Form V māḍī on ḍamma; the wāw is the doer.", "«ve şaşkına döndüler» — tefa''ul bâbından mâzî; vâv fâil.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("تَحَيَّرُوا", "tahayyara", "verb")])])

# ================================================================ §7 من ربي (pp. 13–14)
def hadha_rabbi(punct="."):
    return [ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
            tok("رَبِّي", "rabb", "noun", ["mubtada-khabar", "ya-al-mutakallim", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — the khabar, rafʿ by an estimated ḍamma before the speaker's yāʾ; annexed to «my».", "«Rabbim» — mütekellim yâsından önce takdîrî damme ile merfû haber; yâ muzâfun ileyh.", punct=punct, segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")])]
def laysa_bi_rabbi(punct="!"):
    return [la_nafiya("لَا", punct="!"),
            ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»", tags=["mubtada-khabar"]),
            tok("لَيْسَ", "laysa", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«is not» — the frozen defective verb; its ism is concealed; the clause is the khabar.", "«değildir» — câmid nâkıs fiil; ismi gizli; cümle haberdir."),
            tok("بِرَبِّي", "rabb", "noun", [K, "huruf-jarr", "ya-al-mutakallim"], "الْبَاءُ زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ، وَرَبِّي خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — the extra bāʾ strengthens the negation; the khabar of laysa, jarr in form and naṣb in place.", "«Rabbim» — zâid bâ nefyi pekiştirir; leyse'nin haberi, lafzan mecrûr, mahallen mansub.", punct=punct, segments=[seg("بِ", "bi", "prep"), seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")])]
sen("s12", "And one night Ibrāhīm saw a star, and said: This is my Lord.", "Ve bir gece İbrâhim bir yıldız gördü ve dedi: Bu benim Rabbimdir.", [
  tok("وَذَاتَ", "dhat", "noun", ["maful-fih", "idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَذَاتَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«one (night)» — an adverb of time in naṣb; annexed.", "«bir (gece)» — mansub zaman zarfı; muzâf.", segments=[seg("وَ", "wa", "conj"), seg("ذَاتَ", "dhat", "noun")]),
  mudaf_ilayh_al("لَيْلَةٍ", "layla", "«night»", "«gece»", punct="،"),
  mazi("رَأَى", "raa", "«saw»", "«gördü»", tags=["naqis-verbs"], hidden=None),
  fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  maful("كَوْكَبًا", "kawkab", "«a star»", "«bir yıldız»", punct="،"),
  qala("فَقَالَ", wa=True, hidden="هُوَ")] + hadha_rabbi())
S[-1]["tokens"][5]["segments"] = [seg("فَ", "fa", "conj"), seg("قَالَ", "qala", "verb")]
S[-1]["tokens"][5]["irab"]["ar"] = S[-1]["tokens"][5]["irab"]["ar"].replace("الْوَاوُ عَاطِفَةٌ", "الْفَاءُ عَاطِفَةٌ")
def lamma_ghaba(subj_full, subj_lex, subj_en, subj_tr, fem=False):
    return [tok("وَلَمَّا", "lamma", "part", ["maful-fih"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمَّا حِينِيَّةٌ ظَرْفُ زَمَانٍ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the lammā of time («at the moment that»), with a conditional sense.", "«ve … -ınca» — hîniyye lemmâ: «o zaman ki» mânâsında zaman zarfı, şart mânâlı.", segments=[seg("وَ", "wa", "conj"), seg("لَمَّا", "lamma", "part")]),
            (mazi_ta("غَابَتِ", "ghaba", "«set»", "«battı»", tags=["hollow-verbs"], extra="، وَكُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ") if fem else mazi("غَابَ", "ghaba", "«set»", "«battı»", tags=["hollow-verbs"], hidden=None)),
            fail(subj_full, subj_lex, subj_en, subj_tr, punct=("" if fem else "،") or None)]
sen("s13", "And when the star set, Ibrāhīm said: No! This is not my Lord!", "Ve yıldız batınca İbrâhim dedi: Hayır! Bu benim Rabbim değil!", lamma_ghaba("الْكَوْكَبُ", "kawkab", "«the star»", "«yıldız»") + [
  qala(punct=None), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=":")] + laysa_bi_rabbi())
sen("s14", "And Ibrāhīm saw the moon and said: This is my Lord.", "Ve İbrâhim ayı gördü ve dedi: Bu benim Rabbimdir.", [
  mazi("وَرَأَى", "raa", "«saw»", "«gördü»", tags=["naqis-verbs"], hidden=None, wa=True),
  fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  maful("الْقَمَرَ", "qamar", "«the moon»", "«ayı»"),
  qala("فَقَالَ", wa=True, hidden="هُوَ")] + hadha_rabbi())
S[-1]["tokens"][3]["segments"] = [seg("فَ", "fa", "conj"), seg("قَالَ", "qala", "verb")]
S[-1]["tokens"][3]["irab"]["ar"] = S[-1]["tokens"][3]["irab"]["ar"].replace("الْوَاوُ عَاطِفَةٌ", "الْفَاءُ عَاطِفَةٌ")
sen("s15", "And when the moon set, Ibrāhīm said: No! This is not my Lord!", "Ve ay batınca İbrâhim dedi: Hayır! Bu benim Rabbim değil!", lamma_ghaba("الْقَمَرُ", "qamar", "«the moon»", "«ay»") + [
  qala(punct=None), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=":")] + laysa_bi_rabbi())
sen("s16", "And the sun rose, and Ibrāhīm said: «This is my Lord; this is bigger.» (al-Anʿām 6:78)", "Ve güneş doğdu; İbrâhim dedi: «Bu benim Rabbimdir; bu daha büyüktür.» (En'âm 6:78)", [
  mazi_ta("وَطَلَعَتِ", "talaa", "«rose»", "«doğdu»", wa=True, extra="، وَكُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("الشَّمْسُ", "shams", "«the sun»", "«güneş»", punct="،"),
  qala("فَقَالَ", wa=True, hidden="هُوَ", punct=None), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=":")] + quran(hadha_rabbi(punct=None) + [
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("أَكْبَرُ", "akbar", "noun", ["mubtada-khabar", "ism-tafdil", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ فَلَا يُنَوَّنُ.", "«bigger» — the khabar, in rafʿ; an elative, a diptote and so without tanwīn.", "«daha büyük» — haber, merfû; ism-i tafdîl, gayr-i munsarıf olduğu için tenvinsiz.", punct=".")]))
S[-1]["tokens"][2]["segments"] = [seg("فَ", "fa", "conj"), seg("قَالَ", "qala", "verb")]
S[-1]["tokens"][2]["irab"]["ar"] = S[-1]["tokens"][2]["irab"]["ar"].replace("الْوَاوُ عَاطِفَةٌ", "الْفَاءُ عَاطِفَةٌ")
sen("s17", "And when the sun set in the night, Ibrāhīm said: No! This is not my Lord.", "Ve güneş gece batınca İbrâhim dedi: Hayır! Bu benim Rabbim değil.", lamma_ghaba("الشَّمْسُ", "shams", "«the sun»", "«güneş»", fem=True) + [
  tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("اللَّيْلِ", "layl", "noun", ["huruf-jarr"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the night» — in jarr.", "«gece» — mecrûr."),
  qala(punct=None), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=":")] + laysa_bi_rabbi(punct="."))
sen("s18", "Allah is living; He does not die.", "Allah diridir, ölmez.", [inna(), allah_ism()] + hayy_la_yamut())
sen("s19", "Allah is ever-remaining; He does not vanish.", "Allah bâkîdir, kaybolmaz.", [inna(), allah_ism()] + baqin_la_yaghib())
sen("s20", "Allah is strong; nothing overcomes Him.", "Allah güçlüdür; O'na hiçbir şey galip gelemez.", [inna(), allah_ism()] + qawi_la_yaghlib())
sen("s21", "And the star is weak: the dawn overcomes it.", "Ve yıldız zayıftır; sabah ona galip gelir.", [
  mubtada_al("وَالْكَوْكَبُ", "kawkab", "«the star»", "«yıldız»"), daif_khabar("ضَعِيفٌ", "daif", "«weak»", "«zayıf»"),
  yaghlibu_h("يَغْلِبُهُ", "هُ", "pron-3ms", "«overcomes it»", "«ona galip gelir»"),
  fail("الصُّبْحُ", "subh", "«the dawn»", "«sabah»", punct=".")])
sen("s22", "And the moon is weak: the sun overcomes it.", "Ve ay zayıftır; güneş ona galip gelir.", [
  mubtada_al("وَالْقَمَرُ", "qamar", "«the moon»", "«ay»"), daif_khabar("ضَعِيفٌ", "daif", "«weak»", "«zayıf»"),
  yaghlibu_h("تَغْلِبُهُ", "هُ", "pron-3ms", "«overcomes it»", "«ona galip gelir»"),
  fail("الشَّمْسُ", "shams", "«the sun»", "«güneş»", punct=".")])
sen("s23", "And the sun is weak: the night overcomes it, and the cloud overcomes it.", "Ve güneş zayıftır; gece ona galip gelir, bulut ona galip gelir.", [
  mubtada_al("وَالشَّمْسُ", "shams", "«the sun»", "«güneş»"), daif_khabar("ضَعِيفَةٌ", "daif", "«weak»", "«zayıf»", fem=True),
  yaghlibu_h("يَغْلِبُهَا", "هَا", "pron-3fs", "«overcomes it»", "«ona galip gelir»"),
  fail("اللَّيْلُ", "layl", "«the night»", "«gece»"),
  yaghlibu_h("وَيَغْلِبُهَا", "هَا", "pron-3fs", "«and overcomes it»", "«ve ona galip gelir»", wa=True),
  fail("الْغَيْمُ", "ghaym", "«the cloud»", "«bulut»", punct=".")])
sen("s24", "And the star does not help me, because it is weak.", "Ve yıldız bana yardım etmez; çünkü o zayıftır.", la_yansuruni("يَنْصُرُنِي", "nasara", "«helps me»", "«bana yardım eder»") + [
  fail("الْكَوْكَبُ", "kawkab", "«the star»", "«yıldız»"),
  li_annahu("لِأَنَّهُ", "pron-3ms", "", ""), khabar_inna("ضَعِيفٌ", "daif", "«weak»", "«zayıf»", part="أَنَّ", tags=["sifa-mushabbaha"], punct=".")])
sen("s25", "And the moon does not help me, because it is weak.", "Ve ay bana yardım etmez; çünkü o zayıftır.", la_yansuruni("يَنْصُرُنِي", "nasara", "«helps me»", "«bana yardım eder»") + [
  fail("الْقَمَرُ", "qamar", "«the moon»", "«ay»"),
  li_annahu("لِأَنَّهُ", "pron-3ms", "", ""), khabar_inna("ضَعِيفٌ", "daif", "«weak»", "«zayıf»", part="أَنَّ", tags=["sifa-mushabbaha"], punct=".")])
sen("s26", "And the sun does not help me, because it is weak.", "Ve güneş bana yardım etmez; çünkü o zayıftır.", la_yansuruni("تَنْصُرُنِي", "nasara", "«helps me»", "«bana yardım eder»") + [
  fail("الشَّمْسُ", "shams", "«the sun»", "«güneş»"),
  li_annahu("لِأَنَّهَا", "pron-3fs", "", "", fem=True), khabar_inna("ضَعِيفَةٌ", "daif", "«weak»", "«zayıf»", part="أَنَّ", tags=["sifa-mushabbaha"], punct=".")])
sen("s27", "And Allah helps me.", "Ve Allah bana yardım eder.", [
  tok("وَيَنْصُرُنِي", "nasara", "verb", ["mudari-marfu", "ya-al-mutakallim", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَيَنْصُرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«and helps me» — a muḍāriʿ in rafʿ; the nūn of protection and the speaker's yāʾ as the object.", "«ve bana yardım eder» — merfû muzari; vikâye nûnu ve mütekellim yâsı mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("يَنْصُرُ", "nasara", "verb"), seg("نِي", "pron-1s", "pron")]),
  allah_fail(punct=".")])
sen("s28", "Because Allah is living; He does not die.", "Çünkü Allah diridir, ölmez.", [
  tok("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«because» — the lām of cause on anna.", "«çünkü» — ta'lil lâmı + enne."),
  allah_ism("اللهَ", part="أَنَّ")] + hayy_la_yamut(part="أَنَّ"))
sen("s29", "And ever-remaining; He does not vanish.", "Ve bâkîdir, kaybolmaz.", baqin_la_yaghib(wa=True, part="أَنَّ"))
sen("s30", "And strong; nothing overcomes Him.", "Ve güçlüdür; O'na hiçbir şey galip gelemez.", qawi_la_yaghlib(wa=True, part="أَنَّ"))

# ================================================================ §8 ربي الله (pp. 14–15)
sen("s31", "And Ibrāhīm knew that Allah was his Lord.", "Ve İbrâhim Allah'ın kendi Rabbi olduğunu bildi.", [
  mazi("وَعَرَفَ", "arafa", "«knew»", "«bildi»", hidden=None, wa=True), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  anna(obj_of="عَرَفَ"), allah_ism("اللهَ", part="أَنَّ"),
  tok("رَبُّهُ", "rabb", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his Lord» — the khabar of anna, in rafʿ; annexed to «his».", "«onun Rabbi» — enne'nin haberi, merfû; «o»na muzâf.", punct=".", segments=[seg("رَبُّ", "rabb", "noun"), seg("هُ", "pron-3ms", "pron")])])
sen("s32", "Because Allah is living; He does not die.", "Çünkü Allah diridir, ölmez.", [
  tok("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«because» — the lām of cause on anna.", "«çünkü» — ta'lil lâmı + enne."),
  allah_ism("اللهَ", part="أَنَّ")] + hayy_la_yamut(part="أَنَّ"))
sen("s33", "And that Allah is ever-remaining; He does not vanish.", "Ve Allah'ın bâkî olduğunu, kaybolmadığını.", [anna(wa=True, obj_of="عَرَفَ"), allah_ism("اللهَ", part="أَنَّ")] + baqin_la_yaghib(part="أَنَّ"))
sen("s34", "And that Allah is strong; nothing overcomes Him.", "Ve Allah'ın güçlü olduğunu; O'na hiçbir şeyin galip gelemediğini.", [anna(wa=True, obj_of="عَرَفَ"), allah_ism("اللهَ", part="أَنَّ")] + qawi_la_yaghlib(part="أَنَّ"))
sen("s35", "And Ibrāhīm knew that Allah is the Lord of the star!", "Ve İbrâhim Allah'ın yıldızın Rabbi olduğunu bildi!", [
  mazi("وَعَرَفَ", "arafa", "«knew»", "«bildi»", hidden=None, wa=True), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  anna(obj_of="عَرَفَ"), allah_ism("اللهَ", part="أَنَّ"), rabb_khabar("رَبُّ", "«the Lord»", "«Rabbi»"), mudaf_ilayh_al("الْكَوْكَبِ", "kawkab", "«of the star»", "«yıldızın»", punct="!")])
sen("s36", "And that Allah is the Lord of the moon!", "Ve Allah'ın ayın Rabbi olduğunu!", [anna(wa=True, obj_of="عَرَفَ"), allah_ism("اللهَ", part="أَنَّ"), rabb_khabar("رَبُّ", "«the Lord»", "«Rabbi»"), mudaf_ilayh_al("الْقَمَرِ", "qamar", "«of the moon»", "«ayın»", punct="!")])
sen("s37", "And that Allah is the Lord of the sun!", "Ve Allah'ın güneşin Rabbi olduğunu!", [anna(wa=True, obj_of="عَرَفَ"), allah_ism("اللهَ", part="أَنَّ"), rabb_khabar("رَبُّ", "«the Lord»", "«Rabbi»"), mudaf_ilayh_al("الشَّمْسِ", "shams", "«of the sun»", "«güneşin»", punct="!")])
sen("s38", "And that Allah is the Lord of the worlds!", "Ve Allah'ın âlemlerin Rabbi olduğunu!", [anna(wa=True, obj_of="عَرَفَ"), allah_ism("اللهَ", part="أَنَّ"), rabb_khabar("رَبُّ", "«the Lord»", "«Rabbi»"),
  tok("الْعَالَمِينَ", "alam", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«of the worlds» — the annexed noun; its jarr shown by the yāʾ, as a word attached to the sound masculine plural.", "«âlemlerin» — muzâfun ileyh; cem'-i müzekker sâlime mülhak olduğu için yâ ile mecrûr.", punct="!")])
sen("s39", "And Allah guided Ibrāhīm and made him a prophet and an intimate friend.", "Ve Allah İbrâhim'e hidâyet etti ve onu peygamber ve halîl kıldı.", [
  mazi("وَهَدَى", "hada", "«guided»", "«hidâyet etti»", tags=["naqis-verbs"], hidden=None, wa=True), allah_fail(), ibrahim_maful(),
  tok("وَجَعَلَهُ", "jaala", "verb", ["atf-nasaq", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَجَعَلَ فِعْلٌ مَاضٍ يَنْصِبُ مَفْعُولَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«and made him» — a māḍī that takes two objects; the doer «He» is concealed; «him» is the first object.", "«ve onu kıldı» — iki mef'ûl alan mâzî; fâil gizli «O»; «onu» birinci mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("جَعَلَ", "jaala", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("نَبِيًّا", "nabi", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a prophet» — the second object, in naṣb.", "«peygamber» — ikinci mef'ûl, mansub."),
  tok("وَخَلِيلًا", "khalil", "noun", ["atf-nasaq", "sifa-mushabbaha"], "الْوَاوُ عَاطِفَةٌ، وَخَلِيلًا مَعْطُوفٌ عَلَى نَبِيًّا مَنْصُوبٌ — فَعِيلٌ بِمَعْنَى فَاعِلٍ.", "«and an intimate friend» — joined to «a prophet», in naṣb; faʿīl in the sense of fāʿil.", "«ve halîl» — nebiyyen'e ma'tûf, mansub; fâil mânâsında faîl.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("خَلِيلًا", "khalil", "noun")])])
sen("s40", "And Allah commanded Ibrāhīm to call his people and to keep them from worshipping the idols.", "Ve Allah İbrâhim'e kavmini çağırmasını ve onları putlara tapmaktan alıkoymasını emretti.", [
  mazi("وَأَمَرَ", "amara-v", "«commanded»", "«emretti»", hidden=None, wa=True), allah_fail(), ibrahim_maful(punct="،"),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِحَرْفِ جَرٍّ مَحْذُوفٍ (أَمَرَهُ بِأَنْ…).", "«to» — the maṣdar-making particle; the clause stands under an unspoken jarr letter («commanded him to…»).", "«-masını» — masdariyye harfi; cümle hazfedilmiş cer harfinin mahallindedir («ona … emretti»)."),
  tok("يَدْعُوَ", "daa", "verb", ["an-masdariyya", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«call» — in naṣb by an, the fatḥa written on the wāw; the doer is concealed.", "«çağırmasını» — en ile mansub; fetha vâv üzerinde zâhirdir; fâil gizli."),
  tok("قَوْمَهُ", "qawm", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people» — the object; annexed to «his».", "«kavmini» — mef'ûl; «o»na muzâf.", segments=[seg("قَوْمَ", "qawm", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("وَيَمْنَعَهُمْ", "manaa", "verb", ["atf-nasaq", "an-masdariyya"], "الْوَاوُ عَاطِفَةٌ، وَيَمْنَعَ مَعْطُوفٌ عَلَى يَدْعُوَ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُمْ مَفْعُولٌ بِهِ.", "«and keep them» — joined to «call», in naṣb; «them» is the object.", "«ve onları alıkoymasını» — yed'uve'ye ma'tûf, mansub; «onlar» mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("يَمْنَعَ", "manaa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("عِبَادَةِ", "ibada", "noun", ["huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ بِمِنْ، وَهُوَ مُضَافٌ — مَصْدَرُ عَبَدَ.", "«worshipping» — in jarr by «from»; annexed; the maṣdar of ʿabada.", "«tapmak(tan)» — min ile mecrûr; muzâf; abede'nin masdarı."),
  mudaf_ilayh_al("الْأَصْنَامِ", "sanam", "«the idols»", "«putlara»", punct=".", tags=["jam-taksir"])])

# ---------------------------------------------------------------- glossary
NEW = {
 "ahana": G("ahana", "أَهَانَ", "ه و ن", "verb", "to insult, to treat with contempt", "aşağılamak, hor görmek", 2, form="IV"),
 "iqab": G("iqab", "عِقَاب", "ع ق ب", "noun", "punishment", "ceza", 2),
 "jawab": G("jawab", "جَوَاب", "ج و ب", "noun", "answer", "cevap", 1, plural="أَجْوِبَة"),
 "harraqa": G("harraqa", "حَرَّقَ", "ح ر ق", "verb", "to burn (transitive, intensive)", "yakmak", 2, form="II"),
 "hakadha": G("hakadha", "هٰكَذَا", None, "pron", "thus, so (the kāf of likeness on the demonstrative)", "böyle, öyle (ism-i işâret üzerinde teşbih kâfı)", 1),
 "awqada": G("awqada", "أَوْقَدَ", "و ق د", "verb", "to kindle, light (a fire)", "(ateş) yakmak, tutuşturmak", 2, form="IV"),
 "masrur": G("masrur", "مَسْرُور", "س ر ر", "noun", "happy, glad (passive participle)", "sevinçli (ism-i mef'ûl)", 1),
 "tahayyara": G("tahayyara", "تَحَيَّرَ", "ح ي ر", "verb", "to be bewildered, perplexed", "şaşkına dönmek", 2, form="V"),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü, kuvvetli", 1),
 "ghalaba": G("ghalaba", "غَلَبَ", "غ ل ب", "verb", "to overcome, defeat", "yenmek, galip gelmek", 1, form="I"),
 "ghaym": G("ghaym", "غَيْم", "غ ي م", "noun", "cloud(s)", "bulut", 1, plural="غُيُوم"),
 "khalil": G("khalil", "خَلِيل", "خ ل ل", "noun", "intimate friend (Ibrāhīm's title, khalīl Allāh)", "halîl, can dostu (İbrâhim'in lakabı)", 2),
 "laysa": G("laysa", "لَيْسَ", None, "verb", "is not (a frozen defective verb of kāna's family)", "değildir (kâne grubundan câmid fiil)", 1),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))

# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ghalaba", _sg.sound1("daraba", "غَلَب", "غْلِب", "اِغْلِب", "غَلَبَة", "غَالِب", "مَغْلُوب", "غُلِبَ", "يُغْلَبُ"))
put_morph(mo, "harraqa", _sg.derived("بَابُ التَّفْعِيلِ: فَعَّلَ يُفَعِّلُ", "فَعَّلَ يُفَعِّلُ", "ُ", "حَرَّق", "حَرِّق", "حَرِّق", "تَحْرِيق", "مُحَرِّق", "مُحَرَّق", "حُرِّقَ", "يُحَرَّقُ"))
put_morph(mo, "tahayyara", _sg.derived("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَحَيَّر", "تَحَيَّر", "تَحَيَّر", "تَحَيُّر", "مُتَحَيِّر", note="لَازِمٌ — الْيَاءُ صَحَّتْ لِتَضْعِيفِهَا."))
put_morph(mo, "ahana", _sg.idgham(_sg.derived_hollow("مِنْ بَابِ الْإِفْعَالِ — أَجْوَفُ وَاوِيٌّ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَهَان", "أَهَن", "هِين", "هِن", "أَهِين", "أَهِن", "إِهَانَة", "مُهِين", "مُهَان", "أُهِينَ", "يُهَانُ", note="أَجْوَفُ: قُلِبَتِ الْوَاوُ أَلِفًا فِي الْمَاضِي (أَهْوَنَ → أَهَانَ) وَيَاءً فِي الْمُضَارِعِ.")))
put_morph(mo, "awqada", _sg.derived("مِنْ بَابِ الْإِفْعَالِ — مِثَالٌ وَاوِيٌّ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَوْقَد", "وقِد", "أَوْقِد", "إِيقَاد", "مُوقِد", "مُوقَد", "أُوقِدَ", "يُوقَدُ", note="مِثَالٌ: الْوَاوُ بَعْدَ الضَّمَّةِ حَرْفُ مَدٍّ (يُوقِدُ)، وَبَعْدَ الْكَسْرَةِ تُقْلَبُ يَاءً (إِيقَاد)."))
if "laysa" not in mo["verbs"]:
    try: mo["verbs"]["laysa"] = find_morph("laysa")
    except KeyError: pass
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

ADD_EN = (" Chapter 3 (print pp. 12–15, sections 6–8): the cold fire (s1–s11), «who is my Lord?» — the star, the moon and the sun (s12–s30) and «my Lord is Allah» (s31–s40). "
          "s4 quotes al-Anbiyāʾ 21:68, s7 quotes 21:69 and s16 quotes al-Anʿām 6:78 as the print sets them (marked). One printed line is one sentence; the printed vowelling is kept.")
ADD_TR = (" Üçüncü bölüm (basılı s. 12–15, 6–8. kısımlar): soğuk ateş (s1–s11), «Rabbim kim?» — yıldız, ay ve güneş (s12–s30) ve «Rabbim Allah» (s31–s40). "
          "s4 Enbiyâ 21:68'i, s7 21:69'u, s16 En'âm 6:78'i baskıdaki şekliyle aktarır (işaretli). Basılı her satır bir cümledir; basılı hareke korunmuştur.")
write_out(3, S, TITLE, ADD_EN, ADD_TR, "pp. 12–15", GLOSS_ADD)
report(3, S, GLOSS_ADD, ())
