#!/usr/bin/env node
// Finans360 server: user accounts, roles and shared data for the Finans360 app.
// Requires Node.js 22.13+ (built-in node:sqlite). No third-party dependencies.
//
//   node --no-warnings server.js                       start the server
//   node --no-warnings server.js create-admin <user>   create an admin, prints a one-time password
//   node --no-warnings server.js reset-password <user> prints a new one-time password
//   node --no-warnings server.js backup <file.json>    writes a full JSON backup
import http from 'node:http';
import crypto from 'node:crypto';
import { readFileSync, existsSync, statSync, mkdirSync, chmodSync, writeFileSync, createReadStream } from 'node:fs';
import { join, resolve, extname, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { DatabaseSync } from 'node:sqlite';

export const VERSION = '1.0.0';
const HERE = dirname(fileURLToPath(import.meta.url));
const CFG = {
  port: +process.env.PORT || 8360,
  host: process.env.HOST || '127.0.0.1',
  dataDir: resolve(process.env.DATA_DIR || join(HERE, 'data')),
  webDir: resolve(process.env.WEB_DIR || join(HERE, '..')),
  vendorDir: resolve(join(HERE, 'vendor')),
  trustProxy: process.env.TRUST_PROXY === '1',
  sessionDays: +process.env.SESSION_DAYS || 30,
  maxBody: 8 * 1024 * 1024
};

/* ================= database ================= */
mkdirSync(CFG.dataDir, { recursive: true, mode: 0o700 });
const DB_PATH = process.env.DB_PATH || join(CFG.dataDir, 'finans360.db');
export const db = new DatabaseSync(DB_PATH);
try { if (DB_PATH !== ':memory:') chmodSync(DB_PATH, 0o600); } catch { /* not fatal */ }
db.exec(`
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;
PRAGMA busy_timeout = 3000;
CREATE TABLE IF NOT EXISTS users (
  id TEXT PRIMARY KEY, username TEXT NOT NULL UNIQUE COLLATE NOCASE, name TEXT NOT NULL, role TEXT NOT NULL,
  person_id TEXT, companies TEXT NOT NULL DEFAULT '[]', sensitive INTEGER NOT NULL DEFAULT 0, pass TEXT NOT NULL,
  must_change INTEGER NOT NULL DEFAULT 1, active INTEGER NOT NULL DEFAULT 1, prefs TEXT NOT NULL DEFAULT '{}',
  created_at TEXT NOT NULL, updated_at TEXT NOT NULL, last_login TEXT);
CREATE TABLE IF NOT EXISTS sessions (
  id TEXT PRIMARY KEY, user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  created_at TEXT NOT NULL, last_seen TEXT NOT NULL, expires_at TEXT NOT NULL, ip TEXT, ua TEXT);
CREATE TABLE IF NOT EXISTS people (id TEXT PRIMARY KEY, name TEXT NOT NULL, company TEXT NOT NULL DEFAULT '', data TEXT NOT NULL, updated_at TEXT NOT NULL, updated_by TEXT);
CREATE TABLE IF NOT EXISTS leaves (id TEXT PRIMARY KEY, person_id TEXT, person_name TEXT NOT NULL, company TEXT NOT NULL DEFAULT '', status TEXT NOT NULL, data TEXT NOT NULL, created_by TEXT, updated_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS meetings (id TEXT PRIMARY KEY, owner_id TEXT, data TEXT NOT NULL, updated_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS audit (id INTEGER PRIMARY KEY AUTOINCREMENT, at TEXT NOT NULL, user_id TEXT, username TEXT, action TEXT NOT NULL, target TEXT, detail TEXT, ip TEXT);
CREATE INDEX IF NOT EXISTS audit_at ON audit(at);
CREATE INDEX IF NOT EXISTS leaves_person ON leaves(person_id);
`);
const q = sql => db.prepare(sql);
function tx(fn) { db.exec('BEGIN'); try { const r = fn(); db.exec('COMMIT'); return r; } catch (e) { db.exec('ROLLBACK'); throw e; } }

/* ================= small helpers ================= */
const now = () => new Date().toISOString();
const uid = () => crypto.randomBytes(9).toString('base64url');
const J = s => { try { return JSON.parse(s); } catch { return null; } };
const sha256 = s => crypto.createHash('sha256').update(String(s)).digest('hex');
const str = (v, max = 500) => (v == null ? '' : String(v)).slice(0, max);
const isDate = s => /^\d{4}-\d{2}-\d{2}$/.test(s || '');
const isTime = s => /^\d{2}:\d{2}$/.test(s || '');
const lowerTR = s => String(s == null ? '' : s).toLocaleLowerCase('tr');
const fold = s => lowerTR(s).replace(/[çğıöşüâîû]/g, c => ({ ç: 'c', ğ: 'g', ı: 'i', ö: 'o', ş: 's', ü: 'u', â: 'a', î: 'i', û: 'u' }[c])).replace(/[^a-z0-9]/g, '');
const FREE_MAIL = /^(gmail|googlemail|hotmail|outlook|live|msn|yahoo|ymail|icloud|me|mac|yandex|mail|gmx|aol|proton|protonmail|mynet|windowslive|superonline|ttmail)\./;
const isFreeMail = e => { const d = String(e || '').split('@')[1] || ''; return FREE_MAIL.test(d) || /\.edu(\.[a-z]{2})?$/.test(d); };
const maskTC = t => (!t ? '' : t.length > 5 ? t.slice(0, 3) + '•'.repeat(t.length - 5) + t.slice(-2) : '•••');
function tcValid(t) {
  if (!/^[1-9]\d{10}$/.test(t || '')) return false;
  const d = [...t].map(Number);
  const c10 = ((((d[0] + d[2] + d[4] + d[6] + d[8]) * 7 - (d[1] + d[3] + d[5] + d[7])) % 10) + 10) % 10;
  return c10 === d[9] && d.slice(0, 10).reduce((a, b) => a + b, 0) % 10 === d[10];
}

/* ================= passwords & sessions ================= */
const SCRYPT = { N: 16384, r: 8, p: 1, maxmem: 64 * 1024 * 1024 };
export function hashPassword(pw) {
  const salt = crypto.randomBytes(16);
  return `scrypt$${salt.toString('base64')}$${crypto.scryptSync(String(pw), salt, 32, SCRYPT).toString('base64')}`;
}
function checkPassword(pw, stored) {
  const [alg, s, k] = String(stored || '').split('$');
  if (alg !== 'scrypt' || !s || !k) return false;
  const key = crypto.scryptSync(String(pw), Buffer.from(s, 'base64'), 32, SCRYPT), ref = Buffer.from(k, 'base64');
  return ref.length === key.length && crypto.timingSafeEqual(ref, key);
}
const DUMMY_HASH = hashPassword(crypto.randomBytes(12).toString('hex'));
export function tempPassword() {
  const A = 'abcdefghjkmnpqrstuvwxyzACDEFGHJKLMNPQRSTUVWXYZ23456789';
  for (;;) {
    const p = [...crypto.randomBytes(12)].map(x => A[x % A.length]).join('');
    if (/\d/.test(p) && /[a-z]/i.test(p)) return `${p.slice(0, 4)}-${p.slice(4, 8)}-${p.slice(8)}`;
  }
}
function passwordProblem(pw, username) {
  if (typeof pw !== 'string' || pw.length < 8) return 'Şifre en az 8 karakter olmalı.';
  if (pw.length > 200) return 'Şifre en fazla 200 karakter olabilir.';
  if (username && pw.toLowerCase().includes(String(username).toLowerCase())) return 'Şifre kullanıcı adını içermemeli.';
  if (!/[A-Za-zÇĞİÖŞÜçğıöşü]/.test(pw) || !/\d/.test(pw)) return 'Şifrede en az bir harf ve bir rakam olmalı.';
  return '';
}
const attempts = new Map();
const isLimited = key => { const a = attempts.get(key); return !!a && a.n >= 8 && a.until > Date.now(); };
function noteFail(key) { const a = attempts.get(key) || { n: 0, until: 0 }; if (a.until < Date.now()) a.n = 0; a.n++; a.until = Date.now() + 15 * 60000; attempts.set(key, a); }

function rowUser(u) {
  return { id: u.id, username: u.username, name: u.name, role: u.role, personId: u.person_id || null, companies: J(u.companies) || [], sensitive: !!u.sensitive, mustChange: !!u.must_change, active: !!u.active, prefs: J(u.prefs) || {}, lastLogin: u.last_login || null, createdAt: u.created_at };
}
function createSession(user, ip, ua) {
  const token = crypto.randomBytes(32).toString('base64url'), t = now();
  q('INSERT INTO sessions (id, user_id, created_at, last_seen, expires_at, ip, ua) VALUES (?, ?, ?, ?, ?, ?, ?)')
    .run(sha256(token), user.id, t, t, new Date(Date.now() + CFG.sessionDays * 864e5).toISOString(), ip || '', str(ua, 200));
  return token;
}
function authUser(req) {
  const m = String(req.headers.authorization || '').match(/^Bearer\s+([\w-]{20,})$/);
  if (!m) return null;
  const sid = sha256(m[1]);
  const s = q('SELECT * FROM sessions WHERE id = ?').get(sid);
  if (!s) return null;
  if (s.expires_at < now()) { q('DELETE FROM sessions WHERE id = ?').run(sid); return null; }
  const u = q('SELECT * FROM users WHERE id = ?').get(s.user_id);
  if (!u || !u.active) return null;
  if (Date.parse(s.last_seen) < Date.now() - 600000) q('UPDATE sessions SET last_seen = ?, expires_at = ? WHERE id = ?').run(now(), new Date(Date.now() + CFG.sessionDays * 864e5).toISOString(), sid);
  return { ...rowUser(u), sid };
}

/* ================= access model ================= */
// Roles. "scope" means the companies listed on the user; "self" means the person record linked to the user.
export const ROLES = {
  admin: { label: 'Yönetici', peopleRead: 'all', peopleWrite: 'all', leaveRead: 'all', leaveFor: 'all', approve: 'all', users: true, audit: true, org: true, export: true, sensitive: true },
  manager: { label: 'Birim yöneticisi', peopleRead: 'scope', peopleWrite: 'none', leaveRead: 'scope', leaveFor: 'scope', approve: 'scope', users: false, audit: false, org: false, export: false, sensitive: false },
  employee: { label: 'Personel', peopleRead: 'self', peopleWrite: 'none', leaveRead: 'self', leaveFor: 'self', approve: 'none', users: false, audit: false, org: false, export: false, sensitive: false }
};
function permsOf(u) { const r = ROLES[u.role] || ROLES.employee; return { ...r, role: u.role, sensitive: r.sensitive || !!u.sensitive, companies: u.companies, personId: u.personId }; }
const inScope = (u, company) => u.role === 'admin' || (u.role === 'manager' && !!company && u.companies.includes(company));
function personAccess(u, p) {
  if (u.role === 'admin') return 'full';
  if (p.id && p.id === u.personId) return 'full';
  if (u.role === 'manager' && inScope(u, p.company)) return 'full';
  return 'directory';
}
const canApprove = (u, t) => u.role === 'admin' || (u.role === 'manager' && !(t.id && t.id === u.personId) && inScope(u, t.company));
const canFileFor = (u, t) => u.role === 'admin' || (!!t.id && t.id === u.personId) || (u.role === 'manager' && !!t.id && inScope(u, t.company));

/* ================= audit ================= */
function audit(u, action, target, detail, ip) {
  q('INSERT INTO audit (at, user_id, username, action, target, detail, ip) VALUES (?, ?, ?, ?, ?, ?, ?)')
    .run(now(), u ? u.id : null, u ? u.username : null, action, str(target, 200), str(detail, 1000), ip || '');
}

/* ================= people ================= */
const PERSON_FIELDS = ['name', 'firstName', 'lastName', 'company', 'title', 'hireDate', 'hireYear', 'birthDate', 'birthYear', 'birthPlace', 'tc', 'phone', 'email', 'email2', 'address', 'blood', 'education', 'gradDate', 'languages', 'marital', 'children', 'interests', 'entitlementOverride', 'carryOver', 'notes', 'source'];
const SENSITIVE = ['tc', 'blood', 'address'];
const DIRECTORY = ['id', 'name', 'firstName', 'lastName', 'title', 'company', 'email'];
function cleanPerson(src, keepSensitive) {
  const p = {};
  for (const k of PERSON_FIELDS) {
    if (!keepSensitive && SENSITIVE.includes(k)) continue;
    const v = src[k];
    if (k === 'carryOver') p[k] = Math.max(-365, Math.min(365, parseFloat(String(v ?? '').replace(',', '.')) || 0));
    else if (k === 'hireYear' || k === 'birthYear') p[k] = /^\d{4}$/.test(String(v ?? '')) ? +v : '';
    else if ((k === 'hireDate' || k === 'birthDate') && v && !isDate(v)) p[k] = '';
    else p[k] = str(v, k === 'interests' || k === 'notes' || k === 'address' ? 2000 : 300).trim();
  }
  if (p.tc !== undefined) p.tc = p.tc.replace(/\D/g, '').slice(0, 11);
  return p;
}
const getPersonRow = id => (id ? q('SELECT * FROM people WHERE id = ?').get(id) : null);
const personData = row => ({ ...(J(row.data) || {}), id: row.id });
function findPersonByName(name) {
  const f = fold(name); if (!f) return null;
  for (const r of q('SELECT * FROM people').all()) if (fold(r.name) === f) return r;
  return null;
}
function personOut(u, row) {
  const p = personData(row);
  if (personAccess(u, p) === 'directory') {
    const o = { _access: 'directory' };
    for (const k of DIRECTORY) o[k] = p[k] || '';
    if (o.email && isFreeMail(o.email)) o.email = '';
    return o;
  }
  const out = { ...p, _access: 'full' };
  const tc = String(p.tc || '');
  out.tcInfo = tc ? { masked: maskTC(tc), valid: tcValid(tc) } : null;
  out.hasSensitive = !!(tc || p.blood || p.address);
  for (const k of SENSITIVE) out[k] = '';
  return out;
}
function savePerson(id, p, by) {
  q('INSERT INTO people (id, name, company, data, updated_at, updated_by) VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT(id) DO UPDATE SET name = excluded.name, company = excluded.company, data = excluded.data, updated_at = excluded.updated_at, updated_by = excluded.updated_by')
    .run(id, p.name, p.company || '', JSON.stringify(p), now(), by || null);
}
function renamePersonRefs(personId, oldName, newName, company) {
  if (!oldName || oldName === newName) { q('UPDATE leaves SET company = ? WHERE person_id = ?').run(company || '', personId); return; }
  q('UPDATE leaves SET person_name = ?, company = ? WHERE person_id = ?').run(newName, company || '', personId);
  for (const r of q('SELECT id, data FROM meetings').all()) {
    const d = J(r.data) || {};
    if (!Array.isArray(d.participants) || !d.participants.includes(oldName)) continue;
    d.participants = d.participants.map(n => (n === oldName ? newName : n));
    if (d.attendance && d.attendance[oldName]) { d.attendance[newName] = d.attendance[oldName]; delete d.attendance[oldName]; }
    q('UPDATE meetings SET data = ? WHERE id = ?').run(JSON.stringify(d), r.id);
  }
}
function mergePeople(list, by) {
  let added = 0, updated = 0;
  tx(() => {
    for (const src of list) {
      if (!src || !str(src.name).trim()) continue;
      const rec = cleanPerson(src, true);
      const ex = (rec.tc && tcValid(rec.tc) ? q('SELECT * FROM people').all().find(r => (J(r.data) || {}).tc === rec.tc) : null) || findPersonByName(rec.name);
      if (ex) {
        const prev = personData(ex), next = { ...prev };
        for (const k of PERSON_FIELDS) { const v = rec[k]; if (v !== '' && v != null && !(k === 'carryOver' && !v)) next[k] = v; }
        if (rec.hireDate) next.hireYear = ''; if (rec.birthDate) next.birthYear = '';
        delete next.id;
        savePerson(ex.id, next, by); renamePersonRefs(ex.id, prev.name, next.name, next.company); updated++;
      } else { savePerson(uid(), rec, by); added++; }
    }
  });
  return { added, updated };
}

/* ================= leaves ================= */
const LEAVE_TYPES = ['yillik', 'mazeret', 'saatlik', 'rapor', 'ucretsiz', 'dogum', 'idari', 'dogumgunu'];
const STATUSES = { pending: 'Bekliyor', approved: 'Onaylandı', rejected: 'Reddedildi', cancelled: 'İptal' };
const LEAVE_CORE = ['type', 'sub', 'start', 'end', 'startHalf', 'endHalf', 'startTime', 'endTime'];
function leaveVisible(u, row) {
  if (u.role === 'admin') return true;
  if (row.person_id && row.person_id === u.personId) return true;
  if (row.created_by === u.id) return true;
  return u.role === 'manager' && inScope(u, row.company);
}
function leaveOut(u, row) {
  const d = J(row.data) || {};
  let person = row.person_name;
  if (row.person_id && row.person_id === u.personId) person = 'me';
  else if (row.person_id) { const pr = getPersonRow(row.person_id); if (pr) person = pr.name; }
  const target = { id: row.person_id, company: row.company };
  return { ...d, id: row.id, person, status: row.status, _approve: canApprove(u, target), _mine: !!(row.person_id && row.person_id === u.personId) };
}
function resolveTarget(u, personField) {
  if (personField === 'me') {
    if (!u.personId) return { err: 'Hesabınız bir personel kaydına bağlı değil. Yöneticiden hesabınızı kaydınıza bağlamasını isteyin.' };
    const p = getPersonRow(u.personId);
    return p ? { id: p.id, name: p.name, company: p.company } : { err: 'Personel kaydınız bulunamadı.' };
  }
  const name = str(personField, 200).trim();
  if (!name) return { err: 'Kişi seçin.' };
  const p = findPersonByName(name);
  return p ? { id: p.id, name: p.name, company: p.company } : { id: null, name, company: '' };
}
function cleanLeave(b) {
  const d = {
    type: LEAVE_TYPES.includes(b.type) ? b.type : 'yillik', sub: str(b.sub, 40), start: str(b.start, 10), end: str(b.end, 10),
    startHalf: !!b.startHalf, endHalf: !!b.endHalf, startTime: str(b.startTime, 5), endTime: str(b.endTime, 5),
    deputy: str(b.deputy, 200), contact: str(b.contact, 300), reason: str(b.reason, 2000), note: str(b.note, 1000)
  };
  if (!isDate(d.start)) return { err: 'Başlangıç tarihi geçersiz.' };
  if (d.type === 'saatlik') { d.end = d.start; if (!isTime(d.startTime) || !isTime(d.endTime) || d.endTime <= d.startTime) return { err: 'Saatler geçersiz.' }; }
  else if (!isDate(d.end) || d.end < d.start) return { err: 'Bitiş tarihi başlangıçtan önce olamaz.' };
  return { d };
}
function putLeave(u, id, b, ip) {
  const ex = q('SELECT * FROM leaves WHERE id = ?').get(id);
  if (ex && !leaveVisible(u, ex)) return [404, { error: 'Kayıt bulunamadı.' }];
  const target = resolveTarget(u, b.person);
  if (target.err) return [400, { error: target.err }];
  if (!canFileFor(u, target)) return [403, { error: 'Bu kişi için izin kaydı oluşturma yetkiniz yok.' }];
  if (ex && ex.person_id !== target.id && !canFileFor(u, { id: ex.person_id, company: ex.company })) return [403, { error: 'Bu kaydı değiştirme yetkiniz yok.' }];
  const c = cleanLeave(b); if (c.err) return [400, { error: c.err }];
  const d = c.d, prev = ex ? J(ex.data) || {} : null;
  const approver = canApprove(u, target);
  const wanted = STATUSES[b.status] ? b.status : 'pending';
  const coreChanged = prev ? LEAVE_CORE.some(k => String(prev[k] ?? '') !== String(d[k] ?? '')) : true;
  let status;
  if (approver) status = wanted;
  else if (!ex) status = 'pending';
  else if (wanted === 'cancelled' && ex.status !== 'cancelled') status = 'cancelled';
  else if (ex.status === 'pending') status = 'pending';
  else if (coreChanged) return [403, { error: 'Sonuçlanmış bir izni değiştiremezsiniz. İptal edip yeniden talep oluşturun.' }];
  else status = ex.status;
  if (!approver) d.note = prev ? prev.note || '' : '';
  const hist = prev && Array.isArray(prev.history) ? prev.history.slice(-60) : [];
  if (!ex) hist.push({ at: now(), text: target.id && target.id === u.personId ? 'Talep oluşturuldu' : 'Kayıt eklendi', by: u.name });
  else if (coreChanged) hist.push({ at: now(), text: 'Düzenlendi', by: u.name });
  if ((ex && ex.status !== status) || (!ex && status !== 'pending')) hist.push({ at: now(), text: `Durum: ${STATUSES[status]}`, by: u.name });
  const data = { ...d, history: hist, createdAt: prev && prev.createdAt ? prev.createdAt : now() };
  q('INSERT INTO leaves (id, person_id, person_name, company, status, data, created_by, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id) DO UPDATE SET person_id = excluded.person_id, person_name = excluded.person_name, company = excluded.company, status = excluded.status, data = excluded.data, updated_at = excluded.updated_at')
    .run(id, target.id, target.name, target.company || '', status, JSON.stringify(data), ex ? ex.created_by : u.id, now());
  if (!ex) audit(u, 'leave.create', target.name, `${d.start}–${d.end} ${d.type} (${STATUSES[status]})`, ip);
  else if (ex.status !== status) audit(u, 'leave.status', target.name, `${d.start}–${d.end}: ${STATUSES[ex.status]} → ${STATUSES[status]}`, ip);
  return [200, { item: leaveOut(u, q('SELECT * FROM leaves WHERE id = ?').get(id)) }];
}
function deleteLeave(u, id, ip) {
  const ex = q('SELECT * FROM leaves WHERE id = ?').get(id);
  if (!ex || !leaveVisible(u, ex)) return [404, { error: 'Kayıt bulunamadı.' }];
  const target = { id: ex.person_id, company: ex.company };
  const ownPending = (ex.created_by === u.id || (ex.person_id && ex.person_id === u.personId)) && ex.status === 'pending';
  if (!canApprove(u, target) && !ownPending) return [403, { error: 'Bu izni silemezsiniz; iptal etmeyi deneyin.' }];
  q('DELETE FROM leaves WHERE id = ?').run(id);
  audit(u, 'leave.delete', ex.person_name, `${STATUSES[ex.status]}`, ip);
  return [200, { ok: true }];
}

/* ================= meetings ================= */
const KINDS = ['ekip', 'yonetim', 'banka', 'kapanis', 'denetim', 'birebir', 'diger'];
function meetingVisible(u, row, d) {
  if (u.role === 'admin' || row.owner_id === u.id) return true;
  const me = u.personId ? getPersonRow(u.personId) : null;
  if (!me) return false;
  const f = fold(me.name);
  return (d.participants || []).some(n => fold(n) === f);
}
const ownerName = id => (id ? (q('SELECT name FROM users WHERE id = ?').get(id) || {}).name || '' : '');
function meetingOut(u, row) { return { ...(J(row.data) || {}), id: row.id, _own: u.role === 'admin' || row.owner_id === u.id, _owner: ownerName(row.owner_id) }; }
function cleanMeeting(b) {
  const arr = (v, n) => (Array.isArray(v) ? v.slice(0, n) : []);
  const m = {
    seriesId: b.seriesId ? str(b.seriesId, 40) : null, title: str(b.title, 300).trim(), kind: KINDS.includes(b.kind) ? b.kind : 'diger',
    date: str(b.date, 10), start: str(b.start, 5), end: str(b.end, 5), location: str(b.location, 300), link: str(b.link, 1000),
    participants: arr(b.participants, 300).map(x => str(x, 200)).filter(Boolean),
    agenda: arr(b.agenda, 200).map(a => ({ id: str(a && a.id, 40) || uid(), text: str(a && a.text, 500), done: !!(a && a.done) })),
    notes: str(b.notes, 20000),
    actions: arr(b.actions, 200).map(a => ({ id: str(a && a.id, 40) || uid(), text: str(a && a.text, 500), owner: str(a && a.owner, 200), due: isDate(a && a.due) ? a.due : '', done: !!(a && a.done) })),
    attendance: {}, reminder: Math.max(0, Math.min(10080, +b.reminder || 0)),
    status: ['planned', 'done', 'cancelled'].includes(b.status) ? b.status : 'planned', createdAt: str(b.createdAt, 40) || now()
  };
  if (b.attendance && typeof b.attendance === 'object') for (const [k, v] of Object.entries(b.attendance).slice(0, 300)) if (v === 'yes' || v === 'no') m.attendance[str(k, 200)] = v;
  if (!m.title) return { err: 'Toplantı konusu boş olamaz.' };
  if (!isDate(m.date) || !isTime(m.start) || !isTime(m.end) || m.end <= m.start) return { err: 'Tarih ya da saat geçersiz.' };
  return { m };
}
function putMeeting(u, id, b, ip) {
  const ex = q('SELECT * FROM meetings WHERE id = ?').get(id);
  const prev = ex ? J(ex.data) || {} : null;
  if (ex && !meetingVisible(u, ex, prev)) return [404, { error: 'Toplantı bulunamadı.' }];
  const c = cleanMeeting(b); if (c.err) return [400, { error: c.err }];
  const own = !ex || ex.owner_id === u.id || u.role === 'admin';
  // participants may update the working parts of a meeting; the organiser controls the rest
  const data = own ? c.m : { ...prev, agenda: c.m.agenda, actions: c.m.actions, attendance: c.m.attendance, notes: c.m.notes };
  q('INSERT INTO meetings (id, owner_id, data, updated_at) VALUES (?, ?, ?, ?) ON CONFLICT(id) DO UPDATE SET data = excluded.data, updated_at = excluded.updated_at')
    .run(id, ex ? ex.owner_id : u.id, JSON.stringify(data), now());
  if (!ex) audit(u, 'meeting.create', data.title, `${data.date} ${data.start}`, ip);
  return [200, { item: meetingOut(u, q('SELECT * FROM meetings WHERE id = ?').get(id)) }];
}
function deleteMeeting(u, id, ip) {
  const ex = q('SELECT * FROM meetings WHERE id = ?').get(id);
  if (!ex || !meetingVisible(u, ex, J(ex.data) || {})) return [404, { error: 'Toplantı bulunamadı.' }];
  if (!(u.role === 'admin' || ex.owner_id === u.id)) return [403, { error: 'Yalnız toplantıyı oluşturan kişi silebilir.' }];
  q('DELETE FROM meetings WHERE id = ?').run(id);
  audit(u, 'meeting.delete', (J(ex.data) || {}).title, '', ip);
  return [200, { ok: true }];
}

/* ================= organisation settings ================= */
const getOrg = () => J((q("SELECT value FROM settings WHERE key = 'org'").get() || {}).value) || {};
function cleanOrg(b) {
  const o = {};
  if (Array.isArray(b.rooms)) o.rooms = b.rooms.slice(0, 100).map(x => str(x, 100)).filter(Boolean);
  if (Array.isArray(b.customHolidays)) o.customHolidays = b.customHolidays.slice(0, 500).filter(h => h && isDate(h.date)).map(h => ({ date: h.date, name: str(h.name, 200) || 'Tatil', half: !!h.half }));
  if (b.companyMap && typeof b.companyMap === 'object') { o.companyMap = {}; for (const [k, v] of Object.entries(b.companyMap).slice(0, 500)) o.companyMap[str(k, 200).toLowerCase()] = str(v, 200); }
  if (b.saturdayWork !== undefined) o.saturdayWork = !!b.saturdayWork;
  return o;
}
const saveOrg = o => q("INSERT INTO settings (key, value) VALUES ('org', ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value").run(JSON.stringify({ ...getOrg(), ...o }));

/* ================= users (admin) ================= */
function publicUser(u) { const r = ROLES[u.role] || ROLES.employee; return { id: u.id, username: u.username, name: u.name, role: u.role, roleLabel: r.label, personId: u.personId, companies: u.companies, sensitive: u.sensitive, mustChange: u.mustChange, active: u.active, lastLogin: u.lastLogin }; }
function permsOut(u) { const p = permsOf(u); return { role: p.role, roleLabel: p.label, peopleRead: p.peopleRead, peopleWrite: p.peopleWrite, leaveRead: p.leaveRead, leaveFor: p.leaveFor, approve: p.approve, users: p.users, audit: p.audit, org: p.org, export: p.export, sensitive: p.sensitive, companies: p.companies, personId: p.personId }; }
const userCount = () => q('SELECT COUNT(*) AS n FROM users').get().n;
const activeAdmins = () => q("SELECT COUNT(*) AS n FROM users WHERE role = 'admin' AND active = 1").get().n;
const USERNAME = /^[a-z0-9][a-z0-9._-]{2,39}$/i;
export function createUser({ name, username, role, personId, companies, sensitive, password, mustChange = true }) {
  const id = uid(), t = now();
  q('INSERT INTO users (id, username, name, role, person_id, companies, sensitive, pass, must_change, active, prefs, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?, ?)')
    .run(id, username, name, ROLES[role] ? role : 'employee', personId || null, JSON.stringify(companies || []), sensitive ? 1 : 0, hashPassword(password), mustChange ? 1 : 0, '{}', t, t);
  return rowUser(q('SELECT * FROM users WHERE id = ?').get(id));
}
function adminUserView(row) {
  const u = rowUser(row);
  const p = u.personId ? getPersonRow(u.personId) : null;
  return { ...publicUser(u), personName: p ? p.name : '', personCompany: p ? p.company : '', sessions: q('SELECT COUNT(*) AS n FROM sessions WHERE user_id = ? AND expires_at > ?').get(u.id, now()).n, createdAt: u.createdAt };
}
function cleanUserInput(b, existing) {
  const out = {};
  if (b.name !== undefined) { out.name = str(b.name, 120).trim(); if (!out.name) return { err: 'Ad soyad boş olamaz.' }; }
  if (b.username !== undefined) { out.username = str(b.username, 40).trim(); if (!USERNAME.test(out.username)) return { err: 'Kullanıcı adı 3–40 karakter olmalı; harf, rakam, nokta, tire ve alt çizgi kullanılabilir.' }; }
  if (b.role !== undefined) { if (!ROLES[b.role]) return { err: 'Geçersiz rol.' }; out.role = b.role; }
  if (b.personId !== undefined) { out.personId = b.personId || null; if (out.personId && !getPersonRow(out.personId)) return { err: 'Bağlanacak personel kaydı bulunamadı.' }; }
  if (b.companies !== undefined) out.companies = Array.isArray(b.companies) ? [...new Set(b.companies.map(c => str(c, 200)).filter(Boolean))].slice(0, 50) : [];
  if (b.sensitive !== undefined) out.sensitive = !!b.sensitive;
  if (b.active !== undefined) out.active = !!b.active;
  if (out.personId) {
    const taken = q('SELECT id FROM users WHERE person_id = ?').get(out.personId);
    if (taken && (!existing || taken.id !== existing.id)) return { err: 'Bu personel kaydı başka bir hesaba bağlı.' };
  }
  return { out };
}
function suggestUsername(p) {
  const local = p.email ? p.email.split('@')[0] : '';
  let base = (local && USERNAME.test(local) ? local : `${fold(p.firstName || p.name)}.${fold(p.lastName || '')}`).toLowerCase().replace(/\.+$/, '').slice(0, 34);
  if (base.length < 3) base = `kullanici${base}`;
  let name = base, i = 2;
  while (q('SELECT 1 FROM users WHERE username = ?').get(name)) name = `${base}${i++}`;
  return name;
}

/* ================= backup ================= */
export function exportAll() {
  return {
    app: 'Finans360', kind: 'server-backup', version: VERSION, exportedAt: now(),
    people: q('SELECT * FROM people').all().map(personData),
    leaves: q('SELECT * FROM leaves').all().map(r => ({ ...(J(r.data) || {}), id: r.id, personId: r.person_id, person: r.person_name, company: r.company, status: r.status, createdBy: r.created_by })),
    meetings: q('SELECT * FROM meetings').all().map(r => ({ ...(J(r.data) || {}), id: r.id, ownerId: r.owner_id })),
    org: getOrg(),
    users: q('SELECT * FROM users').all().map(r => { const u = rowUser(r); return { id: u.id, username: u.username, name: u.name, role: u.role, personId: u.personId, companies: u.companies, sensitive: u.sensitive, active: u.active }; })
  };
}
function importDeviceBackup(u, b, ip) {
  if (!b || !Array.isArray(b.leaves) || !Array.isArray(b.meetings)) return [400, { error: 'Bu dosya bir Finans360 yedeği değil.' }];
  const res = { people: { added: 0, updated: 0 }, leaves: 0, meetings: 0 };
  if (Array.isArray(b.people)) res.people = mergePeople(b.people, u.id);
  const meName = b.profile && b.profile.name;
  tx(() => {
    for (const l of b.leaves) {
      if (!l || !l.id || q('SELECT 1 FROM leaves WHERE id = ?').get(String(l.id))) continue;
      const c = cleanLeave(l); if (c.err) continue;
      let t = { id: null, name: str(l.person, 200), company: '' };
      if (l.person === 'me') { const p = (meName && findPersonByName(meName)) || (u.personId && getPersonRow(u.personId)); t = p ? { id: p.id, name: p.name, company: p.company } : { id: null, name: meName || u.name, company: '' }; }
      else { const p = findPersonByName(l.person); if (p) t = { id: p.id, name: p.name, company: p.company }; }
      const status = STATUSES[l.status] ? l.status : 'pending';
      q('INSERT INTO leaves (id, person_id, person_name, company, status, data, created_by, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)')
        .run(String(l.id), t.id, t.name, t.company || '', status, JSON.stringify({ ...c.d, history: Array.isArray(l.history) ? l.history.slice(-60) : [], createdAt: l.createdAt || now() }), u.id, now());
      res.leaves++;
    }
    for (const m of b.meetings) {
      if (!m || !m.id || q('SELECT 1 FROM meetings WHERE id = ?').get(String(m.id))) continue;
      const c = cleanMeeting(m); if (c.err) continue;
      q('INSERT INTO meetings (id, owner_id, data, updated_at) VALUES (?, ?, ?, ?)').run(String(m.id), u.id, JSON.stringify(c.m), now());
      res.meetings++;
    }
    if (b.settings) saveOrg(cleanOrg(b.settings));
  });
  audit(u, 'backup.import', 'cihaz yedeği', JSON.stringify(res), ip);
  return [200, res];
}

/* ================= HTTP ================= */
const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8', '.json': 'application/json', '.webmanifest': 'application/manifest+json', '.svg': 'image/svg+xml', '.png': 'image/png', '.ico': 'image/x-icon' };
const CSP = "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: blob:; connect-src 'self'; worker-src 'self' blob:; frame-ancestors 'none'; base-uri 'none'; form-action 'self'";
function baseHeaders(req, res) {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('Referrer-Policy', 'no-referrer');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Permissions-Policy', 'camera=(), microphone=(), geolocation=()');
  if (CFG.trustProxy && req.headers['x-forwarded-proto'] === 'https') res.setHeader('Strict-Transport-Security', 'max-age=31536000');
}
const clientIp = req => (CFG.trustProxy && req.headers['x-forwarded-for'] ? String(req.headers['x-forwarded-for']).split(',')[0].trim() : req.socket.remoteAddress || '');
function send(res, code, obj) {
  const body = JSON.stringify(obj);
  res.writeHead(code, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'Content-Length': Buffer.byteLength(body) });
  res.end(body);
}
function readBody(req) {
  return new Promise((ok, bad) => {
    let size = 0; const chunks = [];
    req.on('data', c => { size += c.length; if (size > CFG.maxBody) { bad(Object.assign(new Error('İstek çok büyük.'), { code: 413 })); req.destroy(); } else chunks.push(c); });
    req.on('end', () => { if (!size) return ok({}); const v = J(Buffer.concat(chunks).toString('utf8')); v && typeof v === 'object' ? ok(v) : bad(Object.assign(new Error('Geçersiz JSON.'), { code: 400 })); });
    req.on('error', bad);
  });
}
let indexCache = null;
function serveStatic(req, res, path) {
  let rel = path === '/' ? 'index.html' : decodeURIComponent(path.slice(1));
  if (rel.includes('..') || rel.includes('\0')) { res.writeHead(400); return res.end(); }
  let file = null;
  if (['index.html', 'manifest.webmanifest', 'sw.js'].includes(rel) || /^icons\/[\w.-]+$/.test(rel)) file = join(CFG.webDir, rel);
  else if (/^vendor\/[\w.-]+$/.test(rel)) file = join(CFG.vendorDir, rel.slice(7));
  if (!file || !existsSync(file) || !statSync(file).isFile()) { res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }); return res.end('Bulunamadı'); }
  const type = MIME[extname(file)] || 'application/octet-stream';
  if (rel === 'index.html') {
    // mark the page as served by this server so the app starts in server mode
    if (!indexCache || indexCache.mtime !== statSync(file).mtimeMs) indexCache = { mtime: statSync(file).mtimeMs, body: readFileSync(file, 'utf8').replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="f360-server" content="same-origin">') };
    res.writeHead(200, { 'Content-Type': type, 'Content-Security-Policy': CSP, 'Cache-Control': 'no-cache' });
    return res.end(indexCache.body);
  }
  res.writeHead(200, { 'Content-Type': type, 'Cache-Control': rel === 'sw.js' ? 'no-cache' : 'public, max-age=3600' });
  createReadStream(file).pipe(res);
}

