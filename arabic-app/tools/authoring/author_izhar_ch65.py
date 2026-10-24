# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 65: the non-lāzim mabnī continued — the badal and the joined word of the munādā free of the lām share its ruling
# (يَا رَجُلُ زَيْدُ، يَا زَيْدُ وَعَمْرُو); the particles of calling — يَا، أَيَا، هَيَا، آ، آيْ، أَيْ and the hamza — and وَا, particular to the lament; the ism of the
# lā that denies the genus when single, indefinite, joined to lā and not repeated (لَا رَجُلَ); and the muḍāriʿ with the feminine-plural nūn or the nūn of
# emphasis joined to it (يَضْرِبْنَ، تَضْرِبْنَ؛ هَلْ يَضْرِبَنَّ، هَلْ تَضْرِبَنَّ) — all these words must be built. Print pp. 159–160.
# The Ottoman commentary (izhar-full-corrected l. 1945 ff.) is followed for the readings of the examples.
#   python3 author_izhar_ch65.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HV = "hollow-verbs"; MSD = "masdar"; MR = "mudari-marfu"; MAW = "ism-mawsul"; IN = "inna-wa-akhawatuha"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"; IST = "al-istifham"; LN = "la-nafiya"; AMS = "an-masdariyya"
NSB = "ism-mansub"; MQ = "ism-maqsur-manqus"; JT = "jam-taksir"; F2 = "form-ii-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; MNF = "mana-al-fil"; INS = "in-shartiyya"; JZ = "nawasib-wa-jawazim-al-mudari"; YM = "ya-al-mutakallim"; DF = "damir-fasl"
TMZ = "tamyiz"; IRB = "al-murab-wal-mabni-wal-irab"; ND = "vocative-munada"; BD = "badal"; TW = "tawabi-al-musnad-ilayh"; LNJ = "la-nafiya-lil-jins"; NT = "nun-tawkid"; F8 = "form-viii-verbs"; ISH = "asma-al-ishara-wa-sighuha"; IDH = "idha-shartiyya"
K = "al-mabni-ghayr-al-lazim-tawabi-al-munada-wa-huruf-al-nida-wa-ism-la-wal-mudari-bil-nun"
K64 = "al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada"
TITLE = {"ar": "تَوَابِعُ الْمُنَادَى، وَحُرُوفُ النِّدَاءِ، وَاسْمُ لَا لِنَفْيِ الْجِنْسِ، وَالْمُضَارِعُ الْمُتَّصِلُ بِهِ النُّونُ — وَاجِبُ الْبِنَاءِ", "en": "The followers of the munādā, the particles of calling, the ism of the genus-denying lā, and the muḍāriʿ with the nūn joined — what must be built", "tr": "Münâdânın tâbileri, nidâ harfleri, cins olumsuzlayan lâ'nın ismi ve nûn bitişmiş muzâri — binâsı vâcip olanlar"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wnahw(punct=None): return tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«and as in»", "«ve … gibi»", punct=punct, segments=wa("نَحْوُ", "nahw", "noun"))
def ya(): return tok("يَا", "ya-nida", "part", [K, ND], "لَفْظٌ مَحْكِيٌّ: حَرْفُ نِدَاءٍ.", "«O»", "«ey»")
def wya(): return tok("وَيَا", "ya-nida", "part", [K, AT, ND], "الْوَاوُ عَاطِفَةٌ، وَيَا حَرْفُ نِدَاءٍ.", "«and O»", "«ve ey»", segments=wa("يَا", "ya-nida", "part"))
def harf(form, lex, en, tr, first=False, punct=None, ar=None):
    a = ar or (("خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — لَفْظٌ مَحْكِيٌّ: حَرْفُ نِدَاءٍ." if first else "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " مَعْطُوفٌ — لَفْظٌ مَحْكِيٌّ: حَرْفُ نِدَاءٍ."))
    return tok(form, lex, "part", [K, ND] + ([MK, HT] if first else [AT]), a, en, tr, punct=punct, segments=None if first else wa(form[2:], lex, "part"))
def hal_(w=False): return tok("وَهَلْ" if w else "هَلْ", "hal-istifham", "part", [K, IST] + ([AT] if w else []), ("الْوَاوُ عَاطِفَةٌ، وَهَلْ" if w else "لَفْظٌ مَحْكِيٌّ: هَلْ") + " حَرْفُ اسْتِفْهَامٍ.", "«and does»" if w else "«does»", "«ve … mi»" if w else "«… mi»", segments=wa("هَلْ", "hal-istifham", "part") if w else None)

# ----------- s1 — the badal and the joined word of the munādā
S.append({"id": "s1", "translation": {"en": "And the badal and the joined word free of the lām — its ruling is the ruling of the munādā, as in «O man, Zayd!» and «O Zayd and ʿAmr!»;", "tr": "Lâmdan hâlî bedel ve ma'tûfun hükmü münâdânın hükmüdür — «ey adam, Zeyd!» ve «ey Zeyd ve Amr!» gibi;"},
 "tokens": [
  tok("وَالْبَدَلُ", "badal", "noun", [K, AT, MK, BD, TW], "الْوَاوُ عَاطِفَةٌ، وَالْبَدَلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the badal»", "«bedel»", segments=wa("الْبَدَلُ", "badal", "noun")),
  tok("وَالْمَعْطُوفُ", "matuf", "noun", [K, AT, IMF, TW], "الْوَاوُ عَاطِفَةٌ، وَالْمَعْطُوفُ مَعْطُوفٌ عَلَى الْبَدَلُ مَرْفُوعٌ.", "«and the joined word»", "«ve ma'tûf»", segments=wa("الْمَعْطُوفُ", "matuf", "noun")),
  tok("الْخَالِي", "khali", "noun", [K, NA, IFA, MQ], "نَعْتٌ لِلْمَعْطُوفِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«free»", "«hâlî»"),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  tok("اللَّامِ", "lam-letter", "noun", [K, HJ, "anwa-al-lam-al-tarif"], "مَجْرُورٌ بِعَنْ — لَامِ التَّعْرِيفِ؛ فَالْمَعْطُوفُ ذُو اللَّامِ يُنْصَبُ: يَا زَيْدُ وَالْحَارِثَ.", "«the lām» — the definite article; with it the joined word takes naṣb.", "«lâm» — harf-i tarif; onunla ma'tûf nasb alır.", punct="،"),
  tok("حُكْمُهُ", "hukm", "noun", [K, MK, ID], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its ruling»", "«hükmü»", segments=[seg("حُكْمُ", "hukm", "noun"), pr3ms()]),
  tok("حُكْمُ", "hukm", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — وَالْجُمْلَةُ خَبَرُ الْبَدَلُ.", "«the ruling of»", "«hükmüdür»"),
  tok("الْمُنَادَى", "munada", "noun", [K, ID, IMF, ND, MQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — الْبِنَاءُ عَلَى الضَّمِّ.", "«the munādā» — built on ḍamma like it.", "«münâdâ» — onun gibi damme üzere mebnî.", punct="،"),
  nahw(punct=":"),
  ya(),
  tok("رَجُلُ", "rajul", "noun", [K, ND, IRB], "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ.", "«man» — built on ḍamma.", "«adam» — damme üzere mebnî."),
  tok("زَيْدُ", "zayd", "propn", [K, BD, TW, IRB], "بَدَلٌ مِنَ الْمُنَادَى مَبْنِيٌّ عَلَى الضَّمِّ — حُكْمُهُ حُكْمُهُ.", "«Zayd» — the badal, built on ḍamma like the munādā.", "«Zeyd» — bedel, münâdâ gibi damme üzere.", punct="،"),
  wya(),
  tok("زَيْدُ", "zayd", "propn", [K, ND, IRB], "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ.", "«Zayd»", "«Zeyd»"),
  tok("وَعَمْرُو", "amr-name", "propn", [K, AT, TW, IRB], "الْوَاوُ عَاطِفَةٌ، وَعَمْرُو مَعْطُوفٌ خَالٍ عَنِ اللَّامِ مَبْنِيٌّ عَلَى الضَّمِّ.", "«and ʿAmr» — joined, lām-less, built on ḍamma.", "«ve Amr» — lâmsız ma'tûf, damme üzere mebnî.", punct="،", segments=wa("عَمْرُو", "amr-name", "propn")),
 ]})
# ----------- s2 — the particles of calling
S.append({"id": "s2", "translation": {"en": "and the particles of calling are yā, ayā, hayā, ā, āy, ay and the hamza; and wā is particular to the lament;", "tr": "nidâ harfleri yâ, eyâ, heyâ, â, ây, ey ve hemzedir; vâ ise nüdbeye mahsustur;"},
 "tokens": [
  tok("وَحُرُوفُ", "harf", "noun", [K, AT, MK, ID, JT, ND], "الْوَاوُ عَاطِفَةٌ، وَحُرُوفُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the particles of»", "«harfleri»", segments=wa("حُرُوفُ", "harf", "noun")),
  tok("النِّدَاءِ", "nida", "noun", [K, ID, MSD, ND], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«calling»", "«nidâ»"),
  harf("يَا", "ya-nida", "«yā»", "«yâ»", first=True),
  harf("وَأَيَا", "aya-nida", "«ayā» — for the distant", "«eyâ» — uzaktaki için"),
  harf("وَهَيَا", "haya-nida", "«hayā» — for the distant", "«heyâ» — uzaktaki için"),
  harf("وَآ", "a-nida", "«ā»", "«â»"),
  harf("وَآيْ", "ay-long-nida", "«āy»", "«ây»"),
  harf("وَأَيْ", "ay-nida", "«ay» — for the near", "«ey» — yakındaki için"),
  tok("وَالْهَمْزَةُ", "hamza-letter", "noun", [K, AT, ND], "الْوَاوُ عَاطِفَةٌ، وَالْهَمْزَةُ مَعْطُوفٌ مَرْفُوعٌ — أَزَيْدُ، لِلْقَرِيبِ.", "«and the hamza» — a-Zaydu, for the near.", "«ve hemze» — e-Zeydü, yakındaki için.", punct="،", segments=wa("الْهَمْزَةُ", "hamza-letter", "noun")),
  tok("وَوَا", "wa-nudba", "part", [K, AT, MK, ND], "الْوَاوُ عَاطِفَةٌ، وَوَا مُبْتَدَأٌ — لَفْظٌ مَحْكِيٌّ.", "«and wā»", "«ve vâ»", segments=wa("وَا", "wa-nudba", "part")),
  tok("مُخْتَصٌّ", "mukhtass", "noun", [K, MK, IMF, F8], "خَبَرٌ مَرْفُوعٌ.", "«is particular»", "«mahsustur»"),
  tok("بِالنُّدْبَةِ", "nudba", "noun", [K, HJ, MSD, ND], "الْبَاءُ حَرْفُ جَرٍّ، وَالنُّدْبَةِ مَجْرُورٌ — وَا زَيْدَاهْ.", "«to the lament» — wā zaydāh.", "«nüdbeye» — vâ zeydâh.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("النُّدْبَةِ", "nudba", "noun")]),
 ]})
# ----------- s3 — the ism of the genus-denying lā
S.append({"id": "s3", "translation": {"en": "and the ism of the lā that denies the genus, when it is single, indefinite, joined to lā, and lā is not repeated — as in «there is no man»;", "tr": "cins olumsuzlayan lâ'nın ismi — müfred, nekre, lâ'ya bitişik ve lâ tekrarlanmamış olunca — «hiç adam yok» gibi;"},
 "tokens": [
  tok("وَاسْمُ", "ism", "noun", [K, AT, MK, ID, LNJ], "الْوَاوُ عَاطِفَةٌ، وَاسْمُ مَعْطُوفٌ عَلَى الْبَدَلُ مَرْفُوعٌ، مُضَافٌ.", "«and the ism of»", "«ve ismi»", segments=wa("اسْمُ", "ism", "noun")),
  tok("لَا", "la", "part", [K, ID, LNJ], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«lā»", "«lâ»"),
  tok("لِنَفْيِ", "nafy", "noun", [K, HJ, ID, MSD, LNJ], "اللَّامُ حَرْفُ جَرٍّ، وَنَفْيِ مَجْرُورٌ، مُضَافٌ — نَعْتٌ لِلَا.", "«that denies»", "«olumsuzlayan»", segments=[seg("لِ", "li", "prep"), seg("نَفْيِ", "nafy", "noun")]),
  tok("الْجِنْسِ", "jins", "noun", [K, ID, LNJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the genus»", "«cinsi»"),
  tok("إِذَا", "idha", "part", [K, IDH, MF], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-ınca»"),
  tok("كَانَ", "kana", "verb", [K, IDH, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is»", "«olunca»"),
  tok("مُفْرَدًا", "mufrad", "noun", [K, KN, IMF, F4, LNJ], "خَبَرُ كَانَ مَنْصُوبٌ — غَيْرَ مُضَافٍ وَلَا شَبِيهٍ بِهِ.", "«single»", "«müfred»"),
  tok("نَكِرَةً", "nakira", "noun", [K, KN, AT, LNJ], "خَبَرٌ ثَانٍ مَنْصُوبٌ.", "«indefinite»", "«nekre»"),
  tok("مُتَّصِلَةً", "muttasil", "noun", [K, KN, AT, IFA, F8], "خَبَرٌ ثَالِثٌ مَنْصُوبٌ.", "«joined»", "«bitişik»"),
  tok("بِلَا", "la", "part", [K, HJ, LNJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَا لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«to lā»", "«lâ'ya»", segments=[seg("بِ", "bi", "prep"), seg("لَا", "la", "part")]),
  tok("غَيْرَ", "ghayr", "noun", [K, "hal", ID], "حَالٌ مِنْ لَا مَنْصُوبٌ، مُضَافٌ.", "«not»", "«-mamış»"),
  tok("مُكَرَّرَةٍ", "mukarrar", "noun", [K, ID, IMF, F2], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَإِنْ تَكَرَّرَتْ جَازَتِ الْأَوْجُهُ.", "«repeated» — if lā is repeated, the options open.", "«tekrarlanmış» — lâ tekrarlanırsa vecihler açılır.", punct="،"),
  nahw(punct=":"),
  tok("لَا", "la", "part", [K, LNJ], "لَفْظٌ مَحْكِيٌّ: لَا النَّافِيَةُ لِلْجِنْسِ، تَعْمَلُ عَمَلَ إِنَّ.", "«there is no» — lā of the genus, working like inna.", "«hiç … yok» — cins lâ'sı, inne gibi amel eder."),
  tok("رَجُلَ", "rajul", "noun", [K, LNJ, IRB], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَالْخَبَرُ مَحْذُوفٌ: فِي الدَّارِ.", "«man» — lā's ism, built on fatḥa; the khabar dropped.", "«adam» — lâ'nın ismi, fetha üzere mebnî; haber hazfedilmiş.", punct="،"),
 ]})
# ----------- s4 — the muḍāriʿ with the nūn; all must be built
S.append({"id": "s4", "translation": {"en": "and the muḍāriʿ to which the nūn of the feminine plural or the nūn of emphasis is joined — as in «they (f.) strike» and «you (f.) strike», and as in «does he indeed strike?» and «do you indeed strike?». And these words must be built.", "tr": "ve cem'-i müennes nûnu ya da te'kîd nûnu bitişmiş muzâri — «(o kadınlar) döverler» ve «(siz kadınlar) döversiniz» gibi, «gerçekten döver mi?» ve «gerçekten döver misin?» gibi. Bu lafızların binâsı vâciptir."},
 "tokens": [
  tok("وَالْمُضَارِعُ", "mudari", "noun", [K, AT, IFA, MR], "الْوَاوُ عَاطِفَةٌ، وَالْمُضَارِعُ مَعْطُوفٌ عَلَى الْبَدَلُ مَرْفُوعٌ.", "«and the muḍāriʿ»", "«ve muzâri»", segments=wa("الْمُضَارِعُ", "mudari", "noun")),
  tok("الْمُتَّصِلُ", "muttasil", "noun", [K, NA, IFA, F8], "نَعْتٌ مَرْفُوعٌ — سَبَبِيٌّ.", "«to which is joined»", "«bitişmiş»"),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to it»", "«ona»", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("نُونُ", "nun-letter", "noun", [K, FL, ID], "فَاعِلُ الْمُتَّصِلِ مَرْفُوعٌ، مُضَافٌ.", "«the nūn of»", "«nûnu»"),
  tok("جَمْعِ", "jam", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the plural of»", "«cem'-i»"),
  tok("الْمُؤَنَّثِ", "muannath", "noun", [K, ID, IMF, F2], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نُونُ النِّسْوَةِ.", "«the feminine» — the nūn of the women.", "«müennes» — nisve nûnu."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("نُونُ", "nun-letter", "noun", [K, AT, ID, NT], "مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«the nūn of»", "«nûnu»"),
  tok("التَّأْكِيدِ", "takid", "noun", [K, ID, MSD, F2, NT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الثَّقِيلَةُ وَالْخَفِيفَةُ.", "«emphasis» — heavy and light.", "«te'kîd» — sakîle ve hafîfe.", punct="،"),
  nahw(punct=":"),
  tok("يَضْرِبْنَ", "daraba", "verb", [K, MR, FL, IRB], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ فَاعِلٌ.", "«they (f.) strike» — built on sukūn; the nūn is the doer.", "«(onlar) döverler» — sükûn üzere mebnî; nûn fâil.", segments=[seg("يَضْرِبْ", "daraba", "verb"), seg("نَ", "pron-3fp", "pron")]),
  tok("وَتَضْرِبْنَ", "daraba", "verb", [K, AT, MR, FL, IRB], "الْوَاوُ عَاطِفَةٌ، وَتَضْرِبْنَ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالنُّونُ فَاعِلٌ.", "«and you (f.) strike»", "«ve (siz) döversiniz»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("تَضْرِبْ", "daraba", "verb"), seg("نَ", "pron-2fp", "pron")]),
  wnahw(punct=":"),
  hal_(),
  tok("يَضْرِبَنَّ", "daraba", "verb", [K, MR, NT, IRB], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّأْكِيدِ الثَّقِيلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«does he indeed strike» — built on fatḥa with the heavy nūn.", "«gerçekten döver mi» — sakîle nûnla fetha üzere mebnî.", segments=[seg("يَضْرِبَ", "daraba", "verb"), seg("نَّ", "nun-tawkid", "part")]),
  hal_(w=True),
  tok("تَضْرِبَنَّ", "daraba", "verb", [K, MR, NT, IRB], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«do you indeed strike»", "«gerçekten döver misin»", punct="،", segments=[seg("تَضْرِبَ", "daraba", "verb"), seg("نَّ", "nun-tawkid", "part")]),
  tok("وَهٰذِهِ", "hadhihi", "pron", [K, AT, MK, ISH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰذِهِ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and these»", "«ve bu»", segments=wa("هٰذِهِ", "hadhihi", "pron")),
  tok("الْأَلْفَاظُ", "lafz", "noun", [K, BD, JT], "بَدَلٌ مِنْ هٰذِهِ مَرْفُوعٌ — أَوْ عَطْفُ بَيَانٍ.", "«words» — in apposition.", "«lafızlar» — bedel."),
  tok("يَجِبُ", "wajaba", "verb", [K, MK, MR, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرٌ.", "«must» — the khabar clause.", "«vâciptir» — haber cümlesi."),
  tok("بِنَاؤُهَا", "bina", "noun", [K, FL, ID, MSD, IRB], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — خِلَافُ جَائِزِ الْبِنَاءِ الْآتِي.", "«be built» — as against the optional building to come.", "«mebnî olması» — gelecek câiz binânın karşıtı.", punct=".", segments=[seg("بِنَاؤُ", "bina", "noun"), pr3fs()]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "haya-nida": G("haya-nida", "هَيَا", "ه ي ا", "part", "hayā — a particle of calling, for the distant", "heyâ — nidâ harfi, uzaktaki için", 4),
 "a-nida": G("a-nida", "آ", "ا", "part", "ā — a particle of calling", "â — nidâ harfi", 4),
 "ay-long-nida": G("ay-long-nida", "آيْ", "ا ي", "part", "āy — a particle of calling", "ây — nidâ harfi", 4),
 "ay-nida": G("ay-nida", "أَيْ", "أ ي", "part", "ay — a particle of calling, for the near", "ey — nidâ harfi, yakındaki için", 4),
 "wa-nudba": G("wa-nudba", "وَا", "و ا", "part", "wā — the particle of the lament (nudba): wā zaydāh", "vâ — nüdbe harfi: vâ zeydâh", 4),
}
used = set()
for s in S:
    for t in s["tokens"]:
        used.add(t["lex"])
        for sg_ in t.get("segments", []): used.add(sg_["lex"])
CAND = {}
for k in sorted(used):
    if k in TG: continue
    if k in NEW: CAND[k] = NEW[k]
    elif _ic.has_gloss(k): CAND[k] = find_gloss(k)
    else: raise SystemExit(f"no gloss anywhere for {k}")
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch65 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("kana", "daraba", "wajaba") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "بَدَلُ الْمُنَادَى وَمَعْطُوفُهُ الْخَالِي عَنِ اللَّامِ، وَحُرُوفُ النِّدَاءِ السَّبْعَةُ وَوَا، وَاسْمُ لَا لِنَفْيِ الْجِنْسِ الْمَبْنِيُّ، وَالْمُضَارِعُ مَعَ نُونِ النِّسْوَةِ وَنُونِ التَّأْكِيدِ", "en": "The munādā's badal and lām-less joined word; the seven particles of calling and wā; the built ism of the genus-denying lā; the muḍāriʿ with the women's nūn and the nūn of emphasis", "tr": "Münâdânın bedeli ve lâmsız ma'tûfu; yedi nidâ harfi ve vâ; cins olumsuzlayan lâ'nın mebnî ismi; nisve nûnu ve te'kîd nûnu ile muzâri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المبني غير اللازم: توابع المنادى، حروف النداء، اسم لا، المضارع مع النون", "الكافية لابن الحاجب — المنادى، لا لنفي الجنس، نونا التأكيد", "شرح قطر الندى لابن هشام — المنادى وتوابعه، لا النافية للجنس"],
 "amil": "the badal and the joined word of the munādā free of the lām share its ruling (يَا رَجُلُ زَيْدُ، يَا زَيْدُ وَعَمْرُو); the particles of calling are يَا، أَيَا، هَيَا، آ، آيْ، أَيْ and the hamza, with وَا particular to the lament; the ism of the genus-denying lā is built when single, indefinite, joined to lā and lā not repeated (لَا رَجُلَ); the muḍāriʿ joined to the feminine-plural nūn or the nūn of emphasis is built (يَضْرِبْنَ، تَضْرِبْنَ؛ هَلْ يَضْرِبَنَّ، هَلْ تَضْرِبَنَّ) — all these must be built.",
 "question": {
  "en": ["How are the munādā's badal and joined word treated? Like the munādā itself — built on ḍamma when single and definite: يَا رَجُلُ زَيْدُ، يَا زَيْدُ وَعَمْرُو — provided the joined word has no lām; with the lām it takes naṣb (يَا زَيْدُ وَالْحَارِثَ).",
         "What are the particles of calling? Seven: يَا، أَيَا، هَيَا، آ، آيْ، أَيْ and the hamza — أَيَا and هَيَا for the distant, أَيْ and the hamza for the near, يَا for both; and وَا is particular to the lament (وَا زَيْدَاهْ).",
         "When is the ism of lā built? When lā denies the whole genus and its ism is single, indefinite, joined to lā, and lā is not repeated — لَا رَجُلَ, built on fatḥa in the position of naṣb, the khabar often dropped.",
         "What if lā is repeated or the ism is annexed? With repetition (لَا حَوْلَ وَلَا قُوَّةَ) the five options of the next chapter open; annexed or resembling the annexed, the ism takes naṣb (لَا صَاحِبَ عِلْمٍ مَمْقُوتٌ).",
         "Why is the muḍāriʿ built with the two nūns? With the women's nūn it is built on sukūn (يَضْرِبْنَ، تَضْرِبْنَ), with the nūn of emphasis on fatḥa (هَلْ يَضْرِبَنَّ) — the nūn joined directly to it breaks its likeness to the noun.",
         "What does «these words must be built» mark? The end of the obligatory building; the optional building — the adverbs annexed to a sentence, idh, mithl and ghayr, the repeated lā, the ṣifa of lā's ism — follows.",
         "What does the engine READ here? The DabtEngine reads يَا رَجُلُ زَيْدُ with the badal on the munādā's ḍamma, وَعَمْرُو joined on ḍamma, the cited particles as built forms, لَا رَجُلَ as lā's ism on fatḥa, يَضْرِبْنَ on sukūn with the nūn as doer and يَضْرِبَنَّ on fatḥa with the emphasis nūn."],
  "tr": ["Münâdânın bedeli ve ma'tûfu nasıl değerlendirilir? Münâdânın kendisi gibi — müfred ve ma'rife iken damme üzere mebnî: yâ racülü Zeydü, yâ Zeydü ve Amru — ma'tûfta lâm yoksa; lâm ile nasb alır (yâ Zeydü ve'l-Hârise).",
         "Nidâ harfleri nelerdir? Yedi: yâ, eyâ, heyâ, â, ây, ey ve hemze — eyâ ve heyâ uzaktaki, ey ve hemze yakındaki, yâ ikisi için; vâ ise nüdbeye mahsustur (vâ zeydâh).",
         "Lâ'nın ismi ne zaman mebnîdir? Lâ bütün cinsi olumsuzlayıp ismi müfred, nekre, lâ'ya bitişik ve lâ tekrarlanmamış olunca — lâ racüle, nasb mahallinde fetha üzere mebnî, haber çoğu zaman hazfedilir.",
         "Lâ tekrarlanırsa ya da isim muzâf olursa? Tekrarla (lâ havle ve lâ kuvvete) sonraki babın beş vechi açılır; muzâf ya da muzâfa benzer isim nasb alır (lâ sâhibe ilmin memkûtün).",
         "Muzâri iki nûnla neden mebnîdir? Nisve nûnuyla sükûn üzere (yadribne, tadribne), te'kîd nûnuyla fetha üzere (hel yadribenne) — doğrudan bitişen nûn isme benzerliğini bozar.",
         "«Bu lafızların binâsı vâciptir» neyi işaretler? Vâcip binânın sonunu; câiz binâ — cümleye muzâf zarflar, iz, misl ve gayr, tekrarlanan lâ, lâ'nın isminin sıfatı — gelir.",
         "Motor burada neyi OKUR? DabtEngine yâ racülü Zeydü'yü münâdânın dammesinde bedelle, ve Amru'yu damme üzere ma'tûf, alıntı harfleri mebnî şekiller, lâ racüle'yi fetha üzere lâ'nın ismi, yadribne'yi nûnu fâil olarak sükûn üzere ve yadribenne'yi te'kîd nûnuyla fetha üzere okur."],
 },
 "plain": {"en": "A word replacing or added to a called name freezes like it: yā rajulu Zaydu, yā Zaydu wa-ʿAmru. The call-words are yā, ayā, hayā, ā, āy, ay and a-; wā is for laments. After «no» denying a whole kind, a single indefinite noun ends in -a (lā rajula). A verb with the women's -na or the emphatic -nna freezes too.",
           "tr": "Seslenilen adın yerini tutan ya da ona eklenen sözcük onun gibi donar: yâ racülü Zeydü, yâ Zeydü ve Amru. Seslenme sözleri yâ, eyâ, heyâ, â, ây, ey ve e-; vâ ağıt içindir. Bir cinsi olumsuzlayan «hiç»ten sonra tek belirsiz isim -a ile biter (lâ racüle). Kadınların -ne'si ya da vurgulu -nne'siyle fiil de donar."},
 "explanation": {"en": "The badal and the joined word of the munādā free of the lām take the ruling of the munādā — يَا رَجُلُ زَيْدُ، يَا زَيْدُ وَعَمْرُو. The particles of calling are يَا، أَيَا، هَيَا، آ، آيْ، أَيْ and the hamza; وَا is particular to the lament. The ism of the lā that denies the genus is built when it is single, indefinite, joined to lā, and lā is not repeated — لَا رَجُلَ. The muḍāriʿ to which the feminine-plural nūn or the nūn of emphasis is joined is built — يَضْرِبْنَ، تَضْرِبْنَ؛ هَلْ يَضْرِبَنَّ، هَلْ تَضْرِبَنَّ. These words must be built; the optional building follows.",
                 "tr": "Lâmdan hâlî bedel ve münâdânın ma'tûfu münâdânın hükmünü alır — yâ racülü Zeydü, yâ Zeydü ve Amru. Nidâ harfleri yâ, eyâ, heyâ, â, ây, ey ve hemzedir; vâ nüdbeye mahsustur. Cins olumsuzlayan lâ'nın ismi müfred, nekre, lâ'ya bitişik ve lâ tekrarlanmamış olunca mebnîdir — lâ racüle. Cem'-i müennes nûnu ya da te'kîd nûnu bitişmiş muzâri mebnîdir — yadribne, tadribne; hel yadribenne, hel tadribenne. Bu lafızların binâsı vâciptir; câiz binâ gelir."},
 "examples": [
  {"ar": "يَا رَجُلُ زَيْدُ، وَيَا زَيْدُ وَعَمْرُو", "en": "the munādā's badal and joined word", "tr": "münâdânın bedeli ve ma'tûfu", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "يَا وَأَيَا وَهَيَا وَآ وَآيْ وَأَيْ وَالْهَمْزَةُ، وَوَا مُخْتَصٌّ بِالنُّدْبَةِ", "en": "the particles of calling", "tr": "nidâ harfleri", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "لَا رَجُلَ", "en": "the built ism of the genus-denying lā", "tr": "cins lâ'sının mebnî ismi", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "يَضْرِبْنَ وَتَضْرِبْنَ، هَلْ يَضْرِبَنَّ وَهَلْ تَضْرِبَنَّ", "en": "the muḍāriʿ built with the two nūns", "tr": "iki nûnla mebnî muzâri", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "يَا زَيْدُ وَعَمْرًا", "right": "يَا زَيْدُ وَعَمْرُو", "why": {"en": "the lām-less joined word follows the munādā's building on ḍamma", "tr": "lâmsız ma'tûf münâdânın damme üzere binâsına uyar"}},
  {"wrong": "لَا رَجُلٌ فِي الدَّارِ (denying the genus)", "right": "لَا رَجُلَ فِي الدَّارِ", "why": {"en": "the single indefinite ism of the genus-lā is built on fatḥa", "tr": "cins lâ'sının müfred nekre ismi fetha üzere mebnîdir"}},
  {"wrong": "هُنَّ يَضْرِبُونَ", "right": "هُنَّ يَضْرِبْنَ", "why": {"en": "with the women's nūn the muḍāriʿ is built on sukūn", "tr": "nisve nûnuyla muzâri sükûn üzere mebnîdir"}},
  {"wrong": "هَلْ يَضْرِبُنَّ", "right": "هَلْ يَضْرِبَنَّ", "why": {"en": "with the nūn of emphasis the singular muḍāriʿ is built on fatḥa", "tr": "te'kîd nûnuyla müfred muzâri fetha üzere mebnîdir"}},
 ],
}
ADD_EN = (" Chapter 65 (print pp. 159-160): the munādā's badal and lām-less joined word (s1); the seven particles of calling and wā of the lament (s2); the built ism of the genus-denying lā (s3); the muḍāriʿ with the women's nūn and the nūn of emphasis, and the close of the obligatory building (s4).")
ADD_TR = (" Altmış beşinci bab (baskı s. 159-160): münâdânın bedeli ve lâmsız ma'tûfu (s1); yedi nidâ harfi ve nüdbe vâ'sı (s2); cins olumsuzlayan lâ'nın mebnî ismi (s3); nisve nûnu ve te'kîd nûnu ile muzâri ve vâcip binânın kapanışı (s4).")
write_out(65, S, TITLE, ADD_EN, ADD_TR, "pp. 159-160", GLOSS_ADD, notes=(NOTE,),
          related=((K64, [K]), (ND, [K]), (LNJ, [K]), (NT, [K]), (BD, [K]), (IRB, [K])))
report(65, S, GLOSS_ADD, (NOTE,))
