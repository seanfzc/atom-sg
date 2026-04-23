# MEMORY.md - Long-Term Memory (Curated)

## Cost Optimization & Second Brain Principles
*Added: 2026-04-08*

### Core Cost Management Rules
1. **Karpathy's Insight:** Context length drives token cost because every new message re-processes entire history in Transformer forward pass.
2. **Running Summary:** Maintain 200-300 token conversation summary updated every 4-6 turns.
3. **Second Brain Integration:** Route important knowledge to wiki/ instead of repeating in conversation history.
4. **API Cost Tracking:** 
   - Vision APIs expensive (when available)
   - Claude text API: use judiciously
   - OCR (Tesseract): free alternative for PDF extraction
   - Manual processing: fallback when APIs unavailable/expensive

### ATOM-SG Project Specifics
**Project:** Operation Vertical Thread (Syllabus Digital Twin)
**Current Phase:** SOR v4.5 Pilot Validation
**Cost Decisions Made:**
1. **Vision API:** Not available (404 errors on multiple models)
2. **OCR:** Tesseract APPROVED (installation in progress)
3. **Claude API:** Using `claude-sonnet-4-6` for text analysis (not vision)
4. **Heuristic:** Manual validation first, automation for production

### Rendering Stack Project
*Added: 2026-04-12*

**Objective:** Create TikZ/Matplotlib pipeline for diagram rendering (bar models, flowcharts) with pastel colors and SVG output for web.

**Status:** 
- Matplotlib installed and working
- Basic repo structure created (`rendering-stack/`)
- Sample problem card → SVG bar model pipeline functional
- TikZ template created (requires LaTeX installation pending)
- Basictex installation failed (needs sudo password)

**Next Steps:**
1. Manual LaTeX installation (or use smaller distribution)
2. Extend to more diagram types
3. Integrate with ATOM‑SG problem cards

### Geometry Taxonomy Development
*Added: 2026-04-13*

**Objective:** Define P5-P6 geometry nano‑nodes (granular skills), equation shadows, articulation rubrics, and starter problem mapping for ATOM‑SG.

**Status:**
- Drafted `Geometry_Taxonomy_NanoNodes.md` with 18 nano‑nodes across `geometry_measurement` and `geometry_properties`
- Updated `Geometry‑Rubrics.md` template with nano‑node examples
- Aligned with ATOM‑SG schema v4.1 logic families
- Created memory log for continuity
- **Baseline Test Framework:** Developed comprehensive geometry sub‑pathway structure (4 threads: G1 Angle Reasoning, G2 Area & Perimeter, G3 Volume & 3D, G4 Properties & Classification) with equation shadows, 25‑item distribution proposal, and enhanced diagnostic rubric (4 dimensions, 5 points max per item)
- **GeoBot Alignment:** Integrated with GeoBot's Problem‑Pack Plan (25 items mapped to nano‑nodes, sub‑pathways G1‑G4)
- **Taxonomy Approval:** Sean approved nano‑nodes (2026‑04‑13)
- **Rubric Progress:** Populated `Geometry‑Rubrics.md` with 5 detailed examples (angle measurement, area of composite rectangles, angle properties, circle circumference/area, quadrilateral classification)
- **Problem Files:** GeoBot completed T1 (25 problem files) and T2 (sub‑pathway mapping)
- **Rubric Mapping Finalised:** `Geometry‑Rubric‑Mapping.md` — all 25 problems mapped, 100% threshold, Zone A = Level 2, G007 tightened (T3 DONE)

**Key Decisions:**
- Equation shadows emerge in P4–P5; baseline assumes P6 exposure
- Heavier weight on G1 and G2 reflecting P6 exam emphasis
- Rubric separates conceptual (pathway identification) from algebraic (setup/execution) skills
- **Approved nano‑node list** serves as definitive skill inventory for P5‑P6 geometry

**Next Steps:**
1. ✅ Taxonomy review completed (approved)
2. Validate sub‑pathways against P6 syllabus (in progress via GeoBot mapping)
3. ✅ Item distribution balanced via GeoBot's 25‑item plan
4. ✅ 25 problem files drafted (GeoBot T1)
5. Create Second Brain nodes for geometry nano‑nodes
6. ✅ Rubric mapping finalised (`Geometry‑Rubric‑Mapping.md`) — 100% threshold, Zone A = Level 2, G007 tightened (T3 DONE)
7. RenderBot to begin diagram rendering (T4)
8. OcrBot OCR pipeline readiness (T5)

### Technical Limitations Learned
1. **PDF Quality:** Singapore P6 exam papers (2025) are scanned images with minimal OCR text
2. **API Access:** Claude vision models return 404 (may require different plan)
3. **Alternative Tools:** Gemini CLI lacks image upload capability
4. **Local Solution:** Tesseract OCR + Python integration recommended

### Schema Evolution Tracking
- **v4.0:** Corrected node misclassification, added MOE codes, vertical evolution
- **v4.1:** Paper 1 Revolution (time targets, calculator flags), red herring analysis
- **Cost Impact:** Each schema version adds fields but improves accuracy → reduces rework