const routes = [];
const route = (method, pattern, handler, opts = {}) => routes.push({ method, re: new RegExp('^' + pattern.replace(/:(\w+)/g, '(?<$1>[\\w.-]{1,80})') + '$'), handler, opts });

route('GET', '/api/health', () => [200, { ok: true, app: 'finans360-server', version: VERSION, setup: userCount() === 0 }], { public: true });
route('POST', '/api/setup', ({ body, ip }) => {
  if (userCount() > 0) return [409, { error: 'Kurulum zaten yapılmış.' }];
  const c = cleanUserInput({ name: body.name, username: body.username }); if (c.err) return [400, { error: c.err }];
  const problem = passwordProblem(body.password, c.out.username); if (problem) return [400, { error: problem }];
  const u = createUser({ ...c.out, role: 'admin', password: body.password, mustChange: false });
  q('UPDATE users SET last_login = ? WHERE id = ?').run(now(), u.id);
  audit(u, 'setup', u.username, 'İlk yönetici hesabı oluşturuldu', ip);
  const token = createSession(u, ip, '');
  return [200, { token, user: publicUser(u), perms: permsOut(u) }];
}, { public: true });
route('POST', '/api/login', ({ body, ip, req }) => {
  const username = str(body.username, 60).trim().toLowerCase(), pw = str(body.password, 300);
  if (isLimited('ip:' + ip) || isLimited('user:' + username)) return [429, { error: 'Çok fazla hatalı deneme. 15 dakika sonra tekrar deneyin.' }];
  const row = username ? q('SELECT * FROM users WHERE username = ?').get(username) : null;
  const ok = checkPassword(pw, row ? row.pass : DUMMY_HASH);
  if (!row || !ok || !row.active) {
    noteFail('ip:' + ip); noteFail('user:' + username);
    audit(row ? rowUser(row) : null, 'login.fail', username, row && !row.active ? 'pasif hesap' : '', ip);
    return [401, { error: row && ok && !row.active ? 'Hesabınız devre dışı. Yöneticinize başvurun.' : 'Kullanıcı adı ya da şifre hatalı.' }];
  }
  attempts.delete('user:' + username);
  q('UPDATE users SET last_login = ? WHERE id = ?').run(now(), row.id);
  const u = rowUser(row);
  const token = createSession(u, ip, req.headers['user-agent']);
  audit(u, 'login', u.username, '', ip);
  return [200, { token, user: publicUser(u), perms: permsOut(u), mustChange: u.mustChange }];
}, { public: true });
route('POST', '/api/logout', ({ u }) => { q('DELETE FROM sessions WHERE id = ?').run(u.sid); return [200, { ok: true }]; }, { allowMustChange: true });
route('GET', '/api/me', ({ u }) => [200, { user: publicUser(u), perms: permsOut(u), prefs: u.prefs }], { allowMustChange: true });
route('POST', '/api/me/password', ({ u, body, ip }) => {
  const row = q('SELECT * FROM users WHERE id = ?').get(u.id);
  if (!checkPassword(str(body.current, 300), row.pass)) return [400, { error: 'Mevcut şifre yanlış.' }];
  const problem = passwordProblem(body.next, u.username); if (problem) return [400, { error: problem }];
  if (body.next === body.current) return [400, { error: 'Yeni şifre eskisiyle aynı olamaz.' }];
  q('UPDATE users SET pass = ?, must_change = 0, updated_at = ? WHERE id = ?').run(hashPassword(body.next), now(), u.id);
  q('DELETE FROM sessions WHERE user_id = ? AND id <> ?').run(u.id, u.sid);
  audit(u, 'password.change', u.username, '', ip);
  return [200, { ok: true }];
}, { allowMustChange: true });
route('PUT', '/api/me/prefs', ({ u, body }) => {
  const prefs = { ...u.prefs }; for (const k of ['sicil', 'manager', 'managerContact']) if (body[k] !== undefined) prefs[k] = str(body[k], 200);
  q('UPDATE users SET prefs = ?, updated_at = ? WHERE id = ?').run(JSON.stringify(prefs), now(), u.id);
  return [200, { prefs }];
});
route('GET', '/api/me/sessions', ({ u }) => [200, { sessions: q('SELECT id, created_at, last_seen, ip, ua FROM sessions WHERE user_id = ? AND expires_at > ? ORDER BY last_seen DESC').all(u.id, now()).map(s => ({ id: s.id.slice(0, 12), createdAt: s.created_at, lastSeen: s.last_seen, ip: s.ip, ua: s.ua, current: s.id === u.sid })) }], { allowMustChange: true });
route('POST', '/api/me/sessions/close-others', ({ u, ip }) => { const n = q('DELETE FROM sessions WHERE user_id = ? AND id <> ?').run(u.id, u.sid).changes; audit(u, 'sessions.close', u.username, `${n} oturum`, ip); return [200, { closed: n }]; });

