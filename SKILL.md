---
name: geo-seo-pro
description: >
  GEO-SEO Pro — Habilidad maestra unificada de Generative Engine Optimization y SEO
  tradicional. Cubre 128+ factores de ranking SEO organizados en 8 categorías, Core Web
  Vitals (LCP/INP/CLS) con protocolos de optimización quirúrgica, E-E-A-T y Helpful
  Content System (Who/How/Why), Schema JSON-LD para IA (7 esquemas + sameAs), GEO/RAG
  basado en el estudio Princeton GEO-bench (5 estrategias ganadoras, 4 tácticas fallidas,
  Underdog Effect), estándar llms.txt/llms-full.txt con HTTP headers y .well-known,
  configuración de 10+ crawlers IA en robots.txt, protocolos de seguridad anti-inyección
  de prompts, y matriz de integración sistémica SEO+GEO con scoring compuesto de 7
  categorías. Use cuando el usuario diga "geo", "seo", "geo seo pro", "posicionamiento
  IA", "optimizar para IA", "AI search", "generative engine", "llms.txt", "schema",
  "core web vitals", "e-e-a-t", "princeton geo", "crawlers IA", "robots.txt IA", o
  cualquier URL para análisis completo de visibilidad en buscadores tradicionales y
  motores de respuestas generativos.
allowed-tools: Read, Bash, WebFetch, WebSearch, Write, Edit, Grep, Glob
---

# GEO-SEO Pro — Optimización de Búsqueda de Siguiente Generación

> **Filosofía:** GEO-first, SEO-foundation. Los motores de respuestas generativos (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews) están reemplazando el search tradicional. Pero no se puede ganar en GEO sin cimientos SEO sólidos. Esta skill unifica ambos paradigmas en una arquitectura híbrida de optimización.

---

## Quick Reference

| Comando | Qué Hace |
|---------|----------|
| `/geo-seo-pro audit <url>` | Auditoría completa SEO + GEO (4 fases, scoring 0-100) |
| `/geo-seo-pro seo-factors <url>` | Análisis exhaustivo de 128+ factores de ranking |
| `/geo-seo-pro core-web-vitals <url>` | Análisis LCP/INP/CLS con recomendaciones quirúrgicas |
| `/geo-seo-pro e-e-a-t <url>` | Evaluación E-E-A-T y Helpful Content (Who/How/Why) |
| `/geo-seo-pro schema <url>` | Auditoría, validación y generación de JSON-LD |
| `/geo-seo-pro geo <url>` | Análisis GEO puro: Princeton + citabilidad + RAG |
| `/geo-seo-pro llmstxt <url>` | Generar o analizar llms.txt y llms-full.txt |
| `/geo-seo-pro crawlers <url>` | Auditoría y configuración de acceso para crawlers IA |
| `/geo-seo-pro content <url>` | Optimización de contenido para arquitecturas RAG |
| `/geo-seo-pro report <url>` | Informe compuesto cliente-ready con plan de acción |

---

## Market Context — Por Qué GEO Importa

| Métrica | Valor | Fuente |
|---------|-------|--------|
| Mercado GEO services (2025) | $850M-$886M | Yahoo Finance / Superlines |
| Proyección mercado GEO (2031) | $7.3B (34% CAGR) | Industry analysts |
| Sesiones referidas por IA (crecimiento) | +527% (Jan-May 2025) | SparkToro |
| Conversión tráfico IA vs orgánico | 4.4x mayor | Industry data |
| Google AI Overviews alcance | 1.5B usuarios/mes, 200+ países | Google |
| ChatGPT usuarios activos semanales | 900M+ | OpenAI |
| Perplexity queries mensuales | 500M+ | Perplexity |
| Gartner: caída search tradicional 2028 | -50% | Gartner |
| Marketers invirtiendo en GEO | Solo 23% | Industry surveys |
| Brand mentions vs backlinks para IA | 3x correlación más fuerte | Ahrefs (Dec 2025) |

---

## Business Type Detection

Al analizar un sitio, detectar el tipo de negocio para ajustar recomendaciones:

| Tipo | Señales | Schemas Prioritarios |
|------|---------|---------------------|
| **SaaS** | Pricing, "Sign up", "Free trial", /app, /dashboard, API docs | SoftwareApplication, Organization, FAQPage |
| **Local Service** | Teléfono, dirección, "Near me", Google Maps, service area | LocalBusiness, Organization, FAQPage |
| **E-commerce** | Product pages, cart, "Add to cart", precios | Product, Organization, FAQPage |
| **Publisher** | Blog, artículos, bylines, fechas, article schema | BlogPosting/Article, Person, Organization |
| **Agency** | Portfolio, case studies, "Our services", client logos | Organization, Person, Service |
| **Other** | Sin patrón claro | Organization, FAQPage (mínimo) |

---

## Quality Gates

- **Crawl limit:** Máximo 50 páginas por auditoría (calidad sobre cantidad)
- **Timeout:** 30 segundos por página
- **Rate limiting:** 1 segundo entre requests, máximo 5 concurrentes
- **Robots.txt:** Siempre respetar, siempre verificar
- **Duplicate detection:** Saltar páginas con >80% similitud de contenido

---

## PARTE 1: TAXONOMÍA COMPLETA DE FACTORES SEO TRADICIONAL (128+ Factores)

> **Fuente:** Backlinko's Google Ranking Factors (2026), Google Search Central, Moz Panel. Organizados por nivel de influencia: Dominio → Página → Sitio → Backlinks → Usuario → Reglas Algoritmo → Webspam.

### 1.1 Factores de Dominio (IDs 1-9)

La configuración técnica, historial administrativo y decisiones de registro del dominio representan el primer filtro de seguridad y legitimidad que los algoritmos aplican antes de evaluar el contenido.

| ID | Parámetro | Mecanismo Técnico | Impacto y Aplicación |
|----|-----------|-------------------|----------------------|
| 1 | **Edad del Dominio** | Periodo cronológico desde el primer registro activo. | Impacto marginal directo, pero los dominios antiguos se benefician de perfiles de enlaces acumulados y estabilidad histórica. |
| 2 | **Palabra Clave en TLD** | Inclusión del término de búsqueda principal en el TLD. | Factor menor de relevancia temática. No compensa falta de autoridad, pero añade señal de identidad contextual. |
| 3 | **Duración del Registro** | Periodo de contratación a futuro ante el registrador. | Patentes de Google sugieren que dominios legítimos se registran con varios años de antelación; dominios spam rara vez superan 1 año. |
| 4 | **Palabra Clave en Subdominio** | Presencia de la keyword en subdominio (ej. keyword.domain.com). | El panel Moz confirma impulso de relevancia en búsquedas especializadas para subdominios optimizados semánticamente. |
| 5 | **Historial del Dominio** | Registro de penalizaciones previas, inactividad o cambios de titularidad. | Historial inestable o múltiples caídas de registro pueden forzar a Google a "resetear" el historial de rastreo, devaluando enlaces históricos. |
| 6 | **Dominio de Coincidencia Exacta (EMD)** | Dominios que replican textualmente un término de búsqueda. | Ventaja mínima. Si el sitio es detectado como spam o low-quality, el algoritmo EMD reduce drásticamente su visibilidad. |
| 7 | **Privacidad de WhoIs** | Ocultamiento de datos de contacto del registrante. | No penaliza directamente, pero evaluadores asocian WhoIs privado a proyectos que ocultan autoría. Con otras señales negativas, activa revisiones de spam. |
| 8 | **Historial del Propietario (WhoIs)** | Registro de spam/penalizaciones previas del titular. | Google puede extender escrutinio técnico y devaluar preventivamente nuevos dominios de operadores previamente identificados como spammers. |
| 9 | **Extensión ccTLD de País** | Dominios con códigos geográficos (.es, .ca, .mx). | Incrementa exponencialmente la capacidad de posicionar localmente, limitando rendimiento internacional. |

**Protocolo de Auditoría de Dominio:** Verificar edad (whois), duración de registro, historial de penalizaciones (archive.org + GSC), configuración de ccTLD vs geolocalización deseada.

### 1.2 Factores de Página: Contenido y Optimización Semántica (IDs 10-29)

La optimización on-page alinea la estructura lingüística de la página con la intención de búsqueda. El motor evalúa keywords y contextualización semántica mediante análisis sintácticos automatizados. Los motores modernos procesan versiones sofisticadas de TF-IDF para neutralizar la repetición artificial y premiar la diversidad contextual.

