---
name: geo-seo-pro-report
description: Sub-skill de generación de informe compuesto con PDF profesional usando ReportLab.
allowed-tools: Read, Bash, WebFetch, Write
---

# Informe Compuesto GEO-SEO Pro

Genera un informe profesional completo consolidando todos los análisis previos.

## Flujo

1. Recopilar los outputs de los análisis ejecutados (CWV, SEO factors, GEO, Schema, Crawlers, llms.txt, E-E-A-T)
2. Construir un JSON con la estructura del informe
3. Generar PDF con `python3 scripts/report_pdf.py data.json GEO-SEO-PRO-REPORT.pdf`

## Estructura del JSON de Datos

```json
{
  "url": "https://dominio.com",
  "composite_score": 72,
  "score_breakdown": {
    "SEO Tradicional": {"score": 68, "rating": "Bueno"},
    "Core Web Vitals": {"score": 85, "rating": "Excelente"},
    "E-E-A-T": {"score": 55, "rating": "Adecuado"},
    "Schema JSON-LD": {"score": 70, "rating": "Bueno"},
    "GEO (Princeton)": {"score": 62, "rating": "Bueno"},
    "llms.txt + Crawlers": {"score": 90, "rating": "Excelente"},
    "Autoridad de Dominio": {"score": 45, "rating": "Necesita Mejora"}
  },
  "findings": [
    {"severity": "critical", "message": "Sin autoría verificable en los artículos"},
    {"severity": "high", "message": "LCP de 3.2s en móvil — zona de advertencia"}
  ],
  "action_plan": [
    {"timeframe": "quick", "action": "Añadir bylines con enlaces a biografías en todos los posts"},
    {"timeframe": "medium", "action": "Implementar CDN y compresión de imágenes"}
  ]
}
```

## Scoring Compuesto

| Categoría | Peso |
|-----------|------|
| SEO Tradicional | 20% |
| Core Web Vitals | 10% |
| E-E-A-T | 20% |
| GEO (Princeton) | 25% |
| Schema JSON-LD | 10% |
| llms.txt + Crawlers | 10% |
| Autoridad Dominio | 5% |

## PDF Output
El PDF incluye:
- Portada con score global y URL
- Desglose de puntuaciones con tabla
- Hallazgos clave categorizados por severidad
- Plan de acción priorizado (Quick Wins / Medio Plazo / Estratégico)
- Metodología y fuentes

**Output:** `GEO-SEO-PRO-REPORT.md` (markdown) y `GEO-SEO-PRO-REPORT.pdf` (PDF profesional).
