---
type: problem
problemID: P5-Problem-008
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - 3D Visualization - Simple Cuboid Counting
difficulty: Easy
equationShadow: N/A (counting task)
traps: Visual-Linguistic Mismatch (students might miscount hidden cubes)
visualNotes: |
  Diagram: 3×2×1 arrangement of unit cubes shown as isometric drawing.
  - Draw a 3D arrangement: 3 cubes in front row, 3 cubes in back row
  - Each cube is a unit cube (1 cm³)
  - Students need to count total number of cubes and find volume

  TikZ code (isometric):
  \begin{tikzpicture}[scale=1.5]
    % Back row
    \draw[thick] (0,1) -- (1,1.5) -- (2,1) -- (1,0.5) -- cycle;
    \draw[thick] (1,1.5) -- (1,0.5);

    % Middle cube back row
    \draw[thick] (1,1.5) -- (2,2) -- (3,1.5) -- (2,1) -- cycle;
    \draw[thick] (2,2) -- (2,1);

    % Third cube back row
    \draw[thick] (2,2) -- (3,2.5) -- (4,2) -- (3,1.5) -- cycle;
    \draw[thick] (3,2.5) -- (3,1.5);

    % Front row (offset down-right)
    \draw[thick] (1,0.5) -- (2,1) -- (3,0.5) -- (2,0) -- cycle;
    \draw[thick] (2,1) -- (2,0);

    % Middle cube front row
    \draw[thick] (2,1) -- (3,1.5) -- (4,1) -- (3,0.5) -- cycle;
    \draw[thick] (3,1.5) -- (3,0.5);

    % Third cube front row
    \draw[thick] (3,1.5) -- (4,2) -- (5,1.5) -- (4,1) -- cycle;
    \draw[thick] (4,2) -- (4,1);
  \end{tikzpicture}
expectedArtifacts:
  - Student's count: 6 cubes
  - Correct answer: 6 cm³ volume
  - Understanding that each unit cube has volume 1 cm³
notes: |
  Foundation-level problem testing 3D visualization and counting.
  Students must recognize this is a 3×2×1 arrangement from the isometric view.

  Solution reasoning:
  1. Identify this is an isometric view of a 3D arrangement
  2. Count the cubes: 3 in back row, 3 in front row = 6 total
  3. Each cube is a unit cube with volume 1 cm³
  4. Total volume = 6 × 1 cm³ = 6 cm³
  5. Alternatively: dimensions are 3 × 2 × 1 = 6 cm³

  Recognition skill taught: Isometric drawings show 3D shapes; count visible cubes and infer hidden ones systematically.
---