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
