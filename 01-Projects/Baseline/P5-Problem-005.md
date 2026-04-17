---
type: problem
problemID: P5-Problem-005
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Composite Figures - Rectangle Area
difficulty: Easy
equationShadow: Area = length × width (simple multiplication)
traps: Visual-Linguistic Mismatch (students might confuse length and width based on orientation)
visualNotes: |
  Diagram: Simple rectangle with dimensions labeled.
  - Draw a rectangle
  - Length (horizontal) = 8 cm
  - Width (vertical) = 5 cm
  - Students need to find the area

  TikZ code:
  \begin{tikzpicture}[scale=0.8]
    \draw[thick] (0,0) rectangle (8,5);

    \node[below] at (4,0) {8 cm};
    \node[rotate=90,above] at (0,2.5) {5 cm};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculation: 8 × 5 = 40
  - Correct answer: 40 cm²
  - Correct units (square centimeters)
notes: |
  Foundation-level problem testing rectangle area formula.
  Simple application with no traps except remembering units.

  Solution reasoning:
  1. Identify the shape: rectangle
  2. Area of a rectangle = length × width
  3. Length = 8 cm, Width = 5 cm
  4. Area = 8 × 5 = 40
  5. Remember to include units: cm²

  Recognition skill taught: Area = length × width for rectangles.
---