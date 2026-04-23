---
type: problem
problemID: P5-Problem-012
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Angle Chasing - Quadrilateral Angle Sum
difficulty: Medium
equationShadow: x + y + z + w = 360 (sum of angles in quadrilateral)
traps: Visual-Linguistic Mismatch (students might try to divide into triangles without recognizing the quadrilateral property)
visualNotes: |
  Diagram: Irregular quadrilateral ABCD with three angles given.
  - Draw an irregular quadrilateral (not a square, rectangle, or parallelogram)
  - Angle A (top left) = 95°
  - Angle B (top right) = 110°
  - Angle C (bottom right) = 85°
  - Students need to find angle D (bottom left)

  TikZ code:
  \begin{tikzpicture}[scale=1.8]
    \coordinate (A) at (-1,1.2);
    \coordinate (B) at (1.5,1);
    \coordinate (C) at (1,-0.8);
    \coordinate (D) at (-1.2,-0.5);

    \draw[thick] (A) -- (B) -- (C) -- (D) -- (A);

    \node[above left] at (A) {A};
    \node[above right] at (B) {B};
    \node[below right] at (C) {C};
    \node[below left] at (D) {D};

    % Angle marks
    \draw (-0.75,1.15) arc (10:100:0.2);
    \node at (-0.5,1.4) {$95^\circ$};

    \draw (1.3,0.85) arc (140:190:0.2);
    \node at (1.1,0.6) {$110^\circ$};

    \draw (0.85,-0.65) arc (260:350:0.2);
    \node at (0.6,-0.4) {$85^\circ$};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculation: 360° - 95° - 110° - 85° = 70°
  - Correct answer: 70°
  - Recognition that quadrilateral angle sum is 360°
  - Alternative: Drawing diagonal to split into two triangles (180° + 180° = 360°)
notes: |
  Medium-level problem testing quadrilateral angle sum property.
  Students may know triangle sum (180°) but need to extend to quadrilateral (360°).

  Solution reasoning:
  1. Recognize the figure is a quadrilateral (4-sided polygon)
  2. Sum of interior angles in a quadrilateral = 360°
  3. Three angles given: 95°, 110°, 85°
  4. Sum of given angles = 95° + 110° + 85° = 290°
  5. Angle D = 360° - 290° = 70°

  Alternative derivation:
  1. Draw a diagonal from A to C, splitting the quadrilateral into two triangles
  2. Each triangle has angle sum 180°
  3. Total angle sum = 180° + 180° = 360°
  4. Therefore angle D = 360° - (95° + 110° + 85°) = 70°

  Recognition skill taught: The sum of interior angles in a quadrilateral is 360° (can be derived from two triangles).
---
