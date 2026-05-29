---
name: geo-seo-pro-core-web-vitals
description: Sub-skill de Core Web Vitals. Ejecuta medición real con PageSpeed Insights API.
allowed-tools: Read, Bash, WebFetch, Write
---

# Core Web Vitals — Medición Real

**Este sub-skill ejecuta código real, no estima.** Usa PageSpeed Insights API.

## Ejecución

```bash
python3 scripts/page_speed.py <url> mobile
```

El script devuelve JSON con:
- `performance_score`: 0-100
- `metrics.lcp`: Largest Contentful Paint (valor real en segundos, rating good/needs-improvement/poor)
- `metrics.cls`: Cumulative Layout Shift (valor real, rating)
- `metrics.tbt`: Total Blocking Time — proxy de lab para INP
- `metrics.ttfb`: Time to First Byte
- `metrics.fcp`: First Contentful Paint
- `diagnostics`: Top issues (render-blocking, images, unused CSS/JS, etc.)
- `cwv_score`: Puntuación agregada 0-100

## Rangos Oficiales

| Métrica | Bueno | Advertencia | Crítico |
|---------|-------|-------------|---------|
| LCP | ≤ 2.5s | 2.5s - 4.0s | > 4.0s |
| CLS | ≤ 0.1 | 0.1 - 0.25 | > 0.25 |
| TBT (proxy INP) | ≤ 200ms | 200ms - 600ms | > 600ms |

## Optimización Quirúrgica

**LCP:** Comprimir imágenes (AVIF/WebP), CDN, preload hero image (`<link rel="preload">`), eliminar CSS/JS bloqueante, TTFB < 800ms.

**TBT/INP:** Deferir scripts no críticos, trocear long tasks, `requestIdleCallback`, optimizar event handlers, minimizar analytics en carga inicial.

**CLS:** Dimensiones explícitas width/height en todas las imágenes y embeds, `font-display: swap`, reservar espacio para anuncios.

## Output

Generar `GEO-SEO-CWV-ANALYSIS.md` con:
- Score CWV 0-100
- Métricas reales (no estimadas) de PageSpeed Insights
- Top 5 issues con fix específico
- Código HTML/CSS/JS listo para implementar