| ID | Parámetro | Mecanismo Técnico | Impacto y Aplicación |
|----|-----------|-------------------|----------------------|
| 10 | **Palabra Clave en Etiqueta Title** | Inclusión de la keyword principal en `<title>`. | Una de las señales on-page más potentes y directas para categorizar la temática del documento. |
| 11 | **Palabra Clave al Inicio del Title** | Colocación de la keyword en los caracteres iniciales del título. | Títulos que comienzan con el término logran mayor CTR y mejor procesamiento por robots de rastreo. |
| 12 | **Palabra Clave en Meta Description** | Presencia de la keyword en la descripción resumida. | No es factor directo de ordenación, pero resulta crítica para captar atención e incrementar CTR en la SERP. |
| 13 | **Palabra Clave en Etiqueta H1** | Inclusión del término en el encabezado principal. | Actúa como título secundario que los algoritmos cruzan con `<title>` para confirmar enfoque conceptual. |
| 14 | **TF-IDF Avanzado** | Procesamiento analítico de densidad de palabras mediante frecuencia inversa de documentos. | Evita uso artificial de keywords aisladas y premia el despliegue de léxico natural, variado y representativo del sector. |
| 15 | **Longitud del Contenido** | Volumen total de palabras del cuerpo principal. | El promedio en primera página de Google es ~1400 palabras. Contenido extenso permite cubrir espectro más amplio del tema. |
| 16 | **Tabla de Contenidos Vinculada** | Índice interno con anclajes de salto HTML. | Permite a rastreadores comprender jerarquía interna y genera sitelinks en resultados de búsqueda. |
| 17 | **Palabras Clave LSI en Contenido** | Integración de términos semánticos y sinónimos mediante Indexación Semántica Latente. | Ayuda a desambiguar palabras homónimas (ej. "Apple" marca vs fruta) aportando coherencia contextual. |
| 18 | **Palabras Clave LSI en Metadatos** | Presencia de variantes semánticas en title y meta description. | Sirve como señal preliminar para filtros del motor antes del renderizado completo de la página. |
| 19 | **Cobertura Temática Profunda** | Nivel de exhaustividad y desarrollo analítico del tema. | Alta correlación entre profundidad de información provista y posicionamiento en posiciones líderes de la SERP. |
| 20 | **Coincidencia de Entidades** | Adecuación del texto con nodos del Grafo de Conocimiento. | Si la página describe de forma consistente y estructurada una entidad oficial, el algoritmo otorga beneficio directo de clasificación. |
| 21 | **Procesamiento de Hummingbird** | Algoritmo de Google centrado en interpretación de lenguaje natural contextual. | Reorienta la evaluación de términos mecánicos hacia comprensión semántica profunda de frases estructuradas. |
| 22 | **Prominencia de Palabra Clave** | Ubicación del término principal en secciones de apertura del texto. | La presencia del término en las primeras 100 palabras está positivamente correlacionada con posiciones de autoridad. |
| 23 | **Palabra Clave en H2, H3** | Inclusión de keyword o variantes en subtítulos. | Estructura la lectura lógica y actúa como señal de relevancia temática complementaria para Googlebot. |
| 24 | **Calidad de Redacción y Gramática** | Ausencia de errores ortográficos, sintácticos o de puntuación. | Indicador cualitativo de primer orden para medir esfuerzo de edición. Contenidos con mala gramática sufren devaluación. |
| 25 | **Contenido Útil Diferenciado** | Nivel de utilidad real frente a textos genéricos o vacíos. | Google distingue entre redacción formal óptima y valor empírico del texto para resolver una necesidad humana real. |
| 26 | **Contenido con Insights Únicos** | Inclusión de valoraciones originales, perspectivas novedosas o análisis propios. | Penaliza severamente sitios que solo resumen o reescriben contenidos de terceros sin aportar valor agregado. |
| 27 | **Título Coherente y No Exagerado** | Redacción descriptiva libre de sensacionalismo. | Títulos "clickbait" que exageran la realidad degradan la confianza y generan rebotes rápidos (pogosticking). |
| 28 | **Estructuración del Formato** | Distribución visual con encabezados, viñetas y negritas. | Facilita legibilidad y simplifica procesamiento del documento para lectores humanos y robots de indexación. |
| 29 | **Originalidad de la Información** | Aportación de datos de campo, investigación primaria o análisis no disponibles en la red. | El motor prioriza indexación y visibilidad de fuentes primarias sobre portales satélites de curación de contenidos. |

### 1.3 Factores de Página: Técnicos y Estructurales (IDs 30-54)

La solidez de la infraestructura de código en cada URL garantiza que los motores rastreen e indexen sin obstáculos, protegiendo la navegación del usuario.

| ID | Parámetro | Mecanismo Técnico | Impacto y Aplicación |
|----|-----------|-------------------|----------------------|
| 30 | **Velocidad de Carga HTML** | Tiempo del servidor en entregar el documento base e iniciar renderizado. | Factor directo de ordenación. Rendimiento lento degrada UX y reduce la tasa de rastreo permitida para el bot. |
| 31 | **Uso de AMP** | Versiones ultraligeras de páginas para navegación móvil. | No es factor directo de clasificación general, pero resulta indispensable para acceder a carruseles de noticias en móviles. |
| 32 | **Contenido Duplicado On-Site** | Bloques idénticos de texto en diferentes URLs del mismo dominio. | Diluye relevancia y confunde al motor sobre qué página jerarquizar, devaluando el rendimiento de todo el conjunto. |
| 33 | **Marcado de Canonicalización** | `<link rel="canonical" href="...">` en cabecera HTML. | Consolida autoridad de enlaces duplicados y dirige formalmente a Googlebot hacia la URL designada como fuente principal. |
| 34 | **Optimización de Imágenes** | Configuración de atributos técnicos en etiquetas de imagen. | Google extrae señales semánticas mediante nombre de archivo, atributo alt, título y descripción de la imagen. |
| 35 | **Recencia del Contenido (Caffeine)** | Fecha de edición/renovación en encabezados HTTP. | Favorece selectivamente a contenidos actualizados para consultas sensibles a la frescura informativa. |
| 36 | **Magnitud de la Actualización** | Proporción de texto modificado, añadido o eliminado. | La reestructuración profunda de párrafos transmite señal de frescura mucho más potente que correcciones ortográficas menores. |
| 37 | **Historial de Actualizaciones** | Frecuencia cronológica de renovación de la página. | Indica al motor que la página tiene mantenimiento activo, estimulando frecuencia de rastreo más rápida. |
| 38 | **Diseño Responsivo para Móviles** | Adaptabilidad dinámica de la interfaz a múltiples resoluciones. | Tras "Mobilegeddon", sitios sin optimización móvil sufren caídas drásticas de posicionamiento global. |
| 39 | **Usabilidad en Móviles** | Telemetría reportada sobre facilidad de lectura y pulsación en smartphones. | Fuentes diminutas o elementos táctiles próximos se notifican en GSC y penalizan la visibilidad. |
| 40 | **Contenido Oculto en Móviles** | Ocultamiento de texto tras menús desplegables para pantallas pequeñas. | Google permite su uso por razones de UX, pero prioriza indexación del contenido visible sin interacción. |
| 41 | **Contenido Suplementario Útil** | Herramientas dinámicas que complementan la lectura (ej. simuladores). | Eleva notablemente el tiempo de permanencia y la calidad general percibida de la página. |
| 42 | **Contenido Oculto tras Pestañas** | Menús interactivos de navegación interna para segmentar texto. | Los motores rastrean e indexan este contenido, pero con puntuación de peso menor que el texto principal expuesto. |
| 43 | **Gestión de Cookies No Intrusiva** | Diseño adaptado de avisos legales de cookies y privacidad. | Interstitials o popups invasivas que impiden visibilidad del contenido al cargar causan penalizaciones de experiencia. |
| 44 | **Palabra Clave en la URL** | Inclusión del término principal en la dirección web. | Factor de relevancia menor. Facilita usabilidad y ayuda a catalogar inicialmente el recurso. |
| 45 | **Categorización en la Ruta de URL** | Subdirectorios lógicos en la estructura de URL. | Señal complementaria de ordenación jerárquica; proporciona contexto claro sobre taxonomía del dominio. |
| 46 | **Referencias a Fuentes de Autoridad** | Enlace saliente hacia portales académicos, institucionales o gubernamentales. | El uso de citas rigurosas y enlaces externos de calidad actúa como señal de veracidad e investigación profunda. |
| 47 | **Listas Viñetadas y Numeradas** | Formateo de contenido en listas jerárquicas. | Rompe la densidad del texto y simplifica la extracción de bloques estructurados por Google para rich snippets. |
| 48 | **Prioridad en XML Sitemap** | Jerarquía de importancia asignada a la URL en el sitemap. | Orienta a los robots sobre la relevancia relativa de cada página dentro del conjunto de URLs del sitio. |
| 49 | **Exceso de Enlaces Salientes** | Densidad excesiva de hipervínculos hacia páginas externas. | Satura la usabilidad y diluye el flujo interno de PageRank de la URL, degradando la calidad asignada. |
| 50 | **Palabras Clave Concurrentes** | Volumen de términos alternativos para los que la página posiciona. | Indica riqueza de vocabulario y profundidad del tratamiento del tema central, fortaleciendo el ranking principal. |
| 51 | **Madurez o Edad de la Página** | Antigüedad de la URL específica en el índice de Google. | Páginas antiguas con historial limpio resisten mejor oscilaciones algorítmicas que URLs recién creadas. |
| 52 | **Longitud de la URL** | Número total de caracteres de la dirección. | URLs excesivamente extensas o con múltiples variables de seguimiento dificultan usabilidad y reducen tasa de rastreo. |
| 53 | **Profundidad de la Ruta de URL** | Niveles de subcarpetas hasta la raíz. | Páginas más próximas a la raíz reciben mayor proporción de Link Equity y gozan de rastreo prioritario. |
| 54 | **Relevancia de Categoría** | Clasificación temática del directorio primario bajo el que se publica. | Ayuda a rastreadores a contextualizar semánticamente el post mediante su ubicación en la estructura del sitio. |

### 1.4 Factores de Sitio Web (IDs 55-60)

La solidez reputacional y técnica a nivel de dominio actúa como paraguas de confianza que condiciona cada URL individual.

