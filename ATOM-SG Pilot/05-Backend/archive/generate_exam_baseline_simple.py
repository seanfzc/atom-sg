#!/usr/bin/env python3
"""
Generate EXAM-QUALITY 40-question baseline test - Simplified Version
Uses existing test outputs from rendering modules
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Copy existing test outputs
import shutil
source_dir = Path(__file__).parent / "rendering" / "test_outputs"
if source_dir.exists():
    for f in source_dir.glob("*.png"):
        shutil.copy(f, OUTPUT_DIR)
    print(f"Copied {len(list(source_dir.glob('*.png')))} diagram files")

# Define 40 exam-quality problems
PROBLEMS = [
    # WORD PROBLEMS (20) - Cross-Thread Collision
    {"num": 1, "id": "WP001", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Mrs. Lee spent $240 on groceries. She spent 2/5 of the remainder on a dress, then 1/3 of the new remainder on shoes. If she had $72 left, how much did she have at first?",
     "answer": "$480", "marks": 4},
    
    {"num": 2, "id": "WP002", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A tank was 5/6 full. After pouring out 15 litres, it was 2/3 full. What is the capacity of the tank?",
     "answer": "90 litres", "marks": 3},
    
    {"num": 3, "id": "WP003", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "The ratio of red to blue balls was 3:5. After removing 12 red balls, the ratio became 1:3. How many red balls were there at first?",
     "answer": "27 red balls", "marks": 4},
    
    {"num": 4, "id": "WP004", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Alan and Ben's ages are in ratio 4:7. In 6 years, the ratio will be 2:3. How old is Alan now?",
     "answer": "24 years old", "marks": 4},
    
    {"num": 5, "id": "WP005", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A shop had 240 pens. On Monday, they sold 2/5 of the pens. On Tuesday, they sold 1/3 of the remainder. On Wednesday, they sold 1/2 of the new remainder. How many pens were left?",
     "answer": "48 pens", "marks": 4},
    
    {"num": 6, "id": "WP006", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Alice and Betty had $280. After Alice spent 1/3 of her money and Betty spent $40, they had equal amounts. How much did Alice have at first?",
     "answer": "$144", "marks": 4},
    
    {"num": 7, "id": "WP007", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A baker made 360 cupcakes. He sold 1/4 in the morning and 2/3 of the remainder in the afternoon. How many cupcakes did he have left?",
     "answer": "90 cupcakes", "marks": 3},
    
    {"num": 8, "id": "WP008", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "John has 3/5 as many stamps as Mary. Mary has 5/6 as many as Tom. If Tom has 72 stamps, how many does John have?",
     "answer": "36 stamps", "marks": 3},
    
    {"num": 9, "id": "WP009", "type": "WP", "pathway": "Part-Whole", "diff": "M",
     "text": "The ratio of boys to girls in a class is 5:3. If there are 40 students altogether, how many boys are there?",
     "answer": "25 boys", "marks": 2},
    
    {"num": 10, "id": "WP010", "type": "WP", "pathway": "Before-After", "diff": "M",
     "text": "A bus had 60 passengers. 15 got off at the first stop, then 8 at the second. How many were left?",
     "answer": "37 passengers", "marks": 2},
    
    {"num": 11, "id": "WP011", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Ali and Ben had $280 altogether. After Ali gave 1/4 of his money to Ben, they had the same amount. How much did Ali have at first?",
     "answer": "$160", "marks": 4},
    
    {"num": 12, "id": "WP012", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A tank was full. After 3/7 was poured out, then 2/5 of the remainder was used, 48 litres were left. How much was in the tank at first?",
     "answer": "140 litres", "marks": 4},
    
    {"num": 13, "id": "WP013", "type": "WP", "pathway": "Part-Whole", "diff": "M",
     "text": "There are 80 students. 3/8 are girls. How many boys are there?",
     "answer": "50 boys", "marks": 2},
    
    {"num": 14, "id": "WP014", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A seller had 240 apples. He sold 3/4 to Shop A and 1/2 of the remainder to Shop B. How many were left?",
     "answer": "30 apples", "marks": 3},
    
    {"num": 15, "id": "WP015", "type": "WP", "pathway": "Part-Whole", "diff": "M",
     "text": "Jenny and Kelly have 84 stickers. Jenny has 16 more than Kelly. How many does Kelly have?",
     "answer": "34 stickers", "marks": 2},
    
    {"num": 16, "id": "WP016", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A bag's price increased by 20%, then had a 15% discount. If the final price was $204, what was the original?",
     "answer": "$200", "marks": 4},
    
    {"num": 17, "id": "WP017", "type": "WP", "pathway": "Part-Whole", "diff": "H",
     "text": "Apples:Oranges:Pears = 2:3:5. If oranges and pears total 120, how many apples are there?",
     "answer": "30 apples", "marks": 3},
    
    {"num": 18, "id": "WP018", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Mrs. Tan spent $25 on groceries, then deposited 1/4 of the remainder. If $45 was left, how much did she start with?",
     "answer": "$85", "marks": 3},
    
    {"num": 19, "id": "WP019", "type": "WP", "pathway": "Part-Whole", "diff": "M",
     "text": "Boys:Girls = 5:3. There are 24 more boys than girls. How many children in total?",
     "answer": "96 children", "marks": 3},
    
    {"num": 20, "id": "WP020", "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A library had 450 books. They received 120 new books, then donated 1/5 of the total. How many books remained?",
     "answer": "456 books", "marks": 3},
    
    # GEOMETRY (12) - G5-G8
    {"num": 21, "id": "G021", "type": "G", "pathway": "G5-Composite Overlap", "diff": "H",
     "text": "The figure shows two overlapping quarter circles with radius 10 cm. The shaded area OBC is 30 cm². (a) Find the area of figure OABCD. (b) Find the perimeter of figure OABCD.",
     "answer": "(a) 127 cm² (b) 45.4 cm", "marks": 5, "diagram": "composite_quarter_circles.png"},
    
    {"num": 22, "id": "G022", "type": "G", "pathway": "G6-Grid Construction", "diff": "H",
     "text": "Triangle ABC is drawn on the grid. (a) Measure angle ACB. (b) Complete trapezium BCDE where BC is parallel to DE, AB = BE, and DE is twice as long as BC.",
     "answer": "(a) 36° (b) See diagram", "marks": 4, "diagram": "grid_protractor.png"},
    
    {"num": 23, "id": "G023", "type": "G", "pathway": "G7-3D Visualization", "diff": "H",
     "text": "The solid is made up of 8 cubes. (a) Draw the front view of the solid on the grid. (b) What is the maximum number of cubes that can be added without changing the front and side views?",
     "answer": "(a) See diagram (b) 8 cubes", "marks": 4, "diagram": "iso_cubes.png"},
    
    {"num": 24, "id": "G024", "type": "G", "pathway": "G8-Angle Chasing", "diff": "H",
     "text": "In the figure, ABCD is a rhombus and ADEF is a trapezium with AF parallel to DE. Given angle DFE = 21°, angle BCD = 108°, and angle DAB = 33°, find angles x and y.",
     "answer": "x = 18°, y = 126°", "marks": 5, "diagram": "composite_reflex_angle.png"},
    
    {"num": 25, "id": "G025", "type": "G", "pathway": "G5-Composite Overlap", "diff": "M",
     "text": "Five squares are drawn inside a rectangle. Square X has side 4 cm. Find (a) the side of square Y, (b) the length of the rectangle, (c) how many 2cm cubes can be made from the five squares.",
     "answer": "(a) 2 cm (b) 17.5 cm (c) 38 cubes", "marks": 5, "diagram": "composite_multi_shape.png"},
    
    {"num": 26, "id": "G026", "type": "G", "pathway": "G1-Angle Reasoning", "diff": "E",
     "text": "In the diagram, AOB is a straight line. If angle AOC = 65°, find angle COB.",
     "answer": "115°", "marks": 2},
    
    {"num": 27, "id": "G027", "type": "G", "pathway": "G8-Angle Chasing", "diff": "M",
     "text": "Three angles meet at a point. Two angles are 120° and 85°. Find the third angle.",
     "answer": "155°", "marks": 2},
    
    {"num": 28, "id": "G028", "type": "G", "pathway": "G1-Angle Reasoning", "diff": "M",
     "text": "Two straight lines intersect. If one angle is 40°, find the other three angles.",
     "answer": "40°, 140°, 140°", "marks": 2},
    
    {"num": 29, "id": "G029", "type": "G", "pathway": "G2-Area", "diff": "M",
     "text": "In triangle ABC, angle A = 50° and angle B = 70°. Find angle C.",
     "answer": "60°", "marks": 2},
    
    {"num": 30, "id": "G030", "type": "G", "pathway": "G2-Composite", "diff": "M",
     "text": "The figure shows an L-shape made of two rectangles. Find its area and perimeter.",
     "answer": "Area = 64 cm², Perimeter = 34 cm", "marks": 3, "diagram": "iso_lshape.png"},
    
    {"num": 31, "id": "G031", "type": "G", "pathway": "G2-Area", "diff": "M",
     "text": "A rectangular sheet has a smaller rectangle cut out. Find the remaining area.",
     "answer": "See working", "marks": 3},
    
    {"num": 32, "id": "G032", "type": "G", "pathway": "G3-Volume", "diff": "M",
     "text": "Find the volume of a cuboid with length 6 cm, breadth 4 cm, and height 3 cm.",
     "answer": "72 cm³", "marks": 2},
    
    # DATA INTERPRETATION (8)
    {"num": 33, "id": "DI033", "type": "DI", "pathway": "DI1-Line Graph", "diff": "H",
     "text": "The line graph shows T-shirts left unsold over 7 days. (a) Which day had the most sales? (b) What percentage were sold in the first 5 days? (c) On Day 3, the shop collected $192 after 20% discount. What was the original price per T-shirt?",
     "answer": "(a) Day 4 (b) 83% (c) $15", "marks": 6, "diagram": "linegraph_reverse.png"},
    
    {"num": 34, "id": "DI034", "type": "DI", "pathway": "DI1-Line Graph", "diff": "M",
     "text": "Find the total number of T-shirts sold in the first 3 days and the range of daily sales.",
     "answer": "Total: 60, Range: 32", "marks": 3, "diagram": "linegraph_cumulative.png"},
    
    {"num": 35, "id": "DI035", "type": "DI", "pathway": "DI2-Bar Graph", "diff": "M",
     "text": "The bar chart shows books read by 5 students. (a) Who read the most books? (b) Calculate the average. (c) What percentage of total books were read by Ali and Ben together?",
     "answer": "(a) Cal (b) 10.2 (c) 39.2%", "marks": 5},
    
    {"num": 36, "id": "DI036", "type": "DI", "pathway": "DI2-Bar Graph", "diff": "E",
     "text": "Find the total number of books read and the range of the data.",
     "answer": "Total: 51, Range: 9", "marks": 2},
    
    {"num": 37, "id": "DI037", "type": "DI", "pathway": "DI3-Pie Chart", "diff": "M",
     "text": "The pie chart shows Isabelle's spending. Transport is 24% and equals 2/5 of food spending. Savings is 25% of transport. (a) What percentage is food? (b) If savings is $90, what is total spending?",
     "answer": "(a) 60% (b) $1500", "marks": 5},
    
    {"num": 38, "id": "DI038", "type": "DI", "pathway": "DI3-Pie Chart", "diff": "H",
     "text": "The sector for apples is 72° and represents 60 apples. Find the total number of fruits.",
     "answer": "300 fruits", "marks": 3},
    
    {"num": 39, "id": "DI039", "type": "DI", "pathway": "DI1-Line Graph", "diff": "M",
     "text": "Calculate the average temperature for the week and identify days above average.",
     "answer": "Avg: 30.4°C", "marks": 3, "diagram": "linegraph_rate.png"},
    
    {"num": 40, "id": "DI040", "type": "DI", "pathway": "DI1-Line Graph", "diff": "H",
     "text": "Using the temperature data, estimate the temperature on Tuesday afternoon and explain your reasoning.",
     "answer": "~30°C with explanation", "marks": 3},
]

def wrap_text(c, text, x, y, max_width, font="Helvetica", size=9):
    """Wrap text to fit within max_width."""
    c.setFont(font, size)
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        test = current_line + " " + word if current_line else word
        if c.stringWidth(test, font, size) <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    for line in lines:
        c.drawString(x, y, line)
        y -= 0.14 * inch
    
    return y

def generate_pdf():
    output_path = OUTPUT_DIR / "ATOM-SG_Exam_Quality_Baseline_40_Questions.pdf"
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    lm = 0.5 * inch
    rm = 0.5 * inch
    tm = 0.5 * inch
    bm = 0.5 * inch
    cw = width - lm - rm
    
    # Header
    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(width/2, height - tm, "ATOM-SG Exam-Quality Baseline Test")
    c.setFont("Helvetica", 10)
    c.drawCentredString(width/2, height - tm - 0.2*inch, "P6 Mathematics | 40 Questions | 1 Hour | No Calculator")
    
    c.setFont("Helvetica-Bold", 9)
    y = height - tm - 0.55*inch
    c.drawString(lm, y, "Name: _________________________________  Class: _______  Date: ___________")
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 8)
    c.drawString(lm, y, "Instructions: Show all working. Exam-quality problems with professional diagrams.")
    y -= 0.18*inch
    
    for prob in PROBLEMS:
        has_diagram = prob.get("diagram") is not None
        space_needed = 1.0 * inch
        if has_diagram:
            space_needed += 2.5 * inch
        
        if y - space_needed < bm:
            c.showPage()
            y = height - tm
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(width/2, y, "Baseline Test - Continued")
            y -= 0.25*inch
        
        c.setFont("Helvetica-Bold", 8)
        c.drawString(lm, y, f"Q{prob['num']:2d}. [{prob['diff']}] [{prob['type']}] {prob['pathway'][:30]}")
        y -= 0.16*inch
        
        c.setFont("Helvetica", 9)
        y = wrap_text(c, prob['text'], lm + 0.05*inch, y, cw - 0.1*inch)
        
        # Embed diagram
        if has_diagram:
            y -= 0.1*inch
            diag_path = OUTPUT_DIR / prob["diagram"]
            if diag_path.exists():
                img_width = 3.5 * inch
                img_height = 2.2 * inch
                x_pos = lm + (cw - img_width) / 2
                c.drawImage(str(diag_path), x_pos, y - img_height, width=img_width, height=img_height)
                y -= img_height + 0.1*inch
        
        y -= 0.06*inch
        c.setFont("Helvetica-Bold", 7)
        c.drawString(lm + 0.05*inch, y, "Working:")
        y -= 0.12*inch
        wh = 0.5 * inch
        c.rect(lm + 0.05*inch, y - wh, cw - 0.15*inch, wh)
        y -= wh + 0.1*inch
        
        c.setFont("Helvetica-Bold", 8)
        c.drawString(lm + 0.05*inch, y, f"Answer: _________________________ ({prob['marks']} marks)")
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
        c.drawString(lm, y, f"Q{prob['num']:2d}: {prob['answer'][:50]}")
        y -= 0.13*inch
        if y < bm:
            c.showPage()
            y = height - tm
    
    c.save()
    return output_path

if __name__ == "__main__":
    print(f"{'='*60}")
    print("Generating Exam-Quality Baseline Test")
    print(f"{'='*60}")
    print(f"\nTotal Questions: 40")
    print(f"  - 20 Word Problems (Cross-Thread)")
    print(f"  - 12 Geometry (G5-G8)")
    print(f"  - 8 Data Interpretation (DI1-DI3)")
    print(f"\nTotal Marks: {sum(p['marks'] for p in PROBLEMS)}")
    
    pdf_path = generate_pdf()
    
    print(f"\n{'='*60}")
    print("✅ Generation Complete!")
    print(f"{'='*60}")
    print(f"PDF: {pdf_path}")
    print(f"Diagrams: {OUTPUT_DIR}")
