#!/usr/bin/env python3
"""
Generate ATOM-SG Baseline Test v7.0 with Canonical Data
Uses CANONICAL_GEOMETRY_DATA.yaml as single source of truth
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from pathlib import Path
import yaml

# Paths
CANONICAL_YAML = Path(__file__).parent.parent / "02-Geometry" / "CANONICAL_GEOMETRY_DATA.yaml"
OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "baseline-v7-canonical"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
Q12_IMAGE = Path(__file__).parent / "artifacts" / "renders" / "canonical" / "Q12_five_squares_canonical.png"

def load_canonical_data():
    """Load geometry data from canonical YAML."""
    with open(CANONICAL_YAML, 'r') as f:
        data = yaml.safe_load(f)
    return data['problems']

def generate_baseline_pdf():
    """Generate baseline test PDF with canonical data."""
    
    output_path = OUTPUT_DIR / "ATOM-SG_Baseline_Test_v7_Canonical.pdf"
    
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=1  # Center
    )
    
    question_style = ParagraphStyle(
        'QuestionStyle',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        spaceAfter=12
    )
    
    story = []
    
    # Title
    story.append(Paragraph("ATOM-SG Baseline Test v7.0", title_style))
    story.append(Paragraph("Canonical Data Edition - ACS Junior 2025", styles['Heading2']))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("Generated from verified exam extraction", styles['Normal']))
    story.append(Spacer(1, 1*cm))
    
    # Load canonical data
    canonical = load_canonical_data()
    q12 = canonical['Q12']
    
    # Q12 Question
    story.append(Paragraph(f"<b>Question 12</b> ({q12['marks']} marks)", styles['Heading3']))
    story.append(Spacer(1, 0.3*cm))
    
    # Question text
    question_text = q12['question_text'].replace('\n', '<br/>')
    story.append(Paragraph(question_text, question_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Q12 Diagram
    if Q12_IMAGE.exists():
        img = Image(str(Q12_IMAGE), width=10*cm, height=6.67*cm)
        story.append(img)
    else:
        story.append(Paragraph("[Diagram: Q12 - Five Squares in Rectangle]", styles['Normal']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(f"<i>Source: {q12['source']['school']} {q12['source']['year']}, Page {q12['source']['page']}</i>", 
                          styles['Italic']))
    
    story.append(PageBreak())
    
    # Answer Key Section
    story.append(Paragraph("Answer Key", styles['Heading2']))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(f"<b>Q12 Answer:</b> {q12['solution']['final_answer']}", styles['Normal']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("<b>Solution Method:</b>", styles['Normal']))
    for step in q12['solution']['steps']:
        story.append(Paragraph(f"• {step}", styles['Normal']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(f"<b>Verified Dimensions:</b>", styles['Normal']))
    
    vars = q12['variables']
    for key in ['square_X', 'square_Y', 'square_Z', 'square_W', 'square_V']:
        v = vars[key]
        story.append(Paragraph(f"• {v['name']}: {v['side_cm']} cm", styles['Normal']))
    
    # Build PDF
    doc.build(story)
    
    print(f"✅ Generated: {output_path}")
    print(f"   Size: {output_path.stat().st_size / 1024:.1f} KB")
    
    return output_path

if __name__ == '__main__':
    generate_baseline_pdf()
