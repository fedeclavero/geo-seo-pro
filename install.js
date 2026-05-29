#!/usr/bin/env node
// GEO-SEO Pro Skill Installer for Claude Code
// Usage: npx geo-seo-pro-install

const fs = require('fs');
const path = require('path');

const SKILL_DIR = path.join(process.env.HOME || require('os').homedir(), '.claude', 'skills', 'geo-seo-pro');
const SRC_SKILL = path.join(__dirname, 'SKILL.md');

console.log('╔══════════════════════════════════════╗');
console.log('║   GEO-SEO Pro Skill Installer       ║');
console.log('║   Generative Engine Optimization    ║');
console.log('╚══════════════════════════════════════╝');
console.log('');

try {
  fs.mkdirSync(SKILL_DIR, { recursive: true });
  fs.copyFileSync(SRC_SKILL, path.join(SKILL_DIR, 'SKILL.md'));
  console.log(`✅ Installed to ${SKILL_DIR}`);
  console.log('');
  console.log('Usage in Claude Code:');
  console.log('  /geo-seo-pro              — Interactive guided analysis');
  console.log('  /geo-seo-pro audit <url>  — Full SEO + GEO audit');
  console.log('  /geo-seo-pro geo <url>    — AI visibility optimization');
  console.log('  /geo-seo-pro report <url> — Complete client report');
} catch (err) {
  console.error('❌ Installation failed:', err.message);
  process.exit(1);
}
