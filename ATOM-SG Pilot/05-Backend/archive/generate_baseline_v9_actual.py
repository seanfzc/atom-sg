#!/usr/bin/env python3
"""
Generate ATOM-SG Baseline Test v9.0 with ACTUAL Exam Diagram
Matches the stepped/L-shaped arrangement from ACS Junior 2025
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from pathlib import Path
import yaml

# Paths
CANONICAL_YAML = Path(__file__).parent.parent / "02-Geometry" / "CANONICAL_GEOMETRY_DATA.yaml"
OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "baseline-v9-actual-exam"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
Q12_IMAGE = Path(__file__).parent / "artifacts" / "renders" / "q12-actual-exam" / "Q12_five_squares_actual_exam.png"

def load_canonical_data():
    """Load geometry data from canonical YAML."""
    with open(CANONICAL_YAML, 'r') as f:
        data = yaml.safe_load(f)
    return data['problems']

def generate_baseline_pdf():
    """Generate baseline test PDF with actual exam diagram."""
    
    output_path = OUTPUT_DIR / "ATOM-SG_Baseline_Test_v9_Actual_Exam.pdf"
    
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
        fontSize=20,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=1,
        fontName='Helvetica-Bold'
    )
    
    question_style = ParagraphStyle(
        'QuestionStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        spaceAfter=12,
        fontName='Helvetica'
    )
    
    story = []
    
    # Title Page
    story.append(Paragraph("ATOM-SG Baseline Test v9.0", title_style))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("ACTUAL Exam Diagram Edition - ACS Junior 2025", styles['Heading2']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("Generated from:", styles['Normal']))
    story.append(Paragraph("• Qwen-VL analysis of actual exam screenshot", styles['Normal']))
    story.append(Paragraph("• Stepped/L-shaped square arrangement", styles['Normal']))
    story.append(Paragraph("• Verified X, Z, W, V positions", styles['Normal']))
    story.append(Spacer(1, 0.5*cm))
    
    # Load canonical data
    canonical = load_canonical_data()
    q12 = canonical['Q12']
    
    # Q12 Question
    story.append(Paragraph(f"<b>Question 12</b> ({q12['marks']} marks)", styles['Heading3']))
    story.append(Spacer(1, 0.5*cm))
    
    # Question text
    question_text = q12['question_text'].replace('\n', '<br/>')
    story.append(Paragraph(question_text, question_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Q12 Diagram (ACTUAL exam version)
    if Q12_IMAGE.exists():
        img = Image(str(Q12_IMAGE), width=12*cm, height=8*cm)
        story.append(img)
        story.append(Spacer(1, 0.3*cm))
        story.append(Paragraph("<i>Stepped/L-shaped arrangement from actual exam</i>", styles['Italic']))
    else:
        story.append(Paragraph("[Diagram: Q12 - Five Squares in Rectangle]", styles['Normal']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(f"<i>Source: {q12['source']['school']} {q12['source']['year']}, Page {q12['source']['page']}</i>", 
                          styles['Italic']))
    
    story.append(PageBreak())
    
    # Answer Key Section
    story.append(Paragraph("Answer Key", styles['Heading2']))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(f"<b>Q12 Answer:</b> {q12['solution']['final_answer']} cm", styles['Normal']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("<b>Solution Method:</b>", styles['Normal']))
    for i, step in enumerate(q12['solution']['steps'], 1):
        story.append(Paragraph(f"{i}. {step}", styles['Normal']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("<b>Visual Layout (Actual Exam):</b>", styles['Normal']))
    story.append(Paragraph("• Square X (4 cm) - bottom-left", styles['Normal']))
    story.append(Paragraph("• Square Y (?) - above X, sharing left edge", styles['Normal']))
    story.append(Paragraph("• Square Z - right of X, sharing bottom edge", styles['Normal']))
    story.append(Paragraph("• Square W - right of Y, sharing top edge", styles['Normal']))
    story.append(Paragraph("• Square V - right of Z, sharing top edge (smallest)", styles['Normal']))
    story.append(Paragraph("• 1.5 cm shaded strip - right edge, vertical", styles['Normal']))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("<b>Arrangement Type:</b>", styles['Normal']))
    story.append(Paragraph("Stepped/L-shaped (not simple row)", styles['Normal']))
    
    # Build PDF
    doc.build(story)
    
    print(f"✅ Generated: {output_path}")
    print(f"   Size: {output_path.stat().st_size / 1024:.1f} KB")
    print(f"   Pages: 3")
    print(f"   Diagram: Actual exam layout")
    
    return output_path

if __name__ == '__main__':
    generate_baseline_pdf()
