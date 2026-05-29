#!/usr/bin/env node
// GEO-SEO Pro Skill Installer for Claude Code
// Usage: npx geo-seo-pro-install

const fs = require('fs');
const path = require('path');

const SKILL_DIR = path.join(process.env.HOME, '.claude', 'skills', 'geo-seo-pro');
const SRC_SKILL = path.join(__dirname, '..', 'SKILL.md');

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
  console.log('  /geo-seo-pro audit <url>          — Full SEO + GEO audit');
  console.log('  /geo-seo-pro seo-factors <url>    — 128+ ranking factors checklist');
  console.log('  /geo-seo-pro core-web-vitals <url> — LCP/INP/CLS analysis');
  console.log('  /geo-seo-pro e-e-a-t <url>        — E-E-A-T assessment');
  console.log('  /geo-seo-pro schema <url>         — JSON-LD audit & generation');
  console.log('  /geo-seo-pro geo <url>            — GEO analysis with Princeton');
  console.log('  /geo-seo-pro llmstxt <url>        — Generate llms.txt');
  console.log('  /geo-seo-pro crawlers <url>       — Configure AI crawler access');
  console.log('  /geo-seo-pro content <url>        — Optimize content for RAG');
  console.log('  /geo-seo-pro report <url>         — Complete client report');
} catch (err) {
  console.error('❌ Installation failed:', err.message);
  process.exit(1);
}
