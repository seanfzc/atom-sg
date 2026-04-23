#!/usr/bin/env python3
"""
Generate FINAL baseline test v5.0 with ALL fixed diagrams
Uses _fixed.png versions where available
"""

import sys
sys.path.insert(0, '/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/05-Backend')

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v5"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Diagram mapping - use fixed versions where available
DIAGRAM_MAP = {
    # Fixed diagrams
    "Q21": "Q21_fixed.png",
    "G001": "G001_fixed.png",
    "G011": "G011_fixed.png",
    "G017": "G017_fixed.png",
    # Original diagrams (not yet fixed)
    "G002": "G002.png",
    "G003": "G003.png",
    "G004": "G004.png",
    "G005": "G005.png",
    "G009": "G009.png",
    "G010": "G010.png",
    "G012": "G012.png",
    "G015": "G015.png",
    "G018": "G018.png",
    "G019": "G019.png",
    "G020": "G020.png",
    "G021": "G021.png",
    "G022": "G022.png",
    "G023": "G023.png",
    "G024": "G024.png",
    "G025": "G025.png",
    "Q22": "G001_fixed.png",  # Grid construction uses fixed protractor
    "Q23": "G020.png",
    "Q24": "G004.png",
    "Q25": "G011_fixed.png",  # Uses fixed L-shape
    "Q26": "G001_fixed.png",
    "Q27": "G003.png",
    "Q28": "G004.png",
    "Q29": "G005.png",
    "Q30": "G011_fixed.png",
    "Q31": "G012.png",
    "Q32": "G017_fixed.png",  # Uses fixed cuboid
    "Q33": "Q33_line_graph.png",
    "Q34": "Q34_line_graph.png",
    "Q35": "Q35_bar_chart.png",
    "Q36": "Q36_bar_chart.png",
    "Q37": "Q37_pie_chart.png",
    "Q38": "Q38_pie_chart.png",
    "Q39": "Q39_line_graph.png",
    "Q40": "Q40_line_graph.png",
}

