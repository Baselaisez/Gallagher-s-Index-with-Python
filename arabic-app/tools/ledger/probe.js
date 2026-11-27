// v342-N — the book ledger's probe runner, evaluated INSIDE the page (smoke check and tools/ledger/build_ledger.py's prover).
// A probe: { s: the book's example, w: the word (letters only) or its index, re: a regex the engine's line must match (on the
// letters, harakāt stripped), not: a regex it must not match } — or { js: an expression returning true }.
// Returns [{ ok, got }] in the order given.
(probes) => {
  const H = x => String(x || '').normalize('NFC').replace(/[ً-ْٰـ]/g, '');
  const cache = {};
  return probes.map(p => {
    try {
      if (p.js) { const v = (0, eval)(p.js); return { ok: v === true, got: String(v).slice(0, 300) }; }
      const rows = cache[p.s] || (cache[p.s] = SentenceAnalyzer.analyze(p.s));
      let i = typeof p.w === 'number' ? p.w : rows.findIndex(r => H(r.w) === H(p.w));
      if (i < 0) return { ok: false, got: 'no word ' + p.w + ' in ' + rows.map(r => r.w).join(' ') };
      const ln = H((Murib.line(rows, i) || {}).ar);
      const ok = new RegExp(p.re).test(ln) && !(p.not && new RegExp(p.not).test(ln));
      return { ok, got: ln.slice(0, 300) };
    } catch (e) { return { ok: false, got: 'ERR ' + e.message }; }
  });
}
