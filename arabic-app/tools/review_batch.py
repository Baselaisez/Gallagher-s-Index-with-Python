#!/usr/bin/env python3
"""review_batch.py — an AI pre-review of every package marked `pending-scholarly-review`, for the human scholar.

It READS the packages and WRITES a report. It never edits content: every finding is a suggestion for the scholar.

    python3 tools/review_batch.py --dry-run                     # build every request, count input tokens (free), plan the budget
    python3 tools/review_batch.py --pilot 3 [--also-medium P]   # a real batch on 3 packages; measured usage and projections
    python3 tools/review_batch.py --all [--budget 190]          # the shelf in priority order, up to the budget
    python3 tools/review_batch.py --collect <report dir>        # resume: poll a submitted batch and write its report

Options: --packages id,id (choose packages; with --pilot it overrides the automatic pick), --effort low|medium|high|
xhigh|max (default high), --max-findings N (per request, default 40), --budget USD (default 190), --no-wait (submit and
exit; --collect later), --out <dir> (default reports/review-<UTC date>).

Model and API: Claude Fable 5.2 through the Message Batches API (50% of standard price: $4 / $20 per MTok in / out).
Thinking is always on for this model, so no `thinking` parameter is sent; depth is set by `output_config.effort`, and
the answer is JSON constrained by `output_config.format`. One request per package, or per chapter when a package is
large (per chapter part when one chapter alone is very large); `custom_id` names the package and chapter, and results
are keyed by it, never by their order.

What a request carries, and nothing more: each token's written word, its lex key, its grammar note ids and its iʿrāb
line in Arabic, English and Turkish (a line used more than once is given once in a table and referred to); the gloss
of every lex key used; each sentence's English and Turkish translation (where a doctrinal misstatement would live);
the plain-language definition of every grammar note the part uses. Bare spellings (derivable from the vowelled word),
segments, parts of speech, lemmas and roots are left out. The system prompt is two cached blocks: the review rubric
with an index of the grammar registry (shared by every request), then the package's provenance paragraph with its
deliberate readings (shared by the requests of one package; cached only when the package has more than one).

Cost estimate: input is counted exactly with count_tokens. Output is estimated per request as thinking plus the
answer, and the answer is bounded by the findings cap: min(cap, input tokens / tokens-per-finding) findings of a fixed
size. The defaults are assumptions until a pilot measures them; a pilot writes `assumptions.json`, which later dry runs
and --all read. Batch caching is best-effort, so the plan prices the cached blocks at the measured (or assumed) share
of cache hits and prints beside it what the run would cost with no cache_control at all (a cache write costs
twice plain input at the 1-hour TTL, so caching pays only above a ~50% hit rate; the pilot measures the real rate).

--all: packages go in priority order — the Level 1–2 stories first, then the other packages from the smallest to the
largest, so the long classical texts come last — and packages are added until the projected cost reaches --budget.
What does not fit is printed as deferred. Packages that already have a report in the output directory (the pilot's)
are not sent again.

Refusals: the Batches API does not accept the server-side `fallbacks` parameter (and the policy floor rules out its
fallback targets). A request that ends with `stop_reason: "refusal"` is recorded with its category in `refused.json`
for a re-run; one that ends at `max_tokens` goes to `truncated.json`. Neither stops the run.

API key: read from QISSA_ANTHROPIC_API_KEY, or from the gitignored arabic-app/.env.local (a line
`QISSA_ANTHROPIC_API_KEY=...`), and passed explicitly to the client. ANTHROPIC_API_KEY is never read (it would also
move Claude Code's own billing), and the key is never printed, logged or written.
"""
import argparse, concurrent.futures as cf, datetime as dt, json, math, os, re, sys, time, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # arabic-app/
MODEL = "claude-fable-5-2"
PRICE = {"in": 4.00, "out": 20.00, "cache_read": 0.10, "cache_write_1h": 8.00, "cache_write_5m": 5.00}   # $/MTok, batch (50%)
MAX_TOKENS = 64000                                    # thinking + the JSON answer; a hard cap on output, billed as used
PKG_CHARS = 150_000                                   # a package whose request text is longer is sent chapter by chapter
CHAPTER_CHARS = 220_000                               # a chapter longer than this is sent in sentence parts
ASSUME = {"thinking": 8000, "tok_per_finding": 220, "finding_every": 1500, "summary": 500, "cache_hit": 0.5}
ISSUE_TYPES = ["irab_ar", "irab_en", "irab_tr", "tashkeel", "lex_gloss", "grammar_id", "doctrinal_sensitivity"]
SEVERITIES = ["critical", "major", "minor"]
FIELDS = ["surface", "irab.ar", "irab.en", "irab.tr", "lex", "gloss", "grammar", "translation.en", "translation.tr", "other"]
N = lambda s: unicodedata.normalize("NFC", s or "")


# ---------------------------------------------------------------- the key
def api_key():
    k = os.environ.get("QISSA_ANTHROPIC_API_KEY", "").strip()
    if not k:
        f = ROOT / ".env.local"
        if f.is_file():
            for line in f.read_text(encoding="utf-8").splitlines():
                m = re.match(r"\s*(?:export\s+)?QISSA_ANTHROPIC_API_KEY\s*=\s*(.*)$", line)
                if m: k = m.group(1).strip().strip("'\"")
    if not k:
        sys.exit("QISSA_ANTHROPIC_API_KEY is not set (environment or arabic-app/.env.local). Stopping: no request was made.")
    return k


