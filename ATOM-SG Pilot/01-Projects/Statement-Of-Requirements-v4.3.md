---
title: Statement of Requirements (C0) – Pilot v4.3 (Internal Deconstruction & Reconstruction)
objective: Define internal deconstruction pipeline and reconstruction quality requirements.
status: draft — comprehensive stock-taking of existing assets
owner: Zcaethbot → Sean Foo (approval pending)
last_updated: 2026-04-21 07:55 SGT
directive_source: OPENCLAW DIRECTIVE – PILOT v4.1 (Recognition-First Integrated Training)
quality_standard: Quality of reconstruction data must match original exam questions; deconstructed data must enable improvisation during transfer testing without obvious human errors and be solvable using both visual and text information.
---

# Statement of Requirements – ATOM‑SG Pilot v4.3

## Executive Summary

**This SOR takes a fundamentally different approach than v4.1/v4.2.**

Instead of "adding" Vision LLM to the existing system, we must:
1. **Take stock of everything built** — What do we have that's actually working?
2. **Identify issues and root causes** — What went wrong and why?
3. **Define what stays vs. what needs revision** — Clear separation
4. **Establish internal deconstruction pipeline** — No more external processing
5. **Define reconstruction quality standard** — Match to original exam questions
6. **Enable improvisation during transfer testing** — Deconstructed data must support this

**Critical Insight from Sean Foo:**
> "We deconstructed exam data outside of OpenClaw and this resulted in reconstruction deficits. We have no choice but to do it internally. Consequence is we are unable to establish veracity of existing MVP."

---

## 1. Taking Stock — What Do We Have?

### 1.1 External Data (Deconstructed Outside OpenClaw)

| Asset | Location | Format | Quality Issue |
|-------|----------|--------|---------------|
| **5 Exam Papers (PDF)** | `~/Desktop/neo_output/` | Original source — GOOD |
| **Deconstructed Questions (Markdown)** | `~/Desktop/neo_output/*.md` | Human-readable, not machine-parseable — CANNOT RECONSTRUCT |
| **Pathway Classifications** | Embedded in markdown | Inconsistent — REVISION REQUIRED |
| **Equation Shadows** | Embedded in markdown | Good structure — CAN KEEP |
| **Visual Notes** | Mixed (text descriptions, some TikZ) | Inconsistent — REVISION REQUIRED |
| **Extracted Images** | `~/Desktop/neo_output/extracted_images/` | PNG/JPG — GOOD SOURCE |

**Root Cause of Quality Issues:**
- Deconstruction was **manual** (human analysis, not Vision LLM)
- Output format is **markdown**, not **structured YAML**
- No **machine-readable visual data** (coordinates, angles, dimensions)
- No **confidence scores** on any extraction
- Cannot **verify reconstruction fidelity** — no baseline to compare against

### 1.2 Internal Data (Built Within OpenClaw)

| Asset | Location | Status | Verdict |
|-------|----------|--------|---------|
| **28 P5 Problem Cards** | `01-Projects/Baseline/P5-Problem-*.md` | ✅ Created | KEEP — Good structure |
| **25 Geometry Problems (G001-G025)** | `02-Geometry/problems/G*.md` | ✅ Created | KEEP — Good structure |
| **20 Word Problems (WP001-WP020)** | `03-WordProblems/problems/WP*.md` | ✅ Created | KEEP — Good structure |
| **Geometry Taxonomy (18 Nano-Nodes)** | `Geometry_Taxonomy_NanoNodes.md` | ✅ Created | KEEP — Approved by Sean |
| **Geometry Rubrics** | `02-Geometry/Geometry-Rubrics.md` | ✅ Created | KEEP — Good framework |
| **Rubric Mapping** | `02-Geometry/Geometry-Rubric-Mapping.md` | ✅ Created | KEEP — 25 problems mapped |
| **Baseline PDF Generator** | `05-Backend/generate_full_baseline_pdf.py` | ✅ Working | KEEP — Functional |
| **Backend API (19 Endpoints)** | `05-Backend/main.py` | ✅ Implemented | KEEP — Functional |
| **Frontend (Static HTML/JS)** | `05-Backend/frontend/` | ✅ Implemented | KEEP — Functional |
| **33 Bug Fixes** | Multiple files | ✅ Complete | KEEP — Verified |
| **90 Playwright Tests** | `05-Backend/playwright-tests/` | ✅ Passing | KEEP — Good coverage |
| **Action Verification Tests** | `05-Backend/playwright-tests/tests/action-verification.spec.ts` | ✅ Created | KEEP — Addresses START HERE bug |

