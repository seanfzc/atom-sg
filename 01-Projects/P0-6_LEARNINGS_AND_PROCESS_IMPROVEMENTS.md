# P0-6 Learnings & Process Improvements

**Generated:** 2026-04-16 15:30 GMT+8
**From:** P0-6 Visual-Text Mismatches Review + Manual Spot Check
**Purpose:** Capture systemic issues and prevent repetition in future diagram generation/review cycles

---

## 🔍 Issues Missed by Automated/Text-Based Review

### 1. **Visual Placement Ambiguity (G017)**
**Issue:** Height label `h=3` placed in "no-man's-land" – not visually connected to cuboid depth dimension.
**Why ReviewBot Missed It:** Text-based review checked for label presence (`h=3`) but cannot assess visual placement relative to geometry.
**Root Cause:** `generate_renders.py` placed label at mathematical center of back rectangle instead of adjacent to depth dimension line.

**Learning:** Labels must be visually associated with the dimension they represent, not just mathematically correct.

### 2. **Missing Geometric Elements (G001-G003, G007, G008)**
**Issue:** Angle diagrams show arcs but **missing rays** – angles require two intersecting lines to be measurable.
**Why ReviewBot Missed It:** SVG contained angle arcs and labels, but systematic text extraction couldn't identify missing geometric primitives.
**Root Cause:** `draw_angle_diagram()` function drew arcs but omitted radial lines.

**Learning:** Diagrams must include all geometric elements referenced in the problem text (rays for angles, not just arcs).

### 3. **Visual Proportion vs. Label (G025)**
**Issue:** Pie chart sector labeled 90° but visually appeared larger.
**Why ReviewBot Missed It:** Could verify label text but not visual proportion.
**Root Cause:** Matplotlib rendering may have rounding/visual distortion.

**Learning:** Visual proportions must be validated, not just label text.

---

## 🚨 Systemic Gaps in Review Process

### Gap 1: **Text-Only Review Cannot Catch Visual Design Issues**
- Labels can be present but poorly placed
- Geometric elements can be missing despite correct labels
- Visual proportions can mismatch numeric labels

### Gap 2: **No Visual QA Checklist for Diagram Generation**
- Render script lacks validation of visual associations
- No automated checks for label placement relative to geometry
- No verification that all referenced elements are visually present

### Gap 3: **Human Spot-Check Required for Visual Design**
- Automated review insufficient for visual learning considerations
- Must involve human visual inspection, especially for 11-year-old learner perspective

---

## ✅ Process Improvements (Immediate)

### 1. **Enhanced Diagram Generation Checklist** (Add to `generate_renders.py`)
```python
# VISUAL QA CHECKS (to be implemented)
# 1. Angle diagrams: Must have two rays + arc
# 2. Dimension labels: Must be adjacent to dimension line with arrow/connection
# 3. Unit labels: Must be explicit (not just numbers)
# 4. Visual proportions: Angles/sides must match labeled values within ±5° visual tolerance
# 5. Shape correspondence: Diagram shape must match text description
```

### 2. **Updated Review Checklist** (Add to `P0-6_TRACKING_TEMPLATE.md`)
**New Category: "Visual-Geometric Completeness"**
- [ ] Angle diagrams include both rays (lines) and arc
- [ ] Dimension labels visually connected to dimension (arrow, adjacent placement)
- [ ] Labels positioned to avoid ambiguity (not in "no-man's-land")
- [ ] Visual proportions match labeled values (eyeball test)
- [ ] All geometric elements referenced in text are visually present

### 3. **Mandatory Human Visual Spot-Check Step**
**Process:** After automated review, human must:
1. Open 5 random diagrams (20% sample)
2. Verify visual associations (labels → geometry)
3. Check for missing geometric elements
4. Confirm proportions look correct

**Sampling Strategy:**
- At least 1 diagram from each category (angles, area, volume, properties)
- Focus on problems cited in UX test (Brianna, Ivy, Kevin findings)

