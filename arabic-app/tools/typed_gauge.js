#!/usr/bin/env node
// typed_gauge.js — the sentence a learner TYPES, with no vowels at all, read by the ḍabṭ engine and judged against a
// battery of plain everyday sentences whose endings are written out (tools/typed_battery.txt).
//
// The shelf's sweeps cannot see this: the shelf is vowelled, and «blind» there means «endings stripped», so every
// interior vowel still reaches the engine. A typed sentence carries none — the lexicon is asked with bare letters, the
// verb's tense is open, the sound plural's nūn has no vowel to keep. This gauge is the only place that is measured.
//
// Battery line:   expected sentence                (# starts a comment, blank lines are skipped)
//   • the INPUT is the expected sentence with every mark removed;
//   • a word is RIGHT when its letters come back unchanged, every mark the expected word writes stands on the same
//     letter of the engine's word, and the LAST letter carries exactly the expected marks (none where none is written);
//   • a word prefixed with ~ is not judged (a verb whose person the bare letters leave open, a built particle the
//     engine leaves as typed).
//
//   node tools/typed_gauge.js            → the number, then every miss
//   node tools/typed_gauge.js --json     → {words, right, sentences, clean, misses:[…]}
//   node tools/typed_gauge.js --floor N  → exit 1 when fewer than N % of the judged words are right
const path = require('path'), fs = require('fs');
const { chromium } = require('playwright-core');
const ROOT = path.resolve(__dirname, '..');
const READER = process.env.READER || path.join(ROOT, 'prototype', 'reader.html');
const BATTERY = process.env.BATTERY || path.join(__dirname, 'typed_battery.txt');
const MARKS = /[ً-ْٰ]/;
const units = w => { const out = []; for (const ch of String(w || '').normalize('NFC')) { if (MARKS.test(ch)) { if (out.length) out[out.length - 1].m += ch; } else out.push({ l: ch, m: '' }); } return out; };
const sortM = m => m.split('').sort().join('');
const judge = (exp, got) => {
  const a = units(exp), b = units(got);
  if (a.map(x => x.l).join('') !== b.map(x => x.l).join('')) return false;
  for (let i = 0; i < a.length; i++) { const last = i === a.length - 1; if ((a[i].m || last) && sortM(a[i].m) !== sortM(b[i].m)) return false; }
  return true;
};
(async () => {
  const lines = fs.readFileSync(BATTERY, 'utf8').split('\n').map(x => x.trim()).filter(x => x && !x.startsWith('#'));
  const items = lines.map(line => { const words = line.split(/\s+/); return { exp: words.map(w => w.replace(/^~/, '')), skip: words.map(w => w.startsWith('~')), bare: words.map(w => w.replace(/^~/, '').normalize('NFC').replace(/[ً-ْٰ]/g, '')).join(' ') }; });
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH, args: ['--no-sandbox'] });
  const p = await b.newPage(); const errs = []; p.on('pageerror', e => errs.push(String(e).slice(0, 200)));
  await p.addInitScript(() => { window.__QISSA_QUIET_OFF = true; try { localStorage.setItem('qissa-welcomed', '1'); } catch (e) {} });
  await p.goto('file://' + READER);
  await p.waitForFunction(() => typeof STORIES !== 'undefined' && STORIES.length > 0 && typeof DabtEngine !== 'undefined', null, { timeout: 180000 });
  const outs = await p.evaluate(sents => sents.map(t => { DabtEngine._lex24 = null; DabtEngine._pos24 = null; DabtEngine._orig24 = null; DabtEngine._lastGraded26 = null; DabtEngine._carry26 = null;
    try { const v = DabtEngine.vowel(t, 'endings'); return (v.words || []).map(w => [String(w.out || ''), String(w.rule || '')]); } catch (e) { return []; } }), items.map(x => x.bare));
  await b.close();
  let words = 0, right = 0, clean = 0; const misses = [];
  items.forEach((it, k) => { const got = outs[k] || []; let ok = true;
    it.exp.forEach((e, i) => { if (it.skip[i]) return; words++; const g = (got[i] || ['', ''])[0]; if (judge(e, g)) right++; else { ok = false; misses.push({ sentence: it.exp.join(' '), i, want: e, got: g, rule: (got[i] || ['', ''])[1] }); } });
    if (ok) clean++; });
  const pct = words ? (100 * right / words) : 0;
  const res = { words, right, pct: Math.round(pct * 100) / 100, sentences: items.length, clean, misses, pageErrors: errs };
  if (process.argv.includes('--json')) console.log(JSON.stringify(res));
  else { console.log(`typed gauge: ${right} of ${words} judged words right (${res.pct} %), ${clean} of ${items.length} sentences clean`);
    for (const m of misses) console.log(`  ✗ ${m.sentence}  #${m.i}  want ${m.want}  got ${m.got}  (${m.rule})`);
    if (errs.length) console.log('page errors', errs); }
  const fi = process.argv.indexOf('--floor');
  if (fi > -1 && pct < Number(process.argv[fi + 1])) { console.error(`typed gauge below its floor: ${res.pct} % < ${process.argv[fi + 1]} %`); process.exit(1); }
})().catch(e => { console.error(e); process.exit(2); });
