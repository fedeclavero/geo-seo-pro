# Changelog

## 1.0.0 (2026-05-29)

### Initial Release — GEO-SEO Pro Complete Skill

Basado en el documento de investigación "Arquitectura de Optimización de Búsqueda de Siguiente Generación".

**Cobertura completa:**

- **128+ SEO Ranking Factors** organizados en 8 categorías: Dominio (9), Página/Contenido (20), Página/Técnicos (25), Sitio (6), Backlinks (25), Interacción Usuario (13), Reglas Algoritmo (18), Webspam (12)
- **Core Web Vitals** — LCP, INP, CLS con rangos óptimo/advertencia/crítico y protocolos de optimización quirúrgica
- **E-E-A-T y Helpful Content System** — Experience, Expertise, Authoritativeness, Trustworthiness + Who/How/Why framework
- **Schema JSON-LD** — 7 esquemas clave (BlogPosting, FAQPage, HowTo, Organization, Person, Product, LocalBusiness) + sameAs + riesgos de solapamiento
- **GEO y Arquitectura RAG** — AEO vs GEO, RAG 3-capas, principios de recuperación semántica
- **Princeton GEO-bench (KDD 2024)** — 5 estrategias ganadoras (+25-40%), 4 tácticas fallidas, Efecto Underdog
- **llms.txt y llms-full.txt** — Especificación completa, HTTP headers, .well-known, robots.txt para 12 crawlers IA
- **Protocolos de seguridad** — Anti prompt-injection, CI/CD governance, hash monitoring
- **Matriz de Integración SEO+GEO** — Scoring compuesto 7 categorías (0-100), protocolos de ejecución para 10 comandos

**Comandos:**
- `/geo-seo-pro audit <url>` — Auditoría completa
- `/geo-seo-pro seo-factors <url>` — Checklist 128+ factores
- `/geo-seo-pro core-web-vitals <url>` — Análisis LCP/INP/CLS
- `/geo-seo-pro e-e-a-t <url>` — Evaluación E-E-A-T
- `/geo-seo-pro schema <url>` — Auditoría JSON-LD
- `/geo-seo-pro geo <url>` — Análisis Princeton + citabilidad
- `/geo-seo-pro llmstxt <url>` — Generar llms.txt
- `/geo-seo-pro crawlers <url>` — Configurar robots.txt IA
- `/geo-seo-pro content <url>` — Optimizar contenido para RAG
- `/geo-seo-pro report <url>` — Informe completo
