// label_gauge.js — (wave 170) how often does the vowelling engine name the OFFICE the author named?
//
//   CHROMIUM_PATH=… NODE_PATH=$PWD/node_modules node tools/label_gauge.js [reader.html] [--top N] [--out rows.txt]
//
// The sweeps grade the ENDING the engine writes. This grades the label beside it: every token of the shelf is read
// blind (no receipts — the engine sees the sentence a learner would type), the engine's rule is mapped to a seat
// (RuleMiner.RULE_SEAT) and set against the seat the author's iʿrāb line names (RuleMiner.SEATS). A line that names
// several offices («مَعْطُوفٌ … مَجْرُورٌ») agrees when it names the engine's office anywhere. A measuring tool, not a gate:
// it takes about a minute, and the number it prints belongs in CLAUDE.md beside the wave that moved it.
const { chromium } = require('playwright-core');
const fs = require('fs'), os = require('os'), path = require('path');
(async () => {
  const args = process.argv.slice(2);
  const reader = path.resolve(args.find(a => /\.html$/.test(a)) || path.join(__dirname, '..', 'prototype', 'reader.html'));
  const top = Number((args[args.indexOf('--top') + 1]) || 20), outFile = args.includes('--out') ? args[args.indexOf('--out') + 1] : null;
  const src = fs.readFileSync(reader, 'utf8');
  const hook = 'static grade(sen, mode){ this._receiptsOn136 = true;';
  if (src.split(hook).length !== 2) { console.error('label_gauge: the grade() hook was not found exactly once'); process.exit(2); }
  const tmp = path.join(os.tmpdir(), 'qissa-label-gauge-' + process.pid + '.html');
  fs.writeFileSync(tmp, src.replace(hook, 'static grade(sen, mode){ this._receiptsOn136 = !this._blind138;'));
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  try {
    const pg = await b.newPage(); await pg.goto('file://' + tmp); await pg.waitForSelector('.lib-card, .word', { timeout: 180000 });
    const rows = await pg.evaluate(() => { const out = [];
      STORIES.forEach(st => st.chapters.forEach(ch => (ch.sentences || []).forEach(sn => { DabtEngine._blind138 = true; let g = null; try { g = DabtEngine.grade(sn, 'endings'); } catch (e) { return; }
        g.words.forEach((w, i) => { const t = sn.tokens[i]; if (!t) return;
          const es = RuleMiner.RULE_SEAT[w.rule || ''] || '-'; const ar = String((t.irab || {}).ar || '').normalize('NFC'); const first = RuleMiner.seatOf(t) || '-';
          const pat = es !== '-' ? (RuleMiner.SEATS.find(x => x[0] === es) || [])[1] : null; const hs = first === '-' ? '-' : (pat && pat.test(ar) ? es : first);
          out.push([st.id, (ch.n || ch.chapter) + ':' + sn.id + '#' + i, t.s.full, w.rule || '-', es, hs, w.ok].join('|')); }); }))); return out; });
    if (outFile) fs.writeFileSync(outFile, rows.join('\n'));
    const R = rows.map(l => l.split('|')), both = R.filter(r => r[4] !== '-' && r[5] !== '-'), agree = both.filter(r => r[4] === r[5]).length;
    console.log('tokens ' + R.length + ' · both name an office ' + both.length + ' · agree ' + agree + ' · ' + (100 * agree / both.length).toFixed(2) + '%');
    const c = new Map(); both.forEach(r => { if (r[4] !== r[5]) { const k = 'engine ' + r[4] + ' | author ' + r[5]; c.set(k, (c.get(k) || 0) + 1); } });
    [...c.entries()].sort((x, y) => y[1] - x[1]).slice(0, top).forEach(([k, n]) => console.log(String(n).padStart(5) + '  ' + k));
  } finally { await b.close(); try { fs.unlinkSync(tmp); } catch (e) {} }
})().catch(e => { console.error('FAIL', e.message); process.exit(1); });
