// API tests for the Finans360 server. Uses an in-memory database and fictional test people only.
import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

process.env.DB_PATH = ':memory:';
process.env.DATA_DIR = mkdtempSync(join(tmpdir(), 'f360-test-'));
const srv = await import('../server.js');

let base = '', server;
before(() => new Promise(ok => { server = http.createServer(srv.handle).listen(0, '127.0.0.1', () => { base = `http://127.0.0.1:${server.address().port}`; ok(); }); }));
after(() => new Promise(ok => server.close(ok)));

async function call(method, path, body, token) {
  const r = await fetch(base + path, { method, headers: { 'Content-Type': 'application/json', ...(token ? { Authorization: `Bearer ${token}` } : {}) }, body: body === undefined ? undefined : JSON.stringify(body) });
  return { status: r.status, body: await r.json().catch(() => null) };
}
// fictional people; TC numbers are generated to pass the checksum
function tc(seed) { const d = String(seed).split('').map(Number); const c10 = ((((d[0] + d[2] + d[4] + d[6] + d[8]) * 7 - (d[1] + d[3] + d[5] + d[7])) % 10) + 10) % 10; return d.join('') + c10 + ((d.reduce((a, b) => a + b, 0) + c10) % 10); }
const T = {};
async function login(username, password) { const r = await call('POST', '/api/login', { username, password }); assert.equal(r.status, 200, JSON.stringify(r.body)); return r.body.token; }
async function firstLogin(username, temp, next) {
  const tok = await login(username, temp);
  const blocked = await call('GET', '/api/bootstrap', undefined, tok);
  assert.equal(blocked.status, 403); assert.equal(blocked.body.code, 'must_change');
  assert.equal((await call('POST', '/api/me/password', { current: temp, next }, tok)).status, 200);
  return tok;
}

test('first run: health reports setup, weak passwords refused, admin created once', async () => {
  assert.equal((await call('GET', '/api/health')).body.setup, true);
  assert.equal((await call('POST', '/api/setup', { name: 'Test Yönetici', username: 'yonetici', password: 'kisa' })).status, 400);
  const r = await call('POST', '/api/setup', { name: 'Test Yönetici', username: 'yonetici', password: 'Guvenli2026' });
  assert.equal(r.status, 200); T.admin = r.body.token;
  assert.equal(r.body.perms.users, true);
  assert.equal((await call('POST', '/api/setup', { name: 'X', username: 'ikinci', password: 'Guvenli2026' })).status, 409);
  assert.equal((await call('GET', '/api/health')).body.setup, false);
});

test('unauthenticated requests are refused', async () => {
  assert.equal((await call('GET', '/api/bootstrap')).status, 401);
  assert.equal((await call('GET', '/api/bootstrap', undefined, 'x'.repeat(43))).status, 401);
});