---

## 🔧 Technical Fixes Needed

### 1. **Update `draw_angle_diagram()` Function**
```python
# Current: draws arcs only
# Fix: Add radial lines for each angle
for angle_val, label in angles:
    # Draw ray 1
    ax.plot([0, np.cos(np.radians(current_angle))], 
            [0, np.sin(np.radians(current_angle))], 
            color=COLORS['line'], linewidth=1.5)
    # Draw ray 2  
    ax.plot([0, np.cos(np.radians(current_angle + angle_val))],
            [0, np.sin(np.radians(current_angle + angle_val))],
            color=COLORS['line'], linewidth=1.5)
    # Draw arc (existing)
    arc = patches.Arc((0, 0), 1.2, 1.2, angle=current_angle, theta1=0, theta2=angle_val,
                     linewidth=2, edgecolor=COLORS['primary'])
    ax.add_patch(arc)
```

### 2. **Update `draw_cuboid()` Label Placement**
```python
# Current: label at center of back rectangle
ax.text(1.5 + dimensions[0]/2 + offset, 1 + dimensions[1]/2 + offset,
        f"h={dimensions[2]}", ha='center', fontsize=10, color=COLORS['text'])

# Fix: label adjacent to depth dimension line with arrow
ax.annotate(f"h={dimensions[2]}", 
           xy=(1 + dimensions[0]/2 + offset/2, 1 + dimensions[1]/2 + offset/2),
           xytext=(1.5 + dimensions[0] + offset, 1 + dimensions[1]/2 + offset),
           arrowprops=dict(arrowstyle='->', color=COLORS['text'], lw=1),
           fontsize=10, color=COLORS['text'])
```

### 3. **Add Visual QA Function to Render Script**
```python
def validate_diagram_visuals(problem_id, diagram_type, ax):
    """Validate visual aspects of generated diagram."""
    warnings = []
    
    if diagram_type == 'angle-diagram':
        # Check for rays (count line objects)
        line_count = len([obj for obj in ax.get_children() 
                         if isinstance(obj, matplotlib.lines.Line2D)])
        if line_count < 2:  # Need at least 2 rays for an angle
            warnings.append(f"{problem_id}: Missing rays in angle diagram")
    
    if diagram_type in ['cuboid', 'rectangle', 'composite-shape']:
        # Check label placement relative to bounds
        # Implementation depends on specific diagram structure
    
    return warnings
```

---

## 📊 Future Prevention Metrics

### Success Criteria for Next Review Cycle:
- **0** instances of labels in "no-man's-land"
- **0** angle diagrams missing rays
- **100%** of diagrams pass human visual spot-check
- **<5%** of issues require rework after review

### Monitoring:
- Track issues by category (visual placement, missing elements, proportion)
- Measure time spent on visual rework vs. initial generation
- Sample human spot-check satisfaction score (1-5 scale)

---

## 🎯 Key Principle for Future Work

**"If an 11-year-old visual learner (Brianna, Ivy, Kevin) can't immediately understand which label goes with which geometric element, the diagram fails."**

### Implementation Rule:
Every diagram must pass the **5-second visual association test**:
1. Open diagram
2. Identify labeled elements within 5 seconds
3. No ambiguity about what each label refers to

---

## ✅ Action Items

### Immediate (Before Pilot Launch):
1. [ ] Update `generate_renders.py` with angle rays and label placement fixes
2. [ ] Add visual QA checklist to review template
3. [ ] Implement human spot-check step in review process
4. [ ] Regenerate all 25 diagrams with fixes

### Medium-term (Post-Pilot):
1. [ ] Implement automated visual QA in render script
2. [ ] Create diagram validation test suite
3. [ ] Add visual proportion verification (angle/side measurement)
4. [ ] Develop learner-focused diagram guidelines

---

**Last Updated:** 2026-04-16 15:30 GMT+8  
**Owner:** Diagram Generation Team  
**Review Frequency:** Before each major release