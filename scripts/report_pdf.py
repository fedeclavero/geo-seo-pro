#!/usr/bin/env python3
"""
GEO-SEO Pro — Professional PDF Report Generator
Genera un informe PDF profesional en español con ReportLab:
portada, scores con gráficos de barra, tabla de hallazgos, plan de acción.
"""
import json
import sys
import os
from datetime import datetime
from io import BytesIO

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm, cm
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        PageBreak, Image, HRFlowable
    )
    from reportlab.graphics.shapes import Drawing, Rect, String, Line
    from reportlab.graphics.charts.barcharts import HorizontalBarChart
    from reportlab.graphics.charts.legends import Legend
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False


# Color palette
COLORS = {
    "primary": HexColor("#1a365d"),
    "accent": HexColor("#2b6cb0"),
    "good": HexColor("#38a169"),
    "warning": HexColor("#dd6b20"),
    "critical": HexColor("#e53e3e"),
    "light_bg": HexColor("#f7fafc"),
    "medium_bg": HexColor("#edf2f7"),
    "text": HexColor("#2d3748"),
    "text_light": HexColor("#718096"),
}


def build_styles():
    """Build paragraph styles for the report."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "CoverTitle", parent=styles["Title"],
        fontSize=28, leading=34, textColor=COLORS["primary"],
        alignment=TA_CENTER, spaceAfter=10*mm,
    ))
    styles.add(ParagraphStyle(
        "CoverSubtitle", parent=styles["Normal"],
        fontSize=14, leading=20, textColor=COLORS["text_light"],
        alignment=TA_CENTER, spaceAfter=5*mm,
    ))
    styles.add(ParagraphStyle(
        "SectionTitle", parent=styles["Heading2"],
        fontSize=16, leading=22, textColor=COLORS["primary"],
        spaceBefore=10*mm, spaceAfter=5*mm,
    ))
    styles.add(ParagraphStyle(
        "BodyText2", parent=styles["Normal"],
        fontSize=9, leading=14, textColor=COLORS["text"],
        alignment=TA_JUSTIFY,
    ))
    styles.add(ParagraphStyle(
        "TableCell", parent=styles["Normal"],
        fontSize=8, leading=11, textColor=COLORS["text"],
    ))
    return styles


def build_score_bar_chart(scores: dict, width: int = 400, height: int = 180) -> Drawing:
    """Build a horizontal bar chart showing category scores."""
    d = Drawing(width, height)

    categories = list(scores.keys())
    values = list(scores.values())

    bc = HorizontalBarChart()
    bc.x = 160
    bc.y = 30
    bc.width = width - 190
    bc.height = height - 60
    bc.data = [values]
    bc.categoryAxis.categoryNames = categories
    bc.categoryAxis.labels.fontSize = 8
    bc.categoryAxis.labels.fillColor = COLORS["text"]
    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = 100
    bc.valueAxis.valueStep = 20
    bc.valueAxis.labels.fontSize = 7
    bc.bars[0].fillColor = COLORS["accent"]
    bc.barLabelFormat = "%d"

    d.add(bc)
    return d


def build_rating_gauge(score: int, x: int = 0, y: int = 0) -> Drawing:
    """Build a simple gauge showing the overall score."""
    d = Drawing(300, 120)

    # Background bar
    d.add(Rect(x + 10, y + 40, 280, 30, fillColor=COLORS["light_bg"], strokeColor=None))

    # Score bar
    bar_width = (score / 100) * 280
    bar_color = COLORS["good"] if score >= 70 else (COLORS["warning"] if score >= 40 else COLORS["critical"])
    d.add(Rect(x + 10, y + 40, bar_width, 30, fillColor=bar_color, strokeColor=None))

    # Score label
    d.add(String(x + 150, y + 90, f"{score}/100", fontSize=28,
                  fillColor=bar_color, textAnchor="middle"))

    # Rating label
    if score >= 80:
        rating = "Excelente"
    elif score >= 60:
        rating = "Bueno"
    elif score >= 40:
        rating = "Necesita Mejora"
    else:
        rating = "Crítico"
    d.add(String(x + 150, y + 10, rating, fontSize=12,
                  fillColor=COLORS["text_light"], textAnchor="middle"))

    return d


def generate_pdf(data: dict, output_path: str) -> str:
    """Generate a complete GEO-SEO Pro PDF report."""
    if not HAS_REPORTLAB:
        return json.dumps({
            "error": "ReportLab is not installed. Install it with: pip install reportlab",
            "data": data,
        })

    styles = build_styles()
    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=15*mm, bottomMargin=15*mm,
    )
    story = []

    # ── COVER PAGE ──
    story.append(Spacer(1, 40*mm))
    story.append(Paragraph("GEO-SEO Pro", styles["CoverTitle"]))
    story.append(Paragraph("Informe de Auditoría de Posicionamiento<br/>para Buscadores Tradicionales y Motores de IA", styles["CoverSubtitle"]))
    story.append(Spacer(1, 10*mm))

    url = data.get("url", "N/A")
    date_str = datetime.now().strftime("%d de %B de %Y")
    story.append(Paragraph(f"<b>Sitio analizado:</b> {url}", styles["CoverSubtitle"]))
    story.append(Paragraph(f"<b>Fecha:</b> {date_str}", styles["CoverSubtitle"]))
    story.append(Spacer(1, 10*mm))

    # Overall score gauge
    overall = data.get("composite_score", data.get("score", 0))
    gauge = build_rating_gauge(overall)
    story.append(gauge)
    story.append(PageBreak())

    # ── EXECUTIVE SUMMARY ──
    story.append(Paragraph("1. Resumen Ejecutivo", styles["SectionTitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=COLORS["accent"]))
    story.append(Spacer(1, 3*mm))

    rating_labels = {
        (80, 100): "excelente estado de visibilidad tanto en buscadores tradicionales como en motores de IA.",
        (60, 79): "buen estado general, con áreas específicas que requieren optimización para maximizar la visibilidad en IA.",
        (40, 59): "estado intermedio. Se detectaron brechas significativas que limitan la visibilidad, especialmente en motores de IA generativos.",
        (0, 39): "estado crítico. Se requiere intervención fundamental en múltiples frentes para lograr visibilidad en buscadores e IA.",
    }
    rating_text = next(v for (lo, hi), v in rating_labels.items() if lo <= overall <= hi)

    story.append(Paragraph(
        f"El sitio <b>{url}</b> obtuvo una puntuación compuesta GEO-SEO de <b>{overall}/100</b>, "
        f"lo que indica un {rating_text}",
        styles["BodyText2"]
    ))
    story.append(Spacer(1, 5*mm))

    # ── SCORE BREAKDOWN ──
    story.append(Paragraph("2. Desglose de Puntuaciones", styles["SectionTitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=COLORS["accent"]))
    story.append(Spacer(1, 3*mm))

    score_breakdown = data.get("score_breakdown", {})
    if score_breakdown:
        score_data = []
        for cat, info in score_breakdown.items():
            if isinstance(info, dict):
                score_data.append([cat, f"{info.get('score', 'N/A')}/100",
                                   info.get("rating", "N/A")])
            else:
                score_data.append([cat, f"{info}/100", ""])

        t = Table(score_data, colWidths=[120, 80, 250])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
            ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("BACKGROUND", (0, 1), (-1, -1), COLORS["light_bg"]),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["light_bg"], white]),
            ("GRID", (0, 0), (-1, -1), 0.5, COLORS["medium_bg"]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        story.append(t)

    story.append(Spacer(1, 5*mm))

    # ── KEY FINDINGS ──
    story.append(Paragraph("3. Hallazgos Clave", styles["SectionTitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=COLORS["accent"]))
    story.append(Spacer(1, 3*mm))

    findings = data.get("findings", [])
    if not findings:
        findings = data.get("key_issues", [])

    for finding in findings[:10]:
        severity = finding.get("severity", "medium")
        color = COLORS["critical"] if severity == "critical" else (
            COLORS["warning"] if severity == "high" else (
                COLORS["accent"] if severity == "medium" else COLORS["text_light"]
            )
        )
        story.append(Paragraph(
            f'<font color="{color}"><b>[{severity.upper()}]</b></font> {finding.get("message", str(finding))}',
            styles["BodyText2"]
        ))
    story.append(PageBreak())

    # ── ACTION PLAN ──
    story.append(Paragraph("4. Plan de Acción Priorizado", styles["SectionTitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=COLORS["accent"]))
    story.append(Spacer(1, 3*mm))

    actions = data.get("action_plan", [])
    if not actions:
        actions = data.get("recommendations", [])

    # Group by timeframe
    quick = [a for a in actions if a.get("timeframe", "") == "quick"]
    medium = [a for a in actions if a.get("timeframe", "") == "medium"]
    strategic = [a for a in actions if a.get("timeframe", "") == "strategic"]

    for title, items, bg_color in [
        ("Quick Wins (1-7 días)", quick, HexColor("#c6f6d5")),
        ("Mediano Plazo (1-4 semanas)", medium, HexColor("#fefcbf")),
        ("Estratégico (1-6 meses)", strategic, HexColor("#bee3f8")),
    ]:
        if items:
            story.append(Paragraph(f"<b>{title}</b>", styles["BodyText2"]))
            for item in items:
                story.append(Paragraph(
                    f"• {item.get('action', str(item))}",
                    styles["BodyText2"]
                ))
            story.append(Spacer(1, 3*mm))

    # ── METHODOLOGY ──
    story.append(Paragraph("5. Metodología y Fuentes", styles["SectionTitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=COLORS["accent"]))
    story.append(Spacer(1, 3*mm))

    methodology_text = (
        "Este informe fue generado por GEO-SEO Pro, una herramienta de análisis de posicionamiento "
        "basada en las siguientes fuentes de investigación:"
        "<br/><br/>"
        "• <b>PageSpeed Insights API</b> — Métricas de Core Web Vitals en campo y laboratorio.<br/>"
        "• <b>Princeton GEO-bench (KDD 2024)</b> — Estudio científico sobre estrategias de visibilidad en IA.<br/>"
        "• <b>Google Search Central</b> — E-E-A-T, Helpful Content System, directrices oficiales.<br/>"
        "• <b>Backlinko</b> — Taxonomía de 128+ factores de ranking (2026).<br/>"
        "• <b>Especificación llms.txt</b> — Estándar de interfaz para agentes de IA.<br/>"
        "<br/>"
        "Las puntuaciones de Core Web Vitals provienen de mediciones reales de la API de Google. "
        "Las puntuaciones de contenido GEO se calculan mediante heurísticas basadas en el estudio "
        "Princeton GEO-bench. Los datos de acceso de crawlers se verifican parseando el robots.txt real."
    )
    story.append(Paragraph(methodology_text, styles["BodyText2"]))

    # Build PDF
    doc.build(story)
    return output_path


def main():
    if not HAS_REPORTLAB:
        print(json.dumps({
            "error": "ReportLab is not installed. Install with: pip install reportlab"
        }))
        sys.exit(1)

    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: report_pdf.py <data.json> [output.pdf]"}))
        sys.exit(1)

    data_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "GEO-SEO-PRO-REPORT.pdf"

    with open(data_path, "r") as f:
        data = json.load(f)

    result = generate_pdf(data, output_path)
    print(json.dumps({"status": "ok", "output": result, "size_bytes": os.path.getsize(result)}))


if __name__ == "__main__":
    main()
