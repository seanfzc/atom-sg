#!/usr/bin/env python3
"""
Generate complete 40-question baseline test PDF with EMBEDDED visuals.
Diagrams and charts render inline with questions.
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io
import os

# Ensure renders directory exists
RENDERS_DIR = Path(__file__).parent / "artifacts" / "renders"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)

def create_angle_diagram(filename, angle_type="straight"):
    """Create an angle diagram and save as PNG."""
    fig, ax = plt.subplots(figsize=(3, 2), dpi=100)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.axis('off')
    
    if angle_type == "straight":
        # Two angles on straight line
        ax.plot([-1, 0], [0, 0], 'k-', linewidth=2)
        ax.plot([0, 1], [0, 0], 'k-', linewidth=2)
        ax.plot([0, 0], [0, 1], 'k-', linewidth=2)
        # Arc for angle
        theta = np.linspace(0, np.pi/3, 50)
        ax.plot(0.3*np.cos(theta), 0.3*np.sin(theta), 'b-', linewidth=1.5)
        ax.text(0.4, 0.15, '65°', fontsize=10, color='blue')
        ax.text(-0.8, -0.2, 'A', fontsize=10)
        ax.text(0.8, -0.2, 'B', fontsize=10)
        ax.text(-0.1, 1.1, 'C', fontsize=10)
        ax.text(-0.1, -0.15, 'O', fontsize=10)
    elif angle_type == "triangle":
        # Triangle with two angles given
        triangle = plt.Polygon([[0, 0], [2, 0], [1, 1.5]], fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(triangle)
        ax.text(-0.15, -0.15, 'A', fontsize=10)
        ax.text(2.05, -0.15, 'B', fontsize=10)
        ax.text(0.95, 1.65, 'C', fontsize=10)
        # Arc for angles
        ax.text(0.3, 0.15, '50°', fontsize=9, color='blue')
        ax.text(1.5, 0.15, '70°', fontsize=9, color='blue')
    
    plt.tight_layout()
    filepath = RENDERS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    return filepath

def create_bar_chart(filename, title="Books Read by Students"):
    """Create a bar chart."""
    fig, ax = plt.subplots(figsize=(4, 2.5), dpi=100)
    students = ['Ali', 'Ben', 'Cal', 'Dan', 'Eve']
    books = [12, 8, 15, 6, 10]
    colors_list = ['#4472C4', '#ED7D31', '#A5A5A5', '#FFC000', '#5B9BD5']
    bars = ax.bar(students, books, color=colors_list, edgecolor='black')
    ax.set_ylabel('Number of Books', fontsize=9)
    ax.set_title(title, fontsize=10, fontweight='bold')
    ax.set_ylim(0, 18)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    filepath = RENDERS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    return filepath

def create_line_graph(filename, title="Temperature Over Week"):
    """Create a line graph."""
    fig, ax = plt.subplots(figsize=(4, 2.5), dpi=100)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    temp = [28, 30, 32, 29, 31, 33, 30]
    ax.plot(days, temp, marker='o', linewidth=2, markersize=6, color='#4472C4')
    ax.set_ylabel('Temperature (°C)', fontsize=9)
    ax.set_title(title, fontsize=10, fontweight='bold')
    ax.set_ylim(25, 35)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    filepath = RENDERS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    return filepath

def create_pie_chart(filename, title="Fruit Distribution"):
    """Create a pie chart."""
    fig, ax = plt.subplots(figsize=(3.5, 3), dpi=100)
    fruits = ['Apples', 'Oranges', 'Pears', 'Others']
    values = [90, 72, 108, 90]  # Angles: 90°, 72°, 108°, 90°
    colors_list = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    explode = (0.05, 0, 0, 0)
    wedges, texts, autotexts = ax.pie(values, explode=explode, labels=fruits, colors=colors_list,
                                       autopct='%1.0f°', startangle=90, 
                                       wedgeprops=dict(edgecolor='black', linewidth=1))
    ax.set_title(title, fontsize=10, fontweight='bold')
    plt.tight_layout()
    filepath = RENDERS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    return filepath

def create_rectangle_diagram(filename, length=8, breadth=5):
    """Create a rectangle with dimensions."""
    fig, ax = plt.subplots(figsize=(3.5, 2.5), dpi=100)
    rect = plt.Rectangle((0.5, 0.5), length/2, breadth/2, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    # Dimension labels
    ax.text(0.5 + length/4, 0.3, f'{length} cm', ha='center', fontsize=9)
    ax.text(0.3, 0.5 + breadth/4, f'{breadth} cm', ha='center', fontsize=9, rotation=90, va='center')
    ax.set_xlim(0, 5.5)
    ax.set_ylim(0, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    filepath = RENDERS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    return filepath

def create_cuboid_diagram(filename):
    """Create a cuboid diagram."""
    fig = plt.figure(figsize=(3.5, 2.5), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    # Draw cuboid
    x, y, z = [0, 6], [0, 4], [0, 3]
    xx, yy = np.meshgrid(x, y)
    ax.plot_surface(xx, yy, np.full_like(xx, z[0]), alpha=0.3, color='lightblue', edgecolor='black')
    ax.plot_surface(xx, yy, np.full_like(xx, z[1]), alpha=0.3, color='lightblue', edgecolor='black')
    # Labels
    ax.text(3, -0.5, 0, '6 cm', fontsize=8, ha='center')
    ax.text(6.5, 2, 0, '4 cm', fontsize=8, ha='center')
    ax.text(0, -0.5, 1.5, '3 cm', fontsize=8, ha='center')
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 5)
    ax.set_zlim(-1, 5)
    ax.axis('off')
    plt.tight_layout()
    filepath = RENDERS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    return filepath

def create_circle_diagram(filename, radius=7):
    """Create a circle with radius."""
    fig, ax = plt.subplots(figsize=(3, 3), dpi=100)
    circle = plt.Circle((0.5, 0.5), 0.35, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    # Radius line
    ax.plot([0.5, 0.85], [0.5, 0.5], 'b-', linewidth=1.5)
    ax.text(0.675, 0.55, f'r = {radius} cm', fontsize=9, color='blue', ha='center')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    filepath = RENDERS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    return filepath

# Generate all diagram files first
print("Generating diagram files...")
diagram_files = {
    'G001': create_angle_diagram('G001_angle_measure.png', 'straight'),
    'G002': create_angle_diagram('G002_straight_line.png', 'straight'),
    'G005': create_angle_diagram('G005_triangle.png', 'triangle'),
    'G009': create_rectangle_diagram('G009_rectangle.png', 8, 5),
    'G017': create_cuboid_diagram('G017_cuboid.png'),
    'G024': create_circle_diagram('G024_circle.png', 7),
    'DI021': create_bar_chart('DI021_bar_chart.png', 'Books Read by Students'),
    'DI022': create_bar_chart('DI022_bar_chart2.png', 'Monthly Sales'),
    'DI024': create_line_graph('DI024_line_graph.png', 'Temperature Over Week'),
    'DI026': create_line_graph('DI026_line_graph2.png', 'Product Sales Comparison'),
    'DI027': create_pie_chart('DI027_pie_chart.png', 'Fruit Distribution'),
    'DI028': create_pie_chart('DI028_pie_chart2.png', 'Survey Results'),
}
print(f"Generated {len(diagram_files)} diagram files")

# Problem data
BASELINE_PROBLEMS = [
    # WORD PROBLEMS (20)
    {"id": "WP001", "type": "WP", "pathway": "Before-After Change", "diff": "E", 
     "question": "A shop had 240 pens. On Monday, they sold 2/5 of the pens. On Tuesday, they sold 1/3 of the remaining pens. How many pens were left on Wednesday?", 
     "answer": "96 pens", "diagram": None},
    {"id": "WP002", "type": "WP", "pathway": "Before-After Change", "diff": "M", 
     "question": "Sarah spent 3/8 of her money on a book and 2/5 of the remainder on a pen. If she had $30 left, how much did she have at first?", 
     "answer": "$80", "diagram": None},
    {"id": "WP007", "type": "WP", "pathway": "Before-After Change", "diff": "M", 
     "question": "A tank was full of water. After 3/7 of the water was poured out, then 2/5 of the remaining water was used, 48 litres were left. How much water was in the tank at first?", 
     "answer": "140 litres", "diagram": None},
    {"id": "WP009", "type": "WP", "pathway": "Before-After Change", "diff": "E", 
     "question": "A bus had 60 passengers. At the first stop, 15 passengers got off. At the second stop, 8 passengers got off. How many passengers were left on the bus?", 
     "answer": "37 passengers", "diagram": None},
    {"id": "WP012", "type": "WP", "pathway": "Before-After Change", "diff": "M", 
     "question": "A library had 450 books. They received 120 new books on Monday. On Tuesday, they donated 1/5 of their total books to a school. How many books did they have left?", 
     "answer": "456 books", "diagram": None},
    {"id": "WP019", "type": "WP", "pathway": "Before-After Change", "diff": "M", 
     "question": "Mrs. Tan had some money in her purse. She spent $25 on groceries and then deposited 1/4 of the remainder into her bank account. If she had $45 left, how much did she have at first?", 
     "answer": "$85", "diagram": None},
    {"id": "WP003", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "E", 
     "question": "Ali has $120. Ben has 3/4 as much as Ali. How much money do they have altogether?", 
     "answer": "$210", "diagram": None},
    {"id": "WP004", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "M", 
     "question": "The ratio of boys to girls in a class is 5:3. If there are 40 students altogether, how many boys are there?", 
     "answer": "25 boys", "diagram": None},
    {"id": "WP008", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "M", 
     "question": "John has 3/5 as many stamps as Mary. Mary has 5/6 as many stamps as Tom. If Tom has 72 stamps, how many stamps does John have?", 
     "answer": "36 stamps", "diagram": None},
    {"id": "WP013", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "E", 
     "question": "There are 80 students in a hall. 3/8 of them are girls. How many boys are there?", 
     "answer": "50 boys", "diagram": None},
    {"id": "WP015", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "M", 
     "question": "Jenny and Kelly have 84 stickers altogether. Jenny has 16 more stickers than Kelly. How many stickers does Kelly have?", 
     "answer": "34 stickers", "diagram": None},
    {"id": "WP017", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "H", 
     "question": "The ratio of apples to oranges to pears is 2:3:5. If there are 120 oranges and pears altogether, how many apples are there?", 
     "answer": "30 apples", "diagram": None},
    {"id": "WP020", "type": "WP", "pathway": "Part-Whole Comparison", "diff": "M", 
     "question": "The ratio of boys to girls in a club is 5:3. There are 24 more boys than girls. How many children are in the club?", 
     "answer": "96 children", "diagram": None},
    {"id": "WP005", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "M", 
     "question": "A baker made 360 cupcakes. He sold 1/4 of them in the morning and 2/3 of the remainder in the afternoon. How many cupcakes did he have left?", 
     "answer": "90 cupcakes", "diagram": None},
    {"id": "WP006", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "H", 
     "question": "Alice and Betty had $280 altogether. After Alice spent 1/3 of her money and Betty spent $40, they had the same amount left. How much did Alice have at first?", 
     "answer": "$144", "diagram": None},
    {"id": "WP010", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "H", 
     "question": "The ratio of red balls to blue balls in a bag was 3:5. After removing 12 red balls, the ratio became 1:3. How many red balls were there at first?", 
     "answer": "27 red balls", "diagram": None},
    {"id": "WP011", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "H", 
     "question": "The ratio of Alan's age to Ben's age is 4:7. In 6 years, the ratio will be 2:3. How old is Alan now?", 
     "answer": "24 years old", "diagram": None},
    {"id": "WP014", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "M", 
     "question": "A fruit seller had 240 apples. He sold 3/4 of them to Shop A and 1/2 of the remainder to Shop B. How many apples did he have left?", 
     "answer": "30 apples", "diagram": None},
    {"id": "WP018", "type": "WP", "pathway": "Cross-Thread Collision", "diff": "H", 
     "question": "A tank was 5/6 full of water. After 15 litres were poured out, it was 2/3 full. What is the capacity of the tank?", 
     "answer": "90 litres", "diagram": None},
    {"id": "WP016", "type": "WP", "pathway": "Before-After Change", "diff": "H", 
     "question": "A shop increased the price of a bag by 20%. During a sale, they offered a 15% discount on the new price. If the final price was $204, what was the original price?", 
     "answer": "$200", "diagram": None},
    
    # GEOMETRY (12) - WITH DIAGRAMS
    {"id": "G001", "type": "G", "pathway": "Geometry - Angle Measurement", "diff": "E", 
     "question": "Measure the angles A, B, and C in the diagram using a protractor.", 
     "answer": "See diagram", "diagram": "G001_angle_measure.png"},
    {"id": "G002", "type": "G", "pathway": "Geometry - Angle Properties", "diff": "E", 
     "question": "Two angles on a straight line are given. If one angle is 65 degrees, find the other angle.", 
     "answer": "115 degrees", "diagram": "G002_straight_line.png"},
    {"id": "G005", "type": "G", "pathway": "Geometry - Triangle Angles", "diff": "M", 
     "question": "In triangle ABC, angle A = 50 degrees and angle B = 70 degrees. Find angle C.", 
     "answer": "60 degrees", "diagram": "G005_triangle.png"},
    {"id": "G007", "type": "G", "pathway": "Geometry - Combined Angles", "diff": "H", 
     "question": "Angle A and Angle B are on a straight line. Angle B and Angle C are complementary (sum to 90 degrees). If Angle A = 110 degrees, find Angle C.", 
     "answer": "20 degrees", "diagram": None},
    {"id": "G009", "type": "G", "pathway": "Geometry - Perimeter", "diff": "E", 
     "question": "Find the perimeter of the rectangle shown in the diagram.", 
     "answer": "26 cm", "diagram": "G009_rectangle.png"},
    {"id": "G010", "type": "G", "pathway": "Geometry - Composite Perimeter", "diff": "M", 
     "question": "A rectilinear figure consists of two rectangles joined together. Find its perimeter, given some side lengths.", 
     "answer": "See diagram", "diagram": None},
    {"id": "G011", "type": "G", "pathway": "Geometry - Composite Area", "diff": "M", 
     "question": "Find the area of an L-shape figure formed by two rectangles.", 
     "answer": "See diagram", "diagram": None},
    {"id": "G014", "type": "G", "pathway": "Geometry - Unit Conversion", "diff": "M", 
     "question": "Convert 2.5 square metres to square centimetres.", 
     "answer": "25,000 cm squared", "diagram": None},
    {"id": "G017", "type": "G", "pathway": "Geometry - Volume", "diff": "E", 
     "question": "Find the volume of the cuboid shown in the diagram.", 
     "answer": "72 cubic cm", "diagram": "G017_cuboid.png"},
    {"id": "G019", "type": "G", "pathway": "Geometry - 3D Nets", "diff": "M", 
     "question": "Which of the following nets can be folded to form a cube?", 
     "answer": "See diagram", "diagram": None},
    {"id": "G021", "type": "G", "pathway": "Geometry - Triangle Classification", "diff": "E", 
     "question": "Classify the triangle with side lengths 5 cm, 5 cm, 5 cm.", 
     "answer": "Equilateral", "diagram": None},
    {"id": "G024", "type": "G", "pathway": "Geometry - Circle", "diff": "M", 
     "question": "A circle has radius 7 cm as shown. Find its circumference (take pi = 22/7).", 
     "answer": "44 cm", "diagram": "G024_circle.png"},
    
    # DATA INTERPRETATION (8) - WITH CHARTS
    {"id": "DI021", "type": "DI", "pathway": "Data Interpretation - Bar Graph", "diff": "E", 
     "question": "The bar graph shows the number of books read by 5 students. Who read the most books?", 
     "answer": "Cal (15 books)", "diagram": "DI021_bar_chart.png"},
    {"id": "DI022", "type": "DI", "pathway": "Data Interpretation - Bar Graph", "diff": "E", 
     "question": "Calculate the total number of books read by all students and find the average.", 
     "answer": "Total: 51, Average: 10.2", "diagram": "DI021_bar_chart.png"},
    {"id": "DI023", "type": "DI", "pathway": "Data Interpretation - Bar Graph", "diff": "M", 
     "question": "Find the mode and range of the number of books read.", 
     "answer": "Mode: varies, Range: 9", "diagram": "DI022_bar_chart2.png"},
    {"id": "DI024", "type": "DI", "pathway": "Data Interpretation - Line Graph", "diff": "M", 
     "question": "The line graph shows temperature over a week. Describe the trend and identify the hottest day.", 
     "answer": "Saturday (33°C)", "diagram": "DI024_line_graph.png"},
    {"id": "DI025", "type": "DI", "pathway": "Data Interpretation - Line Graph", "diff": "M", 
     "question": "Estimate the temperature on Wednesday afternoon using interpolation.", 
     "answer": "Approximately 31°C", "diagram": "DI024_line_graph.png"},
    {"id": "DI026", "type": "DI", "pathway": "Data Interpretation - Line Graph", "diff": "H", 
     "question": "Compare the sales trends of Product A and Product B over 6 months. Which product showed more consistent growth?", 
     "answer": "See graph", "diagram": "DI026_line_graph2.png"},
    {"id": "DI027", "type": "DI", "pathway": "Data Interpretation - Pie Chart", "diff": "M", 
     "question": "The pie chart shows a sector with angle 90 degrees. What fraction of the whole does this sector represent?", 
     "answer": "1/4", "diagram": "DI027_pie_chart.png"},
    {"id": "DI028", "type": "DI", "pathway": "Data Interpretation - Pie Chart", "diff": "H", 
     "question": "Given that the sector representing apples has angle 72 degrees and there are 60 apples, find the total number of fruits.", 
     "answer": "300 fruits", "diagram": "DI028_pie_chart2.png"},
]

def draw_wrapped_text(c, text, x, y, max_width, line_height=0.16*inch, font_name="Helvetica", font_size=10):
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

def generate_baseline_with_visuals(output_path: Path) -> None:
    """Generate complete baseline test with embedded visuals."""
    all_problems = BASELINE_PROBLEMS
    
    print(f"Generating baseline test with {len(all_problems)} questions and embedded visuals")
    
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    
    left_margin = 0.5 * inch
    right_margin = 0.5 * inch
    top_margin = 0.5 * inch
    bottom_margin = 0.5 * inch
    content_width = width - left_margin - right_margin
    
    def draw_header():
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width/2, height - top_margin, "ATOM-SG Pilot - Week 1 Baseline Test")
        
        c.setFont("Helvetica", 11)
        c.drawCentredString(width/2, height - top_margin - 0.22*inch, 
                           "P6 Mathematics - Recognition-First Assessment")
        
        c.setFont("Helvetica", 10)
        c.drawCentredString(width/2, height - top_margin - 0.4*inch,
                           "40 Questions | 50 Minutes | No Calculator")
        
        # Student info
        c.setFont("Helvetica-Bold", 10)
        y = height - top_margin - 0.7*inch
        c.drawString(left_margin, y, "Name: _________________________________  Class: _______  Date: ___________")
        
        # Instructions
        y -= 0.3*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(left_margin, y, "Instructions:")
        c.setFont("Helvetica", 8)
        instructions = [
            "1. This test has 40 questions: 20 Word Problems, 12 Geometry, 8 Data Interpretation.",
            "2. You have 50 minutes. Work quickly but carefully.",
            "3. Show all working in the spaces provided.",
            "4. Write final answers in the boxes.",
            "5. Calculators are NOT allowed.",
            "6. Diagrams and charts are shown with each question."
        ]
        y -= 0.16*inch
        for inst in instructions:
            c.drawString(left_margin + 0.1*inch, y, inst)
            y -= 0.13*inch
        
        return y - 0.12*inch
    
    def draw_question(c, q_num, problem, y_start):
        y = y_start
        q_type = problem.get('type', 'WP')
        diagram_file = problem.get('diagram')
        
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
        y -= 0.2*inch
        question = problem.get('question', '')[:300]
        c.setFont("Helvetica", 10)
        y = draw_wrapped_text(c, question, left_margin + 0.05*inch, y, 
                             max_width=content_width - 0.1*inch, 
                             line_height=0.15*inch, font_size=10)
        
        # Embed diagram if present
        if diagram_file and diagram_file in diagram_files:
            y -= 0.1*inch
            diagram_path = diagram_files[diagram_file]
            if diagram_path.exists():
                # Draw diagram - scale to fit width
                img_width = 2.5 * inch
                img_height = 1.5 * inch
                c.drawImage(str(diagram_path), left_margin + 0.1*inch, y - img_height, 
                           width=img_width, height=img_height)
                y -= img_height + 0.1*inch
        
        # Working space
        y -= 0.1*inch
        c.setFont("Helvetica-Bold", 8)
        c.drawString(left_margin + 0.05*inch, y, "Working:")
        y -= 0.14*inch
        working_height = 0.6*inch
        c.rect(left_margin + 0.05*inch, y - working_height, content_width - 0.15*inch, working_height)
        
        # Answer box
        y -= working_height + 0.12*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(left_margin + 0.05*inch, y, "Answer: _________________________________")
        
        # Separator
        y -= 0.22*inch
        c.setStrokeColorRGB(0.75, 0.75, 0.75)
        c.line(left_margin, y, width - right_margin, y)
        c.setStrokeColorRGB(0, 0, 0)
        
        return y - 0.08*inch
    
    # Generate pages
    y = draw_header()
    question_count = 0
    
    for i, prob in enumerate(all_problems, 1):
        # Check if we need a new page
        estimated_height = 1.5 * inch  # Base height
        if prob.get('diagram'):
            estimated_height += 1.7 * inch  # Add space for diagram
        
        if y - estimated_height < bottom_margin:
            c.showPage()
            y = height - top_margin
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(width/2, y, f"Baseline Test - Continued")
            y -= 0.3*inch
        
        y = draw_question(c, i, prob, y)
        question_count += 1
    
    # Answer Key Page
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - top_margin, "Answer Key - For Markers Only")
    
    y = height - top_margin - 0.4*inch
    c.setFont("Helvetica-Bold", 8)
    c.drawString(left_margin, y, "Q#  Type  Pathway                           Answer")
    c.line(left_margin, y - 0.06*inch, width - right_margin, y - 0.06*inch)
    
    y -= 0.15*inch
    c.setFont("Courier", 7)
    
    for i, prob in enumerate(all_problems, 1):
        ptype = prob.get('type', '')
        pathway = prob.get('pathway', '')[:25]
        answer = str(prob.get('answer', ''))[:25]
        c.drawString(left_margin, y, f"{i:2d}  {ptype}     {pathway:25s} {answer}")
        y -= 0.11*inch
        
        if y < bottom_margin + 0.3*inch and i < 40:
            c.showPage()
            y = height - top_margin
    
    # Footer
    c.setFont("Helvetica-Oblique", 7)
    c.drawCentredString(width/2, bottom_margin - 0.1*inch,
                       f"ATOM-SG Pilot MVP | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    c.save()
    print(f"\n✅ Generated baseline test with visuals: {output_path}")
    print(f"   Total questions: {len(all_problems)}")
    print(f"   Word Problems: {sum(1 for p in all_problems if p['type'] == 'WP')}")
    print(f"   Geometry: {sum(1 for p in all_problems if p['type'] == 'G')}")
    print(f"   Data Interpretation: {sum(1 for p in all_problems if p['type'] == 'DI')}")
    print(f"   Questions with diagrams: {sum(1 for p in all_problems if p.get('diagram'))}")

if __name__ == "__main__":
    output_path = RENDERS_DIR / "ATOM-SG_Baseline_Test_40_Questions_WITH_VISUALS.pdf"
    generate_baseline_with_visuals(output_path)
