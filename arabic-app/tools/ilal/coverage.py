"""(v348-F) step 5 — the ledger of use: research/commentary-coverage-2026-11-27.md, from the TOCs, the join table, the cut and the
kept reasons. Run: python3 tools/ilal/coverage.py"""
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import BOOKS, ROOT  # noqa: E402
from cut_reasons import WAVE  # noqa: E402

J = lambda f: json.loads((ROOT / f).read_text(encoding="utf-8"))  # noqa: E731


def main():
    links, il, cand = J("content/rules/commentary_links.json"), J("content/rules/ilal.json"), J("research/ilal/candidates.json")["candidates"]
    R = il["reasons"]
    out = ["# The three commentaries — what v348-F used and what remains (2026-11-27)", "",
           "Built by `tools/ilal/coverage.py` from `content/rules/toc_*.json`, `content/rules/commentary_links.json`, "
           "`research/ilal/candidates.json` and `content/rules/ilal.json`. A *reason* is a sentence of taʿlīl kept verbatim "
           "(unvowelled as printed), anchored by book, vol:page and Shamela page; the en/tr renderings are ours and await the hoca.", ""]
    out += ["## Totals", "", f"- Reasons kept: **{len(R)}** — " + ", ".join(f"{k} {v}" for k, v in il["counts"]["by_kind"].items()) +
            f"; rendered {il['counts']['rendered']}, short enough for the round {il['counts']['short']}.",
            f"- Candidates cut by script: {len(cand)}; read by hand: the Shaykhzāde ones that name an iʿrāb term (193 of "
            f"{sum(1 for c in cand if c['book'] == 'shaykhzade')}), and from the two big books the shortest per topic (see below).",
            f"- Join table: {links['counts']['ledger_joined']} of {links['counts']['ledger_entries']} ledger entries and "
            f"{links['counts']['notes_joined']} of {links['counts']['notes']} grammar notes reach at least one commentary section; "
            f"{links['counts']['qawaid_matn_to_shaykhzade']} Qawāʿid entries are joined to the Shaykhzāde page that quotes them.", ""]
    for b in BOOKS:
        toc = J(f"content/rules/toc_{b}.json")
        text = [s for s in toc["sections"] if s["part"] == "text"]
        joined = {r["section"] for x in links["links"] for r in x["commentary"] if r["book"] == b}
        rb = [r for r in R if r["book"] == b]
        cb = [c for c in cand if c["book"] == b]
        out += [f"## {toc['title']['en']} ({toc['title']['ar']})", "",
                f"- Pages {toc['pages']}; sections {toc['counts']['sections']} ({len(text)} of the text"
                + (f"; the naẓm's verses recognised: {toc['counts']['verses']}" if b == "ibn-malik" else "") + ").",
                f"- Sections joined to the app's rules: {len(joined & {s['title'] for s in text})} of {len(text)}.",
                f"- Scanned for reasons: " + ("the whole text (every page)." if b == "shaykhzade" else
                                             "the sections of the topics " + ", ".join(WAVE[b]) + "."),
                f"- Candidates cut: {len(cb)}; kept: {len(rb)} — " + ", ".join(f"{k} {v}" for k, v in Counter(r["kind"] for r in rb).items()) + ".",
                f"- Topics with a reason: " + ", ".join(sorted({r["topic"] for r in rb})) + ".", ""]
        if b != "shaykhzade":
            scanned = {s["n"] for k in WAVE[b] for s in links["topics"][k]["sections"] if s["book"] == b}
            rest = [s for s in text if s["n"] not in scanned]
            out += [f"**Not yet scanned** ({len(rest)} sections, {sum(s['pages'] for s in rest)} pages):", "",
                    "; ".join(f"{s['title']} ({s['vol']}:{s['from']['page']}–{s['to']['page']})" for s in rest), ""]
        else:
            seen = {r["id"] for r in rb}
            unread = [c for c in cb if "ilal-" + c["cid"].replace(":", "-") not in seen]
            out += [f"**Cut but not kept**: {len(unread)} candidates — the preface's etymologies and praise (pp. 13–20), sentences "
                    "that explain Ibn Hishām's wording rather than a rule, Qurʾānic tafsīr, and long disputes left for the next reading.", ""]
    notes = {x["topic"][5:]: x for x in links["links"] if x["topic"].startswith("note:")}
    have = {t for r in R for t in [r["topic"]]}
    got = sorted(n for n, x in notes.items() if set(x["topics"]) & have)
    none = sorted(n for n, x in notes.items() if x.get("group") in ("nahw", "awamil", "sarf") and not set(x["topics"]) & have)
    topics_none = sorted(k for k in links["topics"] if k not in have and links["topics"][k]["sections"])
    out += ["## The app's topics", "", f"**Notes that show at least one reason ({len(got)}):** " + ", ".join(got) + ".", "",
            f"**Naḥw / ṣarf notes with none yet — the next round's list ({len(none)}):** " + ", ".join(none) + ".", "",
            f"**Topics joined to sections but with no reason kept ({len(topics_none)}):** " + ", ".join(topics_none) + ".", "",
            "## Read but not kept, and what the books do not say", "",
            "- From Ibn Mālik's sections of the fāʿil, the nāʾib, the pronouns, the demonstratives and the five verbs the candidates were "
            "read; what was kept is about order, deletion and the follower's case — NEITHER Ibn Mālik's bāb al-fāʿil NOR Shaykhzāde "
            "states why the fāʿil itself is rafʿ, so the chain's «family → state» step for the fāʿil has no book reason (the reason the "
            "owner's own example asks for lives in books like Ibn al-Anbārī's Asrār al-ʿArabiyya — not received).",
            "- How much of the cut was READ: Shaykhzāde — the 193 candidates (of 379) that name an iʿrāb term; Ibn Mālik — per WAVE "
            "topic the shortest 14–25 (about 260 of 350); al-Raḍī — the 26 under 33 words, 23 of 33–70 words in the core iʿlāl / "
            "idghām / hamza sections and a search for the classic formulae (about 60 of 255). The rest of the cut is the next round's "
            "reading list (research/ilal/candidates.json).",
            "- Ibn Mālik's signs chapter (1:174–221) is terse: 25 candidates (most about the jussive jawāb and the asmāʾ al-afʿāl), 6 kept.", "",
            "## For the hoca", "",
            f"- Every rendering ({il['counts']['rendered']}) is ours and shows «çeviri · hoca onayı bekliyor»; not rendered (Arabic only): "
            + ", ".join(r["id"] for r in R if "en" not in r) + ".",
            "- Reasons that report another grammarian's view (al-Kisāʾī, al-Akhfash, al-Khalīl and Sībawayh, Ibn Kharūf, the Kūfans, "
            "the Banū Tamīm) are kept as the book reports them; the rendering names whose view it is: "
            + ", ".join(r["id"] for r in R if any(w in r.get("en", "") for w in ("Kisāʾī", "Akhfash", "Khalīl", "Kharūf", "Kūfans", "Tamīm", "Sībawayh", "Māzinī"))) + ".",
            "- The kinds were assigned by us (why-state / why-sign / why-built / why-form / why-order / objection); `why-order` also "
            "carries the fāʾ of the khabar and of the jawāb (a matter of what may stand where).", "",
            "## Not used at all", "",
            "- al-Raḍī vol. 4 = al-Baghdādī's Sharḥ shawāhid al-Shāfiya (511 pages) — the verses' commentary, not taʿlīl of rules.",
            "- Ibn Mālik vol. 5 (indexes) and both editors' introductions.",
            "- The naẓm's verses themselves (the reasons are cut from the prose «ش» only).",
            "- Footnotes (the editors' variants) everywhere.", ""]
    (ROOT / "research/commentary-coverage-2026-11-27.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("wrote research/commentary-coverage-2026-11-27.md", len(got), len(none), len(topics_none))


if __name__ == "__main__":
    main()
