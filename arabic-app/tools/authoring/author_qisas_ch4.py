# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 4: «دَعْوَةُ إِبْرَاهِيمَ» — sections 9–10 of «من كسر الأصنام؟» (print pp. 15–18): Ibrāhīm's
call to his people (the dialogue of al-Shuʿarāʾ 26:71–74 and the creed of 26:78–81, quoted as the print sets them and marked) and
«before the king» — the king who «gives life and death», the two men, and the sun from the west (al-Baqara 2:258, marked).
Every printed line is one sentence; the vowelling is the print's. python3 tools/authoring/author_qisas_ch4.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
import qisas_common as _qc
PKG = _qc.PKG
TITLE = {"ar": "دَعْوَةُ إِبْرَاهِيمَ", "en": "Ibrāhīm's call", "tr": "İbrâhim'in daveti"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

# ---------------------------------------------------------------- local helpers
def ibrahim_maful(punct=None): return maful_name("إِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm»", "«İbrâhim'i»", punct=punct)
def ibrahim_fail(punct=None): return fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=punct)
def malik_fail(full="الْمَلِكُ", punct=None): return fail(full, "malik-king", "«the king»", "«kral»", punct=punct)
def li_al(full, lex, en, tr, punct=None, tags=(), extra=""):
    """لِلْمَلِكِ، لِلّٰهِ — the jarr lām swallowing the article's alif."""
    return tok(full, lex, "noun" if lex != "allah" else "propn", ["huruf-jarr"] + list(tags),
               "اللَّامُ حَرْفُ جَرٍّ، وَ" + ("لَفْظُ الْجَلَالَةِ" if lex == "allah" else full[2:]) + " مَجْرُورٌ بِالْكَسْرَةِ" + extra + ".",
               en + " — the jarr lām on the noun (the article's alif is swallowed); in jarr.", tr + " — cer lâmı isme bitişik (harf-i tarifin elifi düşer); mecrur.",
               punct=punct, segments=[seg("لِ", "li", "prep"), seg(full[1:] if lex == "allah" else "ا" + full[2:], lex, "propn" if lex == "allah" else "noun")])
def li_nakira(full, lex, en, tr, punct=None):
    return tok(full, lex, "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَ" + full[2:] + " مَجْرُورٌ بِالْكَسْرَةِ.", en + " — the jarr lām on an indefinite noun; in jarr.", tr + " — cer lâmı nekre isimde; mecrur.",
               punct=punct, segments=[seg("لِ", "li", "prep"), seg(full[2:], lex, "noun")])
def khamsa_obj(full, lex, verb_part, pron, pron_lex, en, tr, punct=None, tags=(), wa=False, extra=""):
    """يَسْمَعُونَكُمْ، يَنْفَعُونَكُمْ — one of the five verbs with its object pronoun."""
    return tok(full, lex, "verb", ["afal-khamsa", "mudari-marfu", "maful-bihi"] + list(tags), W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَ" + pron + " ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + extra + ".",
               Wen(wa) + en + " — one of the five verbs, rafʿ by the retained nūn; the wāw is the doer and the attached pronoun its object.", Wtr(wa) + tr + " — ef'âl-i hamseden, nûnun sübûtuyla merfû; vâv fâil, bitişik zamir mef'ûl.",
               punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(verb_part, lex, "verb"), seg(pron, pron_lex, "pron")])
def ni_verb(full, lex, verb_part, en, tr, ar_head, tags=(), punct=None, wa=False, sila=True):
    """خَلَقَنِي، يُطْعِمُنِي، يُمِيتُنِي — the verb reaching the speaker's yāʾ through the nūn of protection."""
    return tok(full, lex, "verb", ["ya-al-mutakallim", "maful-bihi"] + list(tags), W(wa) + ar_head + "، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا" if sila else "") + ".",
               Wen(wa) + en + " — the nūn of protection stands between the verb and the speaker's yāʾ, which is its object" + ("; the clause is the relative's ṣila" if sila else "") + ".",
               Wtr(wa) + tr + " — fiil ile mütekellim yâsı arasında vikâye nûnu; yâ mef'ûl" + ("; cümle sıla cümlesidir" if sila else "") + ".",
               punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(verb_part, lex, "verb"), seg("نِي", "pron-1s", "pron")])
def ni_trimmed(full, lex, en, tr, punct=None, wa=False, khabar="هُوَ"):
    """يَهْدِينِ، يَسْقِينِ، يَشْفِينِ، يُحْيِينِ — the nūn of protection kept, the speaker's yāʾ dropped at the verse end."""
    return tok(full, lex, "verb", ["ya-al-mutakallim", "mudari-marfu", "naqis-verbs", "maful-bihi"], W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ مَحْذُوفَةٌ لِلْفَاصِلَةِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + (f" — وَالْجُمْلَةُ خَبَرُ {khabar}" if khabar else "") + ".",
               Wen(wa) + en + " — a nāqiṣ muḍāriʿ, rafʿ by an estimated ḍamma on the yāʾ; the nūn of protection stays and the speaker's yāʾ is dropped at the verse end (its object)" + (" — the clause is the khabar" if khabar else "") + ".",
               Wtr(wa) + tr + " — nâkıs muzâri, yâ üzerinde takdîrî damme ile merfû; vikâye nûnu kalır, mütekellim yâsı âyet sonunda düşer (mef'ûl)" + (" — cümle haberdir" if khabar else "") + ".",
               punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(full[1:] if wa else full, lex, "verb")])
def alladhi(full="الَّذِي", ar="", en="", tr="", wa=False, punct=None, tags=()):
    full = conj_full(full, wa)
    return tok(full, "alladhi", "pron", ["ism-mawsul"] + list(tags), W(wa) + "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ " + ar + ".", Wen(wa) + "«the One who» — a relative noun, built on sukūn; " + en + ".", Wtr(wa) + "«o ki» — ism-i mevsûl, sükûn üzere mebnî; " + tr + ".",
               punct=punct, segments=([seg("وَ", "wa", "conj"), seg("الَّذِي", "alladhi", "pron")] if wa else None))
