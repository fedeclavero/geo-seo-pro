#!/usr/bin/env python3
"""
GEO-SEO Pro — Brand Mention Scanner
Verifica presencia de marca en plataformas externas usando APIs reales.
Wikipedia, Reddit, YouTube, LinkedIn, G2, Trustpilot, Crunchbase.
"""
import json
import sys
import urllib.request
import urllib.parse
import urllib.error
from typing import Optional


def check_wikipedia(brand_name: str, lang: str = "es") -> dict:
    """Check Wikipedia presence via API. Returns article existence and Wikidata ID."""
    result = {"exists": False, "url": None, "wikidata_id": None, "description": None}

    try:
        # Search Wikipedia
        params = urllib.parse.urlencode({
            "action": "query",
            "list": "search",
            "srsearch": brand_name,
            "srlimit": 3,
            "format": "json",
        })
        url = f"https://{lang}.wikipedia.org/w/api.php?{params}"
        req = urllib.request.Request(url, headers={"User-Agent": "GEO-SEO-Pro/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())

        results = data.get("query", {}).get("search", [])
        if results:
            # Check if the top result matches the brand name closely
            title = results[0]["title"]
            if brand_name.lower() in title.lower():
                result["exists"] = True
                page_title = title.replace(" ", "_")
                result["url"] = f"https://{lang}.wikipedia.org/wiki/{urllib.parse.quote(page_title)}"

                # Get Wikidata ID and description
                wd_result = check_wikidata(brand_name, lang)
                result["wikidata_id"] = wd_result.get("wikidata_id")
                result["description"] = wd_result.get("description")

    except Exception as e:
        result["error"] = str(e)

    return result


def check_wikidata(brand_name: str, lang: str = "es") -> dict:
    """Check Wikidata for entity ID."""
    result = {"wikidata_id": None, "description": None}

    try:
        params = urllib.parse.urlencode({
            "action": "wbsearchentities",
            "search": brand_name,
            "language": lang,
            "format": "json",
        })
        url = f"https://www.wikidata.org/w/api.php?{params}"
        req = urllib.request.Request(url, headers={"User-Agent": "GEO-SEO-Pro/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())

        results = data.get("search", [])
        if results and brand_name.lower() in results[0].get("label", "").lower():
            result["wikidata_id"] = results[0].get("id")
            result["description"] = results[0].get("description")

    except Exception as e:
        result["error"] = str(e)

    return result


def check_reddit(brand_name: str) -> dict:
    """Check Reddit mentions via public API."""
    result = {"mentions_found": False, "subreddits": [], "recent_posts": 0}

    try:
        # Search Reddit (public API, no auth needed for basic search)
        params = urllib.parse.urlencode({
            "q": brand_name,
            "sort": "relevance",
            "limit": 10,
        })
        url = f"https://www.reddit.com/search.json?{params}"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "GEO-SEO-Pro/1.0 (brand scanner)"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())

        posts = data.get("data", {}).get("children", [])
        if posts:
            result["mentions_found"] = True
            result["recent_posts"] = len(posts)

            # Extract unique subreddits
            subreddits = set()
            for post in posts:
                sub = post.get("data", {}).get("subreddit")
                if sub:
                    subreddits.add(sub)
            result["subreddits"] = list(subreddits)[:5]

            # Quick sentiment check (simple heuristic)
            positive = 0
            negative = 0
            for post in posts:
                title = post.get("data", {}).get("title", "").lower()
                score = post.get("data", {}).get("score", 0)
                if any(w in title for w in ("great", "best", "love", "excelente", "bueno", "recomiendo")):
                    positive += 1
                elif any(w in title for w in ("bad", "worst", "terrible", "malo", "pésimo", "estafa")):
                    negative += 1
            result["sentiment"] = "positive" if positive > negative else ("negative" if negative > positive else "neutral")

    except Exception as e:
        result["error"] = str(e)

    return result


def check_youtube(brand_name: str) -> dict:
    """Check YouTube presence via search scraping."""
    result = {"channel_found": False, "video_count": 0, "url": None}

    try:
        # Search YouTube channels
        query = urllib.parse.quote_plus(f"{brand_name} official channel")
        url = f"https://www.youtube.com/results?search_query={query}"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; GEO-SEO-Pro/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        # Look for channel indicators in the response
        if '/c/' in html or '/channel/' in html or '/@' in html:
            result["channel_found"] = True

        # Count video mentions (approximate via videoId patterns)
        import re
        video_ids = re.findall(r'"videoId":"([^"]+)"', html)
        result["video_count"] = len(set(video_ids))

        if result["video_count"] > 0:
            result["has_content"] = True

    except Exception as e:
        result["error"] = str(e)

    return result


def check_linkedin(brand_name: str) -> dict:
    """Check LinkedIn company presence."""
    result = {"company_page_found": False, "employee_count_hint": None, "url": None}

    try:
        # Search LinkedIn companies via Google (since LinkedIn API requires auth)
        query = urllib.parse.quote_plus(f"{brand_name} linkedin company")
        url = f"https://www.google.com/search?q={query}"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; GEO-SEO-Pro/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        if "linkedin.com/company/" in html:
            result["company_page_found"] = True

    except Exception as e:
        result["error"] = str(e)

    return result


def check_review_platforms(brand_name: str) -> dict:
    """Check presence on review platforms (G2, Trustpilot, Crunchbase)."""
    result = {"g2": False, "trustpilot": False, "crunchbase": False, "producthunt": False}

    checks = {
        "g2": f"site:g2.com {brand_name}",
        "trustpilot": f"site:trustpilot.com {brand_name}",
        "crunchbase": f"site:crunchbase.com {brand_name}",
        "producthunt": f"site:producthunt.com {brand_name}",
    }

    for platform, query in checks.items():
        try:
            q = urllib.parse.quote_plus(query)
            url = f"https://www.google.com/search?q={q}"
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 (compatible; GEO-SEO-Pro/1.0)"},
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode("utf-8", errors="replace")
                # Simple check: if results mention the platform domain
                result[platform] = f"{platform}.com" in html.lower()
        except Exception:
            pass

    return result


def calculate_brand_score(results: dict) -> int:
    """Calculate brand presence score (0-100)."""
    score = 0

    # Wikipedia — strongest signal for entity recognition
    if results.get("wikipedia", {}).get("exists"):
        score += 30

    # Wikidata
    if results.get("wikipedia", {}).get("wikidata_id"):
        score += 10

    # Reddit presence and sentiment
    reddit = results.get("reddit", {})
    if reddit.get("mentions_found"):
        score += 15
        if reddit.get("sentiment") == "positive":
            score += 5

    # YouTube
    youtube = results.get("youtube", {})
    if youtube.get("channel_found"):
        score += 10
    if youtube.get("video_count", 0) > 5:
        score += 5

    # LinkedIn
    if results.get("linkedin", {}).get("company_page_found"):
        score += 10

    # Review platforms
    reviews = results.get("review_platforms", {})
    for platform in ("g2", "trustpilot", "crunchbase", "producthunt"):
        if reviews.get(platform):
            score += 5

    return min(100, score)


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: brand_scanner.py <brand_name>"}, indent=2))
        sys.exit(1)

    brand_name = sys.argv[1]

    results = {
        "brand": brand_name,
        "wikipedia": check_wikipedia(brand_name),
        "reddit": check_reddit(brand_name),
        "youtube": check_youtube(brand_name),
        "linkedin": check_linkedin(brand_name),
        "review_platforms": check_review_platforms(brand_name),
    }

    results["overall_score"] = calculate_brand_score(results)
    results["rating"] = (
        "excellent" if results["overall_score"] >= 80
        else "good" if results["overall_score"] >= 60
        else "fair" if results["overall_score"] >= 40
        else "poor"
    )
    results["correlation_note"] = "Brand mentions have 3x stronger correlation with AI visibility than backlinks (Ahrefs, Dec 2025, 75,000 brands analyzed)"

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