def client():
    import anthropic
    os.environ.pop("ANTHROPIC_AUTH_TOKEN", None)      # only the key given here authenticates this process
    return anthropic.Anthropic(api_key=api_key(), max_retries=8)


# ---------------------------------------------------------------- the content
def pending_packages():
    out = []
    for m in sorted(list((ROOT / "content/samples").glob("*/manifest.json")) + list((ROOT / "content/user-uploads").glob("*/manifest.json"))):
        man = json.loads(m.read_text(encoding="utf-8"))
        if ((man.get("attribution") or {}).get("reviewStatus") or man.get("reviewStatus")) == "pending-scholarly-review":
            out.append(m.parent)
    return out


def irab_tr_memory():
    p = ROOT / "content/i18n/irab-tr.json"
    return json.loads(p.read_text(encoding="utf-8")).get("entries", {}) if p.is_file() else {}


def notes():
    out = {}
    for f in sorted((ROOT / "content/grammar").glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        out[d["id"]] = d
    return out


def one_line(s):
    return re.sub(r"\s+", " ", N(s)).strip()


def irab_triple(t, trm):
    ir = t.get("irab") or {}
    tr = ir.get("tr") or trm.get(ir.get("en") or "", "")      # the Turkish the reader shows (the builder merges the same memory)
    return f"AR {one_line(ir.get('ar'))} | EN {one_line(ir.get('en'))} | TR {one_line(tr)}"


def unit_text(items, trm):
    """The sentences of one request; an iʿrāb line used more than once is written once in a table (L1, L2 …)."""
    triples = [irab_triple(t, trm) for _, s in items for t in s.get("tokens") or []]
    count = {}
    for x in triples: count[x] = count.get(x, 0) + 1
    table, ids = [], {}
    for x in triples:
        if count[x] > 1 and x not in ids:
            ids[x] = f"L{len(ids) + 1}"; table.append(f"{ids[x]}\t{x}")
    rows = []
    for c, s in items:
        tr = s.get("translation") or {}
        rows.append(f"@{c}:{s['id']}\tEN: {one_line(tr.get('en'))}\tTR: {one_line(tr.get('tr'))}")
        for i, t in enumerate(s.get("tokens") or []):
            x = irab_triple(t, trm)
            rows.append(f"{i}\t{N((t.get('surface') or {}).get('full'))}\t{t.get('lex')}\t{','.join(t.get('grammar') or [])}\t" + ("=" + ids[x] if x in ids else x))
    return ("REPEATED IʿRĀB LINES (a token line ending in =L<n> carries line L<n>):\n" + "\n".join(table) + "\n\n" if table else "") + "\n".join(rows)


def build_requests(pkgs, trm, reg):
    """Each request: custom_id, package, level, unit, provenance, text, location index {ch:sid:i -> word}."""
    reqs = []
    for pkg in pkgs:
        man = json.loads((pkg / "manifest.json").read_text(encoding="utf-8"))
        gl = json.loads((pkg / "glossary.json").read_text(encoding="utf-8")).get("entries", {}) if (pkg / "glossary.json").is_file() else {}
        prov = (f"PACKAGE {man['id']} — {one_line((man.get('title') or {}).get('en'))} (level {man.get('level')})\n"
                f"PROVENANCE AND DELIBERATE READINGS (do not report these as errors):\n{one_line((man.get('attribution') or {}).get('en'))}")
        titles = {int(x.get("n", k + 1)): one_line((x.get("title") or {}).get("en")) for k, x in enumerate(man.get("chapters") or [])}
        chs = []
        for f in sorted((pkg / "chapters").glob("*.json"), key=lambda p: int(p.stem)):
            d = json.loads(f.read_text(encoding="utf-8"))
            chs.append((int(d.get("chapter", f.stem)), d.get("sentences") or []))
        units, whole = [], [(c, s) for c, ss in chs for s in ss]
        if len(unit_text(whole, trm)) <= PKG_CHARS:
            units.append(("", whole))
        else:
            for c, ss in chs:
                items = [(c, s) for s in ss]
                if len(unit_text(items, trm)) <= CHAPTER_CHARS:
                    units.append((f"c{c}", items)); continue
                part, k = [], 1
                for it in items:
                    if part and len(unit_text(part + [it], trm)) > CHAPTER_CHARS:
                        units.append((f"c{c}-p{k}", part)); part, k = [], k + 1
                    part.append(it)
                if part: units.append((f"c{c}-p{k}", part))
        for label, items in units:
            cid = (man["id"] + ("--" + label if label else ""))[:64]
            toks = [t for _, s in items for t in s.get("tokens") or []]
            keys = sorted({t.get("lex") for t in toks} - {None})
            gids = sorted({g for t in toks for g in t.get("grammar") or []})
            gloss = "\n".join(f"{k} | {one_line((gl.get(k) or {}).get('gloss', {}).get('en'))} | {one_line((gl.get(k) or {}).get('gloss', {}).get('tr'))}" for k in keys if k in gl)
            used = "\n".join(f"{g} | {one_line(((reg.get(g) or {}).get('plain') or {}).get('en'))}" for g in gids if g in reg)
            text = ("CHAPTERS: " + "; ".join(f"{c} {titles.get(c, '')}" for c in sorted({c for c, _ in items})) + "\n\n"
                    + "GLOSSARY (lex key | gloss EN | gloss TR):\n" + gloss + "\n\n"
                    + "GRAMMAR NOTES USED HERE (id | plain EN):\n" + used + "\n\n"
                    + "SENTENCES (@chapter:sentence with its EN / TR translation; then one line per token: index, word, lex key, grammar note ids, iʿrāb AR | EN | TR or =L<n>):\n"
                    + unit_text(items, trm))
            loc = {f"{c}:{s['id']}:{i}": N((t.get("surface") or {}).get("full")) for c, s in items for i, t in enumerate(s.get("tokens") or [])}
            reqs.append({"custom_id": cid, "package": man["id"], "level": man.get("level") or 9, "unit": label or "all",
                         "prov": prov, "text": text, "loc": loc})
    ids = [r["custom_id"] for r in reqs]
    assert len(ids) == len(set(ids)), "custom_id collision"
    assert all(re.fullmatch(r"[A-Za-z0-9_-]{1,64}", i) for i in ids), "custom_id outside [A-Za-z0-9_-]{1,64}"
    per = {}
    for r in reqs: per[r["package"]] = per.get(r["package"], 0) + 1
    for r in reqs: r["shared_prov"] = per[r["package"]] > 1
    return reqs


# ---------------------------------------------------------------- the prompt
RUBRIC = """You are reviewing lessons of Qissa, an app that teaches Classical Arabic through classical texts and original graded stories. Every word carries an iʿrāb line in Arabic, with an English and a Turkish rendering, a glossary key, and the ids of the grammar notes it teaches. The texts are classical Islamic works (grammar, ṣarf, creed, fiqh, prophetic stories). A human scholar will sign each package off; your review is a pre-review that tells the scholar where to look first. You change nothing yourself.

Report only what a careful teacher of Arabic grammar would correct:
- irab_ar: the Arabic iʿrāb line is wrong — the office (fāʿil, mafʿūl bihi, khabar …), the case, the sign of the case, the governor, or a verb's tense, mood or build (bināʾ) — or it does not fit the ending written on the word.
- irab_en / irab_tr: the English or Turkish line does not say what the Arabic line says, or is wrong in itself.
- tashkeel: a vowel, sukūn, shadda or tanwīn on the word is wrong (including a case ending that contradicts the iʿrāb). Do not ask for marks the style leaves out.
- lex_gloss: the lex key points to the wrong word for this place, or its gloss is wrong for this use.
- grammar_id: a listed grammar note does not apply to the word, or one clearly central note is missing. Use only ids from the registry index below.
- doctrinal_sensitivity: a translation or iʿrāb line could misstate a point of creed or law, or misquote the Qurʾān or a ḥadīth. Flag it for the scholar; do not rule on the doctrine yourself. "suggested" may be empty here.

Do not report: style preferences, alternative wordings that are equally correct, the transcription of the classical text itself (only its vowelling), or anything the PROVENANCE AND DELIBERATE READINGS paragraph explains. Where the grammarians differ and the line follows a recognised view, leave it. A quoted example word («…») is cited for its wording (ḥikāya); judge its line as a cited word.

Severity: critical — a learner would absorb a wrong rule or a wrong Arabic form (wrong case or office, a vowel that changes the word, a doctrinal misstatement); major — the English or Turkish misstates the Arabic, a wrong gloss, a wrong grammar note; minor — an imprecise or incomplete line that is not wrong.

Location: give the chapter number, the sentence id and the token index exactly as written in the input, and copy the word into "surface". Use token -1 for a problem in a sentence's translation. "current" quotes the value as it stands (shorten long lines with …); "suggested" gives the corrected value in the same language as the field. Give each reason in English (reason_en) and Turkish (reason_tr), one or two short sentences each.

List at most {max_findings} findings, the most severe first. If you found more, put the number left out in more_findings_not_listed. Write summary_en and summary_tr for the scholar: two to four sentences on the overall quality of this part and the kinds of problems seen, so a reader who has not seen the text understands it.

GRAMMAR REGISTRY INDEX (id | group | title):
"""


def system_main(reg, max_findings):
    idx = "\n".join(f"{k} | {d.get('group')} | {one_line((d.get('title') or {}).get('en'))}" for k, d in sorted(reg.items()))
    return {"type": "text", "text": RUBRIC.replace("{max_findings}", str(max_findings)) + idx, "cache_control": {"type": "ephemeral", "ttl": "1h"}}


def system_blocks(req, main):
    prov = {"type": "text", "text": req["prov"]}
    if req["shared_prov"]: prov["cache_control"] = {"type": "ephemeral", "ttl": "1h"}
    return [main, prov]


SCHEMA = {
    "type": "object",
    "properties": {
        "summary_en": {"type": "string"},
        "summary_tr": {"type": "string"},
        "overall": {"type": "string", "enum": ["clean", "minor_issues", "needs_attention", "serious_problems"]},
        "more_findings_not_listed": {"type": "integer"},
        "findings": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "chapter": {"type": "integer"}, "sentence": {"type": "string"}, "token": {"type": "integer"},
                "surface": {"type": "string"},
                "issue_type": {"type": "string", "enum": ISSUE_TYPES},
                "severity": {"type": "string", "enum": SEVERITIES},
                "field": {"type": "string", "enum": FIELDS},
                "current": {"type": "string"}, "suggested": {"type": "string"},
                "reason_en": {"type": "string"}, "reason_tr": {"type": "string"},
            },
            "required": ["chapter", "sentence", "token", "surface", "issue_type", "severity", "field", "current", "suggested", "reason_en", "reason_tr"],
            "additionalProperties": False}},
    },
    "required": ["summary_en", "summary_tr", "overall", "more_findings_not_listed", "findings"],
    "additionalProperties": False,
}