test('admin imports people and creates scoped accounts', async () => {
  const people = [
    { name: 'Ali Test', firstName: 'Ali', lastName: 'Test', company: 'Alfa A.Ş.', title: 'Müdür', hireDate: '2020-01-15', tc: tc(123456789), phone: '+90 532 000 00 01', address: 'Test Mah. 1', blood: 'A Rh+' },
    { name: 'Ayşe Deneme', firstName: 'Ayşe', lastName: 'Deneme', company: 'Alfa A.Ş.', title: 'Uzman', hireDate: '2022-03-01', tc: tc(198765432), email: 'ayse@alfa.example', address: 'Örnek Sok. 2' },
    { name: 'Bora Örnek', firstName: 'Bora', lastName: 'Örnek', company: 'Beta Ltd.', title: 'Uzman', hireDate: '2021-06-01', tc: tc(345678912) }
  ];
  const imp = await call('POST', '/api/people/import', { people }, T.admin);
  assert.deepEqual(imp.body, { added: 3, updated: 0 });
  const again = await call('POST', '/api/people/import', { people: [{ ...people[0], title: 'Genel Müdür' }] }, T.admin);
  assert.deepEqual(again.body, { added: 0, updated: 1 });
  const boot = await call('GET', '/api/bootstrap', undefined, T.admin);
  T.p = Object.fromEntries(boot.body.people.map(p => [p.firstName, p]));
  assert.equal(T.p.Ali.title, 'Genel Müdür');
  assert.equal(T.p.Ali.tc, '', 'tc is never sent in bulk');
  assert.ok(T.p.Ali.tcInfo.valid && T.p.Ali.tcInfo.masked.includes('•'));

  const mk = async (body) => { const r = await call('POST', '/api/admin/users', body, T.admin); assert.equal(r.status, 200, JSON.stringify(r.body)); return r.body; };
  const mgr = await mk({ name: 'Ali Test', username: 'ali', role: 'manager', personId: T.p.Ali.id, companies: ['Alfa A.Ş.'] });
  const emp = await mk({ name: 'Ayşe Deneme', username: 'ayse', role: 'employee', personId: T.p.Ayşe.id });
  const empB = await mk({ name: 'Bora Örnek', username: 'bora', role: 'employee', personId: T.p.Bora.id });
  assert.equal((await call('POST', '/api/admin/users', { name: 'Kopya', username: 'x', personId: T.p.Ayşe.id }, T.admin)).status, 400, 'short username');
  assert.equal((await call('POST', '/api/admin/users', { name: 'Kopya', username: 'ayse2', personId: T.p.Ayşe.id }, T.admin)).status, 400, 'person already linked');
  T.mgr = await firstLogin('ali', mgr.tempPassword, 'Yonetici2026');
  T.emp = await firstLogin('ayse', emp.tempPassword, 'Personel2026');
  T.empB = await firstLogin('bora', empB.tempPassword, 'Personel2026b');
});

test('employee sees a directory of colleagues and only their own full record', async () => {
  const b = (await call('GET', '/api/bootstrap', undefined, T.emp)).body;
  assert.equal(b.perms.role, 'employee');
  const me = b.people.find(p => p.id === T.p.Ayşe.id), boss = b.people.find(p => p.id === T.p.Ali.id);
  assert.equal(me._access, 'full'); assert.equal(me.hireDate, '2022-03-01');
  assert.equal(boss._access, 'directory'); assert.equal(boss.phone, undefined); assert.equal(boss.hireDate, undefined); assert.equal(boss.tcInfo, undefined);
});

test('leave approval: employees request, managers in scope approve, nobody approves their own', async () => {
  const req = await call('PUT', '/api/leaves/l1', { person: 'me', type: 'yillik', start: '2026-11-02', end: '2026-11-04', status: 'approved' }, T.emp);
  assert.equal(req.status, 200); assert.equal(req.body.item.status, 'pending', 'employee cannot self-approve'); assert.equal(req.body.item.person, 'me');
  assert.equal((await call('PUT', '/api/leaves/l2', { person: 'Ali Test', type: 'yillik', start: '2026-11-02', end: '2026-11-02' }, T.emp)).status, 403);
  const mb = (await call('GET', '/api/bootstrap', undefined, T.mgr)).body;
  const seen = mb.leaves.find(l => l.id === 'l1');
  assert.ok(seen && seen._approve && seen.person === 'Ayşe Deneme');
  const ok = await call('PUT', '/api/leaves/l1', { ...seen, status: 'approved', note: 'Uygundur' }, T.mgr);
  assert.equal(ok.body.item.status, 'approved'); assert.ok(ok.body.item.history.some(h => h.text === 'Durum: Onaylandı' && h.by === 'Ali Test'));
  const own = await call('PUT', '/api/leaves/l3', { person: 'me', type: 'yillik', start: '2026-12-01', end: '2026-12-02', status: 'approved' }, T.mgr);
  assert.equal(own.body.item.status, 'pending', 'manager cannot approve own leave');
  assert.equal(own.body.item._approve, false);
  const adm = await call('PUT', '/api/leaves/l3', { ...own.body.item, person: 'Ali Test', status: 'approved' }, T.admin);
  assert.equal(adm.body.item.status, 'approved');
});

