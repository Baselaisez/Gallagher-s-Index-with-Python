# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 16: «وَمَا كَفَرَ سُلَيْمَانُ» — §15, the last section of the story of Dāwūd and Sulaymān:
what the Jews ascribed to him and how God cleared him (2:102, 38:30, 38:25); print p. 25.
python3 tools/authoring/author_qisas4_ch16.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "وَمَا كَفَرَ سُلَيْمَانُ وَلٰكِنَّ الشَّيَاطِينَ كَفَرُوا", "en": "«Sulaymān did not disbelieve, but the devils did»", "tr": "«Süleyman kâfir olmadı, fakat şeytanlar kâfir oldular»"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"
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
def v_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), wa=False, fa=False, hidden="هُوَ"):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "")
    segs = ([seg("وَ" if wa else "فَ", "wa" if wa else "fa", "conj")] if (wa or fa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if (wa or fa) else []) + [MB] + list(tags), pre + stem + f" فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden}، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", en + " — a māḍī; the pronoun is its object.", tr + " — mâzî; zamir mef'ûl.", punct=punct, segments=segs)

sen("s1", "The Jews ascribed to him what does not befit a believer affirming God's oneness whose breast God opened to faith — let alone a prophet sent, to whom God gave wisdom, whom He honoured with prophethood and ennobled with the vicegerency;",
        "Yahudiler ona, Allah'ın göğsünü imana açtığı muvahhid bir mümine bile yakışmayanı — hele Allah'ın hikmet verdiği, peygamberlikle onurlandırdığı, hilâfetle şereflendirdiği gönderilmiş bir peygambere hiç yakışmayanı — nispet ettiler;", [
  mazi("نَسَبَ", "nasaba-attribute", "«ascribed»", "«nispet etti»", tags=[MB], hidden=None),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to him»", "«ona»"),
  fail("الْيَهُودُ", "yahud", "«the Jews»", "«Yahudiler»"),
  tok("مَا", "ma-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the relative, the object.", "«… -anı» — ism-i mevsûl, mef'ûl."),
  la_nafiya(),
  neg_mudari("يَلِيقُ", "laqa-befit", "«befits»", "«yakışır»", tags=[MW, "hollow-verbs"], hidden="هُوَ", extra=" — صِلَةٌ"),
  tok("بِمُؤْمِنٍ", "mumin", "noun", [HJ, "ism-fail", "form-iv-verbs"], "الْبَاءُ حَرْفُ جَرٍّ، وَمُؤْمِنٍ مَجْرُورٌ.", "«a believer»", "«bir mümine»", segments=[seg("بِ", "bi", "prep"), seg("مُؤْمِنٍ", "mumin", "noun")]),
  naat("مُوَحِّدٍ", "muwahhid", "«affirming God's oneness»", "«muvahhid»", tags=["ism-fail", "form-ii-verbs"]),
  mazi("شَرَحَ", "sharaha", "«opened»", "«açtı»", tags=["jumla-sifa", MB], hidden=None, extra_ar=" — وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِمُؤْمِنٍ"),
  allah_fail(),
  noun_pron("صَدْرَهُ", "sadr", "صَدْرَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his breast»", "«göğsünü»", tags=[MB, ID]),
  tok("لِلْإِيمَانِ", "iman", "noun", [HJ, "masdar"], "اللَّامُ حَرْفُ جَرٍّ، وَالْإِيمَانِ مَجْرُورٌ.", "«to faith»", "«imana»", punct="،", segments=[seg("لِ", "li", "prep"), seg("الْإِيمَانِ", "iman", "noun")]),
  tok("فَضْلًا", "fadl", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ مَنْصُوبٌ — فَضْلًا عَنْ: بِمَعْنَى: نَاهِيكَ عَنْ.", "«let alone» — an absolute object of an understood verb; «faḍlan ʿan».", "«hele … hiç» — mukadder fiilin mef'ûl-i mutlakı; «fadlen an»."),
  prep("عَنْ", "an", "«(let alone)»", "«… -e»"),
  majrur("نَبِيٍّ", "nabi", "«a prophet»", "«bir peygambere»"),
  naat("مُرْسَلٍ", "mursal", "«sent»", "«gönderilmiş»", tags=["ism-maful", "form-iv-verbs"]),
  tok("آتَاهُ", "aataa", "verb", ["jumla-sifa", MX, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ نَعْتٌ.", "«to whom … gave» — a naʿt clause; the hāʾ the first object.", "«… verdiği» — sıfat cümlesi; hâ ilk mef'ûl.", segments=[seg("آتَا", "aataa", "verb"), pr3ms()]),
  allah_fail(),
  tok("الْحِكْمَةَ", "hikma", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«wisdom» — the second object.", "«hikmeti» — ikinci mef'ûl.", punct="،"),
  v_pron("وَأَكْرَمَهُ", "akrama", "أَكْرَمَ", "هُ", "pron-3ms", "«and honoured him»", "«ve onu onurlandırdı»", tags=["form-iv-verbs"], wa=True),
  tok("بِالنُّبُوَّةِ", "nubuwwa", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالنُّبُوَّةِ مَجْرُورٌ.", "«with prophethood»", "«peygamberlikle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("النُّبُوَّةِ", "nubuwwa", "noun")]),
  v_pron("وَشَرَّفَهُ", "sharrafa", "شَرَّفَ", "هُ", "pron-3ms", "«and ennobled him»", "«ve onu şereflendirdi»", tags=["form-ii-verbs"], wa=True),
  tok("بِالْخِلَافَةِ", "khilafa", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْخِلَافَةِ مَجْرُورٌ.", "«with the vicegerency»", "«hilâfetle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْخِلَافَةِ", "khilafa", "noun")]),
])
sen("s2", "they ascribed to him sorcery and unbelief, compromise with idolatry, and wavering in the matter of God's oneness because of his wives; so God cleared him of all that, and said:",
        "ona sihri, küfrü, şirke göz yummayı ve eşleri yüzünden tevhid işinde sarsılmayı nispet ettiler; Allah onu bütün bunlardan temize çıkardı ve buyurdu ki:", [
  mazi_pl("فَنَسَبُوا", "nasaba-attribute", "«they ascribed»", "«nispet ettiler»", tags=[AT, MB]),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to him»", "«ona»"),
  maful_("السِّحْرَ", "sihr", "«sorcery»", "«sihri»"),
  atf("وَالْكُفْرَ", "kufr", "«unbelief»", "«küfrü»", "nasb", punct="،"),
  atf("وَالْمُدَاهَنَةَ", "mudahana", "«compromise»", "«göz yummayı»", "nasb", tags=["masdar"]),
  tok("لِلشِّرْكِ", "shirk", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالشِّرْكِ مَجْرُورٌ — مُتَعَلِّقٌ بِالْمُدَاهَنَةِ.", "«with idolatry»", "«şirke»", punct="،", segments=[seg("لِ", "li", "prep"), seg("الشِّرْكِ", "shirk", "noun")]),
  atf("وَالِاضْطِرَابَ", "idtirab", "«wavering»", "«sarsılmayı»", "nasb", tags=["masdar", "form-viii-verbs"]),
  fi(), majrur("أَمْرِ", "amr-noun", "«the matter»", "«işinde»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  mudaf_ilayh("التَّوْحِيدِ", "tawhid", "«of God's oneness»", "«tevhid»", tags=["masdar"]),
  tok("بِسَبَبِ", "sabab", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَسَبَبِ مَجْرُورٌ، مُضَافٌ.", "«because of»", "«… yüzünden»", segments=[seg("بِ", "bi", "prep"), seg("سَبَبِ", "sabab", "noun")]),
  noun_pron("أَزْوَاجِهِ", "zawj", "أَزْوَاجِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his wives»", "«eşleri»", punct="،", tags=[ID, JT]),
  v_pron("فَبَرَّأَهُ", "barraa", "بَرَّأَ", "هُ", "pron-3ms", "«so … cleared him»", "«onu temize çıkardı»", tags=["form-ii-verbs"], fa=True, hidden=None),
  allah_fail(),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("كُلِّ", "kull", "«all»", "«bütün»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  tok("ذٰلِكَ", "dhalika", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that»", "«bunlar»", punct="،"),
  qala(full="فَقَالَ", wa=False, hidden="هُوَ", tags=[AT]),
])
sen("s3", "«Sulaymān did not disbelieve; but the devils disbelieved, teaching people sorcery» (2:102).",
        "«Süleyman kâfir olmadı, fakat şeytanlar kâfir oldular; insanlara sihri öğretiyorlardı» (2:102).", [
  *quran([
  tok("وَمَا", "ma-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and … not» — the negating mā.", "«ve … -madı» — nefiy mâ'sı.", segments=wa_("مَا", "ma-nafiya", "part")),
  mazi("كَفَرَ", "kafara", "«disbelieved»", "«kâfir oldu»", tags=[], hidden=None),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»"),
  tok("وَلٰكِنَّ", "lakinna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ.", "«but» — lākinna.", "«fakat» — lâkinne.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
  ism_inna("الشَّيَاطِينَ", "shaytan", "«the devils»", "«şeytanlar»", part="لٰكِنَّ", tags=[JT]),
  mazi_pl("كَفَرُوا", "kafara", "«disbelieved»", "«kâfir oldular»", tags=[IW]),
  khamsa("يُعَلِّمُونَ", "allama", "«teaching»", "«öğretiyorlardı»", tags=[HL, MX, "form-ii-verbs"], extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  tok("النَّاسَ", "nas", "noun", [MB, MX], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ.", "«people» — the first object.", "«insanlara» — ilk mef'ûl."),
  tok("السِّحْرَ", "sihr", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«sorcery» — the second object.", "«sihri» — ikinci mef'ûl.", punct="."),
  ]),
])
sen("s4", "And He said: «And We gave to Dāwūd Sulaymān — an excellent servant; he was ever-returning» (38:30).",
        "Ve buyurdu: «Dâvûd'a Süleyman'ı bağışladık; ne güzel kuldu; o çok tövbe edendi» (38:30).", [
  qala(full="وَقَالَ", wa=True, hidden="هُوَ"),
  *quran([
  tok("وَوَهَبْنَا", "wahaba", "verb", [MB, "mithal-verbs"], "الْوَاوُ عَاطِفَةٌ، وَوَهَبْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ.", "«and We gave» — nā the doer.", "«ve bağışladık» — nâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("وَهَبْ", "wahaba", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("لِدَاوُدَ", "dawud", "propn", [HJ, MM], "اللَّامُ حَرْفُ جَرٍّ، وَدَاوُدَ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«to Dāwūd» — jarr by fatḥa.", "«Dâvûd'a» — fetha ile mecrûr.", segments=[seg("لِ", "li", "prep"), seg("دَاوُدَ", "dawud", "propn")]),
  tok("سُلَيْمَانَ", "sulayman", "propn", [MB, MM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān» — the object.", "«Süleyman'ı» — mef'ûl."),
  tok("نِعْمَ", "nima-verb", "verb", ["mana-al-fil"], "فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ الْمَدْحِ.", "«excellent» — the frozen verb of praise.", "«ne güzel» — medih için câmid fiil."),
  tok("الْعَبْدُ", "abd", "noun", [FL], "فَاعِلُ نِعْمَ مَرْفُوعٌ، وَالْمَخْصُوصُ بِالْمَدْحِ مَحْذُوفٌ (سُلَيْمَانُ).", "«the servant» — the doer of niʿma; the one praised is understood.", "«kul» — ni'me'nin fâili; övülen hazfedilmiş."),
  tok("إِنَّهُ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا.", "«he was» (lit. indeed he)", "«şüphesiz o»", segments=[seg("إِنَّ", "inna", "part"), pr3ms()]),
  khabar_inna("أَوَّابٌ", "awwab", "«ever-returning»", "«çok tövbe eden»", tags=["sighat-mubalagha"], punct="."),
  ]),
])
sen("s5", "And He said: «And he has, with Us, nearness and a fine return» (38:25).",
        "Ve buyurdu: «Şüphesiz onun katımızda bir yakınlığı ve güzel bir dönüş yeri vardır» (38:25).", [
  qala(full="وَقَالَ", wa=True, hidden="هُوَ"),
  *quran([
  tok("وَإِنَّ", "inna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«and indeed»", "«ve şüphesiz»", segments=wa_("إِنَّ", "inna", "part")),
  li_pron("لَهُ", "هُ", "pron-3ms", "«he has» — inna's fronted khabar.", "«onun … var» — inne'nin öne alınmış haberi.", tags=[IW], extra=" — خَبَرُ إِنَّ مُقَدَّمٌ"),
  noun_pron("عِنْدَنَا", "inda", "عِنْدَ", "نَا", "pron-1p", "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«with Us»", "«katımızda»", tags=[MF, ID]),
  tok("لَزُلْفَى", "zulfa", "noun", [IW], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَزُلْفَى اسْمُ إِنَّ مُؤَخَّرٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«nearness» — the sliding lām; inna's delayed ism, a maqṣūr.", "«yakınlık» — kaydırılmış lâm; inne'nin ismi, maksûr.", segments=[seg("لَ", "lam-qasam", "part"), seg("زُلْفَى", "zulfa", "noun")]),
  atf("وَحُسْنَ", "husn", "«a fine»", "«güzel»", "nasb", tags=[ID]),
  mudaf_ilayh("مَآبٍ", "maab", "«return»", "«dönüş yeri»", punct="."),
  ]),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: nasaba-attribute is the new key beside idtirab, mudahana, muwahhid, sharrafa, zulfa; laqa-befit and nima-verb reused)
CAND = {
 "nasaba-attribute": G("nasaba-attribute", "نَسَبَ", "ن س ب", "verb", "to ascribe, to attribute (with ilā)", "nispet etmek, yakıştırmak (ilâ ile)", 2),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 1),
 "laqa-befit": G("laqa-befit", "لَاقَ", "ل ي ق", "verb", "to befit, to be fitting (hollow; with bi)", "yakışmak, uygun olmak (ecvef; bi ile)", 3),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "a believer", "mümin", 1),
 "muwahhid": G("muwahhid", "مُوَحِّد", "و ح د", "noun", "one who affirms God's oneness (the active participle of Form II)", "muvahhid, Allah'ı birleyen (tef'îl ism-i fâili)", 2),
 "sharaha": G("sharaha", "شَرَحَ", "ش ر ح", "verb", "to open (the breast); to explain", "açmak (göğsü); şerh etmek", 2),
 "sadr": G("sadr", "صَدْر", "ص د ر", "noun", "the breast, the chest", "göğüs, sadır", 1),
 "iman": G("iman", "إِيمَان", "أ م ن", "noun", "faith", "iman", 1),
 "fadl": G("fadl", "فَضْل", "ف ض ل", "noun", "favour; «let alone» in فَضْلًا عَنْ", "lütuf; «hele, … şöyle dursun» (fadlen an)", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1),
 "mursal": G("mursal", "مُرْسَل", "ر س ل", "noun", "sent (a passive participle); a messenger", "gönderilmiş (ism-i mef'ûl); elçi", 2),
 "aataa": G("aataa", "آتَى", "أ ت ي", "verb", "to give", "vermek", 2),
 "hikma": G("hikma", "حِكْمَة", "ح ك م", "noun", "wisdom", "hikmet", 1),
 "akrama": G("akrama", "أَكْرَمَ", "ك ر م", "verb", "to honour (Form IV)", "onurlandırmak, ikram etmek (if'âl)", 1),
 "nubuwwa": G("nubuwwa", "نُبُوَّة", "ن ب أ", "noun", "prophethood", "peygamberlik", 1),
 "sharrafa": G("sharrafa", "شَرَّفَ", "ش ر ف", "verb", "to ennoble, to honour (Form II)", "şereflendirmek (tef'îl)", 2),
 "khilafa": G("khilafa", "خِلَافَة", "خ ل ف", "noun", "the vicegerency, the caliphate", "hilâfet", 2),
 "sihr": G("sihr", "سِحْر", "س ح ر", "noun", "sorcery, magic", "sihir, büyü", 1),
 "kufr": G("kufr", "كُفْر", "ك ف ر", "noun", "unbelief", "küfür", 1),
 "mudahana": G("mudahana", "مُدَاهَنَة", "د ه ن", "noun", "compromise, dissembling (maṣdar of Form III)", "göz yumma, müdahene (müfâale masdarı)", 3),
 "shirk": G("shirk", "شِرْك", "ش ر ك", "noun", "idolatry", "şirk", 1),
 "idtirab": G("idtirab", "اِضْطِرَاب", "ض ر ب", "noun", "wavering, disturbance (maṣdar of Form VIII; the tāʾ became ṭāʾ)", "sarsılma, karışıklık (iftiâl masdarı; tâ'sı tâ'ya dönmüş)", 3),
 "amr-noun": G("amr-noun", "أَمْر", "أ م ر", "noun", "a matter", "iş", 1),
 "tawhid": G("tawhid", "تَوْحِيد", "و ح د", "noun", "the affirmation of God's oneness", "tevhid", 1),
 "sabab": G("sabab", "سَبَب", "س ب ب", "noun", "a cause; «because of» in بِسَبَبِ", "sebep; «yüzünden» (bi-sebebi)", 1),
 "zawj": G("zawj", "زَوْج", "ز و ج", "noun", "a spouse, a wife", "eş", 1, plural="أَزْوَاج"),
 "barraa": G("barraa", "بَرَّأَ", "ب ر أ", "verb", "to clear, to declare innocent (Form II)", "temize çıkarmak, berî kılmak (tef'îl)", 2),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all", "bütün", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "the negating mā", "nefiy mâ'sı", 1),
 "kafara": G("kafara", "كَفَرَ", "ك ف ر", "verb", "to disbelieve", "kâfir olmak", 1),
 "sulayman": G("sulayman", "سُلَيْمَان", None, "propn", "Sulaymān", "Süleyman", 1),
 "lakinna": G("lakinna", "لٰكِنَّ", None, "part", "but", "fakat", 1),
 "shaytan": G("shaytan", "شَيْطَان", "ش ط ن", "noun", "a devil", "şeytan", 1, plural="شَيَاطِين"),
 "allama": G("allama", "عَلَّمَ", "ع ل م", "verb", "to teach", "öğretmek", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "wahaba": G("wahaba", "وَهَبَ", "و ه ب", "verb", "to give, to bestow (an assimilated verb: يَهَبُ)", "bağışlamak, vermek (misâl fiil: yehebü)", 2),
 "dawud": G("dawud", "دَاوُد", None, "propn", "Dāwūd", "Dâvûd", 1),
 "nima-verb": G("nima-verb", "نِعْمَ", "ن ع م", "verb", "excellent is … — the frozen verb of praise", "ne güzel … — medih fiili", 2),
 "abd": G("abd", "عَبْد", "ع ب د", "noun", "a servant", "kul", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "awwab": G("awwab", "أَوَّاب", "أ و ب", "noun", "ever-returning to God", "çok tövbe eden, evvâb", 3),
 "inda": G("inda", "عِنْدَ", "ع ن د", "noun", "with, at", "katında", 1),
 "lam-qasam": G("lam-qasam", "لَ (لَامُ الْقَسَمِ)", None, "part", "the lām of the oath's answer / of ibtidāʾ", "kasem cevabının lâmı / ibtidâ lâmı", 2),
 "zulfa": G("zulfa", "زُلْفَى", "ز ل ف", "noun", "nearness, closeness (a maqṣūr noun)", "yakınlık (maksûr isim)", 3),
 "husn": G("husn", "حُسْن", "ح س ن", "noun", "fineness, goodness", "güzellik", 1),
 "maab": G("maab", "مَآب", "أ و ب", "noun", "a place of return", "dönüş yeri, meâb", 3),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us / our", "biz / bizi / bizim", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "nasaba-attribute", _sg.sound1("nasara", "نَسَب", "نْسُب", "اُنْسُب", "نِسْبَة", "نَاسِب", "مَنْسُوب", "نُسِبَ", "يُنْسَبُ", "نَسَبَ الشَّيْءَ إِلَيْهِ: عَزَاهُ إِلَيْهِ."))
put_morph(mo, "sharaha", _sg.sound1("fataha", "شَرَح", "شْرَح", "اِشْرَح", "شَرْح", "شَارِح", "مَشْرُوح", "شُرِحَ", "يُشْرَحُ", "شَرَحَ اللهُ صَدْرَهُ: وَسَّعَهُ وَفَتَحَهُ لِلْحَقِّ."))
put_morph(mo, "sharrafa", _sg.derived(_sg.B2, _sg.W2, "ُ", "شَرَّف", "شَرِّف", "شَرِّف", "تَشْرِيف", "مُشَرِّف", "مُشَرَّف", "شُرِّفَ", "يُشَرَّفُ", "شَرَّفَهُ: جَعَلَهُ شَرِيفًا."))
put_morph(mo, "barraa", _sg.entry(_sg.B2 + " — مَهْمُوزُ اللَّامِ", _sg.W2, "تَبْرِئَة", "مُبَرِّئ", ["بَرَّأَ", "بَرَّآ", "بَرَّؤُوا", "بَرَّأَتْ", "بَرَّأَتَا", "بَرَّأْنَ", "بَرَّأْتَ", "بَرَّأْتُمَا", "بَرَّأْتُمْ", "بَرَّأْتِ", "بَرَّأْتُمَا", "بَرَّأْتُنَّ", "بَرَّأْتُ", "بَرَّأْنَا"], ["يُبَرِّئُ", "يُبَرِّئَانِ", "يُبَرِّئُونَ", "تُبَرِّئُ", "تُبَرِّئَانِ", "يُبَرِّئْنَ", "تُبَرِّئُ", "تُبَرِّئَانِ", "تُبَرِّئُونَ", "تُبَرِّئِينَ", "تُبَرِّئَانِ", "تُبَرِّئْنَ", "أُبَرِّئُ", "نُبَرِّئُ"], ["بَرِّئْ", "بَرِّئَا", "بَرِّئُوا", "بَرِّئِي", "بَرِّئَا", "بَرِّئْنَ"], "يُبَرِّئَ", "يُبَرِّئْ", "تُبَرِّئْ", "مُبَرَّأ", "بُرِّئَ", "يُبَرَّأُ", "بَرَّأَهُ مِنَ التُّهْمَةِ: نَزَّهَهُ وَأَعْلَنَ بَرَاءَتَهُ — مَهْمُوزُ اللَّامِ."))
put_morph(mo, "wahaba", _sg.entry("مِنْ بَابِ فَتَحَ يَفْتَحُ — مِثَالٌ وَاوِيٌّ (تَسْقُطُ وَاوُهُ فِي الْمُضَارِعِ)", "فَعَلَ يَفْعَلُ", "هِبَة / وَهْب", "وَاهِب", _sg.mazi14("وَهَب"), _sg.mudari14("َ", "هَب"), _sg.amr_attach("هَب"), "يَهَبَ", "يَهَبْ", "تَهَبْ", "مَوْهُوب", "وُهِبَ", "يُوهَبُ", "وَهَبَ لَهُ الشَّيْءَ: أَعْطَاهُ إِيَّاهُ بِلَا عِوَضٍ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch16 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 16 (print p. 25, §15 — the last section of the story): what the Jews ascribed to Sulaymān and how God cleared him, with 2:102, 38:30 and 38:25 (s1–s5). END of the story of Dāwūd and Sulaymān."
ADD_TR = " On altıncı bölüm (baskı s. 25, 15. kısım — kıssanın son kısmı): Yahudilerin Süleyman'a nispet ettikleri ve Allah'ın onu temize çıkarışı; 2:102, 38:30 ve 38:25 ile (s1–s5). Dâvûd ve Süleyman kıssasının SONU."
write_out(16, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §15", GLOSS_ADD, notes=(), related=())
report(16, S, GLOSS_ADD, ())
