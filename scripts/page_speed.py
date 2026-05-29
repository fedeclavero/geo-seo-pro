#!/usr/bin/env python3
"""
GEO-SEO Pro — PageSpeed Insights & Core Web Vitals Measurement
Llama a la API gratuita de Google PageSpeed Insights (no requiere auth).
Devuelve métricas REALES de LCP, INP, CLS, TTFB, y puntuación de performance.
"""
import json
import sys
import urllib.request
import urllib.parse
import urllib.error
from typing import Optional


API_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"


def fetch_page_speed(url: str, strategy: str = "mobile") -> dict:
    """Fetch real Core Web Vitals from PageSpeed Insights API."""
    params = urllib.parse.urlencode({
        "url": url,
        "strategy": strategy,
        "category": ["performance", "seo", "best-practices", "accessibility"],
    })
    full_url = f"{API_URL}?{params}"

    try:
        req = urllib.request.Request(full_url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}


def extract_cwv(data: dict, strategy: str) -> dict:
    """Extract Core Web Vitals metrics from PageSpeed Insights response."""
    if "error" in data:
        return {"error": data["error"], "strategy": strategy}

    result = {
        "strategy": strategy,
        "performance_score": None,
        "metrics": {},
        "diagnostics": [],
    }

    try:
        lighthouse = data.get("lighthouseResult", {})
        result["performance_score"] = int(
            lighthouse.get("categories", {}).get("performance", {}).get("score", 0) * 100
        )

        audits = lighthouse.get("audits", {})

        # LCP — Largest Contentful Paint
        lcp_audit = audits.get("largest-contentful-paint", {})
        if lcp_audit.get("numericValue") is not None:
            lcp_ms = lcp_audit["numericValue"]
            lcp_s = round(lcp_ms / 1000, 2)
            result["metrics"]["lcp"] = {
                "value_ms": lcp_ms,
                "value_s": lcp_s,
                "display": lcp_audit.get("displayValue", f"{lcp_s}s"),
                "rating": "good" if lcp_s <= 2.5 else ("needs-improvement" if lcp_s <= 4.0 else "poor"),
            }

        # CLS — Cumulative Layout Shift
        cls_audit = audits.get("cumulative-layout-shift", {})
        if cls_audit.get("numericValue") is not None:
            cls_val = round(cls_audit["numericValue"], 3)
            result["metrics"]["cls"] = {
                "value": cls_val,
                "display": cls_audit.get("displayValue", str(cls_val)),
                "rating": "good" if cls_val <= 0.1 else ("needs-improvement" if cls_val <= 0.25 else "poor"),
            }

        # TBT — Total Blocking Time (proxy for INP in lab data)
        tbt_audit = audits.get("total-blocking-time", {})
        if tbt_audit.get("numericValue") is not None:
            tbt_ms = int(tbt_audit["numericValue"])
            result["metrics"]["tbt"] = {
                "value_ms": tbt_ms,
                "display": tbt_audit.get("displayValue", f"{tbt_ms}ms"),
                "rating": "good" if tbt_ms <= 200 else ("needs-improvement" if tbt_ms <= 600 else "poor"),
                "note": "TBT is a lab proxy for INP. Real INP requires CrUX field data.",
            }

        # TTFB — Time to First Byte
        ttfb_audit = audits.get("server-response-time", {})
        if ttfb_audit.get("numericValue") is not None:
            ttfb_ms = round(ttfb_audit["numericValue"], 1)
            result["metrics"]["ttfb"] = {
                "value_ms": ttfb_ms,
                "display": ttfb_audit.get("displayValue", f"{ttfb_ms}ms"),
                "rating": "good" if ttfb_ms <= 800 else ("needs-improvement" if ttfb_ms <= 1800 else "poor"),
            }

        # FCP — First Contentful Paint
        fcp_audit = audits.get("first-contentful-paint", {})
        if fcp_audit.get("numericValue") is not None:
            fcp_ms = fcp_audit["numericValue"]
            fcp_s = round(fcp_ms / 1000, 2)
            result["metrics"]["fcp"] = {
                "value_ms": fcp_ms,
                "value_s": fcp_s,
                "display": fcp_audit.get("displayValue", f"{fcp_s}s"),
                "rating": "good" if fcp_s <= 1.8 else ("needs-improvement" if fcp_s <= 3.0 else "poor"),
            }

        # Key diagnostics (top 3 issues)
        diagnostic_audits = [
            "render-blocking-resources",
            "uses-optimized-images",
            "uses-text-compression",
            "unused-css",
            "unused-javascript",
            "offscreen-images",
            "uses-responsive-images",
            "dom-size",
            "modern-image-formats",
            "efficient-animated-content",
        ]
        for audit_id in diagnostic_audits:
            audit = audits.get(audit_id, {})
            if audit.get("score") is not None and audit["score"] < 0.9:
                result["diagnostics"].append({
                    "id": audit_id,
                    "title": audit.get("title", audit_id),
                    "description": audit.get("description", ""),
                    "displayValue": audit.get("displayValue", ""),
                    "score": int(audit["score"] * 100),
                })

    except Exception as e:
        result["error"] = f"Failed to parse Lighthouse data: {e}"

    return result


def calculate_cwv_score(metrics: dict) -> int:
    """Calculate aggregated Core Web Vitals score (0-100)."""
    if not metrics:
        return 0

    scores = []
    weights = {"lcp": 0.40, "tbt": 0.35, "cls": 0.25}

    for key, weight in weights.items():
        metric = metrics.get(key)
        if not metric:
            continue
        rating = metric.get("rating")
        if rating == "good":
            scores.append(100 * weight)
        elif rating == "needs-improvement":
            scores.append(50 * weight)
        else:
            scores.append(0 * weight)

    return round(sum(scores)) if scores else 0


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: page_speed.py <url> [mobile|desktop]"}, indent=2))
        sys.exit(1)

    url = sys.argv[1]
    strategy = sys.argv[2] if len(sys.argv) > 2 else "mobile"

    # Fetch data for both strategies
    mobile_data = fetch_page_speed(url, "mobile")
    mobile_result = extract_cwv(mobile_data, "mobile")
    mobile_result["cwv_score"] = calculate_cwv_score(mobile_result.get("metrics", {}))

    results = [mobile_result]

    if strategy == "both" or strategy == "desktop":
        desktop_data = fetch_page_speed(url, "desktop")
        desktop_result = extract_cwv(desktop_data, "desktop")
        desktop_result["cwv_score"] = calculate_cwv_score(desktop_result.get("metrics", {}))
        results.append(desktop_result)

    output = {"url": url, "results": results}
    if strategy != "both":
        output["result"] = results[0]

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
