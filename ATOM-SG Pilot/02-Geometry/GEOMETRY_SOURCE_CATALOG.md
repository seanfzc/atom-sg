# Geometry Source Catalog
## Extracted from ACS Junior 2025 Prelim Exam

**Date:** 2026-04-19  
**Purpose:** Document source materials for accurate diagram reconstruction

---

## Source Images

| Q# | ATOM-SG ID | Source | Description | Status |
|----|------------|--------|-------------|--------|
| Q15 | Q21 | ACS_Q15_overlapping_circles.png | Overlapping quarter circles OAC & OBD | ✅ Extracted & Specified |
| Q9 | Q22 | ACS_Q9_grid_triangle.png | Grid construction - triangle ABC | ✅ Extracted |
| Q5 | Q23 | ACS_Q5_3D_solid.png | 3D isometric solid (8 cubes) | ✅ Extracted |
| Q13 | Q24 | ACS_Q13_rhombus_trapezium.png | Rhombus ABCD + Trapezium ADEF | ✅ Extracted |
| Q12 | Q25 | ACS_Q12_five_squares.png | Five squares in rectangle | ✅ Extracted |

---

## Q21: Overlapping Quarter Circles (COMPLETE)

**Source:** ACS Junior Q15  
**Status:** ✅ Fully specified and verified

### Visual Analysis
- Center O at bottom
- Two quarter circles: OAC and OBD (both centered at O)
- Shaded sector OBC in the middle
- Points A, B, C, D on outer arc

### Coordinate Specification
```yaml
points:
  O: [0, 0]
  A: [10*cos(150°), 10*sin(150°)] = [-8.66, 5]
  B: [10*cos(120°), 10*sin(120°)] = [-5, 8.66]
  C: [10*cos(60°), 10*sin(60°)] = [5, 8.66]
  D: [10*cos(30°), 10*sin(30°)] = [8.66, 5]

quarter_circles:
  Q1_OAC:
    center: O
    radius: 10
    start_angle: 60°
    end_angle: 150°
  Q2_OBD:
    center: O
    radius: 10
    start_angle: 30°
    end_angle: 120°

shaded_sector_OBC:
  center: O
  radius: 10
  start_angle: 60°
  end_angle: 120°
  angle_span: 60°
  given_area: 30 cm²
  given_perimeter: 26 cm
```

### Verification
- Arc BC = 6 cm (from perimeter: 26 - 10 - 10 = 6)
- Area OBC = ½ × r × arc = ½ × 10 × 6 = 30 cm² ✓
- Area OABCD = 2 × (¼ × π × 10²) - 30 = 127 cm²
- Perimeter OABCD = 2 × (30° arcs) + 2 × 10 = 30.5 cm

---

## Q22: Grid Construction (PENDING SPEC)

**Source:** ACS Junior Q9  
**Status:** ⏳ Image extracted, needs coordinate spec

### Visual Analysis
- Square grid with 1cm precision
- Triangle ABC already drawn
- Point A at top-left, B at bottom, C at right
- Task: Complete trapezium BCDE

### Requirements
- Measure angle ACB
- Draw DE parallel to BC
- AB = BE
- DE = 2 × BC

---

## Q23: 3D Solid (PENDING SPEC)

**Source:** ACS Junior Q5  
**Status:** ⏳ Image extracted, needs coordinate spec

### Visual Analysis
- Isometric view of 8 cubes
- Top View, Front View, Side View arrows
- Grid provided for drawing front view
- Task: Draw front view, find max cubes to add

### Requirements
- Isometric projection with 3 visible faces
- Orthographic views (front, side, top)
- Grid construction

---

## Q24: Angle Chasing (PENDING SPEC)

**Source:** ACS Junior Q13  
**Status:** ⏳ Image extracted, needs coordinate spec

### Visual Analysis
- Rhombus ABCD
- Trapezium ADEF attached to side AD
- Multiple angles labeled: 21°, 108°, 33°
- Variables x and y to find

### Given Angles
- Angle at F: 21°
- Angle BCD: 108°
- Angle DAB: 33°
- Find: angle x and angle y

---

## Q25: Five Squares (PENDING SPEC)

**Source:** ACS Junior Q12  
**Status:** ⏳ Image extracted, needs coordinate spec

### Visual Analysis
- Rectangle containing 5 squares
- Square X = 4 cm side
- Square Y smaller than X
- Shaded leftover region on right
- 1.5 cm leftover breadth given

### Requirements
- Find side of square Y
- Find length of rectangle
- Calculate cubes from 2cm squares

---

## Next Steps

1. **Create YAML specs** for Q22-Q25 following Q21 format
2. **Verify mathematically** each specification
3. **Generate rendering code** for each diagram
4. **Produce final diagrams** matching exam quality

---

## Agent Instructions

When extracting geometry from exam papers:

1. **Always extract source image first**
2. **Identify ALL labeled points**
3. **Measure/estimate coordinates**
4. **Verify mathematically before finalizing**
5. **Document in YAML format**
6. **Test render and compare to source**

See `GEOMETRY_EXTRACTION_FRAMEWORK.md` for complete process.
