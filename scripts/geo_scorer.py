#!/usr/bin/env python3
"""
GEO-SEO Pro — GEO Citability Scorer (Princeton GEO-bench based)
Evalúa contenido contra las 5 estrategias ganadoras y 4 tácticas fallidas
del estudio Princeton GEO-bench (KDD 2024). Output binario y medible.
"""
import json
import sys
import re
import urllib.request
import urllib.error
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    """Extract visible text from HTML, preserving structure."""
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag in ("script", "style", "noscript", "code", "pre"):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "code", "pre"):
            self.skip = False
        if tag in ("p", "div", "li", "h1", "h2", "h3", "h4", "h5", "h6", "br", "tr"):
            self.text.append("\n")
        self.current_tag = None

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.text.append(data.strip())


def fetch_page_text(url: str) -> dict:
    """Fetch and extract visible text from a URL."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "GEO-SEO-Pro/1.0 (GEO scorer)"},
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            extractor = TextExtractor()
            extractor.feed(html)
            text = " ".join(extractor.text)
            return {
                "url": url,
                "status": resp.status,
                "text": text,
                "word_count": len(text.split()),
                "found": True,
            }
    except Exception as e:
        return {"url": url, "status": None, "text": "", "word_count": 0, "found": False,
                "error": str(e)}


def score_cite_sources(text: str) -> dict:
    """Check for outbound citations and references."""
    # Count external URLs in text
    urls = re.findall(r'https?://[^\s<>"\'\)]+', text)
    # Count citation-like patterns
    citations = re.findall(
        r'(?:según|according to|cited by|fuente|source|referencia|estudio de|'
        r'published in|journal|conference|arXiv|doi:|PMID)',
        text, re.IGNORECASE
    )
    score = min(100, len(set(urls)) * 20 + len(citations) * 10)
    return {
        "score": score,
        "external_urls_count": len(set(urls)),
        "citation_markers": len(citations),
        "rating": "good" if score >= 60 else ("needs-improvement" if score >= 30 else "poor"),
        "recommendation": (
            "Add outbound links to authoritative sources" if score < 60
            else "Good citation profile" if score < 90
            else "Excellent citation profile"
        ),
    }


def score_statistics(text: str) -> dict:
    """Check for quantitative data — percentages, numbers, years."""
    percentages = re.findall(r'\d+[\.,]?\d*\s*%', text)
    years = re.findall(r'\b(19|20)\d{2}\b', text)
    stats = re.findall(
        r'\b\d+[\.,]?\d*\s*(?:millones|millón|billones|mil|k|M|B|%|'
        r'usuarios|visitas|dólares|euros|dollars|users|visits)\b',
        text, re.IGNORECASE
    )

    # Check source+year pairing (most effective combo per Princeton)
    source_year_pairs = 0
    for match in re.finditer(r'(?:fuente|source|según)\s*[:\-]?\s*([^\.]+?)(\d{4})', text, re.IGNORECASE):
        source_year_pairs += 1

    total = len(percentages) + len(set(years)) + len(stats)
    score = min(100, total * 12 + source_year_pairs * 20)
    return {
        "score": score,
        "percentages_found": len(percentages),
        "years_found": len(set(years)),
        "stats_found": len(stats),
        "source_year_pairs": source_year_pairs,
        "rating": "good" if score >= 60 else ("needs-improvement" if score >= 30 else "poor"),
        "recommendation": (
            "Replace generic descriptions with precise data (percentages, numbers, years, sources)"
            if score < 60
            else "Consider adding source-year pairings for maximum GEO impact"
            if score < 90
            else "Strong statistical profile"
        ),
    }


def score_expert_quotes(text: str) -> dict:
    """Check for attributed expert quotes."""
    quotes = re.findall(
        r'["“]([^"”]{20,})["”]',
        text
    )
    attributed = re.findall(
        r'(?:dice|dijo|afirma|explica|según|according to|says|stated|explained|'
        r'Dr\.|Dra\.|PhD|profesor|professor|director|CEO|CTO|founder|fundador)',
        text, re.IGNORECASE
    )
    score = min(100, len(quotes) * 20 + len(attributed) * 8)
    return {
        "score": score,
        "direct_quotes": len(quotes),
        "attribution_markers": len(attributed),
        "rating": "good" if score >= 50 else ("needs-improvement" if score >= 20 else "poor"),
        "recommendation": (
            "Add direct quotes from named experts with full names and positions"
            if score < 50
            else "Good expert attribution" if score < 80
            else "Excellent expert citation profile"
        ),
    }


def score_fluency(text: str) -> dict:
    """Check text fluency — sentence length variety, readability."""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip().split()) > 3]

    if not sentences:
        return {"score": 0, "rating": "poor", "sentence_count": 0}

    lengths = [len(s.split()) for s in sentences]
    avg_len = sum(lengths) / len(lengths)

    # Good: mix of short and long sentences
    has_short = any(l < 10 for l in lengths)
    has_medium = any(10 <= l <= 25 for l in lengths)
    has_long = any(l > 25 for l in lengths)

    variety_score = sum([has_short * 25, has_medium * 35, has_long * 25])
    avg_score = 15 if 15 <= avg_len <= 30 else (5 if 5 <= avg_len <= 40 else 0)

    score = variety_score + avg_score
    return {
        "score": score,
        "rating": "good" if score >= 70 else ("needs-improvement" if score >= 40 else "poor"),
        "sentence_count": len(sentences),
        "avg_sentence_length": round(avg_len, 1),
        "has_sentence_variety": has_short and has_medium and has_long,
        "recommendation": (
            "Vary sentence length and improve syntactic flow"
            if score < 70
            else "Good fluency"
        ),
    }


def score_authoritative_voice(text: str) -> dict:
    """Check for authoritative vs hesitant language."""
    # Weak/hesitant markers (bad per Princeton)
    weak = re.findall(
        r'\b(?:tal vez|quizás|podría ser|posiblemente|probablemente|'
        r'I think|I believe|maybe|perhaps|possibly|might|could be|'
        r'en mi opinión|creo que|pienso que)\b',
        text, re.IGNORECASE
    )
    # Strong markers (good per Princeton)
    strong = re.findall(
        r'\b(?:definitivamente|ciertamente|sin duda|claramente|'
        r'definitely|certainly|clearly|undoubtedly|research shows|'
        r'data confirms|studies demonstrate|evidence indicates)\b',
        text, re.IGNORECASE
    )

    weak_ratio = len(weak) / max(1, len(text.split()) / 500)
    strong_ratio = len(strong) / max(1, len(text.split()) / 500)

    score = min(100, max(0, 50 - weak_ratio * 10 + strong_ratio * 15))
    return {
        "score": score,
        "weak_markers": len(weak),
        "strong_markers": len(strong),
        "rating": "good" if score >= 70 else ("needs-improvement" if score >= 40 else "poor"),
        "recommendation": (
            "Replace hesitant language with confident, assertive statements"
            if score < 70
            else "Good authoritative tone"
        ),
    }


def detect_failed_tactics(text: str) -> list:
    """Detect presence of the 4 failed tactics from Princeton GEO-bench."""
    warnings = []

    # 1. Keyword Stuffing — density check
    words = text.lower().split()
    word_freq = {}
    for w in words:
        if len(w) > 3:
            word_freq[w] = word_freq.get(w, 0) + 1

    stuffed = [(w, c) for w, c in word_freq.items()
               if c > len(words) * 0.02 and w not in
               ("para", "como", "esta", "este", "esto", "con", "los", "las", "del",
                "que", "por", "una", "más", "the", "and", "for", "with", "this", "that")]
    if stuffed:
        warnings.append({
            "tactic": "keyword_stuffing",
            "severity": "high",
            "details": f"Terms exceeding 2% density: {', '.join(f'{w} ({c}x)' for w, c in stuffed[:5])}",
        })

    # 2. Easy-to-Understand — vocabulary simplicity check
    unique_words = len(set(words))
    unique_ratio = unique_words / max(1, len(words))
    if unique_ratio < 0.15:
        warnings.append({
            "tactic": "oversimplification",
            "severity": "medium",
            "details": f"Very low lexical diversity ({unique_ratio:.2f}). LLMs associate rich vocabulary with expertise.",
        })

    # 3. Content Padding
    # Check for very long paragraphs with low info density (heuristic)
    paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 50]
    if not paragraphs:
        warnings.append({
            "tactic": "content_padding",
            "severity": "low",
            "details": "No substantial paragraphs detected. Content may be too thin.",
        })

    # 4. Persuasive/Promotional Language
    promo_terms = re.findall(
        r'\b(?:best|mejor|#1|número 1|increíble|amazing|revolutionary|'
        r'revolucionario|único|exclusive|exclusivo|guaranteed|garantizado|'
        r'buy now|compra ahora|limited offer|oferta limitada)\b',
        text, re.IGNORECASE
    )
    if len(promo_terms) > 3:
        warnings.append({
            "tactic": "persuasive_language",
            "severity": "medium",
            "details": f"{len(promo_terms)} promotional terms found. LLMs prefer factual objective analysis.",
        })

    return warnings


def calculate_geo_score(scores: dict) -> int:
    """Weighted Princeton GEO score (0-100)."""
    weights = {
        "cite_sources": 0.25,
        "statistics": 0.25,
        "expert_quotes": 0.20,
        "fluency": 0.15,
        "authoritative_voice": 0.15,
    }
    total = sum(scores[k]["score"] * weights[k] for k in weights)
    return round(total)


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: geo_scorer.py <url>"}, indent=2))
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith("http"):
        url = "https://" + url

    page = fetch_page_text(url)
    if not page["found"]:
        print(json.dumps(page, indent=2))
        sys.exit(1)

    text = page["text"]

    scores = {
        "cite_sources": score_cite_sources(text),
        "statistics": score_statistics(text),
        "expert_quotes": score_expert_quotes(text),
        "fluency": score_fluency(text),
        "authoritative_voice": score_authoritative_voice(text),
    }

    failed = detect_failed_tactics(text)
    geo_score = calculate_geo_score(scores)

    output = {
        "url": url,
        "http_status": page["status"],
        "word_count": page["word_count"],
        "geo_score": geo_score,
        "geo_rating": (
            "excellent" if geo_score >= 80
            else "good" if geo_score >= 60
            else "needs-improvement" if geo_score >= 40
            else "poor"
        ),
        "princeton_strategies": scores,
        "failed_tactics_detected": failed,
        "underdog_opportunity": geo_score >= 50,
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
