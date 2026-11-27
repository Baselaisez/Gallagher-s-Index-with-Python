// v342-S — turn the ledger's candidates into probes: every book word an engine reproduces becomes a probe with its root, form
// and bāb fixed (so the smoke check re-proves exactly that); every «X أَصْلُهُ Y» the iʿlāl engine does NOT reproduce is listed
// as a contradiction for the open backlog.
//   python3 tools/ledger/sarf_ledger.py --candidates <scratch>/cand.json
//   node tools/ledger/sarf_probe_run.js <scratch>/cand.json content/rules/sarf_ledger_probes.json [hand.json]
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
(async () => {
  const [cand, out, hand] = process.argv.slice(2);
  const C = JSON.parse(fs.readFileSync(cand, 'utf8'));
  // (v345-Q) the hand list defaults to the Maqṣūd's applied units (tools/ledger/maqsud_hand_probes.py writes it)
  const H0 = hand || path.join(__dirname, 'maqsud_hand_probes.json');
  const H = fs.existsSync(H0) ? JSON.parse(fs.readFileSync(H0, 'utf8')) : [];
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const p = await b.newPage();
  await p.addInitScript(() => { try { localStorage.setItem('qissa-welcomed', '1'); } catch (e) {} });
  await p.goto('file://' + path.resolve(__dirname, '..', '..', 'prototype', 'reader.html'), { waitUntil: 'load', timeout: 300000 });
  await p.waitForFunction(() => typeof STORIES !== 'undefined' && STORIES.length > 10, null, { timeout: 300000 });
  const R = await p.evaluate(([src, C, H]) => {
    const L = (0, eval)(src); const probes = [], failed = [];
    for (const u of C.units) {
      let k = 0; const hits = [];
      for (const w of u.words) {
        // a quoted example (Marāḥ's «…») may be any root; a word of running text counts only on the books' own model roots
        const roots = u.quoted ? [...new Set([...L.rootsOf(w), ...C.roots])] : C.roots;
        const f = L.find(w, roots, u.raw);
        if (f) { hits.push({ entry: u.entry, t: 'cells', root: f.root, form: f.form, bab: f.bab, w, raw: u.raw || undefined, got: f.cell }); continue; }
        if (!u.raw && /[فعل]/.test(w) && L.run({ t: 'bab', w }).ok) { hits.push({ entry: u.entry, t: 'bab', w }); continue; }
        // a derived noun of running text counts only bare — no article, no jarr or kāf or joiner in front, no pronoun behind — and never
        // on ف ع ل, whose nouns (الْفَاعِلُ، الْمَفْعُولُ، الْفِعْلُ) are the books' terms, not their examples
        const bareOK = u.quoted || (!/^[وفبلك]?َ?ِ?(ال|لِل)/.test(w.normalize('NFC').replace(/[\u064b-\u0652]/g, '')) && !/^[بلك][َِ]/.test(w) && !/(هُ|هِ|هَا|هُمْ|كَ|كِ|ي)$/.test(w.normalize('NFC').replace(/[\u064b-\u0652]+$/, '')));
        if (bareOK && (w.match(/[\u064b-\u0652]/g) || []).length >= 2) { const r = L.run({ t: 'isht', w, root: '', pat: '' }); const m = /^(.+)\|(.+)$/.exec(r.got || '');
          if (m && (u.quoted || roots.includes(m[1])) && !(/^maqsud:/.test(u.entry) && /^(ف ت ح|ض م م|ك س ر|ف ع ل)$/.test(m[1])) && (u.quoted || m[1] !== 'ف ع ل')) { hits.push({ entry: u.entry, t: 'isht', w, root: m[1], pat: m[2] }); continue; } }
        if (u.mq) { const m = L.mqModelAt(u.mq); if (m && L.run({ t: 'mq', key: m.key, w }).ok) hits.push({ entry: u.entry, t: 'mq', key: m.key, w }); }
      }
      if (hits.length >= (u.min || 1)) hits.forEach(h => probes.push({ ...h, id: u.entry + '#' + (++k) }));
      for (const a of u.asl) {
        const pr = { t: 'ilal', asl: a.asl, w: a.w, raw: u.raw || undefined }; const r = L.run(pr);
        if (r.ok) probes.push({ entry: u.entry, id: u.entry + '#' + (++k), ...pr });
        else if (!u.raw) failed.push({ entry: u.entry, ...pr, got: r.got });   // a raw (unvowelled) aṣl is no test of a vowel rule: kept only when it passes
      }
    }
    // the Maqṣūd's meanings of the augmented bābs: every Bab35Engine.MEANINGS entry citing a Maqṣūd line is asked through meanings()
    for (const [form, list] of Object.entries(Bab35Engine.MEANINGS)) for (const m of list) {
      const mm = /Maqṣūd L(\d+)(?:–L(\d+))?/.exec(m.src || ''); if (!mm) continue; const a = +mm[1], z = +(mm[2] || mm[1]);
      const u = C.units.find(x => x.entry.startsWith('maqsud:') && (x.lines || []).some(n => n >= a && n <= z)) || C.mqUnits.find(x => x.lines.some(n => n >= a && n <= z));
      if (!u) continue; const pr = { t: 'meaning', form, id: m.id, root: m.root }; const r = L.run(pr);
      if (r.ok) probes.push({ entry: u.entry, id: u.entry + '#m-' + form + '-' + m.id, ...pr }); else failed.push({ entry: u.entry, ...pr, got: r.got }); }
    for (const h of H) { const r = L.run(h); if (r.ok) probes.push(h); else failed.push({ ...h, got: r.got, hand: true }); }
    return { probes, failed };
  }, [require('./sarf_probe_eval.js'), C, H]);
  fs.writeFileSync(out, JSON.stringify({ generated_by: 'tools/ledger/sarf_probe_run.js', note: 'every probe passed when written; the smoke check «v342 — the ṣarf ledger» re-runs them all', probes: R.probes }, null, 0).replace(/\},\{/g, '},\n{'));
  fs.writeFileSync(out.replace(/\.json$/, '.failed.json'), JSON.stringify(R.failed, null, 1));
  console.log('probes', R.probes.length, 'failed', R.failed.length, 'entries proved', new Set(R.probes.map(x => x.entry)).size);
  await b.close();
})();
