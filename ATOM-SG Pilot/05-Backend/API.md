# ATOM-SG Pilot v4.1 — Backend API Specification

**Status:** ✅ APPROVED — Pending Proportional Rendering Implementation
**UX/Pedagogical Review:** ✅ APPROVED with recommendations (see review below)
**Priority 2 Enhancement:** Model articulations added to triad feedback response (2026-04-15 06:05 SGT)
**Frontend Enhancement:** Radar chart visualization recommendation added (2026-04-15 08:20 SGT)
**Last Updated:** 2026-04-15 08:20 SGT
**Approval Condition:** Visual rendering tool must deliver accurate drawings drawn to scale (e.g., bar models proportional to values)
**Backend Framework:** FastAPI / Flask (lightweight)
**Frontend:** Static HTML5 + JavaScript (no framework overhead)

---

## 1. Overview

This API serves the ATOM-SG Pilot v4.1 Recognition-First Integrated Training system. It provides endpoints for problem management, rubric evaluation, diagram rendering, milestone tracking, scan ingestion with OCR, practice sessions, pathway radar drills, and analytics.

### Design Principles

- **Local-first:** All file storage is local, no cloud dependencies
- **Minimal overhead:** Simple REST endpoints returning JSON
- **Fast iteration:** Quick to modify based on student data
- **Static frontend ready:** Serves static assets, but business logic is on the server
- **No paid APIs:** Uses Tesseract for OCR, TikZ/Matplotlib for rendering

### Base URL

```
http://localhost:5000/api/v1
```

### Conventions

- All endpoints return JSON
- Standard HTTP status codes: 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found), 500 (Server Error)
- Timestamps in ISO 8601 format: `2026-04-14T17:57:00+08:00`
- File paths are relative to artifact repository: `ATOM-SG Pilot/05-Backend/artifacts/`

---

## 2. Endpoints

### 2.1 Problems

#### GET /problems

List all available problems with optional filtering.

**Query Parameters:**
- `track` (optional): Filter by track (`word-problems`, `geometry`, `data-interpretation`)
- `pathway` (optional): Filter by pathway type
- `week` (optional): Filter by pilot week (1-5)

**Response:**
```json
{
  "problems": [
    {
      "id": "prob_001",
      "title": "Fraction Remainder Problem",
      "track": "word-problems",
      "pathway": "before-after-change",
      "difficulty": "medium",
      "week": 1,
      "createdAt": "2026-04-14T10:00:00+08:00"
    }
  ],
  "total": 40
}
```

#### GET /problems/{id}

Get a specific problem with full details.

**Response:**
```json
{
  "id": "prob_001",
  "title": "A shop sold 3/5 of its pens on Monday...",
  "track": "word-problems",
  "pathway": "before-after-change",
  "difficulty": "medium",
  "questionText": "A shop sold 3/5 of its pens on Monday and 1/4 of the remainder on Tuesday...",
  "diagrams": [
    {
      "type": "bar-model",
      "renderUrl": "/renders/prob_001_bar_model.svg"
    }
  ],
  "expectedAnswer": {
    "type": "numeric",
    "value": 300
  },
  "rubric": {
    "pathwayId": "rub_pathway_001",
    "solutionId": "rub_solution_001"
  },
  "createdAt": "2026-04-14T10:00:00+08:00"
}
```

#### POST /problems

Create a new problem (used by Pedagogy Bureau).

**Request:**
```json
{
  "title": "Problem Title",
  "track": "word-problems",
  "pathway": "before-after-change",
  "difficulty": "medium",
  "questionText": "Full question text...",
  "diagrams": [
    {
      "type": "bar-model",
      "spec": "tikz code here"
    }
  ],
  "expectedAnswer": {
    "type": "numeric",
    "value": 300
  }
}
```

**Response:** `201 Created` with created problem object

#### GET /problems/pdf

Generate a printable baseline or transfer test PDF.

**Query Parameters:**
- `week` (required): Week number (1 = baseline, 5 = transfer)

**Response:** PDF file (application/pdf)

**Implementation Notes:**
- Use `reportlab` or `weasyprint` to generate PDF from problem data
- Include diagrams as embedded images (SVG/PNG)
- Format: A4, 12pt font, include question numbers
- Each problem spans full page for working space

---

### 2.2 Rubrics

#### GET /rubrics

List all evaluation rubrics.

**Response:**
```json
{
  "rubrics": [
    {
      "id": "rub_pathway_001",
      "type": "pathway-identification",
      "pathway": "before-after-change",
      "levels": 3
    },
    {
      "id": "rub_solution_001",
      "type": "solution-evaluation",
      "problemId": "prob_001",
      "levels": 3
    }
  ]
}
```

#### GET /rubrics/{id}

Get a specific rubric with full criteria.

**Response:**
```json
{
  "id": "rub_pathway_001",
  "type": "pathway-identification",
  "pathway": "before-after-change",
  "levels": [
    {
      "level": 1,
      "name": "Basic Recognition",
      "description": "Correctly identifies the pathway type",
      "criteria": ["Mentions 'before-after' or 'remainder'"]
    },
    {
      "level": 2,
      "name": "Clear Articulation",
      "description": "Explains the pathway in own words",
      "criteria": ["Describes sequential changes", "Mentions finding original"]
    },
    {
      "level": 3,
      "name": "Precise Connection",
      "description": "Connects pathway to equation shadow",
      "criteria": ["Links structure to equation framework"]
    }
  ],
  "createdAt": "2026-04-14T10:00:00+08:00"
}
```

#### POST /rubrics

Create a new rubric (used by Pedagogy + Integrity Bureaus).

**Request:**
```json
{
  "type": "pathway-identification",
  "pathway": "before-after-change",
  "levels": [
    {
      "level": 1,
      "name": "Basic Recognition",
      "description": "Correctly identifies the pathway type",
      "criteria": ["Mentions 'before-after' or 'remainder'"]
    }
  ]
}
```

**Response:** `201 Created`

#### POST /rubrics/batch

Create multiple rubrics in a single request (for efficient data seeding).

**Request:**
```json
{
  "rubrics": [
    {
      "type": "pathway-identification",
      "pathway": "before-after-change",
      "levels": [...]
    },
    {
      "type": "solution-evaluation",
      "problemId": "prob_001",
      "levels": [...]
    }
  ]
}
```

**Response:**
```json
{
  "created": [
    {"id": "rub_pathway_001", "type": "pathway-identification"},
    {"id": "rub_solution_001", "type": "solution-evaluation"}
  ],
  "failed": [],
  "total": 2
}
```

---

### 2.3 Renders

**Critical Requirement:** All visual diagrams must be **proportionally accurate to scale** to avoid student confusion.

**Proportional Scaling Rules:**
- **Bar Models:** Bar lengths must be mathematically proportional to values.
  - Example: Bar A = 300 units, Bar B = 100 units → Bar A must be 3× length of Bar B
  - Use consistent scale factor across all bars in same diagram
- **Pie Charts:** Sector angles must accurately represent percentages.
  - Example: 25% = 90°, 50% = 180°, 75% = 270°
- **Geometric Shapes:** All dimensions must match the problem statement.
  - Example: Rectangle with 2:1 aspect ratio must render with twice as wide as tall
- **Number Lines:** Tick marks and intervals must be evenly spaced.
- **Graphs:** Axes, grid lines, and data points must be precisely positioned.

**Validation:**
- Backend validates that rendered diagrams maintain proportional accuracy
- If scaling deviation > 5%, reject render and flag for manual review
- Include `scaleFactor` in render metadata for frontend reference

---

#### POST /renders

Generate a diagram render (TikZ/Matplotlib).

**Request:**
```json
{
  "problemId": "prob_001",
  "diagramType": "bar-model",
  "spec": "tikz code or matplotlib spec",
  "format": "svg",
  "values": {
    "bar1": 300,
    "bar2": 100,
    "bar3": 200
  }
}
```

**Request Parameters:**
- `problemId` (required): Unique problem identifier
- `diagramType` (required): `bar-model`, `pie-chart`, `line-graph`, `geometric-shape`
- `spec` (required): TikZ code or Matplotlib specification
- `format` (optional): `svg` (default) or `png`
- `values` (required for proportional rendering): Numeric values for scaling

**Response:**
```json
{
  "renderId": "rend_001",
  "status": "processing",
  "estimatedTime": 2
}
```

#### GET /renders/{id}

Check render status and get URL when ready.

**Response:**
```json
{
  "id": "rend_001",
  "status": "completed",
  "url": "/artifacts/renders/prob_001_bar_model.svg",
  "format": "svg",
  "createdAt": "2026-04-14T10:00:00+08:00",
  "completedAt": "2026-04-14T10:00:02+08:00",
  "proportionalAccuracy": {
    "scaleFactor": 3.0,
    "deviation": 0.0,
    "validated": true
  }
}
```

**Response Fields:**
- `scaleFactor`: Ratio of largest to smallest value (e.g., 300/100 = 3.0)
- `deviation`: Percent deviation from perfect proportion (0% = perfect)
- `validated`: True if deviation ≤ 5%, False if needs manual review

#### GET /renders/{id}/download

Download the rendered file directly.

#### GET /renders

List all available renders with optional filtering.

**Query Parameters:**
- `problemId` (optional): Filter by problem ID
- `format` (optional): Filter by format (`svg`, `png`, `pdf`)

**Response:**
```json
{
  "renders": [
    {
      "id": "rend_001",
      "problemId": "prob_001",
      "type": "bar-model",
      "url": "/artifacts/renders/prob_001_bar_model.svg",
      "format": "svg",
      "createdAt": "2026-04-14T10:00:00+08:00"
    },
    {
      "id": "rend_002",
      "problemId": "prob_002",
      "type": "pie-chart",
      "url": "/artifacts/renders/prob_002_pie_chart.png",
      "format": "png",
      "createdAt": "2026-04-14T10:05:00+08:00"
    }
  ],
  "total": 45
}
```

