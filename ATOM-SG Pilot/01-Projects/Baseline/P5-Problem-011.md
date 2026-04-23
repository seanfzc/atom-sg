---
type: problem
problemID: P5-Problem-011
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Composite Figures - L-Shape Area
difficulty: Medium
equationShadow: Area = (L × W) - (l × w) or Area = sum of rectangles (decomposition method)
traps: Temporal Misdirection (students must choose between subtraction method or decomposition method)
visualNotes: |
  Diagram: L-shaped figure composed of two rectangles.
  - Draw an L-shape: overall dimensions 10 cm × 8 cm
  - The L is formed by a large rectangle with a smaller rectangle removed from corner
  - OR: two rectangles joined together
  - Rectangle A: 10 cm × 5 cm (bottom part)
  - Rectangle B: 3 cm × 3 cm (vertical part on top left)
  - Students need to find total area

  TikZ code:
  \begin{tikzpicture}[scale=0.6]
    % L-shape drawn as two rectangles
    % Bottom rectangle: 10 x 5
    \draw[thick] (0,0) rectangle (10,5);
    % Top left extension: 3 x 3 on top of left part
    \draw[thick] (0,5) rectangle (3,8);

    % Dimension labels
    \node[below] at (5,0) {10 cm};
    \node[left] at (0,2.5) {5 cm};
    \node[left] at (0,6.5) {3 cm};
    \node[above] at (1.5,8) {3 cm};
    \node[right] at (10,2.5) {5 cm};

    % Total height indicator
    \draw[<->] (11,0) -- (11,8);
    \node[right] at (11,4) {8 cm};
  \end{tikzpicture}
expectedArtifacts:
  - Student's chosen method clearly shown:
    - Method 1 (Decomposition): Area = (10 × 5) + (3 × 3) = 50 + 9 = 59 cm²
    - Method 2 (Subtraction): Area = (10 × 8) - (7 × 3) = 80 - 21 = 59 cm²
  - Correct answer: 59 cm²
  - Clear labeling of which dimensions belong to which part
notes: |
  Medium-level problem testing area of composite L-shaped figure.
  Students can use either decomposition or subtraction method.

  Solution reasoning (Decomposition method):
  1. Divide the L-shape into two rectangles
  2. Rectangle 1 (bottom): 10 cm × 5 cm = 50 cm²
  3. Rectangle 2 (top left): 3 cm × 3 cm = 9 cm²
  4. Total area = 50 + 9 = 59 cm²

  Solution reasoning (Subtraction method):
  1. Enclose the L-shape in a large rectangle: 10 cm × 8 cm = 80 cm²
  2. The "missing" rectangle has dimensions: (10-3) cm × 3 cm = 7 cm × 3 cm = 21 cm²
  3. Total area = 80 - 21 = 59 cm²

  Recognition skill taught: Composite figures can be solved by either breaking them into simpler shapes (decomposition) or completing them to a larger shape and subtracting (subtraction method).
---
