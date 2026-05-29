#!/bin/bash
# GEO-SEO Pro Skill Installer
# Usage: npx geo-seo-pro-install
set -e

SKILL_DIR="$HOME/.claude/skills/geo-seo-pro"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

echo "╔══════════════════════════════════════╗"
echo "║   GEO-SEO Pro Skill Installer       ║"
echo "║   Generative Engine Optimization    ║"
echo "╚══════════════════════════════════════╝"
echo ""

mkdir -p "$SKILL_DIR"
cp "$REPO_DIR/SKILL.md" "$SKILL_DIR/"
echo "✅ Instalado en $SKILL_DIR"
echo ""
echo "Uso en Claude Code:"
echo "  /geo-seo-pro audit <url>          — Auditoría completa SEO + GEO"
echo "  /geo-seo-pro seo-factors <url>    — Análisis 128+ factores SEO"
echo "  /geo-seo-pro core-web-vitals <url> — Análisis LCP/INP/CLS"
echo "  /geo-seo-pro e-e-a-t <url>        — Evaluación E-E-A-T"
echo "  /geo-seo-pro schema <url>         — Auditoría JSON-LD"
echo "  /geo-seo-pro geo <url>            — Análisis GEO con Princeton"
echo "  /geo-seo-pro llmstxt <url>        — Generar llms.txt"
echo "  /geo-seo-pro crawlers <url>       — Configurar crawlers IA"
echo "  /geo-seo-pro content <url>        — Optimizar para RAG"
echo "  /geo-seo-pro report <url>         — Informe completo"