| ID | Parámetro | Mecanismo Técnico | Impacto y Aplicación |
|----|-----------|-------------------|----------------------|
| 55 | **Valor Unificado del Dominio** | Consistencia global en calidad del contenido de todas las URLs. | Un dominio libre de páginas basura transfiere señal positiva general que beneficia a todo el conjunto. |
| 56 | **Arquitectura Interna de Enlaces** | Estructuración lógica que conecta páginas jerárquicamente (ej. Silo). | Distribuye homogéneamente el Link Equity y asegura correcto rastreo de páginas profundas. |
| 57 | **Estabilidad del Servidor (Uptime)** | Porcentaje de tiempo en que el servidor está accesible. | Caídas frecuentes o tiempos prolongados de desconexión impiden el rastreo y provocan caídas masivas. |
| 58 | **Presencia de Páginas Legales** | Términos de servicio, políticas de privacidad y cookies. | Evaluadas positivamente como señales de que se trata de una empresa o proyecto transparente y legítimo. |
| 59 | **Integración de Analíticas Oficiales** | Uso de Google Analytics y Google Search Console. | No eleva posiciones directamente, pero demuestra mantenimiento profesional activo y facilita indexación rápida. |
| 60 | **Consistencia Responsiva Global** | Adaptabilidad móvil uniforme en el 100% de las páginas del dominio. | Evita que secciones aisladas del sitio dañen la valoración general del dominio bajo auditorías móviles. |

### 1.5 Factores de Backlinks (IDs 61-85)

Los enlaces entrantes representan la señal externa más potente para certificar relevancia e influencia en la red global. El valor transferido depende directamente de la autoridad y afinidad temática del emisor.

| ID | Parámetro | Mecanismo Técnico | Impacto y Aplicación |
|----|-----------|-------------------|----------------------|
| 61 | **Edad del Dominio Emisor** | Antigüedad cronológica de la web externa que emite el backlink. | Enlaces de dominios históricos y consolidados transmiten peso de autoridad y confianza sustancialmente mayor. |
| 62 | **Número de Páginas que Enlazan** | Volumen bruto de URLs individuales que dirigen enlaces al sitio. | Google comprime enlaces duplicados de una misma web; el volumen de dominios de referencia únicos tiene mayor impacto. |
| 63 | **Enlaces desde Dominios .edu y .gov** | Backlinks desde extensiones reservadas a educación y gobierno. | Gozan de autoridad algorítmica intrínseca muy elevada. Transmiten grado superior de confianza al perfil de enlaces. |
| 64 | **Enlaces de Competidores Directos** | Backlinks de dominios que compiten por las mismas keywords. | Indica que la competencia reconoce la validez del sitio, otorgando impulso de autoridad en el nicho. |
| 65 | **Enlaces Incrustados en Anuncios** | Hipervínculos en piezas promocionales o banners pagados. | Deben incluir estrictamente `rel="nofollow"` para no infringir directrices de manipulación de enlaces. |
| 66 | **Enlaces con Marcado Publicitario** | Uso obligatorio de `rel="sponsored"`. | Evita penalizaciones automatizadas al categorizar explícitamente enlaces comerciales en el HTML. |
| 67 | **Texto de Ancla de Enlace Interno** | Keywords empleadas para conectar URLs del propio dominio. | Proporciona señal potente para definir de qué trata la página destino sin riesgo de penalización por sobreoptimización. |
| 68 | **Ubicación del Link en el Contenido** | Posición física del enlace en la estructura HTML de la página origen. | Enlaces contextuales en el cuerpo principal transmiten mucho más valor que enlaces en footer o barras laterales. |
| 69 | **Afinidades de Nicho del Dominio** | Grado de coincidencia sectorial entre dominio emisor y receptor. | Un enlace de una web del mismo nicho industrial es infinitamente más valioso que enlaces de temáticas no relacionadas. |
| 70 | **Relevancia a Nivel de Página** | Afinidad temática específica de la URL que contiene el enlace. | Un post con afinidad temática exacta transmite mayor relevancia semántica contextualizada a la página enlazada. |
| 71 | **Palabra Clave en Título Emisor** | Presencia del término en `<title>` de la web que enlaza. | Maximiza fuerza del enlace al certificar que la página origen trata sustancialmente el tema de destino. |
| 72 | **Velocidad de Enlaces Positiva** | Ritmo constante de crecimiento en captación de dominios de referencia. | Señal de popularidad orgánica y frescura que estimula mejora del posicionamiento en SERP. |
| 73 | **Velocidad de Enlaces Negativa** | Descenso prolongado o desvinculación masiva de enlaces. | Alerta al motor de que el sitio pierde relevancia o su contenido está obsoleto, provocando caídas de tráfico. |
| 74 | **Enlaces desde Páginas Hub** | Backlinks de directorios líderes o curadores clave del sector. | Ser mencionado en catálogo de recursos de autoridad sectorial transfiere gran valor de relevancia especializada. |
| 75 | **Enlaces de Sitios con Alta Autoridad** | Hipervínculos desde portales con PageRank masivo. | Transfieren instantáneamente una porción notable de fuerza, elevando competitividad del dominio receptor. |
| 76 | **Enlaces desde Redirecciones 301** | Autoridad transferida a través de redirecciones permanentes. | Transmiten el Link Equity original de forma eficaz, aunque con pequeña pérdida por fricción técnica. |
| 77 | **Implementación de Schema en Web Emisora** | Uso de datos estructurados por la página que contiene el enlace. | Ayuda a robots a procesar con mayor rapidez el propósito exacto y contexto semántico de la recomendación. |
| 78 | **Confianza del Emisor (TrustRank)** | Proximidad del dominio que enlaza a nodos semilla de confianza de Google. | A mayor TrustRank de la fuente, mayor protección y autoridad transferida al receptor ante penalizaciones. |
| 79 | **Densidad de Enlaces Salientes del Emisor** | Volumen de links salientes en la página que enlaza. | El valor del enlace se diluye a medida que comparte espacio con más links; un link solitario en post de calidad es óptimo. |
| 80 | **Enlaces en Hilos de Foros** | Vínculos naturales en comunidades online o foros. | Valor técnico bajo, pero indispensables para aportar naturalidad y diversidad al perfil de enlaces. |
| 81 | **Extensión del Contenido Emisor** | Longitud total del artículo que aloja el backlink. | Un enlace en post profundo de más de 1000 palabras tiene mayor impacto que un link en párrafo aislado. |
| 82 | **Calidad del Texto de Origen** | Nivel de redacción y valor técnico de la página emisora. | Enlaces de textos bien escritos y con buen SEO tienen peso superior frente a enlaces de textos low-quality. |
| 83 | **Compresión de Enlaces Sitewide** | Algoritmo que comprime enlaces repetitivos en todo un portal. | Google unifica enlaces repetidos en headers, menús o footers de un mismo sitio para que cuenten como un único enlace. |
| 84 | **Reinicio de Historial por Expiración** | Anulación del valor de enlaces tras vencer el registro del dominio. | Si el dominio expira y es registrado por un tercero, Google puede resetear su historial, inhabilitando enlaces previos. |
| 85 | **Diversidad de Enlaces** | Variedad en tipos de fuentes y extensiones de dominios enlazados. | Perfil saludable requiere equilibrio de enlaces de blogs, prensa, foros y directorios para evitar sospechas de manipulación. |

### 1.6 Interacción de Usuario y Señales de Marca (IDs 86-98)

La telemetría en tiempo real sobre cómo interactúan los visitantes con las URLs y el reconocimiento de marca offline proporcionan señales de satisfacción y relevancia real.

| ID | Parámetro | Mecanismo Técnico | Impacto y Aplicación |
|----|-----------|-------------------|----------------------|
| 86 | **Comentarios Reales de Usuarios** | Volumen y recurrencia de interacciones en comentarios. | Un hilo activo añade keywords de forma natural y demuestra engagement real. Google confirma impacto positivo. |
| 87 | **Tiempo de Permanencia (Dwell Time)** | Intervalo entre clic en SERP y regreso a Google. | Google monitoriza la duración; visitas prolongadas validan que el contenido resolvió la necesidad con éxito. |
| 88 | **Algoritmo RankBrain** | Procesamiento inteligente que clasifica según satisfacción del usuario. | Reordena dinámicamente los resultados priorizando URLs que consiguen mayor satisfacción interactiva real. |
| 89 | **Tasa de Rebote (Bounce Rate)** | Porcentaje de visitas que abandonan sin interactuar. | Tasas anormalmente elevadas alertan sobre fallos de usabilidad o incoherencia título-contenido. |
| 90 | **Efecto Pogosticking** | Volver rápidamente a Google para abrir otra página. | Señal sumamente negativa: indica que la página no resolvió la consulta, destruyendo posicionamiento para ese término. |
| 91 | **Reputación en Sitios Externos** | Valoraciones en portales de opinión de autoridad (Yelp, Trustpilot). | Influye transversalmente en juicios automáticos del algoritmo sobre legitimidad y calidad del negocio. |
| 92 | **Usabilidad General de la Interfaz** | Facilidad técnica de navegación e interacción en todo el dominio. | Errores constantes o flujos confusos provocan malas señales de comportamiento que erosionan posicionamiento. |
| 93 | **Texto de Ancla con Nombre de Marca** | Predominio de anclajes de marca (Marca, marca.com) en perfil de backlinks. | Es la señal más clara de perfil de enlaces natural. Exceso de anclajes con keyword exacta es penalizado. |
| 94 | **Búsquedas Directas de Marca** | Volumen de consultas que contienen exactamente el nombre de la empresa. | Google interpreta estas búsquedas directas como fuerte indicador de reputación y relevancia de marca real. |
| 95 | **Búsqueda Combinada Marca + Palabra** | Consultas que asocian la marca con un producto o nicho (ej. "Marca SEO"). | Consolida la jerarquía del sitio como referente indiscutible y líder temático dentro de esa categoría. |
| 96 | **Presencia Activa en Facebook** | Cuenta de empresa verificada con volumen saludable de interacciones. | Ayuda a evaluadores de calidad a certificar que la marca posee infraestructura social legítima. |
| 97 | **Presencia Activa en Twitter / X** | Perfil corporativo activo con seguidores reales y menciones sectoriales. | Valida al sitio como actor dinámico de la industria, influyendo en métricas cualitativas. |
| 98 | **Percepción Online de la Marca** | Sentimiento general y menciones sin enlace de la empresa en la red. | El algoritmo procesa el tono de las menciones textuales para categorizar nivel de reputación sectorial. |