def params(req, main, effort):
    return {"model": MODEL, "max_tokens": MAX_TOKENS, "system": system_blocks(req, main),
            "output_config": {"effort": effort, "format": {"type": "json_schema", "schema": SCHEMA}},
            "messages": [{"role": "user", "content": "Review this part of the shelf.\n\n" + req["text"]}]}


# ---------------------------------------------------------------- counting and the cost model
def count_all(c, reqs, main, effort):
    def one(r):
        p = params(r, main, effort)
        return r["custom_id"], c.messages.count_tokens(model=MODEL, system=p["system"], messages=p["messages"], output_config=p["output_config"]).input_tokens
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        return dict(ex.map(one, reqs))


def block_tokens(c, reqs, main, effort):
    """Tokens of the shared main block, and of each package's provenance block (count with and without it)."""
    probe = {"prov": "", "shared_prov": False, "text": "."}
    of = {"effort": effort, "format": {"type": "json_schema", "schema": SCHEMA}}
    msgs = params(probe, main, effort)["messages"]
    bare = c.messages.count_tokens(model=MODEL, messages=msgs, output_config=of).input_tokens
    with_main = c.messages.count_tokens(model=MODEL, system=[main], messages=msgs, output_config=of).input_tokens
    prov = {}
    for r in reqs:
        if r["package"] in prov: continue
        prov[r["package"]] = c.messages.count_tokens(model=MODEL, system=[main, {"type": "text", "text": r["prov"]}], messages=msgs, output_config=of).input_tokens - with_main
    return with_main - bare, prov


