#!/usr/bin/env python3
"""
GEO-SEO Pro — Business Type Detector
Analiza HTML de la homepage y determina el tipo de negocio.
Ajusta recomendaciones de schemas, estrategia GEO y prioridades.
"""
import json
import sys
import re
import urllib.request
import urllib.error
from html.parser import HTMLParser


class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.links = []
        self.images = []
        self.meta_tags = {}
        self.skip = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag in ("script", "style", "noscript"):
            self.skip = True
        if tag == "a" and "href" in attrs_dict:
            self.links.append(attrs_dict["href"])
        if tag == "img" and "src" in attrs_dict:
            self.images.append(attrs_dict["src"])
        if tag == "meta":
            name = attrs_dict.get("name", attrs_dict.get("property", ""))
            content = attrs_dict.get("content", "")
            if name and content:
                self.meta_tags[name] = content

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.skip = False

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.text.append(data.strip())


def fetch_page(url: str) -> dict:
    """Fetch HTML from URL."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "GEO-SEO-Pro/1.0 (business detector)"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            extractor = HTMLTextExtractor()
            extractor.feed(html)
            return {
                "url": url,
                "status": resp.status,
                "html": html,
                "text_blocks": extractor.text,
                "links": extractor.links,
                "images": extractor.images,
                "meta": extractor.meta_tags,
                "found": True,
            }
    except Exception as e:
        return {"url": url, "status": None, "found": False, "error": str(e)}


def detect_business_type(page_data: dict) -> dict:
    """Determine business type from page signals."""
    if not page_data.get("found"):
        return {"type": "other", "confidence": 0, "signals": []}

    html = page_data.get("html", "")
    links = page_data.get("links", [])
    text_blocks = page_data.get("text_blocks", [])
    meta = page_data.get("meta", {})
    all_text = " ".join(text_blocks).lower()
    all_links = " ".join(links).lower()

    scores = {}

    # SaaS signals
    saas_signals = []
    if re.search(r'(pricing|precios|planes|plans|subscription|suscripción)', all_links):
        saas_signals.append("pricing_page")
    if re.search(r'(sign\s*up|signup|registrarse|free\s*trial|prueba\s*gratis|demo|get\s*started|comenzar)', all_text):
        saas_signals.append("cta_trial")
    if re.search(r'(/app|/dashboard|/login|api\s*docs|/docs|documentation)', all_links):
        saas_signals.append("app_routes")
    if re.search(r'(api|integration|sdk|webhook|plugin|extension)', all_text):
        saas_signals.append("tech_terms")
    saas_score = len(saas_signals) * 25
    scores["saas"] = {"score": min(100, saas_score), "signals": saas_signals}

    # Local Service signals
    local_signals = []
    if re.search(r'(tel:|phone|teléfono|llamanos|llámanos|call\s*us|contacto)', all_text + all_links):
        local_signals.append("phone_present")
    if re.search(r'(dirección|address|ubicación|location|estamos\s*en|find\s*us)', all_text):
        local_signals.append("address_mentioned")
    if re.search(r'(google\s*maps|maps\.google|mapa|cómo\s*llegar)', all_text + all_links):
        local_signals.append("maps_embed")
    if re.search(r'(\b(?:cerca|near\s*me|zona|barrio|área|service\s*area)\b)', all_text):
        local_signals.append("service_area")
    local_score = len(local_signals) * 25
    scores["local_service"] = {"score": min(100, local_score), "signals": local_signals}

    # E-commerce signals
    ecom_signals = []
    if re.search(r'(cart|carrito|add\s*to\s*cart|comprar|buy\s*now|shop|tienda|checkout)', all_text + all_links):
        ecom_signals.append("cart_present")
    if re.search(r'(/product|/products|/shop|/tienda|/item|/catalog)', all_links):
        ecom_signals.append("product_routes")
    if re.search(r'(price|precio|\$|€|usd|eur|ars|mxn)', all_text):
        ecom_signals.append("price_indicators")
    if re.search(r'Product', html) and re.search(r'"@type"', html):
        ecom_signals.append("product_schema")
    ecom_score = len(ecom_signals) * 25
    scores["ecommerce"] = {"score": min(100, ecom_score), "signals": ecom_signals}

    # Publisher signals
    pub_signals = []
    if re.search(r'(/blog|/articles|/posts|/news|/noticias|/articulos)', all_links):
        pub_signals.append("blog_routes")
    if re.search(r'(byline|author|autor|escrito\s*por|published|publicado)', all_text):
        pub_signals.append("authorship")
    if re.search(r'Article|BlogPosting|NewsArticle', html):
        pub_signals.append("article_schema")
    if re.search(r'(subscribe|suscribirse|newsletter|rss|feed)', all_text + all_links):
        pub_signals.append("subscription_cta")
    pub_score = len(pub_signals) * 25
    scores["publisher"] = {"score": min(100, pub_score), "signals": pub_signals}

    # Agency signals
    agency_signals = []
    if re.search(r'(portfolio|trabajos|proyectos|case\s*stud|clientes|clients)', all_text + all_links):
        agency_signals.append("portfolio")
    if re.search(r'(our\s*services|servicios|what\s*we\s*do|qué\s*hacemos)', all_text):
        agency_signals.append("services_page")
    if re.search(r'(testimonial|testimonio|logos|clientes\s*que|confían)', all_text):
        agency_signals.append("social_proof")
    if re.search(r'(contact|contacto|hablemos|let\'s\s*talk|presupuesto|cotización|quote)', all_text + all_links):
        agency_signals.append("contact_cta")
    agency_score = len(agency_signals) * 25
    scores["agency"] = {"score": min(100, agency_score), "signals": agency_signals}

    # Determine winner
    best_type = max(scores, key=lambda k: scores[k]["score"])
    best_score = scores[best_type]["score"]

    if best_score < 25:
        best_type = "other"
        confidence = 10
    elif best_score < 50:
        confidence = 40
    else:
        confidence = best_score

    # Recommended schemas and priorities by type
    strategy_map = {
        "saas": {
            "primary_schema": "SoftwareApplication",
            "secondary_schemas": ["Organization", "FAQPage", "WebSite"],
            "priority_checks": ["pricing_page", "demo_cta", "api_docs", "comparison_pages"],
            "geo_focus": "Cite technical benchmarks and API documentation. LLMs love well-structured technical content.",
        },
        "local_service": {
            "primary_schema": "LocalBusiness",
            "secondary_schemas": ["Organization", "FAQPage", "WebSite"],
            "priority_checks": ["google_business_profile", "phone_consistency", "address_schema", "local_backlinks"],
            "geo_focus": "LocalBusiness schema + Google Business Profile. Service area pages with real addresses.",
        },
        "ecommerce": {
            "primary_schema": "Product",
            "secondary_schemas": ["Organization", "WebSite", "FAQPage"],
            "priority_checks": ["product_schema", "review_rich_snippets", "price_updates", "stock_indicators"],
            "geo_focus": "Product schema with reviews, prices, and availability. Comparison content for AI shopping queries.",
        },
        "publisher": {
            "primary_schema": "Article",
            "secondary_schemas": ["Person", "Organization", "WebSite"],
            "priority_checks": ["author_bylines", "e_e_a_t_signals", "date_modified", "original_research"],
            "geo_focus": "Author authority (Person schema with sameAs). Original research and expert quotes win in GEO.",
        },
        "agency": {
            "primary_schema": "Organization",
            "secondary_schemas": ["Person", "WebSite", "FAQPage"],
            "priority_checks": ["portfolio", "testimonials", "team_pages", "case_studies"],
            "geo_focus": "Case studies with statistics. Expert quotes from team members. Portfolio with real results.",
        },
        "other": {
            "primary_schema": "Organization",
            "secondary_schemas": ["WebSite", "FAQPage"],
            "priority_checks": ["business_identity", "content_quality", "technical_basics"],
            "geo_focus": "Start with Organization schema and build content authority through statistics and citations.",
        },
    }

    return {
        "type": best_type,
        "confidence": confidence,
        "scores": {k: v["score"] for k, v in scores.items()},
        "signals": scores[best_type]["signals"],
        "strategy": strategy_map[best_type],
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: business_detector.py <url>"}, indent=2))
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith("http"):
        url = "https://" + url

    page_data = fetch_page(url)
    result = detect_business_type(page_data)

    output = {
        "url": url,
        "http_status": page_data.get("status"),
        "detection": result,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
