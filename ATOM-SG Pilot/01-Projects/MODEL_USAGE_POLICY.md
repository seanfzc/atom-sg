# Model Usage Policy for ATOM-SG Sub-Agents

*Effective: 2026-04-14*
*Project: ATOM-SG (Operation Vertical Thread)*
*Owner: PM Owner (Zcaethbot)*

---

## Overview

All sub-agents MUST follow this model usage policy to balance cost, speed, and quality. The GLM model family offers different capabilities at different price points. Choose the right model for the task.

---

## Model Tiers

### 🟢 **GLM Flash** (glm-4.7-flashx)
**Cost:** $0.06/M input, $0.40/M output
**Use for:** Simple, routine tasks where speed > nuance

**Examples:**
- File I/O, data extraction, formatting
- Template filling, basic text processing
- Simple lookups and validation
- Low-stakes decision making
- Quick code snippets (<50 lines)

### 🔵 **GLM 4.7** (glm-4.7)
**Cost:** $0.60/M input, $2.20/M output
**Use for:** Standard tasks requiring moderate reasoning

**Examples:**
- Content generation with constraints
- Medium-complexity problem solving
- Multi-step processes with clear logic
- Code implementation (50-200 lines)
- Structured output generation
- Analysis with moderate nuance

### 🟣 **GLM 5.1** (glm-5.1)
**Cost:** $1.20/M input, $4.00/M output
**Use for:** Complex reasoning, strategic thinking, high-stakes decisions

**Examples:**
- Deep architectural decisions
- Multi-threaded coordination
- Complex pedagogical reasoning
- Novel solution synthesis
- Critical quality gates (e.g., taxonomy approval)
- Cross-domain synthesis

---

## Sub-Agent Specific Guidelines

### GeoBot (Geometry Specialist)

**Use GLM Flash for:**
- Reading geometry problem templates
- Filling in numeric values
- Simple equation shadow extraction
- Formatting problem files

**Use GLM 4.7 for:**
- Creating geometry problems with diagrams
- Mapping problems to nano-nodes
- Writing solution explanations
- Rubric mapping for standard items

**Use GLM 5.1 for:**
- Designing novel geometry nano-nodes
- Complex articulation rubric development
- High-stakes taxonomy decisions
- Cross-strand synthesis (geometry + algebra)

---

### RenderBot (Diagram Rendering)

**Use GLM Flash for:**
- Reading diagram templates
- Simple parameter substitution
- Format conversion (SVG → PDF metadata)

**Use GLM 4.7 for:**
- Generating TikZ/Matplotlib code for diagrams
- Coordinating with rendering libraries
- Multi-step rendering pipeline
- Quality checks on diagram output

**Use GLM 5.1 for:**
- Novel diagram type design
- Complex multi-element rendering
- High-stakes production renders
- Debugging rendering failures

---

### OcrBot (OCR Pipeline)

**Use GLM Flash for:**
- Running Tesseract OCR
- Simple text cleanup
- File parsing and metadata extraction

**Use GLM 4.7 for:**
- OCR accuracy analysis
- Text normalization and cleanup
- Structured data extraction from OCR
- Pre-processing pipeline logic

**Use GLM 5.1 for:**
- Complex handwritten recognition
- Multi-modal OCR (text + diagrams)
- Critical quality gates on OCR output
- Novel OCR augmentation strategies

---

### BackendBot (Backend/API)

**Use GLM Flash for:**
- API endpoint boilerplate
- Database schema templates
- Basic CRUD operations
- File I/O operations

**Use GLM 4.7 for:**
- API spec development
- Database query optimization
- Endpoint implementation
- Integration testing logic

**Use GLM 5.1 for:**
- Architecture decisions (SQL vs NoSQL)
- Complex multi-system integration
- Critical security considerations
- High-stakes API design decisions

---

### MVPBot (MVP Planning)

**Use GLM Flash for:**
- Milestone tracking updates
- Simple status reports
- Template filling for milestones

**Use GLM 4.7 for:**
- Milestone dependency mapping
- Timeline adjustments
- Cross-bot coordination logic
- Requirements refinement

**Use GLM 5.1 for:**
- High-level MVP strategy
- Critical milestone decisions
- Trade-off analysis (time vs scope)
- Novel user flow design

---

### DashBot (Dashboards)

**Use GLM Flash for:**
- Reading dashboard templates
- Updating status fields
- Simple markdown formatting

**Use GLM 4.7 for:**
- Creating Dataview queries
- Dashboard layout design
- Cross-referencing data
- Template refinement

**Use GLM 5.1 for:**
- Novel dashboard visualizations
- Complex data synthesis
- Critical metrics definition
- Cross-dashboard integration logic

---

## Decision Tree

When choosing a model, ask:

1. **Is this routine, template-based work?**
   - Yes → GLM Flash

2. **Is this complex reasoning or high-stakes?**
   - Yes → GLM 5.1

3. **Otherwise (moderate complexity)**
   - Use GLM 4.7

---

## Enforcement

- **PM Owner:** Periodic audits of sub-agent model usage via cost tracking
- **Sub-Agents:** Self-enforce by referring to this policy before starting tasks
- **Violations:** Document in SubAgentComms.md with cost impact analysis

---

## Updates

This policy will be updated as:
- New models become available
- Cost structures change
- Project phases shift (e.g., production ramp-up)

Last updated: 2026-04-14

---

*Questions? Ping PM Owner (Zcaethbot) in SubAgentComms.md*