**Error Handling:**
- 400: Invalid filter parameter
- 500: Server error when reading render database

---

### 2.4 Milestones

#### GET /milestones

Get student progress milestones.

**Response:**
```json
{
  "milestones": [
    {
      "id": "mile_001",
      "week": 2,
      "pathway": "before-after-change",
      "status": "in-progress",
      "problemsCompleted": 5,
      "problemsTotal": 10,
      "averageScore": 0.8,
      "startedAt": "2026-04-20T10:00:00+08:00"
    }
  ]
}
```

#### GET /milestones/{id}

Get a specific milestone with detailed progress.

**Response:**
```json
{
  "id": "mile_001",
  "week": 2,
  "pathway": "before-after-change",
  "status": "in-progress",
  "problemsCompleted": 5,
  "problemsTotal": 10,
  "averageScore": 0.8,
  "pathwayIdentificationAccuracy": 0.9,
  "articulationLevel": 2,
  "startedAt": "2026-04-20T10:00:00+08:00",
  "lastActivityAt": "2026-04-22T15:30:00+08:00"
}
```

#### PATCH /milestones/{id}

Update milestone progress (called after each problem attempt).

**Request:**
```json
{
  "problemsCompleted": 6,
  "lastAttemptScore": 0.9,
  "pathwayIdentifiedCorrectly": true,
  "articulationLevel": 2
}
```

**Response:** `200 OK` with updated milestone object

---

### 2.5 Scans (Upload & OCR)

#### POST /scans

Upload a scanned baseline test for OCR processing.

**Request:** `multipart/form-data`
- `file`: The scanned image (PDF, PNG, JPG)
- `week`: Week number (baseline = 1, transfer = 5)

**Response:**
```json
{
  "scanId": "scan_001",
  "status": "processing",
  "uploadedAt": "2026-04-18T14:00:00+08:00",
  "estimatedTime": 30
}
```

#### GET /scans/{id}

Check scan processing status and get OCR results.

**Response:**
```json
{
  "id": "scan_001",
  "status": "completed",
  "uploadedAt": "2026-04-18T14:00:00+08:00",
  "completedAt": "2026-04-18T14:00:30+08:00",
  "ocrResults": [
    {
      "questionId": "prob_001",
      "text": "Student's handwritten answer...",
      "confidence": 0.85
    }
  ],
  "gapMap": {
    "weakestPathways": [
      {
        "pathway": "before-after-change",
        "accuracy": 0.3,
        "rank": 1
      },
      {
        "pathway": "part-whole-comparison",
        "accuracy": 0.4,
        "rank": 2
      },
      {
        "pathway": "composite-shapes",
        "accuracy": 0.5,
        "rank": 3
      }
    ]
  }
}
```

#### GET /scans/{id}/download

Download the original uploaded scan file.

---

### 2.6 Practice Sessions

#### POST /practice-sessions

Start a new practice session.

**Request:**
```json
{
  "week": 2,
  "pathway": "before-after-change",
  "sessionType": "intervention"
}
```

**Response:**
```json
{
  "sessionId": "sess_001",
  "week": 2,
  "pathway": "before-after-change",
  "sessionType": "intervention",
  "problems": ["prob_001", "prob_002", "prob_003"],
  "startedAt": "2026-04-20T10:00:00+08:00"
}
```

#### GET /practice-sessions/{id}

Get session details with current problem.

**Response:**
```json
{
  "id": "sess_001",
  "status": "active",
  "currentProblemIndex": 2,
  "currentProblem": {
    "id": "prob_003",
    "title": "Before-After Problem 3",
    "questionText": "...",
    "diagrams": [...]
  },
  "completedProblems": [
    {
      "problemId": "prob_001",
      "score": 0.8,
      "pathwayIdentifiedCorrectly": true,
      "articulationLevel": 2
    }
  ]
}
```

#### POST /practice-sessions/{id}/submit

Submit answer for current problem (with forced articulation). This is **session-based** practice within an active practice session.

**Request:**
```json
{
  "problemId": "prob_003",
  "pathwayType": "before-after-change",
  "equationShadow": "After first change, then after second change, find original",
  "studentAnswer": {
    "type": "numeric",
    "value": 300
  },
  "diagramAnnotations": [
    {
      "type": "sketch",
      "coordinates": [[100, 100], [200, 200]]
    }
  ]
}
```

**Response:**
```json
{
  "submissionId": "sub_001",
  "feedback": {
    "pathwayIdentification": {
      "correct": true,
      "confidence": 0.95
    },
    "articulation": {
      "level": 2,
      "feedback": "Good articulation! You described the sequential changes clearly.",
      "modelArticulation": "After first change, then after second change, find original."
    },
    "solution": {
      "correct": true,
      "score": 1.0
    },
    "overall": "green"
  },
  "nextProblemId": "prob_004"
}
```

**Note:** The `modelArticulation` field provides students with an ideal articulation to compare against their own input. This enables self-reflection and helps students understand what a strong articulation looks like for that problem type.

#### POST /practice

Submit an individual practice attempt in the recognition-first loop. This is **standalone practice** (not session-based) for quick practice on specific problems.

**Key Difference:**
- `POST /practice-sessions/{id}/submit` is for **session-based** practice with curated problem sequences and progress tracking
- `POST /practice` is for **individual** practice submissions on any problem without session context

**Request:**
```json
{
  "problemId": "prob_001",
  "pathwayType": "before-after-change",
  "equationShadow": "After first change, then after second change, find original",
  "studentAnswer": {
    "type": "numeric",
    "value": 300
  },
  "diagramAnnotations": [
    {
      "type": "sketch",
      "coordinates": [[100, 100], [200, 200]]
    },
    {
      "type": "label",
      "text": "3/5",
      "position": [150, 150]
    }
  ]
}
```

**Response:**
```json
{
  "submissionId": "prac_sub_001",
  "problemId": "prob_001",
  "submittedAt": "2026-04-20T10:30:00+08:00",
  "feedback": {
    "pathwayIdentification": {
      "correct": true,
      "identifiedPathway": "before-after-change",
      "confidence": 0.95,
      "feedback": "Correctly identified this as a before-after change problem."
    },
    "articulation": {
      "level": 2,
      "feedback": "Good articulation! You described the sequential changes clearly. Try to be more specific about finding the original value.",
      "modelArticulation": "After first change, then after second change, find original."
    },
    "solution": {
      "correct": true,
      "score": 1.0,
      "expectedAnswer": 300,
      "studentAnswer": 300,
      "feedback": "Your answer is correct. Great work!"
    },
    "overall": "green"
  },
  "recommendedNextSteps": [
    "Practice another before-after change problem",
    "Try articulating the equation shadow more precisely"
  ]
}
```

**Note:** The `modelArticulation` field provides students with an ideal articulation to compare against their own input. This enables self-reflection and helps students understand what a strong articulation looks like for that problem type.

**Error Handling:**
- 400: Invalid problem ID, missing required fields, or malformed request
- 404: Problem not found
- 500: Rubric evaluation error

---

### 2.7 Pathway Radar (Warm-up)

#### GET /pathway-radar/questions

Get 10 mixed pathway identification questions for today's warm-up.

**Query Parameters:**
- `date` (optional): Date for warm-up (default: today)

**Response:**
```json
{
  "questions": [
    {
      "id": "radar_q001",
      "questionText": "A shop sold 3/5 of its pens...",
      "pathways": ["before-after-change", "part-whole-comparison"],
      "timeLimit": 30
    }
  ],
  "total": 10,
  "date": "2026-04-20"
}
```

#### POST /pathway-radar/submit

Submit pathway identification answers.

**Request:**
```json
{
  "date": "2026-04-20",
  "answers": [
    {
      "questionId": "radar_q001",
      "identifiedPathway": "before-after-change",
      "confidence": 0.9
    }
  ]
}
```

**Response:**
```json
{
  "score": {
    "correct": 8,
    "total": 10,
    "accuracy": 0.8
  },
  "feedback": {
    "strongPathways": ["before-after-change"],
    "weakPathways": ["composite-shapes"]
  }
}
```

---

### 2.8 Advanced Analytics (Week 3+)

#### POST /collision

Detect cross-thread collision patterns across multiple pathways. This endpoint analyzes student data to identify when different problem-solving approaches or pathways "collide" (i.e., when the student is confused between similar but distinct pathways).

**Use Case:** Week 3+ intervention for students who struggle to differentiate between similar pathways (e.g., part-whole comparison vs. before-after change).

**Request:**
```json
{
  "week": 3,
  "pathways": [
    "before-after-change",
    "part-whole-comparison"
  ],
  "timeWindow": {
    "start": "2026-04-27T00:00:00+08:00",
    "end": "2026-04-28T23:59:59+08:00"
  },
  "options": {
    "includeArticulation": true,
    "threshold": 0.7,
    "analyzeRecentAttempts": 20
  }
}
```

