---
type: problem
problemID: P5-Problem-018
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Grid Symmetry - Identifying Lines of Symmetry
difficulty: Medium
equationShadow: N/A (visual identification and drawing)
traps: Visual-Linguistic Mismatch (students might miss diagonal lines of symmetry or count the same line twice)
visualNotes: |
  Diagram: Complex shape on a grid with multiple possible lines of symmetry.
  - Draw a shape on a grid that has 2 lines of symmetry (e.g., a rectangle or rhombus pattern)
  - Or draw a shape with only 1 line of symmetry
  - Students need to identify and draw ALL lines of symmetry

  TikZ code:
  \begin{tikzpicture}[scale=0.7]
    % Grid 6x6
    \draw[step=1cm,gray,very thin] (0,0) grid (6,6);
    
    % Draw a shape with 2 lines of symmetry (rectangle pattern)
    % A filled rectangle from (1,2) to (5,4)
    \filldraw[fill=blue!30] (1,2) rectangle (5,4);
    
    % Add some detail to make it interesting - pattern inside
    % Small squares at corners
    \filldraw[fill=white] (1.2,2.2) rectangle (1.8,2.8);
    \filldraw[fill=white] (4.2,2.2) rectangle (4.8,2.8);
    \filldraw[fill=white] (1.2,3.2) rectangle (1.8,3.8);
    \filldraw[fill=white] (4.2,3.2) rectangle (4.8,3.8);

    % Question: Draw all lines of symmetry
  \end{tikzpicture}
expectedArtifacts:
  - Student's identification of lines of symmetry:
    - Horizontal line through y=3 (middle of rectangle)
    - Vertical line through x=3 (middle of rectangle)
  - Correct drawing of both lines on the diagram
  - Recognition that the shape has 2 lines of symmetry (not 4, since it's not a square)
notes: |
  Medium-level problem testing identification of lines of symmetry.
  The shape is a rectangle pattern with 2 lines of symmetry (not 4).

  Solution reasoning:
  1. A line of symmetry divides a shape into two mirror-image halves
  2. For this rectangular shape:
     - Horizontal line through the center (y=3): top half mirrors bottom half ✓
     - Vertical line through the center (x=3): left half mirrors right half ✓
     - Diagonal lines: corners don't match (white squares in corners prevent diagonal symmetry) ✗
  3. Total lines of symmetry: 2

  Common errors:
  - Drawing diagonal lines of symmetry (only valid for squares or specific shapes)
  - Missing one of the symmetry lines
  - Drawing lines that don't pass through the center

  Recognition skill taught: Regular shapes have predictable lines of symmetry; irregular patterns within shapes may reduce the number of symmetry lines.
---
