// v352-A — Ibn ʿAqīl's ledger: the probe runner, evaluated INSIDE the built page (by tools/ledger/aqil_prove.js and by the smoke
// check «v352-A — Ibn ʿAqīl's ledger …»). A probe is one of:
//   { s, w, re }   — the book's own example s (as printed: unvowelled) through SentenceAnalyzer + Murib.line; the line of word w
//                    (letters only) must match re (letters, harakāt stripped);
//   { s, any: re } — the bāb's construction named on the example: SOME word's line must match re.
// Returns [{ ok, offered, got }]: offered = the matching line gives the reading beside another («أو» / «وقيل»).
(probes) => {
  const H = x => String(x || '').normalize('NFC').replace(/[ً-ْٰـ]/g, '').replace(/[أإآٱ]/g, 'ا').replace(/ى/g, 'ي').replace(/ة/g, 'ه');
  const cache = {};
  const OFF = /(^|[^ء-ي])(او|وقيل|ويجوز)([^ء-ي]|$)/;
  return probes.map(p => {
    try {
      const rows = cache[p.s] || (cache[p.s] = SentenceAnalyzer.analyze(p.s));
      const lines = rows.map((r, i) => H((Murib.line(rows, i) || {}).ar));
      if (p.any) {
        const re = new RegExp(H(p.any));
        const k = lines.findIndex(l => re.test(l));
        if (k < 0) return { ok: false, offered: false, got: rows.map((r, i) => r.w + ': ' + lines[i].slice(0, 60)).join(' | ').slice(0, 400) };
        return { ok: true, offered: OFF.test(lines[k]), got: rows[k].w + ': ' + lines[k].slice(0, 200) };
      }
      const i = rows.findIndex(r => H(r.w) === H(p.w));
      if (i < 0) return { ok: false, offered: false, got: 'no word ' + p.w + ' in ' + rows.map(r => r.w).join(' ') };
      const ok = new RegExp(H(p.re)).test(lines[i]);
      return { ok, offered: ok && OFF.test(lines[i]), got: lines[i].slice(0, 300) };
    } catch (e) { return { ok: false, offered: false, got: 'ERR ' + e.message }; }
  });
}
