# GEO-SEO Pro — Claude Code Skill

**Herramienta de análisis de posicionamiento para buscadores tradicionales (Google) y motores de IA (ChatGPT, Perplexity, Gemini, Claude).** Ejecuta mediciones reales con APIs y scripts. Informes PDF en español.

---

## 🎯 ¿Qué hace realmente?

- ✅ **Mide** Core Web Vitals reales con PageSpeed Insights API (no estima)
- ✅ **Verifica** acceso de 12 crawlers IA parseando tu robots.txt (binario: allowed/blocked)
- ✅ **Valida** llms.txt contra el estándar oficial (formato, headers, .well-known)
- ✅ **Detecta** schemas JSON-LD y campos obligatorios faltantes
- ✅ **Evalúa** tu contenido contra las estrategias de Princeton GEO-bench (KDD 2024)
- ✅ **Analiza** los factores que impactan tu posicionamiento y genera recomendaciones priorizadas
- ✅ **Genera** un informe PDF profesional descargable en español

**No garantiza** posicionamiento. **No reemplaza** a un profesional SEO. Es una herramienta de análisis y diagnóstico.

---

## 📦 Instalación

```bash
npx geo-seo-pro-install
```

---

## 🚀 Uso

En Claude Code, escribí:

```
/geo-seo-pro
```

La skill te guía paso a paso. No necesitás saber SEO ni GEO.

### Comandos directos

```
/geo-seo-pro geo https://misitio.com          # Visibilidad en IA
/geo-seo-pro core-web-vitals https://misitio.com  # Velocidad real
/geo-seo-pro crawlers https://misitio.com      # Acceso de bots IA
/geo-seo-pro llmstxt https://misitio.com       # Generar llms.txt
/geo-seo-pro schema https://misitio.com        # Datos estructurados
/geo-seo-pro e-e-a-t https://misitio.com       # Credibilidad
/geo-seo-pro seo-factors https://misitio.com   # 128+ factores
/geo-seo-pro report https://misitio.com        # Informe PDF
```

---

## 🔬 ¿En qué se basa?

- **PageSpeed Insights API** — Métricas reales de Google
- **Princeton GEO-bench (KDD 2024)** — Estudio científico con 10,000 consultas
- **Google Search Central** — E-E-A-T, Helpful Content, Core Web Vitals
- **Especificación llms.txt** — Estándar de interfaz para agentes IA

---

## 🏗️ Arquitectura

La skill es un **orquestador liviano** (6KB) que delega a sub-skills especializados. Cada sub-skill carga solo cuando se necesita, sin saturar el contexto. Scripts Python ejecutan mediciones reales.

```
geo-seo-pro/
├── SKILL.md              # Orquestador (6KB — no 80KB)
├── skills/               # Sub-skills modulares
│   ├── geo/SKILL.md
│   ├── core-web-vitals/SKILL.md
│   ├── eeat/SKILL.md
│   ├── schema/SKILL.md
│   ├── seo-factors/SKILL.md
│   ├── llmstxt/SKILL.md
│   ├── crawlers/SKILL.md
│   └── report/SKILL.md
├── scripts/              # Código real (1511 líneas Python)
│   ├── page_speed.py     # PageSpeed Insights API
│   ├── robots_crawlers.py # Parseo de robots.txt
│   ├── llms_txt_validator.py # Validación llms.txt
│   ├── schema_checker.py # Detección JSON-LD
│   ├── geo_scorer.py     # Princeton GEO scoring
│   └── report_pdf.py     # PDF con ReportLab
└── install.js
```

---

## 📄 Licencia

MIT
