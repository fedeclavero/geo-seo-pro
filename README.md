# GEO-SEO Pro — Claude Code Skill

**Generative Engine Optimization + SEO Tradicional — Habilidad Unificada para Claude Code**

Skill completa y autocontenida que cubre CADA aspecto de la optimización para motores de búsqueda tradicionales y generativos. Basada en investigación académica de Princeton (GEO-bench, KDD 2024), documentación oficial de Google, y el ecosistema de IA conversacional.

---

## 🎯 Capacidades

| Área | Cobertura |
|------|-----------|
| **SEO Tradicional** | 128+ factores de ranking organizados en 8 categorías |
| **Core Web Vitals** | LCP, INP, CLS — rangos, optimización quirúrgica, diagnóstico |
| **E-E-A-T** | Experience, Expertise, Authoritativeness, Trustworthiness + Who/How/Why |
| **Schema JSON-LD** | 7 esquemas clave + sameAs + riesgos de solapamiento |
| **GEO + RAG** | Arquitectura RAG 3-capas, AEO vs GEO |
| **Princeton GEO-bench** | 5 estrategias ganadoras (+25-40%), 4 tácticas fallidas, Underdog Effect |
| **llms.txt** | Especificación completa, HTTP headers, .well-known |
| **Crawlers IA** | Configuración robots.txt para 10+ crawlers (GPTBot, ClaudeBot, PerplexityBot...) |
| **Seguridad** | Anti prompt-injection, CI/CD pipelines, hash monitoring |

---

## 📦 Instalación

```bash
npx geo-seo-pro-install
```

O manualmente:

```bash
git clone https://github.com/fedeclavero/geo-seo-pro.git
mkdir -p ~/.claude/skills/geo-seo-pro
cp geo-seo-pro/SKILL.md ~/.claude/skills/geo-seo-pro/
```

---

## 🚀 Uso en Claude Code

```
/geo-seo-pro audit <url>          — Auditoría completa SEO + GEO
/geo-seo-pro seo-factors <url>    — Análisis de 128+ factores SEO
/geo-seo-pro core-web-vitals <url> — Análisis LCP/INP/CLS
/geo-seo-pro e-e-a-t <url>        — Evaluación E-E-A-T y Helpful Content
/geo-seo-pro schema <url>         — Auditoría y generación JSON-LD
/geo-seo-pro geo <url>            — Análisis GEO (Princeton + citabilidad)
/geo-seo-pro llmstxt <url>        — Generar/analizar llms.txt
/geo-seo-pro crawlers <url>       — Configurar acceso crawlers IA
/geo-seo-pro content <url>        — Optimizar contenido para RAG
/geo-seo-pro report <url>         — Informe completo cliente
```

---

## 📚 Fuente de la Investigación

Esta skill se basa en el documento "Arquitectura de Optimización de Búsqueda de Siguiente Generación: Análisis Técnico Multidimensional de Parámetros SEO Tradicionales, AEO, GEO y Protocolos de Interfaz para Modelos de Lenguaje", que sintetiza:

- Backlinko — Google's 200 Ranking Factors (2026)
- Princeton University / Georgia Tech / Allen Institute for AI — GEO-bench (KDD 2024)
- Google Search Central — Core Web Vitals, Helpful Content, E-E-A-T
- DerivateX — llms.txt Guide, Princeton GEO Paper
- LangSync — Schema Structured Data for AI Search

---

## 🔒 Seguridad

La skill incluye protocolos de:
- Prevención de inyección indirecta de prompts en llms.txt
- Gobernanza mediante pipelines CI/CD
- Autenticación de acceso para documentación privada
- Monitorización de integridad (hash MD5/SHA256)

---

## 📄 Licencia

MIT