### 1.7 Reglas Especiales del Algoritmo (IDs 99-116)

Google aplica filtros contextuales específicos y altera las SERPs de forma dinámica según temática, seguridad, geolocalización o estacionalidad de la consulta.

| ID | Parámetro | Mecanismo Técnico | Impacto y Aplicación |
|----|-----------|-------------------|----------------------|
| 99 | **Query Deserves Freshness (QDF)** | Impulso de visibilidad temporal ante picos de búsquedas estacionales. | El algoritmo desplaza contenido histórico estable para destacar noticias de última hora y posts recientes. |
| 100 | **Historial de Búsqueda del Usuario** | Alteración de resultados según navegación previa. | Google personaliza SERPs basándose en cookies y comportamiento de búsqueda previo registrado. |
| 101 | **Filtro Safe Search** | Exclusión de contenidos en resultados con filtros activos. | URLs con palabras malsonantes o material explícito quedan fuera de SERPs con control parental. |
| 102 | **Clasificación Transaccional** | Ajuste del diseño de SERP para búsquedas con intención de compra. | Google inyecta widgets interactivos (comparadores, reservas) por encima de la primera posición orgánica. |
| 103 | **Vince Update (Big Brand Preference)** | Preferencia algorítmica por grandes marcas en búsquedas amplias. | Otorga beneficio de visibilidad a dominios con enorme autoridad corporativa offline para keywords genéricas. |
| 104 | **Monopolio Controlado de Marca** | Despliegue de múltiples URLs del mismo dominio en SERP. | Si el usuario busca un término que incluye la marca, Google presenta varias páginas del mismo dominio. |
| 105 | **Geolocalización por IP y ccTLD** | Priorización geográfica según procedencia del usuario. | El algoritmo da preferencia a páginas hospedadas localmente e identificadas con ccTLD territoriales. |
| 106 | **Estándares YMYL (Your Money or Your Life)** | Criterios drásticos de evaluación para temáticas sensibles. | Consultas sobre medicina, finanzas o leyes exigen niveles máximos de rigor factual y acreditación científica. |
| 107 | **Denuncias DMCA Activas** | Filtro penalizador ante reclamaciones por derechos de autor. | Google desciende drásticamente o desindexa dominios con notificaciones legítimas por plagio. |
| 108 | **Bigfoot Update (Domain Diversity)** | Garantía de diversidad en SERP controlando dominios repetidos. | Evita que un único portal domine las primeras 10 posiciones, asegurando exposición de diferentes marcas. |
| 109 | **Resultados de Intención Local Prioritarios** | Inyección de Google Local Pack por delante de SERP orgánica. | Búsquedas que denotan proximidad física sitúan negocios geolocalizados en el espacio más visible. |
| 110 | **Bloque Top Stories** | Sección destacada de actualidad inyectada dinámicamente en SERP. | Ciertas palabras de actualidad activan este cajón destacado, requiriendo indexación ultra veloz para noticias. |
| 111 | **Tarjetas de Google Shopping** | Inyección de catálogo comercial directo en búsqueda orgánica. | Muestra productos con precio, foto y opiniones en SERPs transaccionales, desplazando navegación tradicional. |
| 112 | **Integración Visual de Imágenes** | Fusión de imágenes en resultados generales de texto. | Páginas con material gráfico de alta calidad se benefician de clics complementarios mediante miniaturas. |
| 113 | **Payday Loans Update** | Algoritmo antiposting masivo para nichos altamente explotados. | Aplica filtros semánticos y técnicos extremadamente agresivos para búsquedas financieras o de apuestas. |
| 114 | **Ajustes Estacionales** | Adaptación de clasificaciones orgánicas a tendencias masivas estacionales. | Modifica temporalmente el peso de ciertos parámetros para alinearse con momentos álgidos de compra. |
| 115 | **Evaluaciones de Calidad Humana** | Intervenciones del equipo de evaluadores de Google (Quality Raters). | Sus análisis entrenan y calibran las actualizaciones algorítmicas, aunque no bajan posiciones manualmente. |
| 116 | **Relevancia Categórica de la Consulta** | Ajuste entre directorio general del post y la intención de búsqueda. | El motor analiza si la URL forma parte de una categoría con autoridad en el tema antes de autorizar posicionamiento. |

### 1.8 Factores de Webspam On-Site y Off-Site (IDs 117-128)

Las técnicas destinadas a manipular artificialmente las directrices de los motores desencadenan filtros de desvalorización automáticos y penalizaciones manuales severas.

| ID | Parámetro | Mecanismo Técnico | Impacto y Aplicación |
|----|-----------|-------------------|----------------------|
| 117 | **Hackeo de Servidor** | Vulneración de seguridad que inserta código de terceros. | Provoca desindexación inmediata y absoluta del dominio para proteger a usuarios de malware o estafas. |
| 118 | **Captación Veloz de Enlaces Artificiales** | Incremento drástico y antinatural en adquisición de backlinks low-quality. | Activa filtros algorítmicos automáticos que devalúan enlaces sospechosos o aplican penalizaciones directas. |
| 119 | **Perfil de Enlaces de Baja Calidad** | Alta presencia de enlaces en comentarios de spam o perfiles vacíos. | Indica ejecución de esquemas automatizados black hat, anulando el valor de la estrategia de enlaces. |
| 120 | **Enlaces de Temáticas No Relacionadas** | Alta concentración de backlinks sin afinidad conceptual. | Dispara sospechas de compra masiva de enlaces e incrementa posibilidad de penalización manual. |
| 121 | **Advertencia de Enlaces No Naturales** | Mensaje formal en Google Search Console. | Antesala técnica de caída devastadora de posiciones. Requiere desautorizar enlaces con disavow inmediato. |
| 122 | **Enlaces en Directorios Spam** | Backlinks mediante herramientas automáticas en catálogos inútiles. | Google devalúa estos enlaces sistemáticamente para evitar manipulación de PageRank. |
| 123 | **Redes de Blogs bajo Misma IP Clase C** | Recibir backlinks de sitios que comparten segmento IP. | Permite a Google identificar PBN (Private Blog Networks) creadas artificialmente para transferir autoridad. |
| 124 | **Anclajes Venenosos** | Enlaces de spam masivo con palabras farmacéuticas o adultas. | Indica seguridad comprometida o ataque de SEO negativo. Provoca pérdidas severas de tráfico. |
| 125 | **Pico Temporal de Enlaces Patentado** | Patente de detección de inyecciones masivas temporales de hipervínculos. | Evalúa estadísticamente si el crecimiento temporal es natural. Si no, inhabilita la transmisión de PageRank. |
| 126 | **Enlaces en Directorios de Artículos** | Backlinks de plataformas masivas de distribución de textos. | Penaliza notas de prensa y artículos sobreoptimizados publicados masivamente sin filtros de calidad. |
| 127 | **Contenido Copiado o Raspado** | Plagio automatizado o duplicación de textos de otros portales. | El algoritmo omite indexación de URLs copiadas y degrada puntuación de calidad de todo el dominio infractor. |
| 128 | **Enlaces Masivos en Pie de Página** | Enlaces repetitivos colocados masivamente en zonas bajas del HTML. | Google comprime este patrón de manipulación estructural de PageRank y puede devaluar autoridad interna del dominio. |

**Protocolo de Auditoría SEO:** Para `/geo-seo-pro seo-factors <url>`, ejecutar checklist de los 128 factores marcando ✅ (cumple), ⚠️ (mejorable), ❌ (no cumple), N/A (no aplica). Priorizar correcciones por nivel de impacto y factibilidad.

---

## PARTE 2: CORE WEB VITALS — ESTÁNDARES TÉCNICOS Y RANGOS DE RENDIMIENTO

Los Core Web Vitals representan la telemetría oficial de Google para evaluar la calidad técnica de la interacción de usuarios en tiempo real. Se recopilan datos reales a través de Chrome User Experience Report (CrUX) para clasificar cada URL en tres estadios de rendimiento. Un sitio que resuelva la intención de búsqueda con contenido excelente pero que presente diseño lento, inestable o con retrasos interactivos experimentará un rezago progresivo en las clasificaciones.

### 2.1 Métricas y Rangos

| Métrica | Dimensión Evaluada | Rango Óptimo (Bueno) | Rango de Advertencia | Rango Crítico (Pobre) |
|---------|-------------------|----------------------|----------------------|------------------------|
| **LCP** (Largest Contentful Paint) | Velocidad de carga percibida. Tiempo para visualizar el elemento más grande de la pantalla. | ≤ 2.5s | 2.5s - 4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | Capacidad de respuesta interactiva. Retardo total antes de que el navegador actualice la pantalla tras una acción táctil o clic. | ≤ 200ms | 200ms - 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | Estabilidad visual del diseño. Cuantifica movimientos inesperados de elementos durante el renderizado. | ≤ 0.1 | 0.1 - 0.25 | > 0.25 |

### 2.2 Fórmula CLS

El CLS se procesa matemáticamente evaluando el impacto del movimiento de elementos en el viewport:

```
CLS = Σ (Fracción de Impacto × Fracción de Distancia)

Fracción de Impacto = superficie del viewport que experimenta cambio posicional
Fracción de Distancia = longitud máxima desplazada / dimensión más grande del viewport
```

### 2.3 Optimización Técnica Quirúrgica