# All 40 questions
PROBLEMS = [
    # WORD PROBLEMS (20)
    {"num": 1, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Mrs. Lee received $240 as a birthday gift from her family. At the department store, she spent 2/5 of this amount on a designer handbag. From the remainder, she then spent 1/3 on a pair of shoes, leaving her with just enough for dinner. If she had $72 left after all her purchases, how much money did she have at first before receiving the gift?",
     "answer": "$480", "marks": 4},
    
    {"num": 2, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A rectangular water tank at a factory was filled to 5/6 of its capacity at the start of the day. During the morning shift, workers used 15 litres of water for cleaning, causing the water level to drop to exactly 2/3 of the tank's capacity. Assuming the tank was completely full at the beginning of the week, what is the total capacity of the tank in litres?",
     "answer": "90 litres", "marks": 3},
    
    {"num": 3, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "In a sports equipment room, the ratio of red balls to blue balls was 3:5 at the beginning of the term. After 12 red balls were removed for a tournament and not returned, the new ratio of red to blue balls became 1:3. How many red balls were there in the equipment room at the beginning of the term?",
     "answer": "27 red balls", "marks": 4},
    
    {"num": 4, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Alan and Ben have been friends since primary school. Currently, their ages are in the ratio 4:7. Six years from now, when Alan enters secondary school, the ratio of their ages will be 2:3. How old is Alan now?",
     "answer": "24 years old", "marks": 4},
    
    {"num": 5, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A stationery shop received a shipment of 240 pens on Monday morning. That day, they sold 2/5 of the pens to a school. On Tuesday, they sold 1/3 of what remained to walk-in customers. On Wednesday, they sold 1/2 of the new remainder to an office. How many pens were left unsold at the end of Wednesday?",
     "answer": "48 pens", "marks": 4},
    
    {"num": 6, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Alice and Betty had $280 in their shared savings jar. One Saturday, Alice spent 1/3 of her personal share on a book, while Betty spent $40 on art supplies. Surprisingly, they discovered they had equal amounts left in their individual portions. How much did Alice originally contribute to the savings jar?",
     "answer": "$144", "marks": 4},
    
    {"num": 7, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A baker prepared 360 cupcakes for a weekend market. In the morning session, he sold 1/4 of the cupcakes to early customers. In the afternoon, he sold 2/3 of the remaining cupcakes, which was more than he expected. How many cupcakes did the baker have left to take home at the end of the day?",
     "answer": "90 cupcakes", "marks": 3},
    
    {"num": 8, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Three cousins collect stamps. John has 3/5 as many stamps as his older sister Mary. Mary, in turn, has 5/6 as many stamps as their eldest cousin Tom. If Tom has proudly collected 72 stamps from different countries, how many stamps does John have in his collection?",
     "answer": "36 stamps", "marks": 3},
    
    {"num": 9, "type": "WP", "pathway": "Part-Whole", "diff": "M",
     "text": "In Primary 6A, the ratio of boys to girls is 5:3. When the teacher took attendance last Monday, she counted exactly 40 students present in class. How many boys are there in Primary 6A?",
     "answer": "25 boys", "marks": 2},
    
    {"num": 10, "type": "WP", "pathway": "Before-After", "diff": "M",
     "text": "A public bus started its route with 60 passengers on board. At the first bus stop, 15 passengers alighted to go to the market. At the second stop, 8 more passengers got off at the school. How many passengers remained on the bus after the second stop?",
     "answer": "37 passengers", "marks": 2},
    
    {"num": 11, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Ali and Ben had $280 between them in their piggy banks. After Ali kindly gave 1/4 of his savings to Ben to help him buy a toy, they were surprised to find they had exactly the same amount. How much did Ali have in his piggy bank at first?",
     "answer": "$160", "marks": 4},
    
    {"num": 12, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A water tank was completely full at the start of the day. During the morning, 3/7 of the water was used for cleaning. In the afternoon, 2/5 of the remaining water was used for gardening. At the end of the day, exactly 48 litres were left in the tank. How much water was in the tank at the beginning of the day?",
     "answer": "140 litres", "marks": 4},
    
    {"num": 13, "type": "WP", "pathway": "Part-Whole", "diff": "M",
     "text": "There are 80 students registered for the school camp. When the coordinator checked the list, she noticed that 3/8 of the participants are girls. How many boys are going on the camp?",
     "answer": "50 boys", "marks": 2},
    
    {"num": 14, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A fruit seller had 240 apples in his stall at the morning market. He sold 3/4 of them to Shop A before noon. Later in the afternoon, he sold 1/2 of the remaining apples to Shop B. How many apples did the seller have left at the end of the day?",
     "answer": "30 apples", "marks": 3},
    
    {"num": 15, "type": "WP", "pathway": "Part-Whole", "diff": "M",
     "text": "Jenny and Kelly have been collecting stickers together. In total, they have 84 stickers in their album. Jenny has 16 more stickers than Kelly. How many stickers does Kelly have?",
     "answer": "34 stickers", "marks": 2},
    
    {"num": 16, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "A designer bag's price increased by 20% due to high demand. During a sale two weeks later, the shop offered a 15% discount on the new price. If a customer paid $204 for the bag during the sale, what was the original price before the increase?",
     "answer": "$200", "marks": 4},
    
    {"num": 17, "type": "WP", "pathway": "Part-Whole", "diff": "H",
     "text": "At a fruit stall, the ratio of apples to oranges to pears is 2:3:5. One morning, the stall owner counted and found that the oranges and pears together total 120 fruits. How many apples are on display?",
     "answer": "30 apples", "marks": 3},
    
    {"num": 18, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "Mrs. Tan went grocery shopping with some money in her purse. She spent $25 on fresh vegetables. After that, she deposited 1/4 of what remained into her savings. If she had $45 left in her purse for other expenses, how much did she start with?",
     "answer": "$85", "marks": 3},
    
    {"num": 19, "type": "WP", "pathway": "Part-Whole", "diff": "M",
     "text": "In the school choir, the ratio of boys to girls is 5:3. The conductor noticed there are 24 more boys than girls in the group. How many children are in the choir altogether?",
     "answer": "96 children", "marks": 3},
    
    {"num": 20, "type": "WP", "pathway": "Cross-Thread", "diff": "H",
     "text": "The school library had 450 books on its shelves at the start of the term. During a donation drive, they received 120 new books from parents. Later, they donated 1/5 of their total collection to a sister school. How many books remained in the library?",
     "answer": "456 books", "marks": 3},
    
    # GEOMETRY (12)
    {"num": 21, "id": "Q21", "type": "G", "pathway": "G5-Composite Overlap", "diff": "H",
     "text": "Figure OABCD is formed by overlapping 2 similar quarter circles OAC and OBD. OA = OB = OC = OD = 10 cm. The area of the shaded part OBC is 30 cm² and the perimeter of the shaded part OBC is 26 cm. (a) Find the area of figure OABCD. (b) Find the perimeter of figure OABCD. Take π = 3.14",
     "answer": "(a) 127 cm² (b) 30.5 cm", "marks": 5},
    
    {"num": 22, "id": "Q22", "type": "G", "pathway": "G6-Grid Construction", "diff": "H",
     "text": "The diagram shows triangle ABC drawn on a 1cm grid. (a) Using a protractor, measure angle ACB. (b) Complete trapezium BCDE where BC is parallel to DE, AB = BE, and DE is twice as long as BC.",
     "answer": "(a) 36° (b) See diagram", "marks": 4},
    
    {"num": 23, "id": "Q23", "type": "G", "pathway": "G7-3D Visualization", "diff": "H",
     "text": "The solid shown is made up of 8 identical cubes arranged in an L-shape. (a) Draw the front view of the solid on the grid provided. (b) What is the maximum number of additional cubes that can be added to the solid without changing the front and side views?",
     "answer": "(a) See diagram (b) 8 cubes", "marks": 4},
    
    {"num": 24, "id": "Q24", "type": "G", "pathway": "G8-Angle Chasing", "diff": "H",
     "text": "In the diagram, ABCD is a rhombus and ADEF is a trapezium with AF parallel to DE. Given angle DFE = 21°, angle BCD = 108°, and angle DAB = 33°, find the values of angles x and y marked in the diagram.",
     "answer": "x = 18°, y = 126°", "marks": 5},
    
    {"num": 25, "id": "Q25", "type": "G", "pathway": "G5-Composite Overlap", "diff": "M",
     "text": "The diagram shows five squares drawn inside a rectangle. Square X has side 4 cm. Find (a) the side length of square Y, (b) the length of the rectangle, (c) how many 2cm cubes can be made from all five squares combined.",
     "answer": "(a) 2 cm (b) 13 cm (c) 38 cubes", "marks": 5},
    
    {"num": 26, "id": "Q26", "type": "G", "pathway": "G1-Angle Reasoning", "diff": "E",
     "text": "Use the protractor shown in the diagram to measure angles A, B, and C. Write your answers in degrees.",
     "answer": "A = 45°, B = 120°, C = 90°", "marks": 3},
    
    {"num": 27, "id": "Q27", "type": "G", "pathway": "G8-Angle Chasing", "diff": "M",
     "text": "In the diagram, three angles meet at point O. Two of the angles measure 120° and 85°. Find the measure of the third angle marked with a question mark.",
     "answer": "155°", "marks": 2},
    
    {"num": 28, "id": "Q28", "type": "G", "pathway": "G1-Angle Reasoning", "diff": "M",
     "text": "Two straight lines intersect at point O as shown. If one of the angles formed is 50°, find the measures of angles a, b, and c marked in the diagram.",
     "answer": "a = 50°, b = 130°, c = 130°", "marks": 2},
    
    {"num": 29, "id": "Q29", "type": "G", "pathway": "G2-Area", "diff": "M",
     "text": "In triangle ABC shown, angle A measures 55° and angle B measures 65°. Find the measure of angle C.",
     "answer": "60°", "marks": 2},
    
    {"num": 30, "id": "Q30", "type": "G", "pathway": "G2-Composite", "diff": "M",
     "text": "The figure shows an L-shaped figure made by combining two rectangles. Find (a) its total area, (b) its perimeter.",
     "answer": "(a) 64 cm² (b) 34 cm", "marks": 3},
    
    {"num": 31, "id": "Q31", "type": "G", "pathway": "G2-Area", "diff": "M",
     "text": "A rectangular metal sheet measures 12 cm by 8 cm. A smaller rectangular piece measuring 4 cm by 3 cm is cut out from one corner as shown. Find the area of the remaining metal sheet.",
     "answer": "84 cm²", "marks": 3},
    
    {"num": 32, "id": "Q32", "type": "G", "pathway": "G3-Volume", "diff": "M",
     "text": "The diagram shows a cuboid with length 6 cm, breadth 4 cm, and height 3 cm. Find its volume.",
     "answer": "72 cm³", "marks": 2},
    
    # DATA INTERPRETATION (8)
    {"num": 33, "id": "Q33", "type": "DI", "pathway": "DI1-Line Graph", "diff": "H",
     "text": "The line graph shows the number of T-shirts remaining unsold at a shop over one week. (a) Which day had the most sales? (b) What percentage of the original stock were sold in the first 5 days? (c) On Day 3, the shop collected $192 after giving a 20% discount. What was the original price per T-shirt?",
     "answer": "(a) Day 4 (b) 83% (c) $15", "marks": 6},
    
    {"num": 34, "id": "Q34", "type": "DI", "pathway": "DI1-Line Graph", "diff": "M",
     "text": "The line graph shows daily temperature readings over one week. (a) Find the range of temperatures. (b) Calculate the average temperature for the week. (c) On which day was the temperature 5°C above the average?",
     "answer": "(a) 6°C (b) 30°C (c) Wednesday", "marks": 5},
    
    {"num": 35, "id": "Q35", "type": "DI", "pathway": "DI2-Bar Graph", "diff": "M",
     "text": "The bar chart shows the number of books read by 5 students during the holidays. (a) Which student read the most books? (b) Calculate the average number of books read per student. (c) What percentage of the total books were read by Ali and Ben together?",
     "answer": "(a) Cal (b) 10.2 (c) 39.2%", "marks": 5},
    
    {"num": 36, "id": "Q36", "type": "DI", "pathway": "DI2-Bar Graph", "diff": "E",
     "text": "The bar chart shows test scores for 5 subjects. (a) Which subject had the highest score? (b) Calculate the average score across all subjects. (c) How many more marks were scored in Math compared to English?",
     "answer": "(a) Art (b) 78.6 (c) 17", "marks": 3},
    
    {"num": 37, "id": "Q37", "type": "DI", "pathway": "DI3-Pie Chart", "diff": "M",
     "text": "The pie chart shows how Isabelle spent her monthly allowance. She spent 24% on transport, which was exactly 2/5 of what she spent on food. Her savings was 25% of her transport spending. (a) What percentage was spent on food? (b) If she saved $90, what was her total monthly allowance?",
     "answer": "(a) 60% (b) $1500", "marks": 5},
    
    {"num": 38, "id": "Q38", "type": "DI", "pathway": "DI3-Pie Chart", "diff": "H",
     "text": "The pie chart shows the distribution of fruits in a basket. The sector representing apples measures 72° and corresponds to exactly 60 apples. (a) How many oranges are there? (b) What is the total number of fruits? (c) What fraction of the fruits are bananas?",
     "answer": "(a) 105 (b) 300 (c) 1/4", "marks": 5},
    
    {"num": 39, "id": "Q39", "type": "DI", "pathway": "DI1-Line Graph", "diff": "M",
     "text": "The line graph shows website visitor numbers by hour. (a) At what time was traffic highest? (b) Calculate the total visitors from 8am to 12pm. (c) What was the percentage increase in visitors from 4pm to 6pm?",
     "answer": "(a) 6pm (b) 345 (c) 110%", "marks": 5},
    
    {"num": 40, "id": "Q40", "type": "DI", "pathway": "DI1-Line Graph", "diff": "H",
     "text": "The line graph shows plant growth over 6 weeks. (a) In which week did the plant grow the most? (b) Calculate the average weekly growth. (c) If growth continues at the same rate, what will be the height at Week 8?",
     "answer": "(a) Week 5 (b) 4.6 cm/week (c) 37.2 cm", "marks": 5},
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
    output_path = OUTPUT_DIR / "ATOM-SG_Baseline_Test_40_Questions_v5.pdf"
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    lm = 0.5 * inch
    rm = 0.5 * inch
    tm = 0.5 * inch
    bm = 0.5 * inch
    cw = width - lm - rm
    
    # Header
    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(width/2, height - tm, "ATOM-SG Baseline Test v5.0")
    c.setFont("Helvetica", 10)
    c.drawCentredString(width/2, height - tm - 0.2*inch, "P6 Mathematics | 40 Questions | 1 Hour | No Calculator | VRS-Compliant")
    
    c.setFont("Helvetica-Bold", 9)
    y = height - tm - 0.55*inch
    c.drawString(lm, y, "Name: _________________________________  Class: _______  Date: ___________")
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 8)
    c.drawString(lm, y, "Instructions: Show all working. All diagrams are VRS-compliant. Fixed diagrams: Q21, G001, G011, G017.")
    y -= 0.18*inch
    
    for prob in PROBLEMS:
        has_diagram = prob.get("id") in DIAGRAM_MAP
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
        c.drawString(lm, y, f"Q{prob['num']:2d}. [{prob['diff']}] [{prob['type']}] {prob['pathway'][:35]}")
        y -= 0.16*inch
        
        c.setFont("Helvetica", 9)
        y = wrap_text(c, prob['text'], lm + 0.05*inch, y, cw - 0.1*inch)
        
        # Embed diagram
        if has_diagram:
            y -= 0.1*inch
            diagram_file = DIAGRAM_MAP[prob["id"]]
            
            # Check both original and v3 directory
            possible_paths = [
                OUTPUT_DIR / diagram_file,
                Path("/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/05-Backend/artifacts/renders/exam-quality-baseline-v3") / diagram_file,
            ]
            
            diag_path = None
            for p in possible_paths:
                if p.exists():
                    diag_path = p
                    break
            
            if diag_path:
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
        c.drawString(lm, y, f"Q{prob['num']:2d}: {prob['answer'][:55]}")
        y -= 0.13*inch
        if y < bm:
            c.showPage()
            y = height - tm
    
    c.save()
    return output_path

if __name__ == "__main__":
    print(f"\n{'='*60}")
    print("Generating Baseline Test v5.0 with Fixed Diagrams")
    print(f"{'='*60}")
    
    pdf_path = generate_pdf()
    
    print(f"\n{'='*60}")
    print("✅ Generation Complete!")
    print(f"{'='*60}")
    print(f"PDF: {pdf_path}")
    print(f"Total Questions: 40")
    print(f"Total Marks: {sum(p['marks'] for p in PROBLEMS)}")
    print(f"\nFixed diagrams included:")
    print("  - Q21: Radius label outside")
    print("  - G001: Degree labels, spaced arcs")
    print("  - G011: All dimensions including internal")
    print("  - G017: Horizontal labels, dashed edges")
