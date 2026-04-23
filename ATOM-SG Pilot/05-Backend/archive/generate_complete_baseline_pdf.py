#!/usr/bin/env python3
"""
Generate complete 40-question baseline test PDF for ATOM-SG Pilot.
20 Word Problems + 12 Geometry + 8 Data Interpretation = 40 questions
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import yaml
import re

# Load Word Problems
def load_word_problems():
    """Load all WP problems."""
    wp_dir = Path(__file__).parent.parent / "03-WordProblems" / "problems"
    problems = []
    for prob_file in sorted(wp_dir.glob("WP*.md")):
        with open(prob_file, 'r') as f:
            content = f.read()
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if match:
            try:
                metadata = yaml.safe_load(match.group(1))
                body = match.group(2).strip()
                problems.append({
                    'id': metadata.get('problemID', ''),
                    'pathwayType': metadata.get('pathwayType', ''),
                    'difficulty': metadata.get('difficulty', 'Medium'),
                    'question': metadata.get('question', body[:100]),
                    'answer': metadata.get('answer', ''),
                    'type': 'Word Problem'
                })
            except Exception as e:
                print(f"Error parsing {prob_file}: {e}")
    return problems

# Load Geometry Problems (select 12 from 25)
def load_geometry_problems():
    """Load 12 selected geometry problems."""
    geo_dir = Path(__file__).parent.parent / "02-Geometry" / "problems"
    # Select 12 representative problems covering all sub-pathways
    selected = ['G001', 'G002', 'G005', 'G007', 'G009', 'G010', 'G011', 'G014', 'G017', 'G019', 'G021', 'G024']
    problems = []
    for pid in selected:
        prob_file = geo_dir / f"{pid}.md"
        if prob_file.exists():
            with open(prob_file, 'r') as f:
                content = f.read()
            match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
            if match:
                try:
                    metadata = yaml.safe_load(match.group(1))
                    problems.append({
                        'id': pid,
                        'pathwayType': f"Geometry - {metadata.get('subpathway', 'General')}",
                        'difficulty': metadata.get('notes', 'Zone B').split('Zone ')[1][:1] if 'Zone' in metadata.get('notes', '') else 'B',
                        'question': metadata.get('problem', ''),
                        'answer': 'See rubric',
                        'type': 'Geometry'
                    })
                except Exception as e:
                    print(f"Error parsing {prob_file}: {e}")
    return problems

# Load Data Interpretation Problems
def load_di_problems():
    """Load 8 Data Interpretation problems."""
    di_dir = Path(__file__).parent.parent / "01-Projects" / "Baseline"
    problems = []
    for prob_file in sorted(di_dir.glob("P5-Problem-02*.md")):
        with open(prob_file, 'r') as f:
            content = f.read()
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if match:
            try:
                metadata = yaml.safe_load(match.group(1))
                notes = metadata.get('notes', '')
                # Extract question from notes
                question = notes.split('\n')[0] if notes else 'Data interpretation problem'
                problems.append({
                    'id': metadata.get('problemID', ''),
                    'pathwayType': metadata.get('pathwayType', 'Data Interpretation'),
                    'difficulty': metadata.get('difficulty', 'Medium')[:1],
                    'question': question[:200],
                    'answer': 'See expected artifacts',
                    'type': 'Data Interpretation'
                })
            except Exception as e:
                print(f"Error parsing {prob_file}: {e}")
    return problems

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
    word_probs = load_word_problems()
    geo_probs = load_geometry_problems()
    di_probs = load_di_problems()
    
    print(f"Loaded: {len(word_probs)} Word, {len(geo_probs)} Geometry, {len(di_probs)} DI")
    
    # Combine all problems
    all_problems = word_probs + geo_probs + di_probs
    
    if len(all_problems) != 40:
        print(f"WARNING: Expected 40 problems, got {len(all_problems)}")
    
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
        
        # Question header
        c.setFont("Helvetica-Bold", 8)
        diff = problem.get('difficulty', 'M')[0]
        q_type = problem.get('type', '')[0]
        c.drawString(left_margin, y, f"Q{q_num:2d}. [{diff}] [{q_type}]")
        
        # Pathway (abbreviated)
        pathway = problem.get('pathwayType', '')
        pathway_short = pathway.replace('Before-After Change', 'BAC').replace('Part-Whole with Comparison', 'PWC').replace('Cross-Thread Collision', 'CTC').replace('Data Interpretation', 'DI').replace('Geometry - ', 'G-')[:30]
        c.setFont("Helvetica-Oblique", 7)
        c.setFillColorRGB(0.3, 0.3, 0.3)
        c.drawString(left_margin + 1.0*inch, y, pathway_short)
        c.setFillColorRGB(0, 0, 0)
        
        # Question text
        y -= 0.2*inch
        question = problem.get('question', '')[:250]  # Limit length
        c.setFont("Helvetica", 9)
        y = draw_wrapped_text(c, question, left_margin + 0.05*inch, y, 
                             max_width=content_width - 0.1*inch, 
                             line_height=0.15*inch, font_size=9)
        
        # Working space
        y -= 0.1*inch
        c.setFont("Helvetica-Bold", 7)
        c.drawString(left_margin + 0.05*inch, y, "Working:")
        y -= 0.12*inch
        working_height = 0.4*inch
        c.rect(left_margin + 0.05*inch, y - working_height, content_width - 0.15*inch, working_height)
        
        # Answer box
        y -= working_height + 0.1*inch
        c.setFont("Helvetica-Bold", 8)
        c.drawString(left_margin + 0.05*inch, y, "Answer: _________________________")
        
        # Separator
        y -= 0.15*inch
        c.setStrokeColorRGB(0.85, 0.85, 0.85)
        c.line(left_margin, y, width - right_margin, y)
        c.setStrokeColorRGB(0, 0, 0)
        
        return y - 0.06*inch
    
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
        ptype = prob.get('type', '')[0]
        pathway = prob.get('pathwayType', '')[:20]
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
    print(f"   Word Problems: {len(word_probs)}")
    print(f"   Geometry: {len(geo_probs)}")
    print(f"   Data Interpretation: {len(di_probs)}")

if __name__ == "__main__":
    output_dir = Path(__file__).parent / "artifacts" / "renders"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "ATOM-SG_Baseline_Test_40_Questions.pdf"
    generate_complete_baseline(output_path)
