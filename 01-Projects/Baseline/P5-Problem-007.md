---
type: problem
problemID: P5-Problem-007
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Grid Symmetry - Basic Reflection
difficulty: Easy
equationShadow: N/A (visual reflection, no equation)
traps: Visual-Linguistic Mismatch (students might reflect across wrong axis)
visualNotes: |
  Diagram: Simple shape on a grid with mirror line.
  - Draw a 6×6 grid
  - Draw a simple L-shape (like a tetris piece) on the left side
  - Draw a vertical dashed line through the center (mirror line)
  - Students need to draw the reflection of the L-shape

  TikZ code:
  \begin{tikzpicture}[scale=0.7]
    % Draw grid
    \draw[step=1cm,gray,very thin] (0,0) grid (6,6);

    % Draw L-shape (positions: (1,1), (1,2), (1,3), (2,3))
    \filldraw[fill=blue!30] (1,1) rectangle (2,2);
    \filldraw[fill=blue!30] (1,2) rectangle (2,3);
    \filldraw[fill=blue!30] (1,3) rectangle (2,4);
    \filldraw[fill=blue!30] (2,3) rectangle (3,4);

    % Draw mirror line
    \draw[dashed,red,thick] (3,0) -- (3,6);
    \node[red,above] at (3,6) {mirror line};
  \end{tikzpicture}
expectedArtifacts:
  - Student's drawn reflection on the right side of the mirror line
  - Reflected L-shape should be at positions (4,1), (4,2), (4,3), (3,3)
  - Mirror line used correctly
notes: |
  Foundation-level problem testing basic reflection symmetry.
  The skill is understanding that reflection flips the shape across the mirror line.

  Solution reasoning:
  1. Identify the mirror line (vertical dashed line at x=3)
  2. Count the distance from each part of the L-shape to the mirror line
  3. The reflected shape will be the same distance on the other side
  4. Original L-shape occupies: (1,1)-(2,2), (1,2)-(2,3), (1,3)-(2,4), (2,3)-(3,4)
  5. Mirror these positions across x=3:
     - (1,1) → (5,1), so reflected block at (4,1)-(5,2)
     - (1,2) → (5,2), so reflected block at (4,2)-(5,3)
     - (1,3) → (5,3), so reflected block at (4,3)-(5,4)
     - (2,3) → (4,3), so reflected block at (3,3)-(4,4)
  6. Draw the reflected L-shape

  Recognition skill taught: In reflection, each point moves the same distance to the other side of the mirror line.
---