route('GET', '/api/bootstrap', ({ u }) => {
  const peopleRows = q('SELECT * FROM people ORDER BY name').all();
  return [200, {
    version: VERSION, user: publicUser(u), perms: permsOut(u), prefs: u.prefs, org: getOrg(),
    people: peopleRows.map(r => personOut(u, r)),
    leaves: q('SELECT * FROM leaves').all().filter(r => leaveVisible(u, r)).map(r => leaveOut(u, r)),
    meetings: q('SELECT * FROM meetings').all().filter(r => meetingVisible(u, r, J(r.data) || {})).map(r => meetingOut(u, r)),
    companies: [...new Set(peopleRows.map(r => r.company).filter(Boolean))].sort((a, b) => a.localeCompare(b, 'tr')),
    roles: Object.fromEntries(Object.entries(ROLES).map(([k, v]) => [k, v]))
  }];
});
route('PUT', '/api/leaves/:id', ({ u, body, params, ip }) => putLeave(u, params.id, body, ip));
route('DELETE', '/api/leaves/:id', ({ u, params, ip }) => deleteLeave(u, params.id, ip));
route('PUT', '/api/meetings/:id', ({ u, body, params, ip }) => putMeeting(u, params.id, body, ip));
route('DELETE', '/api/meetings/:id', ({ u, params, ip }) => deleteMeeting(u, params.id, ip));
route('PUT', '/api/org', ({ u, body, ip }) => {
  if (!permsOf(u).org) return [403, { error: 'Kurum ayarlarını yalnız yönetici değiştirebilir.' }];
  saveOrg(cleanOrg(body)); audit(u, 'org.update', 'kurum ayarları', '', ip);
  return [200, { org: getOrg() }];
});
route('PUT', '/api/people/:id', ({ u, body, params, ip }) => {
  if (permsOf(u).peopleWrite !== 'all') return [403, { error: 'Personel kayıtlarını yalnız yönetici değiştirebilir.' }];
  const ex = getPersonRow(params.id), prev = ex ? personData(ex) : {};
  const next = { ...prev, ...cleanPerson(body, false) };
  delete next.id;
  next.name = str(next.name, 200).trim() || [next.firstName, next.lastName].filter(Boolean).join(' ');
  if (!next.name) return [400, { error: 'Ad soyad boş olamaz.' }];
  if (body.sensitive && typeof body.sensitive === 'object') { const s = cleanPerson(body.sensitive, true); for (const k of SENSITIVE) if (body.sensitive[k] !== undefined) next[k] = s[k]; }
  const dup = findPersonByName(next.name); if (dup && dup.id !== params.id) return [409, { error: `${dup.name} zaten kayıtlı.` }];
  tx(() => { savePerson(params.id, next, u.id); if (ex) renamePersonRefs(params.id, prev.name, next.name, next.company); });
  audit(u, ex ? 'person.update' : 'person.create', next.name, body.sensitive ? 'hassas alanlar dahil' : '', ip);
  return [200, { item: personOut(u, getPersonRow(params.id)) }];
});
route('DELETE', '/api/people/:id', ({ u, params, ip }) => {
  if (permsOf(u).peopleWrite !== 'all') return [403, { error: 'Personel kayıtlarını yalnız yönetici silebilir.' }];
  const ex = getPersonRow(params.id); if (!ex) return [404, { error: 'Kayıt bulunamadı.' }];
  tx(() => { q('DELETE FROM people WHERE id = ?').run(params.id); q('UPDATE users SET person_id = NULL WHERE person_id = ?').run(params.id); });
  audit(u, 'person.delete', ex.name, '', ip);
  return [200, { ok: true }];
});
route('GET', '/api/people/:id/sensitive', ({ u, params, ip }) => {
  const ex = getPersonRow(params.id); if (!ex) return [404, { error: 'Kayıt bulunamadı.' }];
  const p = personData(ex), own = p.id === u.personId;
  if (personAccess(u, p) !== 'full' || (!own && !permsOf(u).sensitive)) return [403, { error: 'Hassas bilgileri görme yetkiniz yok.' }];
  audit(u, 'person.sensitive', p.name, own ? 'kendi kaydı' : 'TC, kan grubu, adres görüntülendi', ip);
  return [200, { tc: p.tc || '', blood: p.blood || '', address: p.address || '' }];
});
route('POST', '/api/people/import', ({ u, body, ip }) => {
  if (permsOf(u).peopleWrite !== 'all') return [403, { error: 'Toplu içe aktarma yalnız yönetici içindir.' }];
  if (!Array.isArray(body.people)) return [400, { error: 'Kişi listesi bulunamadı.' }];
  const res = mergePeople(body.people.slice(0, 5000), u.id);
  if (body.companyMap && typeof body.companyMap === 'object') saveOrg({ companyMap: { ...(getOrg().companyMap || {}), ...cleanOrg({ companyMap: body.companyMap }).companyMap } });
  audit(u, 'people.import', `${body.people.length} kayıt`, JSON.stringify(res), ip);
  return [200, res];
});

