#!/usr/bin/env python3
"""(v359-E) The level-one Amthila notes — الأمثلة المختلفة والمطردة — and the pronouns where the madrasa teaches them.

Two passes around the page, so that every Arabic form a note shows is the app's own ṣarf engine's:
  python3 tools/emsile/build_emsile359.py spec     # writes tools/emsile/emsile359_spec.json (tables as engine descriptors)
  node tools/emsile/emsile359_derive.js            # the page fills every cell (Emsile359.fill), attests pronoun rows, reads examples
  python3 tools/emsile/build_emsile359.py notes    # writes content/grammar/emsile-*.json from the spec + the cells
What is typed here: the explaining sentences (OURS, en + tr, marked as awaiting the hoca), the form NAMES (the tradition's terms:
the Turkish ones as the received sheet research/sources/ziyade-bab-muhtelife-cekimi.txt writes them, the Arabic ones cited by line
where Taṣrīf al-ʿIzzī / Marāḥ al-Arwāḥ / Iẓhār / al-Kāfiya use them — see TERMS), and WHICH engine list a table shows. No Arabic
form is typed: a table is a descriptor, a mistake is two engine cells, an example is a corpus sentence by its id.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SRC = ROOT / "research" / "sources"
R = "ن ص ر"
S14 = list(range(14))
AMR6 = [6, 7, 8, 9, 10, 11]
GH6 = [0, 1, 2, 3, 4, 5]
PENDING = {"en": " [Explanation ours — awaiting the hoca's review.]", "tr": " [Açıklama bizimdir — hoca onayı bekliyor.]"}


def H(ar, en, tr):
    return {"ar": ar, "en": en, "tr": tr}


def tab(tid, head, src, **kw):
    d = {"id": tid, "head": head, "src": src}
    d.update(kw)
    return d


def raf_keys(seats, hidden):
    return [f"rafMuttasil:{s}" + (":h" if s in hidden else "") for s in seats]


def keys(kind, seats):
    return [f"{kind}:{s}" for s in seats]


# the person/number/gender labels of non-verb paradigms (the Maqṣūd recites them in this order: ism fāʿil L317–L318)
NUM6 = [H("مُفْرَدٌ مُذَكَّرٌ", "masculine singular", "müfred müzekker"), H("مُثَنًّى مُذَكَّرٌ", "masculine dual", "tesniye müzekker"),
        H("جَمْعُ مُذَكَّرٍ سَالِمٌ", "sound masculine plural", "cem'-i müzekker sâlim"), H("مُفْرَدٌ مُؤَنَّثٌ", "feminine singular", "müfred müennes"),
        H("مُثَنًّى مُؤَنَّثٌ", "feminine dual", "tesniye müennes"), H("جَمْعُ مُؤَنَّثٍ سَالِمٌ", "sound feminine plural", "cem'-i müennes sâlim")]

# the 24 forms: slot of MaqsudEngine.emsileI, the particle the row recites before it, the tradition's names, a one-line meaning
FORMS = [
    ("mazi", "", "الْفِعْلُ الْمَاضِي", "Fiil-i mâzî", "Past", "he helped", "yardım etti"),
    ("mudari", "", "الْفِعْلُ الْمُضَارِعُ", "Fiil-i muzâri", "Present–future", "he helps / will help", "yardım eder / edecek"),
    ("masdar", "", "الْمَصْدَرُ", "Masdar (gayr-i mîmî)", "Verbal noun", "helping", "yardım etmek"),
    ("fail", "فَهُوَ ", "اسْمُ الْفَاعِلِ", "İsm-i fâil", "Active participle", "so he is a helper", "o hâlde o, yardım edendir"),
    ("maful", "وَذَاكَ ", "اسْمُ الْمَفْعُولِ", "İsm-i mef'ûl", "Passive participle", "and that one is helped", "şu da yardım olunandır"),
    ("lam", "لَمْ ", "الْجَحْدُ الْمُطْلَقُ", "Cahd-ı mutlak", "Plain denial of the past", "he did not help", "yardım etmedi"),
    ("lamma", "لَمَّا ", "الْجَحْدُ الْمُسْتَغْرَقُ", "Cahd-ı müstağrak", "Denial of the past up to now", "he has not helped, so far", "şimdiye dek yardım etmedi"),
    ("ma", "مَا ", "نَفْيُ الْحَالِ", "Nefy-i hâl", "Denial of the present", "he is not helping (now)", "şu an yardım etmiyor"),
    ("la", "لَا ", "نَفْيُ الِاسْتِقْبَالِ", "Nefy-i istikbâl", "Denial of the future", "he will not help", "yardım etmeyecek"),
    ("lan", "لَنْ ", "تَأْكِيدُ نَفْيِ الِاسْتِقْبَالِ", "Te'kîd-i nefy-i istikbâl", "Emphatic denial of the future", "he will never help", "asla yardım etmeyecek"),
    ("liAmr", "لِ", "أَمْرُ الْغَائِبِ", "Emr-i gâib", "Command to one absent", "let him help", "yardım etsin"),
    ("laNahy", "لَا ", "نَهْيُ الْغَائِبِ", "Nehy-i gâib", "Prohibition to one absent", "let him not help", "yardım etmesin"),
    ("amr", "", "أَمْرُ الْحَاضِرِ", "Emr-i hâzır", "Command to the one present", "help!", "yardım et!"),
    ("laNahy2", "لَا ", "نَهْيُ الْحَاضِرِ", "Nehy-i hâzır", "Prohibition to the one present", "do not help!", "yardım etme!"),
    ("mimi", "", "اسْمُ الزَّمَانِ وَالْمَكَانِ", "İsm-i zaman ve mekân", "Noun of time and place", "the time or place of helping", "yardım etme zamanı ya da yeri"),
    ("alat", "", "اسْمُ الْآلَةِ", "İsm-i âlet", "Noun of instrument", "the tool of helping", "yardım etme âleti"),
    ("marra", "", "بِنَاءُ الْمَرَّةِ", "Binâ-i merre", "Noun of once", "helping once", "bir kere yardım etmek"),
    ("naw", "", "بِنَاءُ النَّوْعِ", "Binâ-i nev'", "Noun of manner", "a manner of helping", "bir çeşit yardım etmek"),
    ("tasghir", "", "التَّصْغِيرُ", "İsm-i tasğîr", "Diminutive", "a little help", "küçük bir yardım"),
    ("nisba", "", "النِّسْبَةُ", "İsm-i mensûb", "Relational adjective", "having to do with help", "yardımla ilgili"),
    ("mubalagha", "", "صِيغَةُ الْمُبَالَغَةِ", "Mübalağa ism-i fâil", "Intensive participle", "one who helps a great deal", "çok yardım eden"),
    ("tafdil", "", "اسْمُ التَّفْضِيلِ", "İsm-i tafdîl", "Elative", "more / most helpful", "daha çok yardım eden"),
    ("taajjub1", "مَا ", "فِعْلُ التَّعَجُّبِ الْأَوَّلُ", "Fiil-i taaccüb-i evvel", "First verb of wonder", "how much he helps!", "ne çok yardım ediyor!"),
    ("taajjub2", "وَ", "فِعْلُ التَّعَجُّبِ الثَّانِي", "Fiil-i taaccüb-i sânî", "Second verb of wonder", "how much he helps!", "ne çok yardım ediyor!"),
]
MASDAR_TOK = ["jumal-al-tadrib", 4, "s7", 3]     # «نَصَرَ اللهُ الْمُؤْمِنِينَ نَصْرًا عَظِيمًا.» — the samāʿī maṣdar from the corpus

# Arabic terms → a line of a received book that uses them (looked up by script in research/sources, letters only)
TERMS = {
    "tasrif-al-izzi-src.txt": ["الماضي", "المضارع", "اسم الفاعل", "اسم المفعول", "أمر الغائب", "نهي الغائب", "نهي الحاضر", "اسم الآلة", "المرة",
                               "لن ينصر", "لم ينصر", "ما ينصر", "لا ينصر", "لينصر", "الأمر"],
    "marah-al-arwah-src.txt": ["المرفوع المتصل", "المرفوع المنفصل", "المنصوب المتصل", "المنصوب المنفصل", "المجرور المتصل", "يستتر",
                               "اسم المكان", "الآلة", "التصغير", "النسبة", "التفضيل", "التعجب", "المبالغة"],
    "maqsud-sarf.txt": ["امر غائب", "امر حاضر", "اسم زمان", "مصدر ميمى", "اسم فاعل", "اسم مفعول", "تفضيل"],
}
SHEET = "ziyade-bab-muhtelife-cekimi.txt"


def strip(s):
    return re.sub("[ً-ْٰـ]", "", s).replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")


def cite_lines():
    out = {}
    for f, terms in TERMS.items():
        lines = [strip(x) for x in (SRC / f).read_text(encoding="utf-8").split("\n")]
        for t in terms:
            k = next((i + 1 for i, x in enumerate(lines) if strip(t) in x), None)
            if k:
                out[t] = f"{f}، س {k}"
    return out


# ───────────────────────────── the notes ─────────────────────────────
def notes_spec():
    N = {}
    rel_all = ["emsile-00-amthila"]

    # 00 — the overview
    N["emsile-00-amthila"] = dict(
        title=H("الْأَمْثِلَةُ الْمُخْتَلِفَةُ", "The Amthila Mukhtalifa — twenty-four forms from one verb", "Emsile-i Muhtelife — bir fiilden yirmi dört sîga"),
        plain={"en": "The madrasa's first table: from نَصَرَ («he helped») come twenty-four forms in a fixed order — past, present, verbal noun, "
                     "doer, done-to, five denials, four commands and prohibitions, and the nouns. Learn the order; every later book uses it.",
               "tr": "Medresenin ilk cetveli: نَصَرَ («yardım etti») fiilinden sabit bir sırayla yirmi dört sîga çıkar — mâzî, muzâri, masdar, "
                     "fâil, mef'ûl, beş nefiy, dört emir ve nehiy, sonra isimler. Sırayı ezberle; sonraki her kitap onu kullanır."},
        explanation={
            "en": "The Amthila (Emsile) is recited aloud, row by row, always in the same order, and always on the model verb نَصَرَ يَنْصُرُ (bāb 1). "
                  "The order is not arbitrary: each form is built from the one before it. The muḍāriʿ is built from the māḍī by a prefix; the five "
                  "denials are the muḍāriʿ with a particle in front (لَمْ and لَمَّا cut its ending to a sukūn, مَا and لَا leave it, لَنْ gives it a fatḥa); "
                  "the commands are built from the jussive; the nouns of time, place, tool, once and manner come from the maṣdar and the muḍāriʿ. "
                  "So the table is a chain, and a student who knows the chain can build any verb's table. The particles فَهُوَ («so he is») and "
                  "وَذَاكَ («and that one is») are part of the recitation, not of the participle: they make the row a sentence a child can say. "
                  "The maṣdar of the bare verb is HEARD, not built (samāʿī): it is the one form the engine does not make, and here it is the corpus's "
                  "own word نَصْرًا. The second half of the curriculum, the Amthila Muṭṭarida, takes each row through its fourteen persons — "
                  "the next notes in this group do that, row by row, with what changes at each person's ending; the pronouns are taught there too. "
                  "The Turkish names are the received sheet's (ZİYADE BABLARDAN MUHTELİFE ÇEKİMİ).",
            "tr": "Emsile yüksek sesle, satır satır, hep aynı sırayla ve hep model fiil نَصَرَ يَنْصُرُ (birinci bâb) üzerinde okunur. Sıra rastgele "
                  "değildir: her sîga bir öncekinden kurulur. Muzâri, mâzîden muzâraat harfiyle; beş nefiy, önüne bir harf gelen muzâridir "
                  "(لَمْ ve لَمَّا sonunu cezmeder, مَا ve لَا dokunmaz, لَنْ fetha verir); emirler meczûm muzâriden kurulur; ism-i zaman, mekân, âlet, "
                  "merre ve nev' masdardan ve muzâriden gelir. Yani cetvel bir zincirdir; zinciri bilen talebe her fiilin cetvelini kurabilir. "
                  "فَهُوَ («o hâlde o») ve وَذَاكَ («şu da») ism-i fâil ile ism-i mef'ûlün parçası değil, okuyuşun parçasıdır: satırı bir çocuğun "
                  "söyleyebileceği bir cümle yapar. Sülâsî mücerredin masdarı kurulmaz, İŞİTİLİR (semâî): motorun yapmadığı tek sîga budur; burada "
                  "külliyatın kendi kelimesi نَصْرًا duruyor. Müfredatın ikinci yarısı, Emsile-i Muttaride, her satırı on dört sîgasıyla çeker — bu "
                  "gruptaki sonraki notlar bunu satır satır yapar, her sîganın sonunda neyin değiştiğini gösterir; zamirler de orada öğretilir. "
                  "Türkçe adlar gelen cetvelindir (ZİYADE BABLARDAN MUHTELİFE ÇEKİMİ)."},
        tables=[tab("forms", H("الْأَمْثِلَةُ الْمُخْتَلِفَةُ — نَصَرَ", "The twenty-four forms of نَصَرَ", "نَصَرَ fiilinin yirmi dört sîgası"),
                    {"k": "row", "root": R, "bab": 1, "slots": [f[0] for f in FORMS], "pres": [f[1] for f in FORMS],
                     "posts": [("@bihi" if f[0] == "taajjub2" else "") for f in FORMS], "corpus": {"masdar": MASDAR_TOK}},
                    labels=[{"ar": f[2], "tr": f[3], "en": f[4], "m": {"en": f[5], "tr": f[6]}} for f in FORMS])],
        quiz=0,
        examples=[["jumal-al-tadrib", 4, "s7"], ["salih-wa-al-naqa", 4, "s10"], ["qarun-wa-kunuzuh", 4, "s3"]],
        mistakes=[dict(w={"src": {"k": "row", "root": R, "bab": 1, "slots": ["lam"], "pres": ["لَمَّا "]}, "i": 0},
                       r={"src": {"k": "row", "root": R, "bab": 1, "slots": ["lam"], "pres": ["لَمْ "]}, "i": 0},
                       why={"en": "لَمَّا يَنْصُرْ is not the same row as لَمْ يَنْصُرْ: both cut the ending to a sukūn, but لَمْ denies the past plainly "
                                  "(cahd-ı mutlak) and لَمَّا denies it right up to now, with the deed still expected (cahd-ı müstağrak).",
                            "tr": "لَمَّا يَنْصُرْ ile لَمْ يَنْصُرْ aynı satır değildir: ikisi de sonu cezmeder; ama لَمْ geçmişi düz nefyeder (cahd-ı mutlak), "
                                  "لَمَّا ise şu âna kadar nefyeder, iş hâlâ beklenir (cahd-ı müstağrak)."})],
        related=["thulathi-mujarrad-babs", "masdar", "imperative-amr", "emsile-01-madi", "emsile-18-abwab"],
        sources=["الأمثلة المختلفة (Emsile)", "تصريف العزي (الزنجاني)", "المقصود في الصرف", f"{SHEET}، س 8–22 — Türkçe sîga adları"],
    )

    # 01 — the māḍī
    N["emsile-01-madi"] = dict(
        title=H("الْفِعْلُ الْمَاضِي — نَصَرَ", "The past: نَصَرَ through its fourteen persons", "Mâzî: نَصَرَ ve on dört sîgası"),
        plain={"en": "نَصَرَ means «he helped». The stem نَصَر does not change; what changes is the ending, and the ending IS the doer: "
                     "ـُوا «they», ـْتَ «you», ـْتُ «I», ـْنَا «we». Only «he» and «she» have no letter for the doer — it is hidden.",
               "tr": "نَصَرَ «yardım etti» demektir. Kök نَصَر değişmez; değişen sondur ve son, FÂİLİN kendisidir: ـُوا «onlar», ـْتَ «sen», "
                     "ـْتُ «ben», ـْنَا «biz». Yalnız «o (eril)» ve «o (dişil)» için fâilin harfi yoktur — zamir müstetirdir."},
        explanation={
            "en": "The māḍī is the first row of the Amthila and the first paradigm of the Muṭṭarida. Read the table from the top: three for "
                  "the absent man (one, two, many), three for the absent woman, three for the man addressed, three for the woman addressed, two "
                  "for the speaker. The māḍī is mabnī (built): its last radical does not take iʿrāb. It stays on a fatḥa — نَصَرَ، نَصَرَا، نَصَرَتْ، "
                  "نَصَرَتَا — except before the wāw of the group, where it takes a ḍamma (نَصَرُوا), and before an attached marfūʿ pronoun that "
                  "has a vowel of its own (the nūn of women, the tāʾ, نَا), where it takes a sukūn (نَصَرْنَ، نَصَرْتَ، نَصَرْنَا). That sukūn is the "
                  "student's clue: a sukūn on the rāʾ means a pronoun follows. The endings column says which letters are added; the pronoun "
                  "column says which of them is the doer. Two endings are NOT pronouns: the tāʾ of نَصَرَتْ is the sign that the doer is feminine "
                  "(Marāḥ ch. 17 s21 — it stays even when the doer is named: نَصَرَتْ هِنْدٌ), so in نَصَرَ and نَصَرَتْ the doer is hidden, «may "
                  "hide» (hidden jāʾizan — a named doer can take its place). Below the active table stands the passive (majhūl): نُصِرَ «he was "
                  "helped» — a ḍamma on the first letter and a kasra before the last, the same endings after it. The last table shows the same "
                  "past in the six bābs of the bare verb: the first vowel pattern of the māḍī is fixed by hearing, not by rule.",
            "tr": "Mâzî, Emsile'nin ilk satırı ve Muttaride'nin ilk çekimidir. Cetveli yukarıdan oku: üçü gâib için (tek, iki, çok), üçü "
                  "gâibe için, üçü muhâtab için, üçü muhâtaba için, ikisi mütekellim için. Mâzî mebnîdir: son harfi i'rab almaz. Fetha üzere "
                  "kalır — نَصَرَ، نَصَرَا، نَصَرَتْ، نَصَرَتَا — yalnız cemaat vâvından önce damme alır (نَصَرُوا) ve kendi harekesi olan bir "
                  "muttasıl merfû zamirden önce (nûn-ı nisve, tâ, نَا) sükûn alır (نَصَرْنَ، نَصَرْتَ، نَصَرْنَا). Bu sükûn talebenin işaretidir: "
                  "râ sakin ise ardından bir zamir gelir. «Son» sütunu hangi harflerin eklendiğini, «zamir» sütunu bunlardan hangisinin fâil "
                  "olduğunu söyler. İki son zamir DEĞİLDİR: نَصَرَتْ'in tâsı fâilin müennes olduğunun alâmetidir (Merâh 17. bölüm s21 — fâil açıkça "
                  "söylenince de kalır: نَصَرَتْ هِنْدٌ); bu yüzden نَصَرَ ve نَصَرَتْ'te fâil cevâzen müstetirdir (yerine açık bir fâil gelebilir). "
                  "Ma'lûm cetvelin altında meçhûl durur: نُصِرَ «yardım olundu» — ilk harf damme, sondan öncesi kesre, sonlar aynı. Son cetvel aynı "
                  "mâzîyi sülâsî mücerredin altı bâbında gösterir: mâzînin harekesi kaideyle değil semâ' ile bilinir."},
        tables=[tab("act", H("الْمَاضِي الْمَعْلُومُ", "Past, active — ending and doer", "Mâzî ma'lûm — son ve fâil"), {"k": "block", "root": R, "bab": 1, "list": "maziM"},
                    rows=S14, endsOf=R, pronOf="mazi", keys=raf_keys(S14, {0, 3})),
                tab("pas", H("الْمَاضِي الْمَجْهُولُ", "Past, passive", "Mâzî meçhûl"), {"k": "block", "root": R, "bab": 1, "list": "maziJ"}, rows=S14, endsOf=R),
                tab("babs", H("الْمَاضِي فِي الْأَبْوَابِ السِّتَّةِ", "The past in the six bābs", "Altı bâbda mâzî"), {"k": "em", "slot": "mazi", "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=0,
        examples=[["tasrif-al-izzi", 5, "s3"], ["jumal-al-tadrib", 4, "s7"], ["al-kafiya", 3, "s11"]],
        mistakes=[dict(w={"src": {"k": "block", "root": R, "bab": 1, "list": "maziM"}, "i": 3}, r={"src": {"k": "block", "root": R, "bab": 1, "list": "maziM"}, "i": 12},
                       why={"en": "«I helped» is نَصَرْتُ — sukūn on the rāʾ, ḍamma on the tāʾ, and the tāʾ is the pronoun. نَصَرَتْ (fatḥa on the rāʾ, sukūn on "
                                  "the tāʾ) is «she helped», and its tāʾ is only the sign of the feminine.",
                            "tr": "«Yardım ettim» نَصَرْتُ'dur — râ sakin, tâ mazmum; tâ zamirdir. نَصَرَتْ (râ meftûh, tâ sakin) «yardım etti (o, dişil)» "
                                  "demektir; tâsı yalnız müennes alâmetidir."})],
        related=["al-fil-wal-madi-wal-mudari-fil-kafiya", "thulathi-mujarrad-babs", "naib-al-fail", "emsile-12-damir-raf-muttasil", "emsile-02-mudari"],
        sources=["تصريف العزي (الزنجاني)", "مراح الأرواح", "المقصود في الصرف"],
    )

    # 02 — the muḍāriʿ
    N["emsile-02-mudari"] = dict(
        title=H("الْفِعْلُ الْمُضَارِعُ — يَنْصُرُ", "The present–future: يَنْصُرُ through its fourteen persons", "Muzâri: يَنْصُرُ ve on dört sîgası"),
        plain={"en": "يَنْصُرُ «he helps / will help» is built from the māḍī: a prefix (أَ نَ يَ تَ — «أَنَيْتُ»), the first radical silenced, "
                     "the bāb's vowel on the middle one. Its last letter takes a ḍamma — it is muʿrab — unless a pronoun's nūn follows.",
               "tr": "يَنْصُرُ «yardım eder / edecek» mâzîden kurulur: başa muzâraat harfi (أَ نَ يَ تَ — «أَنَيْتُ»), birinci harf sakin, ortadaki "
                     "harfe bâbın harekesi. Son harfi damme alır — mu'rabdır — ardından zamirin nûnu gelmedikçe."},
        explanation={
            "en": "The muḍāriʿ is the second row. From نَصَرَ: put a prefix letter in front, silence the first radical (نْ), give the middle "
                  "radical the bāb's vowel (bāb 1: ḍamma — صُ), and end on a ḍamma: يَنْصُرُ. The prefix tells the person: يَـ for the absent "
                  "man (and the women's plural), تَـ for the absent woman and for every «you», أَ for «I», نَ for «we». Unlike the māḍī, the "
                  "muḍāriʿ is muʿrab: its ending changes with the governor (the next note shows the particles). With no governor it is marfūʿ — "
                  "by the ḍamma in the bare singulars, by the nūn that stays (ثُبُوتُ النُّونِ) in the five verbs يَنْصُرَانِ، تَنْصُرَانِ، يَنْصُرُونَ، "
                  "تَنْصُرُونَ، تَنْصُرِينَ. The nūn of women (يَنْصُرْنَ، تَنْصُرْنَ) is a pronoun, and before it the verb is mabnī on a sukūn. "
                  "Pronoun column: the alif of the dual, the wāw of the group, the yāʾ of the woman addressed and the nūn of women are the doer, "
                  "written; in يَنْصُرُ and تَنْصُرُ («she») the doer may hide; in تَنْصُرُ («you»), أَنْصُرُ and نَنْصُرُ it MUST hide — the prefix "
                  "already names it and no noun can stand in its place (Marāḥ ch. 17 s24). The passive, يُنْصَرُ «he is helped», has a ḍamma on "
                  "the prefix and a fatḥa before the last letter. In the six bābs the middle vowel of the muḍāriʿ is what tells the bāb apart.",
            "tr": "Muzâri ikinci satırdır. نَصَرَ'den: başa muzâraat harfi koy, birinci harfi sakin kıl (نْ), ortadaki harfe bâbın harekesini "
                  "ver (birinci bâb: damme — صُ), dammeyle bitir: يَنْصُرُ. Baştaki harf sîgayı söyler: يَـ gâib için (ve cem'-i müennes gâibe "
                  "için), تَـ gâibe için ve her «sen/siz» için, أَ «ben», نَ «biz» için. Mâzînin aksine muzâri mu'rabdır: sonu âmile göre değişir "
                  "(sonraki not harfleri gösterir). Âmil yoksa merfûdur — müfredlerde damme ile, ef'âl-i hamsede (يَنْصُرَانِ، تَنْصُرَانِ، يَنْصُرُونَ، "
                  "تَنْصُرُونَ، تَنْصُرِينَ) nûnun sübûtu ile. Nûn-ı nisve (يَنْصُرْنَ، تَنْصُرْنَ) zamirdir; ondan önce fiil sükûn üzere mebnîdir. "
                  "Zamir sütunu: tesniye elifi, cemaat vâvı, muhâtaba yâsı ve nûn-ı nisve yazılı fâildir; يَنْصُرُ ve تَنْصُرُ'da («o, dişil») fâil "
                  "cevâzen müstetirdir; تَنْصُرُ («sen»), أَنْصُرُ ve نَنْصُرُ'da VÜCÛBEN müstetirdir — baştaki harf onu zaten söyler, yerine bir isim "
                  "gelemez (Merâh 17. bölüm s24). Meçhûl يُنْصَرُ «yardım olunur»: muzâraat harfi mazmum, sondan öncesi meftûh. Altı bâbda bâbı "
                  "ayıran, muzârinin ortadaki harekesidir."},
        tables=[tab("act", H("الْمُضَارِعُ الْمَعْلُومُ", "Present, active — ending and doer", "Muzâri ma'lûm — son ve fâil"), {"k": "mud", "root": R, "bab": 1},
                    rows=S14, endsOf=R, pronOf="mud", keys=raf_keys(S14, {0, 3, 6, 12, 13})),
                tab("pas", H("الْمُضَارِعُ الْمَجْهُولُ", "Present, passive", "Muzâri meçhûl"), {"k": "block", "root": R, "bab": 1, "list": "mudariJ"}, rows=S14, endsOf=R),
                tab("babs", H("الْمَاضِي وَالْمُضَارِعُ فِي الْأَبْوَابِ السِّتَّةِ", "Past and present in the six bābs", "Altı bâbda mâzî ve muzâri"),
                    {"k": "em2", "slots": ["mazi", "mudari"], "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=0,
        examples=[["tasrif-al-izzi", 6, "s9"], ["salih-wa-al-naqa", 4, "s10"]],
        mistakes=[dict(w={"src": {"k": "mud", "root": R, "bab": 1}, "i": 2}, r={"src": {"k": "mud", "root": R, "bab": 1}, "i": 5},
                       why={"en": "For women «they help» is يَنْصُرْنَ — the nūn of women is the doer, and the verb before it is silent on the rāʾ. "
                                  "يَنْصُرُونَ is the men's plural.",
                            "tr": "Kadınlar için «yardım ederler» يَنْصُرْنَ'dir — nûn-ı nisve fâildir, ondan önce râ sakindir. يَنْصُرُونَ erkeklerin "
                                  "cem'idir."})],
        related=["mudari-marfu", "al-fil-wal-madi-wal-mudari-fil-kafiya", "afal-khamsa", "emsile-06-nafy", "emsile-12-damir-raf-muttasil"],
        sources=["تصريف العزي (الزنجاني)", "مراح الأرواح", "المقصود في الصرف"],
    )

    # 03 — maṣdar, marra, nawʿ
    N["emsile-03-masdar"] = dict(
        title=H("الْمَصْدَرُ وَبِنَاءُ الْمَرَّةِ وَالنَّوْعِ", "The verbal noun, the noun of once and the noun of manner", "Masdar, binâ-i merre ve binâ-i nev'"),
        plain={"en": "نَصْرًا is «helping» — the deed with no time and no doer. نَصْرَةً (fatḥa first) is «helping once»; نِصْرَةً (kasra first) "
                     "is «a manner of helping». The bare verb's maṣdar is learnt by hearing; the two others are built from it by rule.",
               "tr": "نَصْرًا «yardım etmek»tir — zamansız ve fâilsiz iş. نَصْرَةً (ilk harf meftûh) «bir kere yardım etmek»; نِصْرَةً (ilk harf "
                     "meksûr) «bir çeşit yardım etmek». Mücerred fiilin masdarı işitilerek öğrenilir; diğer ikisi ondan kaideyle kurulur."},
        explanation={
            "en": "The third row of the Amthila is the maṣdar, the name of the deed itself. The madrasa recites it in the accusative, نَصْرًا, "
                  "because in the row it is the absolute object of the verb before it (نَصَرَ … نَصْرًا). The maṣdar of the three-letter bare verb "
                  "has many measures and is known by hearing (samāʿī) — this is why the app's engine leaves it unbuilt and the table shows the "
                  "corpus's own word from a sentence of the stories. From the bare verb's maṣdar two nouns ARE built by rule (Taṣrīf al-ʿIzzī, "
                  "the chapter on the noun of once): فَعْلَةٌ, with a fatḥa on the first letter, for doing it ONCE — ضَرَبْتُ ضَرْبَةً «I struck one "
                  "blow»; and فِعْلَةٌ, with a kasra, for the MANNER of doing it. The Amthila recites both with the ending -ةً. The only "
                  "difference between them is the first vowel, so read it carefully. The tables show the two in the six bābs, built by the engine.",
            "tr": "Emsile'nin üçüncü satırı masdardır, işin kendi adı. Medrese onu mansûb okur, نَصْرًا, çünkü satırda kendinden önceki fiilin "
                  "mef'ûl-i mutlakıdır (نَصَرَ … نَصْرًا). Sülâsî mücerredin masdarının birçok vezni vardır ve işitilerek bilinir (semâî) — bu "
                  "yüzden uygulamanın motoru onu kurmaz; cetvel hikâyelerdeki bir cümleden külliyatın kendi kelimesini gösterir. Mücerredin "
                  "masdarından iki isim ise kaideyle KURULUR (Tasrîfu'l-İzzî, binâ-i merre bahsi): ilk harfi meftûh فَعْلَةٌ, işi BİR KERE yapmak "
                  "için — ضَرَبْتُ ضَرْبَةً «bir kere vurdum»; ilk harfi meksûr فِعْلَةٌ, işin YAPILIŞ ŞEKLİ için. Emsile ikisini de -ةً ile okur. "
                  "Aralarındaki tek fark ilk harekedir, onu dikkatle oku. Cetveller ikisini altı bâbda, motorun kurduğu şekliyle gösterir."},
        tables=[tab("row", H("الْمَصْدَرُ، الْمَرَّةُ، النَّوْعُ", "Verbal noun, once, manner", "Masdar, merre, nev'"),
                    {"k": "row", "root": R, "bab": 1, "slots": ["masdar", "marra", "naw"], "corpus": {"masdar": MASDAR_TOK}},
                    labels=[{"ar": f[2], "tr": f[3], "en": f[4], "m": {"en": f[5], "tr": f[6]}} for f in FORMS if f[0] in ("masdar", "marra", "naw")]),
                tab("marra", H("بِنَاءُ الْمَرَّةِ فِي الْأَبْوَابِ السِّتَّةِ", "The noun of once in the six bābs", "Altı bâbda binâ-i merre"), {"k": "em", "slot": "marra", "models": [0, 1, 2, 3, 4, 5]}, bab=True),
                tab("naw", H("بِنَاءُ النَّوْعِ فِي الْأَبْوَابِ السِّتَّةِ", "The noun of manner in the six bābs", "Altı bâbda binâ-i nev'"), {"k": "em", "slot": "naw", "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=0,
        examples=[["jumal-al-tadrib", 4, "s7"], ["tasrif-al-izzi", 19, "s6"], ["tasrif-al-izzi", 19, "s8"]],
        mistakes=[dict(w={"src": {"k": "em", "slot": "naw"}, "i": 0}, r={"src": {"k": "em", "slot": "marra"}, "i": 0},
                       why={"en": "«Helping once» is نَصْرَةً with a fatḥa (faʿla); نِصْرَةً with a kasra (fiʿla) is the manner of helping.",
                            "tr": "«Bir kere yardım» fetha ile نَصْرَةً'dir (فَعْلَة); kesre ile نِصْرَةً (فِعْلَة) yardımın şeklidir."})],
        related=["masdar", "ism-al-marra-wal-naw", "al-masdar-fil-kafiya", "emsile-00-amthila"],
        sources=["تصريف العزي (الزنجاني)", "مراح الأرواح"],
    )

    # 04 — ism fāʿil and mubālagha
    N["emsile-04-fail"] = dict(
        title=H("اسْمُ الْفَاعِلِ وَصِيغَةُ الْمُبَالَغَةِ", "The active participle and its intensive", "İsm-i fâil ve mübalağası"),
        plain={"en": "نَاصِرٌ is «a helper, one who helps» — built on فَاعِلٌ from the bare verb. نَصَّارٌ (فَعَّالٌ) is «one who helps a great "
                     "deal». The Amthila recites the first as فَهُوَ نَاصِرٌ, «so he is a helper».",
               "tr": "نَاصِرٌ «yardım eden»dir — mücerred fiilden فَاعِلٌ vezninde kurulur. نَصَّارٌ (فَعَّالٌ) «çok yardım eden»dir. Emsile "
                     "birincisini فَهُوَ نَاصِرٌ, «o hâlde o, yardım edendir» diye okur."},
        explanation={
            "en": "The fourth row names the one who does the deed. From the bare three-letter verb it is built on فَاعِلٌ: an alif after the "
                  "first radical and a kasra under the second — نَاصِرٌ. It is a noun, so it is muʿrab and declines; its Muṭṭarida is not by "
                  "person but by number and gender: نَاصِرٌ، نَاصِرَانِ، نَاصِرُونَ for men; نَاصِرَةٌ، نَاصِرَتَانِ، نَاصِرَاتٌ for women. The "
                  "endings column shows what is added: -َانِ for two, -ُونَ for the sound plural, -َةٌ for the feminine. These endings are signs, "
                  "not pronouns — the alif of نَاصِرَانِ turns to yāʾ in naṣb and jarr (نَاصِرَيْنِ), and a pronoun does not change (Marāḥ ch. 17 "
                  "s22–s23); the doer of a participle hides in it. The books also recite broken plurals for it; the engine does not build broken "
                  "plurals, so they are not in this table — learn them from the book. The intensive (mubālagha) نَصَّارٌ on فَعَّالٌ says the "
                  "deed is done much or often; it is one of several measures and, like the maṣdar, is heard rather than built for every verb.",
            "tr": "Dördüncü satır işi yapanı adlandırır. Sülâsî mücerredden فَاعِلٌ vezninde kurulur: birinci harften sonra elif, ikinci harfin "
                  "altında kesre — نَاصِرٌ. İsimdir, bu yüzden mu'rabdır; Muttaride'si sîgaya göre değil sayı ve cinse göredir: erkekler için "
                  "نَاصِرٌ، نَاصِرَانِ، نَاصِرُونَ; kadınlar için نَاصِرَةٌ، نَاصِرَتَانِ، نَاصِرَاتٌ. «Son» sütunu ekleneni gösterir: iki için "
                  "-َانِ, cem'-i sâlim için -ُونَ, müennes için -َةٌ. Bu sonlar zamir değil, alâmettir — نَاصِرَانِ'nin elifi nasb ve cerde yâya "
                  "döner (نَاصِرَيْنِ), zamir ise değişmez (Merâh 17. bölüm s22–s23); ism-i fâilin fâili onda müstetirdir. Kitaplar ism-i fâilin "
                  "cem'-i mükesserlerini de okur; motor cem'-i mükesser kurmaz, onun için bu cetvelde yoktur — kitaptan öğren. Mübalağa نَصَّارٌ "
                  "(فَعَّالٌ) işin çok ya da sık yapıldığını söyler; birkaç vezinden biridir ve masdar gibi her fiil için kurulmaz, işitilir."},
        tables=[tab("num", H("اسْمُ الْفَاعِلِ — الْمُطَّرِدَةُ", "Active participle by number and gender", "İsm-i fâil — sayı ve cinsiyle"),
                    {"k": "block", "root": R, "bab": 1, "list": "fail", "take": [0, 1, 2, 6, 7, 8]}, labels=NUM6, endsOf=R),
                tab("babs", H("اسْمُ الْفَاعِلِ فِي الْأَبْوَابِ السِّتَّةِ", "The active participle in the six bābs", "Altı bâbda ism-i fâil"), {"k": "em", "slot": "fail", "models": [0, 1, 2, 3, 4, 5]}, bab=True),
                tab("mub", H("صِيغَةُ الْمُبَالَغَةِ (فَعَّالٌ)", "The intensive (faʿʿāl) in the six bābs", "Altı bâbda mübalağa (فَعَّالٌ)"), {"k": "em", "slot": "mubalagha", "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=0,
        examples=[["tasrif-al-izzi", 11, "s1"], ["al-kafiya", 16, "s8"]],
        mistakes=[dict(w={"src": {"k": "em", "slot": "maful"}, "i": 0}, r={"src": {"k": "em", "slot": "fail"}, "i": 0},
                       why={"en": "The one who helps is نَاصِرٌ (فَاعِلٌ); مَنْصُورٌ (مَفْعُولٌ) is the one who is helped.",
                            "tr": "Yardım eden نَاصِرٌ'dir (فَاعِلٌ); مَنْصُورٌ (مَفْعُولٌ) yardım olunandır."})],
        related=["ism-fail", "ism-al-fail-wal-maful-fil-kafiya", "sighat-mubalagha", "mubalagha-maqbula", "emsile-05-maful"],
        sources=["تصريف العزي (الزنجاني)", "مراح الأرواح", "المقصود في الصرف"],
    )

    # 05 — ism mafʿūl
    N["emsile-05-maful"] = dict(
        title=H("اسْمُ الْمَفْعُولِ — مَنْصُورٌ", "The passive participle: مَنْصُورٌ", "İsm-i mef'ûl: مَنْصُورٌ"),
        plain={"en": "مَنْصُورٌ is «helped, one who is helped» — built on مَفْعُولٌ from the bare verb. The Amthila recites it as وَذَاكَ مَنْصُورٌ, "
                     "«and that one is helped».",
               "tr": "مَنْصُورٌ «yardım olunan»dır — mücerred fiilden مَفْعُولٌ vezninde kurulur. Emsile onu وَذَاكَ مَنْصُورٌ, «şu da yardım "
                     "olunandır» diye okur."},
        explanation={
            "en": "The fifth row names the one the deed falls on. From the bare verb it is built on مَفْعُولٌ: a mīm with a fatḥa in front, the "
                  "first radical silent, a wāw after the ḍamma of the second — مَنْصُورٌ. Only a verb that takes an object has it directly; an "
                  "intransitive verb makes it with a preposition and its pronoun (مَمْرُورٌ بِهِ), and in that case it is the pronoun after the "
                  "preposition that changes from person to person, not the participle (Taṣrīf al-ʿIzzī, the chapter on the two participles). "
                  "Its Muṭṭarida, like the active participle's, is by number and gender: مَنْصُورٌ، مَنْصُورَانِ، مَنْصُورُونَ; مَنْصُورَةٌ، "
                  "مَنْصُورَتَانِ، مَنْصُورَاتٌ (the book adds a broken plural, which the engine does not build). The verb whose meaning it shares "
                  "is the passive نُصِرَ يُنْصَرُ: what is مَنْصُورٌ is what نُصِرَ.",
            "tr": "Beşinci satır işin üzerine düştüğü kimseyi adlandırır. Mücerredden مَفْعُولٌ vezninde kurulur: başa meftûh mîm, birinci harf "
                  "sakin, ikinci harfin dammesinden sonra vâv — مَنْصُورٌ. Ancak mef'ûl alan fiilin doğrudan ism-i mef'ûlü olur; lâzım fiil onu bir "
                  "cer harfi ve zamiriyle yapar (مَمْرُورٌ بِهِ) ve o zaman sîgadan sîgaya değişen ism-i mef'ûl değil, cer harfinden sonraki zamirdir "
                  "(Tasrîfu'l-İzzî, ism-i fâil ve mef'ûl bahsi). Muttaride'si ism-i fâilinki gibi sayı ve cinse göredir: مَنْصُورٌ، مَنْصُورَانِ، "
                  "مَنْصُورُونَ; مَنْصُورَةٌ، مَنْصُورَتَانِ، مَنْصُورَاتٌ (kitap bir de cem'-i mükesser ekler; motor onu kurmaz). Anlamını paylaştığı "
                  "fiil meçhûl نُصِرَ يُنْصَرُ'dur: مَنْصُورٌ olan, نُصِرَ olandır."},
        tables=[tab("num", H("اسْمُ الْمَفْعُولِ — الْمُطَّرِدَةُ", "Passive participle by number and gender", "İsm-i mef'ûl — sayı ve cinsiyle"),
                    {"k": "block", "root": R, "bab": 1, "list": "maful", "take": [0, 1, 2, 3, 4, 5]}, labels=NUM6, endsOf=R),
                tab("babs", H("اسْمُ الْمَفْعُولِ فِي الْأَبْوَابِ السِّتَّةِ", "The passive participle in the six bābs", "Altı bâbda ism-i mef'ûl"), {"k": "em", "slot": "maful", "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=0,
        examples=[["tasrif-al-izzi", 11, "s2"]],
        mistakes=[dict(w={"src": {"k": "block", "root": R, "bab": 1, "list": "maful"}, "i": 2}, r={"src": {"k": "block", "root": R, "bab": 1, "list": "maful"}, "i": 5},
                       why={"en": "Women who are helped are مَنْصُورَاتٌ (sound feminine plural); مَنْصُورُونَ is for men.",
                            "tr": "Yardım olunan kadınlar مَنْصُورَاتٌ'tır (cem'-i müennes sâlim); مَنْصُورُونَ erkekler içindir."})],
        related=["ism-al-fail-wal-maful-fil-kafiya", "naib-al-fail", "emsile-04-fail", "emsile-01-madi"],
        sources=["تصريف العزي (الزنجاني)", "المقصود في الصرف"],
    )

    # 06 — the five negated / emphatic muḍāriʿ
    J = {"k": "jus", "root": R, "bab": 1}
    N["emsile-06-nafy"] = dict(
        title=H("لَمْ، لَمَّا، مَا، لَا، لَنْ — مَعَ الْمُضَارِعِ", "The five denials: what each particle does to the meaning and to the ending",
                "Beş nefiy: her harf anlama ve sona ne yapar"),
        plain={"en": "Five particles before يَنْصُرُ: لَمْ and لَمَّا turn it to the past and cut its ending (jazm); مَا (now) and لَا (later) deny "
                     "it and leave it marfūʿ; لَنْ denies the future firmly and gives it a fatḥa (naṣb). Watch the last letter.",
               "tr": "يَنْصُرُ'dan önce beş harf: لَمْ ve لَمَّا onu geçmişe çevirir ve sonunu keser (cezm); مَا (şimdi) ve لَا (gelecek) nefyeder ve "
                     "merfû bırakır; لَنْ geleceği kuvvetle nefyeder ve fetha verir (nasb). Son harfe bak."},
        explanation={
            "en": "Rows six to ten are one muḍāriʿ under five particles, and the student learns two things about each: the MEANING and the "
                  "ENDING. (1) لَمْ يَنْصُرْ — cahd-ı mutlak: «he did not help». لَمْ turns the present into the past and denies it; it is a jāzim: "
                  "the bare singulars lose their ḍamma to a sukūn (يَنْصُرْ), the five verbs lose their nūn (يَنْصُرَا، يَنْصُرُوا، تَنْصُرِي), the nūn "
                  "of women stays (يَنْصُرْنَ — it is a pronoun). (2) لَمَّا يَنْصُرْ — cahd-ı müstağrak: «he has not helped, up to now» (and it is still "
                  "expected); the same jazm. (3) مَا يَنْصُرُ — nefy-i hâl: «he is not helping now»; مَا governs nothing, the ending stays marfūʿ. "
                  "(4) لَا يَنْصُرُ — nefy-i istikbâl: «he will not help»; لَا governs nothing here either. (5) لَنْ يَنْصُرَ — te'kîd-i nefy-i istikbâl: "
                  "«he will never help»; لَنْ is a nāṣib: the bare singulars take a fatḥa (يَنْصُرَ), the five verbs lose their nūn just as in jazm, "
                  "the nūn of women stays (Taṣrīf al-ʿIzzī: «لَنْ يَنْصُرَ لَنْ يَنْصُرَا لَنْ يَنْصُرُوا …»). So the sign to look for is the last vowel "
                  "of the singular — sukūn, ḍamma or fatḥa — and, in the duals and plurals, whether the nūn is there. Each table's endings column "
                  "shows it. Keep apart لَا here (it only denies) and the لَا of prohibition in the next note (it commands NOT, and cuts the ending).",
            "tr": "Altıncı ile onuncu satırlar beş harfin altındaki tek bir muzâridir; talebe her biri için iki şey öğrenir: ANLAM ve SON. "
                  "(1) لَمْ يَنْصُرْ — cahd-ı mutlak: «yardım etmedi». لَمْ muzâriyi mâzîye çevirir ve nefyeder; câzimdir: müfredler dammeyi kaybedip "
                  "sakin olur (يَنْصُرْ), ef'âl-i hamse nûnu kaybeder (يَنْصُرَا، يَنْصُرُوا، تَنْصُرِي), nûn-ı nisve kalır (يَنْصُرْنَ — zamirdir). "
                  "(2) لَمَّا يَنْصُرْ — cahd-ı müstağrak: «şimdiye dek yardım etmedi» (hâlâ bekleniyor); aynı cezm. (3) مَا يَنْصُرُ — nefy-i hâl: "
                  "«şu an yardım etmiyor»; مَا amel etmez, son merfû kalır. (4) لَا يَنْصُرُ — nefy-i istikbâl: «yardım etmeyecek»; burada لَا da amel "
                  "etmez. (5) لَنْ يَنْصُرَ — te'kîd-i nefy-i istikbâl: «asla yardım etmeyecek»; لَنْ nâsıbdır: müfredler fetha alır (يَنْصُرَ), ef'âl-i "
                  "hamse cezmdeki gibi nûnu kaybeder, nûn-ı nisve kalır (Tasrîfu'l-İzzî: «لَنْ يَنْصُرَ لَنْ يَنْصُرَا لَنْ يَنْصُرُوا …»). Demek ki "
                  "bakılacak işaret müfredin son harekesidir — sükûn, damme ya da fetha — ve tesniye ile cem'de nûnun bulunup bulunmadığıdır. Her "
                  "cetvelin «son» sütunu bunu gösterir. Buradaki لَا'yı (yalnız nefyeder) sonraki nottaki nehiy لَا'sından (yapma der ve sonu keser) ayır."},
        tables=[tab("lam", H("لَمْ يَنْصُرْ — الْجَحْدُ الْمُطْلَقُ", "لَمْ — jazm", "لَمْ — cezm"), dict(J, pre="لَمْ "), rows=S14, endsOf=R),
                tab("lamma", H("لَمَّا يَنْصُرْ — الْجَحْدُ الْمُسْتَغْرَقُ", "لَمَّا — jazm", "لَمَّا — cezm"), dict(J, pre="لَمَّا "), rows=S14, endsOf=R),
                tab("ma", H("مَا يَنْصُرُ — نَفْيُ الْحَالِ", "مَا — no change", "مَا — değişmez"), {"k": "mud", "root": R, "bab": 1, "pre": "مَا "}, rows=S14, endsOf=R),
                tab("la", H("لَا يَنْصُرُ — نَفْيُ الِاسْتِقْبَالِ", "لَا — no change", "لَا — değişmez"), {"k": "mud", "root": R, "bab": 1, "pre": "لَا "}, rows=S14, endsOf=R),
                tab("lan", H("لَنْ يَنْصُرَ — تَأْكِيدُ نَفْيِ الِاسْتِقْبَالِ", "لَنْ — naṣb", "لَنْ — nasb"), {"k": "nasb", "root": R, "bab": 1, "pre": "لَنْ "}, rows=S14, endsOf=R)],
        quiz=4,
        examples=[["qisas-al-nabiyyin-1", 3, "s24"], ["qarun-wa-kunuzuh", 4, "s3"], ["tasrif-al-izzi", 7, "s6"], ["tasrif-al-izzi", 7, "s3"],
                  ["tasrif-al-izzi", 7, "s2"], ["tasrif-al-izzi", 7, "s8"]],
        mistakes=[dict(w={"src": {"k": "mud", "root": R, "bab": 1, "pre": "لَمْ "}, "i": 2}, r={"src": dict(J, pre="لَمْ "), "i": 2},
                       why={"en": "لَمْ is a jāzim: in the five verbs it takes the nūn away — لَمْ يَنْصُرُوا, not لَمْ يَنْصُرُونَ.",
                            "tr": "لَمْ câzimdir: ef'âl-i hamsede nûnu düşürür — لَمْ يَنْصُرُوا, لَمْ يَنْصُرُونَ değil."}),
                  dict(w={"src": {"k": "mud", "root": R, "bab": 1, "pre": "لَنْ "}, "i": 0}, r={"src": {"k": "nasb", "root": R, "bab": 1, "pre": "لَنْ "}, "i": 0},
                       why={"en": "لَنْ is a nāṣib: the singular ends on a fatḥa — لَنْ يَنْصُرَ.", "tr": "لَنْ nâsıbdır: müfred fethayla biter — لَنْ يَنْصُرَ."}),
                  dict(w={"src": dict(J, pre="مَا "), "i": 0}, r={"src": {"k": "mud", "root": R, "bab": 1, "pre": "مَا "}, "i": 0},
                       why={"en": "مَا before the muḍāriʿ governs nothing: the ḍamma stays — مَا يَنْصُرُ.", "tr": "Muzâriden önce مَا amel etmez: damme kalır — مَا يَنْصُرُ."})],
        related=["lam-jazim", "la-nafiya", "nawasib-wa-jawazim-al-mudari", "nawasib-al-mudari-fil-kafiya", "jawazim-al-mudari-wal-amr-fil-kafiya", "emsile-07-amr-nahy"],
        sources=["تصريف العزي (الزنجاني)", "مراح الأرواح", "إظهار الأسرار (البركوي)"],
    )

    # 07 — amr and nahy, absent and present
    N["emsile-07-amr-nahy"] = dict(
        title=H("أَمْرُ الْغَائِبِ وَنَهْيُهُ، أَمْرُ الْحَاضِرِ وَنَهْيُهُ", "Command and prohibition — to the absent, to the one present",
                "Emr-i gâib, nehy-i gâib, emr-i hâzır, nehy-i hâzır"),
        plain={"en": "لِيَنْصُرْ «let him help», لَا يَنْصُرْ «let him not help», اُنْصُرْ «help!», لَا تَنْصُرْ «don't help!». All four end in jazm. "
                     "The amr to «you» drops the prefix تَـ and puts a joining hamza in front: تَنْصُرْ → اُنْصُرْ.",
               "tr": "لِيَنْصُرْ «yardım etsin», لَا يَنْصُرْ «yardım etmesin», اُنْصُرْ «yardım et!», لَا تَنْصُرْ «yardım etme!». Dördü de meczûmdur. "
                     "Muhâtaba emir تَـ harfini atar, başa vasıl hemzesi getirir: تَنْصُرْ → اُنْصُرْ."},
        explanation={
            "en": "Rows eleven to fourteen give orders. The order to someone absent uses the lām of command, لِيَنْصُرْ «let him help»; the "
                  "prohibition to someone absent uses the لَا of prohibition, لَا يَنْصُرْ. Both are jāzims, so the endings are exactly those of "
                  "لَمْ: sukūn on the singulars, the nūn dropped from the duals and the men's plural, the women's nūn kept. The order to the one "
                  "present (emr-i hâzır) is built from the jussive of «you»: drop the prefix تَـ from تَنْصُرْ; what remains (نْصُرْ) starts on a "
                  "silent letter, so a joining hamza comes in front, and it takes a ḍamma because the middle radical has a ḍamma — اُنْصُرْ "
                  "(in bāb 2 it is a kasra: اِضْرِبْ; Taṣrīf al-ʿIzzī, the chapter on the command). The amr has six persons only — all «you» — and "
                  "it is mabnī on what its jussive would end in (sukūn, or the dropped nūn). The prohibition to the one present is simply لَا "
                  "before the jussive of «you»: لَا تَنْصُرْ. The doer of اُنْصُرْ is a hidden أَنْتَ that must stay hidden; in the others the "
                  "pronoun is written (اُنْصُرَا، اُنْصُرُوا، اُنْصُرِي، اُنْصُرْنَ). There is no command for «I» and «we» in this table, because, the "
                  "Maqṣūd says, one person cannot at one moment give the order and receive it.",
            "tr": "On birinci ile on dördüncü satırlar emir verir. Gâibe emir emir lâmı ile yapılır, لِيَنْصُرْ «yardım etsin»; gâibe nehiy nehiy "
                  "lâ'sı ile, لَا يَنْصُرْ. İkisi de câzimdir; sonlar tam لَمْ'deki gibidir: müfredlerde sükûn, tesniye ve cem'-i müzekkerde nûn düşer, "
                  "nûn-ı nisve kalır. Emr-i hâzır, «sen»in meczûm muzârisinden kurulur: تَنْصُرْ'dan تَـ harfini at; kalan (نْصُرْ) sakin harfle "
                  "başlar, bu yüzden başa vasıl hemzesi gelir ve ortadaki harf mazmum olduğu için damme alır — اُنْصُرْ (ikinci bâbda kesre: "
                  "اِضْرِبْ; Tasrîfu'l-İzzî, emir bahsi). Emrin yalnız altı sîgası vardır — hepsi «sen/siz» — ve meczûmunun biteceği şey üzere "
                  "mebnîdir (sükûn ya da düşen nûn). Nehy-i hâzır, «sen»in meczûmundan önce لَا'dır: لَا تَنْصُرْ. اُنْصُرْ'un fâili vücûben müstetir "
                  "أَنْتَ'dir; diğerlerinde zamir yazılıdır (اُنْصُرَا، اُنْصُرُوا، اُنْصُرِي، اُنْصُرْنَ). Bu cetvelde «ben» ve «biz» için emir yoktur, "
                  "çünkü Maksûd'un dediği gibi bir kişi bir anda hem âmir hem me'mûr olamaz."},
        tables=[tab("amrGh", H("أَمْرُ الْغَائِبِ — لِيَنْصُرْ", "Command to the absent", "Emr-i gâib"), {"k": "recite", "root": R, "bab": 1, "list": "amrGh"}, rows=GH6, endsOf=R),
                tab("nahyGh", H("نَهْيُ الْغَائِبِ — لَا يَنْصُرْ", "Prohibition to the absent", "Nehy-i gâib"), {"k": "recite", "root": R, "bab": 1, "list": "nahyGh"}, rows=GH6, endsOf=R),
                tab("amr", H("أَمْرُ الْحَاضِرِ — اُنْصُرْ", "Command to the one present — ending and doer", "Emr-i hâzır — son ve fâil"), {"k": "amr", "root": R, "bab": 1},
                    rows=AMR6, endsOf=R, pronOf="amr", keys=raf_keys(AMR6, {6})),
                tab("nahyH", H("نَهْيُ الْحَاضِرِ — لَا تَنْصُرْ", "Prohibition to the one present", "Nehy-i hâzır"), {"k": "recite", "root": R, "bab": 1, "list": "nahyH"}, rows=AMR6, endsOf=R),
                tab("babs", H("أَمْرُ الْحَاضِرِ فِي الْأَبْوَابِ السِّتَّةِ", "The command in the six bābs", "Altı bâbda emr-i hâzır"), {"k": "em", "slot": "amr", "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=2,
        examples=[["tasrif-al-izzi", 7, "s9"], ["tasrif-al-izzi", 7, "s11"], ["tasrif-al-izzi", 7, "s12"], ["dawud-wa-jalut", 2, "s8"]],
        mistakes=[dict(w={"src": {"k": "mud", "root": R, "bab": 1, "pre": "لَا "}, "i": 6}, r={"src": {"k": "recite", "root": R, "bab": 1, "list": "nahyH"}, "i": 0},
                       why={"en": "«Don't help!» is لَا تَنْصُرْ with a sukūn — the لَا of prohibition is a jāzim. لَا تَنْصُرُ with a ḍamma only says «you will not help».",
                            "tr": "«Yardım etme!» sükûnla لَا تَنْصُرْ'dur — nehiy lâ'sı câzimdir. Dammeyle لَا تَنْصُرُ yalnız «yardım etmeyeceksin» demektir."}),
                  dict(w={"src": {"k": "mud", "root": R, "bab": 1, "pre": "لِ"}, "i": 2}, r={"src": {"k": "recite", "root": R, "bab": 1, "list": "amrGh"}, "i": 2},
                       why={"en": "The lām of command is a jāzim: لِيَنْصُرُوا, the nūn gone.", "tr": "Emir lâmı câzimdir: لِيَنْصُرُوا, nûn düşer."})],
        related=["imperative-amr", "lam-amr", "jawab-al-talab", "jawazim-al-mudari-wal-amr-fil-kafiya", "emsile-06-nafy", "emsile-12-damir-raf-muttasil"],
        sources=["تصريف العزي (الزنجاني)", "المقصود في الصرف", "مراح الأرواح"],
    )

    # 08 — ism zamān-makān and ism āla
    N["emsile-08-zaman-ala"] = dict(
        title=H("اسْمُ الزَّمَانِ وَالْمَكَانِ، وَاسْمُ الْآلَةِ", "The noun of time and place, and the noun of instrument", "İsm-i zaman ve mekân, ism-i âlet"),
        plain={"en": "مَنْصَرٌ (fatḥa on the mīm) is the time or place of helping; مِنْصَرٌ (kasra on the mīm) is the tool of helping. One vowel "
                     "tells them apart: «الْمَفْعَلُ لِلْمَوْضِعِ وَالْمِفْعَلُ لِلْآلَةِ».",
               "tr": "مَنْصَرٌ (mîm meftûh) yardımın zamanı ya da yeridir; مِنْصَرٌ (mîm meksûr) yardımın âletidir. Onları bir hareke ayırır: "
                     "«الْمَفْعَلُ لِلْمَوْضِعِ وَالْمِفْعَلُ لِلْآلَةِ»."},
        explanation={
            "en": "Rows fifteen and sixteen are two nouns with a mīm in front. The noun of time and place is built from the muḍāriʿ: where "
                  "the muḍāriʿ has a ḍamma or a fatḥa on its middle radical (يَنْصُرُ، يَفْتَحُ) it is مَفْعَلٌ — مَنْصَرٌ، مَفْتَحٌ; where it has a "
                  "kasra (يَضْرِبُ، يَحْسِبُ) it is مَفْعِلٌ — مَضْرِبٌ، مَحْسِبٌ (Marāḥ: «وَلَا يُبْنَى مِنْ يَفْعُلُ مَفْعُلٌ لِثِقَلِ الضَّمَّةِ»). Where the "
                  "ʿayn is not kasra the same shape serves the mīmī maṣdar; after a kasra the maṣdar keeps the fatḥa (al-Maqṣūd). The noun of instrument is مِفْعَلٌ, with a KASRA on the mīm — «and the mīm was given a kasra to tell it apart "
                  "from the place» (Marāḥ) — and it also comes on مِفْعَالٌ and مِفْعَلَةٌ. The madrasa line the books quote: «الْمَفْعَلُ لِلْمَوْضِعِ "
                  "وَالْمِفْعَلُ لِلْآلَةِ، وَالْفَعْلَةُ لِلْمَرَّةِ وَالْفِعْلَةُ لِلْحَالَةِ». The Amthila recites both on every verb, even where a real "
                  "word of that shape is not used: it is a drill of the patterns. The received sheet adds that the augmented bābs have no noun of "
                  "instrument.",
            "tr": "On beşinci ve on altıncı satırlar başında mîm olan iki isimdir. İsm-i zaman ve mekân muzâriden kurulur: muzârinin ortadaki "
                  "harfi mazmum ya da meftûh ise (يَنْصُرُ، يَفْتَحُ) مَفْعَلٌ'dir — مَنْصَرٌ، مَفْتَحٌ; meksûr ise (يَضْرِبُ، يَحْسِبُ) مَفْعِلٌ'dir — مَضْرِبٌ، مَحْسِبٌ "
                  "(Merâh: «وَلَا يُبْنَى مِنْ يَفْعُلُ مَفْعُلٌ لِثِقَلِ الضَّمَّةِ»). Ayn meksûr değilse aynı kalıp masdar-ı mîmîye de yarar; meksûrsa masdar fethalı kalır (Maksûd). İsm-i âlet mîmi KESRELİ "
                  "مِفْعَلٌ'dir — «mîm, mekândan ayrılsın diye kesrelendi» (Merâh) — ve مِفْعَالٌ ile مِفْعَلَةٌ vezinlerinde de gelir. Kitapların andığı "
                  "medrese beyti: «الْمَفْعَلُ لِلْمَوْضِعِ وَالْمِفْعَلُ لِلْآلَةِ، وَالْفَعْلَةُ لِلْمَرَّةِ وَالْفِعْلَةُ لِلْحَالَةِ». Emsile ikisini her "
                  "fiilde okur, o kalıpta kullanılan bir kelime olmasa da: bu, vezinlerin talimidir. Gelen cetvel ziyade bâblarda ism-i âlet "
                  "gelmediğini ekler."},
        tables=[tab("row", H("مَنْصَرٌ وَمِنْصَرٌ", "Place and tool", "Mekân ve âlet"), {"k": "row", "root": R, "bab": 1, "slots": ["mimi", "alat"]},
                    labels=[{"ar": f[2], "tr": f[3], "en": f[4], "m": {"en": f[5], "tr": f[6]}} for f in FORMS if f[0] in ("mimi", "alat")]),
                tab("mimi", H("اسْمُ الزَّمَانِ وَالْمَكَانِ فِي الْأَبْوَابِ السِّتَّةِ", "Time and place in the six bābs", "Altı bâbda ism-i zaman ve mekân"), {"k": "em", "slot": "mimi", "models": [0, 1, 2, 3, 4, 5]}, bab=True),
                tab("alat", H("اسْمُ الْآلَةِ فِي الْأَبْوَابِ السِّتَّةِ", "The instrument in the six bābs", "Altı bâbda ism-i âlet"), {"k": "em", "slot": "alat", "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=1,
        examples=[["marah-al-arwah", 41, "s4"], ["marah-al-arwah", 41, "s7"], ["marah-al-arwah", 42, "s3"], ["tasrif-al-izzi", 19, "s1"]],
        mistakes=[dict(w={"src": {"k": "em", "slot": "alat"}, "i": 0}, r={"src": {"k": "em", "slot": "mimi"}, "i": 0},
                       why={"en": "The place of helping is مَنْصَرٌ with a fatḥa on the mīm; مِنْصَرٌ with a kasra is the tool.",
                            "tr": "Yardımın yeri mîmi meftûh مَنْصَرٌ'dır; mîmi meksûr مِنْصَرٌ âlettir."})],
        related=["ism-al-zaman-wal-makan", "ism-al-ala", "emsile-03-masdar", "emsile-00-amthila"],
        sources=["مراح الأرواح", "تصريف العزي (الزنجاني)", f"{SHEET}، س 23 — ZİYADE BABLARDAN İSMİ ALET … GELMEZ"],
    )

    # 09 — taṣghīr and nisba
    N["emsile-09-tasghir-nisba"] = dict(
        title=H("التَّصْغِيرُ وَالنِّسْبَةُ", "The diminutive and the relational adjective", "İsm-i tasğîr ve ism-i mensûb"),
        plain={"en": "نُصَيْرٌ is the diminutive, «a little help» — ḍamma, fatḥa, then a silent yāʾ: فُعَيْلٌ. نَصْرِيٌّ is «having to do with help» — "
                     "the maṣdar with a doubled yāʾ of relation: -ِيٌّ.",
               "tr": "نُصَيْرٌ küçültme ismidir, «küçük bir yardım» — damme, fetha, sonra sakin yâ: فُعَيْلٌ. نَصْرِيٌّ «yardımla ilgili»dir — masdara "
                     "şeddeli nisbet yâsı: -ِيٌّ."},
        explanation={
            "en": "Rows nineteen and twenty are two nouns made from the maṣdar نَصْرٌ. The diminutive (taṣghīr) of a three-letter noun is "
                  "فُعَيْلٌ: a ḍamma on the first letter, a fatḥa on the second, and a silent yāʾ after it — نُصَيْرٌ, «a little help»; it can "
                  "also make something small, near or dear. A real name of this shape stands in the stories: مُوسَى بْنُ نُصَيْرٍ. Do not mix it "
                  "with نَصِيرٌ (فَعِيلٌ, «a helper»), which has a fatḥa and a long ī. The relational adjective (nisba) adds a doubled yāʾ with a "
                  "kasra before it: نَصْرِيٌّ, «of help, having to do with help» — as هَاشِمِيٌّ is «of Hāshim». The Amthila recites both on every "
                  "verb; the received sheet adds that the augmented bābs have no diminutive. The tables show the same two forms in the six bābs.",
            "tr": "On dokuzuncu ve yirminci satırlar masdar نَصْرٌ'dan yapılan iki isimdir. Üç harfli ismin tasğîri فُعَيْلٌ'dir: birinci harf "
                  "mazmum, ikinci harf meftûh, ardından sakin bir yâ — نُصَيْرٌ, «küçük bir yardım»; bir şeyi küçük, yakın ya da sevimli de "
                  "kılabilir. Bu kalıpta gerçek bir isim hikâyelerde durur: مُوسَى بْنُ نُصَيْرٍ. Onu نَصِيرٌ ile (فَعِيلٌ, «yardımcı») karıştırma; o "
                  "fethalı ve uzun î'lidir. İsm-i mensûb şeddeli bir yâ ekler, önündeki harf meksûr olur: نَصْرِيٌّ, «yardıma ait» — tıpkı "
                  "هَاشِمِيٌّ'nin «Hâşim'e ait» oluşu gibi. Emsile ikisini her fiilde okur; gelen cetvel ziyade bâblarda tasğîr gelmediğini ekler. "
                  "Cetveller aynı iki sîgayı altı bâbda gösterir."},
        tables=[tab("row", H("نُصَيْرٌ وَنَصْرِيٌّ", "Diminutive and relation", "Tasğîr ve nisbet"), {"k": "row", "root": R, "bab": 1, "slots": ["tasghir", "nisba"]},
                    labels=[{"ar": f[2], "tr": f[3], "en": f[4], "m": {"en": f[5], "tr": f[6]}} for f in FORMS if f[0] in ("tasghir", "nisba")]),
                tab("tasghir", H("التَّصْغِيرُ فِي الْأَبْوَابِ السِّتَّةِ", "The diminutive in the six bābs", "Altı bâbda tasğîr"), {"k": "em", "slot": "tasghir", "models": [0, 1, 2, 3, 4, 5]}, bab=True),
                tab("nisba", H("النِّسْبَةُ فِي الْأَبْوَابِ السِّتَّةِ", "The relational adjective in the six bābs", "Altı bâbda ism-i mensûb"), {"k": "em", "slot": "nisba", "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=1,
        examples=[["tariq-ibn-ziyad", 4, "s4"], ["izhar-al-asrar", 16, "s9"]],
        mistakes=[dict(w={"src": {"k": "corpus", "refs": [["marah-al-arwah", 37, "s1", 5]]}, "i": 0}, r={"src": {"k": "corpus", "refs": [["tariq-ibn-ziyad", 4, "s4", 7]]}, "i": 0},
                       why={"en": "The diminutive is نُصَيْرٍ — ḍamma, fatḥa, silent yāʾ (فُعَيْل). نَصِيرٍ (فَعِيل, as in Marāḥ «نَحْوُ نَصِيرٍ») is another "
                                  "word: «a helper».",
                            "tr": "Tasğîr نُصَيْرٍ'dir — damme, fetha, sakin yâ (فُعَيْل). نَصِيرٍ (فَعِيل, Merâh'taki «نَحْوُ نَصِيرٍ» gibi) başka bir "
                                  "kelimedir: «yardımcı»."})],
        related=["ism-mansub", "emsile-00-amthila", "emsile-03-masdar"],
        sources=["مراح الأرواح", f"{SHEET}، س 23 — … İSMİ TESGIR … GELMEZ"],
    )

    # 10 — ism tafḍīl
    N["emsile-10-tafdil"] = dict(
        title=H("اسْمُ التَّفْضِيلِ — أَنْصَرُ", "The elative: أَنْصَرُ", "İsm-i tafdîl: أَنْصَرُ"),
        plain={"en": "أَنْصَرُ is «more helpful, the most helpful» — أَفْعَلُ for a man, فُعْلَى (نُصْرَى) for a woman. It takes no tanwīn: "
                     "it is a diptote.",
               "tr": "أَنْصَرُ «daha çok / en çok yardım eden»dir — erkek için أَفْعَلُ, kadın için فُعْلَى (نُصْرَى). Tenvin almaz: gayr-i munsarıftır."},
        explanation={
            "en": "Row twenty-two is the elative (ism-i tafḍīl): one who has more of the quality than another. From the bare verb it is "
                  "أَفْعَلُ — a hamza with a fatḥa in front, the first radical silent: أَنْصَرُ. Because it has the measure of a verb and is a "
                  "description, it is a diptote (ghayr munṣarif): no tanwīn, and a fatḥa in jarr. Used with مِنْ it does not change for number "
                  "or gender (هُوَ أَنْصَرُ مِنْهُ، هِيَ أَنْصَرُ مِنْهُ); used with the article or annexed it agrees, and then it has a Muṭṭarida: "
                  "أَنْصَرُ، أَنْصَرَانِ، أَنْصَرُونَ for men; نُصْرَى، نُصْرَيَانِ، نُصْرَيَاتٌ for women (فُعْلَى). The books also recite broken "
                  "plurals, which the engine does not build. The received sheet shows that the augmented bābs make the elative with أَشَدُّ and "
                  "the maṣdar (هُوَ أَشَدُّ مِنْهُ إِكْرَامًا) — the Conjugation panel's Muhtelife tab draws those rows for every augmented verb.",
            "tr": "Yirmi ikinci satır ism-i tafdîldir: bir vasfa başkasından daha çok sahip olan. Mücerredden أَفْعَلُ'dür — başta meftûh hemze, "
                  "birinci harf sakin: أَنْصَرُ. Fiil vezninde ve vasıf olduğu için gayr-i munsarıftır: tenvin almaz, cer hâlinde fetha alır. مِنْ "
                  "ile kullanılınca sayı ve cinse göre değişmez (هُوَ أَنْصَرُ مِنْهُ، هِيَ أَنْصَرُ مِنْهُ); elif-lâmlı ya da muzâf olunca mutâbakat "
                  "eder ve o zaman Muttaride'si olur: erkekler için أَنْصَرُ، أَنْصَرَانِ، أَنْصَرُونَ; kadınlar için نُصْرَى، نُصْرَيَانِ، نُصْرَيَاتٌ "
                  "(فُعْلَى). Kitaplar cem'-i mükesserleri de okur; motor onları kurmaz. Gelen cetvel, ziyade bâbların tafdîli أَشَدُّ ve masdarla "
                  "yaptığını gösterir (هُوَ أَشَدُّ مِنْهُ إِكْرَامًا) — Çekim panelinin Muhtelife sekmesi bu satırları her ziyade fiil için çizer."},
        tables=[tab("num", H("اسْمُ التَّفْضِيلِ — الْمُطَّرِدَةُ", "The elative by number and gender", "İsm-i tafdîl — sayı ve cinsiyle"),
                    {"k": "block", "root": R, "bab": 1, "list": "tafdil", "take": [0, 1, 2, 4, 5, 6]}, labels=NUM6),
                tab("babs", H("اسْمُ التَّفْضِيلِ فِي الْأَبْوَابِ السِّتَّةِ", "The elative in the six bābs", "Altı bâbda ism-i tafdîl"), {"k": "em", "slot": "tafdil", "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=0,
        examples=[["al-kafiya", 19, "s1"], ["izhar-al-asrar", 13, "s1"]],
        mistakes=[dict(w={"src": {"k": "block", "root": R, "bab": 1, "list": "tafdil"}, "i": 4}, r={"src": {"k": "block", "root": R, "bab": 1, "list": "tafdil"}, "i": 0},
                       why={"en": "For a man the elative is أَنْصَرُ (أَفْعَلُ); نُصْرَى (فُعْلَى) is its feminine.",
                            "tr": "Erkek için tafdîl أَنْصَرُ'dür (أَفْعَلُ); نُصْرَى (فُعْلَى) onun müennesidir."})],
        related=["ism-tafdil", "ism-al-tafdil-fil-kafiya", "amal-ism-al-tafdil-wal-masdar", "emsile-11-taajjub"],
        sources=["مراح الأرواح", "الكافية (ابن الحاجب)", "المقصود في الصرف"],
    )

    # 11 — the two verbs of wonder (and the pronouns of naṣb and jarr through them)
    N["emsile-11-taajjub"] = dict(
        title=H("مَا أَنْصَرَهُ وَأَنْصِرْ بِهِ", "The two verbs of wonder: مَا أَنْصَرَهُ and أَنْصِرْ بِهِ", "İki taaccüb fiili: مَا أَنْصَرَهُ ve أَنْصِرْ بِهِ"),
        plain={"en": "«How much he helps!» is said two ways: مَا أَنْصَرَهُ and أَنْصِرْ بِهِ. The verb does not change from person to person — "
                     "the PRONOUN does: هُ … نَا after أَنْصَرَ (naṣb), بِهِ … بِنَا after the bāʾ (jarr).",
               "tr": "«Ne çok yardım ediyor!» iki türlü söylenir: مَا أَنْصَرَهُ ve أَنْصِرْ بِهِ. Fiil sîgadan sîgaya değişmez — ZAMİR değişir: "
                     "أَنْصَرَ'den sonra هُ … نَا (nasb), bâdan sonra بِهِ … بِنَا (cer)."},
        explanation={
            "en": "The last two rows of the Amthila express wonder. In مَا أَنْصَرَهُ, مَا means «what a thing» and أَنْصَرَ is a māḍī verb on "
                  "أَفْعَلَ: «what has made him so helpful!». In أَنْصِرْ بِهِ the verb has the shape of a command (أَفْعِلْ) but is not one; the "
                  "bāʾ is extra, and what follows it is the one wondered at. Neither verb changes: their Muṭṭarida is made by changing the "
                  "pronoun at the end — and that is exactly where the madrasa teaches two kinds of pronoun. After أَنْصَرَ the pronoun is the "
                  "OBJECT, so it is an attached pronoun of naṣb (manṣūb muttaṣil): مَا أَنْصَرَهُ، مَا أَنْصَرَهُمَا، مَا أَنْصَرَهُمْ … مَا أَنْصَرَنِي، "
                  "مَا أَنْصَرَنَا. Before the speaker's yāʾ a verb takes the nūn of protection (nūn al-wiqāya): أَنْصَرَنِي, never أَنْصَرِي. After "
                  "the bāʾ the pronoun is governed by a preposition, so it is an attached pronoun of jarr (majrūr muttaṣil): بِهِ، بِهِمَا، بِهِمْ … "
                  "بِي، بِنَا — and after the kasra of the bāʾ the hāʾ takes a kasra too (بِهِ، بِهِمْ). The letters of the two lists are the same "
                  "(هُ، هُمَا، هُمْ، هَا … كَ … نَا); what tells them apart is what they hang on: a verb or إِنَّ and its sisters → naṣb; a "
                  "preposition or a noun they are annexed to → jarr. A pronoun is mabnī: it never changes its ending, so it has only a PLACE "
                  "(fī maḥalli naṣbin, fī maḥalli jarrin). Tap a «↗» to open a story word whose iʿrāb gives that pronoun that place, with its "
                  "«Neden?» chain.",
            "tr": "Emsile'nin son iki satırı taaccüb bildirir. مَا أَنْصَرَهُ'da مَا «ne şey» demektir, أَنْصَرَ أَفْعَلَ vezninde mâzî bir "
                  "fiildir: «onu bu kadar yardımsever kılan nedir!». أَنْصِرْ بِهِ'de fiil emir kalıbındadır (أَفْعِلْ) ama emir değildir; bâ "
                  "zâiddir, ondan sonraki taaccüb olunandır. İki fiil de değişmez: Muttaride'leri sondaki zamir değiştirilerek yapılır — medrese iki "
                  "çeşit zamiri tam burada öğretir. أَنْصَرَ'den sonraki zamir MEF'ÛLDÜR, yani muttasıl mansûb zamirdir: مَا أَنْصَرَهُ، مَا أَنْصَرَهُمَا، "
                  "مَا أَنْصَرَهُمْ … مَا أَنْصَرَنِي، مَا أَنْصَرَنَا. Fiil, mütekellim yâsından önce nûn-ı vikâye alır: أَنْصَرَنِي, asla أَنْصَرِي "
                  "değil. Bâdan sonraki zamiri cer harfi amel eder, yani muttasıl mecrûr zamirdir: بِهِ، بِهِمَا، بِهِمْ … بِي، بِنَا — bânın "
                  "kesresinden sonra hâ da kesre alır (بِهِ، بِهِمْ). İki listenin harfleri aynıdır (هُ، هُمَا، هُمْ، هَا … كَ … نَا); onları ayıran neye "
                  "bağlandıklarıdır: fiil ya da إِنَّ ve kardeşleri → nasb; cer harfi ya da muzâf olduğu isim → cer. Zamir mebnîdir: sonu hiç "
                  "değişmez, bu yüzden yalnız MAHALLİ vardır (mahallen mansûb, mahallen mecrûr). Bir «↗»'ya dokun: i'rabı o zamire o mahalli veren "
                  "bir hikâye kelimesi «Neden?» zinciriyle açılır."},
        tables=[tab("nasb", H("مَا أَنْصَرَهُ — الضَّمِيرُ الْمَنْصُوبُ الْمُتَّصِلُ", "مَا أَنْصَرَهُ — the attached pronoun of naṣb", "مَا أَنْصَرَهُ — muttasıl mansûb zamir"),
                    {"k": "att", "host": "أَنْصَرَ", "kind": "verb", "pre": "مَا "}, rows=S14, keys=keys("nasbMuttasil", S14)),
                tab("jarr", H("أَنْصِرْ بِهِ — الضَّمِيرُ الْمَجْرُورُ الْمُتَّصِلُ", "أَنْصِرْ بِهِ — the attached pronoun of jarr", "أَنْصِرْ بِهِ — muttasıl mecrûr zamir"),
                    {"k": "att", "host": "بِ", "kind": "harf", "pre": "أَنْصِرْ "}, rows=S14, keys=keys("jarrMuttasil", S14)),
                tab("babs", H("مَا أَفْعَلَهُ فِي الْأَبْوَابِ السِّتَّةِ", "The first verb of wonder in the six bābs", "Altı bâbda birinci taaccüb"), {"k": "em", "slot": "taajjub1", "pre": "مَا ", "models": [0, 1, 2, 3, 4, 5]}, bab=True)],
        quiz=0,
        examples=[["al-kafiya", 27, "s2"], ["talkhis-al-miftah", 58, "s3"], ["izhar-al-asrar", 46, "s3"]],
        mistakes=[dict(w={"src": {"k": "attSkip", "host": "أَنْصَرَ", "kind": "verb", "skip": ["wiqaya"], "pre": "مَا "}, "i": 12},
                       r={"src": {"k": "att", "host": "أَنْصَرَ", "kind": "verb", "pre": "مَا "}, "i": 12},
                       why={"en": "Before the speaker's yāʾ a verb takes the nūn of protection: مَا أَنْصَرَنِي.",
                            "tr": "Mütekellim yâsından önce fiil nûn-ı vikâye alır: مَا أَنْصَرَنِي."}),
                  dict(w={"src": {"k": "attSkip", "host": "بِ", "kind": "harf", "skip": ["harmony"], "pre": "أَنْصِرْ "}, "i": 2},
                       r={"src": {"k": "att", "host": "بِ", "kind": "harf", "pre": "أَنْصِرْ "}, "i": 2},
                       why={"en": "After the kasra of the bāʾ the hāʾ takes a kasra: بِهِمْ, not بِهُمْ.", "tr": "Bânın kesresinden sonra hâ kesre alır: بِهِمْ, بِهُمْ değil."})],
        related=["fil-al-taajjub-fil-kafiya", "emsile-14-damir-nasb-muttasil", "emsile-16-damir-jarr-muttasil", "emsile-17-damir-map", "emsile-10-tafdil"],
        sources=["مراح الأرواح", "الكافية (ابن الحاجب)", "إظهار الأسرار (البركوي)"],
    )

    # ── the pronouns ──
    mabni_en = ("A pronoun is mabnī: its own ending never changes, so its iʿrāb is only a PLACE — fī maḥalli rafʿin, naṣbin or jarrin "
                "(mahallen merfû, mansûb, mecrûr). ")
    mabni_tr = ("Zamir mebnîdir: kendi sonu hiç değişmez; bu yüzden i'rabı yalnız bir MAHALDİR — mahallen merfû, mansûb ya da mecrûr. ")
    neden_en = "Tap «↗» on a row to open a story word whose authored iʿrāb gives that pronoun that place, with its «Neden?» chain."
    neden_tr = "Bir satırdaki «↗»'ya dokun: yazar i'rabı o zamire o mahalli veren bir hikâye kelimesi «Neden?» zinciriyle açılır."

    N["emsile-12-damir-raf-muttasil"] = dict(
        title=H("الضَّمِيرُ الْمَرْفُوعُ الْمُتَّصِلُ — وَالْمُسْتَتِرُ", "The attached pronoun of rafʿ — and the hidden one", "Muttasıl merfû zamir — ve müstetir zamir"),
        plain={"en": "The doer of نَصَرْتُ is the tāʾ, of نَصَرُوا the wāw, of يَنْصُرْنَ the nūn: attached pronouns in rafʿ. Where no letter "
                     "stands — نَصَرَ، يَنْصُرُ، اُنْصُرْ — the doer is a hidden pronoun (هُوَ، أَنْتَ …).",
               "tr": "نَصَرْتُ'un fâili tâ, نَصَرُوا'nun vâv, يَنْصُرْنَ'in nûndur: muttasıl merfû zamirler. Hiç harf olmayan yerde — نَصَرَ، يَنْصُرُ، "
                     "اُنْصُرْ — fâil müstetir bir zamirdir (هُوَ، أَنْتَ …)."},
        explanation={
            "en": "The first kind of pronoun is learnt inside the verb tables. In the māḍī the attached pronouns of rafʿ are ا (نَصَرَا), و "
                  "(نَصَرُوا), نَ (نَصَرْنَ), تَ تُمَا تُمْ تِ تُنَّ تُ (نَصَرْتَ … نَصَرْتُ) and نَا (نَصَرْنَا) — twelve in use (Marāḥ: «اثْنَا عَشَرَ "
                  "لِلْمَرْفُوعِ الْمُتَّصِلِ نَحْوُ ضَرَبَ إِلَى ضَرَبْنَا»). In the muḍāriʿ and the amr they are the alif of two, the wāw of the "
                  "group, the yāʾ of the woman addressed and the nūn of women (يَنْصُرَانِ، يَنْصُرُونَ، تَنْصُرِينَ، يَنْصُرْنَ، اُنْصُرَا …). Each is "
                  "the doer, fī maḥalli rafʿin fāʿil. Where the table shows no pronoun letter the doer is HIDDEN (mustatir). Marāḥ counts five "
                  "places: the absent man and the absent woman (نَصَرَ، نَصَرَتْ، يَنْصُرُ، تَنْصُرُ), the man addressed outside the māḍī (تَنْصُرُ، "
                  "اُنْصُرْ، لَا تَنْصُرْ), and the speaker of the muḍāriʿ (أَنْصُرُ، نَنْصُرُ). With «he» and «she» it hides only MAY-hide "
                  "(jāʾizan): a named doer can take its place (نَصَرَ زَيْدٌ). With أَنْتَ، أَنَا، نَحْنُ in the muḍāriʿ and أَنْتَ in the amr it "
                  "MUST hide (wājiban): «hiding is obligatory in افْعَلْ، تَفْعَلُ، أَفْعَلُ، نَفْعَلُ because the form shows it» (Marāḥ ch. 17 s24). "
                  "Not pronouns: the tāʾ of نَصَرَتْ (a sign of the feminine) and the prefixes يَـ تَـ أَ نَـ (signs of the muḍāriʿ). On the yāʾ of "
                  "تَنْصُرِينَ the books record a difference: a pronoun for Sībawayh and most, a sign of address with a hidden doer for "
                  "al-Akhfash (Marāḥ ch. 17 s4–s5); the table follows the majority. " + mabni_en + neden_en,
            "tr": "İlk zamir çeşidi fiil cetvellerinin içinde öğrenilir. Mâzîde muttasıl merfû zamirler ا (نَصَرَا), و (نَصَرُوا), نَ (نَصَرْنَ), "
                  "تَ تُمَا تُمْ تِ تُنَّ تُ (نَصَرْتَ … نَصَرْتُ) ve نَا'dır (نَصَرْنَا) — kullanımda on iki (Merâh: «اثْنَا عَشَرَ لِلْمَرْفُوعِ "
                  "الْمُتَّصِلِ نَحْوُ ضَرَبَ إِلَى ضَرَبْنَا»). Muzâri ve emirde tesniye elifi, cemaat vâvı, muhâtaba yâsı ve nûn-ı nisvedir "
                  "(يَنْصُرَانِ، يَنْصُرُونَ، تَنْصُرِينَ، يَنْصُرْنَ، اُنْصُرَا …). Her biri fâildir, mahallen merfû. Cetvelin zamir harfi göstermediği "
                  "yerde fâil MÜSTETİRDİR. Merâh beş yer sayar: gâib ve gâibe (نَصَرَ، نَصَرَتْ، يَنْصُرُ، تَنْصُرُ), mâzî dışında muhâtab (تَنْصُرُ، "
                  "اُنْصُرْ، لَا تَنْصُرْ) ve muzârinin mütekellimi (أَنْصُرُ، نَنْصُرُ). «O» ile cevâzen müstetirdir: yerine açık bir fâil gelebilir "
                  "(نَصَرَ زَيْدٌ). Muzâride أَنْتَ، أَنَا، نَحْنُ ile ve emirde أَنْتَ ile VÜCÛBEN müstetirdir: «افْعَلْ، تَفْعَلُ، أَفْعَلُ، نَفْعَلُ'da "
                  "istitâr vâciptir, çünkü sîga onu gösterir» (Merâh 17. bölüm s24). Zamir olmayanlar: نَصَرَتْ'in tâsı (müennes alâmeti) ve يَـ تَـ "
                  "أَ نَـ harfleri (muzâraat alâmetleri). تَنْصُرِينَ'in yâsında kitaplar bir ihtilaf kaydeder: Sîbeveyh ve çoğunluğa göre zamir, "
                  "Ahfeş'e göre muhâtaba alâmeti, fâil müstetir (Merâh 17. bölüm s4–s5); cetvel çoğunluğa uyar. " + mabni_tr + neden_tr},
        tables=[tab("madi", H("فِي الْمَاضِي — نَصَرَ", "In the past", "Mâzîde"), {"k": "raf", "stem": "نَصَر"}, rows=S14, endsOf=R, pronOf="mazi", keys=raf_keys(S14, {0, 3})),
                tab("mud", H("فِي الْمُضَارِعِ — يَنْصُرُ", "In the present", "Muzâride"), {"k": "mud", "root": R, "bab": 1}, rows=S14, endsOf=R, pronOf="mud",
                    keys=raf_keys(S14, {0, 3, 6, 12, 13})),
                tab("amr", H("فِي الْأَمْرِ — اُنْصُرْ", "In the command", "Emirde"), {"k": "amr", "root": R, "bab": 1}, rows=AMR6, endsOf=R, pronOf="amr", keys=raf_keys(AMR6, {6}))],
        quiz=0,
        examples=[["marah-al-arwah", 17, "s1"], ["marah-al-arwah", 17, "s24"], ["al-kafiya", 3, "s12"]],
        mistakes=[dict(w={"src": {"k": "raf", "stem": "نَصَر"}, "i": 3}, r={"src": {"k": "raf", "stem": "نَصَر"}, "i": 9},
                       why={"en": "«You (f.) helped» is نَصَرْتِ: a silent rāʾ, then the pronoun تِ. In نَصَرَتْ the tāʾ is only the feminine sign and the doer is hidden.",
                            "tr": "«Yardım ettin (kadın)» نَصَرْتِ'dir: râ sakin, sonra zamir تِ. نَصَرَتْ'te tâ yalnız müennes alâmetidir, fâil müstetirdir."})],
        related=["fail", "al-fail-al-mudmar-al-mustatir-wujuban", "al-marifa-al-mudmarat-wal-alam", "emsile-01-madi", "emsile-02-mudari", "emsile-17-damir-map"],
        sources=["مراح الأرواح", "الكافية (ابن الحاجب)", "إظهار الأسرار (البركوي)"],
    )

    N["emsile-13-damir-raf-munfasil"] = dict(
        title=H("الضَّمِيرُ الْمَرْفُوعُ الْمُنْفَصِلُ — هُوَ … نَحْنُ", "The detached pronoun of rafʿ: هُوَ … نَحْنُ", "Munfasıl merfû zamir: هُوَ … نَحْنُ"),
        plain={"en": "هُوَ، هُمَا، هُمْ، هِيَ، هُمَا، هُنَّ، أَنْتَ … أَنَا، نَحْنُ stand as words of their own. They are in rafʿ — most often as "
                     "the subject (mubtadaʾ): هُوَ نَاصِرٌ «he is a helper».",
               "tr": "هُوَ، هُمَا، هُمْ، هِيَ، هُمَا، هُنَّ، أَنْتَ … أَنَا، نَحْنُ kendi başına duran kelimelerdir. Merfûdurlar — çoğunlukla mübtedâ "
                     "olarak: هُوَ نَاصِرٌ «o, yardım edendir»."},
        explanation={
            "en": "The detached pronouns of rafʿ are the same twelve persons as the attached ones, but each is a word that can stand alone "
                  "(Marāḥ: «اثْنَا عَشَرَ لِلْمَرْفُوعِ الْمُنْفَصِلِ نَحْوُ هُوَ ضَرَبَ إِلَى نَحْنُ ضَرَبْنَا»). They stand where an attached pronoun "
                  "cannot: at the head of a sentence as the mubtadaʾ (هُوَ نَاصِرٌ), after إِلَّا, to stress the doer (نَصَرْتُ أَنَا — al-Kāfiya's "
                  "example), and they name the hidden pronoun when we spell it out (the doer of نَصَرَ is هُوَ). The rule of al-Kāfiya: the detached "
                  "one is not used where the attached one is possible, because the pronouns were made to be short. The dual هُمَا is shared by "
                  "the man and the woman, and أَنْتُمَا by the two addressed — so twelve words serve fourteen persons. " + mabni_en + neden_en,
            "tr": "Munfasıl merfû zamirler muttasıllarla aynı on iki sîgadır; ama her biri tek başına durabilen bir kelimedir (Merâh: «اثْنَا "
                  "عَشَرَ لِلْمَرْفُوعِ الْمُنْفَصِلِ نَحْوُ هُوَ ضَرَبَ إِلَى نَحْنُ ضَرَبْنَا»). Muttasılın duramayacağı yerde dururlar: cümlenin "
                  "başında mübtedâ olarak (هُوَ نَاصِرٌ), إِلَّا'dan sonra, fâili vurgulamak için (نَصَرْتُ أَنَا — Kâfiye'nin misali); müstetir zamiri "
                  "açıkça söylerken de onu adlandırırlar (نَصَرَ'in fâili هُوَ'dir). Kâfiye'nin kaidesi: muttasıl mümkünken munfasıl kullanılmaz, "
                  "çünkü zamirler kısalık için konmuştur. Tesniye هُمَا eril ve dişil için, أَنْتُمَا iki muhâtab için ortaktır — on iki kelime on "
                  "dört sîgaya yeter. " + mabni_tr + neden_tr},
        tables=[tab("munf", H("الْمَرْفُوعُ الْمُنْفَصِلُ", "Detached, rafʿ", "Munfasıl merfû"), {"k": "munf"}, rows=S14, keys=keys("rafMunfasil", S14))],
        quiz=0,
        examples=[["izhar-al-asrar", 46, "s2"], ["al-kafiya", 3, "s10"], ["al-kafiya", 3, "s13"]],
        mistakes=[dict(w={"src": {"k": "munf"}, "i": 8}, r={"src": {"k": "munf"}, "i": 7},
                       why={"en": "For two people addressed it is أَنْتُمَا; أَنْتُمْ is for three or more men.", "tr": "İki muhâtab için أَنْتُمَا'dır; أَنْتُمْ üç ve daha çok erkek içindir."})],
        related=["al-marifa-al-mudmarat-wal-alam", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan", "damir-fasl", "emsile-12-damir-raf-muttasil", "emsile-17-damir-map"],
        sources=["مراح الأرواح", "الكافية (ابن الحاجب)", "إظهار الأسرار (البركوي)"],
    )

    N["emsile-14-damir-nasb-muttasil"] = dict(
        title=H("الضَّمِيرُ الْمَنْصُوبُ الْمُتَّصِلُ — هُ … نَا", "The attached pronoun of naṣb: هُ … نَا", "Muttasıl mansûb zamir: هُ … نَا"),
        plain={"en": "In نَصَرَهُ «he helped him» the هُ is the object: an attached pronoun of naṣb. Twelve of them, هُ … كَ … نِي، نَا — and "
                     "before the speaker's yāʾ a verb takes the nūn of protection: نَصَرَنِي.",
               "tr": "نَصَرَهُ «ona yardım etti»de هُ mef'ûldür: muttasıl mansûb zamir. On iki tanedir, هُ … كَ … نِي، نَا — ve mütekellim yâsından "
                     "önce fiil nûn-ı vikâye alır: نَصَرَنِي."},
        explanation={
            "en": "The attached pronouns of naṣb hang on a verb (or on إِنَّ and its sisters) as its object: هُ هُمَا هُمْ هَا هُمَا هُنَّ كَ كُمَا "
                  "كُمْ كِ كُمَا كُنَّ نِي نَا (Marāḥ: «اثْنَا عَشَرَ لِلْمَنْصُوبِ الْمُتَّصِلِ نَحْوُ ضَرَبَهُ إِلَى ضَرَبَنَا»). The madrasa recites them "
                  "through مَا أَنْصَرَهُ … مَا أَنْصَرَنَا (the verb of wonder) and through نَصَرَهُ … نَصَرَنَا. The first person singular is a yāʾ, "
                  "and a verb puts a nūn before it so that the verb's own last letter is protected from the kasra the yāʾ would demand: نَصَرَنِي — "
                  "the nūn al-wiqāya, required with the māḍī (al-Kāfiya). The doer and the object cannot be two attached pronouns of the same person "
                  "(no «نَصَرْتُنِي») except with the verbs of the heart (عَلِمْتُنِي فَاضِلًا — Marāḥ ch. 16 s2–s3). Iẓhār calls these and the "
                  "majrūr ones one shared class, because the letters are the same; what they hang on decides. " + mabni_en + neden_en,
            "tr": "Muttasıl mansûb zamirler bir fiile (ya da إِنَّ ve kardeşlerine) mef'ûl olarak bağlanır: هُ هُمَا هُمْ هَا هُمَا هُنَّ كَ كُمَا "
                  "كُمْ كِ كُمَا كُنَّ نِي نَا (Merâh: «اثْنَا عَشَرَ لِلْمَنْصُوبِ الْمُتَّصِلِ نَحْوُ ضَرَبَهُ إِلَى ضَرَبَنَا»). Medrese onları مَا أَنْصَرَهُ … "
                  "مَا أَنْصَرَنَا (taaccüb fiili) ile ve نَصَرَهُ … نَصَرَنَا ile okur. Birinci şahıs müfredi bir yâdır; fiil, yânın isteyeceği kesreden "
                  "kendi son harfini korumak için ondan önce bir nûn koyar: نَصَرَنِي — nûn-ı vikâye, mâzîde lâzımdır (Kâfiye). Fâil ile mef'ûl aynı "
                  "kişinin iki muttasıl zamiri olamaz («نَصَرْتُنِي» olmaz), ef'âl-i kulûb müstesna (عَلِمْتُنِي فَاضِلًا — Merâh 16. bölüm s2–s3). "
                  "İzhâr bunları ve mecrûrları tek bir müşterek kısım sayar, çünkü harfler aynıdır; neye bağlandıkları karar verir. " + mabni_tr + neden_tr},
        tables=[tab("taajjub", H("مَا أَنْصَرَهُ … مَا أَنْصَرَنَا", "Through the verb of wonder", "Taaccüb fiiliyle"), {"k": "att", "host": "أَنْصَرَ", "kind": "verb", "pre": "مَا "},
                    rows=S14, keys=keys("nasbMuttasil", S14)),
                tab("madi", H("نَصَرَهُ … نَصَرَنَا", "Through the past", "Mâzîyle"), {"k": "att", "host": "نَصَرَ", "kind": "verb"}, rows=S14)],
        quiz=1,
        examples=[["qisas-al-nabiyyin-1", 3, "s24"], ["marah-al-arwah", 16, "s1"], ["marah-al-arwah", 16, "s2"], ["izhar-al-asrar", 46, "s3"]],
        mistakes=[dict(w={"src": {"k": "attSkip", "host": "نَصَرَ", "kind": "verb", "skip": ["wiqaya"]}, "i": 12}, r={"src": {"k": "att", "host": "نَصَرَ", "kind": "verb"}, "i": 12},
                       why={"en": "A verb takes the nūn of protection before the speaker's yāʾ: نَصَرَنِي «he helped me».",
                            "tr": "Fiil mütekellim yâsından önce nûn-ı vikâye alır: نَصَرَنِي «bana yardım etti»."})],
        related=["al-marifa-al-mudmarat-wal-alam", "emsile-11-taajjub", "emsile-16-damir-jarr-muttasil", "emsile-15-damir-nasb-munfasil", "emsile-17-damir-map"],
        sources=["مراح الأرواح", "الكافية (ابن الحاجب)", "إظهار الأسرار (البركوي)"],
    )

    N["emsile-15-damir-nasb-munfasil"] = dict(
        title=H("الضَّمِيرُ الْمَنْصُوبُ الْمُنْفَصِلُ — إِيَّاهُ … إِيَّانَا", "The detached pronoun of naṣb: إِيَّاهُ … إِيَّانَا", "Munfasıl mansûb zamir: إِيَّاهُ … إِيَّانَا"),
        plain={"en": "إِيَّاهُ … إِيَّاكَ … إِيَّايَ، إِيَّانَا is the object standing as a word of its own — when it comes first or cannot attach: "
                     "إِيَّاكَ نَصَرَ زَيْدٌ «you it is whom Zayd helped».",
               "tr": "إِيَّاهُ … إِيَّاكَ … إِيَّايَ، إِيَّانَا kendi başına duran mef'ûldür — öne geçtiğinde ya da bitişemediğinde: إِيَّاكَ نَصَرَ زَيْدٌ "
                     "«Zeyd'in yardım ettiği sensin»."},
        explanation={
            "en": "The detached pronoun of naṣb is إِيَّا with the attached letters after it: إِيَّاهُ، إِيَّاهُمَا، إِيَّاهُمْ، إِيَّاهَا، إِيَّاهُمَا، "
                  "إِيَّاهُنَّ، إِيَّاكَ، إِيَّاكُمَا، إِيَّاكُمْ، إِيَّاكِ، إِيَّاكُمَا، إِيَّاكُنَّ، إِيَّايَ، إِيَّانَا (Marāḥ: «اثْنَا عَشَرَ لِلْمَنْصُوبِ "
                  "الْمُنْفَصِلِ نَحْوُ إِيَّاهُ ضَرَبَ إِلَى إِيَّانَا ضَرَبْنَا»). It is used when the object comes before its verb (إِيَّاكَ نَصَرَ زَيْدٌ — "
                  "al-Kāfiya), and when two object pronouns meet and the second cannot attach (أَعْطَيْتُهُ إِيَّاهُ). Otherwise the attached form "
                  "is the rule: نَصَرَكَ, not نَصَرَ إِيَّاكَ. There is no detached pronoun of jarr, Marāḥ explains, because a majrūr never stands "
                  "before the word that governs it. " + mabni_en + neden_en,
            "tr": "Munfasıl mansûb zamir, ardına muttasıl harfler gelen إِيَّا'dır: إِيَّاهُ، إِيَّاهُمَا، إِيَّاهُمْ، إِيَّاهَا، إِيَّاهُمَا، إِيَّاهُنَّ، "
                  "إِيَّاكَ، إِيَّاكُمَا، إِيَّاكُمْ، إِيَّاكِ، إِيَّاكُمَا، إِيَّاكُنَّ، إِيَّايَ، إِيَّانَا (Merâh: «اثْنَا عَشَرَ لِلْمَنْصُوبِ الْمُنْفَصِلِ "
                  "نَحْوُ إِيَّاهُ ضَرَبَ إِلَى إِيَّانَا ضَرَبْنَا»). Mef'ûl fiilinden önce gelince kullanılır (إِيَّاكَ نَصَرَ زَيْدٌ — Kâfiye) ve iki mef'ûl "
                  "zamiri buluşup ikincisi bitişemeyince (أَعْطَيْتُهُ إِيَّاهُ). Aksi hâlde kaide muttasıldır: نَصَرَكَ, نَصَرَ إِيَّاكَ değil. Merâh'ın "
                  "açıkladığı gibi munfasıl mecrûr zamir yoktur, çünkü mecrûr kendisine amel edenden önce gelmez. " + mabni_tr + neden_tr},
        tables=[tab("iyya", H("الْمَنْصُوبُ الْمُنْفَصِلُ", "Detached, naṣb", "Munfasıl mansûb"), {"k": "att", "host": "إِيَّا", "kind": "iyya"}, rows=S14, keys=keys("nasbMunfasil", S14))],
        quiz=0,
        examples=[["izhar-al-asrar", 46, "s4"], ["marah-al-arwah", 16, "s6"], ["al-kafiya", 3, "s10"]],
        mistakes=[dict(w={"src": {"k": "block", "root": R, "bab": 1, "list": "maziM"}, "i": 0, "plus": {"src": {"k": "att", "host": "إِيَّا", "kind": "iyya"}, "i": 6}},
                       r={"src": {"k": "att", "host": "نَصَرَ", "kind": "verb"}, "i": 6},
                       why={"en": "Where the attached pronoun is possible the detached one is not used: «he helped you» is نَصَرَكَ, not نَصَرَ followed "
                                  "by إِيَّاكَ (al-Kāfiya: «لَا يَجُوزُ الْمُنْفَصِلُ مَعَ إِمْكَانِ الْمُتَّصِلِ»).",
                            "tr": "Muttasıl mümkünken munfasıl kullanılmaz: «sana yardım etti» نَصَرَكَ'dir, نَصَرَ ardından إِيَّاكَ değil (Kâfiye: «لَا "
                                  "يَجُوزُ الْمُنْفَصِلُ مَعَ إِمْكَانِ الْمُتَّصِلِ»)."})],
        related=["al-marifa-al-mudmarat-wal-alam", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan", "emsile-14-damir-nasb-muttasil", "emsile-17-damir-map"],
        sources=["مراح الأرواح", "الكافية (ابن الحاجب)", "إظهار الأسرار (البركوي)"],
    )

    N["emsile-16-damir-jarr-muttasil"] = dict(
        title=H("الضَّمِيرُ الْمَجْرُورُ الْمُتَّصِلُ — بِهِ … بِنَا", "The attached pronoun of jarr: بِهِ … بِنَا", "Muttasıl mecrûr zamir: بِهِ … بِنَا"),
        plain={"en": "In أَنْصِرْ بِهِ the هِ hangs on the preposition: an attached pronoun of jarr. The same letters as the naṣb ones — هُ … كَ … "
                     "نَا — but the speaker is a bare yāʾ (بِي), and after a kasra the hāʾ takes a kasra (بِهِ).",
               "tr": "أَنْصِرْ بِهِ'de هِ cer harfine bağlıdır: muttasıl mecrûr zamir. Mansûblarla aynı harfler — هُ … كَ … نَا — ama mütekellim "
                     "yalnız yâdır (بِي) ve kesreden sonra hâ kesre alır (بِهِ)."},
        explanation={
            "en": "The attached pronouns of jarr hang on a preposition (بِهِ، لَهُ، عَلَيْهِ) or on the noun they are annexed to (نَاصِرُهُ «his "
                  "helper»). Marāḥ: «اثْنَا عَشَرَ لِلْمَجْرُورِ الْمُتَّصِلِ نَحْوُ ضَارِبُهُ إِلَى ضَارِبُنَا». The madrasa recites them through "
                  "the second verb of wonder, أَنْصِرْ بِهِ … أَنْصِرْ بِنَا. The letters are the attached naṣb letters; three things differ in "
                  "writing: the speaker is a yāʾ with no nūn of protection (بِي، لِي), the hāʾ takes a kasra after a kasra or a silent yāʾ (بِهِ، "
                  "عَلَيْهِ, against نَصَرَهُ), and لِ opens to لَ before every pronoun but the yāʾ (لَهُ، لَكَ — but لِي). There is no detached "
                  "pronoun of jarr. So when a student meets هُ، كَ or نَا, the question is only: what does it hang on? A verb or إِنَّ → naṣb; a "
                  "preposition or an annexed noun → jarr. " + mabni_en + neden_en,
            "tr": "Muttasıl mecrûr zamirler bir cer harfine (بِهِ، لَهُ، عَلَيْهِ) ya da muzâf olduğu isme (نَاصِرُهُ «onun yardımcısı») bağlanır. "
                  "Merâh: «اثْنَا عَشَرَ لِلْمَجْرُورِ الْمُتَّصِلِ نَحْوُ ضَارِبُهُ إِلَى ضَارِبُنَا». Medrese onları ikinci taaccüb fiiliyle okur: "
                  "أَنْصِرْ بِهِ … أَنْصِرْ بِنَا. Harfler muttasıl mansûb harfleridir; yazıda üç şey farklıdır: mütekellim nûn-ı vikâyesiz bir yâdır "
                  "(بِي، لِي), hâ bir kesreden ya da sakin yâdan sonra kesre alır (بِهِ، عَلَيْهِ; karşılığı نَصَرَهُ), ve لِ yâ dışındaki her zamirden "
                  "önce لَ olur (لَهُ، لَكَ — ama لِي). Munfasıl mecrûr zamir yoktur. Yani talebe هُ، كَ ya da نَا gördüğünde tek soru şudur: neye "
                  "bağlı? Fiil ya da إِنَّ → nasb; cer harfi ya da muzâf isim → cer. " + mabni_tr + neden_tr},
        tables=[tab("bi", H("أَنْصِرْ بِهِ … أَنْصِرْ بِنَا", "Through the second verb of wonder", "İkinci taaccüb fiiliyle"), {"k": "att", "host": "بِ", "kind": "harf", "pre": "أَنْصِرْ "},
                    rows=S14, keys=keys("jarrMuttasil", S14)),
                tab("li", H("لَهُ … لَنَا", "After لِ", "لِ ile"), {"k": "att", "host": "لِ", "kind": "harf"}, rows=S14)],
        quiz=1,
        examples=[["marah-al-arwah", 16, "s7"], ["izhar-al-asrar", 46, "s3"], ["al-kafiya", 3, "s10"]],
        mistakes=[dict(w={"src": {"k": "attSkip", "host": "بِ", "kind": "harf", "skip": ["harmony"]}, "i": 0}, r={"src": {"k": "att", "host": "بِ", "kind": "harf"}, "i": 0},
                       why={"en": "After the kasra of the bāʾ the hāʾ takes a kasra: بِهِ.", "tr": "Bânın kesresinden sonra hâ kesre alır: بِهِ."}),
                  dict(w={"src": {"k": "attSkip", "host": "لِ", "kind": "harf", "skip": ["lam"]}, "i": 6}, r={"src": {"k": "att", "host": "لِ", "kind": "harf"}, "i": 6},
                       why={"en": "لِ opens to لَ before a pronoun (except the yāʾ): لَكَ.", "tr": "لِ zamirden önce (yâ hariç) لَ olur: لَكَ."})],
        related=["huruf-jarr", "emsile-11-taajjub", "emsile-14-damir-nasb-muttasil", "emsile-17-damir-map"],
        sources=["مراح الأرواح", "الكافية (ابن الحاجب)", "إظهار الأسرار (البركوي)"],
    )

    N["emsile-17-damir-map"] = dict(
        title=H("الضَّمَائِرُ — الْخَمْسَةُ فِي جَدْوَلٍ وَاحِدٍ", "The pronouns: the five kinds in one table", "Zamirler: beş çeşit tek cetvelde"),
        plain={"en": "One table: fourteen persons down, five kinds across — attached rafʿ, detached rafʿ, attached naṣb, detached naṣb, attached "
                     "jarr. Tap a pronoun to see a story word that has it, with its iʿrāb.",
               "tr": "Tek cetvel: aşağıya on dört sîga, yana beş çeşit — muttasıl merfû, munfasıl merfû, muttasıl mansûb, munfasıl mansûb, muttasıl "
                     "mecrûr. Bir zamire dokun, onu taşıyan bir hikâye kelimesini i'rabıyla gör."},
        explanation={
            "en": "Marāḥ counts the pronouns instead of listing them: by case three (rafʿ, naṣb, jarr); each attached or detached — six; the "
                  "detached majrūr is taken out, because a majrūr never stands before its governor — five; each has eighteen forms in reason "
                  "and twelve in use, because the duals are shared — five times twelve, sixty. This table is that count. The first column shows "
                  "what the māḍī adds as its doer (empty where the doer hides — see the attached rafʿ note for where it may or must hide); the "
                  "other columns show the pronoun itself: هُوَ … نَحْنُ; هُ … نِي، نَا (with the nūn of protection after a verb); إِيَّاهُ … إِيَّانَا; "
                  "هُ … ي، نَا as it stands after لَ. Every cell is built by the app's pronoun engine; a cell with «*» has no authored iʿrāb line "
                  "on the shelf yet that gives it that place — the table says so rather than pretend. " + mabni_en + neden_en,
            "tr": "Merâh zamirleri listelemek yerine sayar: i'rab bakımından üç (ref', nasb, cer); her biri muttasıl ya da munfasıl — altı; munfasıl "
                  "mecrûr çıkarılır, çünkü mecrûr âmilinden önce gelmez — beş; her birinin akılda on sekiz, kullanımda on iki şekli vardır, çünkü "
                  "tesniyeler ortaktır — beş kere on iki, altmış. Bu cetvel o sayımdır. Birinci sütun mâzînin fâil olarak eklediğini gösterir (fâil "
                  "müstetir olan yerde boş — nerede cevâzen, nerede vücûben müstetir olduğunu muttasıl merfû notu söyler); diğer sütunlar zamirin "
                  "kendisini gösterir: هُوَ … نَحْنُ; هُ … نِي، نَا (fiilden sonra nûn-ı vikâye ile); إِيَّاهُ … إِيَّانَا; لَ'den sonraki hâliyle هُ … ي، "
                  "نَا. Her hücreyi uygulamanın zamir motoru kurar; «*» işaretli hücre için rafta ona o mahalli veren yazar i'rabı satırı henüz "
                  "yoktur — cetvel bunu saklamaz, söyler. " + mabni_tr + neden_tr},
        tables=[tab("map", H("الضَّمَائِرُ السِّتُّونَ", "The sixty pronouns", "Altmış zamir"),
                    {"cols": [{"k": "rafPron"}, {"k": "munf"}, {"k": "pron", "host": "نَصَرَ", "kind": "verb"}, {"k": "att", "host": "إِيَّا", "kind": "iyya"},
                              {"k": "pron", "host": "لِ", "kind": "harf"}]},
                    map=True, rows=S14,
                    keys=[[f"rafMuttasil:{s}" if s not in (0, 3) else None for s in S14], keys("rafMunfasil", S14), keys("nasbMuttasil", S14),
                          keys("nasbMunfasil", S14), keys("jarrMuttasil", S14)])],
        examples=[["izhar-al-asrar", 46, "s1"], ["al-kafiya", 3, "s9"], ["al-kafiya", 3, "s11"]],
        mistakes=[dict(w={"src": {"k": "attSkip", "host": "بِ", "kind": "harf", "skip": ["harmony"]}, "i": 2}, r={"src": {"k": "att", "host": "بِ", "kind": "harf"}, "i": 2},
                       why={"en": "After a kasra the hāʾ of the pronoun takes a kasra: بِهِمْ, as the table's jarr column shows after a kasra.",
                            "tr": "Kesreden sonra zamirin hâsı kesre alır: بِهِمْ."})],
        related=["emsile-12-damir-raf-muttasil", "emsile-13-damir-raf-munfasil", "emsile-14-damir-nasb-muttasil", "emsile-15-damir-nasb-munfasil",
                 "emsile-16-damir-jarr-muttasil", "al-marifa-al-mudmarat-wal-alam"],
        sources=["مراح الأرواح", "إظهار الأسرار (البركوي)", "الكافية (ابن الحاجب)"],
    )

    N["emsile-18-abwab"] = dict(
        title=H("أَبْوَابُ الْفِعْلِ — الْبِنَاءُ", "The bābs of the verb — an overview (the Bināʾ)", "Fiilin bâbları — genel bakış (Binâ)"),
        plain={"en": "Every bare three-letter verb belongs to one of six bābs, told apart by the middle vowel of the māḍī and the muḍāriʿ: "
                     "نَصَرَ يَنْصُرُ، ضَرَبَ يَضْرِبُ، فَتَحَ يَفْتَحُ، عَلِمَ يَعْلَمُ، حَسُنَ يَحْسُنُ، حَسِبَ يَحْسِبُ. The augmented bābs add letters.",
               "tr": "Her sülâsî mücerred fiil altı bâbdan birine aittir; bâbları mâzî ve muzârinin ortadaki harekesi ayırır: نَصَرَ يَنْصُرُ، ضَرَبَ "
                     "يَضْرِبُ، فَتَحَ يَفْتَحُ، عَلِمَ يَعْلَمُ، حَسُنَ يَحْسُنُ، حَسِبَ يَحْسِبُ. Ziyade bâblar harf ekler."},
        explanation={
            "en": "The Amthila recites one verb; the Bināʾ (Bināʾ al-afʿāl) shows which family a verb belongs to. The bare three-letter verb "
                  "has six bābs, named by their model verbs and known by the pair of vowels on the middle radical in the māḍī and the muḍāriʿ: "
                  "a–u (نَصَرَ يَنْصُرُ), a–i (ضَرَبَ يَضْرِبُ), a–a (فَتَحَ يَفْتَحُ — mostly with a throat letter), i–a (عَلِمَ يَعْلَمُ), u–u "
                  "(حَسُنَ يَحْسُنُ — qualities, never transitive), i–i (حَسِبَ يَحْسِبُ — few). A verb's bāb is heard, not reasoned. The augmented "
                  "bābs add one, two or three letters to the root, and each addition brings meanings (making someone do it, doing it together, "
                  "doing it to oneself, asking for it …); the second table shows them with the Bināʾ's sign of each and a model verb, all built by "
                  "the engine. The full account is in the level 2–5 notes linked below, and the Conjugation panel's «النَّقْل» tab carries any "
                  "sound root through all of them.",
            "tr": "Emsile tek bir fiili okur; Binâ (Binâü'l-ef'âl) bir fiilin hangi aileye ait olduğunu gösterir. Sülâsî mücerredin altı bâbı "
                  "vardır; model fiilleriyle anılır ve mâzî ile muzârinin ortadaki harfindeki hareke çiftiyle bilinir: fetha–damme (نَصَرَ يَنْصُرُ), "
                  "fetha–kesre (ضَرَبَ يَضْرِبُ), fethateyn (فَتَحَ يَفْتَحُ — çoğunlukla boğaz harfiyle), kesre–fetha (عَلِمَ يَعْلَمُ), dammeteyn "
                  "(حَسُنَ يَحْسُنُ — vasıflar, hiç müteaddî olmaz), kesreteyn (حَسِبَ يَحْسِبُ — az). Bir fiilin bâbı akılla değil semâ' ile bilinir. "
                  "Ziyade bâblar köke bir, iki ya da üç harf ekler ve her ek anlamlar getirir (yaptırmak, birlikte yapmak, kendine yapmak, istemek …); "
                  "ikinci cetvel onları Binâ'nın alâmetiyle ve bir model fiille gösterir, hepsini motor kurar. Tafsilat aşağıda bağlı 2–5. seviye "
                  "notlarındadır; Çekim panelinin «النَّقْل» sekmesi her sâlim kökü hepsinden geçirir."},
        tables=[tab("six", H("الثُّلَاثِيُّ الْمُجَرَّدُ — السِّتَّةُ الْأَبْوَابُ", "The six bābs of the bare verb", "Sülâsî mücerredin altı bâbı"),
                    {"k": "em2", "slots": ["mazi", "mudari"], "models": [0, 1, 2, 3, 4, 5]}, bab=True),
                tab("mazid", H("الثُّلَاثِيُّ الْمَزِيدُ", "The augmented bābs", "Sülâsî mezîd"), {"k": "door", "group": "mazid"}, door=True)],
        quiz=0,
        examples=[["marah-al-arwah", 7, "s2"], ["tasrif-al-izzi", 2, "s1"]],
        mistakes=[dict(w={"src": {"k": "mud", "root": R, "bab": 2}, "i": 0}, r={"src": {"k": "mud", "root": R, "bab": 1}, "i": 0},
                       why={"en": "نَصَرَ is of bāb 1: its muḍāriʿ is يَنْصُرُ with a ḍamma. The bāb is learnt by hearing; يَنْصِرُ (bāb 2's pattern) is not "
                                  "how the verb is said.",
                            "tr": "نَصَرَ birinci bâbdandır: muzârisi dammeyle يَنْصُرُ'dur. Bâb semâ' ile öğrenilir; يَنْصِرُ (ikinci bâbın kalıbı) bu "
                                  "fiilin söylenişi değildir."})],
        related=["thulathi-mujarrad-babs", "augmented-babs", "rubai-babs", "emsile-00-amthila"],
        sources=["بناء الأفعال", "مراح الأرواح", "تصريف العزي (الزنجاني)"],
    )
    return N


def cmd_spec():
    N = notes_spec()
    spec = {"notes": {}}
    for nid, n in N.items():
        spec["notes"][nid] = {"tables": n["tables"], "examples": n.get("examples", []), "mistakes": n.get("mistakes", [])}
    (HERE / "emsile359_spec.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
    print("spec:", len(spec["notes"]), "notes,", sum(len(n["tables"]) for n in spec["notes"].values()), "tables")


def src_line(text):
    """the book line that holds a story sentence verbatim (ʿIzzī / Marāḥ src) → «file:N (ص P)», else None"""
    for f in ("tasrif-al-izzi-src.txt", "marah-al-arwah-src.txt"):
        page = None
        for i, line in enumerate((SRC / f).read_text(encoding="utf-8").split("\n")):
            m = re.match(r"# page (\d+)", line)
            if m:
                page = m.group(1)
            if text and text in line:
                return f"{f}:{i + 1}" + (f" (ص {page})" if page else "")
    return None


def cmd_notes():
    N = notes_spec()
    cells = json.loads((HERE / "emsile359_cells.json").read_text(encoding="utf-8"))["notes"]
    cites = cite_lines()
    have = {p.stem for p in (ROOT / "content" / "grammar").glob("*.json")} | set(N)
    out_dir = ROOT / "content" / "grammar"
    for nid, n in N.items():
        c = cells[nid]
        exs = []
        for e in c["ex"]:
            if not e.get("ar"):
                raise SystemExit(f"{nid}: example {e['ref']} not found in the corpus")
            x = {"ar": e["ar"], "en": e["en"], "tr": e["tr"], "sourceStory": e["ref"][0], "sentence": e["ref"][2]}
            # ONE book line per note carries its place (the rule of the day reads it, and the hosted core keeps every cited example):
            # the others stay plain corpus examples, so the door's slice grows by one example a note
            s = src_line(e["ar"]) if e["ref"][0] in ("tasrif-al-izzi", "marah-al-arwah") and not any(y.get("source") for y in exs) else None
            if s:
                x["source"] = s
            exs.append(x)
        mks = []
        for m, mc in zip(n["mistakes"], c["mk"]):
            if not mc["wrong"] or not mc["right"] or mc["wrong"] == mc["right"]:
                raise SystemExit(f"{nid}: mistake not built by the engine: {mc}")
            mks.append({"wrong": mc["wrong"], "right": mc["right"], "why": {"en": m["why"]["en"], "tr": m["why"]["tr"]}})
        for t in c["tables"]:
            if not t.get("map") and not any(t.get("cells") or []):
                raise SystemExit(f"{nid}: table {t['id']} came back empty from the engine")
        rel = [r for r in n["related"] if r in have and r != nid]
        missing = [r for r in n["related"] if r not in have]
        if missing:
            raise SystemExit(f"{nid}: related notes missing: {missing}")
        srcs = list(n["sources"])
        # the Arabic terms of this note's tables, cited at a received line where one exists
        terms = set()
        for t in n["tables"]:
            for lab in t.get("labels") or []:
                terms.add(lab["ar"])
        for term, where in cites.items():
            if any(strip(term) in strip(x) for x in terms) or strip(term) in strip(n["title"]["ar"]):
                srcs.append(f"{where} — «{term}»")
        note = {"id": nid, "title": n["title"], "level": 1, "group": "emsile", "classicalSources": srcs,
                "plain": n["plain"],
                "explanation": {"en": n["explanation"]["en"] + PENDING["en"], "tr": n["explanation"]["tr"] + PENDING["tr"]},
                "examples": exs, "commonMistakes": mks, "relatedNotes": rel,
                "emsile359": {"tables": c["tables"], **({"quiz": n["quiz"]} if n.get("quiz") is not None else {}),
                              # how each common mistake was built (engine cells; the check «v359» builds them again)
                              "mk": [{"w": m["w"], "r": m["r"]} for m in n["mistakes"]]}}
        (out_dir / f"{nid}.json").write_text(json.dumps(note, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("notes written:", len(N))


if __name__ == "__main__":
    {"spec": cmd_spec, "notes": cmd_notes}[sys.argv[1] if len(sys.argv) > 1 else "spec"]()