def out_tokens(user, A, cap):
    findings = min(cap, user / A["finding_every"])
    return A["thinking"] + A["summary"] + findings * A["tok_per_finding"], A["thinking"] + A["summary"] + cap * A["tok_per_finding"]


def plan_cost(reqs, counts, main_t, prov_t, A, cap, effort=None):
    """Per package: expected cost (cache hits at A['cache_hit']), no-cache ceiling, and output at the findings cap."""
    h = A["cache_hit"]
    blended = h * PRICE["cache_read"] + (1 - h) * PRICE["cache_write_1h"]   # a cached block is either read or written
    first_main = True
    per = {}
    for r in reqs:
        pk = r["package"]; p = per.setdefault(pk, {"requests": 0, "user": 0, "exp": 0.0, "nocache": 0.0, "capped": 0.0, "level": r["level"]})
        pv = prov_t[pk]; user = max(0, counts[r["custom_id"]] - main_t - pv)
        o, ocap = out_tokens(user, A, cap)
        mainc = (PRICE["cache_write_1h"] if first_main else blended) * main_t; first_main = False
        provc = (blended if r["shared_prov"] else PRICE["in"]) * pv
        p["requests"] += 1; p["user"] += user
        p["exp"] += (user * PRICE["in"] + mainc + provc + o * PRICE["out"]) / 1e6
        p["nocache"] += ((user + main_t + pv) * PRICE["in"] + o * PRICE["out"]) / 1e6
        p["capped"] += (user * PRICE["in"] + mainc + provc + ocap * PRICE["out"]) / 1e6
    return per


def priority(per):
    """Level 1–2 stories first (smallest first), then every other package from the smallest to the largest."""
    return sorted(per, key=lambda k: (0 if per[k]["level"] <= 2 else 1, per[k]["user"]))


def assumptions(effort, override):
    A = dict(ASSUME); src = "defaults (not yet measured)"
    files = sorted(ROOT.glob("reports/review-*/assumptions.json"))
    if files:
        m = json.loads(files[-1].read_text(encoding="utf-8")).get(effort)
        if m: A.update(m); src = f"measured by the pilot ({files[-1].parent.name})"
    for k, v in override.items():
        if v is not None: A[k] = v; src += f"; {k} overridden"
    return A, src