def fa_pron(full, lex, pron, en, tr, ar_fa, punct=None):
    return tok(full, lex, "pron", ["mubtada-khabar"], ar_fa + "، وَ" + pron + " ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", en + " — the detached pronoun is the mubtadaʾ.", tr + " — munfasıl zamir, mübtedâ.",
               punct=punct, segments=[seg("فَ", "fa", "conj"), seg(pron, lex, "pron")])
def ana_mubtada(full="أَنَا", punct=None, extra=""):
    return tok(full, "pron-1s-munfasil", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ" + extra + ".", "«I» — the detached pronoun, the mubtadaʾ.", "«ben» — munfasıl zamir, mübtedâ.", punct=punct)
def mudari_ana(full, lex, en, tr, tags=(), punct=None, wa=False, extra="", khabar=True):
    return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنَا" + extra + (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ" if khabar else "") + ".",
               Wen(wa) + en + " — a muḍāriʿ in rafʿ; the doer «I» is concealed by necessity" + ("; the clause is the khabar" if khabar else "") + ".", Wtr(wa) + tr + " — merfû muzâri; fâil vücûben gizli «ben»" + ("; cümle haberdir" if khabar else "") + ".", punct=punct)
def ahad_maful(full="أَحَدًا", punct=None): return maful(full, "ahad", "«anyone»", "«hiç kimseyi»", punct=punct)
def neg_she(full, lex, en, tr, tags=(), punct=None, wa=False, extra="", muq=False):
    """لَا تَخْلُقُ، وَلَا تَهْدِي — the negated she-verb whose doer is the idols."""
    return tok(full, lex, "verb", ["la-nafiya", "mudari-marfu"] + list(tags), ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ" if muq else "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ") + " بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ" + extra + ".",
               en + " — rafʿ after the negating lā" + (" (an estimated ḍamma on the yāʾ)" if muq else "") + "; the doer «it/they (f.)» is concealed.", tr + " — nefiy lâ'sından sonra merfû" + (" (yâ üzerinde takdîrî damme)" if muq else "") + "; fâil gizli «o (dişil)».", punct=punct)
def wa_la(punct=None): return la_nafiya("وَلَا", wa=True, punct=punct)
def malik_mudaf_li(punct=None): return li_al("لِلْمَلِكِ", "malik-king", "«to the king»", "«krala»", punct=punct)
def mazi_tu(full, lex, en, tr, tags=(), punct=None, wa=False):
    return tok(full, lex, "verb", list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", Wen(wa) + en + " — a māḍī built on sukūn before the doer's tāʾ; the tāʾ «I» is the doer.", Wtr(wa) + tr + " — fâil tâsından önce sükûn üzere mebnî mâzî; tâ fâildir.",
               punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(full[2:-2] if wa else full[:-2], lex, "verb"), seg("تُ", "pron-1s", "pron")])
def rajulan(punct=None, wa=False): return maful("رَجُلًا", "rajul", "«a man»", "«bir adam»", punct=punct)

