---
type: problem
problemID: P5-Problem-019
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Angle Chasing - Multiple Triangles + Parallel Lines
difficulty: Hard
equationShadow: Multiple: x + y + z = 180, alternate angles, corresponding angles, vertically opposite angles (complex system)
traps: Temporal Misdirection (students must plan which angles to find first; multiple valid paths exist)
visualNotes: |
  Diagram: Complex figure with overlapping triangles and parallel lines.
  - Draw two parallel lines l1 (top) and l2 (bottom)
  - Draw triangle ABC with A on l1, B and C on l2
  - Draw another line from A intersecting BC at D and extending to E on l2
  - Given: angle BAE = 35°, angle ABC = 50°, angle ACB = 60°
  - Find: angle between the transversal and l2 at point E

  TikZ code:
  \begin{tikzpicture}[scale=1.5]
    % Parallel lines
    \draw[thick] (-1,2) -- (4,2) node[right] {$l_1$};
    \draw[thick] (-1,0) -- (4,0) node[right] {$l_2$};

    % Triangle vertices
    \coordinate (A) at (0.5,2);
    \coordinate (B) at (0,0);
    \coordinate (C) at (3,0);
    \coordinate (E) at (2.5,0);

    % Lines
    \draw[thick] (A) -- (B);
    \draw[thick] (A) -- (C);
    \draw[thick] (A) -- (E);

    % Labels
    \node[above] at (A) {A};
    \node[below] at (B) {B};
    \node[below] at (C) {C};
    \node[below] at (E) {E};
    \node[below] at (1.25,0) {D};

    % Angle marks
    \draw (0.7,2) arc (180:215:0.25);
    \node at (0.4,1.75) {$35^\circ$};

    \draw (0.15,0.2) arc (70:110:0.2);
    \node at (0.2,0.5) {$50^\circ$};

    \draw (2.7,0.2) arc (110:150:0.2);
    \node at (2.5,0.5) {$60^\circ$};
  \end{tikzpicture}
expectedArtifacts:
  - Student's multi-step solution showing:
    - Step 1: Find angle BAC = 180° - 50° - 60° = 70° (triangle sum)
    - Step 2: Find angle CAE = 70° - 35° = 35°
    - Step 3: Find angle AEC using triangle ADE or alternate angles
    - Or: Use alternate angles from l1 || l2
  - Correct answer: angle AEC = 85°
  - Clear reasoning chain connecting each step
notes: |
  Hard-level problem requiring multiple angle-chasing steps.
  Students must combine triangle angle sum with parallel line properties.

  Solution reasoning:
  Method 1 - Through triangle ABE:
  1. In triangle ABC: angle BAC = 180° - 50° - 60° = 70°
  2. Angle BAE = 35° (given), so angle EAC = 70° - 35° = 35°
  3. In triangle ABE: angle BAE = 35°, angle ABE = 50°
  4. Angle AEB = 180° - 35° - 50° = 95°
  5. Angle AEC = 180° - 95° = 85° (straight line)

  Method 2 - Using parallel lines:
  1. Draw auxiliary line through A parallel to BE... actually, let's verify Method 1

  Rechecking Method 1:
  - Triangle ABC: angles 50°, 60°, so angle BAC = 70° ✓
  - Point E is between B and C on line l2
  - So B, E, C are collinear on l2
  - In triangle ABE: angle BAE = 35°, angle ABE = 50°
  - Angle AEB = 180° - 35° - 50° = 95°
  - Angle AEC = 180° - 95° = 85° (linear pair) ✓

  Recognition skill taught: Complex angle problems require systematic application of triangle and parallel line properties, working step-by-step from known to unknown angles.
---
