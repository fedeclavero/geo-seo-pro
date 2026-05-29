---
name: geo-seo-pro-geo
description: Sub-skill de GEO: Princeton GEO-bench, RAG, citabilidad. Usa geo_scorer.py para medición real.
allowed-tools: Read, Bash, WebFetch, WebSearch, Write, Grep
---

# GEO — Generative Engine Optimization

**Usa geo_scorer.py para medir contenido contra las estrategias de Princeton.**

## Ejecución

```bash
python3 scripts/geo_scorer.py <url>
```

Devuelve JSON con scores reales (no estimados) para las 5 estrategias ganadoras y detección de las 4 tácticas fallidas.

## Las 5 Estrategias Ganadoras (Princeton GEO-bench, KDD 2024)

| # | Estrategia | Incremento | Qué Mide el Script |
|---|-----------|------------|-------------------|
| 1 | Citar Fuentes | +40% | URLs externas, marcadores de citación |
| 2 | Datos Estadísticos | +40% | Porcentajes, años, datos numéricos, pares fuente+año |
| 3 | Citas de Expertos | +35% | Citas directas con atribución, nombres, cargos |
| 4 | Fluidez | +30% | Variedad de longitud de oraciones, fluidez sintáctica |
| 5 | Tono de Autoridad | +25% | Marcadores de certeza vs. vacilación |

## Las 4 Tácticas Fallidas

| Táctica | Detección |
|---------|-----------|
| Keyword Stuffing | Densidad >2% de cualquier término |
| Simplificación Extrema | Ratio de vocabulario único <15% |
| Relleno de Contenido | Párrafos sin sustancia |
| Lenguaje Persuasivo | Adjetivos promocionales >3 ocurrencias |

## Efecto Underdog
Los sitios con baja autoridad SEO tradicional obtienen el MAYOR beneficio proporcional en GEO al aplicar estas estrategias. Esto representa una ventana de oportunidad para sitios pequeños y medianos.

## RAG — Cómo Funciona
Los motores de IA usan arquitectura de 3 capas:
1. Búsqueda semántica vectorial → recupera documentos candidatos
2. Comprensión y filtrado del LLM → evalúa veracidad y autoridad
3. Síntesis conversacional → decide qué fuentes citar con hipervínculos

## Output
`GEO-SEO-GEO-ANALYSIS.md` con GEO score 0-100, análisis párrafo por párrafo, y estrategias de mejora.
