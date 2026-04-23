#!/usr/bin/env python3
"""
Generate EXAM-QUALITY baseline test PDF with embedded diagrams.
Language matches Singapore PSLE standards - precise, unambiguous, exam-authentic.
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from datetime import datetime

# Setup paths
BASE_DIR = Path(__file__).parent
RENDERS_DIR = BASE_DIR / "artifacts" / "renders"
OUTPUT_DIR = BASE_DIR / "artifacts" / "renders"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# EXAM-QUALITY questions - linguistically precise like actual PSLE papers
GEOMETRY_PROBLEMS = [
    {
        "id": "G001",
        "question": "The diagram shows angles ∠AOB, ∠BOC and ∠COD.\n(a) Measure ∠AOB.\n(b) Measure ∠BOC.\n(c) Measure ∠COD.",
        "subpathway": "G1: Measure angles using protractor",
        "difficulty": "A",
        "marks": 3,
        "diagram": "G001-angle-diagram-v1.svg",
        "answer_format": "(a) _____° (b) _____° (c) _____°"
    },
    {
        "id": "G002",
        "question": "In the diagram, AOB is a straight line. ∠AOC = 75°.\nFind ∠COB.",
        "subpathway": "G1: Angles on a straight line",
        "difficulty": "B",
        "marks": 2,
        "diagram": "G002-angle-diagram-v1.svg",
        "answer_format": "∠COB = _____°"
    },
    {
        "id": "G003",
        "question": "In the diagram, three angles meet at point O.\n∠AOB = 120° and ∠BOC = 85°.\nFind ∠AOC.",
        "subpathway": "G1: Angles at a point",
        "difficulty": "B",
        "marks": 2,
        "diagram": "G003-angle-diagram-v1.svg",
        "answer_format": "∠AOC = _____°"
    },
    {
        "id": "G004",
        "question": "In the diagram, straight lines AB and CD intersect at O.\n∠AOC = 40°.\n(a) Find ∠AOD.\n(b) Find ∠BOD.\n(c) Find ∠BOC.",
        "subpathway": "G1: Vertically opposite angles",
        "difficulty": "B",
        "marks": 3,
        "diagram": "G004-angle-diagram-v1.svg",
        "answer_format": "(a) _____° (b) _____° (c) _____°"
    },
    {
        "id": "G005",
        "question": "In triangle ABC, ∠ABC = 50° and ∠BCA = 70°.\nFind ∠CAB.",
        "subpathway": "G1: Angle sum of triangle",
        "difficulty": "C",
        "marks": 2,
        "diagram": "G005-triangle-v1.svg",
        "answer_format": "∠CAB = _____°"
    },
    {
        "id": "G006",
        "question": "The diagram shows a figure with lines AB, CD and EF.\n(a) Identify one pair of perpendicular lines.\n(b) Identify one pair of parallel lines.",
        "subpathway": "G1: Parallel and perpendicular lines",
        "difficulty": "A",
        "marks": 2,
        "diagram": "G006-parallel-perpendicular-v1.svg",
        "answer_format": "(a) _____ ⊥ _____ (b) _____ ∥ _____"
    },
    {
        "id": "G007",
        "question": "In the diagram, AOB is a straight line.\n∠BOD = 90° and ∠AOC = 110°.\nFind ∠COD.",
        "subpathway": "G1: Combined angle properties",
        "difficulty": "D",
        "marks": 3,
        "diagram": "G007-angle-diagram-v1.svg",
        "answer_format": "∠COD = _____°"
    },
    {
        "id": "G008",
        "question": "The diagram shows angle ∠XOY which is reflex.\nMeasure and write down the size of the reflex angle ∠XOY.",
        "subpathway": "G1: Reflex angles",
        "difficulty": "C",
        "marks": 2,
        "diagram": "G008-angle-diagram-v1.svg",
        "answer_format": "Reflex ∠XOY = _____°"
    },
    {
        "id": "G009",
        "question": "The diagram shows rectangle ABCD.\nAB = 8 cm and BC = 5 cm.\nFind the perimeter of rectangle ABCD.",
        "subpathway": "G2: Perimeter of rectangle",
        "difficulty": "A",
        "marks": 2,
        "diagram": "G009-rectangle-v1.svg",
        "answer_format": "Perimeter = _____ cm"
    },
    {
        "id": "G010",
        "question": "The figure is made up of two rectangles.\nFind the perimeter of the figure.",
        "subpathway": "G2: Perimeter of composite figure",
        "difficulty": "B",
        "marks": 3,
        "diagram": "G010-composite-shape-v1.svg",
        "answer_format": "Perimeter = _____ cm"
    },
    {
        "id": "G011",
        "question": "The figure shows an L-shaped figure made up of two rectangles.\nFind the area of the figure.",
        "subpathway": "G2: Area of composite figure",
        "difficulty": "B",
        "marks": 3,
        "diagram": "G011-lshape-area-v1.svg",
        "answer_format": "Area = _____ cm²"
    },
    {
        "id": "G012",
        "question": "A rectangular sheet of paper measures 12 cm by 8 cm.\nA square of side 3 cm is cut from one corner as shown.\nFind the area of the remaining sheet.",
        "subpathway": "G2: Area with missing section",
        "difficulty": "C",
        "marks": 3,
        "diagram": "G012-cutout-rectangle-v1.svg",
        "answer_format": "Area = _____ cm²"
    },
    {
        "id": "G013",
        "question": "Fill in the blanks.\n(a) 3.5 m = __________ cm\n(b) 250 cm = __________ m\n(c) 4.2 km = __________ m",
        "subpathway": "G2: Unit conversion (length)",
        "difficulty": "A",
        "marks": 3,
        "diagram": None,
        "answer_format": "(a) _____ (b) _____ (c) _____"
    },
    {
        "id": "G014",
        "question": "Convert 2.5 m² to square centimetres.\n2.5 m² = __________ cm²",
        "subpathway": "G2: Unit conversion (area)",
        "difficulty": "B",
        "marks": 2,
        "diagram": None,
        "answer_format": "2.5 m² = _____ cm²"
    },
    {
        "id": "G015",
        "question": "The diagram shows a regular hexagon.\n(a) Draw all the lines of symmetry on the hexagon.\n(b) How many lines of symmetry does a regular hexagon have?",
        "subpathway": "G4: Symmetry",
        "difficulty": "A",
        "marks": 2,
        "diagram": "G015-hexagon-symmetry-v1.svg",
        "answer_format": "(b) _____ lines"
    },
    {
        "id": "G016",
        "question": "The diagram shows half of a symmetrical figure.\nThe dotted line is the line of symmetry.\nComplete the symmetrical figure.",
        "subpathway": "G4: Complete symmetrical figure",
        "difficulty": "C",
        "marks": 3,
        "diagram": "G016-symmetry-complete-v1.svg",
        "answer_format": "(Draw on diagram)"
    },
    {
        "id": "G017",
        "question": "The diagram shows a cuboid.\nLength = 6 cm, Breadth = 4 cm, Height = 3 cm.\nFind the volume of the cuboid.",
        "subpathway": "G3: Volume of cuboid",
        "difficulty": "A",
        "marks": 2,
        "diagram": "G017-cuboid-v1.svg",
        "answer_format": "Volume = _____ cm³"
    },
    {
        "id": "G018",
        "question": "A box measures 0.5 m by 30 cm by 200 mm.\nFind the volume of the box in cubic centimetres.",
        "subpathway": "G3: Volume with unit conversion",
        "difficulty": "B",
        "marks": 3,
        "diagram": "G018-cuboid-v1.svg",
        "answer_format": "Volume = _____ cm³"
    },
    {
        "id": "G019",
        "question": "Which of the following nets can be folded to form a cube?\nCircle the letter(s) of the correct answer(s).",
        "subpathway": "G3: Nets of cube",
        "difficulty": "C",
        "marks": 2,
        "diagram": "G019-cube-nets-v1.svg",
        "answer_format": "Answer: _____"
    },
    {
        "id": "G020",
        "question": "The diagram shows a cuboid on an isometric grid.\nDraw a net of the cuboid on the grid provided.",
        "subpathway": "G3: Draw net of cuboid",
        "difficulty": "D",
        "marks": 4,
        "diagram": "G020-cuboid-net-v1.svg",
        "answer_format": "(Draw on grid)"
    },
    {
        "id": "G021",
        "question": "The diagram shows triangle ABC.\nAB = 5 cm, BC = 5 cm and CA = 5 cm.\nWhat type of triangle is ABC?",
        "subpathway": "G4: Classify triangle by sides",
        "difficulty": "A",
        "marks": 1,
        "diagram": "G021-triangle-classification-v1.svg",
        "answer_format": "_____ triangle"
    },
    {
        "id": "G022",
        "question": "Triangle PQR has angles 45°, 45° and 90°.\nWhat type of triangle is PQR?",
        "subpathway": "G4: Classify triangle by angles",
        "difficulty": "A",
        "marks": 1,
        "diagram": "G022-triangle-angles-v1.svg",
        "answer_format": "_____ triangle"
    },
    {
        "id": "G023",
        "question": "The diagram shows quadrilateral PQRS.\nPQ ∥ SR, PS ∥ QR and PQ = QR = RS = SP.\nHowever, ∠PQR ≠ 90°.\nWhat type of quadrilateral is PQRS?",
        "subpathway": "G4: Classify quadrilateral",
        "difficulty": "B",
        "marks": 2,
        "diagram": "G023-quadrilateral-v1.svg",
        "answer_format": "_____"
    },
    {
        "id": "G024",
        "question": "The diagram shows a circle with centre O.\nThe radius of the circle is 7 cm.\nFind the circumference of the circle.\n(Take π = 22/7)",
        "subpathway": "G2: Circumference of circle",
        "difficulty": "C",
        "marks": 2,
        "diagram": "G024-circle-v1.svg",
        "answer_format": "Circumference = _____ cm"
    },
    {
        "id": "G025",
        "question": "The pie chart shows how a student spends 24 hours in a day.\nThe angle of the 'Sleep' sector is 90°.\nWhat fraction of the day does the student spend sleeping?\n(Give your answer in the simplest form.)",
        "subpathway": "G2: Pie chart as fraction",
        "difficulty": "D",
        "marks": 3,
        "diagram": "G025-pie-chart-v1.svg",
        "answer_format": "Fraction = _____"
    }
]


def draw_wrapped_text(c, text, x, y, max_width, line_height=0.18*inch, font_name="Helvetica", font_size=10):
    """Draw text with word wrapping and return new y position."""
    c.setFont(font_name, font_size)
    lines = text.split('\n')
    
    for line in lines:
        words = line.split()
        wrapped_lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, font_name, font_size) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    wrapped_lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            wrapped_lines.append(' '.join(current_line))
        
        for wrapped_line in wrapped_lines:
            c.drawString(x, y, wrapped_line)
            y -= line_height
    
    return y


def embed_diagram(c, diagram_filename, x, y, max_width=3.2*inch, max_height=2*inch):
    """Embed a diagram image into the PDF."""
    if not diagram_filename:
        return y
    
    base_name = diagram_filename.replace('.svg', '').replace('.png', '').replace('.pdf', '')
    
    # Try PNG first (best compatibility)
    for ext in ['.png', '.pdf', '.svg']:
        diagram_path = RENDERS_DIR / (base_name + ext)
        if diagram_path.exists():
            try:
                if ext == '.png':
                    from PIL import Image
                    with Image.open(diagram_path) as img:
                        img_width, img_height = img.size
                        aspect = img_height / img_width
                        
                        draw_width = min(max_width, img_width * 0.15)  # Scale down
                        draw_height = draw_width * aspect
                        
                        if draw_height > max_height:
                            draw_height = max_height
                            draw_width = max_height / aspect
                    
                    c.drawImage(str(diagram_path), x, y - draw_height, 
                               width=draw_width, height=draw_height)
                    return y - draw_height - 0.08*inch
                    
                elif ext == '.pdf':
                    c.drawImage(str(diagram_path), x, y - max_height, 
                               width=max_width, height=max_height)
                    return y - max_height - 0.08*inch
                    
            except Exception as e:
                print(f"Warning: Could not embed {diagram_path}: {e}")
    
    # Fallback
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColorRGB(0.6, 0.6, 0.6)
    c.drawString(x, y - 0.15*inch, f"[Diagram: {base_name}]")
    c.setFillColorRGB(0, 0, 0)
    return y - 0.25*inch


def generate_exam_quality_baseline():
    """Generate exam-quality baseline test PDF."""
    
    output_path = OUTPUT_DIR / "ATOM-SG_Baseline_Test_EXAM_QUALITY_25Q.pdf"
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    
    # Margins
    lm = 0.55 * inch
    rm = 0.55 * inch
    tm = 0.5 * inch
    bm = 0.5 * inch
    cw = width - lm - rm
    
    def draw_header():
        c.setFont("Helvetica-Bold", 15)
        c.drawCentredString(width/2, height - tm, "ATOM-SG Baseline Assessment Test")
        
        c.setFont("Helvetica", 10)
        c.drawCentredString(width/2, height - tm - 0.2*inch, 
                           "Primary 6 Mathematics — Geometry Track")
        
        c.setFont("Helvetica-Bold", 9)
        y = height - tm - 0.5*inch
        c.drawString(lm, y, "Name: _________________________________")
        c.drawString(lm + 3.3*inch, y, "Class: _______")
        c.drawString(lm + 4.6*inch, y, "Date: ___________")
        
        c.setFont("Helvetica-Bold", 9)
        y -= 0.35*inch
        c.drawString(lm, y, "Instructions:")
        c.setFont("Helvetica", 8.5)
        instructions = [
            "• This paper consists of 25 questions. Time allowed: 45 minutes.",
            "• Show all your working clearly in the spaces provided.",
            "• Marks may be awarded for correct method even if answer is wrong.",
            "• Calculators are NOT allowed.",
            "• Diagrams are NOT drawn to scale unless stated otherwise."
        ]
        y -= 0.16*inch
        for instruction in instructions:
            c.drawString(lm + 0.08*inch, y, instruction)
            y -= 0.14*inch
        
        return y - 0.1*inch
    
    def draw_question(c, q_num, problem, y_start):
        y = y_start
        
        # Check page break
        min_space = 2.3*inch if problem.get("diagram") else 1.4*inch
        if y < bm + min_space:
            c.showPage()
            y = height - tm - 0.2*inch
            c.setFont("Helvetica-Bold", 11)
            c.drawCentredString(width/2, y, "Baseline Assessment Test — Continued")
            y -= 0.3*inch
        
        # Question header
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(lm, y, f"Q{q_num}. [{problem['difficulty']}] [{problem['marks']}m]")
        
        # Question text
        question_x = lm + 0.5*inch
        c.setFont("Helvetica", 9.5)
        y = draw_wrapped_text(c, problem['question'], question_x, y - 0.02*inch, 
                             max_width=cw - 0.55*inch, line_height=0.155*inch, font_size=9.5)
        
        # Subpathway (small, grey)
        y -= 0.03*inch
        c.setFont("Helvetica-Oblique", 7)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        y = draw_wrapped_text(c, problem['subpathway'], question_x + 0.05*inch, y, 
                             max_width=cw - 0.6*inch, line_height=0.12*inch, font_size=7)
        c.setFillColorRGB(0, 0, 0)
        
        # Diagram
        if problem.get("diagram"):
            y -= 0.06*inch
            y = embed_diagram(c, problem["diagram"], lm + 0.25*inch, y)
        
        # Working space
        y -= 0.1*inch
        c.setFont("Helvetica-Bold", 8)
        c.drawString(question_x, y, "Working:")
        y -= 0.13*inch
        wh = 0.48*inch
        c.rect(question_x, y - wh, cw - 0.6*inch, wh)
        
        # Answer
        y -= wh + 0.1*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(question_x, y, "Ans: ")
        c.setFont("Helvetica", 9.5)
        c.drawString(question_x + 0.35*inch, y, problem['answer_format'])
        
        # Separator
        y -= 0.18*inch
        c.setStrokeColorRGB(0.75, 0.75, 0.75)
        c.line(lm, y, width - rm, y)
        c.setStrokeColorRGB(0, 0, 0)
        
        return y - 0.06*inch
    
    # Generate pages
    y = draw_header()
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS[:9], 1):
        y = draw_question(c, i, problem, y)
    
    c.showPage()
    y = height - tm - 0.15*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(width/2, y, "Baseline Assessment Test — Page 2")
    y -= 0.28*inch
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS[9:17], 10):
        y = draw_question(c, i, problem, y)
    
    c.showPage()
    y = height - tm - 0.15*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(width/2, y, "Baseline Assessment Test — Page 3")
    y -= 0.28*inch
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS[17:25], 18):
        y = draw_question(c, i, problem, y)
    
    # Answer key
    c.showPage()
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(width/2, height - tm, "Answer Key — For Markers Only")
    c.setFont("Helvetica", 8)
    c.drawCentredString(width/2, height - tm - 0.2*inch, "DO NOT DISTRIBUTE")
    
    y = height - tm - 0.55*inch
    c.setFont("Helvetica-Bold", 8)
    c.drawString(lm, y, "Q#  |  Answer  |  Subpathway")
    c.line(lm, y - 0.06*inch, width - rm, y - 0.06*inch)
    
    y -= 0.18*inch
    c.setFont("Courier", 7.5)
    for i, problem in enumerate(GEOMETRY_PROBLEMS, 1):
        ans = problem['answer_format'][:32] + "..." if len(problem['answer_format']) > 32 else problem['answer_format']
        path = problem['subpathway'][:28] + "..." if len(problem['subpathway']) > 28 else problem['subpathway']
        c.drawString(lm, y, f"Q{i:2d} | {ans:35} | {path:30} | {problem['marks']}m")
        y -= 0.115*inch
        if y < bm + 0.2*inch and i < 25:
            c.showPage()
            y = height - tm - 0.2*inch
    
    # Footer
    c.setFont("Helvetica-Oblique", 7)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawCentredString(width/2, bm - 0.12*inch, 
                       f"ATOM-SG Pilot MVP • Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    c.setFillColorRGB(0, 0, 0)
    
    c.save()
    
    total_marks = sum(p['marks'] for p in GEOMETRY_PROBLEMS)
    with_diagrams = sum(1 for p in GEOMETRY_PROBLEMS if p.get('diagram'))
    
    print(f"\n{'='*65}")
    print("EXAM-QUALITY BASELINE TEST GENERATED")
    print(f"{'='*65}")
    print(f"File: {output_path}")
    print(f"Questions: 25 | Marks: {total_marks} | With diagrams: {with_diagrams}/25")
    print(f"Difficulty: A={sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='A')} | "
          f"B={sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='B')} | "
          f"C={sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='C')} | "
          f"D={sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='D')}")
    print(f"{'='*65}\n")
    
    return output_path


if __name__ == "__main__":
    generate_exam_quality_baseline()