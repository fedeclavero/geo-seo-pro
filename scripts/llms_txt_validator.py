#!/usr/bin/env python3
"""
GEO-SEO Pro — llms.txt Validator
Detecta y valida llms.txt y llms-full.txt contra el estándar oficial.
Verifica: presencia, formato, H1, blockquote, H2, enlaces anotados, headers HTTP.
"""
import json
import sys
import urllib.request
import urllib.error
import re
from typing import Optional


def fetch_text(url: str, timeout: int = 15) -> dict:
    """Fetch text content from a URL."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "GEO-SEO-Pro/1.0 (llms.txt validator)"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return {
                "url": url,
                "status": resp.status,
                "content": resp.read().decode("utf-8", errors="replace"),
                "found": True,
                "headers": dict(resp.headers),
            }
    except urllib.error.HTTPError as e:
        return {"url": url, "status": e.code, "content": "", "found": False,
                "error": f"HTTP {e.code}"}
    except Exception as e:
        return {"url": url, "status": None, "content": "", "found": False,
                "error": str(e)}


def validate_llms_txt(content: str) -> dict:
    """Validate llms.txt against the official specification."""
    issues = []
    warnings = []
    sections = []
    links = []

    lines = content.strip().split("\n")
    if not lines:
        return {"valid": False, "score": 0, "issues": ["Empty file"], "warnings": [],
                "sections": [], "links": []}

    # Rule 1: First non-empty line must be H1
    first_line = lines[0].strip()
    if not first_line.startswith("# "):
        issues.append("First line must be an H1 heading (# Title)")
    else:
        # Check if it has content after the #
        title = first_line[2:].strip()
        if not title:
            issues.append("H1 heading is empty")
        elif len(title) > 100:
            warnings.append("H1 title is very long (>{100} chars)")

    # Rule 2: Check for blockquote summary (optional but recommended)
    has_blockquote = False
    for i, line in enumerate(lines[1:6], 1):  # Check first 5 lines after H1
        if line.strip().startswith("> "):
            has_blockquote = True
            break
    if not has_blockquote:
        warnings.append("No blockquote summary found (recommended: 1-3 line description)")

    # Rule 3: Check for H2 sections
    h2_count = 0
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## ") and not stripped.startswith("### "):
            h2_count += 1
            section_name = stripped[3:].strip()
            sections.append(section_name)

    if h2_count == 0:
        issues.append("No H2 sections found — content must be organized in sections")
    elif h2_count > 20:
        warnings.append(f"Large number of H2 sections ({h2_count}) — consider consolidating")

    # Rule 4: Check for annotated links
    link_pattern = re.compile(r'^\s*-\s*\[([^\]]+)\]\(([^)]+)\):\s*(.+)$')
    for line in lines:
        match = link_pattern.match(line)
        if match:
            title, url, description = match.groups()
            links.append({"title": title, "url": url, "description": description.strip()})
            if len(description.strip()) > 300:
                warnings.append(f"Link description exceeds 300 chars: {title}")

    if not links:
        warnings.append("No annotated links found in Markdown format")

    # Score
    score = 0
    if not issues:
        score = 30  # Basic valid format

    if has_blockquote:
        score += 10

    if h2_count >= 2:
        score += 15
    elif h2_count == 1:
        score += 5

    if len(links) >= 3:
        score += 25
    elif len(links) >= 1:
        score += 10

    # Bonus for comprehensive coverage
    if len(links) >= 10:
        score += 10
    if h2_count >= 4:
        score += 10

    return {
        "valid": len(issues) == 0,
        "score": min(100, score),
        "issues": issues,
        "warnings": warnings,
        "sections": sections,
        "links_count": len(links),
        "links": links[:20],  # Cap at 20 for output
    }


def check_http_headers(headers: dict) -> dict:
    """Check for llms.txt HTTP headers."""
    link_header = headers.get("Link", headers.get("link", ""))
    x_llms = headers.get("X-Llms-Txt", headers.get("x-llms-txt", ""))

    return {
        "link_header_rel_llms_txt": "rel=\"llms-txt\"" in link_header,
        "link_header_rel_llms_full_txt": "rel=\"llms-full-txt\"" in link_header,
        "x_llms_txt": x_llms if x_llms else None,
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: llms_txt_validator.py <domain>"}, indent=2))
        sys.exit(1)

    domain = sys.argv[1]
    if not domain.startswith("http"):
        domain = "https://" + domain
    domain = domain.rstrip("/")

    results = {}

    # Check llms.txt
    llms_txt_data = fetch_text(f"{domain}/llms.txt")
    if llms_txt_data["found"]:
        results["llms_txt"] = validate_llms_txt(llms_txt_data["content"])
        results["llms_txt"]["url"] = llms_txt_data["url"]
        results["llms_txt"]["status_code"] = llms_txt_data["status"]
        results["llms_txt"]["http_headers"] = check_http_headers(
            llms_txt_data.get("headers", {})
        )
    else:
        results["llms_txt"] = {
            "found": False,
            "url": llms_txt_data["url"],
            "status_code": llms_txt_data.get("status"),
            "error": llms_txt_data.get("error"),
        }

    # Check llms-full.txt
    llms_full_data = fetch_text(f"{domain}/llms-full.txt")
    if llms_full_data["found"]:
        results["llms_full_txt"] = {
            "found": True,
            "url": llms_full_data["url"],
            "status_code": llms_full_data["status"],
            "size_chars": len(llms_full_data["content"]),
            "estimated_tokens": len(llms_full_data["content"]) // 4,
        }
    else:
        results["llms_full_txt"] = {
            "found": False,
            "url": llms_full_data["url"],
            "status_code": llms_full_data.get("status"),
            "error": llms_full_data.get("error"),
        }

    # Check .well-known/llms.txt
    wellknown_data = fetch_text(f"{domain}/.well-known/llms.txt")
    results["well_known"] = {
        "found": wellknown_data["found"],
        "url": wellknown_data["url"],
        "status_code": wellknown_data.get("status"),
    }

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
