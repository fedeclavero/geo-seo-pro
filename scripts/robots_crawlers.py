#!/usr/bin/env python3
"""
GEO-SEO Pro — robots.txt AI Crawler Access Checker
Parsea robots.txt y verifica acceso para 12 crawlers de IA de forma objetiva y binaria.
No estima, no alucina — verifica.
"""
import json
import sys
import urllib.request
import urllib.error
from fnmatch import fnmatch
from typing import Optional

# AI Crawlers documented by their respective companies
AI_CRAWLERS = {
    "GPTBot": "OpenAI (ChatGPT training + search)",
    "OAI-SearchBot": "OpenAI (search-only, separate rules)",
    "ChatGPT-User": "OpenAI (ChatGPT browsing mode)",
    "ClaudeBot": "Anthropic / Claude",
    "PerplexityBot": "Perplexity AI search",
    "Google-Extended": "Google (Gemini training, NOT Google Search)",
    "Amazonbot": "Amazon / Alexa AI",
    "Bytespider": "ByteDance / TikTok AI",
    "CCBot": "Common Crawl (feeds many AI models)",
    "Applebot-Extended": "Apple Intelligence features",
    "FacebookBot": "Meta AI features",
    "Cohere-ai": "Cohere models",
}


def fetch_robots_txt(domain: str) -> dict:
    """Fetch robots.txt from a domain."""
    # Ensure domain has scheme
    if not domain.startswith("http"):
        domain = "https://" + domain

    robots_url = domain.rstrip("/") + "/robots.txt"

    try:
        req = urllib.request.Request(
            robots_url,
            headers={"User-Agent": "GEO-SEO-Pro/1.0 (robots.txt checker)"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return {
                "url": robots_url,
                "status": resp.status,
                "content": resp.read().decode("utf-8", errors="replace"),
                "found": True,
            }
    except urllib.error.HTTPError as e:
        return {"url": robots_url, "status": e.code, "content": "", "found": False,
                "error": f"HTTP {e.code}"}
    except Exception as e:
        return {"url": robots_url, "status": None, "content": "", "found": False,
                "error": str(e)}


def parse_robots_txt(content: str) -> dict:
    """Parse robots.txt rules per user-agent."""
    rules = {}
    current_agent = "*"

    for line in content.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # Normalize: handle "User-agent" and "User-Agent"
        if line.lower().startswith("user-agent:"):
            current_agent = line.split(":", 1)[1].strip()
            if current_agent not in rules:
                rules[current_agent] = {"allow": [], "disallow": []}
            continue

        if line.lower().startswith("disallow:"):
            path = line.split(":", 1)[1].strip()
            if path:
                rules.setdefault(current_agent, {"allow": [], "disallow": []})
                rules[current_agent]["disallow"].append(path)
            continue

        if line.lower().startswith("allow:"):
            path = line.split(":", 1)[1].strip()
            if path:
                rules.setdefault(current_agent, {"allow": [], "disallow": []})
                rules[current_agent]["allow"].append(path)
            continue

    return rules


def check_crawler_access(rules: dict, crawler_ua: str) -> dict:
    """Check if a specific crawler has access. Returns deterministic result."""
    # Check crawler-specific rules first, then wildcard
    specific = rules.get(crawler_ua, {"allow": [], "disallow": []})
    wildcard = rules.get("*", {"allow": [], "disallow": []})

    # Check for total block
    for block in specific.get("disallow", []):
        if block == "/":
            return {"access": "blocked", "reason": f"Disallow: / for {crawler_ua}"}

    for block in wildcard.get("disallow", []):
        if block == "/":
            return {"access": "blocked", "reason": "Disallow: / for *"}

    # Check for partial restrictions
    restricted_paths = []
    for block in specific.get("disallow", []):
        if block and block != "/":
            restricted_paths.append(block)

    for block in wildcard.get("disallow", []):
        if block and block != "/" and block not in restricted_paths:
            restricted_paths.append(block)

    if restricted_paths:
        return {"access": "restricted",
                "reason": f"Restricted paths: {', '.join(restricted_paths[:5])}"}

    return {"access": "allowed", "reason": "No blocking rules found"}


def check_sitemaps(content: str) -> list:
    """Extract sitemap URLs from robots.txt."""
    sitemaps = []
    for line in content.split("\n"):
        if line.lower().startswith("sitemap:"):
            sitemaps.append(line.split(":", 1)[1].strip())
    return sitemaps


def check_content_signals(content: str) -> Optional[dict]:
    """Check for Content-Signal directives (IETF draft)."""
    for line in content.split("\n"):
        if line.lower().startswith("content-signal:"):
            signals = {}
            parts = line.split(":", 1)[1].strip()
            for pair in parts.split(","):
                pair = pair.strip()
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    signals[k.strip()] = v.strip()
            return signals
    return None


def calculate_crawler_score(crawler_results: dict) -> int:
    """Calculate Crawler Access Score (0-100)."""
    score = 100
    critical = {"GPTBot", "ClaudeBot", "PerplexityBot", "OAI-SearchBot", "Google-Extended"}
    secondary = {"ChatGPT-User", "CCBot", "Amazonbot", "Applebot-Extended", "Bytespider", "FacebookBot", "Cohere-ai"}

    for crawler, result in crawler_results.items():
        if result["access"] == "blocked":
            if crawler in critical:
                score -= 15
            elif crawler in secondary:
                score -= 5

    return max(0, score)


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: robots_crawlers.py <domain>"}, indent=2))
        sys.exit(1)

    domain = sys.argv[1]
    robots_data = fetch_robots_txt(domain)

    if not robots_data["found"]:
        print(json.dumps(robots_data, indent=2))
        sys.exit(1)

    rules = parse_robots_txt(robots_data["content"])
    sitemaps = check_sitemaps(robots_data["content"])
    content_signals = check_content_signals(robots_data["content"])

    crawler_results = {}
    for ua, description in AI_CRAWLERS.items():
        crawler_results[ua] = check_crawler_access(rules, ua)
        crawler_results[ua]["description"] = description

    crawler_score = calculate_crawler_score(crawler_results)

    output = {
        "domain": domain,
        "robots_txt_url": robots_data["url"],
        "robots_txt_status": robots_data["status"],
        "robots_txt_found": robots_data["found"],
        "crawler_access": crawler_results,
        "crawler_score": crawler_score,
        "sitemaps": sitemaps,
        "content_signals": content_signals,
        "user_agents_found": list(rules.keys()),
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
