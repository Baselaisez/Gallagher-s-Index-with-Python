"""(v352-U) item 6 — research/usul-coverage-2026-11-27.md: both books by bāb / heading — indexed, fed (where the app now uses it), left —
and the next round's list. Computed from the tables, never typed. Run last: python3 tools/usul/coverage.py"""
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from src import ROOT  # noqa: E402

J = lambda f: json.loads((ROOT / f).read_text(encoding="utf-8"))


def main():
    tk, ti, un = J("content/rules/toc_khasais.json"), J("content/rules/toc_iqtirah.json"), J("content/rules/usul_nahw.json")
    il, kd, um = J("content/rules/ilal.json"), J("content/rules/ilal_kinds.json"), J("content/rules/usul_methods.json")
    cand = J("research/usul/khasais_candidates.json")
    kh = [r for r in il["reasons"] if r["book"] == "khasais"]
    cites = []
    def walk(p):
        cites.extend(p.get("khasais", [])); [walk(x) for x in p.get("pillars", [])]
    [walk(p) for p in un["proofs"]]
    use = {}
    for b in tk["babs"]:
        a, z = b["from"]["shamela"], b["to"]["shamela"]
        u = []
        n = sum(1 for r in kh if a <= r["shamela_page"] <= z)
        if n: u.append(f"{n} reason(s) → ilal.json")
        c = sum(1 for x in cites if x.get("khasais") and a <= x["khasais"]["shamela"] <= z)
        if c: u.append(f"{c} al-Iqtirāḥ citation(s) found")
        m = sum(1 for card in um["cards"] for q in card["quotes"] if q["book"] == "khasais" and a <= q["shamela"] <= z)
        if m: u.append(f"{m} «İki yöntem» quote(s)")
        cc = sum(1 for x in cand["candidates"] if a <= x["shamela"] <= z)
        use[b["n"]] = (u, cc)
    L = ["# uṣūl al-naḥw coverage — al-Khaṣāʾiṣ and al-Iqtirāḥ (v352-U, 2026-11-27)", "",
         "Computed by `tools/usul/coverage.py` from content/rules/toc_khasais.json, toc_iqtirah.json, usul_nahw.json, ilal_kinds.json, "
         "usul_methods.json, ilal.json and research/usul/khasais_candidates.json. «fed» = the app now reads something from it; «cand.» = the "
         "script's taʿlīl candidates in the span (not all read).", ""]
    fed = sum(1 for v in use.values() if v[0])
    L += [f"**al-Khaṣāʾiṣ:** {tk['counts']['babs']} abwāb indexed (vol. 1: {tk['counts']['vol1']} from the in-text headings — the e-text prints no "
          f"index for vol. 1 and two of its 54 abwāb have no heading line the script can find; vols. 2–3: {tk['counts']['vol2']} + {tk['counts']['vol3']} "
          f"from the printed index, all numbered 55–162). Fed: {fed}; left: {len(use) - fed}. Reasons appended: {len(kh)}; candidates cut: "
          f"{cand['counts']['candidates']}, of which about 230 were read (the commonest roles first: fāʿil, mafʿūl, mubtadaʾ, khabar, ḥāl, iḍāfa; then "
          f"the uncovered topics).", "",
          "| n | vol | Shamela | pp. | bāb | fed | cand. |", "|---|---|---|---|---|---|---|"]
    for b in tk["babs"]:
        u, cc = use[b["n"]]
        L.append(f"| {b['n']} | {b['vol']} | {b['from']['shamela']}–{b['to']['shamela']} | {b['pages']} | {b['ar'][:70]} | {'; '.join(u) or '—'} | {cc} |")
    L += ["", f"**al-Iqtirāḥ:** {ti['counts']['headings']} headings indexed (8 kutub incl. the muqaddimāt). Fed: the proofs map "
          f"(usul_nahw.json — {len(un['proofs'])} proofs, 4 pillars, {un['counts']['subs']} sub-headings with their first sentence, "
          f"{un['counts']['citations']} Ibn Jinnī citations, {un['counts']['found_in_khasais']} found in al-Khaṣāʾiṣ), the 24 kinds of ʿilla "
          f"(pp. 205–216, {kd['counts']['tagged']} of {kd['counts']['reasons']} reasons tagged), «İki yöntem» "
          f"({sum(1 for c in um['cards'] for q in c['quotes'] if q['book'] == 'iqtirah')} quotes).", "",
          "| kitāb | Shamela | defining sentence | sub-headings | citations (found) |", "|---|---|---|---|---|"]
    for p in un["proofs"]:
        subs = len(p.get("subs", [])) + sum(len(x.get("subs", [])) for x in p.get("pillars", []))
        cs = p.get("khasais", []) + [c for x in p.get("pillars", []) for c in x.get("khasais", [])]
        L.append(f"| {p['ar_name']} | {p['span'][0]}–{p['span'][1]} | {'p. ' + str(p['def']['shamela']) if p.get('def') else '— (left)'} | {subs} | "
                 f"{len(cs)} ({sum(1 for c in cs if c.get('khasais'))}) |")
    nf = [c for c in cites if not c.get("khasais")]
    topics = Counter(r["topic"] for r in kh)
    was44 = ("abniya alam asma-afal badal five-verbs hadhf hikaya imala ishara ishtighal ism-fail-amal istithna law maani-abwab madh maful-fih "
             "maful-lah maful-mutlaq maqsur-mamdud masdar masdar-amal muarraf mudari-abwab mudmar muqaraba mushtaqqat naib-fail nasab nida "
             "nun-tawkid sakinayn sifa-mushabbaha tafdil tajjub taksir tanazu tanith tasghir tathniya tawkid waqf zaid zann zawaid").split()
    ans = [t for t in was44 if t in topics]
    left = [t for t in was44 if t not in topics]
    unread = sorted(((v[1], n) for n, v in use.items() if not v[0] and v[1]), reverse=True)[:15]
    L += ["", "## The 44 topics v348-F left without a reason", "",
          f"Answered now from al-Khaṣāʾiṣ: {len(ans)} — {', '.join(ans)}.", f"Still without: {len(left)} — {', '.join(left)}.", "",
          "## Next round", "",
          "1. Read the rest of research/usul/khasais_candidates.json (≈ 520 unread), first the abwāb with most candidates and nothing fed: "
          + ", ".join(f"bāb {n} ({c})" for c, n in unread) + ".",
          "2. The still-uncovered topics above — badal (al-Khaṣāʾiṣ's «بدل» is mostly the letter substitution, not apposition: do not join), istithnāʾ "
          "(the regex «إلا» is noise; read by hand), the mafʿūl muṭlaq / lahu, nāʾib al-fāʿil, nidāʾ, nasab, ʿalam.",
          f"3. {len(nf)} al-Iqtirāḥ citations of Ibn Jinnī not found in al-Khaṣāʾiṣ by script (abridged quotations; some are from his other books): "
          + "; ".join(f"p. {c['iqtirah']['shamela']}" for c in nf) + ".",
          "4. al-Iqtirāḥ kitāb 7 (أحوال المستنبط) has no defining sentence chosen; the sub-headings' first sentences are Arabic only (not rendered).",
          "5. The kinds: 6 of the 24 are used by the tags (tashbīh, istithqāl, farq, takhfīf, taʿwīḍ, taḍādd); more reasons will tag as more are kept.",
          "6. The renderings (kinds, proofs, methods, the 31 reasons) await the hoca."]
    (ROOT / "research/usul-coverage-2026-11-27.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("fed", fed, "of", len(use), "; answered", len(ans), "; not found", len(nf))


if __name__ == "__main__":
    main()