**Response:**
```json
{
  "analysisId": "coll_001",
  "analyzedAt": "2026-04-28T12:00:00+08:00",
  "collisionDetected": true,
  "collisionDetails": {
    "collidingPathways": [
      {
        "pathway": "before-after-change",
        "identificationAccuracy": 0.82,
        "articulationLevel": 2.1
      },
      {
        "pathway": "part-whole-comparison",
        "identificationAccuracy": 0.78,
        "articulationLevel": 1.9
      }
    ],
    "collisionPoints": [
      {
        "problemId": "prob_015",
        "problemType": "word-problem",
        "detectedConflict": {
          "studentIdentified": "before-after-change",
          "correctPathway": "part-whole-comparison",
          "confidence": 0.65,
          "evidence": "Student used sequential steps (before-after pattern) but problem requires simultaneous comparison."
        },
        "severity": "high"
      },
      {
        "problemId": "prob_018",
        "problemType": "word-problem",
        "detectedConflict": {
          "studentIdentified": "part-whole-comparison",
          "correctPathway": "before-after-change",
          "confidence": 0.72,
          "evidence": "Student compared parts but missed sequential change aspect."
        },
        "severity": "medium"
      }
    ],
    "collisionMetrics": {
      "collisionRate": 0.15,
      "totalAttemptsAnalyzed": 20,
      "collisionsDetected": 3,
      "averageConfidence": 0.68
    }
  },
  "recommendedInterventions": [
    {
      "priority": "high",
      "type": "contrast-drill",
      "title": "Before-After vs. Part-Whole Contrast Drill",
      "description": "Practice with paired problems that highlight the difference between sequential change and simultaneous comparison.",
      "estimatedDuration": 15,
      "problemIds": ["prob_101", "prob_102", "prob_103", "prob_104"]
    },
    {
      "priority": "medium",
      "type": "articulation-focus",
      "title": "Force Articulation on Ambiguous Problems",
      "description": "For the next 5 problems, require explicit verbal articulation before attempting the solution.",
      "estimatedDuration": 30
    },
    {
      "priority": "low",
      "type": "review-rubric",
      "title": "Review Pathway Identification Rubric",
      "description": "Review the key differentiators between before-after and part-whole pathways.",
      "estimatedDuration": 10
    }
  ],
  "nextReviewDate": "2026-04-30"
}
```

**Error Handling:**
- 400: Invalid week, missing pathways, or malformed time window
- 404: No collision data available for specified period
- 500: Analysis engine error

**Storage:** Collision analyses stored under `artifacts/collision/`

#### GET /interpretation

Get data interpretation results and metrics. This endpoint provides analytics on how the student interprets data-based problems (charts, graphs, tables) with a focus on detecting red herrings and distractors.

**Use Case:** Week 3+ intervention for the data interpretation track, especially for problems with red herrings.

**Query Parameters:**
- `week` (optional): Filter by pilot week (default: all weeks)
- `pathway` (optional): Filter by pathway type (default: all data interpretation pathways)
- `includeRedHerringAnalysis` (optional): Include detailed red herring analysis (default: false)

**Response:**
```json
{
  "queryParameters": {
    "week": 3,
    "pathway": "data-interpretation-red-herring",
    "includeRedHerringAnalysis": true
  },
  "summary": {
    "totalAttempts": 15,
    "correctAnswers": 12,
    "accuracy": 0.80,
    "averageTimeToSolve": 245,
    "analyzedAt": "2026-04-28T12:00:00+08:00"
  },
  "metrics": {
    "chartTypeAccuracy": {
      "bar-chart": 0.85,
      "line-graph": 0.75,
      "pie-chart": 0.80,
      "table": 0.90
    },
    "questionTypeAccuracy": {
      "direct-reading": 0.95,
      "calculation": 0.82,
      "comparison": 0.78,
      "trend-analysis": 0.72
    },
    "redHerringPerformance": {
      "problemsWithRedHerrings": 8,
      "correctlyIdentifiedRedHerrings": 6,
      "fellForRedHerring": 2,
      "redHerringAccuracy": 0.75
    }
  },
  "redHerringAnalysis": [
    {
      "problemId": "prob_025",
      "title": "Sales Data with Seasonal Distractor",
      "redHerringType": "seasonal-variation",
      "detected": true,
      "correctlyIgnored": true,
      "feedback": "Good! You correctly identified that the seasonal spike was a distractor and focused on the trend."
    },
    {
      "problemId": "prob_028",
      "title": "Production Output with Outlier",
      "redHerringType": "outlier-data-point",
      "detected": false,
      "correctlyIgnored": false,
      "feedback": "The outlier point in March is unusual and should not be included in the trend calculation. Try identifying anomalies first."
    },
    {
      "problemId": "prob_032",
      "title": "Revenue with Currency Change",
      "redHerringType": "unit-change",
      "detected": true,
      "correctlyIgnored": true,
      "feedback": "Excellent! You noticed the currency changed from SGD to USD in 2023 and adjusted your comparison."
    }
  ],
  "strengths": [
    "Strong at direct reading from tables and charts",
    "Good at identifying unit-based red herrings",
    "Accurate with bar chart interpretation"
  ],
  "areasForImprovement": [
    "Practice trend analysis on line graphs",
    "Work on identifying outlier data points",
    "Slow down on comparison questions to avoid mistakes"
  ],
  "recommendations": [
    {
      "priority": "high",
      "type": "outlier-drill",
      "title": "Outlier Detection Practice",
      "description": "Practice problems specifically designed to train outlier identification.",
      "problemIds": ["prob_201", "prob_202", "prob_203"]
    },
    {
      "priority": "medium",
      "type": "line-graph-practice",
      "title": "Line Graph Trend Analysis",
      "description": "Focus on line graph problems with trend-based questions.",
      "problemIds": ["prob_204", "prob_205"]
    }
  ]
}
```

**Error Handling:**
- 400: Invalid week number or pathway filter
- 404: No interpretation data available for specified criteria
- 500: Analysis error

**Storage:** Interpretation analyses stored under `artifacts/interpretation/`

---

### 2.9 Analytics

#### GET /analytics/baseline

Get baseline test results and gap map.

**Response:**
```json
{
  "scanId": "scan_001",
  "totalScore": 0.6,
  "scoresByTrack": {
    "word-problems": 0.55,
    "geometry": 0.65,
    "data-interpretation": 0.7
  },
  "scoresByPathway": {
    "before-after-change": 0.3,
    "part-whole-comparison": 0.4,
    "composite-shapes": 0.5,
    "angles": 0.7,
    "data-interpretation-red-herring": 0.8
  },
  "gapMap": {
    "weakestPathways": [
      {
        "pathway": "before-after-change",
        "accuracy": 0.3,
        "rank": 1
      }
    ]
  },
  "completedAt": "2026-04-18T14:00:30+08:00"
}
```

#### GET /analytics/transfer

Get transfer test results and ramp-up metrics.

**Response:**
```json
{
  "scanId": "scan_005",
  "trainedPathways": {
    "before-after-change": {
      "identificationAccuracy": 0.85,
      "solvingAccuracy": 0.82
    },
    "part-whole-comparison": {
      "identificationAccuracy": 0.88,
      "solvingAccuracy": 0.80
    },
    "composite-shapes": {
      "identificationAccuracy": 0.90,
      "solvingAccuracy": 0.85
    }
  },
  "heldBackPathways": {
    "angles": {
      "identificationAccuracy": 0.55,
      "solvingAccuracy": 0.60
    },
    "data-interpretation-red-herring": {
      "identificationAccuracy": 0.50,
      "solvingAccuracy": 0.55
    }
  },
  "rampUpMetrics": {
    "baselineIdentificationAccuracy": 0.4,
    "transferIdentificationAccuracy": 0.81,
    "improvement": 0.41,
    "targetMet": true
  },
  "successCriteria": [
    {
      "metric": "pathwayIdentificationAccuracy",
      "value": 0.85,
      "target": 0.9,
      "met": false
    },
    {
      "metric": "articulationLevel2PlusRate",
      "value": 0.92,
      "target": 0.9,
      "met": true
    },
    {
      "metric": "solvingImprovement",
      "value": 0.82,
      "target": 0.8,
      "met": true
    }
  ]
}
```

#### GET /analytics/progress

Get overall progress across all weeks.

**Response:**
```json
{
  "weeklyProgress": [
    {
      "week": 1,
      "status": "completed",
      "baselineScore": 0.6,
      "weakestPathways": ["before-after-change", "part-whole-comparison", "composite-shapes"]
    },
    {
      "week": 2,
      "status": "completed",
      "pathway": "before-after-change",
      "averageScore": 0.82,
      "identificationAccuracy": 0.90,
      "articulationLevel": 2.1
    },
    {
      "week": 3,
      "status": "completed",
      "pathway": "part-whole-comparison",
      "averageScore": 0.85,
      "identificationAccuracy": 0.92,
      "articulationLevel": 2.2
    }
  ],
  "overallMetrics": {
    "totalProblemsAttempted": 30,
    "averageScore": 0.83,
    "averageIdentificationAccuracy": 0.91,
    "averageArticulationLevel": 2.15
  }
}
```

---

### 2.10 Student Reflection

#### POST /reflections

Submit a student reflection (digital reflection sheet).

**Request:**
```json
{
  "week": 2,
  "pathway": "before-after-change",
  "reflection": "I learned that before-after change problems require me to...",
  "confidence": 0.8,
  "struggles": ["calculating remainders"],
  "improvements": ["double-checking my steps"]
}
```

**Response:** `201 Created`

#### GET /reflections

Get student reflections.

**Query Parameters:**
- `week` (optional): Filter by week
- `pathway` (optional): Filter by pathway

**Response:**
```json
{
  "reflections": [
    {
      "id": "ref_001",
      "week": 2,
      "pathway": "before-after-change",
      "reflection": "I learned that before-after change problems...",
      "createdAt": "2026-04-22T18:00:00+08:00"
    }
  ]
}
```

---

### 2.11 System (Admin)

#### GET /system/health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2026-04-14T18:00:00+08:00"
}
```

#### GET /system/stats

Get system statistics (for debugging/monitoring).

**Response:**
```json
{
  "problems": 40,
  "rubrics": 8,
  "renders": 45,
  "scans": 2,
  "practiceSessions": 15,
  "lastActivity": "2026-04-22T18:00:00+08:00"
}
```

---

## 3. File Storage Structure

```
ATOM-SG Pilot/05-Backend/artifacts/
├── renders/           # TikZ/Matplotlib outputs
│   ├── prob_001_bar_model.svg
│   └── prob_002_pie_chart.png
├── ocr/               # Original scan files + OCR results
│   ├── scan_001.pdf
│   ├── scan_001_ocr.json
│   └── scan_002.png
├── sessions/          # Practice session data (optional, could be in-memory)
│   └── sess_001.json
├── collision/         # Cross-thread collision detection analyses
│   └── coll_001.json
└── interpretation/    # Data interpretation analyses
    └── interp_001.json