test('scope: a manager does not see other companies; employees cannot rewrite decided leave', async () => {
  assert.equal((await call('PUT', '/api/leaves/b1', { person: 'me', type: 'yillik', start: '2026-11-10', end: '2026-11-11' }, T.empB)).status, 200);
  const mb = (await call('GET', '/api/bootstrap', undefined, T.mgr)).body;
  assert.ok(!mb.leaves.some(l => l.id === 'b1'));
  assert.equal((await call('PUT', '/api/leaves/b1', { person: 'Bora Örnek', type: 'yillik', start: '2026-11-10', end: '2026-11-11', status: 'approved' }, T.mgr)).status, 404);
  const mine = (await call('GET', '/api/bootstrap', undefined, T.emp)).body.leaves.find(l => l.id === 'l1');
  assert.equal((await call('PUT', '/api/leaves/l1', { ...mine, end: '2026-11-06' }, T.emp)).status, 403);
  assert.equal((await call('DELETE', '/api/leaves/l1', undefined, T.emp)).status, 403);
  const cancel = await call('PUT', '/api/leaves/l1', { ...mine, status: 'cancelled' }, T.emp);
  assert.equal(cancel.body.item.status, 'cancelled');
});

test('sensitive fields: own record yes, others only with the sensitive permission, always audited', async () => {
  assert.equal((await call('GET', `/api/people/${T.p.Ayşe.id}/sensitive`, undefined, T.emp)).status, 200);
  assert.equal((await call('GET', `/api/people/${T.p.Ali.id}/sensitive`, undefined, T.emp)).status, 403);
  assert.equal((await call('GET', `/api/people/${T.p.Ayşe.id}/sensitive`, undefined, T.mgr)).status, 403);
  const users = (await call('GET', '/api/admin/users', undefined, T.admin)).body.users;
  const ali = users.find(u => u.username === 'ali');
  assert.equal((await call('PUT', `/api/admin/users/${ali.id}`, { sensitive: true }, T.admin)).status, 200);
  const s = await call('GET', `/api/people/${T.p.Ayşe.id}/sensitive`, undefined, T.mgr);
  assert.equal(s.status, 200); assert.equal(s.body.address, 'Örnek Sok. 2'); assert.equal(s.body.tc.length, 11);
  assert.equal((await call('GET', `/api/people/${T.p.Bora.id}/sensitive`, undefined, T.mgr)).status, 403, 'out of scope');
  const log = (await call('GET', '/api/admin/audit?action=person.sensitive', undefined, T.admin)).body.items;
  assert.ok(log.some(r => r.username === 'ali' && r.target === 'Ayşe Deneme'));
  assert.equal((await call('GET', '/api/admin/audit', undefined, T.mgr)).status, 403);
});

test('meetings: participants collaborate, only the organiser changes the meeting', async () => {
  const m = { title: 'Bütçe', kind: 'ekip', date: '2026-11-05', start: '10:00', end: '11:00', participants: ['Ali Test'], agenda: [{ id: 'a1', text: 'Gider', done: false }], notes: '' };
  assert.equal((await call('PUT', '/api/meetings/m1', m, T.emp)).status, 200);
  const seen = (await call('GET', '/api/bootstrap', undefined, T.mgr)).body.meetings.find(x => x.id === 'm1');
  assert.ok(seen && seen._own === false && seen._owner === 'Ayşe Deneme');
  const upd = await call('PUT', '/api/meetings/m1', { ...seen, title: 'Değiştirildi', notes: 'Not alındı', agenda: [{ id: 'a1', text: 'Gider', done: true }] }, T.mgr);
  assert.equal(upd.body.item.title, 'Bütçe'); assert.equal(upd.body.item.notes, 'Not alındı'); assert.equal(upd.body.item.agenda[0].done, true);
  assert.equal((await call('DELETE', '/api/meetings/m1', undefined, T.mgr)).status, 403);
  assert.ok(!(await call('GET', '/api/bootstrap', undefined, T.empB)).body.meetings.some(x => x.id === 'm1'), 'not invited');
  assert.equal((await call('DELETE', '/api/meetings/m1', undefined, T.emp)).status, 200);
});