**What Works:**
- ✅ **Data structure** — Markdown format for problems (problem, pathway, shadow, notes)
- ✅ **Backend API** — All 19 endpoints functional
- ✅ **Frontend UI** — Recognition-first loop, forced articulation, triad feedback
- ✅ **Testing** — 90 tests passing, action verification
- ✅ **Bug Fixes** — 33 fixes applied (P0, P1, P2)
- ✅ **Documentation** — SOR, MVP, KANBAN, Coordination Log

**What Doesn't Work:**
- ❌ **Deconstruction Pipeline** — External markdown cannot reconstruct
- ❌ **Visual Reconstruction** — Basic matplotlib/tikZ, no pixel precision
- ❌ **Quality Verification** — No baseline to compare against
- ❌ **Exam-Quality Diagrams** — Missing isometric 3D, grid precision, composite overlap

### 1.3 Vision LLM Documentation (Received 2026-04-21)

| Asset | Location | Purpose | Status |
|-------|----------|---------|--------|
| **00-overview.md** | Inbound/ | File index, architecture | ✅ Reviewed — Good structure |
| **01-rendering-gates.md** | Inbound/ | 5 gates before rendering | ✅ Reviewed — Universal rules |
| **02-label-arrow-rules.md** | Inbound/ | Label placement, arrow types, dimension lines | ✅ Reviewed — Precise rules |
| **03-audit-protocol.md** | Inbound/ | Audit stages, severity, output format | ✅ Reviewed — QA framework |
| **architecture.md** | Inbound/ | 3-layer pipeline, source priority | ✅ Reviewed — Core architecture |
| **ocr-setup.md** | Inbound/ | RapidOCR, EasyOCR, Tesseract comparison | ✅ Reviewed — Tool selection |
| **opencv-analysis.md** | Inbound/ | Geometric analysis functions | ✅ Reviewed — Pixel precision |
| **validation.md** | Inbound/ | Confidence thresholds, re-extraction | ✅ Reviewed — Quality gate |
| **types/*.md (11 files)** | Inbound/ | Diagram-specific rules | ✅ Reviewed — Complete coverage |

**Total:** 20 files, ~6,500 words, covering extraction, validation, rendering, audit.

**Verdict:** ✅ **KEEP AND IMPLEMENT** — This is the solution to our reconstruction deficit.

---

## 2. Issues Encountered & Root Causes

### 2.1 Issue #1: Baseline Test Rendering Quality Crisis

**Symptoms:**
- Missing diagrams (Q35, Q37 had none)
- Visual quality: Basic matplotlib plots, no geometric precision
- Linguistic complexity: 5.2/10 (exams require 10-12/10)
- v2.0 improvements (+83% word count) still not exam-quality

**Root Cause:**
- Deconstruction was **external** (markdown in `~/Desktop/neo_output/`)
- No **machine-readable visual data** (coordinates, angles, dimensions)
- Rendering from **text descriptions only** (no precision)
- No **quality verification loop** (reconstruct → compare → refine)

**Impact:**
- ❌ Cannot establish veracity of existing MVP
- ❌ Cannot generate exam-quality diagrams
- ❌ Cannot verify reconstruction fidelity

### 2.2 Issue #2: Testing Infrastructure Failure

**Symptoms:**
- 90 tests passing but START HERE button routing to dashboard
- Test named `clickPrintBaseline()` never actually clicked
- False confidence from passing tests masked critical bug
- 3 days lost to bug that should have been caught immediately

**Root Cause:**
- Tests only checked **HTML structure**, not **actual click behavior**
- No **action verification tests** (tests that actually click and verify outcomes)
- Misleading test names created false sense of security

**Impact:**
- ❌ Hands-on validation failed (student experience broken)
- ❌ Had to add 15 action verification tests
- ❌ Delayed pilot launch

**Fix Applied:**
- ✅ Action verification tests created (`action-verification.spec.ts`)
- ✅ Auto-fix system deployed
- ✅ START HERE button fixed

**Status:** ✅ **RESOLVED**

### 2.3 Issue #3: Framework Coverage Gap

**Symptoms:**
- Only 40% of exam content covered by current framework
- Missing G5-G8 geometry pathways (composite overlap, grid construction, 3D viz, angle chasing)
- No formal Data Interpretation pathway

**Root Cause:**
- External deconstruction only identified 67-71.3% coverage
- Manual analysis missed complex pathways
- No systematic nano-node taxonomy

**Impact:**
- ❌ Baseline test doesn't cover full exam content
- ❌ Students won't be trained on critical missing pathways

**Fix Applied:**
- ✅ Geometry taxonomy created (18 nano-nodes)
- ✅ Framework gap analysis documented
- ✅ Recommendations for expansion

**Status:** 🟡 **PARTIALLY RESOLVED** — Deconstruction pipeline needed to identify remaining gaps

### 2.4 Issue #4: Missing Word Problems (20 WP)

**Symptoms:**
- Baseline test had only Geometry + Data Interpretation
- 20 Word Problems missing despite being required in SOR v4.1

**Root Cause:**
- Directory structure inconsistency (no dedicated WordProblems folder)
- Assumption that `01-Projects/Baseline/` contained word problems
- No content manifest to verify all 40 questions present

**Impact:**
- ❌ Incomplete baseline test
- ❌ Delayed PDF generation

**Fix Applied:**
- ✅ Created 20 Word Problems (WP001-WP020)
- ✅ Updated `03-WordProblems/README.md`
- ✅ Documented lesson learned

**Status:** ✅ **RESOLVED**

### 2.5 Issue #5: Quality Verification Gap

**Symptoms:**
- v2.0 baseline test improvements still not exam-quality
- Independent QA revealed issues automation missed
- No clear quality standard or verification process

**Root Cause:**
- No **deconstruction → reconstruction loop**
- No **independent QA** before deeming "complete"
- No **explicit quality standard** (what does "exam-quality" mean?)

**Impact:**
- ❌ Cannot verify reconstruction fidelity
- ❌ Launch with sub-quality materials
- ❌ Pilot failure risk

**Fix Required:**
- ❌ **Internal deconstruction pipeline** (Vision LLM 3-layer)
- ❌ **Quality verification process** (audit protocol)
- ❌ **Reconstruction fidelity measurement** (match to original)

**Status:** ❌ **NOT RESOLVED** — BLOCKING

---

## 3. What Stays vs. What Needs Revision

### 3.1 What Stays (Good Assets)

| Asset | Why It Stays | Notes |
|-------|--------------|-------|
| **Problem Card Structure (Markdown)** | Good format, human-readable | Keep `problem`, `pathwayType`, `equationShadow`, `notes` structure |
| **Backend API (19 Endpoints)** | Functional, tested, verified | Keep all endpoints, no changes needed |
| **Frontend UI (Static HTML/JS)** | Recognition-first loop works | Keep all UI, forced articulation, triad feedback |
| **Geometry Taxonomy (18 Nano-Nodes)** | Approved by Sean, good coverage | Keep as foundation for pathway classification |
| **Geometry Rubrics** | Good framework | Keep rubric structure, update with new pathways if needed |
| **Playwright Tests (90 tests)** | Good coverage, verified | Keep all tests, add Vision LLM verification tests |
| **Action Verification Tests (15 tests)** | Addresses START HERE bug | Keep as model for future behavioral tests |
| **Bug Fixes (33 fixes)** | Verified, working | Keep all fixes |
| **OCR Pipeline (Tesseract 5.5.2)** | Tested, ready for production | Keep as Layer 1 of Vision LLM pipeline |

### 3.2 What Needs Revision (Problematic Assets)

| Asset | Why Revision Needed | Revision Approach |
|-------|------------------|-----------------|
| **External Deconstructed Questions (`~/Desktop/neo_output/*.md`)** | Markdown format, not machine-parseable, no visual data | **REDUCE**: Extract insights (pathway classifications, equation shadows), discard structure |
| **External Visual Notes** | Inconsistent, text descriptions only, no precision | **DISCARD**: Re-deconstruct using Vision LLM pipeline |
| **External Pathway Classifications** | Manual, inconsistent, no confidence | **RE-VERIFY**: Re-classify using Vision LLM, keep as reference |
| **Basic Rendering (matplotlib/tikZ)** | No pixel precision, no isometric 3D, no composite overlap | **REPLACE**: Use Vision LLM rendering rules (gates, label rules, geometry rules) |
| **Baseline PDF Generator (v2.0)** | Renders from markdown, no visual data | **UPDATE**: Generate from Vision LLM YAML output, not markdown |
| **Quality Verification Process** | No deconstruction → reconstruction loop | **CREATE**: Implement audit protocol with confidence thresholds |

### 3.3 What Needs Creation (Missing Assets)

| Asset | Purpose | Implementation |
|-------|---------|----------------|
| **Internal Deconstruction Pipeline** | Extract exam data to structured YAML with visual precision | Vision LLM 3-layer: OCR + Vision LLM + OpenCV |
| **YAML Schema for Each Problem Type** | Machine-parseable data format with coordinates, angles, dimensions | Based on `types/*.md` files, add confidence scores |
| **Automated Validation System** | Check confidence thresholds, structural integrity | Based on `validation.md`, implement `validate_yaml.py` |
| **Exam-Quality Rendering Engine** | Render from YAML with pixel precision | Based on `01-rendering-gates.md`, `02-label-arrow-rules.md`, `03-audit-protocol.md` |
| **Quality Verification Loop** | Deconstruct → Render → Audit → Compare to Original → Refine | Implement as automated pipeline with manual QA gate |
| **Reconstruction Fidelity Measurement** | Quantify match between reconstructed output and original | Pixel comparison, semantic comparison, completeness check |
| **94 Exam Questions Deconstructed (Internal)** | Source data for baseline test pack + transfer test | Use Vision LLM pipeline on all 5 exam papers |
| **Reconstructed Baseline Test Pack** | 40 questions with exam-quality visuals | Generate from internal deconstruction, verify fidelity |

---

## 4. Internal Deconstruction Pipeline (New)

### 4.1 Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  5 Exam PDFs  │────▶│  RapidOCR     │────▶│  Vision LLM   │────▶│  OpenCV        │──▶│  YAML Output  │
│  (Original)    ├─────┤   ├───────┤   ├─────┤   ├─────┤   │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
                              Layer 1                Layer 2                Layer 3              Tagged
```

**Layer 1: OCR (RapidOCR)**
- Input: Exam PDF pages
- Output: Text, labels, numeric values with confidence scores
- Responsibility: Extract handwritten text, printed labels, units
- **Why:** OCR excels at character-level recognition (LLMs misread)

**Layer 2: Vision LLM (Qwen/Ollama/Moondream)**
- Input: Exam page images
- Output: Structural YAML (shapes, relationships, pathway classification)
- Responsibility: Identify diagram structure, spatial relationships, semantic meaning
- **Why:** Vision LLM understands context and relationships (OCR cannot)

**Layer 3: OpenCV**
- Input: Exam page images
- Output: Geometric YAML (coordinates, angles, dimensions, line styles)
- Responsibility: Pixel-precise measurements, shape classification, style detection
- **Why:** OpenCV provides measurements (LLMs approximate)

**Merge:**
1. Start with Vision LLM's structural output
2. Override text with OCR readings (higher accuracy)
3. Override measurements with OpenCV data (pixel-precise)
4. Tag every field with `source` and `confidence`
5. Detect conflicts and flag them
6. Output to `validate_yaml`

### 4.2 YAML Schema (Example: Geometry 2D)

```yaml
type: geometry_2d
source_exam: "2025-P6-Maths-Prelim Exam-Henry Park"
question_number: 3
page_number: 2
difficulty: B

# Layer 2: Vision LLM (Structure)
shapes:
  - id: square_1
    type: square
    side_length: {value: 4, unit: "cm", source: "vision_llm", confidence: 0.85}
    position: {x: 100, y: 150, source: "opencv", confidence: 0.95}
  - id: circle_1
    type: circle
    radius: {value: 4, unit: "cm", source: "vision_llm", confidence: 0.82}
    center: {x: 104, y: 154, source: "opencv", confidence: 0.93}
    attachment: "top_right_corner_of_square"

# Layer 1: OCR (Text)
labels:
  - text: "4 cm"
    anchor: "square_1.side_length"
    position: {x: 120, y: 170, source: "ocr", confidence: 0.97}
  - text: "4 cm"
    anchor: "circle_1.radius"
    position: {x: 110, y: 195, source: "ocr", confidence: 0.96}

# Layer 3: OpenCV (Measurements)
measurements:
  - shape: "square_1"
    side_length_px: 80.3
    side_length_cm: 4.0
    source: "opencv"
    confidence: 0.99
  - shape: "circle_1"
    radius_px: 80.1
    radius_cm: 4.0
    source: "opencv"
    confidence: 0.98

# ATOM-SG Classification
pathway_type: "Geometry - Area & Perimeter - Composite Shapes"
subpathway: "Part-Whole (Composite Shapes)"
equation_shadow: "Total area = area of square + area of 3/4 circle"
difficulty_zone: "B"
```

### 4.3 Source Priority (When Sources Disagree)

| Data Type | Best Source | Why Others Fail |
|-----------|------------|-----------------|
| Label text ("12 cm", "35°") | OCR | LLMs misread characters |
| Diagram structure | Vision LLM | OCR and OpenCV can't infer meaning |
| Spatial relationships | OpenCV | LLMs approximate positions |
| Line styles (solid/dashed) | OpenCV | LLMs frequently misidentify |
| Fill patterns | OpenCV | Precise angle/density measurement |
| Angles between lines | OpenCV | LLMs round or guess |

---

## 5. Reconstruction Quality Standard

### 5.1 Definition

**Quality of reconstruction data must match original exam questions.**

This means:
1. **Visual Fidelity:** Reconstructed diagram looks identical to original (pixel-precise)
2. **Semantic Fidelity:** Reconstructed problem has same meaning as original
3. **Linguistic Fidelity:** Reconstructed text matches original exactly
4. **Completeness:** No missing elements (diagrams, labels, annotations)

### 5.2 Measurement Criteria

| Dimension | How to Measure | Target |
|-----------|-----------------|--------|
| **Visual Fidelity** | Pixel comparison: Measure deviation in shape positions, angles, dimensions | ≤3% deviation |
| **Semantic Fidelity** | Pathway classification: Compare reconstructed vs. original classification | Exact match |
| **Linguistic Fidelity** | Text comparison: Reconstructed question text vs. original text | 100% match |
| **Completeness** | Element count: Count shapes, labels, annotations in both | 100% match |

### 5.3 Improvisation During Transfer Testing

**Requirement:** Deconstructed data must allow improvisation during transfer testing without obvious human errors and be solvable using both visual and text information.

**What This Means:**
- Deconstructed YAML contains **all structural information** (shapes, relationships)
- Deconstructed YAML contains **all measurements** (coordinates, angles, dimensions)
- Deconstructed YAML contains **all semantic information** (pathway, equation shadow)
- During transfer test, can **modify parameters** (e.g., change side length from 4cm to 6cm)
- Modified YAML still produces **valid, solvable problem**
- Both visual and text information are **sufficient to solve**

**Example Improvisation:**
```yaml
# Original
shapes:
  - id: square_1
    side_length: {value: 4, unit: "cm"}

# Improvised (Transfer Test)
shapes:
  - id: square_1
    side_length: {value: 6, unit: "cm"}  # Changed value
    # All other structure, relationships, measurements scale proportionally
```

**Result:** Transfer test problem is valid, solvable, visually correct.

---

## 6. Intervention Phase Focus (Weeks 2-4)

### 6.1 Primary Focus Areas

**Based on your clarification:**

| Focus Area | Description |
|------------|-------------|
| **Data Manipulation** | Work with deconstructed YAML data during intervention |
| **Downsizing to Nano-Nodes** | Use geometry taxonomy (18 nano-nodes) for targeted training |
| **Accurate Visuals** | Render exam-quality diagrams from YAML using rendering gates/rules |
| **Teaching Content** | Create Socratic feedback, model articulations, 3-level rubrics |

### 6.2 Week-by-Week Focus

**Week 2:**
- Deconstruct 94 exam questions (internal pipeline)
- Validate reconstruction fidelity (compare to original)
- Generate revised baseline test pack (40 questions)
- Train **Pathway 1** (weakest from baseline)

**Week 3:**
- Focus on **data manipulation**: How to work with YAML structure
- Train **Pathway 2** (second weakest)
- Create intervention problems with **downsized nano-nodes**
- Render exam-quality visuals from YAML

**Week 4:**
- Focus on **teaching content**: Socratic feedback, model articulations
- Train **Pathway 3** (third weakest)
- Verify improvisation capability (modify YAML → generate transfer test)
- Prepare for Week 5/6 transfer test

**Week 5/6:**
- Conduct transfer test (40 new unseen problems)
- Measure ramp-up: Compare baseline vs. transfer performance
- Verify reconstruction fidelity on transfer test problems

---

## 7. Success Criteria

| Criterion | Target | How to Measure |
|-----------|--------|-----------------|
| **Reconstruction Fidelity** | Visual: ≤3% deviation, Semantic: 100% match, Linguistic: 100% match, Completeness: 100% | Automated pixel comparison + semantic comparison |
| **Pathway Identification Accuracy** | ≥90% on trained pathways | Automated QA from student submissions |
| **Articulation Quality (Level 2+)** | ≥90% of problems | Manual QA of student articulations |
| **Solving Accuracy Improvement** | ≥80% from baseline on trained pathways | Compare baseline vs. transfer test scores |
| **Transfer: Identification Accuracy** | ≥80% on trained pathways, ≥50% on held-back pathways | Week 5/6 transfer test results |
| **Improvisation Capability** | Modified YAML produces valid, solvable problems | Manual QA of 10 improvised problems |

---

## 8. Deliverables & Timeline

| Deliverable | Owner | Target | Dependencies |
|-------------|-------|--------|------------|
| **SOR v4.3 (this document)** | Zcaethbot | 2026-04-21 | — |
| **Internal Deconstruction Pipeline** | Vision LLM + OpenCV + OCR Bureaus | 2026-04-23 | Vision LLM documentation reviewed |
| **YAML Schema for Each Problem Type** | Vision LLM Bureau | 2026-04-23 | Deconstruction pipeline |
| **Automated Validation System** | Integrity Bureau | 2026-04-24 | YAML schema |
| **Deconstruct 94 Exam Questions (Internal)** | Vision LLM Bureau | 2026-04-25 | Validation system |
| **Verify Reconstruction Fidelity** | Integrity Bureau | 2026-04-26 | 94 questions deconstructed |
| **Generate Revised Baseline Test Pack** | Pedagogy Bureau | 2026-04-27 | Verified fidelity |
| **Weeks 2-4 Intervention (Data Manipulation Focus)** | All Bureaus | 2026-05-03 | Revised baseline |
| **Week 5/6 Transfer Test** | QA Team | 2026-05-06 | Intervention complete |
| **Ramp-Up Analytics Report** | Zcaethbot | 2026-05-08 | Transfer test results |

---

## 9. Open Decisions

1. **Vision LLM Model Selection:** Which model? Options: Qwen, Ollama, Moondream. **Pending decision.**
2. **Validation Threshold Adjustments:** Are confidence thresholds appropriate? **Pending decision.**
3. **Launch Date:** Is May 10, 2026 (14 days from now) appropriate? **Pending decision.**
4. **Quality Standard Review:** Is "reconstruction data must match original" sufficient? **Pending decision.**

---

*This document supersedes SOR v4.2. Approval pending from Sean Foo.*
