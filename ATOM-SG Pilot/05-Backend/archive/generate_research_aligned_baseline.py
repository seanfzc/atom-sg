#!/usr/bin/env python3
"""
Generate baseline test PDF aligned with research phase.
Based on the 28 problems in 01-Projects/Baseline/ (20 Geometry + 8 Data Interpretation).
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from datetime import datetime
import re
import yaml

# Load all baseline problems from the research phase
BASELINE_PROBLEMS = []

def load_baseline_problems():
    """Load all P5 baseline problems from markdown files."""
    baseline_dir = Path(__file__).parent.parent / "01-Projects" / "Baseline"
    
    problems = []
    for prob_file in sorted(baseline_dir.glob("P5-Problem-*.md")):
        with open(prob_file, 'r') as f:
            content = f.read()
            
        # Extract YAML frontmatter
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if match:
            yaml_content = match.group(1)
            body = match.group(2)
            
            try:
                metadata = yaml.safe_load(yaml_content)
                problems.append({
                    'id': metadata.get('problemID', ''),
                    'type': metadata.get('type', ''),
                    'pathwayType': metadata.get('pathwayType', ''),
                    'difficulty': metadata.get('difficulty', ''),
                    'equationShadow': metadata.get('equationShadow', ''),
                    'traps': metadata.get('traps', ''),
                    'notes': metadata.get('notes', ''),
                    'body': body.strip()
                })
            except Exception as e:
                print(f"Error parsing {prob_file}: {e}")
    
    return problems


def draw_wrapped_text(c, text, x, y, max_width, line_height=0.2*inch, font_name="Helvetica", font_size=10):
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


def generate_research_aligned_baseline(output_path: Path) -> None:
    """
    Generate baseline test PDF with all 28 research-phase problems.
    20 Geometry + 8 Data Interpretation = 28 total questions
    """
    # Load problems
    problems = load_baseline_problems()
    
    if not problems:
        print("Warning: No problems loaded. Using fallback data.")
        problems = get_fallback_problems()
    
    print(f"Loaded {len(problems)} problems from research phase")
    
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
                           f"P6 Mathematics - Research Phase Aligned ({len(problems)} Questions)")
        
        # Student info box
        c.setFont("Helvetica-Bold", 10)
        c.drawString(left_margin, height - top_margin - 0.7*inch, 
                    "Name: _______________________________    Class: _______    Date: ___________")
        
        # Instructions
        c.setFont("Helvetica-Bold", 10)
        c.drawString(left_margin, height - top_margin - 1.1*inch, "Instructions:")
        c.setFont("Helvetica", 9)
        instructions = [
            f"• This test contains {len(problems)} questions: 20 Geometry + 8 Data Interpretation.",
            "• You have 50 minutes to complete the test.",
            "• Show all your working in the spaces provided.",
            "• Write your final answers in the boxes provided.",
            "• Calculators are NOT allowed.",
            "• Diagrams are NOT drawn to scale unless stated otherwise."
        ]
        y = height - top_margin - 1.3*inch
        for instruction in instructions:
            c.drawString(left_margin + 0.1*inch, y, instruction)
            y -= 0.18*inch
        
        return y - 0.2*inch
    
    def draw_question(c, q_num, problem, y_start):
        """Draw a single question with working space."""
        y = y_start
        
        # Question number and difficulty
        c.setFont("Helvetica-Bold", 9)
        difficulty = problem.get('difficulty', 'Medium')[:1]  # E, M, H
        pathway = problem.get('pathwayType', 'Unknown')
        c.drawString(left_margin, y, f"Q{q_num:2d}. [{difficulty}] ")
        
        # Pathway type (abbreviated)
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColorRGB(0.3, 0.3, 0.3)
        pathway_short = pathway.replace('Geometry - ', 'G-').replace('Data Interpretation - ', 'DI-')[:35]
        c.drawString(left_margin + 0.8*inch, y, pathway_short)
        c.setFillColorRGB(0, 0, 0)
        
        # Question text (from notes or body)
        y -= 0.25*inch
        question_text = extract_question_text(problem)
        
        c.setFont("Helvetica", 9)
        y = draw_wrapped_text(c, question_text, left_margin + 0.1*inch, y, 
                             max_width=content_width - 0.2*inch, 
                             line_height=0.16*inch, font_size=9)
        
        # Working space label
        y -= 0.15*inch
        c.setFont("Helvetica-Bold", 8)
        c.drawString(left_margin + 0.1*inch, y, "Working:")
        
        # Working space box
        y -= 0.15*inch
        working_height = 0.5*inch
        c.rect(left_margin + 0.1*inch, y - working_height, content_width - 0.3*inch, working_height)
        
        # Answer box
        y -= working_height + 0.12*inch
        c.setFont("Helvetica-Bold", 8)
        c.drawString(left_margin + 0.1*inch, y, "Answer: ")
        c.setFont("Helvetica", 9)
        c.drawString(left_margin + 0.6*inch, y, "_____________________")
        
        # Separator line
        y -= 0.18*inch
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.line(left_margin, y, width - right_margin, y)
        c.setStrokeColorRGB(0, 0, 0)
        
        return y - 0.08*inch
    
    # Page 1: Header + Questions 1-10
    y = draw_header()
    
    for i, problem in enumerate(problems[:10], 1):
        y = draw_question(c, i, problem, y)
        
        # Check if we need a new page
        if y < bottom_margin + 0.8*inch and i < 10:
            c.showPage()
            y = height - top_margin
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(width/2, y, "Baseline Assessment Test - Page 2")
            y -= 0.35*inch
    
    # Page 2: Questions 11-20
    if len(problems) > 10:
        c.showPage()
        y = height - top_margin
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(width/2, y, "Baseline Assessment Test - Page 2")
        y -= 0.35*inch
        
        for i, problem in enumerate(problems[10:20], 11):
            y = draw_question(c, i, problem, y)
            
            if y < bottom_margin + 0.8*inch and i < 20:
                c.showPage()
                y = height - top_margin
    
    # Page 3: Questions 21-28
    if len(problems) > 20:
        c.showPage()
        y = height - top_margin
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(width/2, y, "Baseline Assessment Test - Page 3")
        y -= 0.35*inch
        
        for i, problem in enumerate(problems[20:], 21):
            y = draw_question(c, i, problem, y)
            
            if y < bottom_margin + 0.8*inch and i < len(problems):
                c.showPage()
                y = height - top_margin
    
    # Answer sheet page
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - top_margin, "Answer Sheet")
    
    c.setFont("Helvetica", 9)
    c.drawCentredString(width/2, height - top_margin - 0.25*inch, 
                       "For marker use only - Students do not write on this page")
    
    y = height - top_margin - 0.6*inch
    c.setFont("Helvetica-Bold", 9)
    c.drawString(left_margin, y, "Q#  |  Student Answer  |  Correct  |  Pathway")
    c.line(left_margin, y - 0.08*inch, width - right_margin, y - 0.08*inch)
    
    y -= 0.2*inch
    c.setFont("Courier", 8)
    
    for i, problem in enumerate(problems, 1):
        pathway_short = problem.get('pathwayType', 'Unknown').replace('Geometry - ', 'G-').replace('Data Interpretation - ', 'DI-')[:20]
        c.drawString(left_margin, y, f"Q{i:2d} | _________________ | _________ | {pathway_short}")
        y -= 0.16*inch
        
        if y < bottom_margin + 0.3*inch and i < len(problems):
            c.showPage()
            y = height - top_margin
    
    # Footer on all pages
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(width/2, bottom_margin - 0.15*inch, 
                       f"ATOM-SG Pilot MVP • Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    c.save()
    print(f"✓ Generated research-aligned baseline PDF: {output_path}")
    print(f"  - Total questions: {len(problems)}")
    print(f"  - Geometry: {sum(1 for p in problems if 'Geometry' in p.get('pathwayType', ''))}")
    print(f"  - Data Interpretation: {sum(1 for p in problems if 'Data Interpretation' in p.get('pathwayType', ''))}")
    
    # Print pathway distribution
    pathway_counts = {}
    for p in problems:
        pt = p.get('pathwayType', 'Unknown')
        pathway_counts[pt] = pathway_counts.get(pt, 0) + 1
    
    print("\n  Pathway Distribution:")
    for pathway, count in sorted(pathway_counts.items()):
        print(f"    - {pathway}: {count}")


def extract_question_text(problem):
    """Extract a concise question text from the problem metadata."""
    # Try to get from notes
    notes = problem.get('notes', '')
    if notes:
        # Extract first sentence that looks like a question
        lines = notes.strip().split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('Solution') and not line.startswith('1.'):
                # Clean up the line
                line = line.replace('This is a foundation-level problem testing', 'Find')
                line = line.replace('The visual trap is', 'Note:')
                if len(line) > 20:
                    return line[:200]  # Limit length
    
    # Fallback to pathway type
    pathway = problem.get('pathwayType', 'Solve this problem')
    difficulty = problem.get('difficulty', '')
    
    return f"Solve this {difficulty} {pathway} problem. Show your working."


def get_fallback_problems():
    """Fallback problems if markdown files can't be loaded."""
    return [
        {"id": f"P5-Problem-{i:03d}", "pathwayType": "Geometry - Angle Chasing", "difficulty": "Easy"}
        for i in range(1, 21)
    ] + [
        {"id": f"P5-Problem-{i:03d}", "pathwayType": "Data Interpretation - Graphs", "difficulty": "Medium"}
        for i in range(21, 29)
    ]


if __name__ == "__main__":
    output_dir = Path(__file__).parent / "artifacts" / "renders"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / "baseline_test_research_aligned_28_questions.pdf"
    generate_research_aligned_baseline(output_path)
    
    print("\n" + "="*60)
    print("RESEARCH-ALIGNED BASELINE PDF GENERATION COMPLETE")
    print("="*60)