# ---------------------------------------------------------------- batch
def submit(c, reqs, main, efforts, outdir, mode):
    from anthropic.types.messages.batch_create_params import Request
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    batch = c.messages.batches.create(requests=[Request(custom_id=r["custom_id"], params=MessageCreateParamsNonStreaming(**params(r, main, efforts[r["custom_id"]]))) for r in reqs])
    state = {"batch_id": batch.id, "mode": mode, "model": MODEL, "created": dt.datetime.now(dt.timezone.utc).isoformat(),
             "requests": {r["custom_id"]: {"package": r["package"], "report_as": r.get("report_as", r["package"]), "unit": r["unit"],
                                           "effort": efforts[r["custom_id"]], "loc": r["loc"], "pair": r.get("pair")} for r in reqs}}
    (outdir / "batch.json").write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"submitted batch {batch.id}: {len(reqs)} requests ({mode}); state in {outdir / 'batch.json'}")
    return state


def wait(c, batch_id, every=60):
    while True:
        b = c.messages.batches.retrieve(batch_id)
        rc = b.request_counts
        print(f"{dt.datetime.now(dt.timezone.utc):%H:%M:%S} {b.processing_status}: processing {rc.processing}, succeeded {rc.succeeded}, errored {rc.errored}, expired {rc.expired}", flush=True)
        if b.processing_status == "ended": return b
        time.sleep(every)


def usage_cost(u):
    cc = getattr(u, "cache_creation", None)
    w1 = getattr(cc, "ephemeral_1h_input_tokens", None) if cc else None
    w5 = getattr(cc, "ephemeral_5m_input_tokens", None) if cc else None
    if w1 is None and w5 is None: w1, w5 = (u.cache_creation_input_tokens or 0), 0
    return (u.input_tokens * PRICE["in"] + (u.cache_read_input_tokens or 0) * PRICE["cache_read"] + (w1 or 0) * PRICE["cache_write_1h"]
            + (w5 or 0) * PRICE["cache_write_5m"] + u.output_tokens * PRICE["out"]) / 1e6


def collect(c, state, outdir):
    reqs = state["requests"]
    got, refused, truncated, failed, usage = {}, [], [], [], {}
    for res in c.messages.batches.results(state["batch_id"]):
        cid = res.custom_id
        if cid not in reqs: continue
        r = res.result
        if r.type != "succeeded":
            failed.append({"custom_id": cid, "result": r.type, "error": getattr(getattr(r, "error", None), "type", None)}); continue
        msg = r.message; u = msg.usage
        thinking = getattr(getattr(u, "output_tokens_details", None), "thinking_tokens", None)
        usage[cid] = {"effort": reqs[cid]["effort"], "input": u.input_tokens, "cache_read": u.cache_read_input_tokens or 0,
                      "cache_write": u.cache_creation_input_tokens or 0, "output": u.output_tokens, "thinking": thinking,
                      "answer": (u.output_tokens - thinking) if thinking is not None else None, "stop_reason": msg.stop_reason, "cost_usd": usage_cost(u)}
        if msg.stop_reason == "refusal":
            sd = getattr(msg, "stop_details", None)
            refused.append({"custom_id": cid, "category": getattr(sd, "category", None), "explanation": getattr(sd, "explanation", None)}); continue
        if msg.stop_reason == "max_tokens":
            truncated.append({"custom_id": cid, "output_tokens": u.output_tokens}); continue
        text = next((b.text for b in msg.content if b.type == "text"), "")
        try:
            got[cid] = json.loads(text); usage[cid]["findings"] = len(got[cid].get("findings") or [])
        except json.JSONDecodeError as e:
            failed.append({"custom_id": cid, "result": "unparsable", "error": str(e)[:200]})
    write_report(state, got, refused, truncated, failed, usage, outdir)
    return got, usage


# ---------------------------------------------------------------- report
SEV_RANK = {s: i for i, s in enumerate(SEVERITIES)}


def findings_of(cid, d, reqs):
    out = []
    for f in d.get("findings") or []:
        key = f"{f.get('chapter')}:{f.get('sentence')}:{f.get('token')}"
        at = reqs[cid]["loc"].get(key)
        ok = (f.get("token") == -1 and any(k.startswith(f"{f.get('chapter')}:{f.get('sentence')}:") for k in reqs[cid]["loc"])) or (at is not None and N(at) == N(f.get("surface")))
        out.append(dict(f, package=reqs[cid]["report_as"], custom_id=cid, location_ok=ok))
    return out


def write_report(state, got, refused, truncated, failed, usage, outdir):
    reqs = state["requests"]
    by = {}
    for cid, meta in reqs.items(): by.setdefault(meta["report_as"], []).append(cid)
    allf = []
    for name, cids in sorted(by.items()):
        parts, fs = [], []
        for cid in sorted(cids):
            d = got.get(cid)
            if not d: parts.append({"custom_id": cid, "unit": reqs[cid]["unit"], "status": "missing"}); continue
            parts.append({"custom_id": cid, "unit": reqs[cid]["unit"], "overall": d.get("overall"), "summary_en": d.get("summary_en"),
                          "summary_tr": d.get("summary_tr"), "more_findings_not_listed": d.get("more_findings_not_listed", 0)})
            fs += findings_of(cid, d, reqs)
        fs.sort(key=lambda f: (SEV_RANK.get(f.get("severity"), 9), f.get("chapter") or 0, f.get("sentence") or "", f.get("token") or 0))
        allf += fs
        (outdir / f"{name}.json").write_text(json.dumps({"package": name, "model": state["model"], "effort": reqs[cids[0]]["effort"], "batch_id": state["batch_id"],
                                                         "cost_usd": round(sum(usage[c]["cost_usd"] for c in cids if c in usage), 4), "parts": parts, "findings": fs},
                                                        ensure_ascii=False, indent=1), encoding="utf-8")
    for nm, obj in (("refused", refused), ("truncated", truncated), ("failed", failed), ("usage", usage)):
        (outdir / f"{nm}.json").write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    write_summary(state, by, got, allf, refused, truncated, failed, usage, outdir)


