#!/usr/bin/env python3
"""
Generate ATOM-SG Baseline Test v8.0 with Proper Rendering
Uses math-diagram-rendering skill and parametric principles
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
OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "baseline-v8-proper"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
Q12_IMAGE = Path(__file__).parent / "artifacts" / "renders" / "q12-proper" / "Q12_five_squares_proper.png"

def load_canonical_data():
    """Load geometry data from canonical YAML."""
    with open(CANONICAL_YAML, 'r') as f:
        data = yaml.safe_load(f)
    return data['problems']

def generate_baseline_pdf():
    """Generate baseline test PDF with proper rendering."""
    
    output_path = OUTPUT_DIR / "ATOM-SG_Baseline_Test_v8_Proper.pdf"
    
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
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
        spaceAfter=15,
        fontName='Helvetica'
    )
    
    answer_style = ParagraphStyle(
        'AnswerStyle',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        leftIndent=20,
        spaceAfter=8,
        fontName='Helvetica'
    )
    
    story = []
    
    # Title Page
    story.append(Paragraph("ATOM-SG Baseline Test v8.0", title_style))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("Proper Rendering Edition", styles['Heading2']))
    story.append(Spacer(1, 1*cm))
    
    story.append(Paragraph("Generated using:", styles['Normal']))
    story.append(Paragraph("• Math Diagram Rendering Skill (4-gates)", answer_style))
    story.append(Paragraph("• Parametric Visual Rendering Guide", answer_style))
    story.append(Paragraph("• Canonical Data from ACS Junior 2025", answer_style))
    story.append(Spacer(1, 1*cm))
    
    story.append(Paragraph("<b>Key Features:</b>", styles['Normal']))
    story.append(Paragraph("✓ Exam-accurate Q12 diagram", answer_style))
    story.append(Paragraph("✓ Proper scale and labeling", answer_style))
    story.append(Paragraph("✓ P6-appropriate visual language", answer_style))
    story.append(Paragraph("✓ Verified dimensions from source", answer_style))
    
    story.append(PageBreak())
    
    # Load canonical data
    canonical = load_canonical_data()
    q12 = canonical['Q12']
    
    # Q12 Question Page
    story.append(Paragraph(f"<b>Question 12</b> ({q12['marks']} marks)", styles['Heading2']))
    story.append(Spacer(1, 0.5*cm))
    
    # Question text
    question_text = q12['question_text'].replace('\n', '<br/>')
    story.append(Paragraph(question_text, question_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Q12 Diagram
    if Q12_IMAGE.exists():
        img = Image(str(Q12_IMAGE), width=12*cm, height=8*cm)
        story.append(img)
        story.append(Spacer(1, 0.3*cm))
        story.append(Paragraph("<i>Diagram generated using 4-gates rendering approach</i>", 
                              styles['Italic']))
    else:
        story.append(Paragraph("[Diagram: Q12 - Five Squares in Rectangle]", styles['Normal']))
    
    story.append(Spacer(1, 0.5*cm))
    
    # Source info
    source_info = f"Source: {q12['source']['school']} {q12['source']['year']}, " \
                  f"Paper {q12['source']['paper']}, Page {q12['source']['page']}"
    story.append(Paragraph(source_info, styles['Italic']))
    
    story.append(PageBreak())
    
    # Answer Key
    story.append(Paragraph("Answer Key & Solution", styles['Heading2']))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(f"<b>Q12 Answer:</b> {q12['solution']['final_answer']}", 
                          styles['Heading3']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("<b>Solution Steps (P6 Level):</b>", styles['Normal']))
    for i, step in enumerate(q12['solution']['steps'], 1):
        story.append(Paragraph(f"{i}. {step}", answer_style))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("<b>Verified Dimensions:</b>", styles['Normal']))
    vars = q12['variables']
    for key in ['square_X', 'square_Y', 'square_Z', 'square_W', 'square_V']:
        v = vars[key]
        given = " (given)" if v.get('given', False) else ""
        answer = " ✓" if v.get('answer', False) else ""
        story.append(Paragraph(f"• Square {v['name']}: {v['side_cm']} cm{given}{answer}", 
                              answer_style))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("<b>Rendering Principles Applied:</b>", styles['Normal']))
    story.append(Paragraph("• Gate 0: Solved problem first", answer_style))
    story.append(Paragraph("• Gate 1: P6-appropriate labels", answer_style))
    story.append(Paragraph("• Gate 2: Visual anchors for reasoning", answer_style))
    story.append(Paragraph("• Gate 3: Consistent scale (1 cm = 40 px)", answer_style))
    story.append(Paragraph("• Parametric: All elements derived from variables", answer_style))
    
    # Build PDF
    doc.build(story)
    
    print(f"✅ Generated: {output_path}")
    print(f"   Size: {output_path.stat().st_size / 1024:.1f} KB")
    print(f"   Pages: 3")
    
    return output_path

if __name__ == '__main__':
    generate_baseline_pdf()