# ================================================================ §9 دعوة إبراهيم (pp. 15–17)
sen("s1", "And Ibrāhīm called his people to Allah and kept them from worshipping the idols.", "Ve İbrâhim kavmini Allah'a davet etti ve onları putlara tapmaktan menetti.", [
  tok("وَدَعَا", "daa", "verb", ["naqis-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَدَعَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«and called» — a nāqiṣ māḍī built on an estimated fatḥa on the alif.", "«ve davet etti» — elif üzerinde takdîrî fetha ile mebnî nâkıs mâzî.", segments=[seg("وَ", "wa", "conj"), seg("دَعَا", "daa", "verb")]),
  ibrahim_fail(),
  tok("قَوْمَهُ", "qawm", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people» — the object; annexed to the pronoun.", "«kavmini» — mef'ûl; zamire muzâf.", segments=[seg("قَوْمَ", "qawm", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("اللهِ", "allah", "propn", ["huruf-jarr"], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«Allah» — in jarr after إِلَى.", "«Allah'a» — ilâ ile mecrur."),
  tok("وَمَنَعَهُمْ", "manaa", "verb", ["atf-nasaq", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَمَنَعَ فِعْلٌ مَاضٍ مَعْطُوفٌ عَلَى دَعَا، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«and kept them» — joined to «called»; the doer is concealed, the pronoun is its object.", "«ve onları menetti» — «davet etti»ye atıf; fâil gizli, zamir mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("مَنَعَ", "manaa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("عِبَادَةِ", "ibada", "noun", ["huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ بِمِنْ، وَهُوَ مُضَافٌ — مَصْدَرُ عَبَدَ.", "«worshipping» — in jarr, and a muḍāf (the maṣdar of عَبَدَ).", "«tapmak(tan)» — mecrur ve muzâf (abede'nin masdarı)."),
  tok("الْأَصْنَامِ", "sanam", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the idols» — the annexed noun, in jarr.", "«putlara» — muzâfun ileyh, mecrur.", punct=".")])
sen("s2", "Ibrāhīm said to his people: What do you worship?", "İbrâhim kavmine dedi: Neye tapıyorsunuz?", [
  qala(punct=None), ibrahim_fail(),
  tok("لِقَوْمِهِ", "qawm", "noun", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَقَوْمِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his people» — the jarr lām; the noun is annexed to the pronoun.", "«kavmine» — cer lâmı; isim zamire muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("قَوْمِ", "qawm", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("مَا", "ma-istifham", "pron", ["al-istifham", "maful-bihi"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«what?» — an interrogative noun, built; the fronted object.", "«ne?» — istifhâm ismi, mebnî; öne alınmış mef'ûl."),
  khamsa("تَعْبُدُونَ", "abada", "«do you worship»", "«tapıyorsunuz»", punct="؟")])
sen("s3", "«They said: We worship idols.» (al-Shuʿarāʾ 26:71)", "«Dediler: Putlara tapıyoruz.» (Şuarâ 26:71)", quran([
  qalu(punct=None),
  tok("نَعْبُدُ", "abada", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: نَحْنُ.", "«we worship» — a muḍāriʿ in rafʿ; the doer «we» is concealed by necessity.", "«tapıyoruz» — merfû muzâri; fâil vücûben gizli «biz»."),
  maful("أَصْنَامًا", "sanam", "«idols»", "«putlara»", tags=["jam-taksir"], punct=".")]))
sen("s4", "Ibrāhīm said: «Do they hear you when you call?» (26:72)", "İbrâhim dedi: «Çağırdığınızda sizi duyuyorlar mı?» (26:72)", [
  qala(punct=None), ibrahim_fail(punct=":")] + quran([
  tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«…?» — the yes/no question particle.", "«mı?» — istifhâm harfi."),
  khamsa_obj("يَسْمَعُونَكُمْ", "samia", "يَسْمَعُونَ", "كُمْ", "pron-2mp", "«do they hear you»", "«sizi duyuyorlar»"),
  tok("إِذْ", "idh", "noun", ["maful-fih"], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ فِيهِ.", "«when» — a mabnī adverb of past time, in the place of naṣb.", "«-dığında» — geçmiş zaman zarfı, mebnî, mahallen mansub."),
  khamsa("تَدْعُونَ", "daa", "«you call»", "«çağırıyorsunuz»", tags=["naqis-verbs"], punct=".", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ إِلَيْهَا")]))
sen("s5", "«Or do they benefit you, or harm?» (26:73)", "«Yahut size fayda veriyorlar mı, ya da zarar?» (26:73)", quran([
  tok("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or» — a joining particle.", "«yahut» — atıf harfi."),
  khamsa_obj("يَنْفَعُونَكُمْ", "nafaa", "يَنْفَعُونَ", "كُمْ", "pron-2mp", "«do they benefit you»", "«size fayda veriyorlar»", tags=["atf-nasaq"], extra=" — مَعْطُوفٌ عَلَى يَسْمَعُونَكُمْ"),
  tok("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  khamsa("يَضُرُّونَ", "darra", "«do they harm»", "«zarar veriyorlar»", tags=["atf-nasaq", "doubled-verbs"], punct=".", extra_ar=" — مَعْطُوفٌ، وَالْمَفْعُولُ مَحْذُوفٌ: يَضُرُّونَكُمْ")]))
sen("s6", "«They said: Rather, we found our fathers doing so.» (26:74)", "«Dediler: Hayır, biz atalarımızı böyle yapar bulduk.» (26:74)", quran([
  qalu(punct=None),
  tok("بَلْ", "bal", "part", ["atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«rather» — the particle of turning away (iḍrāb).", "«bilakis» — idrâb harfi."),
  tok("وَجَدْنَا", "wajada", "verb", ["mafulayn", "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا ضَمِيرٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَوَجَدَ يَنْصِبُ مَفْعُولَيْنِ.", "«we found» — a māḍī built on sukūn before «we»; the pronoun is the doer, and «find» takes two objects.", "«bulduk» — «biz» zamirinden önce sükûn üzere mebnî mâzî; zamir fâil; «bulmak» iki mef'ûl alır.", segments=[seg("وَجَدْ", "wajada", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("آبَاءَنَا", "ab", "noun", ["maful-bihi", "idafa-definiteness", "jam-taksir"], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our fathers» — the first object; annexed to «our».", "«atalarımızı» — birinci mef'ûl; «biz» zamirine muzâf.", segments=[seg("آبَاءَ", "ab", "noun"), seg("نَا", "pron-1p", "pron")]),
  tok("كَذٰلِكَ", "kadhalika", "pron", ["mafulayn", "asma-al-ishara", "huruf-jarr"], "الْكَافُ حَرْفُ جَرٍّ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ لِوَجَدَ.", "«so, thus» — the kāf on the demonstrative; the phrase stands as the second object of «find».", "«böyle» — ism-i işâret üzerinde kâf; terkip «bulmak»ın ikinci mef'ûlü yerinde.", segments=[seg("كَ", "ka", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  khamsa("يَفْعَلُونَ", "faala", "«doing»", "«yapar(lar)»", tags=["hal"], punct=".", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ")]))
sen("s7", "Ibrāhīm said: As for me, I do not worship these idols.", "İbrâhim dedi: Bana gelince, ben bu putlara tapmam.", [
  qala(punct=None), ibrahim_fail(punct=":"),
  fa_pron("فَأَنَا", "pron-1s-munfasil", "أَنَا", "«so I»", "«ben ise»", "الْفَاءُ لِلِاسْتِئْنَافِ"),
  la_nafiya(), mudari_ana("أَعْبُدُ", "abada", "«worship»", "«taparım»", tags=["la-nafiya"]),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«these»", "«bu»"),
  tok("الْأَصْنَامَ", "sanam", "noun", ["badal", "jam-taksir"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) مَنْصُوبٌ بِالْفَتْحَةِ.", "«idols» — the badal of the demonstrative, in naṣb.", "«putlara» — ism-i işâretten bedel, mansub.", punct=".")])
sen("s8", "Rather, I am an enemy to these idols.", "Bilakis ben bu putlara düşmanım.", [
  tok("بَلْ", "bal", "part", ["atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«rather» — iḍrāb.", "«bilakis» — idrâb harfi."),
  ana_mubtada(),
  tok("عَدُوٌّ", "aduww", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«an enemy» — the khabar, in rafʿ.", "«düşman» — haber, merfû."),
  tok("لِهٰذِهِ", "hadhihi", "pron", ["huruf-jarr", "asma-al-ishara"], "اللَّامُ حَرْفُ جَرٍّ، وَهٰذِهِ اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِعَدُوٍّ.", "«to these» — the jarr lām on the demonstrative; it hangs on «enemy».", "«bu …-a» — ism-i işâret üzerinde cer lâmı; «düşman»a müteallik.", segments=[seg("لِ", "li", "prep"), seg("هٰذِهِ", "hadhihi", "pron")]),
  tok("الْأَصْنَامِ", "sanam", "noun", ["badal", "jam-taksir"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«idols» — the badal, in jarr.", "«putlara» — bedel, mecrur.", punct=".")])
sen("s9", "I worship the Lord of the worlds,", "Ben âlemlerin Rabbine taparım,", [
  ana_mubtada(), mudari_ana("أَعْبُدُ", "abada", "«worship»", "«taparım»"),
  tok("رَبَّ", "rabb", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the Lord» — the object, a muḍāf.", "«Rabbine» — mef'ûl, muzâf."),
  tok("الْعَالَمِينَ", "alam", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«of the worlds» — the annexed noun, jarr by the yāʾ (attached to the sound masculine plural).", "«âlemlerin» — muzâfun ileyh, yâ ile mecrur (cem-i müzekker sâlime mülhak).", punct="،")])
sen("s10", "«Who created me, and so guides me,» (26:78)", "«O ki beni yarattı; bana O hidâyet eder,» (26:78)", quran([
  alladhi(ar="فِي مَحَلِّ نَصْبٍ صِفَةٌ لِرَبِّ الْعَالَمِينَ (أَوْ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: هُوَ)", en="a ṣifa of «the Lord of the worlds» (or the khabar of a dropped «He»)", tr="«âlemlerin Rabbi»nin sıfatı (yahut hazfedilmiş «O»nun haberi)"),
  ni_verb("خَلَقَنِي", "khalaqa", "خَلَقَ", "«created me»", "«beni yarattı»", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ"),
  fa_pron("فَهُوَ", "pron-3ms-munfasil", "هُوَ", "«so He»", "«O»", "الْفَاءُ زَائِدَةٌ لِتَضَمُّنِ الْمَوْصُولِ مَعْنَى الشَّرْطِ (أَوْ عَاطِفَةٌ)"),
  ni_trimmed("يَهْدِينِ", "hada", "«guides me»", "«bana hidâyet eder»", punct="،")]))
sen("s11", "«And who feeds me and gives me drink,» (26:79)", "«Ve O ki beni doyurur ve içirir,» (26:79)", quran([
  alladhi(wa=True, ar="فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى الَّذِي قَبْلَهُ", en="joined to the relative before it", tr="önceki mevsûle atıf", tags=["atf-nasaq"]),
  tok("هُوَ", "pron-3ms-munfasil", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ جُمْلَةُ يُطْعِمُنِي — وَالْجُمْلَةُ صِلَةٌ.", "«He» — the mubtadaʾ; its khabar is «feeds me», and the whole is the ṣila.", "«O» — mübtedâ; haberi «beni doyurur»; bütünü sıla."),
  ni_verb("يُطْعِمُنِي", "atama", "يُطْعِمُ", "«feeds me»", "«beni doyurur»", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ", tags=["form-iv-verbs", "mudari-marfu"], sila=False),
  ni_trimmed("وَيَسْقِينِ", "saqa-water", "«and gives me drink»", "«ve beni içirir»", wa=True, punct="،", khabar=None)]))
sen("s12", "«And when I fall ill, it is He who heals me,» (26:80)", "«Ve hastalandığımda bana şifa veren O'dur,» (26:80)", quran([
  tok("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", "«and when» — the conditional time-adverb idhā, built, in the place of naṣb.", "«ve …-dığında» — şart manası taşıyan zaman zarfı izâ, mebnî, mahallen mansub.", segments=[seg("وَ", "wa", "conj"), seg("إِذَا", "idha", "part")]),
  tok("مَرِضْتُ", "marida", "verb", ["idha-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — فِعْلُ الشَّرْطِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا.", "«I fall ill» — the condition's verb; the tāʾ «I» is the doer; the clause is annexed to idhā.", "«hastalandım» — şart fiili; tâ fâil; cümle izâ'ya muzâfun ileyh.", segments=[seg("مَرِضْ", "marida", "verb"), seg("تُ", "pron-1s", "pron")]),
  fa_pron("فَهُوَ", "pron-3ms-munfasil", "هُوَ", "«then He»", "«O»", "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا"),
  ni_trimmed("يَشْفِينِ", "shafa", "«heals me»", "«bana şifa verir»", punct="،")]))
sen("s13", "«And who will make me die, then bring me to life.» (26:81)", "«Ve O ki beni öldürecek, sonra diriltecek.» (26:81)", quran([
  alladhi(wa=True, ar="فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى الَّذِي خَلَقَنِي", en="joined to «who created me»", tr="«beni yaratan»a atıf", tags=["atf-nasaq"]),
  ni_verb("يُمِيتُنِي", "amata", "يُمِيتُ", "«makes me die»", "«beni öldürür»", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ", tags=["form-iv-verbs", "hollow-verbs", "mudari-marfu"]),
  tok("ثُمَّ", "thumma", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "«then» — a joining particle: in order, after an interval.", "«sonra» — tertip ve terâhî için atıf harfi."),
  ni_trimmed("يُحْيِينِ", "ahya", "«brings me to life»", "«beni diriltir»", punct=".", khabar=None)]))
sen("s14", "And the idols do not create and do not guide.", "Ve putlar ne yaratır ne hidâyet eder.", [
  inna("وَإِنَّ", wa=True), ism_inna("الْأَصْنَامَ", "sanam", "«the idols»", "«putlar»", tags=["jam-taksir"]),
  la_nafiya(), neg_she("تَخْلُقُ", "khalaqa", "«create»", "«yaratır»", extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  wa_la(), neg_she("تَهْدِي", "hada", "«guide»", "«hidâyet eder»", tags=["naqis-verbs", "atf-nasaq"], muq=True, punct=".")])
sen("s15", "And they do not feed anyone and do not give drink.", "Ve kimseyi doyurmaz, içirmez.", [
  tok("وَإِنَّهَا", "inna", "part", ["inna-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«and they (the idols)» — inna with its attached pronoun as its ism.", "«ve onlar» — inne, bitişik zamir ismi.", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), seg("هَا", "pron-3fs", "pron")]),
  la_nafiya(), neg_she("تُطْعِمُ", "atama", "«feed»", "«doyurur»", tags=["form-iv-verbs"], extra=" — وَالْجُمْلَةُ خَبَرُ إِنَّ"),
  ahad_maful(),
  wa_la(), neg_she("تَسْقِي", "saqa-water", "«give drink»", "«içirir»", tags=["naqis-verbs", "atf-nasaq"], muq=True, punct=".")])
sen("s16", "And when anyone falls ill, they do not heal.", "Ve biri hastalanınca onlar şifa vermez.", [
  tok("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the conditional time-adverb.", "«ve …-ınca» — şart manalı zaman zarfı.", segments=[seg("وَ", "wa", "conj"), seg("إِذَا", "idha", "part")]),
  mazi("مَرِضَ", "marida", "«falls ill»", "«hastalanır»", hidden=None, extra_ar=" — فِعْلُ الشَّرْطِ"),
  fail("أَحَدٌ", "ahad", "«anyone»", "«biri»"),
  fa_pron("فَهِيَ", "pron-3fs-munfasil", "هِيَ", "«then they»", "«onlar»", "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا"),
  la_nafiya(), neg_she("تَشْفِي", "shafa", "«heal»", "«şifa verir»", tags=["naqis-verbs"], muq=True, punct=".", extra=" — وَالْجُمْلَةُ خَبَرُ هِيَ")])
sen("s17", "And they do not make anyone die and do not bring to life.", "Ve kimseyi öldürmez, diriltmez.", [
  tok("وَإِنَّهَا", "inna", "part", ["inna-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهَا.", "«and they» — inna with its pronoun ism.", "«ve onlar» — inne, zamir ismi.", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), seg("هَا", "pron-3fs", "pron")]),
  la_nafiya(), neg_she("تُمِيتُ", "amata", "«make die»", "«öldürür»", tags=["form-iv-verbs", "hollow-verbs"], extra=" — وَالْجُمْلَةُ خَبَرُ إِنَّ"),
  ahad_maful(),
  wa_la(), neg_she("تُحْيِي", "ahya", "«bring to life»", "«diriltir»", tags=["naqis-verbs", "form-iv-verbs", "atf-nasaq"], muq=True, punct=".")])

# ================================================================ §10 أمام الملك (pp. 17–18)
sen("s18", "There was in the city a very great king, and a very unjust one.", "Şehirde çok büyük bir kral vardı; çok da zâlimdi.", [
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", "«there was» — kāna.", "«vardı» — kâne."),
  tok("فِي", "fi", "prep", ["huruf-jarr", K], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْمَدِينَةِ", "madina", "noun", ["huruf-jarr", K], "مَجْرُورٌ بِفِي، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«the city» — in jarr; the phrase is kāna's khabar, fronted.", "«şehirde» — mecrur; terkip kâne'nin öne alınmış haberi."),
  tok("مَلِكٌ", "malik-king", "noun", [K], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a king» — kāna's ism, delayed, in rafʿ.", "«bir kral» — kâne'nin te'hir edilmiş ismi, merfû."),
  tok("كَبِيرٌ", "kabir", "noun", ["naat-sifa", "sifa-mushabbaha"], "نَعْتٌ لِمَلِكٍ مَرْفُوعٌ بِالضَّمَّةِ.", "«great» — the naʿt of «king», in rafʿ.", "«büyük» — «kral»ın sıfatı, merfû."),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ.", "«very» — standing in for the absolute object (an adjective of a dropped maṣdar).", "«çok» — mef'ûl-i mutlak nâibi (hazfedilmiş masdarın sıfatı).", punct="،"),
  tok("وَظَالِمٌ", "zalim", "noun", ["atf-nasaq", "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَظَالِمٌ مَعْطُوفٌ عَلَى كَبِيرٍ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ فَاعِلٍ.", "«and unjust» — joined to «great»; an active participle.", "«ve zâlim» — «büyük»e atıf; ism-i fâil.", segments=[seg("وَ", "wa", "conj"), seg("ظَالِمٌ", "zalim", "noun")]),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ.", "«very» — standing in for the absolute object.", "«çok» — mef'ûl-i mutlak nâibi.", punct=".")])
sen("s19", "And the people used to prostrate to the king.", "Ve insanlar krala secde ederlerdi.", [
  kana(), tok("النَّاسُ", "nas", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the people» — kāna's ism.", "«insanlar» — kâne'nin ismi."),
  khamsa("يَسْجُدُونَ", "sajada", "«prostrate»", "«secde ederler»", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  malik_mudaf_li(punct=".")])
sen("s20", "And the king heard that Ibrāhīm prostrates to Allah and prostrates to no one.", "Ve kral, İbrâhim'in Allah'a secde ettiğini ve kimseye secde etmediğini duydu.", [
  mazi("وَسَمِعَ", "samia", "«heard»", "«duydu»", hidden=None, wa=True), malik_fail(),
  anna(obj_of="سَمِعَ"), tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — the ism of anna; a diptote.", "«İbrâhim» — enne'nin ismi; gayr-ı munsarif."),
  mudari("يَسْجُدُ", "sajada", "«prostrates»", "«secde eder»", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ"),
  li_al("لِلّٰهِ", "allah", "«to Allah»", "«Allah'a»"),
  wa_la(), neg_mudari("يَسْجُدُ", "sajada", "«prostrates»", "«secde eder»", hidden="هُوَ", tags=["atf-nasaq"]),
  li_nakira("لِأَحَدٍ", "ahad", "«to anyone»", "«kimseye»", punct=".")])
sen("s21", "So the king grew angry and summoned Ibrāhīm.", "Bunun üzerine kral öfkelendi ve İbrâhim'i çağırttı.", [
  tok("فَغَضِبَ", "ghadiba", "verb", [], "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَغَضِبَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«so … grew angry» — the fāʾ of immediate sequence; a māḍī.", "«bunun üzerine öfkelendi» — ta'kîb fâ'sı; mâzî.", segments=[seg("فَ", "fa", "conj"), seg("غَضِبَ", "ghadiba", "verb")]),
  malik_fail(),
  mazi("وَطَلَبَ", "talaba", "«and summoned»", "«ve çağırttı»", hidden="هُوَ", wa=True, tags=["atf-nasaq"]),
  ibrahim_maful(punct=".")])
sen("s22", "And Ibrāhīm came — and Ibrāhīm feared no one but Allah.", "Ve İbrâhim geldi — İbrâhim Allah'tan başka kimseden korkmazdı.", [
  mazi("وَجَاءَ", "jaa", "«came»", "«geldi»", hidden=None, wa=True, tags=["hollow-verbs"]), ibrahim_fail(punct="،"),
  kana(), tok("إِبْرَاهِيمُ", "ibrahim", "propn", [K, "mamnu-min-sarf"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ.", "«Ibrāhīm» — kāna's ism.", "«İbrâhim» — kâne'nin ismi."),
  la_nafiya(), neg_mudari("يَخَافُ", "khafa", "«fears»", "«korkar»", hidden="هُوَ", tags=["hollow-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  ahad_maful(),
  tok("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except» — the particle of exception.", "«başka» — istisnâ edatı."),
  tok("اللهَ", "allah", "propn", ["istithna"], "لَفْظُ الْجَلَالَةِ مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ — وَيَجُوزُ الْبَدَلُ مِنْ أَحَدًا لِأَنَّ الْكَلَامَ مَنْفِيٌّ تَامٌّ.", "«Allah» — the excepted noun, in naṣb; a badal of «anyone» is also allowed, since the clause is negated and complete.", "«Allah» — müstesnâ, mansub; cümle menfî ve tam olduğundan «kimse»den bedel de câizdir.", punct=".")])
sen("s23", "The king said: Who is your Lord, O Ibrāhīm?", "Kral dedi: Rabbin kim, ey İbrâhim?", [
  qala(punct=None), malik_fail(punct=":"),
  tok("مَنْ", "man-istifham", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«who?» — an interrogative noun, built; the mubtadaʾ.", "«kim?» — istifhâm ismi, mebnî; mübtedâ."),
  tok("رَبُّكَ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your Lord» — the khabar; annexed to «your».", "«Rabbin» — haber; «sen» zamirine muzâf.", segments=[seg("رَبُّ", "rabb", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
  tok("إِبْرَاهِيمُ", "ibrahim", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Ibrāhīm» — a single proper-name munādā, built on ḍamma in the place of naṣb.", "«İbrâhim» — müfred alem münâdâ, damme üzere mebnî, mahallen mansub.", punct="؟")])
sen("s24", "Ibrāhīm said: My Lord is Allah!", "İbrâhim dedi: Rabbim Allah'tır!", [
  qala(punct=None), ibrahim_fail(punct=":"),
  tok("رَبِّيَ", "rabb", "noun", ["mubtada-khabar", "ya-al-mutakallim", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — وَفُتِحَتِ الْيَاءُ هُنَا كَمَا فِي الطَّبْعَةِ.", "«my Lord» — the mubtadaʾ, rafʿ by an estimated ḍamma before the speaker's yāʾ (its muḍāf ilayh); the yāʾ carries a fatḥa here as the print has it.", "«Rabbim» — mübtedâ, mütekellim yâsından önce takdîrî damme ile merfû; yâ muzâfun ileyh — baskıdaki gibi fethalı.", segments=[seg("رَبِّ", "rabb", "noun"), seg("يَ", "pron-1s", "pron")]),
  tok("اللهُ", "allah", "propn", ["mubtada-khabar"], "لَفْظُ الْجَلَالَةِ خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Allah» — the khabar, in rafʿ.", "«Allah» — haber, merfû.", punct="!")])
sen("s25", "The king said: Who is Allah, O Ibrāhīm?", "Kral dedi: Allah kim, ey İbrâhim?", [
  qala(punct=None), malik_fail(punct=":"),
  tok("مَنِ", "man-istifham", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَكُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«who?» — the interrogative mubtadaʾ; its sukūn turns to kasra before the article's silent alif.", "«kim?» — istifhâm ismi, mübtedâ; iki sâkin karşılaştığı için kesre aldı."),
  tok("اللهُ", "allah", "propn", ["mubtada-khabar"], "لَفْظُ الْجَلَالَةِ خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Allah» — the khabar.", "«Allah» — haber."),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O».", "«ey»."),
  tok("إِبْرَاهِيمُ", "ibrahim", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Ibrāhīm» — the munādā, built on ḍamma.", "«İbrâhim» — münâdâ, damme üzere mebnî.", punct="؟")])
sen("s26", "Ibrāhīm said: «The One who gives life and causes death.» (al-Baqara 2:258)", "İbrâhim dedi: «O ki diriltir ve öldürür.» (Bakara 2:258)", [
  qala(punct=None), ibrahim_fail(punct=":")] + quran([
  alladhi(ar="فِي مَحَلِّ رَفْعٍ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: رَبِّيَ الَّذِي", en="the khabar of a dropped mubtadaʾ («my Lord is the One who…»)", tr="hazfedilmiş mübtedânın haberi («Rabbim O ki…»)"),
  tok("يُحْيِي", "ahya", "verb", ["mudari-marfu", "naqis-verbs", "form-iv-verbs", "ism-mawsul"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«gives life» — rafʿ by an estimated ḍamma on the yāʾ; the clause is the ṣila.", "«diriltir» — yâ üzerinde takdîrî damme ile merfû; cümle sıladır."),
  mudari("وَيُمِيتُ", "amata", "«and causes death»", "«ve öldürür»", tags=["atf-nasaq", "form-iv-verbs", "hollow-verbs"], punct=".", extra_ar=" — مَعْطُوفٌ عَلَى يُحْيِي")]))
S[-1]["tokens"][-1]["irab"]["ar"] = "الْوَاوُ عَاطِفَةٌ، وَيُمِيتُ " + S[-1]["tokens"][-1]["irab"]["ar"]
sen("s27", "The king said: «I give life and cause death.» (2:258)", "Kral dedi: «Ben de diriltir ve öldürürüm.» (2:258)", [
  qala(punct=None), malik_fail(punct=":")] + quran([
  ana_mubtada(),
  mudari_ana("أُحْيِي", "ahya", "«give life»", "«diriltirim»", tags=["naqis-verbs", "form-iv-verbs"], extra="، وَالضَّمَّةُ مُقَدَّرَةٌ عَلَى الْيَاءِ"),
  mudari_ana("وَأُمِيتُ", "amata", "«and cause death»", "«ve öldürürüm»", tags=["atf-nasaq", "form-iv-verbs", "hollow-verbs"], wa=True, punct=".", khabar=False)]))
sen("s28", "And the king summoned a man and killed him.", "Ve kral bir adam çağırdı ve onu öldürdü.", [
  tok("وَدَعَا", "daa", "verb", ["naqis-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَدَعَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«and summoned» — a nāqiṣ māḍī, fatḥa estimated on the alif.", "«ve çağırdı» — elif üzerinde takdîrî fetha ile mebnî nâkıs mâzî.", segments=[seg("وَ", "wa", "conj"), seg("دَعَا", "daa", "verb")]),
  malik_fail(), rajulan(),
  tok("وَقَتَلَهُ", "qatala", "verb", ["atf-nasaq", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَقَتَلَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«and killed him» — joined; the doer concealed, the pronoun its object.", "«ve onu öldürdü» — atıf; fâil gizli, zamir mef'ûl.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("قَتَلَ", "qatala", "verb"), seg("هُ", "pron-3ms", "pron")])])
sen("s29", "And he summoned another man and let him go.", "Ve başka bir adam çağırdı ve onu bıraktı.", [
  tok("وَدَعَا", "daa", "verb", ["naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَدَعَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and summoned» — the doer «he» (the king) is concealed.", "«ve çağırdı» — fâil gizli «o» (kral).", segments=[seg("وَ", "wa", "conj"), seg("دَعَا", "daa", "verb")]),
  rajulan(),
  tok("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "نَعْتٌ لِرَجُلًا مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ فَلَا يُنَوَّنُ.", "«another» — the naʿt of «a man», in naṣb; a diptote, so no tanwīn.", "«başka» — «bir adam»ın sıfatı, mansub; gayr-ı munsarif, tenvin almaz."),
  tok("وَتَرَكَهُ", "taraka", "verb", ["atf-nasaq", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَتَرَكَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and let him go» — joined; the pronoun is the object.", "«ve onu bıraktı» — atıf; zamir mef'ûl.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("تَرَكَ", "taraka", "verb"), seg("هُ", "pron-3ms", "pron")])])
sen("s30", "And he said: I give life and cause death; I killed a man and I let a man go.", "Ve dedi: Ben diriltir ve öldürürüm; bir adamı öldürdüm, bir adamı bıraktım.", [
  qala("وَقَالَ", wa=True, hidden="هُوَ"),
  ana_mubtada(),
  mudari_ana("أُحْيِي", "ahya", "«give life»", "«diriltirim»", tags=["naqis-verbs", "form-iv-verbs"], extra="، وَالضَّمَّةُ مُقَدَّرَةٌ عَلَى الْيَاءِ"),
  mudari_ana("وَأُمِيتُ", "amata", "«and cause death»", "«ve öldürürüm»", tags=["atf-nasaq", "form-iv-verbs", "hollow-verbs"], wa=True, punct="،", khabar=False),
  mazi_tu("قَتَلْتُ", "qatala", "«I killed»", "«öldürdüm»"), rajulan(),
  mazi_tu("وَتَرَكْتُ", "taraka", "«and I let go»", "«ve bıraktım»", wa=True, tags=["atf-nasaq"]), rajulan(punct=".")])
sen("s31", "And the king was very dull — and so is every idolater.", "Ve kral çok kalın kafalıydı — her müşrik de öyledir.", [
  kana(), tok("الْمَلِكُ", "malik-king", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the king» — kāna's ism.", "«kral» — kâne'nin ismi."),
  tok("بَلِيدًا", "balid", "noun", [K, "sifa-mushabbaha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ مُشَبَّهَةٌ.", "«dull» — kāna's khabar, in naṣb.", "«kalın kafalı» — kâne'nin haberi, mansub."),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ.", "«very» — standing in for the absolute object.", "«çok» — mef'ûl-i mutlak nâibi.", punct="،"),
  tok("وَكَذٰلِكَ", "kadhalika", "pron", ["mubtada-khabar", "asma-al-ishara", "huruf-jarr"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْكَافُ حَرْفُ جَرٍّ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«and likewise» — the kāf on the demonstrative; the phrase is the fronted khabar.", "«ve öyle(dir)» — ism-i işâret üzerinde kâf; terkip öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("كَ", "ka", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  tok("كُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«every» — the delayed mubtadaʾ, a muḍāf.", "«her» — te'hir edilmiş mübtedâ, muzâf."),
  tok("مُشْرِكٍ", "mushrik", "noun", ["idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ فَاعِلٍ مِنْ أَشْرَكَ.", "«idolater» — the annexed noun, in jarr; the active participle of أَشْرَكَ.", "«müşrik» — muzâfun ileyh, mecrur; eşreke'nin ism-i fâili.", punct=".")])
sen("s32", "And Ibrāhīm wanted the king to understand, and his people to understand.", "Ve İbrâhim kralın anlamasını ve kavminin anlamasını istedi.", [
  mazi("وَأَرَادَ", "arada", "«wanted»", "«istedi»", hidden=None, wa=True, tags=["form-iv-verbs", "hollow-verbs"]), ibrahim_fail(),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِأَرَادَ.", "«that» — the subjunctive maṣdar particle; the clause is the object of «wanted».", "«-mesini» — nasb eden masdariyye harfi; te'vilî masdar «istedi»nin mef'ûlü."),
  tok("يَفْهَمَ", "fahima", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«understand» — in naṣb after an.", "«anlasın» — en ile mansub."),
  malik_fail(punct="،"),
  tok("وَيَفْهَمَ", "fahima", "verb", ["atf-nasaq", "an-masdariyya"], "الْوَاوُ عَاطِفَةٌ، وَيَفْهَمَ مَعْطُوفٌ عَلَى يَفْهَمَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and … understand» — joined to the first, in naṣb.", "«ve anlasın» — ilkine atıf, mansub.", segments=[seg("وَ", "wa", "conj"), seg("يَفْهَمَ", "fahima", "verb")]),
  tok("قَوْمُهُ", "qawm", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people» — the doer; annexed to the pronoun.", "«kavmi» — fâil; zamire muzâf.", punct=".", segments=[seg("قَوْمُ", "qawm", "noun"), seg("هُ", "pron-3ms", "pron")])])
sen("s33", "So Ibrāhīm said to the king: «Allah brings the sun from the east, so bring it from the west!» (2:258)", "Bunun üzerine İbrâhim krala dedi: «Allah güneşi doğudan getirir, haydi sen onu batıdan getir!» (2:258)", [
  qala("فَقَالَ", punct=None, wa=True, hidden=None), ibrahim_fail(), malik_mudaf_li(punct=":")] + quran([
  tok("فَإِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ (أَوِ اسْتِئْنَافِيَّةٌ)، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«for indeed» — the fāʾ of reason, then inna.", "«zira şüphesiz» — ta'lil fâ'sı, sonra inne.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part")]),
  allah_ism(),
  tok("يَأْتِي", "ata", "verb", ["mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«brings» — rafʿ by an estimated ḍamma; the clause is inna's khabar.", "«getirir» — takdîrî damme ile merfû; cümle inne'nin haberi."),
  tok("بِالشَّمْسِ", "shams", "noun", ["huruf-jarr"], "الْبَاءُ لِلتَّعْدِيَةِ، وَالشَّمْسِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the sun» — the bāʾ of transitivity on the noun; in jarr.", "«güneşi» — ta'diye bâ'sı; mecrur.", segments=[seg("بِ", "bi", "prep"), seg("الشَّمْسِ", "shams", "noun")]),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَفُتِحَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from» — its nūn takes a fatḥa before the article.", "«-den» — iki sâkin karşılaştığı için fethalı."),
  tok("الْمَشْرِقِ", "mashriq", "noun", ["huruf-jarr"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the east» — in jarr.", "«doğu(dan)» — mecrur."),
  tok("فَأْتِ", "ata", "verb", ["imperative-amr", "naqis-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَأْتِ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«so bring» — an imperative built on the dropping of its weak letter; the doer «you» is concealed by necessity.", "«haydi getir» — illet harfinin hazfi üzere mebnî emir; fâil vücûben gizli «sen».", segments=[seg("فَ", "fa", "conj"), seg("أْتِ", "ata", "verb")]),
  tok("بِهَا", "bi", "prep", ["huruf-jarr"], "الْبَاءُ لِلتَّعْدِيَةِ، وَهَا ضَمِيرٌ فِي مَحَلِّ جَرٍّ.", "«it» — the bāʾ on the pronoun.", "«onu» — bâ zamir üzerinde.", segments=[seg("بِ", "bi", "prep"), seg("هَا", "pron-3fs", "pron")]),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الْمَغْرِبِ", "maghrib", "noun", ["huruf-jarr"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the west» — in jarr.", "«batı(dan)» — mecrur.", punct=".")]))
S[-1]["tokens"][0]["segments"] = [seg("فَ", "fa", "conj"), seg("قَالَ", "qala", "verb")]
S[-1]["tokens"][0]["irab"]["ar"] = S[-1]["tokens"][0]["irab"]["ar"].replace("الْوَاوُ عَاطِفَةٌ", "الْفَاءُ عَاطِفَةٌ")
sen("s34", "The king was bewildered and fell silent.", "Kral şaşırıp kaldı ve sustu.", [
  tok("فَتَحَيَّرَ", "tahayyara", "verb", ["form-v-verbs"], "الْفَاءُ عَاطِفَةٌ، وَتَحَيَّرَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«so … was bewildered» — the fāʾ of sequence; a Form V māḍī.", "«şaşırıp kaldı» — ta'kîb fâ'sı; V. bâb mâzî.", segments=[seg("فَ", "fa", "conj"), seg("تَحَيَّرَ", "tahayyara", "verb")]),
  malik_fail(),
  mazi("وَسَكَتَ", "sakata", "«and fell silent»", "«ve sustu»", hidden="هُوَ", wa=True, tags=["atf-nasaq"], punct=".")])
sen("s35", "And the king was ashamed, and found no answer.", "Ve kral utandı ve bir cevap bulamadı.", [
  mazi("وَخَجِلَ", "khajila", "«was ashamed»", "«utandı»", hidden=None, wa=True), malik_fail(punct="،"),
  tok("وَمَا", "ma-nafiya", "part", ["anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«and … not» — the negating mā, no government.", "«ve …-madı» — nefiy mâ'sı, amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  mazi("وَجَدَ", "wajada", "«found»", "«buldu»", hidden="هُوَ", tags=["mithal-verbs"]),
  maful("جَوَابًا", "jawab", "«an answer»", "«bir cevap»", punct=".")])

# ---------------------------------------------------------------- glossary
NEW = {
 "balid": G("balid", "بَلِيد", "ب ل د", "noun", "dull, slow-witted", "kalın kafalı, ahmak", 2),
 "mushrik": G("mushrik", "مُشْرِك", "ش ر ك", "noun", "idolater, one who associates partners with Allah (ism fāʿil of أَشْرَكَ)", "müşrik, Allah'a ortak koşan (eşreke'nin ism-i fâili)", 2),
 "mashriq": G("mashriq", "مَشْرِق", "ش ر ق", "noun", "the east, the place of sunrise", "doğu, güneşin doğduğu yer", 1),
 "maghrib": G("maghrib", "مَغْرِب", "غ ر ب", "noun", "the west, the place of sunset", "batı, güneşin battığı yer", 1),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
# ---------------------------------------------------------------- paradigms (every verb copied with its stored paradigm after a lemma check)
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 4 (print pp. 15–18, sections 9–10): Ibrāhīm's call to his people (s1–s17) and «before the king» (s18–s35). "
          "s3–s6 quote al-Shuʿarāʾ 26:71–74, s10–s13 quote 26:78–81, and s26, s27 and s33 quote al-Baqara 2:258 as the print sets them (marked). One printed line is one sentence; the printed vowelling is kept (رَبِّيَ in s24 with the fatḥa the print carries).")
ADD_TR = (" Dördüncü bölüm (basılı s. 15–18, 9–10. kısımlar): İbrâhim'in kavmini daveti (s1–s17) ve «kralın huzurunda» (s18–s35). "
          "s3–s6 Şuarâ 26:71–74'ü, s10–s13 26:78–81'i, s26, s27 ve s33 Bakara 2:258'i baskıdaki şekliyle aktarır (işaretli). Basılı her satır bir cümledir; basılı hareke korunmuştur (s24'teki رَبِّيَ baskıdaki fethayla).")
write_out(4, S, TITLE, ADD_EN, ADD_TR, "pp. 15–18", GLOSS_ADD)
report(4, S, GLOSS_ADD, ())
