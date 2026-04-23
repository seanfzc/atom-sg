---
type: problem
problemID: P5-Problem-013
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Composite Figures - Shaded Region
difficulty: Medium
equationShadow: Area_shaded = Area_large - Area_small (subtraction of areas)
traps: Visual-Linguistic Mismatch (students might calculate total area instead of shaded area, or confuse radius and diameter)
visualNotes: |
  Diagram: Square with a circle inscribed, find shaded area (square minus circle).
  - Draw a square with side length 10 cm
  - Draw a circle inscribed in the square (touches all four sides)
  - Shade the region between the square and the circle (the four corner regions)
  - Students need to find the shaded area

  TikZ code:
  \begin{tikzpicture}[scale=0.5]
    % Square
    \draw[thick] (0,0) rectangle (10,10);
    
    % Inscribed circle
    \draw[thick,fill=gray!30] (5,5) circle (5);
    
    % Actually, shade the corners, not the circle
    % Redraw with proper shading
    \begin{scope}
      \clip (0,0) rectangle (10,10);
      \fill[gray!30] (0,0) rectangle (10,10);
      \fill[white] (5,5) circle (5);
    \end{scope}
    
    \draw[thick] (0,0) rectangle (10,10);
    \draw[thick] (5,5) circle (5);

    % Labels
    \node[below] at (5,0) {10 cm};
    \node[left] at (0,5) {10 cm};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculation:
    - Area of square = 10 × 10 = 100 cm²
    - Radius of circle = 10 ÷ 2 = 5 cm
    - Area of circle = π × 5² = 25π ≈ 78.5 cm² (using π = 3.14)
    - Shaded area = 100 - 78.5 = 21.5 cm²
  - Correct answer: 100 - 25π cm² or approximately 21.5 cm² (accept 21-22 cm²)
  - Clear identification that diameter = side length of square
notes: |
  Medium-level problem testing area of composite shaded region.
  Requires understanding that inscribed circle diameter equals square side.

  Solution reasoning:
  1. Identify the shape: square with inscribed circle
  2. Shaded region = Area of square - Area of circle
  3. Area of square = side × side = 10 × 10 = 100 cm²
  4. For inscribed circle: diameter = side of square = 10 cm
  5. Radius = diameter ÷ 2 = 5 cm
  6. Area of circle = π × r² = π × 25 = 25π cm²
  7. Using π = 3.14: Area of circle ≈ 78.5 cm²
  8. Shaded area = 100 - 78.5 = 21.5 cm²

  Common errors:
  - Using radius = 10 cm instead of 5 cm
  - Calculating only the circle area
  - Forgetting to square the radius

  Recognition skill taught: For a circle inscribed in a square, the circle's diameter equals the square's side length.
---
