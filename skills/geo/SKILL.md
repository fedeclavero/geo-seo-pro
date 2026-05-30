---
name: geo-seo-pro-geo
description: Optimiza contenido para visibilidad en IA. No solo mide — reescribe pasajes aplicando estrategias de Princeton GEO-bench.
allowed-tools: Read, Bash, WebFetch, WebSearch, Write, Edit, Grep
---

# GEO — Generative Engine Optimization

**REESCRIBO tu contenido para maximizar la probabilidad de ser citado por ChatGPT, Perplexity, Gemini y Claude.**

## Flujo de Acción

1. Ejecutar `python3 scripts/geo_scorer.py <url>` → obtener scores por estrategia
2. Para cada pasaje con score bajo, aplicar la estrategia correspondiente
3. Reescribir párrafos específicos con mejoras concretas
4. Generar `GEO-SEO-CONTENT-FIX.md` con antes/después

## Las 5 Estrategias — Cómo las Aplico

| Estrategia | Si el score es bajo... | Acción concreta |
|-----------|----------------------|-----------------|
| **Citar Fuentes** (+40%) | < 60 puntos | Añadir 2-3 enlaces a fuentes autoritativas por cada afirmación clave |
| **Datos Estadísticos** (+40%) | < 60 puntos | Sustituir descripciones genéricas por porcentajes, cifras y años concretos con fuente |
| **Citas de Expertos** (+35%) | < 50 puntos | Insertar 1-2 citas textuales atribuidas (nombre + cargo + organización) |
| **Fluidez** (+30%) | < 70 puntos | Variar longitud de oraciones, eliminar muletillas, mejorar transiciones |
| **Tono de Autoridad** (+25%) | < 70 puntos | Reemplazar "podría", "quizás", "creo que" por afirmaciones directas |

## Tácticas que ELIMINO activamente

| Táctica | Si la detecto... |
|---------|-----------------|
| Keyword Stuffing | Reescribo para densidad natural (<2%) |
| Simplificación Extrema | Restauro vocabulario técnico y jerga del sector |
| Relleno | Elimino párrafos sin contenido y consolido |
| Lenguaje Persuasivo | Reemplazo adjetivos comerciales por datos objetivos |

## Output

`GEO-SEO-CONTENT-FIX.md` con:
- Párrafo original → Párrafo optimizado (con cambios resaltados)
- Score antes → Score estimado después
- Justificación basada en Princeton GEO-bench
