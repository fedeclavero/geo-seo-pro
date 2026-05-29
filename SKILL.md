---
name: geo-seo-pro
description: >
  GEO-SEO Pro — Herramienta de análisis de posicionamiento para buscadores tradicionales
  (Google) y motores de IA (ChatGPT, Perplexity, Gemini, Claude). Ejecuta mediciones reales
  con PageSpeed Insights API, parseo de robots.txt, validación de llms.txt, detección de
  JSON-LD, y scoring GEO basado en Princeton GEO-bench (KDD 2024). Arquitectura modular:
  cada análisis carga solo el contexto que necesita. Informes PDF descargables en español.
  Use cuando el usuario diga "geo", "seo", "geo seo pro", "posicionamiento IA", "AI search",
  "optimizar sitio", "auditar web", o escriba una URL para analizar.
allowed-tools: Read, Bash, WebFetch, WebSearch, Write, Edit, Grep, Glob
---

# GEO-SEO Pro — Análisis de Posicionamiento para Google + IA

> **Lo que esta herramienta realmente hace:** analiza los factores que impactan tu posicionamiento en buscadores tradicionales y motores de IA, obtiene métricas reales mediante APIs y scripts, y genera recomendaciones priorizadas con PDF descargable en español.

---

## 🤖 Protocolo Interactivo

Cuando el usuario escriba `/geo-seo-pro`:

### Paso 1 — Bienvenida y URL

```markdown
# 🚀 GEO-SEO Pro

Analizo los factores que impactan tu visibilidad en Google, ChatGPT, Perplexity,
Gemini y Claude. Mis mediciones usan APIs y scripts reales — no estimaciones.
Todo en español, con informe PDF descargable.

**¿Qué URL querés analizar?**
```

Si el usuario ya pasó una URL (`/geo-seo-pro https://ejemplo.com`), continuar al Paso 2.

### Paso 2 — Elegir enfoque

Usar `AskUserQuestion`:

```
Header: "Análisis"
Pregunta: "¿Qué querés analizar de <dominio>?"
Opciones:
  - "🔍 Análisis completo (recomendado)" → Ejecutar Paso 3 con TODOS los módulos
  - "📈 Visibilidad en IA (ChatGPT, Perplexity...)" → Delegar a sub-skill geo
  - "🔧 Rendimiento y velocidad" → Delegar a sub-skill core-web-vitals
  - "📝 Contenido y credibilidad (E-E-A-T)" → Delegar a sub-skill eeat
  - "🏷️ Datos estructurados (Schema)" → Delegar a sub-skill schema
  - "🤖 Acceso de crawlers IA y llms.txt" → Delegar a sub-skills crawlers + llmstxt
  - "📊 Informe PDF profesional" → Delegar a sub-skill report
```

### Paso 3 — Ejecutar y reportar

Para cada módulo seleccionado:
1. **SIEMPRE ejecutar el script Python correspondiente primero** — obtener datos reales
2. Interpretar los resultados combinando datos reales + conocimiento del sub-skill
3. Presentar hallazgos priorizados (críticos primero)
4. Al final de todo, preguntar: "¿Querés que profundice en algo o genero el PDF?"

---

## 🛠️ Scripts de Medición Real

Cada script devuelve datos medibles y reproducibles. **Ejecutalos siempre antes de emitir conclusiones.**

| Script | Qué Mide | Output |
|--------|----------|--------|
| `python3 scripts/page_speed.py <url>` | Core Web Vitals reales (LCP/CLS/TBT) vía PageSpeed Insights API | JSON con métricas, ratings, diagnóstico |
| `python3 scripts/robots_crawlers.py <domain>` | Acceso de 12 crawlers IA en robots.txt | JSON con allowed/blocked/restricted |
| `python3 scripts/llms_txt_validator.py <domain>` | Presencia y validez de llms.txt | JSON con formato, score, headers |
| `python3 scripts/schema_checker.py <url>` | JSON-LD detectado y validado | JSON con schemas, conflictos, score |
| `python3 scripts/geo_scorer.py <url>` | GEO score basado en Princeton | JSON con 5 estrategias + 4 tácticas |
| `python3 scripts/report_pdf.py <data.json>` | PDF profesional con ReportLab | PDF descargable en español |

---

## 📦 Sub-Skills — Carga Bajo Demanda

Cada comando activa solo el sub-skill que necesita. Nada de cargar 80KB de framework para cada análisis.

| Comando | Sub-skill | Script Asociado |
|---------|-----------|-----------------|
| `/geo-seo-pro seo-factors <url>` | `skills/seo-factors/SKILL.md` | No (checklist manual) |
| `/geo-seo-pro core-web-vitals <url>` | `skills/core-web-vitals/SKILL.md` | `page_speed.py` |
| `/geo-seo-pro e-e-a-t <url>` | `skills/eeat/SKILL.md` | No (evaluación cualitativa) |
| `/geo-seo-pro schema <url>` | `skills/schema/SKILL.md` | `schema_checker.py` |
| `/geo-seo-pro geo <url>` | `skills/geo/SKILL.md` | `geo_scorer.py` |
| `/geo-seo-pro llmstxt <url>` | `skills/llmstxt/SKILL.md` | `llms_txt_validator.py` |
| `/geo-seo-pro crawlers <url>` | `skills/crawlers/SKILL.md` | `robots_crawlers.py` |
| `/geo-seo-pro report <url>` | `skills/report/SKILL.md` | `report_pdf.py` |

---

## 📊 Scoring Compuesto

| Categoría | Peso | Fuente |
|-----------|------|--------|
| SEO Tradicional | 20% | Checklist 128 factores |
| Core Web Vitals | 10% | PageSpeed Insights API |
| E-E-A-T | 20% | Evaluación Who/How/Why |
| GEO (Princeton) | 25% | geo_scorer.py |
| Schema JSON-LD | 10% | schema_checker.py |
| llms.txt + Crawlers | 10% | llms_txt_validator.py + robots_crawlers.py |
| Autoridad Dominio | 5% | Estimación cualitativa |

---

## 📁 Outputs

| Archivo | Contenido |
|---------|-----------|
| `GEO-SEO-PRO-REPORT.pdf` | Informe PDF profesional con portada, scores, hallazgos y plan de acción |
| `GEO-SEO-CWV-ANALYSIS.md` | Core Web Vitals con métricas reales |
| `GEO-SEO-FACTORS-CHECKLIST.md` | Checklist 128 factores SEO |
| `GEO-SEO-GEO-ANALYSIS.md` | Análisis Princeton + recomendaciones |
| `GEO-SEO-SCHEMA-REPORT.md` | Schema detectados + JSON-LD generado |
| `GEO-SEO-CRAWLER-ACCESS.md` | Acceso crawlers IA + robots.txt |
| `llms.txt` | Archivo generado listo para desplegar |

---

## ⚠️ Límites Honestos

- **Core Web Vitals:** Mediciones de laboratorio (Lighthouse). Datos de campo (CrUX) disponibles solo para sitios con tráfico suficiente. PageSpeed Insights API tiene rate limits sin API key.
- **GEO Score:** Basado en heurísticas del estudio Princeton. No garantiza visibilidad en IA — identifica factores que Princeton demostró que correlacionan.
- **SEO Tradicional:** Checklist basado en documentación pública de Google (Backlinko, Google Search Central). No es un algoritmo oficial.
- **Resultados:** Las mediciones de scripts son reproducibles. Las interpretaciones y recomendaciones del LLM son asistencia experta, no verdad absoluta.
