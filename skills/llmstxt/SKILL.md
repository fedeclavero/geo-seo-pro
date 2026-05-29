---
name: geo-seo-pro-llmstxt
description: Sub-skill de llms.txt y llms-full.txt. Usa script de validación real.
allowed-tools: Read, Bash, WebFetch, Write
---

# llms.txt y llms-full.txt — Interfaz para Agentes de IA

**Usa llms_txt_validator.py para validación real contra el estándar.**

## Ejecución

```bash
python3 scripts/llms_txt_validator.py <domain>
```

Devuelve:
- Presencia de llms.txt, llms-full.txt, .well-known/llms.txt
- Validación de formato (H1, blockquote, H2, enlaces anotados)
- Score 0-100
- HTTP headers detectados

## Especificación

**llms.txt** (≤ 5000 tokens):
```markdown
# Nombre del Proyecto
> Descripción de 1-3 líneas sobre qué cubre la web.

## Sección
- [Título del recurso](https://url.com/doc.md): Descripción concisa (máx 300 chars).
```

**llms-full.txt** (≤ 50000 tokens): Documentación completa concatenada en Markdown.

## HTTP Headers Requeridos
```
Link: <https://domain.com/llms.txt>; rel="llms-txt"
Link: <https://domain.com/llms-full.txt>; rel="llms-full-txt"
X-Llms-Txt: /llms.txt
```

## Seguridad — Crítico
- **NUNCA editar llms.txt manualmente en producción** — solo vía CI/CD como artefacto de build
- Monitorizar hash MD5/SHA256 del archivo para detectar modificaciones no autorizadas
- Si hay contenido con autenticación, las rutas en llms.txt deben usar el mismo esquema de seguridad
- Riesgo: inyección indirecta de prompts si un atacante modifica el archivo

## Output
`llms.txt` y `llms-full.txt` generados, listos para desplegar. Incluye diagnóstico de seguridad.
