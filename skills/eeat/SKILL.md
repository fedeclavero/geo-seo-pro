---
name: geo-seo-pro-eeat
description: Sub-skill de evaluación E-E-A-T y Helpful Content System (Who/How/Why).
allowed-tools: Read, Bash, WebFetch, Write, Grep, Glob
---

# E-E-A-T y Helpful Content System

Evaluá el contenido contra el marco E-E-A-T de Google y el sistema de autoevaluación "Who, How, Why".

## Dimensiones E-E-A-T

| Dimensión | Peso | Señales a Verificar |
|-----------|------|---------------------|
| Experience | 25% | Fotos originales, datos de primera mano, anécdotas reales, casos propios |
| Expertise | 25% | Credenciales, certificaciones, formación verificable, publicaciones previas |
| Authoritativeness | 20% | Citas de otras organizaciones, presencia Wikipedia, menciones sector |
| Trustworthiness | 30% | HTTPS, transparencia autoría, políticas legales, contacto, datos factuales |

## Evaluación Who/How/Why

- **¿Quién creó?** Verificar bylines, biografías enlazadas, perfiles sociales vinculados, credenciales contrastables
- **¿Cómo se creó?** Detectar transparencia sobre uso de IA, fuentes primarias citadas, datos originales vs. curación
- **¿Por qué se creó?** Evaluar si el contenido resuelve una necesidad real o es contenido masivo para SEO. ¿El visitante completa su tarea sin necesitar otra búsqueda?

## Detección de Contenido "Para Buscadores"
- URLs sobre temas inconexos con la temática del sitio
- Contenido sin valor único (reescritura de terceros)
- Fechas de publicación masivas sin profundidad
- Ausencia total de autoría

## Scoring
| Rango | Calificación |
|-------|-------------|
| 90-100 | Excelente — referente sectorial |
| 70-89 | Bueno — sólido con mejoras menores |
| 50-69 | Adecuado — gaps de credibilidad |
| 30-49 | Pobre — señales insuficientes |
| 0-29 | Crítico — sin validación humana |

**Output:** `GEO-SEO-EEAT-ASSESSMENT.md` con score por dimensión, gaps detectados, y recomendaciones accionables.