const adminOnly = h => ctx => (permsOf(ctx.u).users ? h(ctx) : [403, { error: 'Bu işlem yalnız yöneticiler içindir.' }]);
route('GET', '/api/admin/users', adminOnly(() => [200, { users: q('SELECT * FROM users ORDER BY name').all().map(adminUserView) }]));
route('POST', '/api/admin/users', adminOnly(({ u, body, ip }) => {
  const c = cleanUserInput({ name: body.name, username: body.username, role: body.role || 'employee', personId: body.personId || null, companies: body.companies || [], sensitive: !!body.sensitive });
  if (c.err) return [400, { error: c.err }];
  if (q('SELECT 1 FROM users WHERE username = ?').get(c.out.username)) return [409, { error: 'Bu kullanıcı adı kullanılıyor.' }];
  const pw = tempPassword();
  const nu = createUser({ ...c.out, password: pw, mustChange: true });
  audit(u, 'user.create', nu.username, `${ROLES[nu.role].label}`, ip);
  return [200, { user: adminUserView(q('SELECT * FROM users WHERE id = ?').get(nu.id)), tempPassword: pw }];
}));
route('PUT', '/api/admin/users/:id', adminOnly(({ u, body, params, ip }) => {
  const row = q('SELECT * FROM users WHERE id = ?').get(params.id); if (!row) return [404, { error: 'Kullanıcı bulunamadı.' }];
  const cur = rowUser(row);
  const c = cleanUserInput(body, cur); if (c.err) return [400, { error: c.err }];
  const o = c.out;
  if (o.username && o.username.toLowerCase() !== cur.username.toLowerCase() && q('SELECT 1 FROM users WHERE username = ?').get(o.username)) return [409, { error: 'Bu kullanıcı adı kullanılıyor.' }];
  const losesAdmin = cur.role === 'admin' && cur.active && ((o.role && o.role !== 'admin') || o.active === false);
  if (losesAdmin && activeAdmins() <= 1) return [400, { error: 'Son aktif yöneticinin yetkisi kaldırılamaz.' }];
  if (cur.id === u.id && o.active === false) return [400, { error: 'Kendi hesabınızı devre dışı bırakamazsınız.' }];
  const next = { ...cur, ...o };
  q('UPDATE users SET username = ?, name = ?, role = ?, person_id = ?, companies = ?, sensitive = ?, active = ?, updated_at = ? WHERE id = ?')
    .run(next.username, next.name, next.role, next.personId || null, JSON.stringify(next.companies || []), next.sensitive ? 1 : 0, next.active ? 1 : 0, now(), cur.id);
  if (!next.active) q('DELETE FROM sessions WHERE user_id = ?').run(cur.id);
  const changes = Object.keys(o).filter(k => JSON.stringify(o[k]) !== JSON.stringify(cur[k]));
  audit(u, 'user.update', next.username, changes.join(', '), ip);
  return [200, { user: adminUserView(q('SELECT * FROM users WHERE id = ?').get(cur.id)) }];
}));
route('POST', '/api/admin/users/:id/reset-password', adminOnly(({ u, params, ip }) => {
  const row = q('SELECT * FROM users WHERE id = ?').get(params.id); if (!row) return [404, { error: 'Kullanıcı bulunamadı.' }];
  const pw = tempPassword();
  q('UPDATE users SET pass = ?, must_change = 1, updated_at = ? WHERE id = ?').run(hashPassword(pw), now(), row.id);
  q('DELETE FROM sessions WHERE user_id = ?').run(row.id);
  audit(u, 'user.reset', row.username, '', ip);
  return [200, { tempPassword: pw }];
}));
route('POST', '/api/admin/users/:id/logout', adminOnly(({ u, params, ip }) => {
  const n = q('DELETE FROM sessions WHERE user_id = ?').run(params.id).changes;
  audit(u, 'user.logout', params.id, `${n} oturum`, ip);
  return [200, { closed: n }];
}));
route('DELETE', '/api/admin/users/:id', adminOnly(({ u, params, ip }) => {
  const row = q('SELECT * FROM users WHERE id = ?').get(params.id); if (!row) return [404, { error: 'Kullanıcı bulunamadı.' }];
  if (row.id === u.id) return [400, { error: 'Kendi hesabınızı silemezsiniz.' }];
  if (row.role === 'admin' && row.active && activeAdmins() <= 1) return [400, { error: 'Son aktif yönetici silinemez.' }];
  q('DELETE FROM users WHERE id = ?').run(row.id);
  audit(u, 'user.delete', row.username, '', ip);
  return [200, { ok: true }];
}));
route('POST', '/api/admin/users/bulk', adminOnly(({ u, body, ip }) => {
  const role = ROLES[body.role] ? body.role : 'employee';
  const ids = Array.isArray(body.personIds) ? body.personIds.slice(0, 1000) : [];
  const created = [];
  tx(() => {
    for (const pid of ids) {
      const pr = getPersonRow(pid); if (!pr || q('SELECT 1 FROM users WHERE person_id = ?').get(pid)) continue;
      const p = personData(pr), pw = tempPassword(), username = suggestUsername(p);
      createUser({ name: p.name, username, role, personId: pid, companies: role === 'manager' && p.company ? [p.company] : [], sensitive: false, password: pw, mustChange: true });
      created.push({ name: p.name, company: p.company || '', username, tempPassword: pw });
    }
  });
  audit(u, 'user.bulk', `${created.length} hesap`, ROLES[role].label, ip);
  return [200, { created }];
}));
route('GET', '/api/admin/audit', adminOnly(({ url }) => {
  const limit = Math.max(1, Math.min(500, +url.searchParams.get('limit') || 100));
  const before = +url.searchParams.get('before') || 0, action = str(url.searchParams.get('action'), 40);
  const rows = q(`SELECT * FROM audit WHERE (? = 0 OR id < ?) AND (? = '' OR action LIKE ? || '%') ORDER BY id DESC LIMIT ?`).all(before, before, action, action, limit);
  return [200, { items: rows }];
}));
route('GET', '/api/admin/export', adminOnly(({ u, ip }) => { audit(u, 'backup.export', 'sunucu yedeği', '', ip); return [200, exportAll()]; }));
route('POST', '/api/admin/import-backup', adminOnly(({ u, body, ip }) => importDeviceBackup(u, body.backup, ip)));

