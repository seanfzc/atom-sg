#!/usr/bin/env python3
"""
Generate baseline test with TRUE INLINE visuals.
Each question with a diagram has the visual immediately adjacent to the question text.
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

RENDERS_DIR = Path(__file__).parent / "artifacts" / "renders"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)

def create_diagram(filename, diagram_type, **kwargs):
    """Create diagram and save as PNG."""
    fig, ax = plt.subplots(figsize=(2.8, 1.6), dpi=120)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    if diagram_type == "angle_straight":
        # Straight line with two angles
        ax.plot([1, 9], [3, 3], 'k-', linewidth=2.5)
        ax.plot([5, 5], [3, 5.5], 'k-', linewidth=2.5)
        # Arc
        theta = np.linspace(0, np.pi/3, 30)
        ax.plot(5 + 1.2*np.cos(theta), 3 + 1.2*np.sin(theta), 'b-', linewidth=2)
        ax.text(6.2, 3.6, '65°', fontsize=11, color='blue', fontweight='bold')
        ax.text(0.5, 2.4, 'A', fontsize=11, fontweight='bold')
        ax.text(9.2, 2.4, 'B', fontsize=11, fontweight='bold')
        ax.text(4.7, 5.8, 'C', fontsize=11, fontweight='bold')
        ax.text(4.7, 2.4, 'O', fontsize=11, fontweight='bold')
        
    elif diagram_type == "triangle":
        # Triangle
        triangle = plt.Polygon([[2, 1], [8, 1], [5, 5]], fill=False, edgecolor='black', linewidth=2.5)
        ax.add_patch(triangle)
        ax.text(1.5, 0.5, 'A', fontsize=11, fontweight='bold')
        ax.text(8.2, 0.5, 'B', fontsize=11, fontweight='bold')
        ax.text(4.7, 5.5, 'C', fontsize=11, fontweight='bold')
        ax.text(2.8, 1.5, '50°', fontsize=10, color='blue', fontweight='bold')
        ax.text(7, 1.5, '70°', fontsize=10, color='blue', fontweight='bold')
        
    elif diagram_type == "rectangle":
        # Rectangle with dimensions
        rect = plt.Rectangle((2, 1.5), 6, 3, fill=False, edgecolor='black', linewidth=2.5)
        ax.add_patch(rect)
        ax.text(5, 0.8, '8 cm', fontsize=11, ha='center', fontweight='bold')
        ax.text(1.2, 3, '5 cm', fontsize=11, ha='center', fontweight='bold', rotation=90)
        
    elif diagram_type == "cuboid":
        # Simple 3D cuboid representation
        # Front face
        rect = plt.Rectangle((3, 1), 4, 2.5, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        # Top face
        ax.plot([3, 4], [3.5, 4.5], 'k-', linewidth=2)
        ax.plot([7, 8], [3.5, 4.5], 'k-', linewidth=2)
        ax.plot([4, 8], [4.5, 4.5], 'k-', linewidth=2)
        # Side face
        ax.plot([7, 8], [1, 1], 'k-', linewidth=2)
        ax.plot([8, 8], [1, 4.5], 'k-', linewidth=2)
        # Labels
        ax.text(5, 0.5, '6 cm', fontsize=10, ha='center')
        ax.text(2.3, 2.2, '3 cm', fontsize=10, ha='center', rotation=90)
        ax.text(5.8, 4.8, '4 cm', fontsize=10, ha='center')
        
    elif diagram_type == "circle":
        # Circle with radius
        circle = plt.Circle((5, 3), 2, fill=False, edgecolor='black', linewidth=2.5)
        ax.add_patch(circle)
        ax.plot([5, 7], [3, 3], 'b-', linewidth=2)
        ax.text(6, 3.4, 'r = 7 cm', fontsize=11, color='blue', fontweight='bold')
        ax.plot(5, 3, 'ko', markersize=4)
        
    elif diagram_type == "bar_chart":
        ax.axis('on')
        students = ['Ali', 'Ben', 'Cal', 'Dan', 'Eve']
        books = [12, 8, 15, 6, 10]
        colors = ['#4472C4', '#ED7D31', '#A5A5A5', '#FFC000', '#5B9BD5']
        bars = ax.bar(students, books, color=colors, edgecolor='black', linewidth=1)
        ax.set_ylabel('Books', fontsize=9)
        ax.set_ylim(0, 18)
        ax.set_title('Books Read by Students', fontsize=10, fontweight='bold')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
    elif diagram_type == "line_graph":
        ax.axis('on')
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        temp = [28, 30, 32, 29, 31, 33, 30]
        ax.plot(days, temp, marker='o', linewidth=2.5, markersize=8, color='#4472C4', markerfacecolor='red')
        ax.set_ylabel('Temp (°C)', fontsize=9)
        ax.set_ylim(25, 35)
        ax.set_title('Temperature Over Week', fontsize=10, fontweight='bold')
        ax.grid(True, alpha=0.3, linestyle='--')
        
    elif diagram_type == "pie_chart":
        ax.axis('on')
        labels = ['Apples\n72°', 'Oranges', 'Pears', 'Others']
        sizes = [72, 90, 108, 90]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        explode = (0.05, 0, 0, 0)
        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
               autopct='%1.0f°', startangle=90, 
               wedgeprops=dict(edgecolor='black', linewidth=1.5),
               textprops={'fontsize': 9})
        ax.set_title('Fruit Distribution', fontsize=10, fontweight='bold')
    
    plt.tight_layout(pad=0.3)
    filepath = RENDERS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white', pad_inches=0.1)
    plt.close()
    return filepath

# Generate all diagrams
print("Generating inline diagrams...")
diagrams = {
    'G001': create_diagram('inline_G001.png', 'angle_straight'),
    'G002': create_diagram('inline_G002.png', 'angle_straight'),
    'G005': create_diagram('inline_G005.png', 'triangle'),
    'G009': create_diagram('inline_G009.png', 'rectangle'),
    'G017': create_diagram('inline_G017.png', 'cuboid'),
    'G024': create_diagram('inline_G024.png', 'circle'),
    'DI021': create_diagram('inline_DI021.png', 'bar_chart'),
    'DI022': create_diagram('inline_DI022.png', 'bar_chart'),
    'DI024': create_diagram('inline_DI024.png', 'line_graph'),
    'DI026': create_diagram('inline_DI026.png', 'line_graph'),
    'DI027': create_diagram('inline_DI027.png', 'pie_chart'),
    'DI028': create_diagram('inline_DI028.png', 'pie_chart'),
}
print(f"Generated {len(diagrams)} diagrams")

# Problem definitions with diagram references
PROBLEMS = [
    # WORD PROBLEMS (20) - no diagrams
    {"num": 1, "id": "WP001", "type": "WP", "pathway": "Before-After", "diff": "E", 
     "text": "A shop had 240 pens. On Monday, they sold 2/5 of the pens. On Tuesday, they sold 1/3 of the remaining pens. How many pens were left?", "ans": "96 pens", "diagram": None},
    {"num": 2, "id": "WP002", "type": "WP", "pathway": "Before-After", "diff": "M", 
     "text": "Sarah spent 3/8 of her money on a book and 2/5 of the remainder on a pen. If she had $30 left, how much did she have at first?", "ans": "$80", "diagram": None},
    {"num": 3, "id": "WP003", "type": "WP", "pathway": "Part-Whole", "diff": "E", 
     "text": "Ali has $120. Ben has 3/4 as much as Ali. How much money do they have altogether?", "ans": "$210", "diagram": None},
    {"num": 4, "id": "WP004", "type": "WP", "pathway": "Part-Whole", "diff": "M", 
     "text": "The ratio of boys to girls in a class is 5:3. If there are 40 students altogether, how many boys are there?", "ans": "25 boys", "diagram": None},
    {"num": 5, "id": "WP005", "type": "WP", "pathway": "Cross-Thread", "diff": "M", 
     "text": "A baker made 360 cupcakes. He sold 1/4 of them in the morning and 2/3 of the remainder in the afternoon. How many cupcakes did he have left?", "ans": "90 cupcakes", "diagram": None},
    {"num": 6, "id": "WP006", "type": "WP", "pathway": "Cross-Thread", "diff": "H", 
     "text": "Alice and Betty had $280 altogether. After Alice spent 1/3 of her money and Betty spent $40, they had the same amount left. How much did Alice have at first?", "ans": "$144", "diagram": None},
    {"num": 7, "id": "WP007", "type": "WP", "pathway": "Before-After", "diff": "M", 
     "text": "A tank was full of water. After 3/7 of the water was poured out, then 2/5 of the remaining water was used, 48 litres were left. How much water was in the tank at first?", "ans": "140 litres", "diagram": None},
    {"num": 8, "id": "WP008", "type": "WP", "pathway": "Part-Whole", "diff": "M", 
     "text": "John has 3/5 as many stamps as Mary. Mary has 5/6 as many stamps as Tom. If Tom has 72 stamps, how many stamps does John have?", "ans": "36 stamps", "diagram": None},
    {"num": 9, "id": "WP009", "type": "WP", "pathway": "Before-After", "diff": "E", 
     "text": "A bus had 60 passengers. At the first stop, 15 passengers got off. At the second stop, 8 passengers got off. How many passengers were left?", "ans": "37 passengers", "diagram": None},
    {"num": 10, "id": "WP010", "type": "WP", "pathway": "Cross-Thread", "diff": "H", 
     "text": "The ratio of red balls to blue balls in a bag was 3:5. After removing 12 red balls, the ratio became 1:3. How many red balls were there at first?", "ans": "27 red balls", "diagram": None},
    {"num": 11, "id": "WP011", "type": "WP", "pathway": "Cross-Thread", "diff": "H", 
     "text": "The ratio of Alan's age to Ben's age is 4:7. In 6 years, the ratio will be 2:3. How old is Alan now?", "ans": "24 years old", "diagram": None},
    {"num": 12, "id": "WP012", "type": "WP", "pathway": "Before-After", "diff": "M", 
     "text": "A library had 450 books. They received 120 new books on Monday. On Tuesday, they donated 1/5 of their total books to a school. How many books did they have left?", "ans": "456 books", "diagram": None},
    {"num": 13, "id": "WP013", "type": "WP", "pathway": "Part-Whole", "diff": "E", 
     "text": "There are 80 students in a hall. 3/8 of them are girls. How many boys are there?", "ans": "50 boys", "diagram": None},
    {"num": 14, "id": "WP014", "type": "WP", "pathway": "Cross-Thread", "diff": "M", 
     "text": "A fruit seller had 240 apples. He sold 3/4 of them to Shop A and 1/2 of the remainder to Shop B. How many apples did he have left?", "ans": "30 apples", "diagram": None},
    {"num": 15, "id": "WP015", "type": "WP", "pathway": "Part-Whole", "diff": "M", 
     "text": "Jenny and Kelly have 84 stickers altogether. Jenny has 16 more stickers than Kelly. How many stickers does Kelly have?", "ans": "34 stickers", "diagram": None},
    {"num": 16, "id": "WP016", "type": "WP", "pathway": "Before-After", "diff": "H", 
     "text": "A shop increased the price of a bag by 20%. During a sale, they offered a 15% discount on the new price. If the final price was $204, what was the original price?", "ans": "$200", "diagram": None},
    {"num": 17, "id": "WP017", "type": "WP", "pathway": "Part-Whole", "diff": "H", 
     "text": "The ratio of apples to oranges to pears is 2:3:5. If there are 120 oranges and pears altogether, how many apples are there?", "ans": "30 apples", "diagram": None},
    {"num": 18, "id": "WP018", "type": "WP", "pathway": "Cross-Thread", "diff": "H", 
     "text": "A tank was 5/6 full of water. After 15 litres were poured out, it was 2/3 full. What is the capacity of the tank?", "ans": "90 litres", "diagram": None},
    {"num": 19, "id": "WP019", "type": "WP", "pathway": "Before-After", "diff": "M", 
     "text": "Mrs. Tan had some money in her purse. She spent $25 on groceries and then deposited 1/4 of the remainder into her bank account. If she had $45 left, how much did she have at first?", "ans": "$85", "diagram": None},
    {"num": 20, "id": "WP020", "type": "WP", "pathway": "Part-Whole", "diff": "M", 
     "text": "The ratio of boys to girls in a club is 5:3. There are 24 more boys than girls. How many children are in the club?", "ans": "96 children", "diagram": None},
    
    # GEOMETRY (12) - WITH INLINE DIAGRAMS
    {"num": 21, "id": "G001", "type": "G", "pathway": "Geometry-Angle", "diff": "E", 
     "text": "Measure the angles A, B, and C in the diagram using a protractor.", "ans": "See diagram", "diagram": "G001"},
    {"num": 22, "id": "G002", "type": "G", "pathway": "Geometry-Angle", "diff": "E", 
     "text": "Two angles on a straight line are given. If angle AOC = 65°, find angle COB.", "ans": "115°", "diagram": "G002"},
    {"num": 23, "id": "G005", "type": "G", "pathway": "Geometry-Triangle", "diff": "M", 
     "text": "In triangle ABC, angle A = 50° and angle B = 70°. Find angle C.", "ans": "60°", "diagram": "G005"},
    {"num": 24, "id": "G007", "type": "G", "pathway": "Geometry-Angle", "diff": "H", 
     "text": "Angle A and Angle B are on a straight line. Angle B and Angle C are complementary. If Angle A = 110°, find Angle C.", "ans": "20°", "diagram": None},
    {"num": 25, "id": "G009", "type": "G", "pathway": "Geometry-Perimeter", "diff": "E", 
     "text": "Find the perimeter of the rectangle shown in the diagram.", "ans": "26 cm", "diagram": "G009"},
    {"num": 26, "id": "G010", "type": "G", "pathway": "Geometry-Composite", "diff": "M", 
     "text": "A rectilinear figure consists of two rectangles joined together. Find its perimeter.", "ans": "See working", "diagram": None},
    {"num": 27, "id": "G011", "type": "G", "pathway": "Geometry-Area", "diff": "M", 
     "text": "Find the area of an L-shape figure formed by two rectangles.", "ans": "See working", "diagram": None},
    {"num": 28, "id": "G014", "type": "G", "pathway": "Geometry-Conversion", "diff": "M", 
     "text": "Convert 2.5 square metres to square centimetres.", "ans": "25,000 cm²", "diagram": None},
    {"num": 29, "id": "G017", "type": "G", "pathway": "Geometry-Volume", "diff": "E", 
     "text": "Find the volume of the cuboid shown in the diagram.", "ans": "72 cm³", "diagram": "G017"},
    {"num": 30, "id": "G019", "type": "G", "pathway": "Geometry-3D", "diff": "M", 
     "text": "Which of the following nets can be folded to form a cube? (Draw your answer)", "ans": "See drawing", "diagram": None},
    {"num": 31, "id": "G021", "type": "G", "pathway": "Geometry-Classify", "diff": "E", 
     "text": "Classify the triangle with side lengths 5 cm, 5 cm, 5 cm.", "ans": "Equilateral", "diagram": None},
    {"num": 32, "id": "G024", "type": "G", "pathway": "Geometry-Circle", "diff": "M", 
     "text": "A circle has radius 7 cm as shown. Find its circumference (take π = 22/7).", "ans": "44 cm", "diagram": "G024"},
    
    # DATA INTERPRETATION (8) - WITH INLINE CHARTS
    {"num": 33, "id": "DI021", "type": "DI", "pathway": "DI-Bar Chart", "diff": "E", 
     "text": "The bar chart shows books read by 5 students. Who read the most books?", "ans": "Cal (15 books)", "diagram": "DI021"},
    {"num": 34, "id": "DI022", "type": "DI", "pathway": "DI-Bar Chart", "diff": "E", 
     "text": "Calculate the total number of books read by all students and find the average.", "ans": "Total: 51, Average: 10.2", "diagram": "DI022"},
    {"num": 35, "id": "DI023", "type": "DI", "pathway": "DI-Bar Chart", "diff": "M", 
     "text": "Find the mode and range of the number of books read from the chart.", "ans": "Mode: varies, Range: 9", "diagram": None},
    {"num": 36, "id": "DI024", "type": "DI", "pathway": "DI-Line Graph", "diff": "M", 
     "text": "The line graph shows temperature over a week. Identify the hottest day.", "ans": "Saturday (33°C)", "diagram": "DI024"},
    {"num": 37, "id": "DI025", "type": "DI", "pathway": "DI-Line Graph", "diff": "M", 
     "text": "Estimate the temperature on Wednesday afternoon using interpolation.", "ans": "Approximately 31°C", "diagram": None},
    {"num": 38, "id": "DI026", "type": "DI", "pathway": "DI-Line Graph", "diff": "H", 
     "text": "Compare the sales trends of Product A and Product B. Which showed more consistent growth?", "ans": "See graph", "diagram": "DI026"},
    {"num": 39, "id": "DI027", "type": "DI", "pathway": "DI-Pie Chart", "diff": "M", 
     "text": "The pie chart shows a sector with angle 72°. What fraction of the whole does this represent?", "ans": "1/5", "diagram": "DI027"},
    {"num": 40, "id": "DI028", "type": "DI", "pathway": "DI-Pie Chart", "diff": "H", 
     "text": "Given that apples = 72° (60 apples), find the total number of fruits.", "ans": "300 fruits", "diagram": "DI028"},
]

def wrap_text(c, text, x, y, max_width, font_size=9, line_height=0.14*inch):
    """Simple text wrapping."""
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
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    lm = 0.5 * inch  # left margin
    rm = 0.5 * inch
    tm = 0.5 * inch
    bm = 0.5 * inch
    cw = width - lm - rm
    
    # Header
    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(width/2, height - tm, "ATOM-SG Pilot - Week 1 Baseline Test")
    c.setFont("Helvetica", 10)
    c.drawCentredString(width/2, height - tm - 0.2*inch, "P6 Mathematics | 40 Questions | 50 Minutes | No Calculator")
    
    # Student info
    c.setFont("Helvetica-Bold", 9)
    y = height - tm - 0.55*inch
    c.drawString(lm, y, "Name: _________________________________  Class: _______  Date: ___________")
    
    # Instructions
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 8)
    c.drawString(lm, y, "Instructions: Show all working. Write answers in the boxes. Diagrams are shown with each question.")
    y -= 0.18*inch
    
    for prob in PROBLEMS:
        # Estimate space needed
        has_diagram = prob.get("diagram") is not None
        space_needed = 1.0 * inch  # Base
        if has_diagram:
            space_needed += 1.8 * inch  # Diagram space
        
        # Page break if needed
        if y - space_needed < bm:
            c.showPage()
            y = height - tm
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(width/2, y, "Baseline Test - Continued")
            y -= 0.25*inch
        
        # Question header
        c.setFont("Helvetica-Bold", 8)
        c.drawString(lm, y, f"Q{prob['num']:2d}. [{prob['diff']}] [{prob['type']}] {prob['pathway'][:25]}")
        y -= 0.16*inch
        
        # Question text
        c.setFont("Helvetica", 9)
        y = wrap_text(c, prob['text'], lm + 0.05*inch, y, cw - 0.1*inch, font_size=9, line_height=0.14*inch)
        
        # Diagram - INLINE (immediately after question)
        if has_diagram:
            y -= 0.08*inch
            diag_key = prob['diagram']
            if diag_key in diagrams:
                diag_path = diagrams[diag_key]
                # Draw diagram inline
                img_width = 2.6 * inch
                img_height = 1.5 * inch
                # Center the diagram
                x_pos = lm + (cw - img_width) / 2
                c.drawImage(str(diag_path), x_pos, y - img_height, width=img_width, height=img_height)
                y -= img_height + 0.1*inch
        
        # Working space
        y -= 0.06*inch
        c.setFont("Helvetica-Bold", 7)
        c.drawString(lm + 0.05*inch, y, "Working:")
        y -= 0.12*inch
        wh = 0.5 * inch
        c.rect(lm + 0.05*inch, y - wh, cw - 0.15*inch, wh)
        y -= wh + 0.1*inch
        
        # Answer box
        c.setFont("Helvetica-Bold", 8)
        c.drawString(lm + 0.05*inch, y, f"Answer: _________________________")
        y -= 0.18*inch
        
        # Separator line
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.line(lm, y, width - rm, y)
        c.setStrokeColorRGB(0, 0, 0)
        y -= 0.1*inch
    
    # Answer key page
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
    print(f"   40 questions with {sum(1 for p in PROBLEMS if p.get('diagram'))} inline visuals")

if __name__ == "__main__":
    output_path = RENDERS_DIR / "ATOM-SG_Baseline_Test_INLINE_VISUALS.pdf"
    generate_pdf(output_path)
