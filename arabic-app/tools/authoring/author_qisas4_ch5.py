# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 5: «السَّهْمُ الْأَخِيرُ» — sections 10–14 of the story of Shuʿayb (print pp. 8–10):
the last arrow of the proud (7:88), Shuʿayb's cutting answer (7:88–89), the old refrain (26:185–187), the end of a people (7:91–92), and the prophet who delivered (7:93).
python3 tools/authoring/author_qisas4_ch5.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "السَّهْمُ الْأَخِيرُ", "en": "The last arrow", "tr": "Son ok"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; SH = "in-shartiyya"; JS = "jam-mudhakkar-salim"; TW = "tawkid"; NT = "nun-tawkid"
def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=(), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [ID] + list(tags), ar, en, tr, punct=punct)
def naat(full, lex, en, tr, punct=None, tags=(), case="jarr"):
    C = {"jarr": "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
    return tok(full, lex, "noun", [NA] + list(tags), C, en + " — the naʿt.", tr + " — sıfat.", punct=punct)
def prep_pron(full, lex, pron_form, pron_lex, en, tr, punct=None, tags=(), extra_ar=""):
    pre = full[:len(full) - len(pron_form)]
    return tok(full, lex, "prep", [HJ] + list(tags), "حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra_ar + ".", en, tr, punct=punct, segments=[seg(pre, lex, "prep"), seg(pron_form, pron_lex, "pron")])
def maful_(full, lex, en, tr, punct=None, tags=(), ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [MB] + list(tags), ar, en, tr, punct=punct)
def jarr_salim(full, lex, en, tr, punct=None, tags=(), pre_ar="مَجْرُورٌ"): return tok(full, lex, "noun", [HJ, JS] + list(tags), pre_ar + " بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", en + " — a sound masculine plural, jarr by the yāʾ.", tr + " — cem-i müzekker sâlim, yâ ile mecrûr.", punct=punct)
def noun_pron(full, lex, stem, pron_form, pron_lex, ar, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", list(tags), ar, en, tr, punct=punct, segments=[seg(stem, lex, "noun"), seg(pron_form, pron_lex, "pron")])
def ya_qawmi(): return [tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
                        tok("قَوْمِ", "qawm", "noun", ["vocative-munada", ID, "ya-al-mutakallim"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَالْكَسْرَةُ دَلِيلُهَا.", "«my people» — the munādā annexed to the dropped yāʾ.", "«kavmim» — hazfedilmiş mütekellim yâsına muzâf münâdâ.")]

# ---------------------------------------------------------------- §10 السَّهْمُ الْأَخِيرُ
sen("s1", "And when their argument was cut off they loosed the last arrow — the one the proud of every nation have loosed at their prophet and his followers:",
        "Delilleri tükenince son oku attılar: her ümmetin kibirlilerinin peygamberlerine ve ona uyanlara attığı oku:", [
  tok("وَلَمَّا", "lamma", "part", [AT, MF, SH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the ẓarf lammā, with a shart's sense.", "«ve … -ınca» — şart anlamı taşıyan lemmâ zarfı.", segments=wa_("لَمَّا", "lamma", "part")),
  mazi_ta("انْقَطَعَتْ", "inqataa", "«was cut off»", "«kesildi, tükendi»", tags=[SH, "form-vii-verbs"]),
  noun_pron("حُجَّتُهُمْ", "hujja", "حُجَّتُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their argument» — the doer.", "«delilleri» — fâil.", tags=[FL, ID]),
  mazi_pl("أَطْلَقُوا", "atlaqa", "«they loosed»", "«attılar»", tags=[SH, MB, "form-iv-verbs"]),
  maful_("السَّهْمَ", "sahm", "«the arrow»", "«oku»"),
  naat("الْأَخِيرَ", "akhir-last", "«the last»", "«son»", case="nasb"),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِلسَّهْمِ.", "«which» — a naʿt of the arrow.", "«… -dığı» — okun sıfatı."),
  tok("أَطْلَقَهُ", "atlaqa", "verb", [MW, MB, "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«loosed» — the ṣila; its object the hāʾ.", "«attığı» — sıla; hâ mef'ûl.", segments=[seg("أَطْلَقَ", "atlaqa", "verb"), pr3ms()]),
  tok("الْمُتَكَبِّرُونَ", "mutakabbir", "noun", [FL, JS, "ism-fail", "form-v-verbs"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the proud» — the doer, rafʿ by the wāw.", "«kibirlenenler» — fâil, vâv ile merfû."),
  tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"), majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID]), mudaf_ilayh("أُمَّةٍ", "umma", "«nation»", "«ümmet»"),
  tok("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«at»", "«-e»"),
  noun_pron("نَبِيِّهِمْ", "nabi", "نَبِيِّ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«their prophet»", "«peygamberlerine»", tags=[HJ, ID]),
  noun_pron("وَأَتْبَاعِهِمْ", "atba", "وَأَتْبَاعِ", "هِمْ", "pron-3mp", "الْوَاوُ عَاطِفَةٌ، وَأَتْبَاعِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and his followers»", "«ve ona uyanlara»", punct=":", tags=[AT, ID, "jam-taksir"]),
])
sen("s2", "«The chiefs who were proud among his people said: We shall surely drive you out, O Shuʿayb, and those who believe with you, from our town — or you shall return to our creed» (7:88).",
        "«Kavminden büyüklük taslayan ileri gelenler dediler ki: Ey Şuayb, seni ve seninle birlikte iman edenleri kasabamızdan mutlaka çıkaracağız; ya da dinimize döneceksiniz» (7:88).", [
  *quran([
  qala(punct=None), tok("الْمَلَأُ", "mala-chiefs", "noun", [FL], "فَاعِلٌ مَرْفُوعٌ.", "«the chiefs» — the doer.", "«ileri gelenler» — fâil."),
  tok("الَّذِينَ", "alladhina", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِلْمَلَإِ.", "«who» — a naʿt of the chiefs.", "«… olanlar» — mele'in sıfatı."),
  mazi_pl("اسْتَكْبَرُوا", "istakbara", "«were proud»", "«büyüklük tasladılar»", tags=[MW, "form-x-verbs"]),
  tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ.", "«among»", "«-den»"),
  noun_pron("قَوْمِهِ", "qawm", "قَوْمِ", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people»", "«kavminden»", punct=":", tags=[HJ, ID]),
  tok("لَنُخْرِجَنَّكَ", "akhraja", "verb", [TW, NT, MB, "form-iv-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مُقَدَّرٍ، وَنُخْرِجَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«we shall surely drive you out» — the oath's lām, the heavy nūn: the verb is built on fatḥa.", "«seni mutlaka çıkaracağız» — kasem lâmı, şeddeli tekid nûnu: fiil fetha üzere mebnî.", segments=[seg("لَ", "lam-qasam", "part"), seg("نُخْرِجَنَّ", "akhraja", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("شُعَيْبُ", "shuayb", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ.", "«Shuʿayb» — the munādā on the ḍamma.", "«Şuayb» — damme üzere münâdâ."),
  tok("وَالَّذِينَ", "alladhina", "pron", [AT, MW], "الْوَاوُ عَاطِفَةٌ، وَالَّذِينَ مَعْطُوفٌ عَلَى الْكَافِ فِي مَحَلِّ نَصْبٍ.", "«and those who» — joined to the object كَ.", "«ve … olanları» — kâf'a atıf.", segments=wa_("الَّذِينَ", "alladhina", "pron")),
  mazi_pl("آمَنُوا", "aamana", "«believe»", "«iman eden»", tags=[MW, "form-iv-verbs"]),
  prep_pron("مَعَكَ", "maa", "كَ", "pron-2ms", "«with you»", "«seninle»", extra_ar=" — مَعَ ظَرْفٌ مُضَافٌ"),
  tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  noun_pron("قَرْيَتِنَا", "qarya", "قَرْيَتِ", "نَا", "pron-1p", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our town»", "«kasabamızdan»", tags=[HJ, ID]),
  tok("أَوْ", "aw", "part", [AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("لَتَعُودُنَّ", "ada-return", "verb", [TW, NT, AK, "hollow-verbs"], "اللَّامُ لِلْقَسَمِ، وَتَعُودُنَّ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ الْمَحْذُوفَةِ لِتَوَالِي الْأَمْثَالِ، وَوَاوُ الْجَمَاعَةِ الْمَحْذُوفَةُ لِالْتِقَاءِ السَّاكِنَيْنِ فَاعِلٌ، وَالنُّونُ لِلتَّوْكِيدِ.", "«you shall surely return» — the raf-nūn dropped before the heavy nūn, the group's wāw dropped for the two sukūns.", "«mutlaka döneceksiniz» — ref nûnu tekid nûnu önünde, cemaat vâvı iki sâkin için düşmüş.", segments=[seg("لَ", "lam-qasam", "part"), seg("تَعُودُنَّ", "ada-return", "verb")]),
  fi(), noun_pron("مِلَّتِنَا", "milla", "مِلَّتِ", "نَا", "pron-1p", "مَجْرُورٌ بِفِي، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our creed»", "«dinimize»", punct=".", tags=[HJ, ID]),
  ]),
])
# ---------------------------------------------------------------- §11 حُجَّةٌ قَاطِعَةٌ
sen("s3", "And his answer was the answer of one proud of his religion, jealous for his belief and his conscience; he said:",
        "Onun cevabı, dinini övünçle taşıyan, inancı ve vicdanı üzerine titreyen birinin cevabı oldu; dedi ki:", [
  tok("فَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«and was» — kāna.", "«ve … oldu» — kâne.", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  noun_pron("جَوَابُهُ", "jawab", "جَوَابُ", "هُ", "pron-3ms", "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his answer» — the ism of kāna.", "«cevabı» — kâne'nin ismi.", tags=[KN, ID]),
  tok("جَوَابَ", "jawab", "noun", [KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«the answer of» — kāna's khabar, annexed.", "«cevabı» — kâne'nin haberi, muzâf."),
  mudaf_ilayh("فَخُورٍ", "fakhur", "«one proud»", "«övünen birinin»", tags=["sighat-mubalagha"]),
  tok("بِدِينِهِ", "din", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَدِينِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«of his religion»", "«diniyle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("دِينِ", "din", "noun"), pr3msi()]),
  tok("غَيُورٍ", "ghayur", "noun", [NA, "sighat-mubalagha"], "نَعْتٌ لِفَخُورٍ مَجْرُورٌ.", "«jealous» — a second naʿt.", "«kıskanç, titreyen» — ikinci sıfat."),
  tok("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«for»", "«üzerine»"),
  noun_pron("عَقِيدَتِهِ", "aqida", "عَقِيدَتِ", "هِ", "pron-3ms", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his belief»", "«inancı»", tags=[HJ, ID]),
  noun_pron("وَضَمِيرِهِ", "damir", "وَضَمِيرِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَضَمِيرِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and his conscience»", "«ve vicdanı»", punct="،", tags=[AT, ID]),
  qala(punct=":"),
])
sen("s4", "«Even though we hate it?» (7:88).", "«İstemesek de mi?» (7:88).", [
  *quran([
  tok("أَوَلَوْ", "law", "part", ["al-istifham", AT, SH], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَالْوَاوُ لِلْحَالِ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ — جَوَابُهُ مَحْذُوفٌ.", "«even if?» — the question hamza, the wāw of state, law.", "«… -sa da mı?» — inkârî istifham hemzesi, hâl vâvı, lev.", segments=[seg("أَ", "hamza-istifham", "part"), seg("وَ", "wa", "conj"), seg("لَوْ", "law", "part")]),
  tok("كُنَّا", "kana", "verb", [SH, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَنَا اسْمُهُ.", "«we were» — kāna with its ism نَا.", "«biz … idik» — kâne; nâ ismi.", segments=[seg("كُنْ", "kana", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("كَارِهِينَ", "karih", "noun", [KN, JS, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«hating [it]» — kāna's khabar, naṣb by the yāʾ.", "«istemeyenler» — kâne'nin haberi, yâ ile mansûb.", punct="."),
  ]),
])
sen("s5", "«We would have invented a lie against God if we returned to your creed after God had saved us from it» (7:89).",
        "«Allah bizi ondan kurtardıktan sonra dininize dönersek Allah'a karşı yalan uydurmuş oluruz» (7:89).", [
  *quran([
  tok("قَدِ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«indeed» — qad, kasra for the two sukūns.", "«gerçekten» — kad, iki sâkin için kesre."),
  tok("افْتَرَيْنَا", "iftara", "verb", [MB, "naqis-verbs", "form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ.", "«we would have invented» — built on sukūn before نَا, the doer.", "«uydurmuş oluruz» — nâ önünde sükûn üzere mebnî; nâ fâil.", segments=[seg("افْتَرَيْ", "iftara", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«against»", "«-e karşı»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«God»", "«Allah'a»"),
  maful_("كَذِبًا", "kadhib", "«a lie»", "«yalan»", tags=["masdar"]),
  tok("إِنْ", "in-shartiyya", "part", [SH], "حَرْفُ شَرْطٍ جَازِمٌ — وَجَوَابُهُ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«if» — the shart; its answer is shown by what precedes.", "«eğer» — şart edatı; cevabı öncesinden anlaşılır."),
  tok("عُدْنَا", "ada-return", "verb", [SH, "hollow-verbs"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَنَا فَاعِلٌ.", "«we returned» — the shart verb, in the place of jazm.", "«dönersek» — şart fiili, cezm mahallinde.", segments=[seg("عُدْ", "ada-return", "verb"), seg("نَا", "pron-1p", "pron")]),
  fi(), noun_pron("مِلَّتِكُمْ", "milla", "مِلَّتِ", "كُمْ", "pron-2mp", "مَجْرُورٌ بِفِي، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your creed»", "«dininize»", tags=[HJ, ID]),
  tok("بَعْدَ", "bada", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ إِلَى إِذْ.", "«after» — annexed to idh.", "«sonra» — iz'e muzâf."),
  tok("إِذْ", "idh", "part", [MF, ID], "ظَرْفٌ لِمَا مَضَى مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«when» — the ẓarf of the past, mudāf ilayh in place.", "«-dığı zaman» — mâzî zarfı, mahallen muzâfun ileyh."),
  tok("نَجَّانَا", "najja", "verb", [MB, "naqis-verbs", "form-ii-verbs"], "فِعْلٌ مَاضٍ، وَنَا مَفْعُولٌ بِهِ.", "«saved us»", "«bizi kurtardı»", segments=[seg("نَجَّا", "najja", "verb"), seg("نَا", "pron-1p", "pron")]),
  allah_fail(),
  prep_pron("مِنْهَا", "min", "هَا", "pron-3fs", "«from it»", "«ondan»", punct="."),
  ]),
])
sen("s6", "«And it is not for us to return to it unless God our Lord should will; our Lord encompasses all things in knowledge» (7:89).",
        "«Rabbimiz Allah dilemedikçe ona dönmemiz bize yakışmaz; Rabbimiz ilmiyle her şeyi kuşatmıştır» (7:89).", [
  *quran([
  tok("وَمَا", "ma-nafiya", "part", [AT, "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and not»", "«ve … değil»", segments=wa_("مَا", "ma-nafiya", "part")),
  tok("يَكُونُ", "kana", "verb", [KN, "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«is» — kāna's muḍāriʿ.", "«olur» — kâne'nin muzarisi."),
  prep_pron("لَنَا", "li", "نَا", "pron-1p", "«for us» — kāna's fronted khabar.", "«bize» — kâne'nin öne alınmış haberi.", tags=[KN]),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", KN], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ اسْمُ يَكُونُ.", "«that» — the clause is kāna's ism.", "«-memiz» — tevil edilen masdar kâne'nin ismi."),
  tok("نَعُودَ", "ada-return", "verb", ["an-masdariyya", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«we return» — naṣb by an.", "«dönmemiz» — en ile mansûb."),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«to it»", "«ona»"),
  tok("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except»", "«ancak, -medikçe»"),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "istithna"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مُسْتَثْنًى، أَوْ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ: إِلَّا وَقْتَ مَشِيئَةِ اللهِ.", "«that» — the clause is the mustathnā: «except [the time] God wills».", "«-mesi» — müstesnâ: Allah'ın dilemesi vakti dışında."),
  tok("يَشَاءَ", "shaa", "verb", ["an-masdariyya", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ.", "«should will»", "«dilemesi»"),
  allah_fail(),
  noun_pron("رَبُّنَا", "rabb", "رَبُّ", "نَا", "pron-1p", "نَعْتٌ لِلَفْظِ الْجَلَالَةِ مَرْفُوعٌ — أَوْ بَدَلٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our Lord» — a naʿt (or badal) of the Name.", "«Rabbimiz» — lafza-i celâlin sıfatı (veya bedeli).", tags=[NA, "badal", ID]),
  mazi("وَسِعَ", "wasia", "«encompasses»", "«kuşatmıştır»", tags=[MB, "mithal-verbs"], hidden=None),
  noun_pron("رَبُّنَا", "rabb", "رَبُّ", "نَا", "pron-1p", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our Lord» — the doer.", "«Rabbimiz» — fâil.", tags=[FL, ID]),
  maful_("كُلَّ", "kull", "«all»", "«her»", tags=[ID]), mudaf_ilayh("شَيْءٍ", "shay", "«things»", "«şeyi»"),
  tok("عِلْمًا", "ilm", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — مُحَوَّلٌ عَنِ الْفَاعِلِ: وَسِعَ عِلْمُهُ كُلَّ شَيْءٍ.", "«in knowledge» — the tamyīz, converted from the doer.", "«ilim bakımından» — fâilden dönüşmüş temyiz.", punct="."),
  ]),
])
sen("s7", "«In God we have placed our trust. Our Lord, decide between us and our people with the truth, for You are the best of deciders» (7:89).",
        "«Allah'a tevekkül ettik. Rabbimiz, bizimle kavmimiz arasında hak ile hükmet; Sen hükmedenlerin en hayırlısısın» (7:89).", [
  *quran([
  tok("عَلَى", "ala", "prep", [HJ, "taqdim-al-musnad"], "حَرْفُ جَرٍّ — وَتَقْدِيمُ الْجَارِّ وَالْمَجْرُورِ لِلِاخْتِصَاصِ.", "«in» — fronted for restriction: in God alone.", "«-e» — tahsis için öne alınmış."),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«God»", "«Allah'a»"),
  tok("تَوَكَّلْنَا", "tawakkala", "verb", ["form-v-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ.", "«we have placed our trust»", "«tevekkül ettik»", punct=".", segments=[seg("تَوَكَّلْ", "tawakkala", "verb"), seg("نَا", "pron-1p", "pron")]),
  noun_pron("رَبَّنَا", "rabb", "رَبَّ", "نَا", "pron-1p", "مُنَادًى مُضَافٌ مَنْصُوبٌ، حُذِفَ حَرْفُ النِّدَاءِ، وَنَا مُضَافٌ إِلَيْهِ.", "«our Lord» — the annexed munādā, its yā dropped.", "«Rabbimiz» — nida harfi hazfedilmiş muzâf münâdâ.", punct="،", tags=["vocative-munada", ID]),
  tok("افْتَحْ", "fataha", "verb", ["imperative-amr", "jawab-al-talab"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — وَالْفَتْحُ هُنَا الْحُكْمُ.", "«decide» — the imperative; fatḥ here is judgement.", "«hükmet» — emir; buradaki feth hüküm demektir."),
  noun_pron("بَيْنَنَا", "bayna", "بَيْنَ", "نَا", "pron-1p", "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«between us»", "«bizimle»", tags=[MF, ID]),
  tok("وَبَيْنَ", "bayna", "noun", [AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and between»", "«ve … arasında»", segments=wa_("بَيْنَ", "bayna", "noun")),
  noun_pron("قَوْمِنَا", "qawm", "قَوْمِ", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our people»", "«kavmimiz»", tags=[ID]),
  tok("بِالْحَقِّ", "haqq", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَقِّ مَجْرُورٌ.", "«with the truth»", "«hak ile»", segments=[seg("بِ", "bi", "prep"), seg("الْحَقِّ", "haqq", "noun")]),
  tok("وَأَنْتَ", "anta", "pron", [AT, MK], "الْوَاوُ لِلْحَالِ أَوْ لِلِاسْتِئْنَافِ، وَأَنْتَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and You» — the mubtadaʾ.", "«ve Sen» — mübtedâ.", segments=wa_("أَنْتَ", "anta", "pron")),
  tok("خَيْرُ", "khayr", "noun", [MK, ID, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — أَفْعَلُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ.", "«the best of» — the khabar; an elative without its hamza.", "«en hayırlısı» — haber; hemzesi düşmüş ism-i tafdîl."),
  tok("الْفَاتِحِينَ", "fatih", "noun", [ID, JS, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«deciders» — a sound plural, jarr by the yāʾ.", "«hükmedenlerin» — cem-i müzekker sâlim, yâ ile mecrûr.", punct="."),
  ]),
])
# ---------------------------------------------------------------- §12 بَلْ قَالُوا مِثْلَ مَا قَالَ الْأَوَّلُونَ
sen("s8", "But that did not profit them; rather they said the like of what the first ones had said:", "Fakat bu onlara fayda vermedi; aksine öncekilerin dediği gibi dediler:", [
  tok("فَلَمْ", "lam", "part", [AT, "lam-jazim"], "الْفَاءُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«but did not» — lam: it negates, puts in jazm and turns the tense.", "«fakat … -medi» — lem: nefy, cezm ve kalb harfi.", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam", "part")]),
  tok("يَنْفَعْهُمْ", "nafaa", "verb", ["lam-jazim", MB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَهُمْ مَفْعُولٌ بِهِ.", "«profit them» — jazm by lam, the sukūn its sign.", "«fayda vermedi» — lem ile meczûm, alâmeti sükûn.", segments=[seg("يَنْفَعْ", "nafaa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  ishara("ذٰلِكَ", "dhalika", "raf", "«that» — the doer.", "«bu» — fâil.", punct="،", tags=[FL]),
  tok("بَلْ", "bal", "part", [AT], "حَرْفُ إِضْرَابٍ وَابْتِدَاءٍ.", "«rather» — the particle of turning away.", "«aksine» — idrâb harfi."),
  qalu(punct=None),
  tok("مِثْلَ", "mithl", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ — أَوْ نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ.", "«the like of» — the object (or standing for the absolute object).", "«… gibisini» — mef'ûl (veya mef'ûl-i mutlak nâibi)."),
  tok("مَا", "ma-mawsula", "pron", [MW, ID], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — mudāf ilayh in place.", "«… şeyin» — mahallen muzâfun ileyh."),
  qala(punct=None, tags=[MW]),
  tok("الْأَوَّلُونَ", "awwal", "noun", [FL, JS, MW], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — صِلَةٌ.", "«the first ones» — the doer in the ṣila.", "«öncekiler» — sılada fâil.", punct=":"),
])
sen("s9", "«They said: You are only one of the bewitched» (26:185).", "«Dediler ki: Sen ancak büyülenmişlerdensin» (26:185).", [
  *quran([
  qalu(punct=None),
  tok("إِنَّمَا", "innama", "part", ["innama-kaffa", "qasr"], "إِنَّ الْمَكْفُوفَةُ بِمَا الزَّائِدَةِ — أَدَاةُ قَصْرٍ، لَا عَمَلَ لَهَا.", "«only» — inna stopped by mā: a tool of restriction, no government.", "«ancak» — mâ ile amelden kesilmiş inne: kasr edatı."),
  tok("أَنْتَ", "anta", "pron", [MK, "innama-kaffa"], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«you» — the mubtadaʾ.", "«sen» — mübtedâ."),
  tok("مِنَ", "min", "prep", [HJ, MK], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the phrase is the khabar.", "«-den» — câr-mecrûr haber."),
  jarr_salim("الْمُسَحَّرِينَ", "musahhar", "«the bewitched»", "«büyülenmişler»", punct=".", tags=["ism-maful", "form-ii-verbs"]),
  ]),
])
sen("s10", "«And you are nothing but a man like us, and we think you are surely one of the liars» (26:186).", "«Sen ancak bizim gibi bir insansın; biz seni kesinlikle yalancılardan sanıyoruz» (26:186).", [
  *quran([
  tok("وَمَا", "ma-nafiya", "part", [AT, "anwa-ma", "istithna-mufarragh"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ — بَطَلَ عَمَلُهَا بِإِلَّا.", "«and not» — mā, its work undone by illā.", "«ve … değil» — illâ ile ameli bozulmuş mâ.", segments=wa_("مَا", "ma-nafiya", "part")),
  tok("أَنْتَ", "anta", "pron", [MK], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«you» — the mubtadaʾ.", "«sen» — mübtedâ."),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh"], "أَدَاةُ حَصْرٍ — اسْتِثْنَاءٌ مُفَرَّغٌ.", "«but» — the emptied exception.", "«ancak» — müferrağ istisnâ."),
  tok("بَشَرٌ", "bashar", "noun", [MK], "خَبَرٌ مَرْفُوعٌ.", "«a man» — the khabar.", "«bir insan» — haber."),
  noun_pron("مِثْلُنَا", "mithl", "مِثْلُ", "نَا", "pron-1p", "نَعْتٌ لِبَشَرٍ مَرْفُوعٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«like us» — a naʿt of the man.", "«bizim gibi» — beşer'in sıfatı.", tags=[NA, ID]),
  tok("وَإِنْ", "in-mukhaffafa", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَإِنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ مُهْمَلَةٌ — وَاللَّامُ بَعْدَهَا فَارِقَةٌ.", "«and surely» — the lightened inn, its lām the distinguishing lām.", "«ve gerçekten» — tahfif edilmiş inne; ardındaki lâm fârika.", segments=wa_("إِنْ", "in-mukhaffafa", "part")),
  tok("نَظُنُّكَ", "zanna", "verb", ["zanna-wa-akhawatuha", "mafulayn", "doubled-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ، وَالْكَافُ مَفْعُولٌ أَوَّلُ.", "«we think you» — ẓanna; the kāf its first object.", "«seni sanıyoruz» — zanne; kâf birinci mef'ûl.", segments=[seg("نَظُنُّ", "zanna", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("لَمِنَ", "min", "prep", [HJ, "mafulayn"], "اللَّامُ الْفَارِقَةُ، وَمِنْ حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مَفْعُولٌ ثَانٍ.", "«surely among» — the distinguishing lām; the phrase is the second object.", "«kesinlikle … -den» — fârika lâmı; câr-mecrûr ikinci mef'ûl.", segments=[seg("لَ", "lam-ibtida", "part"), seg("مِنَ", "min", "prep")]),
  jarr_salim("الْكَاذِبِينَ", "kadhib-liar", "«the liars»", "«yalancılar»", punct=".", tags=["ism-fail"]),
  ]),
])
sen("s11", "«So make pieces of the sky fall on us, if you are of the truthful» (26:187).", "«Eğer doğru söyleyenlerdensen üzerimize gökten parçalar düşür» (26:187).", [
  *quran([
  tok("فَأَسْقِطْ", "asqata", "verb", [AT, "imperative-amr", MB, "form-iv-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَأَسْقِطْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«so make fall» — the imperative.", "«o hâlde düşür» — emir.", segments=[seg("فَ", "fa", "conj"), seg("أَسْقِطْ", "asqata", "verb")]),
  prep_pron("عَلَيْنَا", "ala", "نَا", "pron-1p", "«on us»", "«üzerimize»"),
  maful_("كِسَفًا", "kisaf", "«pieces»", "«parçalar»", tags=["jam-taksir"]),
  tok("مِنَ", "min", "prep", [HJ, NA], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِكِسَفًا.", "«of» — the phrase qualifies the pieces.", "«-den» — kisef'in sıfatı."),
  majrur("السَّمَاءِ", "sama", "«the sky»", "«gök»"),
  tok("إِنْ", "in-shartiyya", "part", [SH], "حَرْفُ شَرْطٍ جَازِمٌ — جَوَابُهُ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«if»", "«eğer»"),
  tok("كُنْتَ", "kana", "verb", [SH, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ اسْمُهُ.", "«you are» — kāna in the place of jazm; the tāʾ its ism.", "«isen» — cezm mahallinde kâne; tâ ismi.", segments=[seg("كُنْ", "kana", "verb"), seg("تَ", "pron-2ms", "pron")]),
  tok("مِنَ", "min", "prep", [HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«of» — the phrase is kāna's khabar.", "«-den» — kâne'nin haberi."),
  jarr_salim("الصَّادِقِينَ", "sadiq", "«the truthful»", "«doğru söyleyenler»", punct=".", tags=["ism-fail"]),
  ]),
])
# ---------------------------------------------------------------- §13 عَاقِبَةُ أُمَّةٍ كَذَّبَتْ نَبِيَّهَا
sen("s12", "And the end was one — the end of every nation that called its prophet a liar and was ungrateful for God's blessing:",
        "Ve âkıbet bir oldu: peygamberini yalanlayan ve Allah'ın nimetine nankörlük eden her ümmetin âkıbeti:", [
  tok("وَكَانَتِ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and was» — kāna; its tāʾ takes a kasra before the sukūn.", "«ve … oldu» — kâne; tâ'sı iki sâkin için kesre aldı.", segments=wa_("كَانَتِ", "kana", "verb")),
  tok("الْعَاقِبَةُ", "aqiba", "noun", [KN], "اسْمُ كَانَ مَرْفُوعٌ.", "«the end» — kāna's ism.", "«âkıbet» — kâne'nin ismi."),
  tok("وَاحِدَةً", "wahid", "noun", [KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«one» — kāna's khabar.", "«bir» — kâne'nin haberi.", punct="،"),
  tok("عَاقِبَةَ", "aqiba", "noun", ["badal", ID], "بَدَلٌ مِنْ وَاحِدَةً مَنْصُوبٌ، مُضَافٌ.", "«the end of» — a badal of «one».", "«âkıbeti» — «bir»den bedel."),
  mudaf_ilayh("كُلِّ", "kull", "«every»", "«her»", tags=[ID]), mudaf_ilayh("أُمَّةٍ", "umma", "«nation»", "«ümmet»"),
  mazi_ta("كَذَّبَتْ", "kadhdhaba", "«called a liar»", "«yalanlayan»", tags=[NA, MB, "form-ii-verbs", "jumla-sifa"]),
  noun_pron("نَبِيَّهَا", "nabi", "نَبِيَّ", "هَا", "pron-3fs", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ صِفَةٌ لِأُمَّةٍ.", "«its prophet» — the object; the clause qualifies the nation.", "«peygamberini» — mef'ûl; cümle ümmet'in sıfatı.", tags=[MB, ID]),
  mazi_ta("وَكَفَرَتْ", "kafara", "«and was ungrateful»", "«ve nankörlük eden»", tags=[AT], wa=True),
  tok("بِنِعْمَةِ", "nima", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَنِعْمَةِ مَجْرُورٌ، مُضَافٌ.", "«for the blessing of»", "«nimetine»", segments=[seg("بِ", "bi", "prep"), seg("نِعْمَةِ", "nima", "noun")]),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»", punct=":"),
])
sen("s13", "«So the earthquake seized them, and they lay in their dwelling, fallen on their faces» (7:91).", "«Derken onları o sarsıntı yakaladı da yurtlarında diz üstü çöküp kaldılar» (7:91).", [
  *quran([
  tok("فَأَخَذَتْهُمُ", "akhadha", "verb", [AT, MB], "الْفَاءُ عَاطِفَةٌ، وَأَخَذَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَهُمْ مَفْعُولٌ بِهِ، حُرِّكَتْ مِيمُهُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«so seized them» — the object هُمْ, its mīm given a ḍamma.", "«derken onları yakaladı» — hüm mef'ûl; mîm'i iki sâkin için damme aldı.", segments=[seg("فَ", "fa", "conj"), seg("أَخَذَتْ", "akhadha", "verb"), seg("هُمُ", "pron-3mp", "pron")]),
  tok("الرَّجْفَةُ", "rajfa", "noun", [FL], "فَاعِلٌ مَرْفُوعٌ.", "«the earthquake» — the doer.", "«sarsıntı» — fâil."),
  tok("فَأَصْبَحُوا", "asbaha", "verb", [AT, KN, "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ، وَأَصْبَحُوا فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«and they became» — a sister of kāna; the wāw its ism.", "«ve … oldular» — kâne kardeşi; vâv ismi.", segments=[seg("فَ", "fa", "conj"), seg("أَصْبَحُوا", "asbaha", "verb")]),
  fi(), noun_pron("دَارِهِمْ", "dar", "دَارِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِفِي، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«their dwelling»", "«yurtlarında»", tags=[HJ, ID]),
  tok("جَاثِمِينَ", "jathim", "noun", [KN, JS, "ism-fail"], "خَبَرُ أَصْبَحَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«fallen on their faces» — aṣbaḥa's khabar, naṣb by the yāʾ.", "«diz üstü çökmüşler» — asbaha'nın haberi, yâ ile mansûb.", punct="."),
  ]),
])
sen("s14", "«Those who called Shuʿayb a liar — as though they had never dwelt there; those who called Shuʿayb a liar — they were the losers» (7:92).",
        "«Şuayb'ı yalanlayanlar sanki orada hiç oturmamış gibi oldular; Şuayb'ı yalanlayanlar, asıl hüsrana uğrayanlar onlar oldu» (7:92).", [
  *quran([
  tok("الَّذِينَ", "alladhina", "pron", [MW, MK], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«those who» — the mubtadaʾ.", "«… olanlar» — mübtedâ."),
  mazi_pl("كَذَّبُوا", "kadhdhaba", "«called a liar»", "«yalanladılar»", tags=[MW, MB, "form-ii-verbs"]),
  maful_("شُعَيْبًا", "shuayb", "«Shuʿayb»", "«Şuayb'ı»"),
  tok("كَأَنْ", "kaan", "part", [IW, MK, "tashbih"], "كَأَنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ — وَالْجُمْلَةُ بَعْدَهَا خَبَرُهَا، وَالْجُمْلَةُ كُلُّهَا خَبَرُ الْمُبْتَدَإِ.", "«as though» — the lightened ka-anna; its ism the dropped pronoun of the matter.", "«sanki» — tahfif edilmiş keenne; ismi mahzûf şe'n zamiri."),
  tok("لَمْ", "lam", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-memiş»"),
  tok("يَغْنَوْا", "ghaniya-dwell", "verb", ["lam-jazim", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«had dwelt» — jazm by the dropped nūn.", "«oturmuş» — nûn hazfiyle meczûm."),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«there»", "«orada»"),
  tok("الَّذِينَ", "alladhina", "pron", [MW, MK], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«those who» — the mubtadaʾ.", "«… olanlar» — mübtedâ."),
  mazi_pl("كَذَّبُوا", "kadhdhaba", "«called a liar»", "«yalanladılar»", tags=[MW, MB, "form-ii-verbs"]),
  maful_("شُعَيْبًا", "shuayb", "«Shuʿayb»", "«Şuayb'ı»"),
  tok("كَانُوا", "kana", "verb", [KN, MK, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ.", "«they were» — kāna; the clause is the khabar.", "«oldular» — kâne; cümle mübtedânın haberi.", segments=[seg("كَانُ", "kana", "verb"), seg("وا", "pron-3mp", "pron")]),
  tok("هُمُ", "hum", "pron", ["damir-fasl"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ، حُرِّكَ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«they» — the pronoun of separation.", "«onlar» — fasıl zamiri."),
  tok("الْخَاسِرِينَ", "khasir", "noun", [KN, JS, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the losers» — kāna's khabar, naṣb by the yāʾ.", "«hüsrana uğrayanlar» — kâne'nin haberi, yâ ile mansûb.", punct="."),
  ]),
])
# ---------------------------------------------------------------- §14 بَلَّغَ الرِّسَالَةَ وَأَدَّى الْأَمَانَةَ
sen("s15", "And Shuʿayb's case was the case of every prophet who delivered the message, discharged the trust and established the proof:",
        "Şuayb'ın hâli, risaleti tebliğ eden, emaneti yerine getiren ve hücceti ikame eden her peygamberin hâli oldu:", [
  kana(),
  tok("شَأْنُ", "shan", "noun", [KN, ID], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ.", "«the case of» — kāna's ism.", "«hâli» — kâne'nin ismi."),
  tok("شُعَيْبٍ", "shuayb", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Shuʿayb»", "«Şuayb'ın»"),
  tok("شَأْنَ", "shan", "noun", [KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«the case of» — kāna's khabar.", "«hâli» — kâne'nin haberi."),
  mudaf_ilayh("كُلِّ", "kull", "«every»", "«her»", tags=[ID]), mudaf_ilayh("نَبِيٍّ", "nabi", "«prophet»", "«peygamberin»"),
  mazi("بَلَّغَ", "ballagha", "«delivered»", "«tebliğ etti»", tags=[NA, MB, "form-ii-verbs", "jumla-sifa"]),
  maful_("الرِّسَالَةَ", "risala", "«the message»", "«risaleti»"),
  mazi("وَأَدَّى", "adda", "«and discharged»", "«ve yerine getirdi»", tags=[AT, MB, "form-ii-verbs", "naqis-verbs"], wa=True),
  maful_("الْأَمَانَةَ", "amana", "«the trust»", "«emaneti»", punct="،"),
  mazi("وَأَقَامَ", "aqama", "«and established»", "«ve ikame etti»", tags=[AT, MB, "form-iv-verbs", "hollow-verbs"], wa=True),
  maful_("الْحُجَّةَ", "hujja", "«the proof»", "«hücceti»", punct=":"),
])
sen("s16", "«So he turned away from them and said: O my people, I delivered to you the messages of my Lord and counselled you; how then should I grieve for an unbelieving people?» (7:93).",
        "«Onlardan yüz çevirdi ve dedi ki: Ey kavmim, Rabbimin risaletlerini size tebliğ ettim ve size öğüt verdim; kâfir bir kavme nasıl üzüleyim?» (7:93).", [
  *quran([
  tok("فَتَوَلَّى", "tawalla", "verb", [AT, "form-v-verbs", "naqis-verbs"], "الْفَاءُ عَاطِفَةٌ، وَتَوَلَّى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«so he turned away»", "«yüz çevirdi»", segments=[seg("فَ", "fa", "conj"), seg("تَوَلَّى", "tawalla", "verb")]),
  prep_pron("عَنْهُمْ", "an", "هُمْ", "pron-3mp", "«from them»", "«onlardan»"),
  qala("وَقَالَ", punct=":", wa=True),
  *ya_qawmi(),
  tok("لَقَدْ", "qad", "part", ["qad-harf", TW], "اللَّامُ لِلْقَسَمِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«surely, indeed» — the oath's lām and qad.", "«gerçekten» — kasem lâmı ve kad.", segments=[seg("لَ", "lam-qasam", "part"), seg("قَدْ", "qad", "part")]),
  tok("أَبْلَغْتُكُمْ", "ablagha", "verb", [MB, "mafulayn", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَكُمْ مَفْعُولٌ أَوَّلُ.", "«I delivered to you» — the tāʾ the doer, كُمْ the first object.", "«size tebliğ ettim» — tâ fâil, küm birinci mef'ûl.", segments=[seg("أَبْلَغْ", "ablagha", "verb"), seg("تُ", "pron-1s", "pron"), seg("كُمْ", "pron-2mp", "pron")]),
  tok("رِسَالَاتِ", "risala", "noun", [MB, "mafulayn", ID, "jam-muannath-salim"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ، مُضَافٌ.", "«the messages of» — the second object; a sound feminine plural takes a kasra for naṣb.", "«risaletlerini» — ikinci mef'ûl; cem-i müennes sâlim nasbı kesre ile."),
  tok("رَبِّي", "rabb", "noun", [ID, "ya-al-mutakallim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord»", "«Rabbimin»", segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("وَنَصَحْتُ", "nasaha", "verb", [AT], "الْوَاوُ عَاطِفَةٌ، وَنَصَحْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I counselled»", "«ve öğüt verdim»", segments=[seg("وَ", "wa", "conj"), seg("نَصَحْ", "nasaha", "verb"), seg("تُ", "pron-1s", "pron")]),
  prep_pron("لَكُمْ", "li", "كُمْ", "pron-2mp", "«you»", "«size»"),
  tok("فَكَيْفَ", "kayfa", "part", [AT, "al-istifham", "adawat-al-tasawwur", "hal"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«how then» — the question noun as ḥāl.", "«o hâlde nasıl» — hâl mahallinde istifham ismi.", segments=[seg("فَ", "fa", "conj"), seg("كَيْفَ", "kayfa", "part")]),
  tok("آسَى", "asiya", "verb", ["mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«should I grieve» — rafʿ by an estimated ḍamma on the alif.", "«üzüleyim» — elif üzerinde takdirî damme ile merfû."),
  tok("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«for»", "«-e»"),
  majrur("قَوْمٍ", "qawm", "«a people»", "«bir kavme»"),
  jarr_salim("كَافِرِينَ", "kafir", "«unbelieving»", "«kâfir»", punct=".", tags=[NA, "ism-fail"], pre_ar="نَعْتٌ مَجْرُورٌ"),
  ]),
])

CAND = {
 "lamma": G("lamma", "لَمَّا", None, "part", "when — the ẓarf that joins a cause to its sequel (lammā al-ḥīniyya)", "lemmâ — -ınca; sebebi sonucuna bağlayan zarf", 2),
 "inqataa": G("inqataa", "اِنْقَطَعَ", "ق ط ع", "verb", "to be cut off, to cease (Form VII)", "kesilmek, tükenmek (infiâl)", 3),
 "hujja": G("hujja", "حُجَّة", "ح ج ج", "noun", "an argument, a proof", "hüccet, delil", 2, plural="حُجَج"),
 "atlaqa": G("atlaqa", "أَطْلَقَ", "ط ل ق", "verb", "to loose, to let fly; to set free (Form IV)", "salmak, atmak; serbest bırakmak (if'âl)", 3),
 "sahm": G("sahm", "سَهْم", "س ه م", "noun", "an arrow", "ok", 1, plural="سِهَام"),
 "akhir-last": G("akhir-last", "أَخِير", "أ خ ر", "noun", "last, final", "son, sonuncu", 1),
 "mutakabbir": G("mutakabbir", "مُتَكَبِّر", "ك ب ر", "noun", "proud, arrogant (ism fāʿil of تَكَبَّرَ)", "kibirli, büyüklük taslayan", 3),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation, a community", "ümmet", 1, plural="أُمَم"),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "nebi, peygamber", 1, plural="أَنْبِيَاء"),
 "atba": G("atba", "أَتْبَاع", "ت ب ع", "noun", "followers (plural of تَابِع)", "tâbiler, uyanlar", 3),
 "mala-chiefs": G("mala-chiefs", "مَلَأ", "م ل أ", "noun", "the chiefs, the notables of a people", "mele' — ileri gelenler", 3),
 "istakbara": G("istakbara", "اِسْتَكْبَرَ", "ك ب ر", "verb", "to be proud, to disdain (Form X)", "büyüklük taslamak (istif'âl)", 2),
 "akhraja": G("akhraja", "أَخْرَجَ", "خ ر ج", "verb", "to drive out, to bring out (Form IV)", "çıkarmak (if'âl)", 1),
 "lam-qasam": G("lam-qasam", "لَ (لَامُ الْقَسَمِ)", None, "part", "the lām of the oath's answer — before the heavy nūn or قَدْ", "kasem lâmı — şeddeli nûn veya kad önünde", 4),
 "qarya": G("qarya", "قَرْيَة", "ق ر ي", "noun", "a town, a village", "kasaba, köy", 1, plural="قُرًى"),
 "aw": G("aw", "أَوْ", None, "part", "or", "veya, ya da", 1),
 "ada-return": G("ada-return", "عَادَ", "ع و د", "verb", "to return (عَادَ إِلَى / فِي)", "dönmek", 1),
 "milla": G("milla", "مِلَّة", "م ل ل", "noun", "a creed, a religious community", "millet — din, inanç yolu", 3, plural="مِلَل"),
 "jawab": G("jawab", "جَوَاب", "ج و ب", "noun", "an answer", "cevap", 1, plural="أَجْوِبَة"),
 "fakhur": G("fakhur", "فَخُور", "ف خ ر", "noun", "proud, boastful (a ṣīghat mubālagha)", "övünen, iftihar eden (mübalağa sîgası)", 4),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1, plural="أَدْيَان"),
 "ghayur": G("ghayur", "غَيُور", "غ ي ر", "noun", "jealous, zealous for (a ṣīghat mubālagha)", "kıskanç, gayretli (mübalağa sîgası)", 4),
 "aqida": G("aqida", "عَقِيدَة", "ع ق د", "noun", "a belief, a creed", "akide, inanç", 2, plural="عَقَائِد"),
 "damir": G("damir", "ضَمِير", "ض م ر", "noun", "conscience; a pronoun", "vicdan; zamir", 2, plural="ضَمَائِر"),
 "karih": G("karih", "كَارِه", "ك ر ه", "noun", "hating, unwilling (ism fāʿil of كَرِهَ)", "istemeyen, hoşlanmayan", 2),
 "kadhib": G("kadhib", "كَذِب", "ك ذ ب", "noun", "a lie, lying", "yalan", 1),
 "najja": G("najja", "نَجَّى", "ن ج و", "verb", "to save, to rescue (Form II)", "kurtarmak (tef'îl)", 2),
 "bada": G("bada", "بَعْدَ", "ب ع د", "noun", "after (a ẓarf)", "sonra (zarf)", 1),
 "wasia": G("wasia", "وَسِعَ", "و س ع", "verb", "to encompass, to be wide enough for (وَسِعَ يَسَعُ)", "kuşatmak, kapsamak (vesia yeseu)", 3),
 "fataha": G("fataha", "فَتَحَ", "ف ت ح", "verb", "to open; to decide, to judge between", "açmak; hükmetmek", 1),
 "fatih": G("fatih", "فَاتِح", "ف ت ح", "noun", "one who opens, who decides (ism fāʿil of فَتَحَ)", "açan, hükmeden", 2),
 "bal": G("bal", "بَلْ", None, "part", "rather, nay — the particle of iḍrāb", "bilakis, aksine — idrâb harfi", 2),
 "mithl": G("mithl", "مِثْل", "م ث ل", "noun", "the like of, similar to", "benzer, gibi", 1),
 "awwal": G("awwal", "أَوَّل", "أ و ل", "noun", "first", "ilk, birinci", 1),
 "musahhar": G("musahhar", "مُسَحَّر", "س ح ر", "noun", "bewitched (ism mafʿūl of سَحَّرَ)", "büyülenmiş", 3),
 "bashar": G("bashar", "بَشَر", "ب ش ر", "noun", "a human being, mankind", "beşer, insan", 1),
 "in-mukhaffafa": G("in-mukhaffafa", "إِنْ (الْمُخَفَّفَة)", None, "part", "the lightened inn — إِنَّ without its shadda; the lām after it tells it from the negating إِنْ", "tahfif edilmiş inne — şeddesiz inne; ardındaki lâm onu nefiy in'inden ayırır", 5),
 "zanna": G("zanna", "ظَنَّ", "ظ ن ن", "verb", "to think, to suppose (two objects)", "sanmak, zannetmek (iki mef'ûllü)", 2),
 "kadhib-liar": G("kadhib-liar", "كَاذِب", "ك ذ ب", "noun", "a liar (ism fāʿil of كَذَبَ)", "yalancı", 1),
 "asqata": G("asqata", "أَسْقَطَ", "س ق ط", "verb", "to make fall, to drop (Form IV)", "düşürmek (if'âl)", 2),
 "kisaf": G("kisaf", "كِسَف", "ك س ف", "noun", "pieces, fragments (plural of كِسْفَة)", "parçalar", 4),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "the sky, heaven", "gök, semâ", 1, plural="سَمَاوَات"),
 "sadiq": G("sadiq", "صَادِق", "ص د ق", "noun", "truthful (ism fāʿil of صَدَقَ)", "doğru sözlü, sâdık", 1),
 "wahid": G("wahid", "وَاحِد", "و ح د", "noun", "one, single", "bir, tek", 1),
 "kadhdhaba": G("kadhdhaba", "كَذَّبَ", "ك ذ ب", "verb", "to call a liar, to deny (Form II)", "yalanlamak (tef'îl)", 1),
 "kafara": G("kafara", "كَفَرَ", "ك ف ر", "verb", "to disbelieve; to be ungrateful (كَفَرَ بِ)", "inkâr etmek; nankörlük etmek", 1),
 "nima": G("nima", "نِعْمَة", "ن ع م", "noun", "a blessing, a favour", "nimet", 1, plural="نِعَم"),
 "akhadha": G("akhadha", "أَخَذَ", "أ خ ذ", "verb", "to take, to seize", "almak, yakalamak", 1),
 "rajfa": G("rajfa", "رَجْفَة", "ر ج ف", "noun", "an earthquake, a violent tremor", "sarsıntı, zelzele", 3),
 "asbaha": G("asbaha", "أَصْبَحَ", "ص ب ح", "verb", "to become (a sister of كَانَ); to enter the morning (Form IV)", "olmak (kâne kardeşi); sabaha girmek (if'âl)", 2),
 "dar": G("dar", "دَار", "د و ر", "noun", "a house, a dwelling", "ev, yurt", 1, plural="دِيَار"),
 "jathim": G("jathim", "جَاثِم", "ج ث م", "noun", "fallen prone, crouched motionless (ism fāʿil of جَثَمَ)", "diz üstü çökmüş, yere kapanmış", 4),
 "kaan": G("kaan", "كَأَنْ (الْمُخَفَّفَة)", None, "part", "the lightened ka-anna — its ism the dropped pronoun of the matter", "tahfif edilmiş keenne — ismi mahzûf şe'n zamiri", 5),
 "ghaniya-dwell": G("ghaniya-dwell", "غَنِيَ", "غ ن ي", "verb", "to dwell, to live in a place (غَنِيَ بِالْمَكَانِ); to be rich", "bir yerde oturmak; zengin olmak", 4),
 "hum": G("hum", "هُمْ", None, "pron", "they (masculine)", "onlar", 1),
 "khasir": G("khasir", "خَاسِر", "خ س ر", "noun", "a loser (ism fāʿil of خَسِرَ)", "hüsrana uğrayan, zarar eden", 2),
 "ballagha": G("ballagha", "بَلَّغَ", "ب ل غ", "verb", "to convey, to deliver (a message) (Form II)", "tebliğ etmek, ulaştırmak (tef'îl)", 2),
 "risala": G("risala", "رِسَالَة", "ر س ل", "noun", "a message, a mission; a letter", "risalet, mesaj; mektup", 1, plural="رِسَالَات"),
 "adda": G("adda", "أَدَّى", "أ د ي", "verb", "to discharge, to fulfil, to render (Form II)", "edâ etmek, yerine getirmek (tef'îl)", 3),
 "amana": G("amana", "أَمَانَة", "أ م ن", "noun", "a trust", "emanet", 2),
 "aqama": G("aqama", "أَقَامَ", "ق و م", "verb", "to set up, to establish; to stay (Form IV)", "ikame etmek, dikmek; kalmak (if'âl)", 2),
 "tawalla": G("tawalla", "تَوَلَّى", "و ل ي", "verb", "to turn away (تَوَلَّى عَنْ); to take charge of (Form V)", "yüz çevirmek; üstlenmek (tefa''ul)", 3),
 "ablagha": G("ablagha", "أَبْلَغَ", "ب ل غ", "verb", "to convey, to deliver to (two objects) (Form IV)", "ulaştırmak, tebliğ etmek (iki mef'ûllü; if'âl)", 2),
 "nasaha": G("nasaha", "نَصَحَ", "ن ص ح", "verb", "to counsel, to advise sincerely (نَصَحَ لَهُ)", "nasihat etmek, öğüt vermek", 2),
 "asiya": G("asiya", "أَسِيَ", "أ س و", "verb", "to grieve (أَسِيَ عَلَى، يَأْسَى)", "üzülmek, kederlenmek", 4),
 "kafir": G("kafir", "كَافِر", "ك ف ر", "noun", "unbelieving; an unbeliever (ism fāʿil of كَفَرَ)", "kâfir, inkârcı", 1),
 "an": G("an", "عَنْ", None, "prep", "from, away from; about", "-den, hakkında", 1),
 "idh": G("idh", "إِذْ", None, "part", "when (of the past) — a ẓarf built on sukūn", "-dığı zaman (geçmiş) — sükûn üzere mebnî zarf", 2),
 "kayfa": G("kayfa", "كَيْفَ", None, "part", "how?", "nasıl?", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except, but", "ancak, hariç", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "inqataa", _sg.derived(_sg.B7, _sg.W7, "َ", "اِنْقَطَع", "نْقَطِع", "اِنْقَطِع", "اِنْقِطَاع", "مُنْقَطِع", None, None, None, "اِنْقَطَعَ يَنْقَطِعُ: زَالَ وَانْتَهَى — بَابُ الِانْفِعَالِ، مُطَاوِعُ قَطَعَ"))
put_morph(mo, "atlaqa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَطْلَق", "طْلِق", "أَطْلِق", "إِطْلَاق", "مُطْلِق", "مُطْلَق", "أُطْلِقَ", "يُطْلَقُ", "أَطْلَقَ يُطْلِقُ: أَرْسَلَ وَخَلَّى — بَابُ الْإِفْعَالِ"))
put_morph(mo, "istakbara", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَكْبَر", "سْتَكْبِر", "اِسْتَكْبِر", "اِسْتِكْبَار", "مُسْتَكْبِر", None, None, None, "اِسْتَكْبَرَ يَسْتَكْبِرُ: تَعَظَّمَ — بَابُ الِاسْتِفْعَالِ"))
put_morph(mo, "akhraja", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَخْرَج", "خْرِج", "أَخْرِج", "إِخْرَاج", "مُخْرِج", "مُخْرَج", "أُخْرِجَ", "يُخْرَجُ", "أَخْرَجَ يُخْرِجُ — بَابُ الْإِفْعَالِ، مُتَعَدِّي خَرَجَ"))
put_morph(mo, "ada-return", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "عَاد", "عُد", "عُود", "عُد", "عُود", "عُد", "عَوْد", "عَائِد", None, None, None, "لَازِمٌ، يَتَعَدَّى بِإِلَى أَوْ فِي: عَادَ يَعُودُ، عُدْتُ — الْعَيْنُ وَاوٌ"))
put_morph(mo, "kadhdhaba", _sg.derived(_sg.B2, _sg.W2, "ُ", "كَذَّب", "كَذِّب", "كَذِّب", "تَكْذِيب", "مُكَذِّب", "مُكَذَّب", "كُذِّبَ", "يُكَذَّبُ", "كَذَّبَ يُكَذِّبُ: نَسَبَ إِلَى الْكَذِبِ — بَابُ التَّفْعِيلِ"))
put_morph(mo, "kafara", _sg.sound1("nasara", "كَفَر", "كْفُر", "اُكْفُر", "كُفْر", "كَافِر", "مَكْفُور", "كُفِرَ", "يُكْفَرُ", "كَفَرَ يَكْفُرُ: جَحَدَ — بَابُ نَصَرَ؛ كَفَرَ بِالنِّعْمَةِ: جَحَدَهَا"))
put_morph(mo, "asqata", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَسْقَط", "سْقِط", "أَسْقِط", "إِسْقَاط", "مُسْقِط", "مُسْقَط", "أُسْقِطَ", "يُسْقَطُ", "أَسْقَطَ يُسْقِطُ: جَعَلَهُ يَسْقُطُ — بَابُ الْإِفْعَالِ"))
put_morph(mo, "asbaha", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَصْبَح", "صْبِح", "أَصْبِح", "إِصْبَاح", "مُصْبِح", None, None, None, "أَصْبَحَ يُصْبِحُ: دَخَلَ فِي الصَّبَاحِ؛ وَمِنْ أَخَوَاتِ كَانَ: صَارَ — بَابُ الْإِفْعَالِ"))
put_morph(mo, "ballagha", _sg.derived(_sg.B2, _sg.W2, "ُ", "بَلَّغ", "بَلِّغ", "بَلِّغ", "تَبْلِيغ", "مُبَلِّغ", "مُبَلَّغ", "بُلِّغَ", "يُبَلَّغُ", "بَلَّغَ يُبَلِّغُ: أَوْصَلَ — بَابُ التَّفْعِيلِ"))
put_morph(mo, "ablagha", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَبْلَغ", "بْلِغ", "أَبْلِغ", "إِبْلَاغ", "مُبْلِغ", "مُبْلَغ", "أُبْلِغَ", "يُبْلَغُ", "أَبْلَغَ يُبْلِغُ: أَوْصَلَ — بَابُ الْإِفْعَالِ، يَتَعَدَّى إِلَى مَفْعُولَيْنِ"))
put_morph(mo, "nasaha", _sg.sound1("fataha", "نَصَح", "نْصَح", "اِنْصَح", "نُصْح", "نَاصِح", "مَنْصُوح", "نُصِحَ", "يُنْصَحُ", "نَصَحَ يَنْصَحُ، نَصَحَ لَهُ: أَخْلَصَ لَهُ الْقَوْلَ — بَابُ فَتَحَ"))
put_morph(mo, "akhadha", _sg.sound1("nasara", "أَخَذ", "أْخُذ", "خُذ", "أَخْذ", "آخِذ", "مَأْخُوذ", "أُخِذَ", "يُؤْخَذُ", "أَخَذَ يَأْخُذُ — بَابُ نَصَرَ، مَهْمُوزُ الْفَاءِ؛ الْأَمْرُ خُذْ بِحَذْفِ الْهَمْزَةِ"))
put_morph(mo, "najja", _sg.derived_naqis("مِنْ بَابِ التَّفْعِيلِ", "فَعَّلَ يُفَعِّلُ", "ُ", "نَجَّ", "نَجّ", "i", "نَجّ", "تَنْجِيَة", "مُنَجٍّ (الْمُنَجِّي)", "مُنَجًّى (الْمُنَجَّى)", "نُجِّيَ", "يُنَجَّى", note="نَجَّى يُنَجِّي: خَلَّصَ — بَابُ التَّفْعِيلِ، نَاقِصٌ"))
put_morph(mo, "tawalla", _sg.derived_naqis("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَوَلَّ", "تَوَلّ", "a", "تَوَلّ", "تَوَلٍّ (التَّوَلِّي)", "مُتَوَلٍّ (الْمُتَوَلِّي)", "مُتَوَلًّى", "تُوُلِّيَ", "يُتَوَلَّى", note="تَوَلَّى عَنْهُ يَتَوَلَّى: أَعْرَضَ — بَابُ التَّفَعُّلِ، نَاقِصٌ"))
put_morph(mo, "fataha", _sg.sound1("fataha", "فَتَح", "فْتَح", "اِفْتَح", "فَتْح", "فَاتِح", "مَفْتُوح", "فُتِحَ", "يُفْتَحُ", "فَتَحَ يَفْتَحُ — بَابُ فَتَحَ؛ فَتَحَ بَيْنَهُمْ: حَكَمَ"))
put_morph(mo, "wasia", _sg.entry(_sg.BABS["samia"][0] + " — مِثَالٌ وَاوِيٌّ", _sg.BABS["samia"][1], "سَعَة", "وَاسِع", _sg.mazi14("وَسِع"), _sg.mudari14("َ", "سَع"), _sg.amr_attach("سَع"), "يَسَعَ", "يَسَعْ", "تَسَعْ", "مَوْسُوع", "وُسِعَ", "يُوسَعُ", "وَسِعَ يَسَعُ: أَحَاطَ بِهِ وَاتَّسَعَ لَهُ — مِثَالٌ وَاوِيٌّ مِنْ بَابِ سَمِعَ، تَسْقُطُ وَاوُهُ فِي الْمُضَارِعِ"))
put_morph(mo, "asiya", _sg.entry(_sg.BABS["samia"][0] + " — نَاقِصٌ يَائِيٌّ مَهْمُوزُ الْفَاءِ", _sg.BABS["samia"][1], "أَسًى", "آسٍ (الْآسِي)", _sg.mazi_naqis_kasra("أَسِ", "أَسُوا"), _sg.mudari_naqis("َ", "أْس", "a"), _sg.amr_naqis("اِئْس", "a"), "يَأْسَى", "يَأْسَ", "تَأْسَ", None, None, None, "أَسِيَ عَلَيْهِ يَأْسَى: حَزِنَ — نَاقِصٌ مِنْ بَابِ سَمِعَ"))
put_morph(mo, "ghaniya-dwell", _sg.entry(_sg.BABS["samia"][0] + " — نَاقِصٌ يَائِيٌّ", _sg.BABS["samia"][1], "غِنًى", "غَانٍ (الْغَانِي)", _sg.mazi_naqis_kasra("غَنِ", "غَنُوا"), _sg.mudari_naqis("َ", "غْن", "a"), _sg.amr_naqis("اِغْن", "a"), "يَغْنَى", "يَغْنَ", "تَغْنَ", None, None, None, "غَنِيَ بِالْمَكَانِ يَغْنَى: أَقَامَ بِهِ — نَاقِصٌ مِنْ بَابِ سَمِعَ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch5 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 5 (print pp. 8–10, sections 10–14): the last arrow of the proud with 7:88 (s1–s2), Shuʿayb's cutting answer 7:88–89 (s3–s7), the old refrain 26:185–187 (s8–s11), the end of a nation 7:91–92 (s12–s14), the prophet who delivered 7:93 (s15–s16)."
ADD_TR = " Beşinci bölüm (baskı s. 8–10, 10–14. kısımlar): kibirlilerin son oku ve 7:88 (s1–s2), Şuayb'ın kesin cevabı 7:88–89 (s3–s7), eski nakarat 26:185–187 (s8–s11), bir ümmetin sonu 7:91–92 (s12–s14), tebliğ eden peygamber 7:93 (s15–s16)."
write_out(5, S, TITLE, ADD_EN, ADD_TR, "sections 10–14", GLOSS_ADD, notes=(), related=())
report(5, S, GLOSS_ADD, ())
