---
name: geo-seo-pro-schema
description: Sub-skill de auditoría y generación de Schema JSON-LD. Usa script real de detección.
allowed-tools: Read, Bash, WebFetch, Write, Grep
---

# Schema JSON-LD — Auditoría y Generación

**Usa código real para detectar schemas.** No alucina — extrae y valida.

## Ejecución

```bash
python3 scripts/schema_checker.py <url>
```

El script devuelve JSON con:
- `jsonld_blocks_found`: Número de bloques JSON-LD en la página
- `valid_blocks` / `invalid_blocks`
- `schemas`: Lista de schemas detectados con validación de campos obligatorios
- `conflicts`: Conflictos de solapamiento detectados
- `schema_score`: 0-100

## Esquemas Clave

| Schema | Uso | Campos Obligatorios |
|--------|-----|---------------------|
| BlogPosting | Posts y artículos | mainEntityOfPage, author, publisher, datePublished, dateModified, image |
| FAQPage | Preguntas frecuentes | mainEntity (texto debe coincidir con HTML visible) |
| HowTo | Tutoriales paso a paso | name, step (solo para guías secuenciales prácticas) |
| Organization | Identidad corporativa | name, sameAs (perfiles verificados) |
| Person | Autoría | name, sameAs (LinkedIn, Wikipedia, académicas) |
| Product | E-commerce | name (precios y stock actualizados) |
| LocalBusiness | Negocio físico | name, address (debe coincidir con Google Business Profile) |

## Regla de Oro
**Un solo schema primario por URL.** Múltiples schemas primarios (FAQPage + HowTo + Product en misma URL) diluyen la claridad semántica.

## sameAs — La Señal Más Potente
Conectar con Wikipedia, LinkedIn, Wikidata, GitHub, perfiles académicos. Wikipedia es la señal más fuerte para reconocimiento de entidades por IA.

## Output
`GEO-SEO-SCHEMA-REPORT.md` + `generated-schema.jsonld` con esquemas corregidos o nuevos listos para implementar.