def md(s):
    return one_line(str(s)).replace("|", "\\|")


def write_summary(state, by, got, findings, refused, truncated, failed, usage, outdir):
    sev = {s: sum(1 for f in findings if f.get("severity") == s) for s in SEVERITIES}
    cost = sum(u["cost_usd"] for u in usage.values())
    L = [f"# Qissa — yapay zekâ ön incelemesi / AI pre-review ({state['created'][:10]})", "",
         "**TR:** Bu rapor, «pending-scholarly-review» durumundaki paketlerin yapay zekâ ile yapılmış bir ön incelemesidir. "
         "İçerikte hiçbir şey değiştirilmedi; her bulgu, hocanın karar vereceği bir öneridir.",
         "**EN:** This report is an AI pre-review of the packages marked «pending-scholarly-review». "
         "Nothing in the content was changed; every finding is a suggestion for the scholar to decide on.", "",
         f"Model `{state['model']}` · batch `{state['batch_id']}` · {len(state['requests'])} requests · cost / maliyet ${cost:.2f}", "",
         "| Önem / Severity | Sayı / Count |", "|---|---|"] + [f"| {s} | {sev[s]} |" for s in SEVERITIES] + [""]
    if refused or truncated or failed:
        L += ["## Yeniden çalıştırılacaklar / To re-run", ""]
        L += [f"- refused / reddedildi: `{r['custom_id']}` ({r.get('category')})" for r in refused]
        L += [f"- max_tokens / kesildi: `{r['custom_id']}`" for r in truncated]
        L += [f"- {r['result']}: `{r['custom_id']}`" for r in failed] + [""]
    L += ["## Paketler / Packages", ""]
    for name, cids in sorted(by.items()):
        n = [f for f in findings if f["package"] == name]
        L += [f"### {name} (" + ", ".join(f"{s} {sum(1 for f in n if f['severity'] == s)}" for s in SEVERITIES) + ")", ""]
        for cid in sorted(cids):
            d = got.get(cid)
            if not d: L += [f"- `{cid}`: sonuç yok / no result"]; continue
            more = d.get("more_findings_not_listed") or 0
            L += [f"- `{cid}` — **{d.get('overall')}**" + (f" (+{more} listelenmedi / not listed)" if more else ""),
                  f"  - TR: {md(d.get('summary_tr'))}", f"  - EN: {md(d.get('summary_en'))}"]
        L += [""]
    for s in SEVERITIES:
        rows = [f for f in findings if f.get("severity") == s]
        if not rows: continue
        L += [f"## {s} ({len(rows)})", "",
              "| Paket / Package | Yer / Location | Tür / Type | Alan / Field | Şimdi / Current | Öneri / Suggested | Gerekçe (TR) | Reason (EN) |",
              "|---|---|---|---|---|---|---|---|"]
        for f in rows:
            loc = f"{f['chapter']}:{f['sentence']}:{f['token']} {f.get('surface', '')}" + ("" if f.get("location_ok") else " ⚠")
            L.append(f"| {f['package']} | {md(loc)} | {f['issue_type']} | {f['field']} | {md(f['current'])} | {md(f['suggested'])} | {md(f['reason_tr'])} | {md(f['reason_en'])} |")
        L += [""]
    L += ["⚠ = konum girdiyle eşleşmedi, elle doğrulayın / the location did not match the input; check it by hand.", ""]
    (outdir / "SUMMARY.md").write_text("\n".join(L), encoding="utf-8")
    print(f"report: {outdir}  ({sum(sev.values())} findings: " + ", ".join(f"{s} {sev[s]}" for s in SEVERITIES) + f"; cost ${cost:.2f})")


# ---------------------------------------------------------------- pilot measurement
def measure(usage, effort, user_by_cid):
    rows = [(cid, u) for cid, u in usage.items() if u["effort"] == effort and u.get("thinking") is not None and "findings" in u]
    if not rows: return None
    th = sum(u["thinking"] for _, u in rows) / len(rows)
    fnd = sum(u["findings"] for _, u in rows); ans = sum(u["answer"] for _, u in rows); usr = sum(user_by_cid.get(cid, 0) for cid, _ in rows)
    cr = sum(u["cache_read"] for _, u in rows); cw = sum(u["cache_write"] for _, u in rows)
    return {"thinking": round(th), "summary": 0, "tok_per_finding": round(ans / max(1, fnd)), "finding_every": round(usr / max(1, fnd)),
            "cache_hit": round(cr / (cr + cw), 3) if cr + cw else ASSUME["cache_hit"], "requests": len(rows)}


