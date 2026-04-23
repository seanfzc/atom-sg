#!/usr/bin/env python3
"""
Generate Baseline Test v6.0 FIXED PDF using corrected diagrams
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from pathlib import Path
from datetime import datetime

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "baseline-v6-fixed"
PDF_OUTPUT = OUTPUT_DIR / "ATOM-SG_Baseline_Test_v6_FIXED.pdf"

def create_baseline_pdf():
    """Create the baseline test PDF with fixed diagrams."""
    
    doc = SimpleDocTemplate(
        str(PDF_OUTPUT),
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
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=12,
        alignment=TA_CENTER,
        spaceAfter=30,
        fontName='Helvetica'
    )
    
    question_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_LEFT,
        spaceAfter=10,
        fontName='Helvetica'
    )
    
    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading2'],
        fontSize=14,
        alignment=TA_LEFT,
        spaceAfter=15,
        fontName='Helvetica-Bold'
    )
    
    story = []
    
    # Title Page
    story.append(Paragraph("ATOM-SG Baseline Test", title_style))
    story.append(Paragraph("Version 6.0 - FIXED", subtitle_style))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", subtitle_style))
    story.append(Spacer(1, 1*cm))
    
    # Test Info
    story.append(Paragraph("Instructions:", section_style))
    story.append(Paragraph("1. This test contains sample questions with FIXED diagrams.", question_style))
    story.append(Paragraph("2. All diagrams verified for accuracy and solvability.", question_style))
    story.append(Paragraph("3. Show all working clearly.", question_style))
    story.append(Spacer(1, 2*cm))
    
    # Section: Geometry
    story.append(PageBreak())
    story.append(Paragraph("Section 1: Geometry (FIXED)", section_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Q15: Overlapping Quarter Circles (FIXED)
    story.append(Paragraph("<b>Question 15 (5 marks) - FIXED</b>", question_style))
    story.append(Paragraph(
        "The figure shows two overlapping quarter circles with centre O. "
        "Each quarter circle has a radius of 10 cm. The shaded part OBC has an area of 30 cm² "
        "and a perimeter of 26 cm. Find the area and perimeter of figure OABCD. "
        "(Take π = 3.14)",
        question_style
    ))
    story.append(Spacer(1, 0.3*cm))
    
    q15_img = OUTPUT_DIR / "Q15_overlapping_quarter_circles_FIXED.png"
    if q15_img.exists():
        img = Image(str(q15_img), width=14*cm, height=11*cm)
        story.append(img)
    story.append(Spacer(1, 0.5*cm))
    
    # Q12: Five Squares (FIXED)
    story.append(Paragraph("<b>Question 12 (4 marks) - FIXED</b>", question_style))
    story.append(Paragraph(
        "The figure shows a rectangle made up of 5 squares. Square X has a side of 4 cm. "
        "Find (a) the side of square Y, (b) the length of the rectangle, "
        "(c) the number of 2 cm cubes that can be cut from the rectangle.",
        question_style
    ))
    story.append(Spacer(1, 0.3*cm))
    
    q12_img = OUTPUT_DIR / "Q12_five_squares_FIXED.png"
    if q12_img.exists():
        img = Image(str(q12_img), width=12*cm, height=8*cm)
        story.append(img)
    story.append(Spacer(1, 0.5*cm))
    
    # Q19: 3D Solid (FIXED)
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 19 (3 marks) - FIXED</b>", question_style))
    story.append(Paragraph(
        "The solid below is made up of 7 identical cubes. The isometric view is shown with front direction indicated. "
        "Draw the front view of the solid on the grid provided.",
        question_style
    ))
    story.append(Spacer(1, 0.3*cm))
    
    q19_img = OUTPUT_DIR / "Q19_3d_solid_FIXED.png"
    if q19_img.exists():
        img = Image(str(q19_img), width=14*cm, height=10*cm)
        story.append(img)
    story.append(Spacer(1, 0.5*cm))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Baseline Test v6.0 FIXED PDF created: {PDF_OUTPUT}")
    print(f"   File size: {PDF_OUTPUT.stat().st_size / 1024:.1f} KB")
    return PDF_OUTPUT


if __name__ == "__main__":
    print("=" * 60)
    print("Generating Baseline Test v6.0 FIXED PDF")
    print("=" * 60)
    pdf_path = create_baseline_pdf()
    print("=" * 60)
    print(f"PDF_PATH:{pdf_path}")
