# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 39: God forgives what is less than shirk; punishment for the small sin and pardon for the great are possible;
deeming a sin lawful is unbelief. Source: matn line 53 (والله لا يغفر أن يشرك به … والاستحلال كفر); the first sentence of the line is chapter 9 s1.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch39.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْمَغْفِرَةُ وَالْعِقَابُ وَالِاسْتِحْلَالُ", "en": "Forgiveness, Punishment, and Deeming Lawful", "tr": "Mağfiret, İkâb ve İstihlâl"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And God does not forgive that partners be ascribed to Him, and He forgives what is less than that to whom He wills, of the small sins and the great.",
 "tr": "Allah, kendisine ortak koşulmasını bağışlamaz; bundan aşağısını — küçük günahlardan ve büyüklerden — dilediğine bağışlar."},
 "tokens": [
  MUB("وَاللهُ", "allah", "«and God» — the sentence follows the wording of al-Nisāʾ 4:48.", "«ve Allah» — cümle Nisâ 4:48'in ifadesini izler.", wa="isti", pos="propn"),
  LA("«does not».", "«-maz».", ar="حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ — وَالْجُمْلَةُ الْفِعْلِيَّةُ بَعْدَهُ خَبَرُ الْمُبْتَدَإِ."),
  MUDA("يَغْفِرُ", "ghafara", "«forgives».", "«bağışlar».", HIDDEN_HUWA, tags=["anwa-al-khabar"]),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ: لَا يَغْفِرُ الْإِشْرَاكَ بِهِ.", "«that» — the an-clause is the object: He does not forgive «the ascribing of partners».", "«… -masını» — en'li masdar mef'ûldür: «ortak koşulmasını» bağışlamaz."),
  W("يُشْرَكَ", "ashraka", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "nawasib-wa-jawazim-al-mudari", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ «بِهِ».", "«partners be ascribed» — a passive in naṣb; its deputy doer is the jarr phrase بِهِ.", "«ortak koşulması» — mansûb meçhul; nâib-i fâili câr-mecrûr بِهِ'dir."),
  PRON_J("بِهِ", "بِ", "«to Him».", "«O'na».", None, extra="، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ", tags=["naib-al-fail"], punct="،"),
  MUDA("وَيَغْفِرُ", "ghafara", "«and He forgives».", "«ve bağışlar».", HIDDEN_HUWA, wa="atf", tags=["atf-nasaq"]),
  MAWSUL("مَا", "ma-mawsula", "«what» — the object.", "«… -ını» — mef'ûl.", "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", tags=["maful-bihi", "anwa-ma"]),
  W("دُونَ", "duna", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ مُتَعَلِّقٌ بِمَحْذُوفٍ صِلَةُ الْمَوْصُولِ، وَهُوَ مُضَافٌ.", "«less than» — a ẓarf that is the whole ṣila: «what is below that».", "«aşağısı» — sılanın tamamı olan zarf: «ondan aşağı olanı»."),
  ISHARA("ذَلِكَ", "dhalika", "«that» — shirk.", "«bu» — şirk.", "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", tags=["idafa-definiteness"]),
  W("لِمَنْ", "man-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "mahall-al-majrur"], "اللَّامُ حَرْفُ جَرٍّ، وَ«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَغْفِرُ».", "«to whom».", "«kime».", segments=[seg("لِ", "li", "prep"), seg("مَنْ", "man-mawsula", "pron")]),
  MUDA("يَشَاءُ", "shaa", "«He wills» — the ṣila; the ʿāʾid is dropped.", "«diler» — sıla; âid hazfedilmiştir.", HIDDEN_HUWA + " — صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ", tags=["ism-mawsul", "hollow-verbs"]),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of» — explaining «what is less».", "«-den» — «aşağısı»nı açıklar."),
  MAJ("الصَّغَائِرِ", "saghira", "«the small sins» — the plural of صَغِيرَة on فَعَائِل.", "«küçük günahlar» — صَغِيرَة'nin فَعَائِل veznindeki çoğulu.", "مِنَ", "مَحْذُوفٍ حَالٌ مِنْ «مَا»", tags=["jam-taksir", "hal"]),
  ATF("وَالْكَبَائِرِ", "kabira", "«and the great».", "«ve büyükler».", "الصَّغَائِرِ", "jarr", punct=".", tags=["jam-taksir"])]})
S.append({"id": "s2", "translation": {
 "en": "And punishment for the small sin is possible, and pardon for the great one, when it was not out of deeming it lawful.",
 "tr": "Küçük günaha ikâb da câizdir, helâl sayma yoluyla olmadığında büyük günahın affı da."},
 "tokens": [
  MUDA("وَيَجُوزُ", "jaaza", "«and is possible» — God may punish the small sin; nothing obliges Him to pardon it.", "«ve câizdir» — Allah küçük günahı cezalandırabilir; affetmesi O'na vâcip değildir.", "وَالْفَاعِلُ «الْعِقَابُ»", wa="isti", tags=["hollow-verbs", "fail"]),
  FAIL("الْعِقَابُ", "iqab", "«punishment».", "«ikâb».", tags=["masdar"]),
  PREP("عَلَى", "ala", "«for».", "«için»."),
  MAJ("الصَّغِيرَةِ", "saghira", "«the small sin».", "«küçük günah».", "عَلَى", "«الْعِقَابُ»", punct="،"),
  ATF("وَالْعَفْوُ", "afw", "«and pardon» — joined to الْعِقَابُ: pardon for the great sin is also possible.", "«ve af» — الْعِقَابُ'ya atıf: büyük günahın affı da câizdir.", "الْعِقَابُ", "raf", tags=["masdar"]),
  PREP("عَنِ", "an", "«for» — the nūn takes a kasra before the article.", "«-den» — nûn, elif-lâm önünde kesre alır."),
  MAJ("الْكَبِيرَةِ", "kabira", "«the great one».", "«büyük günah».", "عَنِ", "«الْعَفْوُ»"),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِجَوَابِهِ، وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«when» — the conditional ẓarf; its answer is understood from what precedes.", "«… -dığında» — şart zarfı; cevabı öncesinden anlaşılır."),
  W("لَمْ", "lam-jazima", "part", ["lam-jazim", "nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«was not» — lam negates, cuts the muḍāriʿ and turns it to the past.", "«olmadı» — lem nefyeder, muzârii cezmeder ve mâzîye çevirir."),
  W("تَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "nawasib-wa-jawazim-al-mudari", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ يَعُودُ عَلَى الْكَبِيرَةِ — فِعْلُ الشَّرْطِ.", "«it was» — the jazm empties the hollow verb's middle: تَكُونُ → تَكُنْ.", "«olmadı» — cezm, ecvef fiilin ortasını boşaltır: تَكُونُ → تَكُنْ."),
  PREP("عَنِ", "an", "«out of».", "«-den»."),
  MAJ("اسْتِحْلَالٍ", "istihlal-lawful", "«deeming lawful» — the kāna-khabar: the sin was not «out of» treating it as permitted.", "«helâl sayma» — kâne'nin haberi: günah, onu mubah saymaktan kaynaklanmadı.", "عَنِ", "مَحْذُوفٍ خَبَرُ «تَكُنْ»", punct="،", tags=["masdar", "form-x-verbs", "kana-wa-akhawatuha"])]})
S.append({"id": "s3", "translation": {"en": "And deeming (a sin) lawful is unbelief.", "tr": "(Günahı) helâl saymak ise küfürdür."},
 "tokens": [
  MUB("وَالِاسْتِحْلَالُ", "istihlal-lawful", "«and deeming lawful».", "«ve istihlâl».", wa="isti", tags=["masdar", "form-x-verbs"]),
  KHA("كُفْرٌ", "kufr", "«is unbelief».", "«küfürdür».", of="الِاسْتِحْلَالُ", punct=".")]})

CAND = {
 "afw": need("afw", "عَفْو", "ع ف و", "noun", "pardon, forgiveness (masdar)", "af, bağışlama (masdar)", 3),
 "istihlal-lawful": need("istihlal-lawful", "اسْتِحْلَال", "ح ل ل", "noun", "deeming lawful — treating a forbidden thing as permitted (masdar of Form X)", "istihlâl, helâl sayma — haramı mubah görme (istif'âl masdarı)", 4),
}
ADD_EN = (" Chapter 39 (matn line 53): God forgives what is less than shirk; punishment for the small sin and pardon for the great are possible"
          " when there was no deeming-lawful, which is itself unbelief; the line's first sentence is chapter 9.")
ADD_TR = (" Otuz dokuzuncu bâb (matn satırı 53): Allah şirkten aşağısını bağışlar; istihlâl olmadıkça küçük günaha ikâb da büyüğüne af da"
          " câizdir, istihlâlin kendisi küfürdür; satırın ilk cümlesi dokuzuncu bâbdır.")
finish(39, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 39 (matn line 53)")