```

---

## 9. Data Models

### Problem
```typescript
interface Problem {
  id: string;
  title: string;
  track: "word-problems" | "geometry" | "data-interpretation";
  pathway: string;
  difficulty: "easy" | "medium" | "hard";
  questionText: string;
  diagrams: Diagram[];
  expectedAnswer: Answer;
  rubric: {
    pathwayId: string;
    solutionId: string;
  };
  createdAt: string;
}
```

### Rubric
```typescript
interface Rubric {
  id: string;
  type: "pathway-identification" | "solution-evaluation";
  pathway?: string;
  levels: RubricLevel[];
  createdAt: string;
}

interface RubricLevel {
  level: number;
  name: string;
  description: string;
  criteria: string[];
}
```

### Feedback (Triad)
```typescript
interface Feedback {
  pathwayIdentification: {
    correct: boolean;
    confidence: number;
  };
  articulation: {
    level: number;
    feedback: string;
  };
  solution: {
    correct: boolean;
    score: number;
  };
  overall: "green" | "yellow" | "red";
}
```

---

## 10. Error Responses

All endpoints may return these error codes:

| Code | Description |
|------|-------------|
| 400 | Bad Request (invalid input) |
| 404 | Not Found (resource doesn't exist) |
| 500 | Internal Server Error |
| 503 | Service Unavailable (OCR/rendering overloaded) |

**Error Response Format:**
```json
{
  "error": {
    "code": 400,
    "message": "Invalid pathway type",
    "details": "Pathway 'invalid-type' not found"
  }
}
```

---

## 11. Implementation Notes

### Backend Technology Stack

- **Framework:** FastAPI (recommended) or Flask
- **OCR:** Tesseract (local, no paid APIs)
- **Rendering:** TikZ (geometry) + Matplotlib (bar models, graphs)
- **File Storage:** Local filesystem
- **Frontend:** Static HTML5 + JavaScript served from `/static`

### Scope and Assumptions

**Single-Student Pilot:**
- This API spec assumes a single student for the pilot phase (P6 student with 5-week intervention)
- No student ID or authentication required in the current design
- All endpoints operate on a single student's data
- If multi-student support is needed in production, add `studentId` parameter to all relevant endpoints

### OCR Configuration

**Tesseract Settings:**
- **Confidence Threshold:** 0.70 (70%) — Minimum OCR confidence for automatic text recognition
- **Low-Confidence Handling:**
  - If OCR confidence < 0.70: Flag for manual review
  - Return `"reviewRequired": true` in scan response
  - Allow parent/teacher to correct OCR text via manual entry UI
- **Preprocessing:** Grayscale conversion, noise reduction, contrast enhancement before OCR
- **Timeout:** 30 seconds per page (A4)

### Rendering Configuration

**Proportional Accuracy Requirement (Critical):**
- All diagrams must maintain proportional accuracy within 5% deviation
- Validate scale factors against input values
- Reject renders with deviation > 5% and flag for manual review
- Log all deviations for quality monitoring

**TikZ Rendering:**
- **Timeout:** 10 seconds max per diagram
- **Proportional Scaling:**
  - Use TikZ coordinate system with explicit unit scaling
  - Example: For bars 300, 100, 200 → scale to 3cm, 1cm, 2cm
  - Add grid lines for reference (optional)
- **Error Handling:**
  - If compilation timeout: Return `"status": "failed"` with error message
  - If LaTeX syntax error: Return `"status": "failed"` with compiler output
  - Retry failed renders once with simplified template
- **Cache:** Rendered diagrams cached for 24 hours

**Matplotlib Rendering:**
- **Timeout:** 5 seconds max per diagram
- **Proportional Scaling:**
  - Use `plt.bar()` with explicit width parameters proportional to values
  - Example: `width=[3, 1, 2]` for values [300, 100, 200]
  - Add data labels showing actual values
  - Use aspect ratio `equal` for geometric shapes
- **Error Handling:**
  - If generation timeout: Return `"status": "failed"`
  - Retry with fallback defaults (simple bar model without custom colors)
- **Formats:** SVG (default), PNG (fallback)

### Key Workflows

1. **Baseline Test Flow:**
   - GET /problems (week=1) → Print test
   - POST /scans (week=1) → Upload completed test
   - GET /scans/{id} → Get gap map with weakest 3 pathways

2. **Daily Practice Flow:**
   - POST /practice-sessions → Start session (recommended for structured practice)
   - OR POST /practice → Submit individual attempt (for quick practice on specific problems)
   - GET /practice-sessions/{id} → Get current problem (session-based)
   - POST /practice-sessions/{id}/submit → Submit with forced articulation (session-based)
   - Receive instant triad feedback

3. **Pathway Radar Flow:**
   - GET /pathway-radar/questions → Get 10 mixed questions
   - POST /pathway-radar/submit → Submit identifications
   - Receive feedback on strong/weak pathways

4. **Transfer Test Flow:**
   - GET /problems (week=5) → Print transfer test
   - POST /scans (week=5) → Upload completed test
   - GET /analytics/transfer → Get ramp-up metrics and success criteria

5. **Cross-Thread Collision Detection Flow (Week 3+):**
   - POST /collision → Analyze collision patterns across pathways
   - Review collision details (colliding pathways, collision points, metrics)
   - Implement recommended interventions (contrast drills, articulation focus)
   - Re-run collision analysis to track improvement

6. **Data Interpretation Flow (Week 3+):**
   - Practice data interpretation problems with red herrings
   - GET /interpretation → Get detailed interpretation metrics and insights
   - Review red herring analysis (what was detected, what was missed)
   - Practice on recommended problem sets based on weaknesses

---

## 7. Design Decisions & Trade-offs

### Endpoint Design: `POST /practice` vs. `POST /practice-sessions/{id}/submit`

**Decision (MVP Primary):** Session-based practice is the primary approach, with individual submission as optional.

**Primary Use Case: Session-Based Practice**
- `POST /practice-sessions/{id}/submit`: Session-based practice for structured intervention
  - Curated problem sequences (Weeks 2-4 pathway drills)
  - Progress tracking across multiple problems
  - Maintains session state (current problem, completed problems)
  - Best for: Daily intervention sessions, pathway-focused training, Week 2-5 MVP

**Optional Use Case: Individual Submission**
- `POST /practice`: Standalone practice for individual submissions
  - No session state required
  - Quick practice on any problem
  - Returns triad feedback without next problem recommendation
  - Best for: Warm-up radar checks, quick diagnostic checks, ad-hoc problem solving

**Implementation Guidance:**
- **Frontend should prioritize** session-based practice for Weeks 2-5 intervention
- **Individual submission** should be exposed as a secondary option for warm-up radar and spot checks
- **Both endpoints use same** triad feedback format (pathwayIdentification, articulation, solution)

**Trade-off:** Dual endpoints provide flexibility for different use cases. Session-based is primary for MVP, individual submission is optional for flexibility. Clear documentation guides frontend development.

### Collision Detection Implementation

**Storage Strategy:** Collision analyses stored under `artifacts/collision/` for offline review and trend tracking.

**Algorithm Design:**
- Compare pathway identification accuracy across similar pathways
- Identify problems where student's identification differs from correct pathway
- Rate collision severity by confidence gap and articulation level
- Recommend interventions based on collision patterns

**Performance Considerations:** Collision analysis is computationally intensive. Implement:
- Async processing for large time windows
- Caching of collision analyses (24-hour TTL)
- Limit to recent attempts (default: last 20)

### Interpretation Analysis Design

**Red Herring Types Detected:**
- Seasonal variation (unusual data points due to seasonal factors)
- Outlier data points (anomalies that skew analysis)
- Unit changes (currency, measurement unit changes mid-series)
- Time discontinuities (gaps or breaks in time series)

**Data Sources:**
- Practice submissions for data interpretation problems
- Trained pathways: `data-interpretation-red-herring`
- Analyzed by rubric and problem metadata

**Storage Strategy:** Interpretation analyses stored under `artifacts/interpretation/` for tracking progress over time.

### Renders List Endpoint

**Design Decision:** `GET /renders` returns a paginated list with optional filtering.

**Rationale:**
- Frontend may need to enumerate all renders for problem preview or troubleshooting
- Filtering by `problemId` and `format` enables efficient queries
- Cache-friendly: can be cached client-side for reduced server load

**Implementation Notes:**
- Index renders by `problemId` and `format` for fast filtering
- Implement pagination if render count exceeds 100 (not expected in pilot)
- Include `createdAt` for freshness checks

---

## 8. OpenAPI Specification (Optional)

This Markdown API spec can be converted to OpenAPI 3.0 format for code generation. Key mappings:

- `GET /problems` → `paths./problems.get`
- `POST /scans` → `paths./scans.post` (multipart/form-data)
- `POST /practice-sessions/{id}/submit` → `paths./practice-sessions.{id}.submit.post`

Use tools like `swagger-codegen` or `openapi-generator` to generate client SDKs if needed.

---

**Next Steps:**
1. Implement backend endpoints (FastAPI recommended)
2. Set up Tesseract OCR pipeline
3. Implement TikZ/Matplotlib rendering service
4. Build static HTML5 + JavaScript frontend
5. Test with sample baseline data

---

## 📋 Independent API Review

**Reviewer:** API-Reviewer (Independent Subagent)
**Review Date:** 2026-04-14 20:09 SGT
**Status:** ⚠️ **REVIEW WITH FEEDBACK**

---

### Executive Summary

The API specification is well-structured, comprehensive, and follows RESTful conventions. The documentation quality is high with clear request/response schemas, error handling, and implementation notes. However, **critical gaps exist** in MVP requirements coverage that must be addressed before this spec can be marked production-ready.

**Overall Assessment:** 75% complete - Strong foundation with specific missing endpoints.

---

### 1. MVP Requirements Coverage ❌

**Core Endpoints (Week 2 - Must Have):**

| MVP Requirement | API Status | Notes |
|-----------------|------------|-------|
| `GET /problems` | ✅ Present | Includes track/pathway/week filtering |
| `GET /problems/{id}` | ✅ Present | Full problem details with diagrams |
| `GET /rubrics` | ✅ Present | Lists all rubrics |
| `GET /rubrics/{id}` | ✅ Present | Detailed rubric with criteria |
| `GET /renders` | ❌ **MISSING** | No list endpoint - only POST/GET/{id} |
| `GET /renders/{id}` | ✅ Present | Download/render status |
| `POST /practice` | ❌ **MISSING** | Only POST /practice-sessions exists |
| `GET /milestones` | ✅ Present | Milestone tracking |

**Extended Endpoints (Week 3-4 - Must Have):**

| MVP Requirement | API Status | Notes |
|-----------------|------------|-------|
| `POST /collision` | ❌ **MISSING** | Not documented anywhere |
| `GET /interpretation` | ❌ **MISSING** | Not documented anywhere |

**Other MVP Requirements:**
- ✅ Scan ingestion with OCR: `POST /scans`, `GET /scans/{id}` - Covered
- ✅ Analytics (baseline): `GET /analytics/baseline` - Covered
- ✅ Analytics (transfer): `GET /analytics/transfer` - Covered
- ✅ Analytics (progress): `GET /analytics/progress` - Covered
- ⚠️ Geometry pack support: Implicit via track filter, but no dedicated geometry pack endpoint

**CRITICAL ISSUE:** **4 out of 10 MVP endpoints are missing**. This blocks Week 2 readiness.

---

### 2. Completeness ✅ (for documented endpoints)

**Strengths:**
- ✅ All documented endpoints have complete request/response schemas
- ✅ Error handling is well-specified (400, 404, 500, 503)
- ✅ File storage structure is clear and local-first
- ✅ Data models (TypeScript interfaces) are defined
- ✅ Implementation notes are detailed (OCR config, rendering timeouts)
- ✅ Workflows are documented (Baseline, Practice, Radar, Transfer)

**Gaps:**
- ❌ Missing endpoints (see section 1)
- ❌ No batch endpoint for problems (only rubrics have batch)

---

### 3. Consistency ⚠️

**Strengths:**
- ✅ Consistent versioning: `/api/v1` base path
- ✅ Proper HTTP methods used (GET for retrieval, POST for creation, PATCH for updates)
- ✅ Logical endpoint organization by domain
- ✅ Standard JSON response format
- ✅ ISO 8601 timestamps throughout

**Minor Issues:**
- ⚠️ **Naming inconsistency:** Some endpoints use hyphens (`practice-sessions`, `pathway-radar`), others don't (`problems`, `rubrics`). Recommend consistent hyphenation: `practice-sessions` → `practice-sessions` (keep), but consider `pathway-radar` → `pathway-radar` (keep), ensure others follow pattern
- ⚠️ **Endpoint granularity:** `POST /practice-sessions` creates sessions, but MVP requires `POST /practice` for individual submissions. These serve different purposes, causing confusion.

**Recommendations:**
1. Clarify the distinction between session management (`practice-sessions`) and practice submission (`practice`)
2. If session-based is preferred, update MVP requirements to reflect this
3. Ensure all endpoint names follow consistent hyphenation pattern

---

### 4. Implementation Feasibility ✅

**Local-First Approach:** ✅
- All file storage is local under `artifacts/`
- No cloud dependencies or paid APIs
- Tesseract OCR and TikZ/Matplotlib are open-source
- Single-student assumption is explicitly documented

**Tesseract OCR Integration:** ✅
- Configuration is well-documented (70% confidence threshold)
- Low-confidence handling is specified (manual review flow)
- Preprocessing steps are defined (grayscale, noise reduction)
- 30-second timeout is reasonable

**TikZ/Matplotlib Rendering:** ⚠️
- Timeout is specified (10s TikZ, 5s Matplotlib)
- Error handling includes retry logic
- **Potential issue:** 10-second TikZ timeout may be tight for complex diagrams
- **Recommendation:** Consider caching rendered diagrams more aggressively or simplifying initial renders

**Single-Student Pilot:** ✅
- Assumption is clearly documented
- No authentication required (appropriate for pilot)
- Clear path to multi-student support (add `studentId` parameter)

---

### Critical Issues Blocking Production 🚫

1. **`GET /renders` (LIST)** - MVP requires this endpoint. Add it.
   ```json
   // Suggested response
   {
     "renders": [
       {"id": "rend_001", "problemId": "prob_001", "type": "bar-model", "format": "svg", "createdAt": "..."}
     ],
     "total": 45
   }
   ```

2. **`POST /practice`** - MVP requires this for individual practice submissions. Current design uses session-based approach.
   - **Option A:** Add `POST /practice` for individual submissions (align with MVP)
   - **Option B:** Update MVP requirements to use session-based approach

3. **`POST /collision`** - Required for Week 3+ cross-thread collision detection. Not documented.
   - **Need clarification:** What data does this endpoint accept? What does it return?
   - **Storage suggested:** `artifacts/collision/`

4. **`GET /interpretation`** - Required for Week 3+ data interpretation results. Not documented.
   - **Need clarification:** What interpretation results? How are they generated/stored?

---

### Recommendations 📝

**Immediate Actions (Before Approval):**

1. **Add missing MVP endpoints:**
   - Implement `GET /renders` (list all renders)
   - Implement `POST /practice` (individual practice submission) OR clarify session-based approach
   - Implement `POST /collision` (cross-thread collision detection)
   - Implement `GET /interpretation` (data interpretation results)

2. **Clarify geometry pack support:**
   - Add explicit documentation for geometry pack endpoints
   - Consider `GET /problems/geometry-pack` for dedicated geometry pack retrieval

3. **Add batch endpoint for problems:**
   - Implement `POST /problems/batch` (aligns with `POST /rubrics/batch`)

4. **Clarify endpoint naming consistency:**
   - Document naming convention and ensure all endpoints follow it

**Future Enhancements:**

1. **Performance optimization:** Consider increasing TikZ timeout or implementing async rendering queue
2. **Multi-student support:** Document path to adding `studentId` parameter
3. **Authentication:** Add note about authentication strategy for production
4. **Rate limiting:** Add documentation about rate limiting for API endpoints

---

### Final Verdict ⚠️

**Status:** **REVIEW WITH FEEDBACK**

**Summary:** The API specification has a solid foundation with excellent documentation quality. However, **4 critical MVP endpoints are missing** and must be added before this spec can be marked production-ready. The implementation approach is sound, and the local-first design is appropriate for the pilot phase.

**Decision:** ❌ **DO NOT APPROVE** - Requires implementation of missing endpoints.

**Next Steps:**
1. BackendBot should add the 4 missing endpoints with full documentation
2. MVPBot should confirm the distinction between `POST /practice-sessions` and `POST /practice`
3. All stakeholders should review and approve collision/interpretation endpoint designs
4. Re-submit for review once all endpoints are documented

**Estimated time to completion:** 1-2 hours for BackendBot to implement missing endpoints.

---

*This review was conducted by the independent API Reviewer subagent as part of the ATOM-SG Pilot project quality assurance process.*

---

## 🎓 Independent MVP UX & Pedagogical Review

**Reviewer:** MVP-UX-Reviewer (Independent Subagent)
**Review Date:** 2026-04-15 05:55 GMT+8
**Status:** ✅ **APPROVE** with recommendations
**Review Model:** GLM 5.1

---

### Executive Summary

The ATOM-SG Pilot MVP represents a **novel and pedagogically sound approach** to P6 mathematics training. The recognition-first methodology is innovative, well-designed, and has strong potential to improve student learning outcomes. The 5-week intervention timeline is realistic, and the technical implementation (local-first, no cloud dependencies) is appropriate for a pilot.

**Overall Assessment:** **APPROVE for pilot deployment** — The MVP is practical, powerful enough to improve learning, and will be engaging for students when implemented with the recommended enhancements.

**Critical Strengths:**
- ✅ Novel recognition-first pedagogical approach (metacognitive skill building)
- ✅ Triad feedback system (pathway + articulation + solution)
- ✅ Realistic 5-week timeline with structured daily practice
- ✅ Clear success criteria and measurable outcomes
- ✅ Local-first technical design appropriate for pilot

**Key Recommendations:**
- 🔧 **Priority 1 (Before Pilot Launch):** Reduce student dependency on parent/teacher for scans
- 🎨 **Priority 2 (During Pilot):** Enhance articulation feedback specificity
- 🎯 **Priority 3 (Post-Pilot):** Add minimal gamification elements

---

## 1. Student Journey Analysis

### Week 1 – Baseline Test (Offline → Online)

**Workflow:**
1. Student completes 40-question paper test (word problems, geometry, data interpretation)
2. Parent scans and uploads via `POST /scans`
3. OCR processes scan (30-second timeout)
4. System generates gap map identifying weakest 3 pathways
5. Determines focus for Weeks 2-4

**Pain Points:**
- ⚠️ **Parent dependency:** Student cannot complete baseline without parent involvement
- ⚠️ **OCR reliability:** Poor-quality scans may require manual review (low confidence < 70%)
- ⚠️ **Offline friction:** Paper-based test creates manual workflow interruption

**Moments of Delight:**
- ✅ Clear gap map with specific pathway targeting (personalized diagnosis)
- ✅ Visual breakdown of performance across tracks (word problems, geometry, data interpretation)
- ✅ Objective data-driven decision-making for Weeks 2-4 focus

**Verdict:** Baseline workflow is functional but introduces dependency on parent/teacher. Recommended improvement: Consider allowing students to type answers directly into MVP interface for online baseline (fallback to scan for offline preference).

### Weeks 2–4 – Daily Intervention (Online)

**Daily Workflow (20 minutes total):**

**Part 1: Pathway Radar Warm-Up (5 minutes)**
- Student answers 10 identification-only questions
- 30 seconds per question, mixed pathways
- Immediate feedback on strong/weak pathways
- Builds recognition muscle memory

**Part 2: Practice Session (15 minutes)**
1. Student reads problem with embedded diagram
2. **Forced articulation phase:**
   - Must identify pathway type
   - Must articulate equation shadow in own words
   - UI blocks solving until articulation complete
3. Student solves problem
4. Instant triad feedback via `POST /practice-sessions/{id}/submit`
5. Progress tracked in milestones via `PATCH /milestones/{id}`

**Pain Points:**
- ⚠️ **Forced articulation friction:** Students accustomed to solving immediately may find typing articulations tedious
- ⚠️ **No diagram annotation:** API supports diagram annotations, but UX must provide canvas tool
- ⚠️ **Repetition fatigue:** 30 problems per pathway over 3 weeks may feel repetitive

**Moments of Delight:**
- ✅ **Quick wins:** 5-minute warm-up provides immediate gratification
- ✅ **Clarity:** Forced articulation creates "aha" moments when student sees pattern
- ✅ **Instant feedback:** Triad feedback provides immediate validation/correction
- ✅ **Progress visibility:** Milestone tracking shows completion (e.g., "5/10 problems complete")
- ✅ **Visual engagement:** Radar warm-up creates visual representation of strengths/weaknesses

**Verdict:** Daily intervention workflow is well-designed and engaging. The 5-minute warm-up + 15-minute practice balance is appropriate. Recommended improvement: Add optional "skip articulation" mode after pathway mastery confirmed (to avoid over-practicing)

### Week 5 – Transfer Test (Offline → Online)

**Workflow:**
1. Student completes 40 new unseen problems (trained + held-back pathways)
2. Parent scans and uploads
3. System generates ramp-up analytics
4. Compares baseline vs. transfer performance
5. Evaluates success criteria (90% ID accuracy, 90% articulation Level 2+, 80% solving improvement)

**Pain Points:**
- ⚠️ **Same dependency:** Parent scan required again (no improvement from baseline)
- ⚠️ **Delayed gratification:** Student doesn't see results immediately after test

**Moments of Delight:**
- ✅ **Clear progress:** Ramp-up metrics show measurable improvement (e.g., "identification accuracy: 40% → 81%")
- ✅ **Transfer validation:** Demonstrates whether recognition skill transfers to new problems
- ✅ **Success criteria met:** Visual confirmation of meeting targets (green checkmarks)

**Verdict:** Transfer test workflow is sound for measuring intervention effectiveness. Recommended improvement: Consider allowing student to type answers directly for immediate feedback (optional online mode).

---

## 2. Pedagogical Effectiveness

### 2.1 Recognition-First Approach ✅ **Strong**

**Core Concept:** Teach students to identify problem type (pathway) and articulate equation shadow BEFORE solving.

**Why This Works:**
1. **Metacognitive skill building:** Students develop "pattern recognition" rather than memorizing formulas
2. **Transferability:** Recognition skill applies to unseen problems within same pathway
3. **Reduces careless errors:** Explicit articulation prevents jumping to wrong approach
4. **PSLE alignment:** PSLE often tests which approach to apply, not just calculation

**Evidence from API:**
- ✅ `POST /practice` endpoint requires `pathwayType` and `equationShadow` before `studentAnswer`
- ✅ Triad feedback (`POST /practice-sessions/{id}/submit` response) evaluates all three dimensions
- ✅ Rubrics (Section 2.2) have 3-level articulation criteria (Vague/Partial/Clear)
- ✅ Pathway radar warm-up (Section 2.7) builds pure recognition muscle

**Potential Weakness:**
- ⚠️ **Over-reliance on articulation:** Students who can solve correctly but cannot articulate well may be penalized
- ⚠️ **Language barrier:** P6 students with weaker language skills may struggle to express "equation shadow"

**Verdict:** Recognition-first approach is pedagogically sound and innovative. It addresses a gap in traditional math instruction (teaching which approach to apply, not just how to execute). Recommended improvement: Allow students to use dropdown templates for equation shadows after first few attempts (to reduce language burden while still checking understanding).

### 2.2 Triad Feedback System ✅ **Strong**

**The Three Dimensions:**
1. **Pathway Identification:** Did student correctly identify problem type?
2. **Articulation:** Did student clearly explain equation shadow and cues?
3. **Solution:** Did student solve correctly?

**Feedback Quality (from API spec):**
```json
{
  "feedback": {
    "pathwayIdentification": {
      "correct": true,
      "confidence": 0.95
    },
    "articulation": {
      "level": 2,
      "feedback": "Good articulation! You described the sequential changes clearly."
    },
    "solution": {
      "correct": true,
      "score": 1.0
    },
    "overall": "green"
  }
}
```

**Why This Works:**
1. **Granular feedback:** Student knows exactly which dimension succeeded/failed
2. **Specific guidance:** Articulation feedback provides actionable next steps
3. **Overall color coding:** Green/Yellow/Red provides at-a-glance assessment
4. **Builds metacognition:** Student learns to self-evaluate across dimensions

**Potential Weakness:**
- ⚠️ **Feedback generality:** Current articulation feedback is generic ("Good articulation!")
- ⚠️ **No exemplars:** API doesn't provide model articulations for comparison

**Verdict:** Triad feedback system is well-designed and pedagogically valuable. Recommended improvement: Add "model articulation" field to feedback response showing ideal articulation for comparison.

### 2.3 Pathway Radar Warm-Up ✅ **Adequate**

**Purpose:** Rapid recognition training (identification only, no solving)

**Design (from API spec):**
- 10 mixed pathway questions per day
- 30 seconds per question (5 minutes total)
- No solving required
- Feedback on strong/weak pathways

**Why This Works:**
1. **Time-efficient:** 5 minutes is manageable daily commitment
2. **Pure recognition:** Focuses entirely on pathway identification skill
3. **Mixed practice:** Prevents over-specialization on single pathway
4. **Immediate feedback:** Students see which pathways need focus

**Potential Weakness:**
- ⚠️ **Tedious repetition:** Same format every day may become boring
- ⚠️ **No variety:** Always 10 questions, always 30 seconds

**Verdict:** Pathway radar is functional but lacks engagement. Recommended improvement: Vary question count (5-15) and time limits (15-45 seconds) to maintain freshness. Consider adding "streak" tracking for consecutive correct identifications.

### 2.4 5-Week Timeline ✅ **Realistic**

**Breakdown:**
- Week 1: Baseline (40 problems)
- Weeks 2-4: Daily intervention (10 problems/pathway × 3 pathways = 90 problems)
- Week 5: Transfer test (40 problems)

**Volume Analysis:**
- **Total practice problems:** 90 problems over 18 days = **5 problems/day**
- **Per pathway:** 30 problems over 6 days = **5 problems/day**
- **Daily commitment:** 20 minutes (5 min warm-up + 15 min practice)

**Is This Enough for Improvement?**
- ✅ **Yes, for recognition skills:** 30 problems/pathway is sufficient to build pattern recognition
- ✅ **Yes, for PSLE context:** Focused intervention beats unfocused practice
- ⚠️ **Marginal for deep fluency:** 30 problems may not build full automaticity, but recognition skill should transfer

**Evidence from API:**
- ✅ Milestone tracking (`GET /milestones`, `PATCH /milestones/{id}`) supports progress monitoring
- ✅ Transfer analytics (`GET /analytics/transfer`) compare baseline vs. transfer performance
- ✅ Success criteria (90% ID accuracy, 90% articulation Level 2+, 80% solving improvement) are achievable

**Verdict:** 5-week timeline is realistic and appropriate for pilot. Recognition skills should develop sufficiently for measurable improvement. Recommended improvement: If student exceeds success criteria by Week 4, allow early progression to Week 5 transfer test (adaptive pacing).

---

## 3. Engagement Factors

### 3.1 Gamification Elements ⚠️ **Minimal**

**Current Implementation:**
- ❌ No points, badges, levels, or achievements
- ❌ No leaderboard or social comparison
- ❌ No streak tracking
- ✅ Progress visibility (milestones, "5/10 problems complete")
- ✅ Color-coded feedback (green/yellow/red)
- ✅ Radar visualization (strengths/weaknesses)

**Impact on Engagement:**
- ⚠️ **Lower intrinsic motivation:** Without gamification, students may view daily practice as "homework"
- ⚠️ **No reward mechanism:** No sense of achievement beyond progress bars
- ✅ **Extrinsic motivation:** Success criteria (meet targets by Week 5) provides goal

**Verdict:** Gamification is minimal but not critical for pedagogical effectiveness. Recommended improvement (Priority 3): Add simple streak counter for consecutive days of practice, and achievement badges for milestones ("First Week Complete", "Mastered Before-After Change").

### 3.2 Visual Appeal ✅ **Adequate**

**Diagrams (from API spec):**
- ✅ TikZ renders for geometry diagrams (high-quality SVG)
- ✅ Matplotlib for bar models, graphs, pie charts
- ✅ Embedded directly in problem display
- ✅ Multiple formats (SVG/PNG/PDF)

**Radar Visualization:**
- ✅ Feedback shows "strongPathways" and "weakPathways"
- ✅ Accuracy metrics (e.g., 80% correct)
- ⚠️ **No actual radar chart:** API returns text-based feedback, not visual radar plot

**Progress Visualization:**
- ✅ Milestone tracking shows problems completed vs. total
- ✅ Overall metrics (identification accuracy, articulation level)
- ⚠️ **No trend line:** API doesn't provide progress over time visualization

**Verdict:** Visual elements are functional but could be enhanced. Recommended improvement: Generate actual radar chart (SVG) for warm-up feedback, and add progress line chart for tracking improvement over time.

### 3.3 Feedback Immediacy ✅ **Excellent**

**Current Implementation:**
- ✅ Instant feedback after each problem submission
- ✅ Triad feedback covers all three dimensions
- ✅ Specific feedback text (e.g., "Good articulation! You described the sequential changes clearly.")
- ✅ Recommended next steps provided

**Example Feedback (from API spec):**
```json
{
  "recommendedNextSteps": [
    "Practice another before-after change problem",
    "Try articulating the equation shadow more precisely"
  ]
}
```

**Impact on Engagement:**
- ✅ **High:** Immediate feedback creates sense of progress
- ✅ **High:** Specific guidance reduces frustration
- ✅ **High:** Next steps provide clear direction

**Verdict:** Feedback immediacy is excellent. This is a key strength of the MVP.

### 3.4 Progress Visibility ✅ **Adequate**

**Current Implementation:**
- ✅ Milestone status ("in-progress", "completed")
- ✅ Problems completed vs. total (e.g., "5/10")
- ✅ Average score and accuracy metrics
- ✅ Pathway identification accuracy and articulation level

**Example Milestone Data (from API spec):**
```json
{
  "id": "mile_001",
  "status": "in-progress",
  "problemsCompleted": 5,
  "problemsTotal": 10,
  "averageScore": 0.8,
  "pathwayIdentificationAccuracy": 0.9,
  "articulationLevel": 2
}
```

**Impact on Engagement:**
- ✅ **Moderate:** Students see progress but no cumulative view
- ⚠️ **No overall progress:** API doesn't aggregate across pathways
- ⚠️ **No prediction:** No estimate of when success criteria will be met

**Verdict:** Progress visibility is adequate but could be enhanced. Recommended improvement: Add dashboard showing overall progress toward success criteria (e.g., "85% of 90% target").

---

## 4. Practicality Assessment

### 4.1 Single-Student vs. Multi-Student Implications ✅ **Well-Designed for Pilot**

**Current Design (from API spec):**
- ✅ Explicitly designed for single-student pilot
- ✅ No authentication or student ID required
- ✅ All endpoints operate on single student's data
- ✅ Clear path to multi-student support (add `studentId` parameter)

**Verdict:** Single-student design is appropriate for pilot. Multi-student support can be added in production.

### 4.2 Local-First Deployment ✅ **Appropriate**

**Current Design:**
- ✅ All file storage is local (`artifacts/` directory)
- ✅ No cloud dependencies or paid APIs
- ✅ Tesseract OCR and TikZ/Matplotlib are open-source
- ✅ Backend is simple Flask/FastAPI

**Accessibility for Target Students:**
- ✅ **High:** Any modern browser (Chrome, Safari, Edge) on laptop/tablet
- ✅ **High:** No internet connectivity required for core functionality
- ✅ **Moderate:** Requires technical parent/teacher to set up local server
- ⚠️ **Low:** Requires parent/teacher involvement for scan uploads

**Verdict:** Local-first design is appropriate for pilot but requires technical setup. Recommended improvement: Create one-click installation script for non-technical parents/teachers.

### 4.3 Technical Requirements ✅ **Minimal**

**Requirements (from API spec):**
- Backend: Flask or FastAPI (lightweight)
- OCR: Tesseract (open-source)
- Rendering: TikZ (LaTeX) + Matplotlib (Python)
- Frontend: Static HTML5 + JavaScript (no framework overhead)
- Browser: Any modern browser

**Deployment Complexity:**
- ⚠️ **Moderate:** Requires Python environment + LaTeX (for TikZ)
- ⚠️ **Moderate:** Tesseract installation varies by OS
- ✅ **Low:** Frontend is static files, no build process

**Verdict:** Technical requirements are minimal but may be challenging for non-technical parents/teachers. Recommended improvement: Provide Docker container for one-click deployment (all dependencies pre-installed).

### 4.4 Parent/Teacher Involvement Requirements ⚠️ **High**

**Current Requirements:**
- ⚠️ **Week 1:** Parent must scan and upload baseline test
- ⚠️ **Week 5:** Parent must scan and upload transfer test
- ⚠️ **Low OCR confidence:** Parent/teacher may need to manually correct OCR text
- ⚠️ **Technical setup:** Parent/teacher may need to set up local server

**Impact on Practicality:**
- ⚠️ **Moderate:** Students cannot complete baseline/transfer tests independently
- ⚠️ **Moderate:** Parents/teachers with limited time may find this burdensome
- ⚠️ **Low:** Non-technical parents/teachers may struggle with setup

**Verdict:** Parent/teacher involvement is a significant friction point. This is the **top practical issue** blocking MVP adoption. Recommended improvement (Priority 1): Allow students to type answers directly into MVP interface for online baseline/transfer tests (fallback to scan for offline preference).

---

## 5. Answering Key Questions

### Question 1: Is the MVP practical yet powerful enough to improve student's learning?

**Answer:** ✅ **Yes, with minor improvements.**

**Practicality:**
- ✅ Daily 20-minute commitment is reasonable
- ✅ Technical requirements are minimal (local-first, no cloud)
- ⚠️ Parent/teacher involvement for scans is friction point (see Priority 1 recommendation)

**Power:**
- ✅ Recognition-first approach is novel and pedagogically sound
- ✅ Triad feedback system provides granular, actionable insights
- ✅ 30 problems/pathway over 6 days is sufficient for skill development
- ✅ Success criteria (90% ID accuracy, 90% articulation Level 2+, 80% solving improvement) are achievable

**Will the workflow make sense from a student's perspective?**
- ✅ **Yes:** Read → Identify → Articulate → Solve → Feedback is logical
- ✅ **Yes:** Forced articulation becomes natural after first few attempts
- ✅ **Yes:** Pathway radar warm-up builds recognition muscle

**Are the features balanced between simplicity and power?**
- ✅ **Yes:** 5-minute warm-up + 15-minute practice is balanced
- ✅ **Yes:** Triad feedback is comprehensive but not overwhelming
- ✅ **Yes:** Local-first design keeps technical complexity low

**Will the triad feedback actually help students improve?**
- ✅ **Yes:** Granular feedback shows exactly which dimension succeeded/failed
- ✅ **Yes:** Specific articulation feedback provides actionable guidance
- ✅ **Yes:** Recommended next steps provide clear direction
- ⚠️ **Improvement needed:** Add model articulations for comparison (see Priority 2 recommendation)

**Is the 5-week timeline realistic for measurable improvement?**
- ✅ **Yes:** 30 problems/pathway over 6 days is sufficient for recognition skill development
- ✅ **Yes:** Recognition skill should transfer to unseen problems
- ✅ **Yes:** Success criteria are ambitious but achievable

### Question 2: Will students find it helpful and engaging?

**Answer:** ⚠️ **Mostly helpful, somewhat engaging.**

**Helpfulness:**
- ✅ **High:** Recognition-first approach addresses a gap in traditional instruction
- ✅ **High:** Triad feedback provides specific, actionable guidance
- ✅ **High:** Progress visibility shows improvement over time
- ✅ **High:** Immediate feedback reduces frustration

**Engagement:**
- ⚠️ **Moderate:** No gamification elements (points, badges, streaks)
- ⚠️ **Moderate:** Pathway radar may become repetitive
- ✅ **High:** Quick wins from 5-minute warm-up
- ✅ **High:** "Aha" moments from forced articulation
- ✅ **High:** Visual radar feedback is engaging
- ✅ **High:** Diagram renders are high-quality

**Are the practice sessions engaging or tedious?**
- ⚠️ **Mixed:** 15-minute practice session is appropriate length, but 30 problems/pathway may feel repetitive
- ✅ **Engaging:** Forced articulation creates "aha" moments
- ✅ **Engaging:** Instant feedback provides gratification

**Does the "forced articulation" feel like a chore or a learning aid?**
- ✅ **Learning aid:** After first 2-3 attempts, students understand why articulation matters
- ✅ **Learning aid:** Provides structure for problem-solving
- ⚠️ **Potential chore:** Students who struggle with language may find typing articulations difficult

**Is the pathway radar warm-up fun or boring?**
- ⚠️ **Mixed:** 5-minute format is quick, but same structure every day may become boring
- ✅ **Fun element:** "Game" aspect of rapid identification is engaging
- ✅ **Fun element:** Immediate feedback on strong/weak pathways
- ⚠️ **Improvement needed:** Vary question count and time limits to maintain freshness

**Will students want to use this daily?**
- ✅ **Yes, for motivated students:** Clear progress and success criteria provide motivation
- ⚠️ **Maybe, for unmotivated students:** Lack of gamification may reduce intrinsic motivation
- ⚠️ **Depends on parent involvement:** Students with supportive parents are more likely to maintain daily practice

**Are the visual elements (diagrams, renders) engaging?**
- ✅ **Yes:** TikZ/Matplotlib renders are high-quality
- ✅ **Yes:** Embedded diagrams are clear and helpful
- ⚠️ **Improvement needed:** Generate actual radar chart (not just text feedback)

---

## 6. Critical Issues Blocking Deployment

### Priority 1 (Before Pilot Launch): Reduce Student Dependency on Parent/Teacher for Scans

**Issue:** Students cannot complete baseline and transfer tests without parent/teacher involvement (scan upload).

**Impact:**
- ⚠️ **High friction:** Students who want to practice independently are blocked
- ⚠️ **Time burden:** Parents/teachers with limited schedules may not be available to scan
- ⚠️ **Technical barrier:** Non-technical parents/teachers may struggle with scan workflow

**Recommended Solution:**
1. Add **online mode** for baseline and transfer tests:
   - Student types answers directly into MVP interface
   - No scan upload required
   - Immediate feedback (no OCR processing delay)
2. Keep **offline mode** as fallback:
   - Parent/teacher scans and uploads (current workflow)
   - Useful for students who prefer paper-based tests

**Implementation:**
- Add new endpoint: `POST /answers/online` (submit typed answers directly)
- Update frontend to provide mode selection (online vs. offline)
- No backend changes required for offline mode (already implemented)

### Priority 2 (During Pilot): Enhance Articulation Feedback Specificity

**Issue:** Current articulation feedback is generic (e.g., "Good articulation!"). Students don't see model articulations to compare against.

**Impact:**
- ⚠️ **Reduced learning value:** Students cannot learn from ideal articulations
- ⚠️ **Slower improvement:** Without exemplars, students may struggle to improve articulation quality

**Recommended Solution:**
1. Add **model articulation** field to `POST /practice-sessions/{id}/submit` response:
   ```json
   {
     "feedback": {
       "articulation": {
         "level": 2,
         "studentArticulation": "After first change, then after second change, find original.",
         "modelArticulation": "This is a Before-After Change problem. First, 3/5 of pens were sold, leaving 2/5. Then, 1/4 of the remaining 2/5 was sold. The equation shadow is: original × (1 - 3/5) × (1 - 1/4) = 150. The cues are: 'sold 3/5' (first change), 'remainder' (indicates sequential change), 'had 150 left' (final state).",
         "comparison": "Good! You correctly identified the sequential change pattern. Try to be more specific about the equation shadow structure."
       }
     }
   }
   ```
2. Update frontend to display side-by-side comparison (student vs. model)

**Implementation:**
- Backend: Pre-populate `modelArticulation` field in rubric data (stored with problem/rubric)
- Backend: Return `modelArticulation` and `comparison` in feedback response
- Frontend: Display model articulation for student to review

### Priority 3 (Post-Pilot): Add Minimal Gamification Elements

**Issue:** No points, badges, streaks, or achievements. Students may view daily practice as "homework" without intrinsic motivation.

**Impact:**
- ⚠️ **Lower engagement:** Unmotivated students may not maintain daily practice
- ⚠️ **Reduced completion:** Without extrinsic motivation, some students may abandon pilot

**Recommended Solution:**
1. Add **streak counter** for consecutive days of practice:
   - Track days since first practice session
   - Reset streak if practice is missed
   - Display streak on dashboard
2. Add **achievement badges** for milestones:
   - "First Week Complete" (complete Week 2 practice)
   - "Mastered Before-After Change" (articulation Level 3 on 10 problems)
   - "7-Day Streak" (practice for 7 consecutive days)
3. Add **simple points** for activities:
   - 10 points per completed problem
   - 50 points per completed warm-up (10 questions)
   - Leaderboard is NOT needed (single-student pilot)

**Implementation:**
- Backend: Add `streak` and `badges` fields to student data model
- Backend: Track practice history for streak calculation
- Backend: Add `POST /achievements` endpoint to award badges
- Frontend: Display streak, badges, and points on dashboard

---

## 7. Strengths & Opportunities for Enhancement

### Core Strengths (What to Keep)

1. **Novel Pedagogical Approach:** Recognition-first training is innovative and addresses a gap in traditional instruction
2. **Triad Feedback System:** Granular feedback on pathway identification, articulation, and solution is excellent
3. **Realistic Timeline:** 5-week intervention with 30 problems/pathway is sufficient for measurable improvement
4. **Clear Success Criteria:** 90% ID accuracy, 90% articulation Level 2+, 80% solving improvement are achievable targets
5. **Local-First Design:** No cloud dependencies or paid APIs reduces cost and complexity
6. **Immediate Feedback:** Instant triad feedback provides gratification and guidance
7. **Pathway Radar Warm-Up:** 5-minute rapid recognition training builds muscle memory
8. **Data-Driven:** Gap map from baseline objectively identifies weakest pathways

### Opportunities for Enhancement (What to Improve)

1. **Student Independence:** Allow students to complete baseline/transfer tests online (no scan dependency)
2. **Feedback Specificity:** Add model articulations for comparison
3. **Gamification:** Add streak counter, achievement badges, and simple points
4. **Visual Engagement:** Generate actual radar chart (not just text feedback)
5. **Adaptive Pacing:** Allow early progression to transfer test if success criteria met early
6. **Template Support:** Allow students to use dropdown templates for equation shadows (after first few attempts)
7. **Progress Dashboard:** Add overall progress view toward success criteria
8. **Variety:** Vary warm-up question count (5-15) and time limits (15-45 seconds) to maintain freshness

---

## 8. Final Verdict

### Overall Assessment: ✅ **APPROVE** with recommendations

**Decision:** The ATOM-SG Pilot MVP is **practical, powerful enough to improve learning, and will be engaging for students** when implemented with the recommended enhancements.

**Why Approve?**
1. ✅ **Novel pedagogical approach:** Recognition-first training is innovative and addresses a gap in traditional instruction
2. ✅ **Triad feedback system:** Granular feedback is excellent for learning
3. ✅ **Realistic timeline:** 5-week intervention is sufficient for measurable improvement
4. ✅ **Clear success criteria:** Targets are achievable and measurable
5. ✅ **Local-first design:** Appropriate for pilot, reduces cost and complexity
6. ✅ **Immediate feedback:** Provides gratification and guidance

**Why Recommendations?**
1. ⚠️ **Priority 1:** Reduce student dependency on parent/teacher for scans (friction point)
2. 🎨 **Priority 2:** Enhance articulation feedback specificity (improves learning value)
3. 🎯 **Priority 3:** Add minimal gamification elements (improves engagement)

### Recommendations Summary

| Priority | Recommendation | Impact | Effort | Timeline |
|----------|----------------|--------|--------|----------|
| **1** | Allow online baseline/transfer tests (no scan dependency) | High | Medium | Before pilot launch |
| **2** | Add model articulations for comparison | Medium | Low | During pilot |
| **3** | Add minimal gamification (streaks, badges, points) | Medium | Medium | Post-pilot |

### Next Steps

1. **Immediate (Before Pilot Launch):**
   - Implement Priority 1 recommendation (online mode for baseline/transfer tests)
   - Create one-click installation script for non-technical parents/teachers

2. **During Pilot:**
   - Implement Priority 2 recommendation (model articulations)
   - Monitor student engagement and feedback
   - Adjust practice difficulty based on performance

3. **Post-Pilot:**
   - Implement Priority 3 recommendation (gamification elements)
   - Analyze effectiveness of recognition-first approach
   - Scale to multi-student support for production

### Expected Outcomes

If implemented with recommendations, the MVP should achieve:
- ✅ **90%+ pathway identification accuracy** on trained pathways
- ✅ **90%+ articulation Level 2+ rate** on trained pathways
- ✅ **80%+ solving improvement** from baseline on trained pathways
- ✅ **80%+ transfer accuracy** on trained pathways (first 3 items)
- ✅ **Daily practice engagement** for motivated students

---

**Reviewer Confidence:** **High** — The MVP has a strong pedagogical foundation, realistic timeline, and appropriate scope. The recommendations address the primary practical issues without compromising core pedagogy.

**Risk Assessment:** **Low** — The main risk is student dependency on parent/teacher for scans (Priority 1). This is addressable with online mode. Other risks (engagement, technical setup) are manageable with minimal enhancements.

**Recommendation for Stakeholders:** Proceed with pilot deployment, implementing Priority 1 recommendation before launch. Monitor student engagement during pilot and implement Priority 2 and 3 recommendations based on feedback.

---

*This review was conducted by the independent MVP UX & Pedagogical Reviewer subagent using GLM 5.1 for complex reasoning and high-stakes decision-making.*

---

## ✅ BackendBot Resolution (2026-04-14 20:20 SGT)

**Action:** Implemented all 4 missing endpoints as requested by API Reviewer.

**Endpoints Added:**
1. ✅ **GET /renders** — List all available renders with optional filtering (`problemId`, `format`)
2. ✅ **POST /practice** — Submit individual practice attempt (recognition-first loop), with clear distinction from session-based approach
3. ✅ **POST /collision** — Cross-thread collision detection for Week 3+, with comprehensive analysis and intervention recommendations
4. ✅ **GET /interpretation** — Data interpretation results for Week 3+, including red herring analysis and recommendations

**Additional Updates:**
- ✅ Updated API status to "Ready for Independent Review (all endpoints implemented)"
- ✅ Updated section numbering to reflect new Advanced Analytics section (2.8)
- ✅ Expanded File Storage Structure to include `collision/` and `interpretation/` directories
- ✅ Added comprehensive Design Decisions & Trade-offs section (Section 7)
- ✅ Updated Key Workflows to include Collision Detection and Data Interpretation flows

**Design Decisions Documented:**
- Dual endpoint approach for practice (session-based vs. standalone) with clear use cases
- Collision detection algorithm design with storage and performance considerations
- Interpretation analysis design with red herring type detection
- Renders list endpoint design with filtering and caching strategy

**Status:** ✅ All critical MVP endpoints now implemented. API spec ready for independent review.

---

## 9. Frontend Visualization Enhancements (Post-MVP)

### 9.1 Pathway Radar Chart Visualization

**Recommendation from MVP-UX Reviewer (Low severity, Post-MVP priority)**

**Current State:**
- Pathway Radar API (`GET /pathway-radar/questions`, `POST /pathway-radar/submit`) returns text-based feedback only
- No visual chart showing pathway identification accuracy or trends over time
- Students receive strong/weak pathway lists in text format

**Issue:** Lack of visual engagement may reduce student motivation and make progress less tangible


**Proposed Enhancement:**
- **Implementation:** Frontend-only enhancement using Chart.js or D3.js
- **Visual Component:** Radar chart showing:
  - Pathway identification accuracy per pathway (x-axis: pathway types, y-axis: accuracy %)
  - Trends over time (multiple radar chart snapshots showing improvement)
  - Color coding: Green (strong, ≥80%), Yellow (moderate, 60-79%), Red (weak, <60%)
- **Data Source:** Use `POST /pathway-radar/submit` response plus historical data from `GET /analytics/progress`
- **Benefits:**
  - Visual progress tracking (students can see improvement at a glance)
  - Increased engagement (gamification element through visual progress)
  - Metacognitive awareness (students understand which pathways need focus)

**Implementation Notes:**
- Client-side rendering (no backend changes required)
- Cache radar chart data locally for performance
- Responsive design for mobile/tablet/desktop

---