export async function handle(req, res) {
  baseHeaders(req, res);
  const url = new URL(req.url, 'http://x');
  const path = url.pathname, ip = clientIp(req);
  if (!path.startsWith('/api/')) {
    if (req.method !== 'GET' && req.method !== 'HEAD') { res.writeHead(405); return res.end(); }
    return serveStatic(req, res, path);
  }
  // Bearer tokens only (no cookies), so cross-origin use from the Android app is safe to allow.
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Headers', 'Authorization, Content-Type');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Max-Age', '600');
  if (req.method === 'OPTIONS') { res.writeHead(204); return res.end(); }
  const r = routes.find(x => x.method === req.method && x.re.test(path));
  if (!r) return send(res, 404, { error: 'Bulunamadı.' });
  try {
    const params = path.match(r.re).groups || {};
    const body = req.method === 'POST' || req.method === 'PUT' ? await readBody(req) : {};
    let u = null;
    if (!r.opts.public) {
      u = authUser(req);
      if (!u) return send(res, 401, { error: 'Oturum açmanız gerekiyor.', code: 'unauthenticated' });
      if (u.mustChange && !r.opts.allowMustChange) return send(res, 403, { error: 'Devam etmeden önce şifrenizi değiştirin.', code: 'must_change' });
    }
    const [code, out] = await r.handler({ req, url, params, body, u, ip });
    send(res, code, out);
  } catch (e) {
    if (e.code === 413 || e.code === 400) return send(res, e.code, { error: e.message });
    console.error(new Date().toISOString(), req.method, path, e);
    send(res, 500, { error: 'Sunucu hatası. Kayıt yapılamadı; tekrar deneyin.' });
  }
}

