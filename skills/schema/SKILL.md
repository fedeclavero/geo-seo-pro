---
name: geo-seo-pro-schema
description: Detecta schemas faltantes y genera automáticamente JSON-LD listo para implementar.
allowed-tools: Read, Bash, WebFetch, Write
---

# Schema JSON-LD — Detectar y ARREGLAR

**No solo detecto. Genero el JSON-LD correcto para tu tipo de negocio.**

## Flujo de Acción

1. Ejecutar `python3 scripts/schema_checker.py <url>` → detectar qué schemas existen y qué falta
2. Ejecutar `python3 scripts/business_detector.py <url>` → determinar tipo de negocio
3. Seleccionar template correcto de `templates/` según tipo
4. Extraer datos del HTML (nombre empresa, logo, redes sociales, dirección, etc.)
5. Rellenar el template con los datos extraídos
6. Entregar el archivo `.jsonld` listo para que el usuario lo incruste en el `<head>`

## Mapeo Tipo de Negocio → Template

| Tipo | Template Principal | Templates Secundarios |
|------|-------------------|----------------------|
| SaaS | `software-saas.json` | `organization.json`, `faq-page.json`, `website-searchaction.json` |
| Local Service | `local-business.json` | `organization.json`, `faq-page.json`, `website-searchaction.json` |
| E-commerce | `product-ecommerce.json` | `organization.json`, `website-searchaction.json` |
| Publisher | `article-author.json` | `organization.json`, `website-searchaction.json` |
| Agency | `organization.json` | `website-searchaction.json`, `faq-page.json` |
| Other | `organization.json` | `website-searchaction.json` |

## sameAs — Crítico para IA

Para `Organization` y `Person`, los perfiles `sameAs` son LA señal más potente de autenticidad. Siempre incluir:
- Wikipedia (si existe)
- LinkedIn
- Wikidata (si existe)
- Twitter/X
- GitHub (si es tech)
- Google Scholar (si es académico)

## Output

- `generated-schema.jsonld` — archivo listo para copiar al `<head>`
- Instrucciones de instalación (dónde pegarlo, cómo verificar en Rich Results Test)
