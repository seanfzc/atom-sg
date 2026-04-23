# Exam Paper Analysis Framework
## New Approach: Parametric + 4-Gates

**Date:** 2026-04-19  
**Purpose:** Analyze original exam PDFs using new rendering approach

---

## Analysis Process

### Step 1: Extract Question from PDF
- Locate question in exam paper
- Extract text and any existing diagram
- Note the question number and marks

### Step 2: Apply Gate 0 — Solve First
- Solve the problem completely
- Identify all variables and relationships
- Note the solution method (bar model, unitary, etc.)

### Step 3: Apply Gate 1 — Audience Check
- Target: P5-P6
- Remove any algebra or advanced concepts
- Ensure vocabulary is age-appropriate

### Step 4: Apply Gate 2 — Map Reasoning Chain
- Break solution into steps
- Identify what needs to be visual at each step
- Choose visual strategy (bar model, comparison, etc.)

### Step 5: Apply Gate 3 — Parametric Scale
- Define variables from question
- Plan scale for bars/shapes
- Ensure proportions are exact

### Step 6: Generate Parametric Diagram
- Use variable-driven rendering
- Apply collision detection for labels
- Verify against audit rules

---

## Source Exam Papers

| School | File | Status |
|--------|------|--------|
| ACS Junior | 2025-P6-Maths-Prelim Exam-ACS Junior.pdf | Images extracted |
| Henry Park | 2025-P6-Maths-Prelim Exam-Henry Park.pdf | Images extracted |
| Nan Hua | 2025-P6-Maths-Prelim Exam-Nan Hua.pdf | Images extracted |
| Nanyang | 2025-P6-Maths-Prelim Exam-Nanyang.pdf | Images extracted |
| Raffles Girls | 2025-P6-Maths-Prelim Exam-Raffles Girls.pdf | Images extracted |

**Total images extracted:** 171

---

## Geometry Questions to Analyze

From baseline test requirements:

### G1: Angle Reasoning (8 questions)
- Q21: Protractor measurement
- Q22: Grid construction
- Q26: Protractor angles
- Q27: Angles at point
- Q28: Vertically opposite
- Q29: Triangle angles
- Others from exam papers

### G2: Area & Perimeter (8 questions)
- Q25: Five squares
- Q30: L-shape
- Q31: Rectangle cut-out
- Others from exam papers

### G3: Volume & 3D (4 questions)
- Q23: 3D solid views
- Q32: Cuboid volume
- Others from exam papers

### G4: Properties (5 questions)
- Q24: Angle chasing
- Others from exam papers

### G5-G8: Advanced (from exam papers)
- Composite overlap
- Grid construction
- 3D visualization
- Angle chasing

---

## Data Interpretation Questions

### DI1: Line Graphs
- Q33: T-shirt sales
- Q34: Temperature
- Q39: Website traffic
- Q40: Plant growth

### DI2: Bar Graphs
- Q35: Books read
- Q36: Test scores

### DI3: Pie Charts
- Q37: Spending
- Q38: Fruit distribution

---

## Output Structure

For each analyzed question:

```yaml
question_id: "Q21"
source: "ACS Junior 2025 Q15"

analysis:
  gate_0_solution: "..."
  gate_1_audience_check: "..."
  gate_2_reasoning_chain:
    - step_1: "..."
    - step_2: "..."
  gate_3_parametric_vars:
    radius: 10
    arc_BC: 6
    # etc.

visual_strategy: "bar_model_panels" | "comparison" | "part_whole" | ...

parametric_diagram:
  type: "..."
  variables: {...}
  elements: [...]
  
verification:
  audit_passed: true/false
  notes: "..."
```

---

## Next Steps

1. Review extracted images from exam papers
2. Analyze each geometry/DI question
3. Create parametric deconstructed data
4. Generate new diagrams
5. Audit with MATH_DIAGRAM_AUDIT_INSTRUCTION.md
6. Build new baseline test PDF

---

*Framework for systematic exam paper analysis*
