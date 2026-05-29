---
name: geo-seo-pro-seo-factors
description: Sub-skill de 128+ factores de ranking SEO. Se carga solo cuando el usuario pide análisis SEO tradicional.
allowed-tools: Read, Bash, WebFetch, Write, Grep, Glob
---

# SEO Tradicional — 128+ Factores de Ranking

Analizá la URL objetivo contra los 128+ factores documentados, marcando cada uno como:
✅ Cumple | ⚠️ Mejorable | ❌ No cumple | N/A No aplica

Al terminar, generá `GEO-SEO-FACTORS-CHECKLIST.md` con el checklist completo y las 10 acciones prioritarias.

## Factores de Dominio (1-9)
Edad, keyword en TLD, duración registro, keyword en subdominio, historial, EMD, privacidad WhoIs, historial propietario, ccTLD.

## Factores de Página: Contenido (10-29)
Title (keyword al inicio), meta description, H1, TF-IDF, longitud (>1400 palabras), TOC vinculada, LSI en contenido y metadatos, cobertura temática, coincidencia entidades, Hummingbird, prominencia keyword (primeras 100 palabras), H2/H3, gramática, contenido útil, insights únicos, título no clickbait, formato (viñetas/negritas), originalidad.

## Factores de Página: Técnicos (30-54)
Velocidad HTML, AMP, duplicado on-site, canonical, optimización imágenes (alt/title/filename), recencia Caffeine, magnitud actualización, historial actualizaciones, responsive móvil, usabilidad móvil, contenido oculto móvil, contenido suplementario, pestañas, cookies no intrusiva, keyword en URL, categorización ruta, referencias fuentes autoridad, listas viñetadas, prioridad sitemap, exceso enlaces salientes, keywords concurrentes, madurez página, longitud URL, profundidad ruta, relevancia categoría.

## Factores de Sitio (55-60)
Valor unificado dominio, arquitectura interna enlaces (silo), uptime servidor, páginas legales, analíticas oficiales, consistencia responsive global.

## Backlinks (61-85)
Edad dominio emisor, nº páginas enlazan, .edu/.gov, competidores, anuncios (nofollow), sponsored, texto ancla interno, ubicación link, afinidad nicho, relevancia página, keyword título emisor, velocidad positiva/negativa, páginas hub, alta autoridad, redirecciones 301, schema emisor, TrustRank, densidad salientes emisor, foros, extensión contenido emisor, calidad texto origen, compresión sitewide, reinicio historial expiración, diversidad enlaces.

## Interacción Usuario y Marca (86-98)
Comentarios, dwell time, RankBrain, bounce rate, pogosticking, reputación externa, usabilidad interfaz, anclas de marca, búsquedas directas marca, búsquedas combinadas marca+keyword, presencia Facebook/Twitter, percepción online marca.

## Reglas Especiales Algoritmo (99-116)
QDF, historial búsqueda usuario, Safe Search, transaccional, Vince Update, monopolio marca, geolocalización IP/ccTLD, YMYL, DMCA, Bigfoot, Local Pack, Top Stories, Shopping, imágenes, Payday Loans, ajustes estacionales, quality raters, relevancia categórica.

## Webspam (117-128)
Hackeo servidor, captación veloz enlaces, perfil low-quality, temáticas no relacionadas, advertencia enlaces no naturales, directorios spam, PBN misma IP clase C, anclajes venenosos, pico temporal patentado, directorios artículos, contenido copiado/raspado, enlaces masivos footer.

## Scoring

| Categoría | Peso |
|-----------|------|
| Dominio | 10% |
| Contenido On-Page | 25% |
| Técnico On-Page | 20% |
| Sitio | 10% |
| Backlinks | 15% |
| Interacción/Marca | 10% |
| Cumplimiento Reglas | 5% |
| Ausencia Webspam | 5% |

**Output:** Checklist completo con score 0-100 y top 10 acciones priorizadas por impacto.
