---
type: problem
problemID: P5-Problem-015
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - 3D Visualization - Cube Face Identification
difficulty: Medium
equationShadow: N/A (spatial reasoning)
traps: Visual-Linguistic Mismatch (students must mentally unfold or rotate the cube)
visualNotes: |
  Diagram: Net of a cube with numbered faces, asking which numbers are opposite each other.
  - Draw a cube net (cross shape: center square with one on each side)
  - Label faces with numbers 1-6
  - Layout: 1 on top, 2 left, 3 center, 4 right, 5 bottom, 6 attached to 4
  - Question: "When folded into a cube, which number is opposite 3? Which is opposite 1?"

  TikZ code:
  \begin{tikzpicture}[scale=1]
    % Cube net - cross pattern
    %     [1]
    % [2] [3] [4] [6]
    %     [5]
    
    % Face 3 (center)
    \draw[thick] (0,0) rectangle (1,1);
    \node at (0.5,0.5) {3};
    
    % Face 1 (top)
    \draw[thick] (0,1) rectangle (1,2);
    \node at (0.5,1.5) {1};
    
    % Face 2 (left)
    \draw[thick] (-1,0) rectangle (0,1);
    \node at (-0.5,0.5) {2};
    
    % Face 4 (right)
    \draw[thick] (1,0) rectangle (2,1);
    \node at (1.5,0.5) {4};
    
    % Face 5 (bottom)
    \draw[thick] (0,-1) rectangle (1,0);
    \node at (0.5,-0.5) {5};
    
    % Face 6 (right of 4)
    \draw[thick] (2,0) rectangle (3,1);
    \node at (2.5,0.5) {6};
  \end{tikzpicture}
expectedArtifacts:
  - Student's identification of opposite faces:
    - Opposite 3: 6
    - Opposite 1: 5
    - Opposite 2: 4
  - Reasoning showing understanding that opposite faces don't share edges in the net
  - Possibly a sketch showing how the cube folds
notes: |
  Medium-level problem testing spatial visualization of 3D nets.
  Students must mentally fold the 2D net into a 3D cube.

  Solution reasoning:
  Key rule: In a cube net, faces that are opposite each other:
  1. Do not share an edge in the net
  2. Have exactly one face between them in a row/column of four

  For this net:
  - Row: 2-3-4-6: faces 2 and 4 are opposite (one face between), 3 and 6 are opposite
  - Column: 1-3-5: faces 1 and 5 are opposite

  Verification:
  - Face 3 is center, face 6 is at the end → opposite
  - Face 1 is above 3, face 5 is below 3 → opposite
  - Face 2 is left of 3, face 4 is right of 3 → opposite

  Common errors:
  - Thinking adjacent faces in the net are opposite
  - Confusing which faces meet at edges vs. which are opposite

  Recognition skill taught: In a cube net, opposite faces are separated by one face in any row or column of four squares.
---