def compare(got, reqs, outdir, k=3):
    """Side by side: the same package at high and at medium effort."""
    pairs = [(cid, reqs[cid]["pair"]) for cid in reqs if reqs[cid].get("pair")]
    hi = [f for m, h in pairs for f in findings_of(h, got.get(h) or {}, reqs)]
    lo = [f for m, h in pairs for f in findings_of(m, got.get(m) or {}, reqs)]
    key = lambda f: (f["chapter"], f["sentence"], f["token"], f["field"])
    lo_by = {key(f): f for f in lo}
    rank = lambda f: SEV_RANK.get(f["severity"], 9)
    both = sorted([f for f in hi if key(f) in lo_by], key=rank)[:k]
    rows = [(f, lo_by[key(f)]) for f in both]
    rest_hi = sorted([f for f in hi if key(f) not in lo_by], key=rank)
    rest_lo = sorted([f for f in lo if key(f) not in {key(x) for x in hi}], key=rank)
    while len(rows) < k and (rest_hi or rest_lo):
        rows.append((rest_hi.pop(0) if rest_hi else None, rest_lo.pop(0) if rest_lo else None))
    cell = lambda f: "—" if not f else f"{f['severity']} {f['issue_type']} @{f['chapter']}:{f['sentence']}:{f['token']} {f.get('surface','')}: «{md(f['current'])[:90]}» → «{md(f['suggested'])[:90]}» — {md(f['reason_en'])[:160]}"
    L = [f"# high vs medium — {len(hi)} findings at high, {len(lo)} at medium, {len({key(f) for f in hi} & {key(f) for f in lo})} at the same place", "",
         "| high | medium |", "|---|---|"] + [f"| {cell(a)} | {cell(b)} |" for a, b in rows]
    (outdir / "compare-high-medium.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


# ---------------------------------------------------------------- main
def pick_pilot(per, n):
    ranked = sorted(per, key=lambda k: per[k]["user"])
    if len(ranked) <= n: return ranked
    # spread across the size range, skewed upward: most of the shelf's tokens are in the long classical texts
    qs = [0.2, 0.55, 0.85] if n == 3 else [(k + 1) / (n + 1) for k in range(n)]
    return list(dict.fromkeys(ranked[min(len(ranked) - 1, round((len(ranked) - 1) * q))] for q in qs))


def print_plan(per, budget, label):
    order = priority(per); total = 0.0; take, defer = [], []
    for pk in order:
        if total + per[pk]["exp"] <= budget: take.append(pk); total += per[pk]["exp"]
        else: defer.append(pk)
    print(f"{label}: {len(take)} packages fit ${budget:.0f} (expected ${total:.2f}, ceiling with output at the findings cap "
          f"${sum(per[p]['capped'] for p in take):.2f}, without caching ${sum(per[p]['nocache'] for p in take):.2f})")
    if defer: print("  deferred (in order): " + ", ".join(f"{p} ${per[p]['exp']:.2f}" for p in defer))
    return take, defer


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--pilot", type=int); g.add_argument("--all", action="store_true")
    g.add_argument("--collect")
    ap.add_argument("--packages"); ap.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--also-medium", help="pilot: send this package a second time at effort medium, for comparison")
    ap.add_argument("--max-findings", type=int, default=40); ap.add_argument("--budget", type=float, default=190.0)
    ap.add_argument("--no-wait", action="store_true"); ap.add_argument("--out")
    for k in ASSUME: ap.add_argument("--assume-" + k.replace("_", "-"), type=float, default=None)
    a = ap.parse_args()
    c = client()
    if a.collect:
        outdir = Path(a.collect); state = json.loads((outdir / "batch.json").read_text(encoding="utf-8"))
        wait(c, state["batch_id"]); collect(c, state, outdir); return
    outdir = Path(a.out) if a.out else ROOT / "reports" / f"review-{dt.datetime.now(dt.timezone.utc):%Y-%m-%d}"
    outdir.mkdir(parents=True, exist_ok=True)
    pkgs = pending_packages()
    if a.packages and not a.pilot:
        want = set(a.packages.split(",")); pkgs = [p for p in pkgs if p.name in want]
        if want - {p.name for p in pkgs}: sys.exit("not pending or not found: " + ", ".join(sorted(want - {p.name for p in pkgs})))
    reg = notes(); trm = irab_tr_memory()
    reqs = build_requests(pkgs, trm, reg)
    main_block = system_main(reg, a.max_findings)
    override = {k: getattr(a, "assume_" + k) for k in ASSUME}
    print(f"{len(pkgs)} packages pending review → {len(reqs)} requests ({sum(1 for r in reqs if r['unit'] == 'all')} whole packages, "
          f"{sum(1 for r in reqs if r['unit'] != 'all')} chapter or chapter-part requests)")
    main_t, prov_t = block_tokens(c, reqs, main_block, a.effort)
    counts = count_all(c, reqs, main_block, a.effort)
    user = {r["custom_id"]: max(0, counts[r["custom_id"]] - main_t - prov_t[r["package"]]) for r in reqs}
    if a.dry_run:
        A, src = assumptions(a.effort, override)
        per = plan_cost(reqs, counts, main_t, prov_t, A, a.max_findings)
        tot_user = sum(user.values()); big = max(counts.values())
        print(f"shared main block (rubric + registry index of {len(reg)} notes): {main_t:,} tokens; provenance blocks: "
              f"{sum(prov_t.values()):,} tokens over {len(prov_t)} packages (cached where a package has several requests)")
        print(f"input outside the cached blocks: {tot_user:,} tokens; largest request {big:,} tokens in all")
        print(f"output model ({src}): thinking {A['thinking']:.0f} + summary {A['summary']:.0f} + min({a.max_findings}, input / {A['finding_every']:.0f}) "
              f"findings × {A['tok_per_finding']:.0f} tokens per request; cache hits assumed {A['cache_hit']:.0%}")
        exp = sum(p["exp"] for p in per.values()); cap = sum(p["capped"] for p in per.values()); nc = sum(p["nocache"] for p in per.values())
        print(f"full run, effort {a.effort}: expected ${exp:.2f}; with every request at the findings cap ${cap:.2f}; without prompt caching ${nc:.2f}")
        print_plan(per, a.budget, f"--all --budget {a.budget:.0f}")
        pil = pick_pilot(per, 3)
        print(f"default --pilot 3: {', '.join(pil)} — {sum(per[p]['requests'] for p in pil)} requests, expected ${sum(per[p]['exp'] for p in pil):.2f}")
        (outdir / "dry-run.json").write_text(json.dumps({"effort": a.effort, "main_tokens": main_t, "prov_tokens": prov_t, "counts": counts,
                                                         "assumptions": A, "assumption_source": src, "per_package": per}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"written: {outdir / 'dry-run.json'}")
        return
    efforts = {r["custom_id"]: a.effort for r in reqs}
    A, src = assumptions(a.effort, override)
    per = plan_cost(reqs, counts, main_t, prov_t, A, a.max_findings)
    if a.pilot:
        names = a.packages.split(",") if a.packages else pick_pilot(per, a.pilot)
        sel = [r for r in reqs if r["package"] in names]
        if a.also_medium:
            for r in [r for r in reqs if r["package"] == a.also_medium]:
                m = dict(r, custom_id=(r["custom_id"] + "--med")[:64], report_as=r["package"] + "@medium", pair=r["custom_id"])
                sel.append(m); efforts[m["custom_id"]] = "medium"; counts[m["custom_id"]] = counts[r["custom_id"]]; user[m["custom_id"]] = user[r["custom_id"]]
        print("pilot packages: " + ", ".join(names) + (f"; {a.also_medium} also at medium" if a.also_medium else ""))
        state = submit(c, sel, main_block, efforts, outdir, "pilot")
        if a.no_wait: return
        wait(c, state["batch_id"]); got, usage = collect(c, state, outdir)
        print("\nper request: custom_id | effort | input | cache read | cache write | output = thinking + answer | findings | cost")
        for cid, u in sorted(usage.items()):
            print(f"  {cid} | {u['effort']} | {u['input']:,} | {u['cache_read']:,} | {u['cache_write']:,} | {u['output']:,} = {u['thinking']} + {u['answer']} | {u.get('findings', '-')} | ${u['cost_usd']:.3f}")
        meas = {}
        for eff in ("high", "medium"):
            m = measure(usage, eff, user)
            if m: meas[eff] = m
        (outdir / "assumptions.json").write_text(json.dumps(meas, indent=1), encoding="utf-8")
        for eff, m in meas.items():
            print(f"measured at {eff}: thinking {m['thinking']:,}/request, {m['tok_per_finding']} answer tokens per finding, one finding per {m['finding_every']:,} input tokens, cache hits {m['cache_hit']:.0%} ({m['requests']} requests)")
            pe = plan_cost(reqs, counts, main_t, prov_t, dict(ASSUME, **m), a.max_findings)
            print(f"  projected full run at {eff}: expected ${sum(p['exp'] for p in pe.values()):.2f}, at the findings cap ${sum(p['capped'] for p in pe.values()):.2f}, without caching ${sum(p['nocache'] for p in pe.values()):.2f}")
            print_plan(pe, a.budget, f"  --all --effort {eff} --budget {a.budget:.0f}")
        if a.also_medium: compare(got, state["requests"], outdir)
        return
    # --all: priority order up to the budget; packages already reported in this directory are not sent again
    done = {p.stem for p in outdir.glob("*.json") if p.stem not in ("batch", "dry-run", "assumptions", "refused", "truncated", "failed", "usage") and "@" not in p.stem}
    per = {k: v for k, v in per.items() if k not in done}
    print(f"cost model: {src}" + (f"; already reviewed here, skipped: {', '.join(sorted(done))}" if done else ""))
    take, defer = print_plan(per, a.budget, f"--all --budget {a.budget:.0f}")
    sel = [r for pk in take for r in reqs if r["package"] == pk]     # grouped by package, in priority order, for cache reuse
    if not sel: sys.exit("nothing fits the budget")
    state = submit(c, sel, main_block, efforts, outdir, "all")
    (outdir / "deferred.json").write_text(json.dumps(defer, indent=1), encoding="utf-8")
    if a.no_wait: return
    wait(c, state["batch_id"]); collect(c, state, outdir)


if __name__ == "__main__":
    main()
