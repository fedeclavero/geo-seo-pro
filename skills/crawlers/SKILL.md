---
name: geo-seo-pro-crawlers
description: Sub-skill de configuración de acceso para crawlers IA en robots.txt. Usa script de parseo real.
allowed-tools: Read, Bash, WebFetch, Write
---

# Crawlers IA — Configuración de robots.txt

**Usa robots_crawlers.py para parsear el robots.txt real.** Resultados binarios: allowed/blocked/restricted.

## Ejecución

```bash
python3 scripts/robots_crawlers.py <domain>
```

Devuelve acceso verificado para 12 crawlers IA + sitemaps + Content-Signals.

## Crawlers Verificados

| Crawler | Servicio | Critical |
|---------|----------|----------|
| GPTBot | OpenAI (training + ChatGPT) | ✅ Sí |
| OAI-SearchBot | OpenAI (search-only) | ✅ Sí |
| ChatGPT-User | ChatGPT browsing | No |
| ClaudeBot | Anthropic / Claude | ✅ Sí |
| PerplexityBot | Perplexity AI | ✅ Sí |
| Google-Extended | Gemini training | ✅ Sí |
| Amazonbot | Alexa AI | No |
| Bytespider | ByteDance / TikTok AI | No |
| CCBot | Common Crawl | No |
| Applebot-Extended | Apple Intelligence | No |
| FacebookBot | Meta AI | No |
| Cohere-ai | Cohere | No |

## Configuración Recomendada

```robots.txt
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: OAI-SearchBot
Allow: /

Sitemap: https://domain.com/sitemap.xml
Sitemap: https://domain.com/llms.txt
```

## Scoring
- 100 puntos base
- -15 por cada crawler crítico bloqueado
- -5 por cada crawler secundario bloqueado
- -10 si no hay sitemap

## Output
`GEO-SEO-CRAWLER-ACCESS.md` con tabla de acceso por crawler + `robots.txt` corregido.
