"""(v352-U) item 3 — the kinds of ʿilla AS al-Iqtirāḥ GIVES THEM (masʾala 2 of the faṣl on the ʿilla, Shamela pp. 205–216): al-Dīnawarī
al-Jalīs's list of twenty-four (reported from «ثمار الصناعة»), each kind with the example Ibn Maktūm gives in his Tadhkira as al-Suyūṭī
quotes it (Ibn al-Ṣāʾigh's for «التحليل», which Ibn Maktūm could not explain) — verbatim, page by page; then the reasons already in
content/rules/ilal.json tagged with a kind ONLY where the reason's own words decide it (a marker below, read in the reason clause from
`why_at`); untagged otherwise. Writes content/rules/ilal_kinds.json — a NEW side table; ilal.json's entries are never edited.
Run after any append to ilal.json: python3 tools/usul/kinds.py"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from src import ROOT, norm, on_page, pages  # noqa: E402

LIST = {"ar": "إلا أن مدار المشهورة منها على أربعة وعشرين نوعا", "shamela": 205, "page": "1:227"}
# (id, the example line verbatim, its Shamela page, en, tr) — the order is the list's
KINDS = [
    ("sama", "علة سماع", "قوله: علة سماع: مثل قولهم: امرأة ثدياء، ولا يقال: رجل أثدي، وليس لذلك علة سوى السماع.", 208,
     "Hearing: they say «imraʾa thadyāʾ» but not «rajul athdā» — there is no reason for it but that it was heard.",
     "Semâ': «imraetün sedyâ» denir, «racülün esdâ» denmez — bunun duyulmaktan başka sebebi yoktur."),
    ("tashbih", "علة تشبيه", "وعلة تشبيه مثل إعراب المضارع لمشابهته الاسم وبناء بعض الأسماء لمشابهتها الحروف.", 208,
     "Likeness: the muḍāriʿ is declined because it resembles the noun; some nouns are built because they resemble particles.",
     "Benzetme: muzâri' isme benzediği için mu'rebdir; bazı isimler harflere benzedikleri için mebnîdir."),
    ("istighna", "علة استغناء", "وعلة استغناء كاستغنائهم بـ ترك عن ودع", 208,
     "Dispensing: they make do with «taraka» instead of «wadaʿa».", "İstiğnâ: «vede'a» yerine «terake» ile yetinmeleri."),
    ("istithqal", "علة استثقال", "وعلة استثقال كاستثقالهم الواو في يعد لوقوعها بين ياء وكسرة", 208,
     "Heaviness: they find the wāw of «yaʿidu» heavy, standing between a yāʾ and a kasra.",
     "Ağırlık: «ya'idu»daki vâvı, yâ ile kesre arasında kaldığı için ağır bulmaları."),
    ("farq", "علة فرق", "وعلة فرق وذلك فيما ذهبوا إليه من رفع الفاعل ونصب المفعول وفتح نون الجمع وكسر نون المثنى.", 209,
     "Distinction: the fāʿil is rafʿ and the mafʿūl naṣb, the plural's nūn has fatḥa and the dual's kasra — to tell them apart.",
     "Ayırma: fâil merfû, mef'ûl mansûb; cemi nûnu fethalı, tesniye nûnu kesreli — ayırt etmek için."),
    ("tawkid", "علة توكيد", "وعلة توكيد مثل إدخالهم النون الخفيفة والثقيلة في فعل الأمر لتأكيد إيقاعه.", 209,
     "Emphasis: they add the light and the heavy nūn to the imperative to stress that it be done.",
     "Te'kîd: emir fiiline hafif ve sakil nûnu, yapılmasını pekiştirmek için katmaları."),
    ("tawid", "علة تعويض", "وعلة تعويض مثل تعويضهم الميم في اللهم من حرف النداء.", 209,
     "Compensation: the mīm of «allāhumma» stands in for the vocative particle.",
     "Ivaz: «Allâhümme»deki mîm, nidâ harfinin yerine gelmiştir."),
    ("nazir", "علة نظير", "وعلة نظير مثل كسرهم أحد الساكنين إذا التقيا في الجزم حملا على الجر إذ هو نظيره.", 209,
     "Counterpart: when two sukūns meet in the jazm they give one a kasra, carrying it over to the jarr, its counterpart.",
     "Nazîr: cezimde iki sâkin buluşunca birini kesrelemeleri — nazîri olan cerre hamlederek."),
    ("naqid", "علة نقيض", "وعلة نقيض مثل نصبهم النكرة بـ لا حملا على نقيضها إن.", 209,
     "Opposite: the indefinite after «lā» is naṣb, carried over to its opposite «inna».",
     "Nakîz: «lâ»dan sonraki nekrenin, zıddı olan «inne»ye hamlen mansûb olması."),
    ("haml_mana", "علة حمل على المعنى", "وعلة حمل على المعنى مثل (فمن جاءه موعظة) ذكر فعل الموعظة وهي مؤنثة حملا لها على المعنى وهو الوعظ", 209,
     "Carrying on the meaning: «fa-man jāʾahu mawʿiẓa» — the verb is masculine though «mawʿiẓa» is feminine, carried on its meaning, «waʿẓ».",
     "Mânâya hamil: «fe-men câehû mev'ızatün» — mev'ıza müennes iken fiil müzekker; mânâsı olan «va'z»a hamledilmiştir."),
    ("mushakala", "علة مشاكلة", "وعلة مشاكلة مثل قوله (سلاسلا وأغلالا)", 210,
     "Matching: «salāsilan wa-aghlālan» (sic: the diptote given tanwīn to match its neighbour).",
     "Müşâkele: «selâsilen ve ağlâlen» (gayr-i munsarif, yanındakine uysun diye tenvinli)."),
    ("muadala", "علة معادلة", "وعلة معادلة مثل جرهم ما لا ينصرف بالفتح حملا على النصب ثم عادلوا بينهما فحملوا النصب على الجر في جمع المؤنث السالم.", 210,
     "Balancing: the diptote's jarr is a fatḥa, carried on the naṣb; then they balanced it — the sound feminine plural's naṣb is carried on the jarr.",
     "Muâdele: gayr-i munsarifin cerri fethadır, nasba hamlen; sonra denkleştirdiler — cem-i müennes-i sâlimin nasbı cerre hamledildi."),
    ("mujawara", "علة قرب ومجاورة", "وعلة مجاورة مثل الجر بالمجاورة في قولهم جحر ضب خرب وضم لام (الله) في (الحمد لله)", 210,
     "Neighbourhood: the jarr by neighbourhood in «juḥru ḍabbin kharibin», and the ḍamma on the lām of «lillāh» in «al-ḥamdu lillāh» (beside the dāl).",
     "Komşuluk: «cuhru dabbin haribin»deki komşuluk cerri ve «el-hamdu lillâh»da lâmın (dâle komşu olduğu için) zammesi."),
    ("wujub", "علة وجوب", "وعلة وجوب وذلك تعليلهم رفع الفاعل ونحوه.", 212,
     "Necessity: as when they give the reason why the fāʿil MUST be rafʿ, and the like.",
     "Vücûb: fâilin merfû olmasının (ve benzerlerinin) gerekçesini vermeleri gibi."),
    ("jawaz", "علة جواز", "وعلة جواز وذلك ما ذكروه في تعليل الإمالة من الأسباب المعروفة فإن ذلك علة لجواز الإمالة فيما أميل لا لوجوبها.", 212,
     "Permission: the known causes of imāla — they let a word be pronounced with imāla, they do not require it.",
     "Cevaz: imâlenin bilinen sebepleri — imâleyi câiz kılar, vâcip kılmaz."),
    ("taghlib", "علة تغليب", "وعلة تغليب مثل (وكانت من القانتين)", 212,
     "Predominance: «wa-kānat mina l-qānitīn» (a woman counted among the masculine «qānitīn»).",
     "Tağlîb: «ve kânet mine'l-kânitîn» (bir kadın müzekker «kânitîn» içinde sayılır)."),
    ("ikhtisar", "علة اختصار", "وعلة اختصار مثل باب الترخيم و (لم يك)", 212,
     "Brevity: the chapter of tarkhīm, and «lam yaku».", "İhtisâr: terhîm bâbı ve «lem yek»."),
    ("takhfif", "علة تخفيف", "وعلة تخفيف كالإدغام.", 213, "Lightening: as with idghām.", "Tahfîf: idğam gibi."),
    ("dalalat_hal", "علة دلالة حال", "وعلة دلالة حال كقول المستهل الهلال أي هذا الهلال فحذف لدلالة الحال عليه.", 214,
     "The situation's pointing: one who sights the new moon says «al-hilāl», i.e. «this is the new moon» — left out because the situation shows it.",
     "Hâlin delâleti: hilâli gören «el-hilâl» der, yani «bu hilâldir» — hâl gösterdiği için hazfedilmiştir."),
    ("asl", "علة أصل", "وعلة أصل كـ استحوذ ويؤكرم وصرف", 213,
     "The origin: as in «istaḥwadha», «yuʾakrimu» and giving tanwīn to (a diptote) — the original form showing.",
     "Asıl: «istahveze», «yu'ekrimu» ve (gayr-i munsarifin) sarfı gibi — aslın görünmesi."),
    ("tahlil", "علة تحليل", "في نحو الاستدلال على اسمية كيف بنفي حرفيتها لأنها مع الاسم كلام ونفي فعليتها لمجاورتها الفعل بلا فاصل", 216,
     "Analysis (Ibn al-Ṣāʾigh's explanation): proving «kayfa» a noun by ruling out the particle (with a noun it makes speech) and the verb (it stands next to a verb).",
     "Tahlîl (İbnü's-Sâiğ'in açıklaması): «keyfe»nin isim olduğunu, harf (isimle kelâm olur) ve fiil (fiile bitişik gelir) olmadığını göstererek ispat."),
    ("ishar", "علة إشعار", "وعلة إشعار كقولهم في جمع موسى موسون بفتح ما قبل الواو إشعار بأن المحذوف ألف.", 214,
     "Signalling: the plural of «Mūsā» is «Mūsawn», with a fatḥa before the wāw to signal that what dropped was an alif.",
     "İş'âr: «Mûsâ»nın cemi «Mûsevn» — vâvdan önceki fetha, düşenin elif olduğunu bildirir."),
    ("tadadd", "علة تضاد", "وعلة تضاد مثل قولهم في الأفعال التي يجوز إلغاؤها متى تقدمت وأكدت بالمصدر أو بضميره لم تلغ أصلا لما بين", 214,
     "Contrariety: the verbs that may be left ungoverning are never left so when they come first and are stressed by their maṣdar — stress and cancelling are contraries.",
     "Tezâd: ilgâsı câiz fiiller öne geçip masdarla te'kîd edilince asla ilgâ edilmez — te'kîd ile ilgâ zıttır."),
    ("awla", "علة أولى", "وعلة أولى كقولهم: إن الفاعل أولى برتبة التقديم من المفعول", 214,
     "Priority: as they say, the fāʿil has the better claim to the front than the mafʿūl.",
     "Evleviyet: fâil öne geçmeye mef'ûlden daha lâyıktır demeleri gibi."),
]
NAMES_PAGE = {"istithqal": 208, "mushakala": 210, "sama": 205, "tashbih": 205, "istighna": 205, "farq": 206, "tawkid": 206, "tawid": 206, "nazir": 206, "naqid": 206,
              "haml_mana": 206, "muadala": 207, "mujawara": 207, "wujub": 207, "jawaz": 207, "taghlib": 207,
              "ikhtisar": 207, "takhfif": 207, "dalalat_hal": 207, "asl": 207, "tahlil": 207, "ishar": 207, "tadadd": 207, "awla": 207}
SEC = {"ar": "اعتلالات النحويين صنفان", "shamela": 205}
SARRAJ = {"ar": "وضرب يسمى علة العلة مثل أن يقولوا:", "shamela": 216}

# markers, by the reason's own words (letters-only match, see norm): first one in the reason clause decides
MARK = [
    ("tadadd", r"لتدافع|للتضاد|من التضاد|لتضاد"),   # contrariety named as THE reason outranks an earlier adverbial («ما حذف تخفيفًا»)
    ("farq", r"للفرق|فرقا بين|فرقًا بين|ليفرق|ليفرقوا|للفصل بين"),
    ("haml_mana", r"حملا على المعنى|حمل على المعنى|حملًا على المعنى"),
    ("naqid", r"حملا على (نقيض|ضد)|لأنه نقيض|لانه نقيض|نقيضه|نقيضها"),
    ("nazir", r"نظيره|نظيرها|لأنه نظير"),
    ("haml_lafz", r"حملا على (اللفظ|الموضع|المحل)|حملًا على (اللفظ|الموضع|المحل)"),
    ("tashbih", r"تشبيها|تشبيهًا|لشبهه|لشبهها|لمشابهته|لمشابهتها|لمضارعته|لمضارعتها|حملا على|حملًا على|بالحمل على"),
    ("tawid", r"عوضا|عوضًا|للتعويض|تعويضا"),
    ("takhfif", r"إرادة التخفيف|للتخفيف|تخفيفا|تخفيفًا|طلبا للخفة|للخفة|استخفافا"),
    ("istithqal", r"الثقل|لثقل|الاستثقال|استثقالا|لاستثقال|استثقال|لثقله|لثقلها"),
    ("tawkid", r"للتأكيد|للتوكيد|تأكيدا|توكيدا"),
    ("istighna", r"استغناء|للاستغناء|استغنوا|استغني"),
    ("ikhtisar", r"اختصارا|للاختصار|للإيجاز|إيجازا"),
    ("mujawara", r"للمجاورة|لمجاورة|بالمجاورة|لمجاورته|لمجاورتها"),
    ("mushakala", r"للمشاكلة|مشاكلة"),
    ("dalalat_hal", r"لدلالة الحال"),
    ("ishar", r"إشعارا|للإشعار|ليشعر"),
    ("taghlib", r"تغليبا|للتغليب"),
]


def tag(r):
    s = norm(r["ar"][r.get("why_at") or 0:])
    best = None
    for k, rx in MARK:
        m = re.search(r"(?:^|(?<=[\s(«\"،,.:؛]))[وف]?(?:" + norm(rx) + ")", s)
        if m and k == "tadadd":
            return (k, m.start(), m.group(0))
        if m and k == "haml_lafz":
            return None        # ḥaml on the word / the position: the words say ḥaml, not one of the twenty-four — left untagged
        if m and (best is None or m.start() < best[1]):
            best = (k, m.start(), r["ar"][r.get("why_at") or 0:][m.start():m.end()] if False else m.group(0))
    return best


def main():
    t, ps = pages("iqtirah")
    for k, name, ex, sp, en, tr in KINDS:
        assert on_page("iqtirah", sp, ex, t, ps), (k, sp)
        assert on_page("iqtirah", NAMES_PAGE.get(k, 205), name, t, ps), (k, name)
    for x in (LIST, SEC, SARRAJ):
        assert on_page("iqtirah", x["shamela"], x["ar"], t, ps), x
    reasons = json.loads((ROOT / "content/rules/ilal.json").read_text(encoding="utf-8"))["reasons"]
    tags = {}
    for r in reasons:
        b = tag(r)
        if b:
            tags[r["id"]] = {"kind": b[0], "marker": b[2]}
    vp = {p["sp"]: f"{p['vol']}:{p['pp']}" for p in ps}
    d = {"built_by": "tools/usul/kinds.py (v352-U)",
         "about": "The kinds of ʿilla as al-Suyūṭī's al-Iqtirāḥ reports them (al-Dīnawarī al-Jalīs, «ثمار الصناعة»: twenty-four, «the "
                  "famous ones»; the examples are Ibn Maktūm's from his Tadhkira, «التحليل» Ibn al-Ṣāʾigh's), verbatim with the Shamela page; "
                  "and the reasons of content/rules/ilal.json tagged with a kind only where their own words decide it (the marker, in "
                  "letters-only form). The renderings are ours, pending the hoca.",
         "source": {"book": "iqtirah", "file": "research/sources/al-iqtirah-suyuti-src.txt", "list": {**LIST, "page": vp[205]},
                    "classes": SEC, "illat_al_illa": SARRAJ},
         "kinds": [{"id": k, "name_ar": name, "n": i + 1, "list_shamela": NAMES_PAGE.get(k, 205), "ex_ar": ex, "shamela": sp,
                    "page": vp[sp], "by": "tahlil" == k and "ابن الصائغ" or "ابن مكتوم", "en": en, "tr": tr}
                   for i, (k, name, ex, sp, en, tr) in enumerate(KINDS)],
         "counts": {"kinds": len(KINDS), "reasons": len(reasons), "tagged": len(tags)},
         "tags": tags}
    (ROOT / "content/rules/ilal_kinds.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    from collections import Counter
    print(d["counts"], Counter(v["kind"] for v in tags.values()))


if __name__ == "__main__":
    main()
