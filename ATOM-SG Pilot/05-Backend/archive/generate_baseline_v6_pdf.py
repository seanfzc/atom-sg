#!/usr/bin/env python3
"""
Generate Baseline Test v6.0 PDF using parametric diagrams
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from pathlib import Path
from datetime import datetime

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "baseline-v6-all"
PDF_OUTPUT = Path(__file__).parent / "artifacts" / "renders" / "baseline-v6-all" / "ATOM-SG_Baseline_Test_v6_Parametric.pdf"

def create_baseline_pdf():
    """Create the baseline test PDF."""
    
    doc = SimpleDocTemplate(
        str(PDF_OUTPUT),
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
    story.append(Paragraph("Version 6.0 - Parametric Approach", subtitle_style))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d')}", subtitle_style))
    story.append(Spacer(1, 1*cm))
    
    # Test Info
    story.append(Paragraph("Instructions:", section_style))
    story.append(Paragraph("1. This test contains 40 questions total:", question_style))
    story.append(Paragraph("   - 20 Word Problems", question_style))
    story.append(Paragraph("   - 12 Geometry Questions", question_style))
    story.append(Paragraph("   - 8 Data Interpretation Questions", question_style))
    story.append(Paragraph("2. All diagrams use parametric rendering with variable-driven elements.", question_style))
    story.append(Paragraph("3. Show all working clearly.", question_style))
    story.append(Spacer(1, 2*cm))
    
    # Section: Geometry
    story.append(PageBreak())
    story.append(Paragraph("Section 1: Geometry", section_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Q15: Overlapping Quarter Circles
    story.append(Paragraph("<b>Question 15 (5 marks)</b>", question_style))
    story.append(Paragraph(
        "The figure shows two overlapping quarter circles with centre O. "
        "Each quarter circle has a radius of 10 cm. The shaded part OBC has an area of 30 cm² "
        "and a perimeter of 26 cm. Find the area and perimeter of figure OABCD. "
        "(Take π = 3.14)",
        question_style
    ))
    story.append(Spacer(1, 0.3*cm))
    
    q15_img = OUTPUT_DIR / "Q15_overlapping_quarter_circles.png"
    if q15_img.exists():
        img = Image(str(q15_img), width=14*cm, height=11*cm)
        story.append(img)
    story.append(Spacer(1, 0.5*cm))
    
    # Answer space
    story.append(Paragraph("Answer: Area = __________ cm², Perimeter = __________ cm", question_style))
    story.append(Spacer(1, 1*cm))
    
    # Q12: Five Squares
    story.append(Paragraph("<b>Question 12 (4 marks)</b>", question_style))
    story.append(Paragraph(
        "The figure shows a rectangle made up of 5 squares. Square X has a side of 4 cm. "
        "Find (a) the side of square Y, (b) the length of the rectangle, "
        "(c) the number of 2 cm cubes that can be cut from the rectangle.",
        question_style
    ))
    story.append(Spacer(1, 0.3*cm))
    
    q12_img = OUTPUT_DIR / "Q12_five_squares.png"
    if q12_img.exists():
        img = Image(str(q12_img), width=12*cm, height=8*cm)
        story.append(img)
    story.append(Spacer(1, 0.5*cm))
    
    # Q19: 3D Solid
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 19 (3 marks)</b>", question_style))
    story.append(Paragraph(
        "The solid below is made up of 7 identical cubes. The top view and side view are shown. "
        "Draw the front view of the solid on the grid below.",
        question_style
    ))
    story.append(Spacer(1, 0.3*cm))
    
    q19_img = OUTPUT_DIR / "Q19_3d_solid.png"
    if q19_img.exists():
        img = Image(str(q19_img), width=12*cm, height=9*cm)
        story.append(img)
    story.append(Spacer(1, 0.5*cm))
    
    # Section: Data Interpretation
    story.append(PageBreak())
    story.append(Paragraph("Section 2: Data Interpretation", section_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Q35: Bar Chart
    story.append(Paragraph("<b>Question 35 (3 marks)</b>", question_style))
    story.append(Paragraph(
        "The bar graph shows the number of books read by 5 students. "
        "(a) Who read the most books? (b) How many books did they read in total? "
        "(c) What is the average number of books read?",
        question_style
    ))
    story.append(Spacer(1, 0.3*cm))
    
    q35_img = OUTPUT_DIR / "Q35_books_bar_chart.png"
    if q35_img.exists():
        img = Image(str(q35_img), width=12*cm, height=7.5*cm)
        story.append(img)
    story.append(Spacer(1, 0.5*cm))
    
    # Q37: Pie Chart
    story.append(Paragraph("<b>Question 37 (3 marks)</b>", question_style))
    story.append(Paragraph(
        "The pie chart shows how Isabelle spent her $100 pocket money. "
        "(a) How much did she spend on food? (b) What fraction was spent on transport? "
        "(c) How much did she save?",
        question_style
    ))
    story.append(Spacer(1, 0.3*cm))
    
    q37_img = OUTPUT_DIR / "Q37_spending_pie_chart.png"
    if q37_img.exists():
        img = Image(str(q37_img), width=9*cm, height=9*cm)
        story.append(img)
    story.append(Spacer(1, 0.5*cm))
    
    # Q33: Line Graph
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 33 (4 marks)</b>", question_style))
    story.append(Paragraph(
        "The line graph shows the sales of T-shirts over 6 months. "
        "(a) What was the increase in sales from Month 1 to Month 4? "
        "(b) Calculate the average monthly sales. "
        "(c) Express the sales in Month 6 as a percentage of Month 1.",
        question_style
    ))
    story.append(Spacer(1, 0.3*cm))
    
    q33_img = OUTPUT_DIR / "Q33_tshirt_sales_line_graph.png"
    if q33_img.exists():
        img = Image(str(q33_img), width=12*cm, height=7.5*cm)
        story.append(img)
    story.append(Spacer(1, 0.5*cm))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Baseline Test v6.0 PDF created: {PDF_OUTPUT}")
    print(f"   File size: {PDF_OUTPUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    print("=" * 60)
    print("Generating Baseline Test v6.0 PDF")
    print("=" * 60)
    create_baseline_pdf()
    print("=" * 60)