test('admin-only areas and guard rails', async () => {
  assert.equal((await call('PUT', '/api/org', { rooms: ['A'] }, T.emp)).status, 403);
  assert.equal((await call('PUT', '/api/org', { rooms: ['Salon 1'], customHolidays: [{ date: '2026-12-31', name: 'İdari izin', half: true }] }, T.admin)).status, 200);
  assert.deepEqual((await call('GET', '/api/bootstrap', undefined, T.emp)).body.org.rooms, ['Salon 1']);
  assert.equal((await call('PUT', `/api/people/${T.p.Bora.id}`, { title: 'X' }, T.mgr)).status, 403);
  assert.equal((await call('GET', '/api/admin/users', undefined, T.emp)).status, 403);
  const me = (await call('GET', '/api/me', undefined, T.admin)).body.user;
  assert.equal((await call('PUT', `/api/admin/users/${me.id}`, { role: 'employee' }, T.admin)).status, 400, 'last admin');
  assert.equal((await call('DELETE', `/api/admin/users/${me.id}`, undefined, T.admin)).status, 400);
});

test('renaming a person follows into leaves; bulk accounts; export', async () => {
  assert.equal((await call('PUT', `/api/people/${T.p.Bora.id}`, { name: 'Bora Örnekoğlu', lastName: 'Örnekoğlu' }, T.admin)).status, 200);
  const leaf = (await call('GET', '/api/bootstrap', undefined, T.admin)).body.leaves.find(l => l.id === 'b1');
  assert.equal(leaf.person, 'Bora Örnekoğlu');
  await call('POST', '/api/people/import', { people: [{ name: 'Cem Yeni', company: 'Beta Ltd.', email: 'cem.yeni@beta.example' }] }, T.admin);
  const cem = (await call('GET', '/api/bootstrap', undefined, T.admin)).body.people.find(p => p.name === 'Cem Yeni');
  const bulk = await call('POST', '/api/admin/users/bulk', { personIds: [cem.id, T.p.Ayşe.id], role: 'employee' }, T.admin);
  assert.equal(bulk.body.created.length, 1, 'already-linked people are skipped');
  assert.equal(bulk.body.created[0].username, 'cem.yeni');
  const exp = await call('GET', '/api/admin/export', undefined, T.admin);
  assert.ok(exp.body.people.some(p => p.tc && p.tc.length === 11), 'export has full records');
  assert.ok(exp.body.users.every(u => !('pass' in u)), 'no password hashes in export');
});

test('password reset ends sessions; inactive users cannot sign in; brute force is slowed', async () => {
  const users = (await call('GET', '/api/admin/users', undefined, T.admin)).body.users;
  const bora = users.find(u => u.username === 'bora');
  const reset = await call('POST', `/api/admin/users/${bora.id}/reset-password`, undefined, T.admin);
  assert.equal((await call('GET', '/api/bootstrap', undefined, T.empB)).status, 401);
  assert.equal((await call('PUT', `/api/admin/users/${bora.id}`, { active: false }, T.admin)).status, 200);
  assert.equal((await call('POST', '/api/login', { username: 'bora', password: reset.body.tempPassword })).status, 401);
  let last;
  for (let i = 0; i < 9; i++) last = await call('POST', '/api/login', { username: 'ayse', password: 'yanlis-sifre-1' });
  assert.equal(last.status, 429);
});
