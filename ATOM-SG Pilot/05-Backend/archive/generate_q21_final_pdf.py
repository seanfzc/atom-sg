#!/usr/bin/env python3
"""Generate final Q21 PDF for review."""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"

def generate():
    output_path = OUTPUT_DIR / "Q21_Final_Review.pdf"
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    lm = 0.75 * inch
    cw = width - 2 * lm
    
    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - 0.75*inch, "Q21 Final Review - ACS Junior Q15")
    
    y = height - 1.2*inch
    
    # Question
    c.setFont("Helvetica-Bold", 11)
    c.drawString(lm, y, "Q21. [H] [G] G5-Composite Overlap (5 marks)")
    y -= 0.25*inch
    
    c.setFont("Helvetica", 10)
    text = """Figure OABCD is formed by overlapping 2 similar quarter circles OAC and OBD.
OA = OB = OC = OD = 10 cm.
The area of the shaded part OBC is 30 cm² and the perimeter of the shaded part OBC is 26 cm.

(a) Find the area of figure OABCD. Take π = 3.14
(b) Find the perimeter of figure OABCD. Take π = 3.14"""
    
    for line in text.split('\n'):
        c.drawString(lm, y, line)
        y -= 0.18*inch
    
    # Diagram
    y -= 0.1*inch
    diag_path = OUTPUT_DIR / "Q21_proper.png"
    if diag_path.exists():
        img_width = 5 * inch
        img_height = 4 * inch
        x_pos = lm + (cw - img_width) / 2
        c.drawImage(str(diag_path), x_pos, y - img_height, width=img_width, height=img_height)
        y -= img_height + 0.2*inch
    
    # Working space
    c.setFont("Helvetica-Bold", 10)
    c.drawString(lm, y, "Working:")
    y -= 0.15*inch
    c.rect(lm, y - 1.0*inch, cw, 1.0*inch)
    y -= 1.2*inch
    
    c.drawString(lm, y, "(a) Area: _________________  (b) Perimeter: _________________")
    
    # Answer key on second page
    c.showPage()
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width/2, height - 0.75*inch, "Answer Key")
    
    y = height - 1.2*inch
    c.setFont("Courier", 9)
    
    answer = """Given:
  - Two quarter circles OAC and OBD, both centered at O
  - Radius r = 10 cm
  - Shaded sector OBC: area = 30 cm², perimeter = 26 cm
  - π = 3.14

Solution:
  From perimeter of OBC = 26 cm:
    OB + OC + arc BC = 26
    10 + 10 + arc BC = 26
    arc BC = 6 cm

  Verify area of OBC:
    Area = (1/2) × r × arc = (1/2) × 10 × 6 = 30 cm² ✓

(a) Area of OABCD:
    = Area(Q1) + Area(Q2) - Area(OBC)
    = (1/4)πr² + (1/4)πr² - 30
    = 78.5 + 78.5 - 30
    = 127 cm²

(b) Perimeter of OABCD:
    = arc AB + arc CD + OA + OD
    = 5.23 + 5.23 + 10 + 10
    = 30.5 cm
    
    (where arc AB = arc CD = (30/360) × 2πr = 5.23 cm)"""
    
    for line in answer.split('\n'):
        c.drawString(lm, y, line)
        y -= 0.15*inch
    
    c.save()
    return output_path

if __name__ == "__main__":
    pdf_path = generate()
    print(f"✅ Generated: {pdf_path}")
