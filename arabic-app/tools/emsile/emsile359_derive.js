#!/usr/bin/env node
/* (v359-E) the Amthila notes' cells, written by the app's own ṣarf engines.
   Reads tools/emsile/emsile359_spec.json (written by build_emsile359.py spec), opens prototype/reader.html, and for every table calls
   Emsile359.fill (sarfDerive · MaqsudEngine.emsileI / blocksI / recite / jus14 · DamirEngine), attaches each pronoun row's corpus token
   (Emsile359.attest: an authored iʿrāb line that gives that pronoun that place), builds each common mistake from engine cells, and reads
   each example sentence and its translation from the corpus. Writes tools/emsile/emsile359_cells.json; build_emsile359.py notes then
   writes content/grammar/emsile-*.json. Usage: NODE_PATH=… CHROMIUM_PATH=… node tools/emsile/emsile359_derive.js */
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const root = path.resolve(__dirname, '..', '..');
(async () => {
  const spec = JSON.parse(fs.readFileSync(path.join(__dirname, 'emsile359_spec.json'), 'utf8'));
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH }); const p = await b.newPage();
  await p.addInitScript(() => { try { localStorage.setItem('qissa-welcomed', '1'); } catch (e) {} });
  await p.goto('file://' + path.join(root, 'prototype', 'reader.html'), { waitUntil: 'load', timeout: 300000 });
  await p.waitForFunction(() => typeof STORIES !== 'undefined' && STORIES.length > 10 && typeof Emsile359 !== 'undefined', null, { timeout: 300000 });
  const out = await p.evaluate(spec => {
    const E = Emsile359, att = E.attest(), res = { notes: {}, attKeys: Object.keys(att).length };
    const sent = r => { const st = STORIES.find(x => x.id === r[0]); const ch = st && st.chapters.find(c => (c.n !== undefined ? c.n : c.chapter) === r[1]);
      const sn = ch && ch.sentences.find(x => x.id === r[2]); if (!sn) return null;
      return { ar: sn.tokens.map(t => t.s.full + (t.punctAfter || '')).join(' '), en: (sn.translation || {}).en || '', tr: (sn.translation || {}).tr || '', level: st.level }; };
    for (const [id, n] of Object.entries(spec.notes)) {
      const tables = n.tables.map(t => { const f = E.fill(t);
        if (t.keys) f.refs = t.map ? t.keys.map(col => col.map(k => k ? att[k] || null : null)) : t.keys.map(k => k ? att[k] || null : null);
        return f; });
      const cell = c => { const a = (E.list(c.src) || [])[c.i] || null, b = c.plus ? (E.list(c.plus.src) || [])[c.plus.i] || null : ''; return a && b !== null ? (b ? a + ' ' + b : a) : null; };
      const mk = (n.mistakes || []).map(m => ({ wrong: cell(m.w), right: cell(m.r) }));
      const ex = (n.examples || []).map(r => Object.assign({ ref: r }, sent(r)));
      res.notes[id] = { tables, mk, ex };
    }
    return res;
  }, spec);
  fs.writeFileSync(path.join(__dirname, 'emsile359_cells.json'), JSON.stringify(out, null, 1));
  console.log('notes', Object.keys(out.notes).length, 'attested keys', out.attKeys);
  await b.close();
})();
