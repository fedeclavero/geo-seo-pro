#!/usr/bin/env node
// GEO-SEO Pro Skill Installer for Claude Code
// Installs main skill, sub-skills, and scripts
// Usage: npx geo-seo-pro-install

const fs = require('fs');
const path = require('path');

const SKILL_DIR = path.join(process.env.HOME || require('os').homedir(), '.claude', 'skills', 'geo-seo-pro');
const BASE_DIR = __dirname;

console.log('╔══════════════════════════════════════╗');
console.log('║   GEO-SEO Pro Skill Installer       ║');
console.log('║   Generative Engine Optimization    ║');
console.log('╚══════════════════════════════════════╝');
console.log('');

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

try {
  // Install main skill
  fs.mkdirSync(SKILL_DIR, { recursive: true });
  fs.copyFileSync(path.join(BASE_DIR, 'SKILL.md'), path.join(SKILL_DIR, 'SKILL.md'));
  console.log('✅ Main skill installed');

  // Install sub-skills
  const subSkillsSrc = path.join(BASE_DIR, 'skills');
  const subSkillsDest = path.join(SKILL_DIR, 'skills');
  if (fs.existsSync(subSkillsSrc)) {
    copyDir(subSkillsSrc, subSkillsDest);
    const count = fs.readdirSync(subSkillsSrc).length;
    console.log(`✅ ${count} sub-skills installed`);
  }

  // Install scripts
  const scriptsSrc = path.join(BASE_DIR, 'scripts');
  const scriptsDest = path.join(SKILL_DIR, 'scripts');
  if (fs.existsSync(scriptsSrc)) {
    copyDir(scriptsSrc, scriptsDest);
    // Make Python scripts executable
    for (const f of fs.readdirSync(scriptsDest)) {
      if (f.endsWith('.py')) {
        fs.chmodSync(path.join(scriptsDest, f), 0o755);
      }
    }
    const count = fs.readdirSync(scriptsDest).filter(f => f.endsWith('.py')).length;
    console.log(`✅ ${count} measurement scripts installed`);
  }

  console.log('');
  console.log('Usage in Claude Code:');
  console.log('  /geo-seo-pro              — Interactive guided analysis');
  console.log('  /geo-seo-pro geo <url>    — AI visibility optimization');
  console.log('  /geo-seo-pro report <url> — Complete PDF report');
} catch (err) {
  console.error('❌ Installation failed:', err.message);
  process.exit(1);
}