/* ================= CLI & start ================= */
const [cmd, arg, arg2] = process.argv.slice(2);
const isMain = process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain && cmd === 'create-admin') {
  if (!arg || !USERNAME.test(arg)) { console.error('Kullanım: node server.js create-admin <kullanici-adi> ["Ad Soyad"]'); process.exit(1); }
  if (q('SELECT 1 FROM users WHERE username = ?').get(arg)) { console.error('Bu kullanıcı adı zaten var. Şifre sıfırlamak için: node server.js reset-password ' + arg); process.exit(1); }
  const pw = tempPassword();
  const u = createUser({ name: arg2 || arg, username: arg, role: 'admin', password: pw, mustChange: true });
  audit(null, 'cli.create-admin', u.username, '', 'cli');
  console.log(`Yönetici oluşturuldu: ${u.username}\nTek kullanımlık şifre: ${pw}\nİlk girişte yeni şifre belirlenecek.`);
  process.exit(0);
} else if (isMain && cmd === 'reset-password') {
  const row = arg ? q('SELECT * FROM users WHERE username = ?').get(arg) : null;
  if (!row) { console.error('Kullanıcı bulunamadı.'); process.exit(1); }
  const pw = tempPassword();
  q('UPDATE users SET pass = ?, must_change = 1, active = 1, updated_at = ? WHERE id = ?').run(hashPassword(pw), now(), row.id);
  q('DELETE FROM sessions WHERE user_id = ?').run(row.id);
  audit(null, 'cli.reset-password', row.username, '', 'cli');
  console.log(`Yeni tek kullanımlık şifre (${row.username}): ${pw}`);
  process.exit(0);
} else if (isMain && cmd === 'backup') {
  const file = resolve(arg || `finans360-yedek-${now().slice(0, 10)}.json`);
  writeFileSync(file, JSON.stringify(exportAll(), null, 1), { mode: 0o600 });
  audit(null, 'cli.backup', file, '', 'cli');
  console.log(`Yedek yazıldı: ${file}`);
  process.exit(0);
} else if (isMain) {
  setInterval(() => q('DELETE FROM sessions WHERE expires_at < ?').run(now()), 3600000).unref();
  const server = http.createServer((req, res) => { handle(req, res).catch(e => { console.error(e); try { send(res, 500, { error: 'Sunucu hatası.' }); } catch { /* closed */ } }); });
  server.listen(CFG.port, CFG.host, () => console.log(`Finans360 sunucusu ${VERSION} · http://${CFG.host}:${CFG.port} · veri: ${DB_PATH}${userCount() ? '' : ' · ilk açılışta yönetici hesabını oluşturun'}`));
  const stop = () => { server.close(() => { db.close(); process.exit(0); }); setTimeout(() => process.exit(0), 3000).unref(); };
  process.on('SIGTERM', stop); process.on('SIGINT', stop);
}
