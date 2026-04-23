#!/usr/bin/env python3
"""Generate single-page PDF with Q21 only."""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"

def generate():
    output_path = OUTPUT_DIR / "Q21_Single_Review.pdf"
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    lm = 0.75 * inch
    cw = width - 2 * lm
    
    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - 0.75*inch, "Q21 Review")
    
    y = height - 1.2*inch
    
    # Question
    c.setFont("Helvetica-Bold", 11)
    c.drawString(lm, y, "Q21. [H] [G] G5-Composite Overlap (5 marks)")
    y -= 0.25*inch
    
    c.setFont("Helvetica", 10)
    text = """The figure shows two overlapping quarter circles with radius 10 cm.
The shaded area OBC is 30 cm².

(a) Find the area of figure OABCD.
(b) Find the perimeter of figure OABCD."""
    
    for line in text.split('\n'):
        c.drawString(lm, y, line)
        y -= 0.18*inch
    
    # Diagram
    y -= 0.1*inch
    diag_path = OUTPUT_DIR / "Q21_v3_final.png"
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
    c.rect(lm, y - 1.2*inch, cw, 1.2*inch)
    y -= 1.4*inch
    
    c.drawString(lm, y, "(a) Area: _________________  (b) Perimeter: _________________")
    
    c.save()
    return output_path

if __name__ == "__main__":
    pdf_path = generate()
    print(f"✅ Generated: {pdf_path}")
