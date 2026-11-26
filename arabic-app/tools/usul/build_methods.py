"""(v352-U) item 4 — «المنهجان / İki yöntem»: Basra and Kufa as METHODS, for the top of the khilaf lab. Four cards, each the books' own
sentences verbatim with page (al-Iqtirāḥ's matn — never its editor's hashiya — and al-Khaṣāʾiṣ), our rendering, and the masāʾil of
content/rules/insaf_masail.json that show the method at work, joined BY SCRIPT: a masʾala is linked to a card only where al-Inṣāf's
stored text (`*_ar`, `others[].ar`) names that card's proof outright (samāʿ: النقل / السماع / سماعا / المسموع; qiyās: القياس / قياسا /
الشاذ). Writes content/rules/usul_methods.json. Run: python3 tools/usul/build_methods.py"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from src import BOOKS, ROOT, norm, on_page, pages  # noqa: E402

Q = lambda book, sp, ar, en, tr, by=None: {"book": book, "shamela": sp, "ar": ar, "en": en, "tr": tr, **({"by": by} if by else {})}
CARDS = [
    {"id": "sama", "title": {"en": "What counts as heard Arabic (samāʿ)", "tr": "Neyin duyulmuş Arapça (semâ') sayıldığı"},
     "join": r"النقل|السماع|سماعا|المسموع",
     "quotes": [
         Q("iqtirah", 391, "اتفقوا على أن البصريين أصح قياسا لأنهم لا يلتفتون إلى كل مسموع ولا يقيسون على الشاذ والكوفيين أوسع رواية.",
           "They agree that the Basrans are sounder in analogy — they do not heed everything heard, nor build analogy on the anomalous — and that the Kufans are wider in transmission.",
           "Basralıların kıyasta daha sağlam olduğunda ittifak ederler — her duyulana itibar etmez, şâza kıyas etmezler —; Kûfeliler ise rivayette daha geniştir."),
         Q("iqtirah", 392, "الكوفيون لو سمعوا بيتا واحدا فيه جواز شيء مخالف للأصول جعلوه أصلا وبوبوا عليه بخلاف البصريين",
           "(al-Andalusī, quoted:) Had the Kufans heard one verse allowing something against the rules, they would have made it a rule and given it a chapter — unlike the Basrans.",
           "(Endelüsî'den:) Kûfeliler kaidelere aykırı bir şeyi câiz kılan tek bir beyit duysalar onu asıl yapar, ona bâb açarlardı — Basralıların aksine.", "الأندلسي"),
         Q("iqtirah", 391, "الكوفيون علامون بأشعار العرب مطلعون عليها",
           "(Ibn Jinnī, quoted:) The Kufans are very learned in the Arabs' poetry and well acquainted with it.",
           "(İbn Cinnî'den:) Kûfeliler Arapların şiirlerini çok iyi bilir, onlara vâkıftırlar.", "ابن جني")]},
    {"id": "qiyas", "title": {"en": "How far analogy (qiyās) is carried", "tr": "Kıyasın ne kadar ileri götürüldüğü"},
     "join": r"القياس|قياسا|الشاذ",
     "quotes": [
         Q("iqtirah", 402, "فإن مذهب الكوفيين القياس على الشاذ, ومذهب البصريين اتباع التأويلات البعيدة",
           "The Kufans' way is analogy on the anomalous; the Basrans' way is to follow far-fetched interpretations.",
           "Kûfelilerin yolu şâza kıyastır; Basralılarınki uzak te'villere uymaktır."),
         Q("khasais", 121, "إذا تعارضا نطقت بالمسموع على ما جاء عليه ولم تقسه في غيره",
           "(Ibn Jinnī, on hearing and analogy:) When the two conflict, you say the heard form as it came and do not extend it by analogy to anything else.",
           "(İbn Cinnî, semâ' ile kıyas hakkında:) İkisi çatışınca duyulanı geldiği gibi söylersin, başkasına kıyas etmezsin."),
         Q("iqtirah", 168, "كما لا يقاس على الشاذ نطقا لا يقاس عليه تركا",
           "As the anomalous is no model for what you say, it is no model for what you leave unsaid.",
           "Şâz söylenende kıyas yeri olmadığı gibi, terk edilende de kıyas yeri değildir.")]},
    {"id": "whom", "title": {"en": "From whom the language is taken", "tr": "Dilin kimden alındığı"},
     "join": None,
     "quotes": [
         Q("khasais", 397, "علّة امتناع ذلك ما عَرَضَ للغات الحاضرة وأهل المدر من الاختلال والفساد والخطل",
           "(Ibn Jinnī, on not taking from the town-dwellers as from the tent-dwellers:) the reason is the disorder, corruption and error that befell the speech of the settled.",
           "(İbn Cinnî, şehirlilerden bedevîlerden alındığı gibi alınmaması hakkında:) sebebi, yerleşiklerin dilini saran bozukluk, fesat ve hatadır."),
         Q("iqtirah", 392, "ومما افتخر به البصريون على الكوفيون أن قالوا: نحن نأخذ اللغة من حوشة الضباب وأكلة اليرابيع",
           "Among the Basrans' boasts over the Kufans: «We take the language from the hunters of lizards and the eaters of jerboas» (the desert Arabs)…",
           "Basralıların Kûfelilere övündüklerinden: «Biz dili kertenkele avcılarından ve araptavşanı yiyenlerden (çöl Araplarından) alırız»…"),
         Q("iqtirah", 393, "وأنتم تأخذونها عن أكلة الشواء وباعة الكواميخ",
           "…«and you take it from the eaters of roast meat and the sellers of pickles» (the townsfolk).",
           "…«siz ise onu kebap yiyenlerden ve turşu satanlardan (şehirlilerden) alırsınız».")]},
    {"id": "dalil", "title": {"en": "The proof, not the school", "tr": "Mezhep değil, delil"},
     "join": None,
     "quotes": [
         Q("iqtirah", 392, "ولسنا متعبدين باتباع مذهب البصريين بل نتبع الدليل",
           "(Abū Ḥayyān, quoted:) We are not bound to follow the Basrans' school as a matter of worship; we follow the proof.",
           "(Ebû Hayyân'dan:) Basralıların mezhebine uymakla mükellef değiliz; delile uyarız.", "أبو حيان"),
         Q("iqtirah", 402, "لابن مالك في النحو طريقة سلكها بين طريقي البصريين والكوفيين",
           "Ibn Mālik has his own way in grammar, taken between the ways of the Basrans and the Kufans.",
           "İbn Mâlik'in nahivde, Basralılar ile Kûfelilerin yolları arasında tuttuğu bir yolu vardır.")]},
]


def main():
    src = {b: pages(b) for b in BOOKS}
    ins = json.loads((ROOT / "content/rules/insaf_masail.json").read_text(encoding="utf-8"))["masail"]
    def stored(r):
        return norm(" ".join([r.get("title_ar", ""), r.get("kufa_ar", ""), r.get("basra_ar", ""), r.get("tarjih_ar", "")] +
                             [o.get("ar", "") for o in r.get("others", [])]))
    cards = []
    for c in CARDS:
        qs = []
        for q in c["quotes"]:
            t, ps = src[q["book"]]
            assert on_page(q["book"], q["shamela"], q["ar"], t, ps), (c["id"], q["shamela"], q["ar"][:30])
            p = next(x for x in ps if x["sp"] == q["shamela"])
            qs.append({**q, "page": f"{p['vol']}:{p['pp']}", "book_ar": BOOKS[q["book"]]["ar"]})
        ms = [r["n"] for r in ins if c["join"] and re.search(norm(c["join"]), stored(r))]
        cards.append({"id": c["id"], "title": c["title"], "quotes": qs, "masail": ms, "join": c["join"]})
    d = {"built_by": "tools/usul/build_methods.py (v352-U)",
         "about": "«المنهجان / İki yöntem» — why Basra and Kufa differ as methods: the books' own sentences, verbatim with page; our renderings "
                  "pending the hoca; `masail` = the al-Inṣāf records whose stored text names the card's proof outright (`join`, letters-only).",
         "counts": {"cards": len(cards), "quotes": sum(len(c["quotes"]) for c in cards), "links": sum(len(c["masail"]) for c in cards)},
         "cards": cards}
    (ROOT / "content/rules/usul_methods.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(d["counts"], [(c["id"], c["masail"]) for c in cards])


if __name__ == "__main__":
    main()