### File Organization
- **Conversation Summaries:** `conversation_summary_*.md` (token-efficient context)
- **Daily Logs:** `memory/YYYY-MM-DD.md` (detailed activity)
- **Second Brain:** `second-brain-simple/wiki/` (structured knowledge)
- **Pilot Results:** `P6_Pilot_Validation/` and `second-brain-simple/Pilot_Results/`
- **Sub‑agent communications:** `subagentcomms.md` (daily updates and status reports)

### User Preferences
- **Cost Sensitivity:** Yes (implementing Karpathy + Second Brain skill)
- **Verification Process:** Independent LLM review of manual samples before automation
- **Technical Approval:** Required for system changes (`brew install tesseract`) - APPROVAL GRANTED 2026-04-08
- **Quality Focus:** Schema accuracy over speed (manual validation phase)
- **Cost-Optimized Skill:** Implemented 2026-04-08 with conversation summaries and wiki integration
- **Daily Updates:** Proactively write status reports to `subagentcomms.md` at least once daily or when updates occur
- **Model Usage Policy:** Created 2026-04-14 — GLM tiered usage (Flash/4.7/5.1) for all ATOM-SG sub-agents (see `ATOM-SG Pilot/MODEL_USAGE_POLICY.md`)

### Workflow Optimization
1. **Validation First:** Manual processing to verify schema/methodology
2. **Automation Second:** Scale with OCR/APIs once validated
3. **Cost Monitoring:** Track API calls, token usage, processing time
4. **Knowledge Compounding:** All outputs feed back into Second Brain

### MVP Verification & Deployment Patterns
*Added: 2026-04-15*

**Verification Process:**
1. **Comprehensive test suite:** 23 verification points covering backend, frontend, OCR, rendering, integration
2. **Critical bug fix validation:** Ensure P0-P2 fixes are functional (pathway validation, gaming detection, vocabulary gap, etc.)
3. **Integration workflow testing:** Practice submission → triad feedback, pathway radar → gaming detection, OCR → text extraction
4. **Performance benchmarks:** API response < 100ms, OCR processing ~3.5s/page, memory usage minimal

**Deployment Artifact Patterns:**
1. **Docker multi‑stage build:** Builder stage with compile‑time dependencies, runtime stage with minimal footprint
2. **System‑aware install script:** Detects OS (macOS/Ubuntu/RHEL/Arch), installs system packages (Tesseract, libraries), set up Python venv
3. **Configuration templating:** `.env.example` with sensible defaults, documentation of all environment variables
4. **Backup automation:** Scheduled backups with retention policy (keep last 30), easy restore procedure
5. **Health monitoring:** Built‑in health check endpoint (`/api/v1/system/health`), Docker HEALTHCHECK, systemd service file
6. **Pilot launch checklist:** Comprehensive timeline (11‑day countdown) with clear milestones and success criteria

**Key Decisions:**
- **OCR dependency:** Tesseract 5.5.2 installed system‑wide (not Python package) → requires apt/brew install
- **Rendering dependencies:** Matplotlib requires GL libraries; LaTeX optional for TikZ
- **Database:** In‑memory storage for MVP; SQLite/PostgreSQL migration path documented
- **Port configuration:** Default 5000, configurable via environment variable
- **Security:** Non‑root user in Docker, environment‑based secrets, HTTPS via reverse proxy

**Lessons Learned:**
- **UX fixes are frontend‑only:** Can be implemented post‑backend completion without API changes
- **Verification scripts are reusable:** `final_verification.sh` can be run in CI/CD pipeline
- **Deployment artifacts should be created early:** Even before pilot launch, reduces last‑minute stress

**Next Steps:**
- Apply verification pattern to future MVP projects
- Extend deployment patterns to multi‑container setups (database, cache, queue)
- Create reusable templates for FastAPI + frontend projects

### Cost Management - Model Usage Policy
*Added: 2026-04-14*

**Objective:** Optimize GLM model usage across all ATOM-SG sub-agents (GeoBot, RenderBot, OcrBot, BackendBot, MVPBot, DashBot).

**Model Tiers:**
- **GLM Flash (glm-4.7-flashx):** $0.06/M in, $0.40/M out — basic/template tasks
- **GLM 4.7:** $0.60/M in, $2.20/M out — moderate complexity
- **GLM 5.1:** $1.20/M in, $4.00/M out — complex reasoning, high-stakes decisions

**Decision Tree:**
1. Routine/template work → GLM Flash
2. Complex reasoning/high-stakes → GLM 5.1
3. Otherwise (moderate complexity) → GLM 4.7

**Location:** `ATOM-SG Pilot/MODEL_USAGE_POLICY.md` — sub-agent specific guidelines included.

**Next Steps:**
- Monitor sub-agent compliance via cost tracking
- Adjust policy as models change or project phases shift

### MVP Final Verification & Launch Readiness
*Added: 2026-04-16*

**Objective:** Validate ATOM‑SG MVP functionality after Phase 1 P0/P1 fixes.