**Optimización del LCP:**
- Comprimir y redimensionar estrictamente todas las imágenes principales, priorizando formatos modernos (AVIF, WebP).
- Configurar CDN con almacenamiento en caché perimetral.
- Precargar la imagen destacada (hero image) en cabecera HTML: `<link rel="preload" as="image" href="hero.webp">`.
- Eliminar CSS o JS que bloquee el renderizado inicial.
- Asegurar tiempo de respuesta de servidor rápido (TTFB < 800ms).

**Optimización del INP:**
- Aligerar el hilo principal del navegador difiriendo scripts secundarios que no participen en el pintado inicial.
- Trocear tareas largas de JavaScript mediante técnicas de planificación de frames.
- Priorizar procesamiento interactivo mediante `requestIdleCallback`.
- Optimizar ejecución de controladores de eventos de botones y formularios.
- Minimizar llamadas repetitivas de telemetría o analíticas externas durante los instantes iniciales de navegación.

**Optimización del CLS:**
- Declarar explícitamente dimensiones geométricas (width y height) en el HTML de TODAS las imágenes, vídeos y banners publicitarios dinámicos.
- Reservar espacio para embeds (iframes, videos) antes de su carga.
- Usar `font-display: swap` para evitar FOIT (Flash of Invisible Text).
- Evitar insertar contenido dinámico sobre contenido existente sin interacción del usuario.
- Predefinir dimensiones de contenedores de anuncios.

### 2.4 Protocolo de Diagnóstico

Para `/geo-seo-pro core-web-vitals <url>`:
1. Obtener métricas de campo reales vía PageSpeed Insights API
2. Ejecutar Lighthouse audit para diagnóstico de laboratorio
3. Verificar informe CrUX si está disponible
4. Identificar elementos específicos que causan puntuación subóptima
5. Proporcionar recomendaciones quirúrgicas con código específico
6. Asignar puntuación Core Web Vitals: Bueno (90-100), Necesita Mejora (50-89), Pobre (0-49)

---

## PARTE 3: E-E-A-T Y SISTEMA DE CONTENIDO ÚTIL

Google prioriza de manera sistemática los contenidos que demuestran claro rigor humano y profesional en su concepción, devaluando páginas con sesgo manipulativo centrado exclusivamente en posicionar para algoritmos de búsqueda.

### 3.1 El Ecosistema de Validación E-E-A-T

E-E-A-T representa el marco analítico que define la legitimidad de un creador de contenido y de la web donde publica:

| Dimensión | Definición | Cómo Demostrarlo |
|-----------|------------|------------------|
| **Experiencia (Experience)** | Evidencia de conocimiento real de primera mano y contacto directo con la temática. | Fotos originales de proyectos propios, anécdotas vividas, análisis de pruebas empíricas ejecutadas personalmente. |
| **Expertise (Experiencia Técnica)** | Credenciales de formación formal, certificaciones reconocidas o bagaje técnico contrastado del firmante. | Publicar credenciales verificables, certificaciones, enlaces a publicaciones académicas o técnicas previas. |
| **Authoritativeness (Autoridad)** | Grado de liderazgo y reputación del autor y la empresa en su sector digital. | Ser citado por otras organizaciones destacadas del área como fuente técnica de consulta recurrente. |
| **Trustworthiness (Confianza)** | El núcleo transversal del modelo de calidad. Incluye seguridad técnica, transparencia y honestidad factual. | HTTPS, transparencia sobre quién escribe, acceso claro a soporte, datos factuales verificables, políticas legales visibles. |

### 3.2 El Sistema de Contenido Útil (Helpful Content System)

El Helpful Content System es un algoritmo que evalúa la calidad general del dominio completo para clasificarlo como "útil para humanos" o "creado para buscadores". El agente debe aplicar un protocolo de autoevaluación continua basado en tres ejes analíticos críticos:

```
                    EVALUACIÓN DE CONTENIDO ÚTIL
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
   ¿QUIÉN CREÓ?         ¿CÓMO SE CREÓ?        ¿POR QUÉ CREÓ?
(Acreditación Humana)  (Garantía Técnica)   (Propósito de Valor)
         │                    │                    │
 • Firmas de autor     • IA declarada      • Resuelve intención
   claras                con valor           de búsqueda real
 • Biografías          • Fuentes citadas   • Evita clickbait
   enlazadas             y fiables           vacío
 • Perfiles sociales   • Datos originales  • Aporta valor
   vinculados            demostrados         duradero
```

**¿Quién creó el contenido?** Exige transparencia total en la firma de cada página. Los posts deben incluir "bylines" o bloques de autoría legibles que enlacen a biografías de perfiles donde se expongan con total honestidad estudios, experiencia y por qué son competentes para desarrollar la temática.

**¿Cómo se creó el contenido?** Demanda declarar con honestidad los procesos técnicos detrás del texto. Si se empleó inteligencia artificial para redactar borradores o compilar datos, esto debe ser evidente para el visitante a través de avisos de transparencia. Se debe acreditar la veracidad de los datos citando de forma inequívoca las fuentes primarias y adjuntando pruebas de contraste empírico.

**¿Por qué se creó el contenido?** Determina que el post tiene como único fin aportar valor a las personas de forma duradera. Se debe evitar la redacción masiva de contenidos sobre temas de tendencia inconexos con la temática habitual del negocio, con el único fin de capturar tráfico residual en búsquedas orgánicas. El visitante debe terminar la lectura sintiendo que ha completado con éxito su tarea sin requerir una nueva búsqueda.

### 3.3 Protocolo de Evaluación E-E-A-T

Para `/geo-seo-pro e-e-a-t <url>`:
1. Verificar presencia de autoría (bylines, biografías enlazadas, perfiles sociales)
2. Evaluar credenciales del autor contrastables (formación, certificaciones)
3. Analizar transparencia sobre uso de IA en la creación
4. Verificar citación de fuentes primarias en afirmaciones clave
5. Comprobar señales de experiencia de primera mano (fotos, datos propios, casos reales)
6. Revisar seguridad del sitio (HTTPS, páginas legales, contacto)
7. Detectar posible contenido masivo solo para SEO (temas inconexos, sin valor real)
8. Asignar puntuación E-E-A-T: Excelente (90-100), Bueno (70-89), Adecuado (50-69), Pobre (30-49), Crítico (0-29)

---

## PARTE 4: SCHEMA JSON-LD PARA BÚSQUEDAS TRADICIONALES Y MODELOS DE IA

La inyección de código estructurado JSON-LD en el backend del sitio permite que tanto los motores tradicionales como los modelos generativos de IA decodifiquen y entiendan con total precisión el significado conceptual detrás de cada elemento textual del portal.

### 4.1 Esquemas Clave de Alto Rendimiento

| Esquema JSON-LD | Caso de Uso | Directrices Técnicas Obligatorias |
|-----------------|-------------|-----------------------------------|
| **BlogPosting / Article** | Define el post principal, identificando al autor y fechas exactas de edición. | Incluir `mainEntityOfPage`, `author`, `publisher`, `datePublished`, `dateModified` y recurso gráfico de portada (`image`). |
| **FAQPage** | Estructura bloques de preguntas y respuestas cortas para recuperación conversacional por IAs. | Las preguntas y respuestas del JSON-LD deben guardar total coincidencia textual con los bloques visibles para el usuario. |
| **HowTo** | Detalla guías y tutoriales resueltos paso a paso con herramientas y duraciones. | Reservar exclusivamente para explicaciones secuenciales de carácter práctico. Evitar en posts analíticos generales. |
| **Organization** | Certifica la identidad fiscal o corporativa del negocio titular de la página. | Integrar en la home principal. Usar `sameAs` para enlazar perfiles verificados de redes sociales y directorios oficiales. |
| **Person** | Identifica credenciales profesionales, formación y perfiles del autor de forma rastreable. | Utilizar enlaces externos en `sameAs` para certificar experiencia técnica y potenciar E-E-A-T. |
| **Product** | Permite inyectar precios, stocks y variaciones comerciales en las búsquedas. | Mantener actualizados valores económicos y opiniones reales. Inhabilitar comentarios manipulados o falsificados. |
| **LocalBusiness** | Posiciona el negocio físico en área geográfica determinada en búsquedas locales. | Declarar dirección física precisa, teléfono y datos que coincidan milimétricamente con Google Business Profile. |

