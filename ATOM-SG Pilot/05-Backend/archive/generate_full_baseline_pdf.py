#!/usr/bin/env python3
"""
Generate full baseline test PDF with all 25 geometry problems.
This creates a comprehensive test paper for student assessment.
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from datetime import datetime
import re

# All 25 geometry problems from G001-G025
GEOMETRY_PROBLEMS = [
    {
        "id": "G001",
        "question": "Measure the angles ∠A, ∠B, and ∠C in the diagram using a protractor.",
        "subpathway": "Identify and measure angles using a protractor",
        "difficulty": "A",
        "answer_format": "∠A = _____°, ∠B = _____°, ∠C = _____°"
    },
    {
        "id": "G002",
        "question": "Two angles on a straight line are given. If one angle is 75°, find the other angle.",
        "subpathway": "Use angle properties to find unknown angles (angles on straight line)",
        "difficulty": "B",
        "answer_format": "The other angle = _____°"
    },
    {
        "id": "G003",
        "question": "Three angles meet at a point. Two angles are 120° and 85°. Find the third angle.",
        "subpathway": "Use angle properties to find unknown angles (angles at a point)",
        "difficulty": "B",
        "answer_format": "The third angle = _____°"
    },
    {
        "id": "G004",
        "question": "In the diagram, two straight lines intersect. If one angle is 40°, find the other three angles.",
        "subpathway": "Use angle properties to find unknown angles (vertically opposite angles)",
        "difficulty": "B",
        "answer_format": "∠1 = _____°, ∠2 = _____°, ∠3 = _____°"
    },
    {
        "id": "G005",
        "question": "In triangle ABC, ∠A = 50° and ∠B = 70°. Find ∠C.",
        "subpathway": "Apply angle sum of triangle (180°) to find missing angles",
        "difficulty": "C",
        "answer_format": "∠C = _____°"
    },
    {
        "id": "G006",
        "question": "Mark all pairs of perpendicular lines and parallel lines in the diagram.",
        "subpathway": "Identify perpendicular and parallel lines in diagrams",
        "difficulty": "A",
        "answer_format": "Perpendicular: _____, Parallel: _____"
    },
    {
        "id": "G007",
        "question": "∠A and ∠B are on a straight line. ∠B and ∠C are complementary (sum to 90°). If ∠A = 110°, find ∠C.",
        "subpathway": "Combined angle properties (multi-step)",
        "difficulty": "D",
        "answer_format": "∠C = _____°"
    },
    {
        "id": "G008",
        "question": "Measure the reflex angle ∠R in the diagram (angle greater than 180°).",
        "subpathway": "Measure reflex angles (protractor)",
        "difficulty": "C",
        "answer_format": "∠R = _____°"
    },
    {
        "id": "G009",
        "question": "Find the perimeter of a rectangle with length 8 cm and breadth 5 cm.",
        "subpathway": "Calculate perimeter of rectilinear figures",
        "difficulty": "A",
        "answer_format": "Perimeter = _____ cm"
    },
    {
        "id": "G010",
        "question": "A rectilinear figure consists of two rectangles joined together. Find its perimeter, given some side lengths.",
        "subpathway": "Calculate perimeter of rectilinear figures with missing lengths",
        "difficulty": "B",
        "answer_format": "Perimeter = _____ cm"
    },
    {
        "id": "G011",
        "question": "Find the area of an L-shape figure formed by two rectangles.",
        "subpathway": "Calculate area of composite rectangular figures",
        "difficulty": "B",
        "answer_format": "Area = _____ cm²"
    },
    {
        "id": "G012",
        "question": "A rectangular sheet has a smaller rectangle cut out from one corner. Find the remaining area.",
        "subpathway": "Calculate area of composite rectangular figures with missing sections",
        "difficulty": "C",
        "answer_format": "Remaining area = _____ cm²"
    },
    {
        "id": "G013",
        "question": "Convert 3.5 m to cm, and 250 cm to m.",
        "subpathway": "Convert between units of measurement (length)",
        "difficulty": "A",
        "answer_format": "3.5 m = _____ cm, 250 cm = _____ m"
    },
    {
        "id": "G014",
        "question": "Convert 2.5 m² to cm².",
        "subpathway": "Convert between units of measurement (area)",
        "difficulty": "B",
        "answer_format": "2.5 m² = _____ cm²"
    },
    {
        "id": "G015",
        "question": "Draw all lines of symmetry for a regular hexagon.",
        "subpathway": "Identify line(s) of symmetry in 2D shapes",
        "difficulty": "A",
        "answer_format": "Number of lines of symmetry = _____"
    },
    {
        "id": "G016",
        "question": "Complete the symmetrical figure given the mirror line (vertical).",
        "subpathway": "Complete symmetrical figures given mirror line",
        "difficulty": "C",
        "answer_format": "(Draw the completed figure in the space provided)"
    },
    {
        "id": "G017",
        "question": "Find the volume of a cuboid with length 6 cm, breadth 4 cm, height 3 cm.",
        "subpathway": "Calculate volume of cubes and cuboids",
        "difficulty": "A",
        "answer_format": "Volume = _____ cm³"
    },
    {
        "id": "G018",
        "question": "Find the volume of a box with dimensions 0.5 m × 30 cm × 200 mm. Give answer in cm³.",
        "subpathway": "Calculate volume of cubes and cuboids with unit conversion",
        "difficulty": "B",
        "answer_format": "Volume = _____ cm³"
    },
    {
        "id": "G019",
        "question": "Which of the following nets can be folded to form a cube?",
        "subpathway": "Visualize nets of cubes/cuboids and identify 3D shapes from nets",
        "difficulty": "C",
        "answer_format": "Valid net(s): _____ (circle your answer)"
    },
    {
        "id": "G020",
        "question": "Draw the net of a cuboid with dimensions 4 cm × 2 cm × 1 cm.",
        "subpathway": "Visualize nets of cubes/cuboids (draw net given 3D shape)",
        "difficulty": "D",
        "answer_format": "(Draw the net in the space provided)"
    },
    {
        "id": "G021",
        "question": "Classify the triangle with side lengths 5 cm, 5 cm, 5 cm.",
        "subpathway": "Classify triangles by sides (equilateral, isosceles, scalene)",
        "difficulty": "A",
        "answer_format": "Type of triangle: _____"
    },
    {
        "id": "G022",
        "question": "Classify the triangle with angles 45°, 45°, 90°.",
        "subpathway": "Classify triangles by angles (acute, right, obtuse)",
        "difficulty": "A",
        "answer_format": "Type of triangle: _____"
    },
    {
        "id": "G023",
        "question": "Identify the quadrilateral: It has two pairs of parallel sides, all sides equal, and angles are not 90°.",
        "subpathway": "Classify quadrilaterals (square, rectangle, parallelogram, rhombus, trapezium)",
        "difficulty": "B",
        "answer_format": "Quadrilateral type: _____"
    },
    {
        "id": "G024",
        "question": "A circle has radius 7 cm. Find its circumference (take π = 22/7).",
        "subpathway": "Calculate circumference/area of circle using π",
        "difficulty": "C",
        "answer_format": "Circumference = _____ cm"
    },
    {
        "id": "G025",
        "question": "A pie chart shows a sector with angle 90°. What fraction of the whole does this sector represent?",
        "subpathway": "Interpret pie charts as fractions of a circle",
        "difficulty": "D",
        "answer_format": "Fraction = _____"
    }
]


def draw_wrapped_text(c, text, x, y, max_width, line_height=0.2*inch, font_name="Helvetica", font_size=11):
    """Draw text with word wrapping and return new y position."""
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


def generate_full_baseline_pdf(output_path: Path, include_answer_sheet: bool = True) -> None:
    """
    Generate a comprehensive baseline test PDF with all 25 geometry problems.
    
    Args:
        output_path: Where to save the PDF
        include_answer_sheet: Whether to include a separate answer sheet page
    """
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    
    # Margins
    left_margin = 0.75 * inch
    right_margin = 0.75 * inch
    top_margin = 0.75 * inch
    bottom_margin = 0.75 * inch
    content_width = width - left_margin - right_margin
    
    def draw_header():
        """Draw the test header."""
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width/2, height - top_margin, "ATOM-SG Baseline Assessment Test")
        
        c.setFont("Helvetica", 12)
        c.drawCentredString(width/2, height - top_margin - 0.3*inch, 
                           "P6 Mathematics - Geometry Track (25 Questions)")
        
        # Student info box
        c.setFont("Helvetica-Bold", 10)
        c.drawString(left_margin, height - top_margin - 0.7*inch, "Name: _______________________________    Class: _______    Date: ___________")
        
        # Instructions
        c.setFont("Helvetica-Bold", 10)
        c.drawString(left_margin, height - top_margin - 1.1*inch, "Instructions:")
        c.setFont("Helvetica", 9)
        instructions = [
            "• This test contains 25 geometry questions. You have 45 minutes to complete it.",
            "• Show all your working in the spaces provided. Marks may be awarded for correct method.",
            "• Write your final answers in the boxes provided.",
            "• Calculators are NOT allowed unless specified.",
            "• Diagrams are NOT drawn to scale unless stated otherwise."
        ]
        y = height - top_margin - 1.3*inch
        for instruction in instructions:
            c.drawString(left_margin + 0.1*inch, y, instruction)
            y -= 0.18*inch
        
        return y - 0.2*inch  # Return starting y for questions
    
    def draw_question(c, q_num, problem, y_start):
        """Draw a single question with working space."""
        y = y_start
        
        # Question number and difficulty
        c.setFont("Helvetica-Bold", 10)
        c.drawString(left_margin, y, f"Q{q_num}. [{problem['difficulty']}] ")
        
        # Question text (wrapped)
        question_x = left_margin + 0.6*inch
        c.setFont("Helvetica", 10)
        y = draw_wrapped_text(c, problem['question'], question_x, y, 
                             max_width=content_width - 0.7*inch, 
                             line_height=0.18*inch, font_size=10)
        
        # Subpathway (smaller, lighter)
        y -= 0.05*inch
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColorRGB(0.4, 0.4, 0.4)
        y = draw_wrapped_text(c, f"Skill: {problem['subpathway']}", 
                             question_x + 0.1*inch, y, 
                             max_width=content_width - 0.8*inch, 
                             line_height=0.15*inch, font_size=8)
        c.setFillColorRGB(0, 0, 0)
        
        # Working space label
        y -= 0.15*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(question_x, y, "Working:")
        
        # Working space box
        y -= 0.15*inch
        working_height = 0.6*inch
        c.rect(question_x, y - working_height, content_width - 0.8*inch, working_height)
        
        # Answer box
        y -= working_height + 0.15*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(question_x, y, "Answer: ")
        c.setFont("Helvetica", 10)
        c.drawString(question_x + 0.6*inch, y, problem['answer_format'])
        
        # Separator line
        y -= 0.25*inch
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.line(left_margin, y, width - right_margin, y)
        c.setStrokeColorRGB(0, 0, 0)
        
        return y - 0.1*inch
    
    # Page 1: Header + Questions 1-8
    y = draw_header()
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS[:8], 1):
        y = draw_question(c, i, problem, y)
        
        # Check if we need a new page
        if y < bottom_margin + 1*inch and i < 8:
            c.showPage()
            y = height - top_margin
    
    # Page 2: Questions 9-17
    c.showPage()
    y = height - top_margin
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width/2, y, "Baseline Assessment Test - Page 2")
    y -= 0.4*inch
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS[8:17], 9):
        y = draw_question(c, i, problem, y)
        
        if y < bottom_margin + 1*inch and i < 17:
            c.showPage()
            y = height - top_margin
    
    # Page 3: Questions 18-25
    c.showPage()
    y = height - top_margin
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width/2, y, "Baseline Assessment Test - Page 3")
    y -= 0.4*inch
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS[17:25], 18):
        y = draw_question(c, i, problem, y)
        
        if y < bottom_margin + 1*inch and i < 25:
            c.showPage()
            y = height - top_margin
    
    # Optional: Answer sheet page
    if include_answer_sheet:
        c.showPage()
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width/2, height - top_margin, "Answer Sheet")
        
        c.setFont("Helvetica", 10)
        c.drawCentredString(width/2, height - top_margin - 0.3*inch, 
                           "For marker use only - Students do not write on this page")
        
        y = height - top_margin - 0.8*inch
        c.setFont("Helvetica-Bold", 10)
        c.drawString(left_margin, y, "Q#  |  Student Answer  |  Correct Answer  |  Marks")
        c.line(left_margin, y - 0.1*inch, width - right_margin, y - 0.1*inch)
        
        y -= 0.3*inch
        c.setFont("Courier", 9)
        
        # Sample answer key (would be populated with actual answers)
        for i in range(1, 26):
            c.drawString(left_margin, y, f"Q{i:2d} | _________________ | _________________ | ___/2")
            y -= 0.22*inch
            
            if y < bottom_margin + 0.5*inch and i < 25:
                c.showPage()
                y = height - top_margin
    
    # Footer on all pages
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(width/2, bottom_margin - 0.2*inch, 
                       f"ATOM-SG Pilot MVP • Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} • Page {c.getPageNumber()}")
    
    c.save()
    print(f"✓ Generated full baseline test PDF: {output_path}")
    print(f"  - Total questions: 25")
    print(f"  - Total pages: ~4 (including answer sheet)")
    print(f"  - Difficulty distribution: A={sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='A')}, "
          f"B={sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='B')}, "
          f"C={sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='C')}, "
          f"D={sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='D')}")


def generate_persona_answer_key(persona_name: str, accuracy: float) -> dict:
    """
    Generate an answer key for a specific persona with given accuracy.
    
    Args:
        persona_name: Name of the persona
        accuracy: Target accuracy (0.0 to 1.0)
    
    Returns:
        Dictionary with answers and working quality for each question
    """
    import random
    random.seed(persona_name)  # Reproducible for same persona
    
    # Define correct answers (simplified - would need actual solutions)
    correct_answers = {
        "G001": {"angles": [60, 80, 40]},  # Example values
        "G002": 105,
        "G003": 155,
        "G004": [40, 140, 140],
        "G005": 60,
        "G006": "marked",
        "G007": 20,
        "G008": 270,
        "G009": 26,
        "G010": "depends_on_diagram",
        "G011": "depends_on_diagram",
        "G012": "depends_on_diagram",
        "G013": [350, 2.5],
        "G014": 25000,
        "G015": 6,
        "G016": "drawn",
        "G017": 72,
        "G018": 3000,
        "G019": "selected",
        "G020": "drawn",
        "G021": "equilateral",
        "G022": "right-angled isosceles",
        "G023": "rhombus",
        "G024": 44,
        "G025": "1/4"
    }
    
    answer_key = {
        "persona": persona_name,
        "accuracy": accuracy,
        "answers": {},
        "working_quality": {},
        "time_estimate_minutes": 0
    }
    
    for problem in GEOMETRY_PROBLEMS:
        pid = problem["id"]
        is_correct = random.random() < accuracy
        
        answer_key["answers"][pid] = {
            "correct": is_correct,
            "difficulty": problem["difficulty"]
        }
        
        # Working quality varies by persona
        if accuracy > 0.9:
            answer_key["working_quality"][pid] = "detailed"
        elif accuracy > 0.7:
            answer_key["working_quality"][pid] = "adequate" if is_correct else "partial"
        elif accuracy > 0.5:
            answer_key["working_quality"][pid] = "minimal"
        else:
            answer_key["working_quality"][pid] = "none_or_wrong"
    
    # Time estimate based on accuracy
    if accuracy > 0.9:
        answer_key["time_estimate_minutes"] = 25
    elif accuracy > 0.7:
        answer_key["time_estimate_minutes"] = 35
    else:
        answer_key["time_estimate_minutes"] = 45
    
    return answer_key


if __name__ == "__main__":
    # Generate the full baseline test PDF
    output_dir = Path(__file__).parent / "artifacts" / "renders"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / "baseline_test_full_25_questions.pdf"
    generate_full_baseline_pdf(output_path)
    
    print("\n" + "="*60)
    print("BASELINE TEST PDF GENERATION COMPLETE")
    print("="*60)
