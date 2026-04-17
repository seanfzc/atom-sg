---
type: problem
problemID: P5-Problem-006
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Composite Figures - Square Perimeter
difficulty: Easy
equationShadow: Perimeter = 4 × side (multiplication by 4)
traps: Visual-Linguistic Mismatch (students might calculate area instead of perimeter)
visualNotes: |
  Diagram: Square with side length labeled.
  - Draw a square
  - Each side = 6 cm
  - Students need to find the perimeter

  TikZ code:
  \begin{tikzpicture}[scale=1]
    \draw[thick] (0,0) rectangle (6,6);

    \node[below] at (3,0) {6 cm};
    \node[left] at (0,3) {6 cm};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculation: 6 × 4 = 24
  - Correct answer: 24 cm
  - Distinction from area (not 36 cm²)
notes: |
  Foundation-level problem testing square perimeter.
  The key skill is recognizing the question asks for perimeter, not area.

  Solution reasoning:
  1. Identify the shape: square
  2. Question asks for perimeter (distance around the shape)
  3. Perimeter of a square = 4 × side length
  4. Side length = 6 cm
  5. Perimeter = 4 × 6 = 24 cm
  6. Note: Perimeter is in cm, not cm²

  Recognition skill taught: Perimeter is the distance around a shape (1D measurement), area is the space inside (2D measurement).
---