#!/usr/bin/env python3
"""
Generate FINAL baseline test with PROFESSIONAL PNG renders embedded inline.
Uses the high-quality renders from generate_renders.py (now with PNG output).
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from datetime import datetime
import subprocess
import sys

BACKEND_DIR = Path(__file__).parent
RENDERS_DIR = BACKEND_DIR / "artifacts" / "renders"
OUTPUT_DIR = RENDERS_DIR

def ensure_renders():
    """Generate professional renders if needed."""
    render_script = BACKEND_DIR / "generate_renders.py"
    if render_script.exists():
        # Check if PNGs exist
        png_count = len(list(RENDERS_DIR.glob("G*-v1.png")))
        if png_count < 20:
            print("Generating professional renders with PNG output...")
            subprocess.run([sys.executable, str(render_script)], 
                         capture_output=True, cwd=BACKEND_DIR)
            print(f"✓ Renders generated")

# Problem definitions with render mappings
PROBLEMS = [
    # WORD PROBLEMS (20) - no diagrams
    {"num": 1, "id": "WP001", "type": "WP", "pathway": "Before-After", "diff": "E", 
     "text": "A shop had 240 pens. On Monday, they sold 2/5 of the pens. On Tuesday, they sold 1/3 of the remaining pens. How many pens were left?", "ans": "96 pens"},
    {"num": 2, "id": "WP002", "type": "WP", "pathway": "Before-After", "diff": "M", 
     "text": "Sarah spent 3/8 of her money on a book and 2/5 of the remainder on a pen. If she had $30 left, how much did she have at first?", "ans": "$80"},
    {"num": 3, "id": "WP003", "type": "WP", "pathway": "Part-Whole", "diff": "E", 
     "text": "Ali has $120. Ben has 3/4 as much as Ali. How much money do they have altogether?", "ans": "$210"},
    {"num": 4, "id": "WP004", "type": "WP", "pathway": "Part-Whole", "diff": "M", 
     "text": "The ratio of boys to girls in a class is 5:3. If there are 40 students altogether, how many boys are there?", "ans": "25 boys"},
    {"num": 5, "id": "WP005", "type": "WP", "pathway": "Cross-Thread", "diff": "M", 
     "text": "A baker made 360 cupcakes. He sold 1/4 of them in the morning and 2/3 of the remainder in the afternoon. How many cupcakes did he have left?", "ans": "90 cupcakes"},
    {"num": 6, "id": "WP006", "type": "WP", "pathway": "Cross-Thread", "diff": "H", 
     "text": "Alice and Betty had $280 altogether. After Alice spent 1/3 of her money and Betty spent $40, they had the same amount left. How much did Alice have at first?", "ans": "$144"},
    {"num": 7, "id": "WP007", "type": "WP", "pathway": "Before-After", "diff": "M", 
     "text": "A tank was full of water. After 3/7 of the water was poured out, then 2/5 of the remaining water was used, 48 litres were left. How much water was in the tank at first?", "ans": "140 litres"},
    {"num": 8, "id": "WP008", "type": "WP", "pathway": "Part-Whole", "diff": "M", 
     "text": "John has 3/5 as many stamps as Mary. Mary has 5/6 as many stamps as Tom. If Tom has 72 stamps, how many stamps does John have?", "ans": "36 stamps"},
    {"num": 9, "id": "WP009", "type": "WP", "pathway": "Before-After", "diff": "E", 
     "text": "A bus had 60 passengers. At the first stop, 15 passengers got off. At the second stop, 8 passengers got off. How many passengers were left?", "ans": "37 passengers"},
    {"num": 10, "id": "WP010", "type": "WP", "pathway": "Cross-Thread", "diff": "H", 
     "text": "The ratio of red balls to blue balls in a bag was 3:5. After removing 12 red balls, the ratio became 1:3. How many red balls were there at first?", "ans": "27 red balls"},
    {"num": 11, "id": "WP011", "type": "WP", "pathway": "Cross-Thread", "diff": "H", 
     "text": "The ratio of Alan's age to Ben's age is 4:7. In 6 years, the ratio will be 2:3. How old is Alan now?", "ans": "24 years old"},
    {"num": 12, "id": "WP012", "type": "WP", "pathway": "Before-After", "diff": "M", 
     "text": "A library had 450 books. They received 120 new books on Monday. On Tuesday, they donated 1/5 of their total books to a school. How many books did they have left?", "ans": "456 books"},
    {"num": 13, "id": "WP013", "type": "WP", "pathway": "Part-Whole", "diff": "E", 
     "text": "There are 80 students in a hall. 3/8 of them are girls. How many boys are there?", "ans": "50 boys"},
    {"num": 14, "id": "WP014", "type": "WP", "pathway": "Cross-Thread", "diff": "M", 
     "text": "A fruit seller had 240 apples. He sold 3/4 of them to Shop A and 1/2 of the remainder to Shop B. How many apples did he have left?", "ans": "30 apples"},
    {"num": 15, "id": "WP015", "type": "WP", "pathway": "Part-Whole", "diff": "M", 
     "text": "Jenny and Kelly have 84 stickers altogether. Jenny has 16 more stickers than Kelly. How many stickers does Kelly have?", "ans": "34 stickers"},
    {"num": 16, "id": "WP016", "type": "WP", "pathway": "Before-After", "diff": "H", 
     "text": "A shop increased the price of a bag by 20%. During a sale, they offered a 15% discount on the new price. If the final price was $204, what was the original price?", "ans": "$200"},
    {"num": 17, "id": "WP017", "type": "WP", "pathway": "Part-Whole", "diff": "H", 
     "text": "The ratio of apples to oranges to pears is 2:3:5. If there are 120 oranges and pears altogether, how many apples are there?", "ans": "30 apples"},
    {"num": 18, "id": "WP018", "type": "WP", "pathway": "Cross-Thread", "diff": "H", 
     "text": "A tank was 5/6 full of water. After 15 litres were poured out, it was 2/3 full. What is the capacity of the tank?", "ans": "90 litres"},
    {"num": 19, "id": "WP019", "type": "WP", "pathway": "Before-After", "diff": "M", 
     "text": "Mrs. Tan had some money in her purse. She spent $25 on groceries and then deposited 1/4 of the remainder into her bank account. If she had $45 left, how much did she have at first?", "ans": "$85"},
    {"num": 20, "id": "WP020", "type": "WP", "pathway": "Part-Whole", "diff": "M", 
     "text": "The ratio of boys to girls in a club is 5:3. There are 24 more boys than girls. How many children are in the club?", "ans": "96 children"},
    
    # GEOMETRY (12) - Professional renders
    {"num": 21, "id": "G001", "type": "G", "pathway": "Geometry-Angle", "diff": "E", 
     "text": "Measure the angles A, B, and C in the diagram using a protractor.", "ans": "See rubric", "render": "G001-angle-diagram-v1.png"},
    {"num": 22, "id": "G002", "type": "G", "pathway": "Geometry-Angle", "diff": "E", 
     "text": "Two angles on a straight line are given. If one angle is 75°, find the other angle.", "ans": "105°", "render": "G002-angle-diagram-v1.png"},
    {"num": 23, "id": "G005", "type": "G", "pathway": "Geometry-Triangle", "diff": "M", 
     "text": "In triangle ABC, angle A = 50° and angle B = 70°. Find angle C.", "ans": "60°", "render": "G005-triangle-v1.png"},
    {"num": 24, "id": "G007", "type": "G", "pathway": "Geometry-Angle", "diff": "H", 
     "text": "Angle A and Angle B are on a straight line. Angle B and Angle C are complementary. If Angle A = 110°, find Angle C.", "ans": "20°", "render": "G007-angle-diagram-v1.png"},
    {"num": 25, "id": "G009", "type": "G", "pathway": "Geometry-Perimeter", "diff": "E", 
     "text": "Find the perimeter of the rectangle shown in the diagram.", "ans": "26 cm", "render": "G009-rectangle-v1.png"},
    {"num": 26, "id": "G010", "type": "G", "pathway": "Geometry-Composite", "diff": "M", 
     "text": "A rectilinear figure consists of two rectangles joined together. Find its perimeter.", "ans": "See rubric", "render": "G010-composite-shape-v1.png"},
    {"num": 27, "id": "G011", "type": "G", "pathway": "Geometry-Area", "diff": "M", 
     "text": "Find the area of an L-shape figure formed by two rectangles.", "ans": "See rubric", "render": "G011-composite-shape-v1.png"},
    {"num": 28, "id": "G014", "type": "G", "pathway": "Geometry-Conversion", "diff": "M", 
     "text": "Convert 2.5 square metres to square centimetres.", "ans": "25,000 cm²", "render": "G014-conversion-v1.png"},
    {"num": 29, "id": "G017", "type": "G", "pathway": "Geometry-Volume", "diff": "E", 
     "text": "Find the volume of the cuboid shown in the diagram.", "ans": "72 cm³", "render": "G017-cuboid-v1.png"},
    {"num": 30, "id": "G019", "type": "G", "pathway": "Geometry-3D", "diff": "M", 
     "text": "Which of the following nets can be folded to form a cube?", "ans": "See rubric", "render": "G019-net-v1.png"},
    {"num": 31, "id": "G021", "type": "G", "pathway": "Geometry-Classify", "diff": "E", 
     "text": "Classify the triangle with side lengths 5 cm, 5 cm, 5 cm.", "ans": "Equilateral", "render": "G021-triangle-classification-v1.png"},
    {"num": 32, "id": "G024", "type": "G", "pathway": "Geometry-Circle", "diff": "M", 
     "text": "A circle has radius 7 cm as shown. Find its circumference (take π = 22/7).", "ans": "44 cm", "render": "G024-circle-v1.png"},
    
    # DATA INTERPRETATION (8)
    {"num": 33, "id": "DI021", "type": "DI", "pathway": "DI-Pie Chart", "diff": "E", 
     "text": "The pie chart shows fruit distribution. What fraction represents the 72° sector?", "ans": "1/5", "render": "G025-pie-chart-v1.png"},
    {"num": 34, "id": "DI022", "type": "DI", "pathway": "DI-Pie Chart", "diff": "E", 
     "text": "If 72° represents 60 apples, how many fruits are there in total?", "ans": "300 fruits", "render": "G025-pie-chart-v1.png"},
    {"num": 35, "id": "DI023", "type": "DI", "pathway": "DI-Pie Chart", "diff": "M", 
     "text": "Calculate the percentage for each fruit type in the pie chart.", "ans": "See working", "render": "G025-pie-chart-v1.png"},
    {"num": 36, "id": "DI024", "type": "DI", "pathway": "DI-Chart", "diff": "M", 
     "text": "The chart shows survey results. Which category has the highest percentage?", "ans": "See chart", "render": None},
    {"num": 37, "id": "DI025", "type": "DI", "pathway": "DI-Chart", "diff": "M", 
     "text": "Calculate the difference between the largest and smallest sectors.", "ans": "See working", "render": None},
    {"num": 38, "id": "DI026", "type": "DI", "pathway": "DI-Chart", "diff": "H", 
     "text": "If the total number of respondents was 500, how many chose each category?", "ans": "See working", "render": None},
    {"num": 39, "id": "DI027", "type": "DI", "pathway": "DI-Pie Chart", "diff": "M", 
     "text": "Convert each sector angle to a fraction of the whole circle.", "ans": "See working", "render": "G025-pie-chart-v1.png"},
    {"num": 40, "id": "DI028", "type": "DI", "pathway": "DI-Pie Chart", "diff": "H", 
     "text": "If oranges represent 90° and there are 75 oranges, find the total number of fruits.", "ans": "300 fruits", "render": "G025-pie-chart-v1.png"},
]

def wrap_text(c, text, x, y, max_width, font_size=9, line_height=0.14*inch):
    c.setFont("Helvetica", font_size)
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = ' '.join(current + [word])
        if c.stringWidth(test, "Helvetica", font_size) <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(' '.join(current))
            current = [word]
    if current:
        lines.append(' '.join(current))
    for line in lines:
        c.drawString(x, y, line)
        y -= line_height
    return y

def generate_pdf(output_path):
    ensure_renders()
    
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    lm = 0.5 * inch
    rm = 0.5 * inch
    tm = 0.5 * inch
    bm = 0.5 * inch
    cw = width - lm - rm
    
    # Header
    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(width/2, height - tm, "ATOM-SG Pilot - Week 1 Baseline Test")
    c.setFont("Helvetica", 10)
    c.drawCentredString(width/2, height - tm - 0.2*inch, "P6 Mathematics | 40 Questions | 50 Minutes | No Calculator")
    
    c.setFont("Helvetica-Bold", 9)
    y = height - tm - 0.55*inch
    c.drawString(lm, y, "Name: _________________________________  Class: _______  Date: ___________")
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 8)
    c.drawString(lm, y, "Instructions: Show all working. Professional-grade diagrams included with Geometry questions.")
    y -= 0.18*inch
    
    for prob in PROBLEMS:
        has_render = prob.get("render") and (RENDERS_DIR / prob["render"]).exists()
        
        space_needed = 1.0 * inch
        if has_render:
            space_needed += 2.3 * inch
        
        if y - space_needed < bm:
            c.showPage()
            y = height - tm
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(width/2, y, "Baseline Test - Continued")
            y -= 0.25*inch
        
        c.setFont("Helvetica-Bold", 8)
        c.drawString(lm, y, f"Q{prob['num']:2d}. [{prob['diff']}] [{prob['type']}] {prob['pathway'][:28]}")
        y -= 0.16*inch
        
        c.setFont("Helvetica", 9)
        y = wrap_text(c, prob['text'], lm + 0.05*inch, y, cw - 0.1*inch, font_size=9, line_height=0.14*inch)
        
        # Embed professional PNG render
        if has_render:
            y -= 0.1*inch
            render_path = RENDERS_DIR / prob["render"]
            img_width = 3.0 * inch
            img_height = 2.0 * inch
            x_pos = lm + (cw - img_width) / 2
            try:
                c.drawImage(str(render_path), x_pos, y - img_height, width=img_width, height=img_height)
                y -= img_height + 0.1*inch
            except Exception as e:
                print(f"Error embedding {render_path}: {e}")
                c.setFillColorRGB(0.9, 0.9, 0.9)
                c.rect(x_pos, y - img_height, img_width, img_height, fill=1, stroke=1)
                c.setFillColorRGB(0, 0, 0)
                c.setFont("Helvetica-Oblique", 10)
                c.drawCentredString(x_pos + img_width/2, y - img_height/2, "[Diagram]")
                y -= img_height + 0.1*inch
        
        y -= 0.06*inch
        c.setFont("Helvetica-Bold", 7)
        c.drawString(lm + 0.05*inch, y, "Working:")
        y -= 0.12*inch
        wh = 0.5 * inch
        c.rect(lm + 0.05*inch, y - wh, cw - 0.15*inch, wh)
        y -= wh + 0.1*inch
        
        c.setFont("Helvetica-Bold", 8)
        c.drawString(lm + 0.05*inch, y, f"Answer: _________________________")
        y -= 0.18*inch
        
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.line(lm, y, width - rm, y)
        c.setStrokeColorRGB(0, 0, 0)
        y -= 0.1*inch
    
    # Answer key
    c.showPage()
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(width/2, height - tm, "Answer Key - For Markers Only")
    y = height - tm - 0.4*inch
    c.setFont("Courier", 8)
    for prob in PROBLEMS:
        c.drawString(lm, y, f"Q{prob['num']:2d}: {prob['ans'][:50]}")
        y -= 0.13*inch
        if y < bm:
            c.showPage()
            y = height - tm
    
    c.save()
    print(f"\n✅ Generated: {output_path}")
    print(f"   40 questions with professional PNG renders")

if __name__ == "__main__":
    output_path = OUTPUT_DIR / "ATOM-SG_Baseline_Test_FINAL.pdf"
    generate_pdf(output_path)
