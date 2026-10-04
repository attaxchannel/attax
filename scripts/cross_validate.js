#!/usr/bin/env node
/*
 * cross_validate.js — independent second-opinion validation of every project.
 *
 * Uses a separate runtime/parser from scripts/validate_json.py, so a bug in one
 * path is very unlikely to be mirrored in the other.
 *
 * Discovers any top-level directory containing character/*.json and
 * lorebook/*.json, then checks:
 *   1. Both files parse.
 *   2. Character card V2 envelope and required string fields.
 *   3. Lorebook is native World Info with >= 15 entries.
 *   4. Every lorebook entry has the ST entry schema.
 *   5. Dialogue macros and first_mes hygiene.
 *   6. No markdown fences / placeholders.
 *
 * Exit 0 on success, 1 on any failure.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const failures = [];
const notes = [];

function check(label, condition, detail) {
  const line = '  ' + (condition ? 'OK  ' : 'FAIL') + ' ' + label +
    (detail ? ' — ' + detail : '');
  if (condition) notes.push(line); else failures.push(line);
}

const V2_REQUIRED = ['name', 'description', 'personality', 'scenario', 'first_mes',
  'mes_example', 'creator_notes', 'system_prompt', 'post_history_instructions'];

const ENTRY_FIELDS = ['uid', 'key', 'keysecondary', 'comment', 'content', 'constant',
  'selective', 'selectiveLogic', 'order', 'position', 'disable', 'depth',
  'probability', 'useProbability', 'group', 'groupWeight', 'role'];

function firstJson(dir) {
  if (!fs.existsSync(dir)) return null;
  const name = fs.readdirSync(dir).filter((f) => f.endsWith('.json')).sort()[0];
  return name ? path.join(dir, name) : null;
}

function validateProject(proj) {
  const cardPath = firstJson(path.join(ROOT, proj, 'character'));
  const lorePath = firstJson(path.join(ROOT, proj, 'lorebook'));

  let card = null;
  let lore = null;
  try {
    card = JSON.parse(fs.readFileSync(cardPath, 'utf8'));
    notes.push(`  [${proj}] OK   character json parsed by Node`);
  } catch (e) {
    failures.push(`  [${proj}] FAIL character json — ${e.message}`);
  }
  try {
    lore = JSON.parse(fs.readFileSync(lorePath, 'utf8'));
    notes.push(`  [${proj}] OK   lorebook json parsed by Node`);
  } catch (e) {
    failures.push(`  [${proj}] FAIL lorebook json — ${e.message}`);
  }
  if (!card || !lore) return;

  check(`[${proj}] spec is chara_card_v2`, card.spec === 'chara_card_v2', String(card.spec));
  check(`[${proj}] spec_version is 2.0`, card.spec_version === '2.0', String(card.spec_version));
  const data = card.data || {};
  V2_REQUIRED.forEach((k) => {
    const v = data[k];
    check(`[${proj}] data.${k} non-empty string`,
      typeof v === 'string' && v.trim().length > 0,
      typeof v === 'string' ? v.length + ' chars' : String(v));
  });
  const ag = data.alternate_greetings || [];
  check(`[${proj}] alternate_greetings is string array`,
    Array.isArray(ag) && ag.every((s) => typeof s === 'string'), `${ag.length} greetings`);
  const tags = data.tags || [];
  check(`[${proj}] tags is string array`,
    Array.isArray(tags) && tags.every((s) => typeof s === 'string'), `${tags.length} tags`);

  const entries = lore.entries;
  check(`[${proj}] lorebook.entries is plain object`,
    !!entries && typeof entries === 'object' && !Array.isArray(entries));
  if (!entries) return;
  const uids = Object.keys(entries);
  check(`[${proj}] lorebook has at least 15 entries`, uids.length >= 15, `${uids.length} entries`);

  let bad = 0;
  const problems = [];
  uids.forEach((uid) => {
    const e = entries[uid];
    ENTRY_FIELDS.forEach((f) => { if (!(f in e)) { problems.push(`${uid}:missing ${f}`); bad += 1; } });
    if (!Array.isArray(e.key) || e.key.some((k) => typeof k !== 'string')) { problems.push(`${uid}:key`); bad += 1; }
    if (!Array.isArray(e.keysecondary)) { problems.push(`${uid}:keysecondary`); bad += 1; }
    if (typeof e.content !== 'string' || !e.content.trim()) { problems.push(`${uid}:empty content`); bad += 1; }
    if (Number(uid) !== e.uid) { problems.push(`${uid}:uid mismatch`); bad += 1; }
    if ([0, 1, 2, 3, 4, 5, 6, 7].indexOf(e.position) === -1) { problems.push(`${uid}:position enum`); bad += 1; }
    if ([0, 1, 2, 3].indexOf(e.selectiveLogic) === -1) { problems.push(`${uid}:selectiveLogic enum`); bad += 1; }
  });
  check(`[${proj}] every entry matches ST entry schema`, bad === 0,
    bad === 0 ? `all ${uids.length} entries` : problems.slice(0, 5).join('; '));

  const mes = data.mes_example || '';
  check(`[${proj}] mes_example uses <START>`, (mes.match(/<START>/g) || []).length >= 3);
  check(`[${proj}] mes_example uses {{user}}/{{char}}`,
    mes.indexOf('{{user}}') !== -1 && mes.indexOf('{{char}}') !== -1);
  const first = data.first_mes || '';
  check(`[${proj}] first_mes does not write {{user}} lines`, first.indexOf('{{user}}:') === -1);
  check(`[${proj}] first_mes does not dictate user actions`,
    !/\byou (say|reply|answer|respond|step|walk|decide)\b/i.test(first));

  const blob = JSON.stringify(card) + JSON.stringify(lore);
  check(`[${proj}] no markdown fences`, blob.indexOf('```') === -1);
  check(`[${proj}] no TODO/FIXME/PLACEHOLDER`,
    !/\bTODO\b|\bFIXME\b|\bPLACEHOLDER\b/.test(blob));
}

const projects = fs.readdirSync(ROOT).filter((n) => {
  const d = path.join(ROOT, n);
  return fs.statSync(d).isDirectory() &&
    fs.existsSync(path.join(d, 'character')) &&
    fs.existsSync(path.join(d, 'lorebook'));
});

if (!projects.length) {
  console.log('no projects found');
  process.exit(1);
}

projects.forEach(validateProject);

console.log(`cross_validate.js — Node ${process.version}`);
console.log(notes.join('\n'));
if (failures.length) {
  console.log('');
  console.log(failures.join('\n'));
}
console.log('');
console.log(`${notes.length} checks passed, ${failures.length} failed`);
process.exit(failures.length === 0 ? 0 : 1);