### 4.2 Ejemplo Canónico: BlogPosting con sameAs

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://tusitio.com/posicionamiento-geo"
  },
  "headline": "Guía de Optimización GEO para Inteligencia Artificial",
  "image": "https://tusitio.com/images/geo-guide.jpg",
  "datePublished": "2026-01-15T08:00:00+01:00",
  "dateModified": "2026-05-20T10:30:00+02:00",
  "author": {
    "@type": "Person",
    "name": "Dr. Carlos Mendoza",
    "url": "https://tusitio.com/autores/carlos-mendoza",
    "sameAs": "https://www.linkedin.com/in/carlos-mendoza-phd"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Agencia GEO Global",
    "logo": {
      "@type": "ImageObject",
      "url": "https://tusitio.com/logo.png"
    }
  }
}
```

La propiedad `sameAs` dentro de los esquemas `Person` u `Organization` conecta la marca o autor con perfiles públicos de autoridad de terceros (Wikipedia, LinkedIn, bases de datos académicas), dotando de una señal contundente de autenticidad y consolidando su posición dentro del Grafo de Conocimiento del motor de búsqueda.

### 4.3 Esquemas de Bajo Impacto y Riesgos de Sobreoptimización

| Esquema | Evaluación |
|---------|------------|
| **BreadcrumbList** | Asiste en visualización de rutas lógicas en resultados tradicionales, pero resulta **irrelevante para modelos de IA generativos**, que ignoran estas estructuras posicionales. |
| **Event** | Cuenta con rápida caducidad de calendario que resta influencia en recuperación semántica de posts evergreen. |
| **Sitelinks Search Box** | Responde a integraciones de diseño para SERPs clásicas que no intervienen en procesamiento moderno de sistemas de IA generativa. |
| **Speakable** | Diseñado para interfaces de audio antiguas, sin relevancia para IA conversacional moderna. |

**⚠️ Riesgo Crítico de Solapamiento:** Intentar forzar la inyección de múltiples marcados incompatibles como prioritarios en una misma URL (ej. saturar un blog con FAQPage + HowTo + Product) **destruye la claridad conceptual del documento**. Confunde los filtros automáticos y diluye el impacto semántico. **Regla de oro:** Aplicar exclusivamente UN único marcado primario por URL y subordinar los esquemas secundarios como dependencias lógicas.

### 4.4 Protocolo de Auditoría Schema

Para `/geo-seo-pro schema <url>`:
1. Detectar todos los esquemas JSON-LD presentes en la página
2. Validar contra especificación Schema.org (Rich Results Test)
3. Verificar campos obligatorios por tipo de esquema
4. Evaluar uso de `sameAs` en Organization y Person
5. Detectar solapamientos y conflictos entre esquemas
6. Identificar esquemas faltantes según tipo de negocio
7. Generar JSON-LD corregido o nuevo
8. Asignar puntuación Schema: Completo (90-100), Mayormente Completo (70-89), Parcial (50-69), Mínimo (30-49), Ausente (0-29)

---

## PARTE 5: GEO — GENERATIVE ENGINE OPTIMIZATION Y ARQUITECTURA RAG

La consolidación masiva de herramientas conversacionales (ChatGPT Search, Perplexity, Gemini, Claude, Google AI Overviews) está propiciando un cambio drástico en los patrones de comportamiento digital. El posicionamiento tradicional enfocado en clics a URLs está convergiendo hacia el modelo de Generative Engine Optimization (GEO): posicionar de manera prioritaria la marca dentro de la respuesta resumida que redacta la IA de forma conversacional.

### 5.1 Diferencias Fundamentales: AEO vs GEO

| Dimensión | Answer Engine Optimization (AEO) | Generative Engine Optimization (GEO) |
|-----------|----------------------------------|--------------------------------------|
| **Plataformas** | Asistentes de voz tradicionales (Alexa, Siri, Google Assistant). | LLMs y buscadores con IA (ChatGPT, Perplexity, Gemini, Claude). |
| **Longitud de Consulta** | Consultas orales breves y directas (promedio 4 palabras). | Búsquedas conversacionales ricas en contexto (promedio 23 palabras). |
| **Estructuración** | Formatos muy fijos de Q&A (pregunta/respuesta directa). | Cobertura en profundidad y diversidad de formatos lógicos orientados a síntesis. |
| **Comportamiento Usuario** | Interacciones de "cero clics": el usuario escucha y finaliza la sesión. | El usuario visualiza la respuesta del LLM y hace clic en las citas de fuente adjuntas (alto CTR). |

### 5.2 Arquitectura RAG de 3 Capas

Los motores de búsqueda de IA operan internamente sobre una arquitectura estructurada de Generación Aumentada por Recuperación (RAG). Al recibir una consulta conversacional, el motor despliega un proceso técnico de tres capas secuenciales:

```
                     FLUJO INTERNO DE BÚSQUEDA RAG
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────┐
│ CAPA 1: BÚSQUEDA SEMÁNTICA (RETRIEVAL)                          │
│ • El motor de IA escanea bases de datos vectoriales y webs       │
│ • Recupera un grupo selecto de documentos candidatos relevantes  │
├──────────────────────────────────────────────────────────────────┤
│ CAPA 2: COMPRENSIÓN Y FILTRADO DEL LLM                           │
│ • El modelo procesa y lee las estructuras de los textos origen   │
│ • Evalúa la veracidad, autoridad y rigor factual del contenido   │
├──────────────────────────────────────────────────────────────────┤
│ CAPA 3: SÍNTESIS, COMPRENSIÓN Y SINOPSIS                         │
│ • Se redacta la respuesta final en lenguaje natural conversacional│
│ • El modelo decide qué portales citar oficialmente con hiperlinks│
└──────────────────────────────────────────────────────────────────┘
```

**Principio clave:** El motor de IA prefiere extraer información de páginas que presentan una estructura de datos clara y lógica, lo que facilita mapear el contenido en forma de grafo conceptual y representarlo espacialmente en sus bases de datos vectoriales para ser recuperado sin fricciones durante las búsquedas.

---

## PARTE 6: PRINCETON GEO-BENCH — EL ESTUDIO CIENTÍFICO FUNDACIONAL

Estudio académico publicado en KDD 2024 por Princeton University, Georgia Tech, Allen Institute for AI e IIT Delhi. Analizó por primera vez qué cambios de contenido incrementan de forma real la visibilidad en respuestas con IA. Benchmark: **GEO-bench**, evaluando **10,000 consultas** en 8-9 conjuntos de datos temáticos.

### 6.1 Métricas de Medición Científica

| Métrica | Definición |
|---------|------------|
| **Position-Adjusted Word Count** | Puntuación que pondera el número total de términos extraídos del sitio que aparecen en la respuesta del LLM, asignando peso superior a palabras en secciones de apertura o más visibles de la respuesta. |
| **Subjective Impression** | Escala cualitativa que mide qué tan destacado, confiable y con qué nivel de autoridad visual se proyecta el portal ante el usuario dentro de la respuesta generada. |

### 6.2 Las 5 Estrategias GANADORAS (Resultados Empíricos)

| # | Estrategia | Incremento | Mecanismo |
|---|-----------|------------|-----------|
| 1 | **Citar Fuentes (Cite Sources)** | **+40%** | Integrar enlaces salientes de calidad y referencias explícitas a estudios de autoridad. Los LLMs confían de forma nativa en afirmaciones con claro respaldo documental a nivel de párrafo. |
| 2 | **Adición de Datos Estadísticos (Statistics Addition)** | **+40%** | Sustituir descripciones genéricas por datos cuantitativos exactos. La combinación ganadora máxima: **dato estadístico preciso + mención de la fuente de origen + año de recolección**. |
| 3 | **Adición de Citas de Expertos (Quotation Addition)** | **+35%** | Insertar declaraciones directas atribuidas con nombre, apellido y cargo a referentes sectoriales reconocidos. Los LLMs extraen prioritariamente estos fragmentos como evidencias factuales. |
| 4 | **Optimización de Fluidez (Fluency Optimization)** | **+30%** | Mejorar la coherencia sintáctica del texto, eliminando palabras innecesarias y estructurando de manera fluida el paso de las ideas. Facilita que la IA procese y reformule sin diluir el sentido original. |
| 5 | **Tono de Autoridad (Authoritative Voice)** | **+25%** | Adoptar un tono narrativo firme, directo y seguro de la información, descartando expresiones de vacilación lingüística. |

### 6.3 Las 4 Tácticas FALLIDAS

| # | Táctica | Resultado | Por Qué Fracasa |
|---|---------|-----------|-----------------|
| 1 | **Keyword Stuffing** | ❌ Impacto negativo | Forzar repetición artificial de términos por encima del 2% de densidad dañó la coherencia del contenido. Fracaso más severo del estudio en validación real con Perplexity. |
| 2 | **Simplificación Extrema (Easy-to-Understand)** | ❌ Devalúa | Reescribir textos rebajando excesivamente el vocabulario eliminó riqueza semántica y jerga especializada que los LLMs asocian con fuentes de verdadera experiencia. |
| 3 | **Relleno de Contenido (Content Padding)** | ❌ Impacto nulo | Escribir párrafos vacíos para aumentar artificialmente el recuento de palabras. Los algoritmos de síntesis resumen el texto, descartando la paja informativa. |
| 4 | **Lenguaje Persuasivo Puro** | ❌ Sin beneficio | Incorporar adjetivos subjetivos de carácter promocional no reportó beneficio frente al análisis factual objetivo que ejecutan los LLMs. |

### 6.4 El Efecto Underdog (Descubrimiento Clave)

**Los portales con menor autoridad técnica tradicional (bajo PageRank, pocos backlinks) son los que reciben el MAYOR beneficio de visibilidad proporcional en GEO al desplegar estas estrategias.** Al basarse la arquitectura RAG en la recuperación semántica de datos a nivel de fragmento, un portal modesto pero que incorpore datos estadísticos impecables, citas directas y referencias rigurosas puede **superar a marcas históricas y monopolizar el espacio de cita destacada en las respuestas de la IA**. Esto representa una ventana de oportunidad sin precedentes para sitios pequeños y medianos.

---

## PARTE 7: ESTÁNDAR llms.txt Y llms-full.txt

Los archivos `llms.txt` y `llms-full.txt` constituyen un nuevo estándar técnico diseñado para estructurar y optimizar cómo los agentes inteligentes autónomos, herramientas de desarrollo (Cursor, GitHub Copilot) y rastreadores automáticos consumen la información de un sitio web. Se sirven en formato Markdown texto plano en el directorio raíz del servidor.

### 7.1 Comparativa: llms.txt vs llms-full.txt

| Parámetro | llms.txt | llms-full.txt |
|-----------|----------|---------------|
| **Propósito** | Mapa semántico ordenado y resumido de la arquitectura del sitio. | Totalidad del contenido y documentación textual concatenado en una única interfaz. |
| **Estructura** | Listado de enlaces lógicos acompañados de una frase de descripción semántica. | Unificación de la documentación íntegra del sitio, incluyendo especificaciones de APIs. |
| **Tokens** | Sumamente ligero (< 5,000 tokens en la mayoría de webs). | Mayor huella; se recomienda < 50,000 tokens. |
| **Casos de Uso** | Portales corporativos, blogs amplios, índices de documentación. | Bibliotecas de código, referencias completas de APIs, documentación técnica profunda. |

### 7.2 Sintaxis y Requisitos de Markdown

Para que la interfaz semántica sea procesada de forma óptima, debe respetar estrictamente las reglas de sintaxis Markdown:

1. **Título Principal (H1):** Elemento de apertura obligatorio en la primera línea, detallando exactamente el nombre del proyecto o empresa.
   ```markdown
   # Nombre del Proyecto
   ```

2. **Resumen Informativo (Blockquote):** Bloque de cita inmediatamente después del título, 1-3 líneas explicando qué cubre la web.
   ```markdown
   > Somos una agencia de marketing digital especializada en SEO y GEO para empresas B2B.
   ```

3. **Secciones Lógicas (H2):** Clasifican y dividen los temas principales de la web para orientar el rastreo de la IA.
   ```markdown
   ## Servicios
   ## Blog
   ## Documentación
   ```

4. **Enlaces Anotados:** Listado de enlaces Markdown estructurados. Los enlaces deben apuntar a versiones de texto plano o Markdown (.md) de cada sección. Cada link incluye una descripción concisa sin adjetivos comerciales, extraída de metadatos o frontmatter. Longitud máxima recomendada: **300 caracteres**.
   ```markdown
   - [Guía de SEO Técnico](https://tusitio.com/blog/seo-tecnico.md): Fundamentos de rastreo, indexación y arquitectura web para optimización técnica.
   - [Estrategia GEO 2026](https://tusitio.com/blog/geo-2026.md): Estrategias de Generative Engine Optimization basadas en el estudio Princeton GEO-bench.
   ```

### 7.3 Integración en Servidores y HTTP Headers

**HTTP Link Header:**
```
Link: <https://tusitio.com/llms.txt>; rel="llms-txt", <https://tusitio.com/llms-full.txt>; rel="llms-full-txt"
```

**X-Llms-Txt Header (conveniencia):**
```
X-Llms-Txt: /llms.txt
```

**Compatibilidad .well-known:** Además de hospedar en raíz `/llms.txt`, habilitar una redirección o clon en la ruta `/.well-known/llms.txt` para asegurar compatibilidad con herramientas que operan bajo este estándar.

### 7.4 Configuración del robots.txt para IA

Los archivos `llms.txt` **no poseen funciones de bloqueo ni directivas de seguridad** para denegar el paso de robots. El acceso legítimo debe gobernarse desde `/robots.txt`. Es imperativo estructurar los permisos de manera proactiva:

```robots.txt
User-agent: *
Allow: /

# Autorizar rastreadores de IA
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: CCBot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: FacebookBot
Allow: /

User-agent: Cohere-ai
Allow: /

# Declarar llms.txt como sitemap complementario
Sitemap: https://tusitio.com/sitemap.xml
Sitemap: https://tusitio.com/llms.txt
```

Al declarar `llms.txt` como un mapa complementario en la base de `robots.txt`, se guía directamente a los crawlers para que asimilen la arquitectura semántica del sitio antes de procesar el código HTML complejo.

### 7.5 Protocolos de Seguridad y Prevención de Inyección de Prompts

El despliegue de una interfaz semántica estructurada expone la arquitectura de información del sitio a procesos de toma de decisiones autónomos de IAs. Esto plantea desafíos críticos de seguridad:

**⚠️ Riesgo de Inyección Indirecta de Prompts:** Si un atacante externo logra comprometer la seguridad del servidor y modificar maliciosamente las descripciones textuales de los enlaces en `llms.txt`, podría inyectar secuencias de comandos de manipulación semántica. Al leer este archivo, los agentes autónomos (asistentes de código, chats inteligentes) podrían verse forzados a saltarse sus directrices de seguridad, descargar software malicioso o filtrar información privada.

**Gobernanza mediante CI/CD:** Queda **terminantemente prohibida** la edición o mantenimiento manual de los archivos `llms.txt` en entornos de producción. Se debe configurar un proceso automatizado dentro del pipeline de despliegue que genere de manera estática los archivos `llms.txt` y `llms-full.txt` como artefactos de compilación limpios del código fuente de documentación verificada.

**Autenticación de Acceso:** Si el sitio requiere controles de acceso o credenciales para ciertas secciones de documentación, las rutas correspondientes en `llms.txt` y `llms-full.txt` deben configurarse bajo el mismo esquema de cifrado y autenticación de seguridad de APIs para evitar fugas masivas de datos confidenciales a rastreadores de terceros.

**Monitorización de Integridad:** Es mandatorio implementar sistemas de detección de cambios de archivos en tiempo real en la raíz del servidor web, alertando al instante ante cualquier modificación de la firma criptográfica (hash MD5/SHA256) del archivo `llms.txt` ajena a los despliegues autorizados.

### 7.6 Protocolo de Auditoría llms.txt

Para `/geo-seo-pro llmstxt <url>`:
1. Verificar presencia de `https://domain.com/llms.txt` y `llms-full.txt`
2. Validar formato contra especificación (H1, blockquote, H2, enlaces anotados)
3. Evaluar completitud (cobertura de secciones clave del sitio)
4. Verificar HTTP Link Headers y X-Llms-Txt
5. Comprobar ruta `/.well-known/llms.txt`
6. Revisar configuración robots.txt para crawlers IA
7. Si no existe, generar llms.txt completo basado en la estructura del sitio
8. Incluir advertencias de seguridad (CI/CD, hash, autenticación)

---

## PARTE 8: MATRIZ DE INTEGRACIÓN SISTÉMICA Y PROTOCOLOS DE EJECUCIÓN

La optimización moderna de activos digitales exige trascender de las metodologías aisladas hacia una arquitectura híbrida unificada. Los parámetros que tradicionalmente han impulsado la autoridad orgánica ante Google actúan hoy como la zapata de confianza técnica indispensable sobre la cual operan los motores de respuestas generativos de IA. Un sitio web técnicamente inestable o sin validación de autoridad humana (E-E-A-T) quedará fuera del radar de indexación de los modelos semánticos de forma fulminante.

### 8.1 Matriz de Integración SEO + GEO

```
                 ACCIONES DE ENFOQUE SEO                    ACCIONES DE ENFOQUE GEO
┌──────────────────────────────────────┐    ┌──────────────────────────────────────┐
│ • Core Web Vitals optimizados:       │    │ • Interfaces semánticas:             │
│   LCP < 2.5s, INP < 200ms,          │    │   Generación e integración de        │
│   CLS < 0.1                          │    │   llms.txt + llms-full.txt           │
│ • Marcado estructural sin errores:   │    │ • Despliegue de pautas RAG:          │
│   BlogPosting, FAQ, Organization     │    │   Citas, datos estadísticos,         │
│ • Directrices cualitativas:          │    │   citas de expertos                  │
│   Rigor en Who/How/Why y E-E-A-T    │    │ • Sincronización de entidades:       │
│                                      │    │   sameAs apuntando a Wikipedia,      │
│                                      │    │   LinkedIn, Wikidata                  │
└──────────────────────────────────────┘    └──────────────────────────────────────┘
```

**Sincronización del Rendimiento Técnico y UX:** Resolver deficiencias críticas de velocidad y usabilidad web mediante cumplimiento estricto de Core Web Vitals. Garantizar que la navegación móvil sea impecable y que la página se encuentre libre de interstitials de cookies invasivos. Esto asegura retención de usuarios y facilita el rastreo profundo de bots tradicionales y agentes de IA.

**Arquitectura Semántica de Datos:** Desplegar ecosistema estructurado mediante marcado JSON-LD libre de solapamientos técnicos. Consolidar propiedades de marca y perfiles de autores mediante la inyección del atributo `sameAs` permite que las IAs verifiquen la autenticidad e incorporen de manera confiable al dominio dentro de sus grafos de conocimiento sectoriales.

**Optimización del Contenido Basada en Evidencias (RAG):** Integrar en cada artículo de blog y página de servicio las directrices ganadoras del estudio Princeton. Dotar al texto de rigor científico sustituyendo descripciones genéricas por porcentajes y datos medibles precisos (emparejados con su fuente de origen y año), incorporar declaraciones textuales firmadas por expertos reales del sector y citar referencias salientes fiables para respaldar cada afirmación.

**Habilitación de Interfaces para Agentes Autónomos:** Desplegar obligatoriamente los archivos estáticos de Markdown `llms.txt` y `llms-full.txt` en el directorio raíz del servidor, automatizando su generación a través de pipelines de integración continua para neutralizar riesgos de inyección indirecta de comandos. Configurar el archivo `robots.txt` para autorizar explícitamente el paso de los bots de IA (OpenAI, Anthropic, Perplexity, Google) y utilizar encabezados HTTP para facilitar la autodetectabilidad del índice semántico.

### 8.2 Metodología de Scoring Compuesto GEO-SEO Pro (0-100)

| Categoría | Peso | Sub-componentes |
|-----------|------|-----------------|
| **Fundamentos SEO Tradicional** | 20% | 128 factores en 8 categorías: dominio, contenido, técnicos, sitio, backlinks, usuario, reglas algoritmo, webspam |
| **Core Web Vitals** | 10% | LCP (40%), INP (35%), CLS (25%) |
| **E-E-A-T y Helpful Content** | 20% | Experience (25%), Expertise (25%), Authoritativeness (20%), Trustworthiness (30%) |
| **GEO — Citabilidad y Princeton** | 25% | Citas fuentes (25%), Datos estadísticos (25%), Citas expertos (20%), Fluidez (15%), Tono autoridad (15%) |
| **Schema JSON-LD** | 10% | Completitud (60%), Validación (20%), sameAs (20%) |
| **llms.txt y Crawlers IA** | 10% | llms.txt (50%), llms-full.txt (25%), robots.txt IA (25%) |
| **Autoridad de Dominio** | 5% | Backlinks calidad, Diversidad enlaces, TrustRank |

**Bandas de Puntuación:**
- **90-100: Excelencia GEO-SEO** — Visible para buscadores tradicionales y todos los motores de IA. Listo para dominar.
- **75-89: Avanzado** — Sólido en la mayoría de áreas. Ajustes específicos necesarios para alcanzar la excelencia.
- **60-74: Intermedio** — Presente pero con gaps significativos. Requiere plan de acción estructurado.
- **40-59: Básico** — Visibilidad limitada. Necesita intervención en múltiples frentes.
- **0-39: Crítico** — Invisible para IAs. Requiere reconstrucción fundamental.

### 8.3 Protocolo de Auditoría Completa (`/geo-seo-pro audit <url>`)

**Fase 1 — Discovery (Secuencial):**
1. Fetch homepage HTML (curl o WebFetch)
2. Detectar tipo de negocio (SaaS, Local, E-commerce, Publisher, Agency, Other)
3. Extraer páginas clave de sitemap.xml o enlaces internos (hasta 50 páginas)
4. Identificar competidores principales para benchmarking

**Fase 2 — Análisis Multidimensional (Ejecutar en Paralelo):**

| Dimensión | Responsabilidad | Output |
|-----------|----------------|--------|
| SEO Tradicional | Checklist 128 factores, priorizando por tipo de negocio | SEO Score + Top 10 Issues |
| Core Web Vitals | Obtener métricas CrUX/PSI, analizar elementos problemáticos | CWV Score + Recomendaciones |
| E-E-A-T | Evaluar autoría, credenciales, transparencia, fuentes | E-E-A-T Score + Gaps |
| Schema JSON-LD | Detectar, validar, evaluar sameAs y solapamientos | Schema Score + JSON-LD generado |
| GEO (Princeton) | Evaluar contenido contra 5 estrategias ganadoras y 4 fallidas | GEO Score + Recomendaciones |
| llms.txt + Crawlers | Verificar/analizar/generar llms.txt, auditar robots.txt IA | llms.txt Score + Configuración |
| Autoridad | Verificar backlinks (.edu/.gov, diversidad, velocidad) | Authority Score |

**Fase 3 — Síntesis:**
1. Consolidar todos los scores dimensionales
2. Calcular GEO-SEO Pro Score compuesto (promedio ponderado según 8.2)
3. Identificar top 10 issues críticos
4. Priorizar por impacto × factibilidad

**Fase 4 — Informe:**
1. Generar informe markdown estructurado con todas las secciones
2. Incluir gráficos ASCII de scores
3. Generar plan de acción priorizado: Quick Wins (1-7 días), Medium-Term (1-4 semanas), Strategic (1-6 meses)
4. Incluir snippets de código para implementación directa

### 8.4 Protocolos de Ejecución por Comando

**`/geo-seo-pro seo-factors <url>`:**
1. Obtener homepage HTML
2. Ejecutar checklist de 128 factores — marcar ✅ ⚠️ ❌ N/A
3. Agrupar hallazgos por categoría
4. Priorizar: críticos (afectan indexación), altos (afectan ranking), medios (optimización), bajos (refinamiento)
5. Output: tabla de cumplimiento + top acciones priorizadas

**`/geo-seo-pro core-web-vitals <url>`:**
1. Ejecutar PageSpeed Insights API (si está disponible) o simular diagnóstico
2. Evaluar cada métrica contra rangos óptimo/advertencia/crítico
3. Identificar elementos específicos degradando cada métrica
4. Proporcionar correcciones con código específico (HTML/CSS/JS)
5. Output: score CWV + diagnóstico element-by-element + código de fix

**`/geo-seo-pro e-e-a-t <url>`:**
1. Inspeccionar página en busca de: autoría (bylines), biografías, credenciales, fuentes citadas
2. Evaluar señales de transparencia (declaración de uso de IA, fuentes primarias)
3. Verificar seguridad (HTTPS, políticas legales)
4. Analizar si el contenido aporta valor único o es contenido masivo para SEO
5. Output: score E-E-A-T por dimensión + gaps + recomendaciones

**`/geo-seo-pro schema <url>`:**
1. Extraer y validar todos los bloques JSON-LD presentes
2. Verificar campos obligatorios según tipo de esquema
3. Evaluar uso de sameAs en Organization y Person
4. Detectar conflictos de solapamiento
5. Generar JSON-LD corregido o nuevo
6. Output: inventario de schemas + validación + JSON-LD listo para implementar

**`/geo-seo-pro geo <url>`:**
1. Extraer bloques de contenido textual
2. Evaluar cada bloque contra las 5 estrategias Princeton ganadoras
3. Detectar presencia de las 4 tácticas fallidas
4. Calcular GEO Score por bloque y página
5. Aplicar principio Underdog: si el sitio tiene baja autoridad SEO, enfatizar oportunidad de visibilidad desproporcionada
6. Recomendar mejoras específicas párrafo por párrafo
7. Output: GEO Score + análisis táctico + recomendaciones textuales

**`/geo-seo-pro llmstxt <url>`:**
1. Verificar `https://domain.com/llms.txt`
2. Si existe: validar formato, evaluar cobertura, verificar headers y .well-known
3. Si no existe: analizar estructura del sitio y generar llms.txt completo
4. Verificar configuración robots.txt para crawlers IA
5. Incluir advertencias de seguridad (CI/CD, monitorización de hash)
6. Output: llms.txt generado (listo para desplegar) + diagnóstico de configuración IA

**`/geo-seo-pro crawlers <url>`:**
1. Fetch y parsear `/robots.txt`
2. Evaluar acceso para los 12 crawlers IA (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Amazonbot, Bytespider, Google-Extended, CCBot, Applebot-Extended, FacebookBot, Cohere-ai)
3. Detectar over-blocking o bloqueos accidentales
4. Verificar sitemaps declarados
5. Output: tabla de acceso por crawler + robots.txt corregido

**`/geo-seo-pro content <url>`:**
1. Extraer contenido textual de la página
2. Evaluar contra las 5 estrategias Princeton (¿tiene citas? ¿datos? ¿expertos? ¿fluidez? ¿tono autoridad?)
3. Detectar tácticas fallidas (keyword stuffing, simplificación extrema, relleno, lenguaje persuasivo)
4. Recomendar reescritura de pasajes específicos
5. Sugerir adiciones: datos estadísticos + fuentes + año, citas de expertos con nombre y cargo
6. Output: análisis párrafo por párrafo + versiones mejoradas de pasajes clave

**`/geo-seo-pro report <url>`:**
1. Ejecutar análisis rápido de todas las dimensiones
2. Consolidar en informe estructurado cliente-ready
3. Incluir: Executive Summary, GEO-SEO Score, Score Breakdown, Key Findings, Prioritized Action Plan
4. Output: `GEO-SEO-PRO-REPORT.md` listo para entregar a cliente

---

## Output Files

| Comando | Archivo de Salida |
|---------|-------------------|
| `/geo-seo-pro audit` | `GEO-SEO-PRO-AUDIT-REPORT.md` |
| `/geo-seo-pro seo-factors` | `GEO-SEO-FACTORS-CHECKLIST.md` |
| `/geo-seo-pro core-web-vitals` | `GEO-SEO-CWV-ANALYSIS.md` |
| `/geo-seo-pro e-e-a-t` | `GEO-SEO-EEAT-ASSESSMENT.md` |
| `/geo-seo-pro schema` | `GEO-SEO-SCHEMA-REPORT.md` + `generated-schema.jsonld` |
| `/geo-seo-pro geo` | `GEO-SEO-GEO-ANALYSIS.md` |
| `/geo-seo-pro llmstxt` | `llms.txt` y `llms-full.txt` (listos para desplegar) |
| `/geo-seo-pro crawlers` | `GEO-SEO-CRAWLER-ACCESS.md` + `robots.txt` corregido |
| `/geo-seo-pro content` | `GEO-SEO-CONTENT-OPTIMIZATION.md` |
| `/geo-seo-pro report` | `GEO-SEO-PRO-CLIENT-REPORT.md` |

---

## Fuentes de la Investigación

1. **GEO: Generative Engine Optimization** — arXiv, https://arxiv.org/pdf/2311.09735
2. **Generative Engine Optimization (GEO): The Definitive Guide [2026]** — GEOptie, https://geoptie.com/blog/generative-engine-optimization
3. **Google's 200 Ranking Factors: The Complete List (2026)** — Backlinko, https://backlinko.com/google-ranking-factors
4. **Essential Schema Structured Data for AI Search Optimisation** — LangSync, https://blog.langsync.ai/structured-data-for-ai-search/
5. **LLMs.txt Guide: What It Does and Doesn't Do (2026)** — DerivateX, https://derivatex.agency/blog/llms-txt-guide/
6. **Creating Helpful, Reliable, People-First Content** — Google Search Central, https://developers.google.com/search/docs/fundamentals/creating-helpful-content
7. **Understanding Core Web Vitals and Google search results** — Google, https://developers.google.com/search/docs/appearance/core-web-vitals
8. **The Princeton GEO Paper in Plain English: 5 Tactics That Boost AI Citation by 40%** — DerivateX, https://derivatex.agency/blog/princeton-geo-paper-plain-english/
9. **llms.txt and llms-full.txt** — Fern Documentation, https://buildwithfern.com/learn/docs/ai-features/llms-txt
10. **Google's E-E-A-T** — Moz, https://moz.com/learn/seo/google-eat