**Verification Results (2026‑04‑16):**
- **Total Tests:** 23 (backend, frontend, OCR, rendering, integration)
- **Passed:** 22
- **Failed:** 0
- **Warnings:** 1 (CORS headers missing—non‑critical)
- **Outcome:** ✅ MVP Final Verification PASSED

**Critical Components Validated:**
1. Backend health & all API endpoints (problems, rubrics, renders, practice sessions, pathway radar, glossary, milestones, reflections)
2. Critical bug fixes: pathway‑type validation (P0‑1), gaming detection (P0‑3)
3. Practice submission & triad feedback workflow
4. OCR pipeline (Tesseract 5.5.2) functional
5. Rendering pipeline (SVG/PDF diagrams) present
6. Frontend static files & root endpoint serving
7. System statistics & API documentation (/docs)

**Next Steps (from verification script):**
1. ✅ Implement 8 critical UX fixes (2–3 h) – COMPLETED
2. Final hands‑on review by stakeholders
3. ✅ Deployment preparation (Docker, installation script) – COMPLETED
4. Pilot launch: Week 2 (2026‑04‑26)

**Status:** MVP is stable, functional, and ready for pilot deployment.

### Deployment Artifacts & Patterns
*Added: 2026-04-16*

**Deployment Artifacts Created:**
1. **Docker multi‑stage build** – Python 3.11, Tesseract, GL libraries, non‑root user
2. **Docker Compose** – Backend + nginx reverse proxy with health checks
3. **System‑aware install script** – Detects macOS, Ubuntu, RHEL, Arch; installs system packages, Python venv
4. **Configuration templating** – `.env.example` with sensible defaults
5. **Backup automation** – Daily backups keeping last 30, easy restore procedure
6. **Health monitoring** – Built‑in health endpoint, cron‑ready health check script
7. **Service management** – systemd service file generation for Linux production
8. **Frontend serving** – Backend modified to serve `index.html` at root with SPA catch‑all route
9. **Pilot launch checklist** – 11‑day countdown with clear milestones and success criteria

**Key Decisions:**
- **Frontend serving:** Backend serves frontend directly (simpler for pilot), nginx optional for production
- **Backup strategy:** Keep last 30 daily backups; restore script with confirmation
- **Monitoring:** Health check endpoint + script for cron monitoring
- **Security:** Non‑root user in Docker, environment‑based secrets, HTTPS via reverse proxy

**Files Created:**
- `Dockerfile`, `docker‑compose.yml`, `Dockerfile.nginx`
- `install.sh`, `start.sh`, `test_deployment.sh`
- `DEPLOYMENT.md`, `PILOT_LAUNCH_CHECKLIST.md`
- `nginx.conf`, `backup.sh`, `restore_backup.sh`, `health_check.sh`

**Next Steps:**
1. Test Docker build on clean environment
2. Test install script on target OS (Ubuntu 22.04)
3. Deploy to pilot server
4. Run verification on deployed instance

### Math Diagram Skills (Audit & Rendering)
*Added: 2026‑04‑16, Updated: 2026‑04‑17*

**Skills Created:**
1. **`math-diagram-audit`** – Systematic audit framework for testing math diagrams. Measure everything, accept nothing on faith. Includes audit pipeline (Stages 0‑5), type‑specific checks, tester procedures, and severity classification.
2. **`math-diagram-rendering`** – Guidelines for rendering math diagrams with audience‑appropriate constraints. Includes four gates (solve first, audience constraint, reasoning chain mapping, scale planning), visual strategies, and anti‑patterns.

**Key Learnings Incorporated from ATOM‑SG P0‑6 Review:**
1. **Missing angle rays:** Angle diagrams must include both rays (lines) and arc, not just arc
2. **Label placement ambiguity:** Labels must be visually connected to the dimension they represent (not in "no‑man's‑land")
3. **Visual‑text mismatch:** Diagram shape must match text description exactly (quarter‑circle vs half‑circle)
4. **Unit label completeness:** All measurements must include explicit unit labels
5. **5‑second visual association test:** If an 11‑year‑old visual learner cannot immediately understand which label goes with which geometric element, the diagram fails.
6. **Audience constraint gates:** Diagrams must avoid concepts above target level (variables for pre‑algebra, formal notation, adult vocabulary)
7. **Reasoning chain visibility:** Every solution step must have a visual anchor
8. **Scale consistency:** Within‑panel proportions must be exact (25‑unit segment 5× wider than 5‑unit segment)

**Code Fixes Implemented:**
- `generate_renders.py` updated for all P0 issues (angle rays, height label annotation, quarter‑circle shape)
- Visual‑geometric completeness checklist added to review process
- Future diagram generation will include validation of visual associations

**Impact:** Prevents repetition of P0‑6 issues; ensures diagrams are pedagogically sound and geometrically complete. Provides separate, focused skills for auditing (tester) and rendering (agent) workflows.

---

*Memory maintenance: Review weekly, distill key learnings, remove outdated entries*
