#!/usr/bin/env python3
"""
GEO-SEO Pro — JSON-LD Schema Detector & Validator
Extrae y valida bloques JSON-LD de una página. Verifica campos obligatorios,
uso de sameAs, y detecta solapamientos entre esquemas.
"""
import json
import sys
import re
import html
import urllib.request
import urllib.error
from typing import Optional


SCHEMA_REQUIRED_FIELDS = {
    "BlogPosting": ["mainEntityOfPage", "author", "publisher", "datePublished", "headline"],
    "Article": ["author", "datePublished", "headline"],
    "FAQPage": ["mainEntity"],
    "HowTo": ["name", "step"],
    "Organization": ["name"],
    "Person": ["name"],
    "Product": ["name"],
    "LocalBusiness": ["name", "address"],
}


def fetch_html(url: str) -> dict:
    """Fetch HTML from URL."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "GEO-SEO-Pro/1.0 (schema checker)"},
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {
                "url": url,
                "status": resp.status,
                "html": resp.read().decode("utf-8", errors="replace"),
                "found": True,
            }
    except Exception as e:
        return {"url": url, "status": None, "html": "", "found": False, "error": str(e)}


def extract_jsonld(html: str) -> list:
    """Extract all JSON-LD blocks from HTML."""
    blocks = []
    # Match <script type="application/ld+json">...</script>
    pattern = re.compile(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        re.DOTALL | re.IGNORECASE,
    )
    for i, match in enumerate(pattern.finditer(html)):
        raw_json = match.group(1).strip()
        try:
            data = json.loads(raw_json)
            blocks.append({
                "index": i,
                "raw": raw_json,
                "data": data,
                "parse_error": None,
            })
        except json.JSONDecodeError as e:
            blocks.append({
                "index": i,
                "raw": raw_json,
                "data": None,
                "parse_error": str(e),
            })
    return blocks


def validate_block(block: dict) -> dict:
    """Validate a single schema block."""
    result = {
        "index": block["index"],
        "parse_error": block["parse_error"],
        "schemas": [],
    }

    if block["parse_error"]:
        return result

    data = block["data"]
    items = data if isinstance(data, list) else [data]

    for item in items:
        if isinstance(item, dict):
            schema_type = item.get("@type", "Unknown")
            # Can be a string or a list
            types = schema_type if isinstance(schema_type, list) else [schema_type]

            for t in types:
                schema_info = {
                    "@type": t,
                    "@context": item.get("@context", "missing"),
                    "has_sameAs": "sameAs" in item,
                    "sameAs_count": len(item.get("sameAs", [])),
                    "required_fields": {},
                    "issues": [],
                }

                # Check required fields
                required = SCHEMA_REQUIRED_FIELDS.get(t, [])
                for field in required:
                    schema_info["required_fields"][field] = field in item

                missing = [f for f in required if not schema_info["required_fields"].get(f)]
                if missing:
                    schema_info["issues"].append(f"Missing required fields: {', '.join(missing)}")

                # Check sameAs quality
                if item.get("sameAs"):
                    wikipedia = any("wikipedia.org" in s for s in item["sameAs"])
                    linkedin = any("linkedin.com" in s for s in item["sameAs"])
                    schema_info["sameAs_quality"] = {
                        "has_wikipedia": wikipedia,
                        "has_linkedin": linkedin,
                    }
                    if not wikipedia:
                        schema_info["issues"].append(
                            "No Wikipedia link in sameAs (strongest signal for entity recognition)"
                        )

                # Check date freshness for BlogPosting/Article
                if t in ("BlogPosting", "Article"):
                    if not item.get("dateModified"):
                        schema_info["issues"].append(
                            "dateModified is missing — freshness signals are critical for AI search"
                        )

                result["schemas"].append(schema_info)

    return result


def check_conflicts(blocks: list) -> list:
    """Detect schema conflicts — multiple primary schemas on same page."""
    conflicts = []
    primary_types = {"FAQPage", "HowTo", "Product", "BlogPosting", "Article"}
    found_primaries = []

    for block in blocks:
        if block.get("parse_error"):
            continue
        data = block["data"]
        items = data if isinstance(data, list) else [data]
        for item in items:
            if isinstance(item, dict):
                types = item.get("@type", [])
                if isinstance(types, str):
                    types = [types]
                for t in types:
                    if t in primary_types:
                        found_primaries.append(t)

    if len(set(found_primaries) & primary_types) > 1:
        conflicts.append({
            "type": "multiple_primary_schemas",
            "severity": "high",
            "message": (
                f"Multiple primary schemas detected: {found_primaries}. "
                "Apply ONE primary schema per URL. Multiple schemas dilute semantic clarity "
                "for AI engines and confuse automated filters."
            ),
        })

    return conflicts


def calculate_schema_score(blocks: list) -> int:
    """Calculate schema completeness score (0-100)."""
    if not blocks:
        return 0

    score = 0
    valid_blocks = [b for b in blocks if not b.get("parse_error")]
    if not valid_blocks:
        return 0

    # Base: schema presence
    score += 20

    # Valid JSON-LD
    score += 20

    # Has Organization or Person
    has_entity = False
    has_sameas = False
    has_blog = False

    for block in valid_blocks:
        for schema in block.get("schemas", []):
            t = schema.get("@type", "")
            if t in ("Organization", "Person"):
                has_entity = True
                if schema.get("has_sameAs"):
                    has_sameas = True
            if t in ("BlogPosting", "Article", "FAQPage", "HowTo", "Product"):
                has_blog = True

    if has_entity:
        score += 20
    if has_sameas:
        score += 15
    if has_blog:
        score += 15

    # Completeness bonus
    completeness = 0
    for block in valid_blocks:
        for schema in block.get("schemas", []):
            required = schema.get("required_fields", {})
            if required:
                completeness += sum(1 for v in required.values() if v) / len(required)
    if valid_blocks:
        score += int((completeness / len(valid_blocks)) * 15)

    return min(100, score)


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: schema_checker.py <url>"}, indent=2))
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith("http"):
        url = "https://" + url

    html_data = fetch_html(url)
    if not html_data["found"]:
        print(json.dumps(html_data, indent=2))
        sys.exit(1)

    blocks = extract_jsonld(html_data["html"])
    validated = [validate_block(b) for b in blocks]
    conflicts = check_conflicts(validated)
    schema_score = calculate_schema_score(validated)

    output = {
        "url": url,
        "http_status": html_data["status"],
        "jsonld_blocks_found": len(blocks),
        "valid_blocks": sum(1 for b in validated if not b.get("parse_error")),
        "invalid_blocks": sum(1 for b in validated if b.get("parse_error")),
        "schemas": validated,
        "conflicts": conflicts,
        "schema_score": schema_score,
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
