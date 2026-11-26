// v342-S — the ṣarf ledger's probes, run INSIDE the page (the smoke check and tools/ledger/sarf_probe_run.js both pass this
// source to page.evaluate). A probe runs a book's own words through an engine and answers {ok, got}:
//   cells {root, form, bab, w}   the word is a cell the engine builds for that root / form / bāb (sarfDerive + its alternatives,
//                                the passive by sjMajhul, the emphatic by TawkidEngine)
//   ilal  {asl, w}               IlalEngine.derive(aṣl) spells the book's word
//   kept  {asl, gate}            the book's word comes out unchanged, the named gate blocking (ilalAslRead)
//   isht  {w, root, pat}         IshtiqaqEngine.read0 reads the word as that root on that pattern (a derived noun built by rule)
//   js    {expr, want}           an expression whose String() is want
// `raw: true` compares the bare letters only (the uncollated matn prints few vowels).
module.exports = `(() => {
  const NFC = s => String(s == null ? '' : s).normalize('NFC');
  const W = s => NFC(s).replace(/\\u0640/g, '').replace(/[ٱأإ]/g, 'ا').replace(/آ/g, 'ا').replace(/ٰ/g, '').replace(/[ًٌٍْ]/g, '')
    .replace(/ى(?=[\\u064b-\\u0652]*(?:$|\\s))/g, 'ي').replace(/^ا[َُِ]/, 'ا').replace(/(?<=.)ا[َ]/g, 'ا').replace(/[َ](?=ا)/g, '').replace(/ا(?=$)/, '').replace(/\\s+/g, ' ').trim();
  const B = s => W(s).replace(/[\\u064b-\\u0652]/g, '').replace(/[ؤئء]/g, 'ء').replace(/ة$/, 'ه');
  const memo = new Map();
  const strs = (v, out) => { if (typeof v === 'string') { if (/[ء-ي]/.test(v) && !/\\s—\\s|[a-z]/i.test(v) && v.split(/\\s+/).length <= 2) out.push(v); }
    else if (Array.isArray(v)) v.forEach(x => strs(x, out)); else if (v && typeof v === 'object') for (const k of Object.keys(v)) { if (/^(wazn|reason|note|notes|why|steps|gates|bab|cls|label|lbl|title|en|tr|src|book)$/i.test(k)) continue; strs(v[k], out); } return out; };
  const cells = (root, form, bab) => { const key = root + '|' + form + '|' + bab; if (memo.has(key)) return memo.get(key);
    let set = new Set();
    try { const cls = sarfClassX({ root }); const d = cls ? sarfDerive(cls, form, bab) : null;
      if (d && d.ok) { const all = strs(d, []);
        (d.mazi || []).forEach(c => { try { const p = sjMajhul(c, true); if (p) all.push(p); } catch (e) {} });
        (d.mudari || []).forEach(c => { try { const p = sjMajhul(c, false); if (p) all.push(p); } catch (e) {} });
        try { all.push(...TawkidEngine.all(d)); } catch (e) {}
        all.forEach(x => String(x).split(/\\s+|،/).forEach(y => y && set.add(NFC(y)))); } } catch (e) {}
    memo.set(key, set); return set; };
  const idx = new WeakMap();
  const has = (set, w, raw) => { let I = idx.get(set); if (!I) { I = { w: new Map(), b: new Map() }; for (const c of set) { if (!I.w.has(W(c))) I.w.set(W(c), c); if (!I.b.has(B(c))) I.b.set(B(c), c); } idx.set(set, I); }
    return (raw ? I.b.get(B(w)) : I.w.get(W(w))) || null; };
  const FORMS = [['I', 1], ['I', 2], ['I', 3], ['I', 4], ['I', 5], ['I', 6], ['II'], ['III'], ['IV'], ['V'], ['VI'], ['VII'], ['VIII'], ['IX'], ['X']];
  const find = (w, roots, raw) => { for (const r of roots) for (const [f, b] of FORMS) { const c = has(cells(r, f, b || 1), w, raw); if (c) return { root: r, form: f, bab: b || 1, cell: c }; } return null; };
  // a word's own root, only where the shelf attests it (RootFinder answered from the corpus, not from letter rules: كُلِنَّ is no root «ك ل ن»)
  const rootsOf = w => { const out = []; try { const r = RootFinder.find(NFC(w)); if (r && r.root && r.via === 'corpus') out.push(String(r.root).split('').filter(x => x.trim()).join(' ')); } catch (e) {} return out; };
  // the print's spelling, read as the engine writes: ى bearing a vowel is a yāʾ (the Maqṣūd's print), a fatḥa written after an alif belongs before it
  const IN = s => NFC(s).replace(/ى(?=[\\u064b-\\u0652])/g, 'ي').replace(/([ء-ي])ا َ/g, '$1َا').replace(/([ء-ي])اَ/g, '$1َا').replace(/^اَ/, 'أَ').replace(/^اُ(?=[ء-ي]ْ)/, 'اُ');
  const spell = d => { try { return IlalEngine.spell(d.out, d.asl); } catch (e) { return d && d.out; } };
  // the 35-door table's templates and model verbs (Bab35Engine.DOORS ar / model, Bab35Engine.MODELS) — a bāb the book names
  let babSet = null; const babs = () => { if (babSet) return babSet; babSet = new Set();
    const add = t => String(t || '').split(/[\s،·]+/).forEach(x => x && babSet.add(W(x)));
    (Bab35Engine.DOORS || []).forEach(d => { add(d.ar); add(d.model); }); Object.values(Bab35Engine.MODELS || {}).forEach(add); return babSet; };
  // the Maqṣūd's eighteen models: every cell MaqsudEngine derives for one (emsile, blocks, naql, the bāb rows)
  const mqMemo = new Map();
  const mqCells = key => { if (mqMemo.has(key)) return mqMemo.get(key); const m = MaqsudEngine.MODELS.find(x => x.key === key); const set = new Set();
    if (m) { const all = []; try { strs(MaqsudEngine.emsileI(m), all); } catch (e) {} try { strs(MaqsudEngine.blocksI(m), all); } catch (e) {} try { strs(MaqsudEngine.nakil(m), all); } catch (e) {}
      for (const r of m.babs || []) { try { strs(MaqsudEngine.babRow(m, r.form), all); } catch (e) {} }
      all.forEach(x => String(x).split(/\s+|،/).forEach(y => y && set.add(NFC(y)))); }
    mqMemo.set(key, set); return set; };
  // (v345-Q) the Maqṣūd's recitation of ANY bāb — MaqsudEngine.recite: the Emsile row, the amr ghāʾib / nahy blocks active and passive, the nūns
  //   mqr {root, key, variant?, w}   key = a Bab35Engine door (I1…I6, II…XIII, R1…R17); variant 'idgham-ta' = the permitted idghām of tafaʿʿul / tafāʿul
  const mqrMemo = new Map();
  const mqrCells = (root, key, variant) => { const k = root + '|' + key + '|' + (variant || ''); if (mqrMemo.has(k)) return mqrMemo.get(k);
    let set = new Set(); try { set = MaqsudEngine.reciteCells(String(root).split(/\\s+/), key, variant ? { variant } : {}); } catch (e) {} mqrMemo.set(k, set); return set; };
  const mqModelAt = line => { let best = null; for (const m of MaqsudEngine.MODELS) if (m.line <= line && (!best || m.line > best.line)) best = m; return best; };
  const run = p => { try {
    if (p.t === 'meaning') { const sh = Bab35Engine.meanings(p.form, { root: p.root }) || []; const list = Array.isArray(sh) ? sh : (sh.list || sh.items || []);
      const ok = list.some(m => (m.id || m) === p.id); return { ok, got: list.map(m => m.id || m).join(',') }; }
    if (p.t === 'bab') { const ok = babs().has(W(p.w)); return { ok, got: ok ? W(p.w) : null }; }
    if (p.t === 'mq') { const c = has(mqCells(p.key), p.w); return { ok: !!c, got: c }; }
    if (p.t === 'mqr') { const c = has(mqrCells(p.root, p.key, p.variant), IN(p.w), p.raw); return { ok: !!c, got: c }; }
    if (p.t === 'cells') { const c = has(cells(p.root, p.form, p.bab || 1), p.w, p.raw); return { ok: !!c, got: c }; }
    if (p.t === 'ilal') { const d = IlalEngine.derive(IN(p.asl)); const o = spell(d); return { ok: (p.raw ? B(o) === B(p.w) : W(o) === W(p.w)), got: o }; }
    if (p.t === 'kept') { const d = (ilalAslRead(NFC(p.asl)) || [])[0]; if (!d) return { ok: false, got: null };
      const ok = W(d.out) === W(d.w) && !d.steps.length && (d.gates || []).some(g => g.verdict === 'blocked' && (g.id === p.gate)); return { ok, got: d.out + ' ' + (d.gates || []).map(g => g.verdict + ':' + g.id).join(',') }; }
    if (p.t === 'isht') { const d = IshtiqaqEngine.read0(NFC(p.w)); const got = d ? [].concat(d.root).join(' ') + '|' + (d.pat && d.pat.id) : null; return { ok: got === p.root + '|' + p.pat, got }; }
    if (p.t === 'js') { const v = String((0, eval)(p.expr)); return { ok: v === p.want, got: v }; }
    return { ok: false, got: 'unknown probe ' + p.t };
  } catch (e) { return { ok: false, got: 'ERR ' + e.message }; } };
  return { W, B, IN, babs, mqCells, mqrCells, mqModelAt, cells, has, find, rootsOf, run, FORMS };
})()`;
