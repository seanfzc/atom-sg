#!/usr/bin/env python3
"""
Generate complete 40-question baseline test PDF for ATOM-SG Pilot.
20 Word Problems + 12 Geometry + 8 Data Interpretation = 40 questions
Version 2: Inline problem definitions to avoid YAML parsing issues
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime

# Complete 40-question baseline test
BASELINE_PROBLEMS = [
    # WORD PROBLEMS (20) - Before-After Change
    {"id": "WP001", "type": "WP", "pathway": "Before-After Change", "diff": "E", 
     "question": "A shop had 240 pens. On Monday, they sold 2/5 of the pens. On Tuesday, they sold 1/3 of the remaining pens. How many pens were left on Wednesday?", 
     "answer": "96 pens"},
    {"id": "WP002", "type": "WP", "pathway": "Before-After Change", "diff": "M", 
     "question": "Sarah spent 3/8 of her money on a book and 2/5 of the remainder on a pen. If she had $30 left, how much did she have at first?", 
     "answer": "$80"},
    {"id": "WP007", "type": "WP", "pathway": "Before-After Change", "diff": "M", 
     "question": "A tank was full of water. After 3/7 of the water was poured out, then 2/5 of the remaining water was used, 48 litres were left. How much water was in the tank at first?", 
     "answer": "140 litres"},
    {"id": "WP009", "type": "WP", "pathway": "Before-After Change", "diff": "E", 
     "question": "A bus had 60 passengers. At the first stop, 15 passengers got off. At the second stop, 8 passengers got off. How many passengers were left on the bus?", 
     "answer": "37 passengers"},
    {"id": "WP012", "type": "WP", "pathway": "Before-After Change", "diff": "M", 
     "question": "A library had 450 books. They received 120 new books on Monday. On Tuesday, they donated 1/5 of their total books to a school. How many books did they have left?", 
     "answer": "456 books"},
    {"id": "WP019", "type": "WP", "pathway": "Before-After Change", "diff": "M", 
     "question": "Mrs. Tan had some money in her purse. She spent $25 on groceries and then deposited 1/4 of the remainder into her bank account. If she had $45 left, how much did she have at first?", 
     "answer": "$85"},
    
    # WORD PROBLEMS - Part-Whole with Comparison
    {"id": "WP003", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "E", 
     "question": "Ali has $120. Ben has 3/4 as much as Ali. How much money do they have altogether?", 
     "answer": "$210"},
    {"id": "WP004", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "M", 
     "question": "The ratio of boys to girls in a class is 5:3. If there are 40 students altogether, how many boys are there?", 
     "answer": "25 boys"},
    {"id": "WP008", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "M", 
     "question": "John has 3/5 as many stamps as Mary. Mary has 5/6 as many stamps as Tom. If Tom has 72 stamps, how many stamps does John have?", 
     "answer": "36 stamps"},
    {"id": "WP013", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "E", 
     "question": "There are 80 students in a hall. 3/8 of them are girls. How many boys are there?", 
     "answer": "50 boys"},
    {"id": "WP015", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "M", 
     "question": "Jenny and Kelly have 84 stickers altogether. Jenny has 16 more stickers than Kelly. How many stickers does Kelly have?", 
     "answer": "34 stickers"},
    {"id": "WP017", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "H", 
     "question": "The ratio of apples to oranges to pears is 2:3:5. If there are 120 oranges and pears altogether, how many apples are there?", 
     "answer": "30 apples"},
    {"id": "WP020", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "M", 
     "question": "The ratio of boys to girls in a club is 5:3. There are 24 more boys than girls. How many children are in the club?", 
     "answer": "96 children"},
    
    # WORD PROBLEMS - Cross-Thread Collision
    {"id": "WP005", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "M", 
     "question": "A baker made 360 cupcakes. He sold 1/4 of them in the morning and 2/3 of the remainder in the afternoon. How many cupcakes did he have left?", 
     "answer": "90 cupcakes"},
    {"id": "WP006", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "H", 
     "question": "Alice and Betty had $280 altogether. After Alice spent 1/3 of her money and Betty spent $40, they had the same amount left. How much did Alice have at first?", 
     "answer": "$144"},
    {"id": "WP010", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "H", 
     "question": "The ratio of red balls to blue balls in a bag was 3:5. After removing 12 red balls, the ratio became 1:3. How many red balls were there at first?", 
     "answer": "27 red balls"},
    {"id": "WP011", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "H", 
     "question": "The ratio of Alan's age to Ben's age is 4:7. In 6 years, the ratio will be 2:3. How old is Alan now?", 
     "answer": "24 years old"},
    {"id": "WP014", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "M", 
     "question": "A fruit seller had 240 apples. He sold 3/4 of them to Shop A and 1/2 of the remainder to Shop B. How many apples did he have left?", 
     "answer": "30 apples"},
    {"id": "WP016", "type": "WP", "pathway": "Before-After Change", "diff": "H", 
     "question": "A shop increased the price of a bag by 20%. During a sale, they offered a 15% discount on the new price. If the final price was $204, what was the original price?", 
     "answer": "$200"},
    {"id": "WP018", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "H", 
     "question": "A tank was 5/6 full of water. After 15 litres were poured out, it was 2/3 full. What is the capacity of the tank?", 
     "answer": "90 litres"},
    
    # GEOMETRY (12)
    {"id": "G001", "type": "G", "pathway": "Geometry - Angle Measurement", "diff": "E", 
     "question": "Measure the angles A, B, and C in the diagram using a protractor.", 
     "answer": "See diagram"},
    {"id": "G002", "type": "G", "pathway": "Geometry - Angle Properties", "diff": "E", 
     "question": "Two angles on a straight line are given. If one angle is 75 degrees, find the other angle.", 
     "answer": "105 degrees"},
    {"id": "G005", "type": "G", "pathway": "Geometry - Triangle Angles", "diff": "M", 
     "question": "In triangle ABC, angle A = 50 degrees and angle B = 70 degrees. Find angle C.", 
     "answer": "60 degrees"},
    {"id": "G007", "type": "G", "pathway": "Geometry - Combined Angles", "diff": "H", 
     "question": "Angle A and Angle B are on a straight line. Angle B and Angle C are complementary (sum to 90 degrees). If Angle A = 110 degrees, find Angle C.", 
     "answer": "20 degrees"},
    {"id": "G009", "type": "G", "pathway": "Geometry - Perimeter", "diff": "E", 
     "question": "Find the perimeter of a rectangle with length 8 cm and breadth 5 cm.", 
     "answer": "26 cm"},
    {"id": "G010", "type": "G", "pathway": "Geometry - Composite Perimeter", "diff": "M", 
     "question": "A rectilinear figure consists of two rectangles joined together. Find its perimeter, given some side lengths.", 
     "answer": "See diagram"},
    {"id": "G011", "type": "G", "pathway": "Geometry - Composite Area", "diff": "M", 
     "question": "Find the area of an L-shape figure formed by two rectangles.", 
     "answer": "See diagram"},
    {"id": "G014", "type": "G", "pathway": "Geometry - Unit Conversion", "diff": "M", 
     "question": "Convert 2.5 square metres to square centimetres.", 
     "answer": "25,000 cm squared"},
    {"id": "G017", "type": "G", "pathway": "Geometry - Volume", "diff": "E", 
     "question": "Find the volume of a cuboid with length 6 cm, breadth 4 cm, height 3 cm.", 
     "answer": "72 cubic cm"},
    {"id": "G019", "type": "G", "pathway": "Geometry - 3D Nets", "diff": "M", 
     "question": "Which of the following nets can be folded to form a cube?", 
     "answer": "See diagram"},
    {"id": "G021", "type": "G", "pathway": "Geometry - Triangle Classification", "diff": "E", 
     "question": "Classify the triangle with side lengths 5 cm, 5 cm, 5 cm.", 
     "answer": "Equilateral"},
    {"id": "G024", "type": "G", "pathway": "Geometry - Circle", "diff": "M", 
     "question": "A circle has radius 7 cm. Find its circumference (take pi = 22/7).", 
     "answer": "44 cm"},
    
    # DATA INTERPRETATION (8)
    {"id": "DI021", "type": "DI", "pathway": "Data Interpretation - Bar Graph", "diff": "E", 
     "question": "The bar graph shows the number of books read by 5 students. Who read the most books?", 
     "answer": "See graph"},
    {"id": "DI022", "type": "DI", "pathway": "Data Interpretation - Bar Graph", "diff": "E", 
     "question": "Calculate the total number of books read by all students and find the average.", 
     "answer": "See graph"},
    {"id": "DI023", "type": "DI", "pathway": "Data Interpretation - Bar Graph", "diff": "M", 
     "question": "Find the mode and range of the number of books read.", 
     "answer": "See graph"},
    {"id": "DI024", "type": "DI", "pathway": "Data Interpretation - Line Graph", "diff": "M", 
     "question": "The line graph shows temperature over a week. Describe the trend and identify the hottest day.", 
     "answer": "See graph"},
    {"id": "DI025", "type": "DI", "pathway": "Data Interpretation - Line Graph", "diff": "M", 
     "question": "Estimate the temperature on Wednesday afternoon using interpolation.", 
     "answer": "See graph"},
    {"id": "DI026", "type": "DI", "pathway": "Data Interpretation - Line Graph", "diff": "H", 
     "question": "Compare the sales trends of Product A and Product B over 6 months. Which product showed more consistent growth?", 
     "answer": "See graph"},
    {"id": "DI027", "type": "DI", "pathway": "Data Interpretation - Pie Chart", "diff": "M", 
     "question": "A pie chart shows a sector with angle 90 degrees. What fraction of the whole does this sector represent?", 
     "answer": "1/4"},
    {"id": "DI028", "type": "DI", "pathway": "Data Interpretation - Pie Chart", "diff": "H", 
     "question": "Given that the sector representing apples has angle 72 degrees and there are 60 apples, find the total number of fruits.", 
     "answer": "300 fruits"},
]

def draw_wrapped_text(c, text, x, y, max_width, line_height=0.18*inch, font_name="Helvetica", font_size=10):
    """Draw text with word wrapping."""
    c.setFont(font_name, font_size)
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        if c.stringWidth(test_line, font_name, font_size) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    for line in lines:
        c.drawString(x, y, line)
        y -= line_height
    return y

def generate_complete_baseline(output_path: Path) -> None:
    """Generate complete 40-question baseline test."""
    all_problems = BASELINE_PROBLEMS
    
    print(f"Generating baseline test with {len(all_problems)} questions")
    
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    
    left_margin = 0.6 * inch
    right_margin = 0.6 * inch
    top_margin = 0.6 * inch
    bottom_margin = 0.6 * inch
    content_width = width - left_margin - right_margin
    
    def draw_header():
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width/2, height - top_margin, "ATOM-SG Pilot - Week 1 Baseline Test")
        
        c.setFont("Helvetica", 11)
        c.drawCentredString(width/2, height - top_margin - 0.25*inch, 
                           "P6 Mathematics - Recognition-First Assessment")
        
        c.setFont("Helvetica", 10)
        c.drawCentredString(width/2, height - top_margin - 0.45*inch,
                           "40 Questions | 50 Minutes | No Calculator")
        
        # Student info
        c.setFont("Helvetica-Bold", 10)
        y = height - top_margin - 0.8*inch
        c.drawString(left_margin, y, "Name: _________________________________  Class: _______  Date: ___________")
        
        # Instructions
        y -= 0.35*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(left_margin, y, "Instructions:")
        c.setFont("Helvetica", 8)
        instructions = [
            "1. This test has 40 questions: 20 Word Problems, 12 Geometry, 8 Data Interpretation.",
            "2. You have 50 minutes. Work quickly but carefully.",
            "3. Show all working in the spaces provided.",
            "4. Write final answers in the boxes.",
            "5. Calculators are NOT allowed.",
            "6. Diagrams are NOT drawn to scale unless stated."
        ]
        y -= 0.18*inch
        for inst in instructions:
            c.drawString(left_margin + 0.1*inch, y, inst)
            y -= 0.14*inch
        
        return y - 0.15*inch
    
    def draw_question(c, q_num, problem, y_start):
        y = y_start
        q_type = problem.get('type', 'WP')
        
        # Question header
        c.setFont("Helvetica-Bold", 9)
        diff = problem.get('diff', 'M')
        c.drawString(left_margin, y, f"Q{q_num:2d}. [{diff}] [{q_type}]")
        
        # Pathway (abbreviated)
        pathway = problem.get('pathway', '')
        pathway_short = pathway.replace('Before-After Change', 'BAC').replace('Part-Whole Comparison', 'PWC').replace('Cross-Thread Collision', 'CTC').replace('Data Interpretation', 'DI').replace('Geometry - ', 'G-')[:35]
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColorRGB(0.3, 0.3, 0.3)
        c.drawString(left_margin + 1.1*inch, y, pathway_short)
        c.setFillColorRGB(0, 0, 0)
        
        # Question text
        y -= 0.22*inch
        question = problem.get('question', '')[:280]
        c.setFont("Helvetica", 10)
        y = draw_wrapped_text(c, question, left_margin + 0.05*inch, y, 
                             max_width=content_width - 0.1*inch, 
                             line_height=0.16*inch, font_size=10)
        
        # Visual placeholder for Geometry and Data Interpretation
        if q_type in ['G', 'DI']:
            y -= 0.1*inch
            c.setFont("Helvetica-Oblique", 8)
            c.setFillColorRGB(0.5, 0.5, 0.5)
            if q_type == 'G':
                c.drawString(left_margin + 0.05*inch, y, "[Diagram: See separate diagram sheet]")
            else:
                c.drawString(left_margin + 0.05*inch, y, "[Chart/Graph: See separate diagram sheet]")
            c.setFillColorRGB(0, 0, 0)
            y -= 0.15*inch
        
        # Working space - INCREASED
        y -= 0.12*inch
        c.setFont("Helvetica-Bold", 8)
        c.drawString(left_margin + 0.05*inch, y, "Working:")
        y -= 0.15*inch
        working_height = 0.7*inch  # Increased from 0.4
        c.rect(left_margin + 0.05*inch, y - working_height, content_width - 0.15*inch, working_height)
        
        # Answer box - INCREASED
        y -= working_height + 0.15*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(left_margin + 0.05*inch, y, "Answer: _________________________________")
        
        # Separator with more space
        y -= 0.25*inch
        c.setStrokeColorRGB(0.7, 0.7, 0.7)
        c.line(left_margin, y, width - right_margin, y)
        c.setStrokeColorRGB(0, 0, 0)
        
        return y - 0.1*inch
    
    # Page 1: Header + Q1-12
    y = draw_header()
    for i, prob in enumerate(all_problems[:12], 1):
        y = draw_question(c, i, prob, y)
        if y < bottom_margin + 0.6*inch and i < 12:
            c.showPage()
            y = height - top_margin
    
    # Page 2: Q13-26
    c.showPage()
    y = height - top_margin
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(width/2, y, "Baseline Test - Page 2 (Questions 13-26)")
    y -= 0.3*inch
    
    for i, prob in enumerate(all_problems[12:26], 13):
        y = draw_question(c, i, prob, y)
        if y < bottom_margin + 0.6*inch and i < 26:
            c.showPage()
            y = height - top_margin
    
    # Page 3: Q27-40
    c.showPage()
    y = height - top_margin
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(width/2, y, "Baseline Test - Page 3 (Questions 27-40)")
    y -= 0.3*inch
    
    for i, prob in enumerate(all_problems[26:], 27):
        y = draw_question(c, i, prob, y)
        if y < bottom_margin + 0.6*inch and i < 40:
            c.showPage()
            y = height - top_margin
    
    # Diagram Sheet Page for Geometry and Data Interpretation
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - top_margin, "Diagram Sheet - Geometry & Data Interpretation")
    
    c.setFont("Helvetica", 9)
    c.drawCentredString(width/2, height - top_margin - 0.25*inch, 
                       "This sheet contains diagrams for Geometry (G) and Data Interpretation (DI) questions")
    
    y = height - top_margin - 0.6*inch
    
    # Geometry Diagrams
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin, y, "GEOMETRY DIAGRAMS")
    y -= 0.3*inch
    
    geo_questions = [p for p in all_problems if p['type'] == 'G']
    for i, prob in enumerate(geo_questions, 1):
        q_num = all_problems.index(prob) + 1
        c.setFont("Helvetica-Bold", 9)
        c.drawString(left_margin, y, f"Q{q_num}: {prob['id']}")
        y -= 0.18*inch
        
        # Draw diagram placeholder box
        diagram_height = 1.2*inch
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.setFillColorRGB(0.95, 0.95, 0.95)
        c.rect(left_margin + 0.2*inch, y - diagram_height, content_width - 0.4*inch, diagram_height, fill=1)
        c.setFillColorRGB(0, 0, 0)
        c.setStrokeColorRGB(0, 0, 0)
        
        c.setFont("Helvetica-Oblique", 10)
        c.setFillColorRGB(0.4, 0.4, 0.4)
        c.drawCentredString(width/2, y - diagram_height/2, f"[Diagram for {prob['id']} - {prob['pathway'][:30]}...]")
        c.setFillColorRGB(0, 0, 0)
        
        y -= diagram_height + 0.15*inch
        
        if y < bottom_margin + 1.5*inch and i < len(geo_questions):
            c.showPage()
            y = height - top_margin
            c.setFont("Helvetica-Bold", 11)
            c.drawString(left_margin, y, "GEOMETRY DIAGRAMS (continued)")
            y -= 0.3*inch
    
    # Data Interpretation Charts
    c.showPage()
    y = height - top_margin
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin, y, "DATA INTERPRETATION CHARTS")
    y -= 0.3*inch
    
    di_questions = [p for p in all_problems if p['type'] == 'DI']
    for i, prob in enumerate(di_questions, 1):
        q_num = all_problems.index(prob) + 1
        c.setFont("Helvetica-Bold", 9)
        c.drawString(left_margin, y, f"Q{q_num}: {prob['id']}")
        y -= 0.18*inch
        
        # Draw chart placeholder box
        chart_height = 1.5*inch
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.setFillColorRGB(0.95, 0.95, 0.95)
        c.rect(left_margin + 0.2*inch, y - chart_height, content_width - 0.4*inch, chart_height, fill=1)
        c.setFillColorRGB(0, 0, 0)
        c.setStrokeColorRGB(0, 0, 0)
        
        c.setFont("Helvetica-Oblique", 10)
        c.setFillColorRGB(0.4, 0.4, 0.4)
        c.drawCentredString(width/2, y - chart_height/2, f"[Chart/Graph for {prob['id']} - {prob['pathway'][:30]}...]")
        c.setFillColorRGB(0, 0, 0)
        
        y -= chart_height + 0.15*inch
        
        if y < bottom_margin + 1.8*inch and i < len(di_questions):
            c.showPage()
            y = height - top_margin
            c.setFont("Helvetica-Bold", 11)
            c.drawString(left_margin, y, "DATA INTERPRETATION CHARTS (continued)")
            y -= 0.3*inch
    
    # Answer Key Page
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - top_margin, "Answer Key - For Markers Only")
    
    y = height - top_margin - 0.4*inch
    c.setFont("Helvetica-Bold", 8)
    c.drawString(left_margin, y, "Q#  Type  Pathway                    Answer")
    c.line(left_margin, y - 0.06*inch, width - right_margin, y - 0.06*inch)
    
    y -= 0.15*inch
    c.setFont("Courier", 7)
    
    for i, prob in enumerate(all_problems, 1):
        ptype = prob.get('type', '')
        pathway = prob.get('pathway', '')[:20]
        answer = str(prob.get('answer', ''))[:20]
        c.drawString(left_margin, y, f"{i:2d}  {ptype}     {pathway:20s} {answer}")
        y -= 0.11*inch
        
        if y < bottom_margin + 0.3*inch and i < 40:
            c.showPage()
            y = height - top_margin
    
    # Footer
    c.setFont("Helvetica-Oblique", 7)
    c.drawCentredString(width/2, bottom_margin - 0.1*inch,
                       f"ATOM-SG Pilot MVP | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    c.save()
    print(f"\n✅ Generated complete baseline test: {output_path}")
    print(f"   Total questions: {len(all_problems)}")
    print(f"   Word Problems: {sum(1 for p in all_problems if p['type'] == 'WP')}")
    print(f"   Geometry: {sum(1 for p in all_problems if p['type'] == 'G')}")
    print(f"   Data Interpretation: {sum(1 for p in all_problems if p['type'] == 'DI')}")

if __name__ == "__main__":
    output_dir = Path(__file__).parent / "artifacts" / "renders"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "ATOM-SG_Baseline_Test_40_Questions.pdf"
    generate_complete_baseline(output_path)
