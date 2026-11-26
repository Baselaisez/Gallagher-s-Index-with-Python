// v342-A — the other resources' ledger: the probe runner, evaluated INSIDE the built page (by tools/ledger/aux_prove.js and by
// the «v342 — the other resources' ledger …» smoke check). A probe is one of:
//   { s, w, re, not }  — the source's own example s run through SentenceAnalyzer + Murib.line; the line of word w (letters only, or
//                        an index) must match re (on the letters, harakāt stripped) and must not match not;
//   { ilal, out }      — IlalEngine.derive(ilal).out must equal out (both written with the engine's canonical mark order);
//   { js }             — an expression that must evaluate to true;
//   { any: [probes] }  — story sentences (verbatim from the shelf) where the source gives no example: one passing is the proof,
//                        the count k/n is kept in the ledger.
// Returns [{ ok, got }] in the order given.
(probes) => {
  const H = x => String(x || '').normalize('NFC').replace(/[ً-ْٰـ]/g, '').replace(/[أإآٱ]/g, 'ا').replace(/ى/g, 'ي');
  const cache = {};
  const one = p => {
    try {
      if (p.all) { const rs = p.all.map(one); const k = rs.filter(r => r.ok).length; return { ok: k === rs.length, got: k + '/' + rs.length + ' pass; ' + rs.map(r => r.got.slice(0, 120)).join(' ‖ ') }; }
      if (p.any) { const rs = p.any.map(one); const k = rs.filter(r => r.ok).length; return { ok: k > 0, got: k + '/' + rs.length + ' pass; ' + rs.map(r => r.got).join(' ‖ ') }; }
      if (p.js) { const v = (0, eval)(p.js); return { ok: v === true, got: String(v).slice(0, 300) }; }
      if (p.ilal) {
        // the sheets' Ottoman spelling, compared away: ى for a yāʾ, a final ى for the alif, no hamza seat, a fatḥa on the madd alif,
        // the wiqāya alif after a final wāw written or not — the comparison is of the iʿlāl, not of the orthography
        const O = s => String(s || '').normalize('NFC').replace(/[أإ]/g, 'ا').replace(/(.)اَ/g, '$1ا').replace(/َى$/, 'َا').replace(/ى/g, 'ي').replace(/َ(?=ا)/g, '');
        const C = s => IlalEngine.join(IlalEngine.parse(O(s).replace(/وْ?ا$/, 'و').replace(/وْ$/, 'و')));
        const I = s => String(s || '').normalize('NFC').replace(/َى$/, 'َا').replace(/ى/g, 'ي');   // the origin as typed: only its yāʾ is read
        const r = IlalEngine.derive(I(p.ilal)) || {};
        return { ok: C(r.out) === C(p.out), got: String(r.out) + ' ← ' + (r.steps || []).map(x => x.id).join(',') };
      }
      const rows = cache[p.s] || (cache[p.s] = SentenceAnalyzer.analyze(p.s));
      const i = typeof p.w === 'number' ? p.w : rows.findIndex(r => H(r.w) === H(p.w));
      if (i < 0) return { ok: false, got: 'no word ' + p.w + ' in ' + rows.map(r => r.w).join(' ') };
      const ln = H((Murib.line(rows, i) || {}).ar);
      const ok = new RegExp(H(p.re)).test(ln) && !(p.not && new RegExp(H(p.not)).test(ln));
      return { ok, got: ln.slice(0, 300) };
    } catch (e) { return { ok: false, got: 'ERR ' + e.message }; }
  };
  return probes.map(one);
}
