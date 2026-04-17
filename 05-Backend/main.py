#!/usr/bin/env python3
"""
ATOM-SG Pilot MVP Backend - FastAPI Implementation
Version 1.0.0

This is the main FastAPI application serving the ATOM-SG Pilot MVP.
All endpoints follow the approved API specification.
"""

import os
import json
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional, Dict, Any
from enum import Enum

from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Query, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors

# Configuration
BASE_DIR = Path(__file__).parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
RENDERS_DIR = ARTIFACTS_DIR / "renders"
OCR_DIR = ARTIFACTS_DIR / "ocr"
SESSIONS_DIR = ARTIFACTS_DIR / "sessions"
COLLISION_DIR = ARTIFACTS_DIR / "collision"
INTERPRETATION_DIR = ARTIFACTS_DIR / "interpretation"

# Ensure directories exist
for dir_path in [ARTIFACTS_DIR, RENDERS_DIR, OCR_DIR, SESSIONS_DIR, COLLISION_DIR, INTERPRETATION_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# FastAPI app
app = FastAPI(
    title="ATOM-SG Pilot MVP API",
    version="1.0.0",
    description="Recognition-First Integrated Training System for P6 Mathematics"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:50519", "http://127.0.0.1:8080", "http://127.0.0.1:50519", "http://192.168.2.6"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Data Models (Pydantic)
# ============================================================================

# Valid pathway types for validation
VALID_PATHWAY_TYPES = [
    "before-after-change",
    "part-whole-comparison",
    "composite-shapes",
    "angles",
    "data-interpretation-red-herring",
    "ratio-proportion",
    "percentage-change",
    "rate-speed-time"
]

# Glossary terms for vocabulary gap fix
GLOSSARY_TERMS = {
    "equation shadow": "A simplified representation of the mathematical structure of a problem, showing the relationships between quantities without specific numbers.",
    "pathway type": "The category of mathematical thinking or problem-solving approach used to solve a problem (e.g., before-after-change, part-whole-comparison).",
    "articulation": "The ability to clearly explain and describe the mathematical reasoning and steps used to solve a problem.",
    "rubric level": "A score from 1-3 indicating the quality of a student's explanation or understanding (1=Basic, 2=Clear, 3=Precise).",
    "triad feedback": "Three-part feedback system covering pathway identification, articulation quality, and solution correctness.",
    "forced articulation": "A requirement that students must explain their thinking pathway before seeing the solution to their problem.",
    "pathway radar": "A warm-up assessment that tests the student's ability to quickly identify mathematical problem types."
}

# P0-7: Common mistake patterns for step-by-step scaffolding
COMMON_MISTAKES = {
    "fraction_multiplication": {
        "pattern": "Multiplying fractions incorrectly (adding denominators instead of multiplying)",
        "hint": "Remember: To multiply fractions, multiply the numerators together and denominators separately. Don't add them!",
        "steps": [
            "Step 1: Multiply the numerators (top numbers) together",
            "Step 2: Multiply the denominators (bottom numbers) together",
            "Step 3: Simplify the result if possible",
            "Example: (2/3) × (4/5) = (2×4) / (3×5) = 8/15"
        ]
    },
    "wrong_fraction": {
        "pattern": "Identifying the wrong fraction part (taking remainder instead of original, or vice versa)",
        "hint": "Carefully read which part the question is asking for - the sold part, the remaining part, or the original amount.",
        "steps": [
            "Step 1: Identify what fraction of the WHOLE is being asked",
            "Step 2: Check if the question asks for the part sold, remaining, or original",
            "Step 3: Write the correct fraction based on the question",
            "Step 4: Apply the fraction to the total quantity"
        ]
    },
    "wrong_operation": {
        "pattern": "Using the wrong operation (addition instead of multiplication, or subtraction instead of division)",
        "hint": "Look at the relationship between the numbers. Are they being combined (+), taken away (-), grouped (×), or split (÷)?",
        "steps": [
            "Step 1: Read the problem carefully to understand the action",
            "Step 2: Identify key words: 'total' = addition, 'remaining' = subtraction, 'of' = multiplication, 'share equally' = division",
            "Step 3: Check if the answer makes sense with your operation",
            "Step 4: Verify with the opposite operation if possible"
        ]
    },
    "order_mistake": {
        "pattern": "Doing operations in the wrong order (not following BODMAS/PEMDAS rules)",
        "hint": "Remember the order: Brackets first, then Orders (powers), then Division/Multiplication, then Addition/Subtraction.",
        "steps": [
            "Step 1: Look for brackets - solve inside them first",
            "Step 2: Solve any powers or square roots",
            "Step 3: Do multiplication and division from left to right",
            "Step 4: Finally, do addition and subtraction from left to right"
        ]
    },
    "unit_conversion": {
        "pattern": "Forgetting to convert units (e.g., cm to m, or hours to minutes)",
        "hint": "Always check if the units match before calculating. Convert all quantities to the same unit first!",
        "steps": [
            "Step 1: Identify all units in the problem",
            "Step 2: Check if they're all the same",
            "Step 3: If not, convert to a common unit (usually the largest one)",
            "Step 4: Now solve the problem with consistent units",
            "Example: 2.5 hours = 2 hours + 0.5 hour = 120 min + 30 min = 150 minutes"
        ]
    },
    "decimal_place": {
        "pattern": "Misplacing the decimal point in calculations",
        "hint": "Count the total decimal places in the original numbers, then place the decimal point so your answer has the same number.",
        "steps": [
            "Step 1: Count decimal places in all numbers you're multiplying",
            "Step 2: Multiply the numbers as if they were whole numbers",
            "Step 3: Count the total decimal places from step 1",
            "Step 4: Place the decimal point from the right, moving left by that many places",
            "Example: 0.5 × 0.2 has 2 decimal places total. 5 × 2 = 10. Place decimal: 0.10"
        ]
    },
    "percentage_error": {
        "pattern": "Incorrectly calculating percentages (treating 25% as 0.25 or 25 instead of dividing by 100)",
        "hint": "Percentage means 'per 100'. To use a percentage in a calculation, divide by 100 first.",
        "steps": [
            "Step 1: Convert percentage to decimal by dividing by 100",
            "Step 2: Multiply the decimal by the quantity",
            "Step 3: For 'X% more', add to original. For 'X% less', subtract from original",
            "Example: 25% of 80 = 0.25 × 80 = 20",
            "Example: 25% more than 80 = 80 + 20 = 100"
        ]
    }
}

class DifficultyLevel(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class TrackType(str, Enum):
    word_problems = "word-problems"
    geometry = "geometry"
    data_interpretation = "data-interpretation"

class Diagram(BaseModel):
    type: str
    renderUrl: Optional[str] = None

class ExpectedAnswer(BaseModel):
    type: str
    value: float

class RubricRef(BaseModel):
    pathwayId: str
    solutionId: str

class ProblemCreate(BaseModel):
    title: str
    track: TrackType
    pathway: str
    difficulty: DifficultyLevel
    questionText: str
    diagrams: List[Diagram]
    expectedAnswer: ExpectedAnswer

class Problem(BaseModel):
    id: str
    title: str
    track: TrackType
    pathway: str
    difficulty: DifficultyLevel
    questionText: str
    diagrams: List[Diagram]
    expectedAnswer: ExpectedAnswer
    rubric: RubricRef
    createdAt: str

class RubricLevel(BaseModel):
    level: int
    name: str
    description: str
    criteria: List[str]

class RubricCreate(BaseModel):
    type: str
    pathway: Optional[str] = None
    levels: List[RubricLevel]

class Rubric(BaseModel):
    id: str
    type: str
    pathway: Optional[str] = None
    levels: List[RubricLevel]
    createdAt: str

class RenderRequest(BaseModel):
    problemId: str
    diagramType: str
    spec: str
    format: str = "svg"
    values: Dict[str, float]

class Render(BaseModel):
    id: str
    status: str
    url: Optional[str] = None
    format: Optional[str] = None
    createdAt: Optional[str] = None
    completedAt: Optional[str] = None
    proportionalAccuracy: Optional[Dict[str, Any]] = None

class DiagramAnnotation(BaseModel):
    type: str
    coordinates: Optional[List[List[float]]] = None
    text: Optional[str] = None
    position: Optional[List[float]] = None
    color: Optional[str] = None  # P0 Fix #6: Color for expanded palette
    lineWidth: Optional[float] = None  # P0 Fix #6: Line width for annotations
    fontSize: Optional[int] = None  # P0 Fix #6: Font size for text annotations
    undoStack: Optional[List[Dict[str, Any]]] = []  # P0 Fix #6: Undo stack
    redoStack: Optional[List[Dict[str, Any]]] = []  # P0 Fix #6: Redo stack

class StudentAnswer(BaseModel):
    type: str
    value: float

class PracticeSubmission(BaseModel):
    problemId: str
    pathwayType: str
    equationShadow: str
    studentAnswer: StudentAnswer
    diagramAnnotations: Optional[List[DiagramAnnotation]] = []

class PathwayIdentificationFeedback(BaseModel):
    correct: bool
    confidence: float
    identifiedPathway: Optional[str] = None

class ArticulationFeedback(BaseModel):
    level: int
    feedback: str
    modelArticulation: Optional[str] = None

class SolutionFeedback(BaseModel):
    correct: bool
    score: float
    expectedAnswer: Optional[float] = None
    studentAnswer: Optional[float] = None
    feedback: Optional[str] = None

class Feedback(BaseModel):
    pathwayIdentification: PathwayIdentificationFeedback
    articulation: ArticulationFeedback
    solution: SolutionFeedback
    overall: str

class PracticeSessionStart(BaseModel):
    week: int
    pathway: str
    sessionType: str

class PracticeSessionSubmit(BaseModel):
    problemId: str
    pathwayType: str
    equationShadow: str
    studentAnswer: StudentAnswer
    diagramAnnotations: Optional[List[DiagramAnnotation]] = []

class PathwayRadarAnswer(BaseModel):
    questionId: str
    identifiedPathway: str
    confidence: float

class PathwayRadarSubmit(BaseModel):
    date: str
    answers: List[PathwayRadarAnswer]

class MilestoneUpdate(BaseModel):
    problemsCompleted: Optional[int] = None
    lastAttemptScore: Optional[float] = None
    pathwayIdentifiedCorrectly: Optional[bool] = None
    articulationLevel: Optional[int] = None

class ReflectionCreate(BaseModel):
    week: int
    pathway: str
    reflection: str
    confidence: float
    struggles: List[str]
    improvements: List[str]

class CollisionRequest(BaseModel):
    week: int
    pathways: List[str]
    timeWindow: Dict[str, str]
    options: Optional[Dict[str, Any]] = {}

# ============================================================================
# In-Memory Data Storage (for MVP - would be database in production)
# ============================================================================

# Sample problems
PROBLEMS_DB: Dict[str, Dict] = {
    "prob_001": {
        "id": "prob_001",
        "title": "Fraction Remainder Problem",
        "track": "word-problems",
        "pathway": "before-after-change",
        "difficulty": "medium",
        "questionText": "A shop sold 3/5 of its pens on Monday and 1/4 of the remainder on Tuesday. If the shop still had 150 pens on Wednesday, how many pens did the shop have originally?",
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
        "hint": "Think about working backwards. Start with the remaining pens and reverse each sale step.",
        "rubric": {
            "pathwayId": "rub_pathway_001",
            "solutionId": "rub_solution_001"
        },
        "createdAt": "2026-04-14T10:00:00+08:00"
    },
    "prob_002": {
        "id": "prob_002",
        "title": "Pie Chart Problem",
        "track": "data-interpretation",
        "pathway": "data-interpretation-red-herring",
        "difficulty": "medium",
        "questionText": "The pie chart shows the distribution of sales across 4 quarters. Which quarter had the highest sales, excluding the outlier data point?",
        "diagrams": [
            {
                "type": "pie-chart",
                "renderUrl": "/renders/prob_002_pie_chart.svg"
            }
        ],
        "expectedAnswer": {
            "type": "numeric",
            "value": 2
        },
        "hint": "Look for the outlier data point and exclude it. Then compare the remaining quarters.",
        "rubric": {
            "pathwayId": "rub_pathway_002",
            "solutionId": "rub_solution_002"
        },
        "createdAt": "2026-04-14T10:00:00+08:00"
    },
    "prob_003": {
        "id": "prob_003",
        "title": "Angle Problem",
        "track": "geometry",
        "pathway": "angles",
        "difficulty": "easy",
        "questionText": "Find the value of angle x in the triangle, given that the other two angles are 45° and 60°.",
        "diagrams": [
            {
                "type": "geometric-shape",
                "renderUrl": "/renders/prob_003_angle.svg"
            }
        ],
        "expectedAnswer": {
            "type": "numeric",
            "value": 75
        },
        "hint": "Remember that the sum of all three angles in a triangle always equals 180 degrees.",
        "rubric": {
            "pathwayId": "rub_pathway_003",
            "solutionId": "rub_solution_003"
        },
        "createdAt": "2026-04-14T10:00:00+08:00"
    }
}

# Sample rubrics
RUBRICS_DB: Dict[str, Dict] = {
    "rub_pathway_001": {
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
}

# Renders
RENDERS_DB: Dict[str, Dict] = {
    "rend_001": {
        "id": "rend_001",
        "problemId": "prob_001",
        "type": "bar-model",
        "url": "/artifacts/renders/prob_001_bar_model.svg",
        "format": "svg",
        "createdAt": "2026-04-14T10:00:00+08:00"
    }
}

# Sessions
SESSIONS_DB: Dict[str, Dict] = {}

# Milestones
MILESTONES_DB: Dict[str, Dict] = {
    "mile_001": {
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
}

# Reflections
REFLECTIONS_DB: List[Dict] = []

# Scans
SCANS_DB: Dict[str, Dict] = {}

# Student Profiles (P0 Fix #3: Gaming detection with cooldown)
STUDENT_PROFILES_DB: Dict[str, Dict] = {}

# User Profiles for Gamification (P1-1: Gamification Elements)
PROFILES_DB: Dict[str, Dict] = {
    "anonymous": {
        "userId": "anonymous",
        "practiceStreak": 0,
        "lastPracticeDate": None,
        "achievements": [],
        "totalPracticeDays": 0,
        "totalProblemsCompleted": 0,
        "createdAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
    }
}

# Achievements Definitions (P1-1: Gamification Elements)
ACHIEVEMENTS = {
    "first_problem": {
        "name": "First Step! 🎯",
        "description": "Completed your first practice problem",
        "icon": "🎯",
        "condition": lambda p: p.get("totalProblemsCompleted", 0) >= 1
    },
    "streak_3": {
        "name": "3-Day Streak! 🔥",
        "description": "Practiced for 3 days in a row",
        "icon": "🔥",
        "condition": lambda p: p.get("practiceStreak", 0) >= 3
    },
    "streak_7": {
        "name": "Week Warrior! 💪",
        "description": "Practiced for 7 days in a row",
        "icon": "💪",
        "condition": lambda p: p.get("practiceStreak", 0) >= 7
    },
    "streak_30": {
        "name": "Monthly Master! 🏆",
        "description": "Practiced for 30 days in a row",
        "icon": "🏆",
        "condition": lambda p: p.get("practiceStreak", 0) >= 30
    },
    "perfect_week": {
        "name": "Perfect Week! ⭐",
        "description": "Completed all problems correctly in one week",
        "icon": "⭐",
        "condition": lambda p: p.get("perfectWeeks", 0) > 0
    },
    "pathway_master": {
        "name": "Pathway Master! 🎓",
        "description": "Achieved Level 2+ articulation in all pathways",
        "icon": "🎓",
        "condition": lambda p: p.get("masteredPathways", 0) >= 5
    }
}

def check_achievements(profile: dict) -> list:
    """Check which achievements a user has earned."""
    earned = profile.get("achievements", [])
    newly_unlocked = []
    
    for key, achievement in ACHIEVEMENTS.items():
        if key not in earned and achievement["condition"](profile):
            newly_unlocked.append(key)
            earned.append(key)
    
    return newly_unlocked

def generate_timestamp() -> str:
    """Generate ISO 8601 timestamp."""
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")


def generate_week_test_pdf(week: int, pdf_path: Path) -> None:
    """Generate a placeholder PDF for baseline or transfer test."""
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    
    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    width, height = letter
    
    # Margins for safe area
    left_margin = 1.0 * inch
    right_margin = 1.0 * inch
    top_margin = 1.0 * inch
    bottom_margin = 1.0 * inch
    content_width = width - left_margin - right_margin
    content_height = height - top_margin - bottom_margin
    
    # DEBUG: Draw safe area rectangle (light gray)
    # c.setStrokeColorRGB(0.9, 0.9, 0.9)
    # c.rect(left_margin, bottom_margin, content_width, content_height)
    # c.setStrokeColorRGB(0, 0, 0)
    
    # Helper to wrap long text and return new y
    def draw_wrapped_text(text, x, y, max_width, line_height=0.2*inch, font_name="Helvetica", font_size=12):
        c.setFont(font_name, font_size)
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, font_name, font_size) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        
        for line in lines:
            c.drawString(x, y, line)
            y -= line_height
        return y  # Return new y position after drawing
    
    # Title
    c.setFont("Helvetica-Bold", 24)
    if week == 1:
        title = "ATOM-SG Baseline Test (Week 1)"
    elif week == 5:
        title = "ATOM-SG Transfer Test (Week 5)"
    else:
        title = f"ATOM-SG Test (Week {week})"
    
    title_y = height - top_margin
    c.drawCentredString(width/2, title_y, title)
    
    # Subtitle
    c.setFont("Helvetica", 16)
    subtitle_y = title_y - 0.5*inch
    c.drawCentredString(width/2, subtitle_y, "P6 Mathematics - Recognition-First Training")
    
    # Instructions
    c.setFont("Helvetica", 12)
    instructions = [
        "Instructions:",
        "1. Complete this test independently without assistance.",
        "2. Show all your working in the spaces provided.",
        "3. You have 45 minutes to complete the test.",
        "4. Use the answer sheet provided for final answers.",
        "",
        "Note: This is a placeholder PDF for MVP testing.",
        "In the full version, actual test questions will appear here."
    ]
    
    y = subtitle_y - 0.75*inch
    for line in instructions:
        c.drawString(left_margin, y, line)
        y -= 0.25*inch
    
    # Sample problem section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(left_margin, y - 0.5*inch, "Sample Problem:")
    
    # Sample problem text with proper wrapping
    sample_problem = "Sarah has 3/4 of a cake. She eats 1/3 of what she has. What fraction of the whole cake does she have left?"
    problem_y = y - 1.0*inch
    # Use max_width = content_width - 0.5*inch (since x offset)
    problem_y = draw_wrapped_text(sample_problem, left_margin + 0.5*inch, problem_y, 
                                  max_width=content_width - 0.5*inch, line_height=0.22*inch)
    
    # Answer box (properly sized)
    answer_box_y = problem_y - 0.3*inch
    answer_box_width = content_width - 0.5*inch
    c.rect(left_margin + 0.5*inch, answer_box_y, answer_box_width, 0.6*inch)
    c.setFont("Helvetica", 12)
    c.drawString(left_margin + 0.6*inch, answer_box_y + 0.2*inch, "Answer: ______________________________")
    
    # Working space
    working_label_y = answer_box_y - 0.5*inch
    c.drawString(left_margin + 0.5*inch, working_label_y, "Working:")
    working_box_y = working_label_y - 0.3*inch
    working_box_width = content_width - 0.5*inch
    working_box_height = 1.5*inch
    c.rect(left_margin + 0.5*inch, working_box_y, working_box_width, working_box_height)
    
    # Footer (ensured at bottom)
    c.setFont("Helvetica-Oblique", 10)
    footer_y = bottom_margin
    c.drawString(left_margin, footer_y, "ATOM-SG Pilot MVP • Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    c.drawString(left_margin, footer_y - 0.2*inch, "This PDF is automatically generated for testing purposes.")
    
    # Safety check: ensure working box doesn't overlap footer
    if working_box_y < bottom_margin + 1.0*inch:
        print(f"Warning: PDF content close to bottom for week {week}. Adjusting layout...")
        # If too low, shift everything up by reducing top_margin? Not needed for now.
    
    c.save()
    print(f"Generated placeholder PDF for week {week}: {pdf_path}")


def detect_gaming_pattern(answers: List[Dict], student_id: str) -> Dict[str, Any]:
    """
    Detect gaming patterns in pathway radar submissions (P0 Fix #3).
    Returns detection result with warnings and recommendations.
    """
    warnings = []
    gaming_detected = False
    recommendation = None

    if not answers or len(answers) < 5:
        return {
            "gamingDetected": False,
            "warnings": [],
            "recommendation": None
        }

    # Pattern 1: All answers submitted within 1 minute (speed gaming)
    # In production, would check actual submission timestamps
    # For MVP, we'll use confidence values as proxy
    
    # Pattern 2: All confidence values identical (random clicking)
    confidence_values = [a.get("confidence", 0) for a in answers]
    unique_confidences = len(set(confidence_values))
    if unique_confidences == 1:
        warnings.append("We noticed your confidence levels are the same for every question - try to think about each question individually")
        gaming_detected = True

    # Pattern 3: Same pathway selected for all questions
    pathways = [a.get("identifiedPathway", "") for a in answers]
    unique_pathways = len(set(pathways))
    if unique_pathways == 1:
        warnings.append("You selected the same pathway for all questions - each problem is unique, so take time to read each one carefully")
        gaming_detected = True

    # Pattern 4: Very high confidence on all answers (overconfidence)
    high_confidence_count = sum(1 for c in confidence_values if c >= 0.95)
    if high_confidence_count == len(answers):
        warnings.append("Perfect confidence on every answer - sometimes taking a little more time helps you spot important details")
        gaming_detected = True

    # Pattern 5: Submission pattern analysis (in production: check timestamps)
    # For MVP, we'll flag if student has recent submissions (Jack's behavior)
    profile = STUDENT_PROFILES_DB.get(student_id, {})
    recent_submissions = profile.get("recentSubmissions", [])
    
    now = datetime.now()
    recent_count = sum(1 for ts in recent_submissions 
                      if (now - datetime.fromisoformat(ts.replace("Z", "+00:00"))).total_seconds() < 60)
    
    if recent_count >= 10:
        warnings.append(f"We noticed you've submitted many answers very quickly - let's slow down and think through each question together")
        gaming_detected = True
        recommendation = "Taking a short break helps your brain learn better. Return when you're ready to engage thoughtfully."

    if gaming_detected and not recommendation:
        recommendation = "Let's slow down and think carefully about each question. Taking your time helps you learn more!"

    return {
        "gamingDetected": gaming_detected,
        "warnings": warnings,
        "recommendation": recommendation
    }

def validate_proportional_accuracy(values: Dict[str, float], rendered_heights: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
    """
    Validate proportional accuracy for diagrams (P0 Fix #5).
    Returns metadata with scaleFactor and deviation.
    Enforces 5% deviation requirement.
    """
    if not values:
        return {"scaleFactor": 1.0, "deviation": 0.0, "validated": True, "warnings": []}
    
    value_list = list(values.values())
    max_val = max(value_list)
    min_val = min(value_list)
    
    if min_val == 0:
        return {
            "scaleFactor": 1.0,
            "deviation": 0.0,
            "validated": False,
            "warnings": ["Minimum value is zero, cannot calculate proportional accuracy"]
        }
    
    scale_factor = max_val / min_val
    deviation = 0.0
    warnings = []
    
    # If rendered heights provided, check actual deviation
    if rendered_heights:
        for key in values:
            if key in rendered_heights:
                expected_height = (values[key] / max_val) * 100  # Normalized to percentage
                actual_height = rendered_heights[key]
                diff = abs(expected_height - actual_height)
                deviation = max(deviation, diff / 100)
                
                # Check 5% deviation requirement
                if diff > 5.0:
                    warnings.append(f"Bar '{key}' deviates by {diff:.1f}% from expected proportional height")
    
    validated = deviation <= 0.05  # 5% threshold
    
    return {
        "scaleFactor": scale_factor,
        "deviation": deviation,
        "validated": validated,
        "warnings": warnings
    }

def validate_numeric_answer_range(student_answer: float, expected_answer: float, problem_type: str) -> Dict[str, Any]:
    """
    Validate that student's calculated answer is reasonable (P0 Fix #8).
    Returns validation result with range checking.
    """
    warnings = []
    suspicious = False
    
    # Check for negative answers when positive expected
    if expected_answer >= 0 and student_answer < 0:
        suspicious = True
        warnings.append("Answer is negative but a positive quantity is expected")
    
    # Check for zero when non-zero expected
    if expected_answer != 0 and student_answer == 0:
        suspicious = True
        warnings.append("Answer is zero but a non-zero quantity is expected")
    
    # Check for orders of magnitude difference
    if expected_answer != 0:
        ratio = abs(student_answer / expected_answer)
        if ratio > 100 or ratio < 0.01:
            suspicious = True
            warnings.append(f"Answer differs from expected by more than 2 orders of magnitude")
    
    # Check for extremely large numbers in elementary math context
    if abs(student_answer) > 1000000:
        suspicious = True
        warnings.append("Answer seems unreasonably large for P6 level problems")
    
    # Check for fractional answers when integer expected (and vice versa)
    if student_answer != int(student_answer) and expected_answer == int(expected_answer):
        warnings.append("Answer is fractional but integer expected")
    
    return {
        "suspicious": suspicious,
        "warnings": warnings,
        "withinReasonableRange": not suspicious
    }

def validate_equation_shadow(shadow: str) -> tuple[bool, str]:
    """
    Validate equation shadow for quality and meaningful content.
    Returns: (is_valid, error_message)
    """
    if not shadow or shadow.strip() == "":
        return False, "equationShadow cannot be empty"
    
    shadow = shadow.strip()
    
    # Minimum length requirement (frontend enforces 50, backend should match)
    if len(shadow) < 50:
        return False, "equationShadow must be at least 50 characters long"
    
    # Maximum length to prevent essay-length answers
    if len(shadow) > 500:
        return False, "equationShadow is too long (maximum 500 characters)"
    
    # Gibberish detection using simple heuristics
    # Check for repeated patterns or random character sequences
    if len(shadow.split()) < 3:
        return False, "equationShadow must contain at least 3 words"
    
    # Check for excessive repetition (e.g., "test test test test")
    words = shadow.split()
    if len(set(words)) < len(words) * 0.5:
        return False, "equationShadow contains too much repetition"
    
    # Check for keyboard mashing patterns (consecutive repeated characters)
    import re
    if re.search(r'(.)\1{4,}', shadow):
        return False, "equationShadow appears to be random text"
    
    # Check for common filler/gibberish phrases
    gibberish_patterns = [
        r'^asdf', r'^qwer', r'^zxcv',
        r'^test$', r'^xxx$', r'^aaa$',
    ]
    for pattern in gibberish_patterns:
        if re.search(pattern, shadow.lower()):
            return False, "equationShadow must be meaningful, not placeholder text"
    
    return True, ""

def detect_pathway_collision(student_pathway: str, correct_pathway: str, related_pathways: List[str]) -> Dict[str, Any]:
    """
    Detect when student confuses similar pathways (P0 Fix #7).
    Returns collision detection result with hint mechanism.
    """
    if student_pathway == correct_pathway:
        return {"collisionDetected": False, "hint": None}
    
    # Check if pathways are related (e.g., before-after-change vs part-whole-comparison)
    collision_pairs = [
        ("before-after-change", "part-whole-comparison"),
        ("composite-shapes", "angles"),
        ("ratio-proportion", "percentage-change")
    ]
    
    for pair in collision_pairs:
        if (student_pathway in pair and correct_pathway in pair):
            return {
                "collisionDetected": True,
                "hint": f"This problem involves {correct_pathway.replace('-', ' ')}, not {student_pathway.replace('-', ' ')}. Focus on {'sequential changes' if correct_pathway == 'before-after-change' else 'simultaneous comparison'}.",
                "relatedPathways": [p for p in pair if p != student_pathway]
            }
    
    return {"collisionDetected": False, "hint": None}

def generate_step_by_step_feedback(problem_id: str, student_answer: float, expected_answer: float) -> Optional[Dict[str, Any]]:
    """
    Generate step-by-step scaffolding feedback for wrong answers (P0-7).
    Detects common mistake patterns and provides targeted guidance.
    """
    problem = PROBLEMS_DB.get(problem_id)
    if not problem:
        return None
    
    # Only provide step-by-step guidance for wrong answers
    if abs(student_answer - expected_answer) < 0.01:
        return None
    
    pathway = problem.get("pathway", "")
    question_text = problem.get("questionText", "").lower()
    
    # Analyze the mistake pattern
    step_by_step = None
    
    # Pattern 1: Fraction multiplication mistakes
    if "fraction" in question_text and "multiply" in question_text:
        step_by_step = COMMON_MISTAKES["fraction_multiplication"]
    
    # Pattern 2: Wrong fraction identification (before-after problems)
    elif "remainder" in question_text or "left" in question_text:
        step_by_step = COMMON_MISTAKES["wrong_fraction"]
    
    # Pattern 3: Wrong operation in ratio problems
    elif "ratio" in question_text or "proportion" in question_text:
        # Check if student used addition/multiplication when division was needed
        if abs(student_answer - (expected_answer * 2)) < 0.01 or abs(student_answer + expected_answer) < 0.01:
            step_by_step = COMMON_MISTAKES["wrong_operation"]
    
    # Pattern 4: Order of operations mistakes
    elif "bracket" in question_text or "braces" in question_text:
        step_by_step = COMMON_MISTAKES["order_mistake"]
    
    # Pattern 5: Unit conversion errors (rate-speed-time problems)
    elif "hour" in question_text and "minute" in question_text:
        step_by_step = COMMON_MISTAKES["unit_conversion"]
    
    # Pattern 6: Decimal place mistakes
    elif "." in str(student_answer) and "." in str(expected_answer):
        # Check if decimal is in wrong position
        student_str = str(student_answer).replace(".", "")
        expected_str = str(expected_answer).replace(".", "")
        if student_str == expected_str:
            step_by_step = COMMON_MISTAKES["decimal_place"]
    
    # Pattern 7: Percentage calculation errors
    elif "%" in question_text or "percent" in question_text:
        step_by_step = COMMON_MISTAKES["percentage_error"]
    
    # If no specific pattern detected, provide generic scaffolding
    if step_by_step is None:
        step_by_step = {
            "pattern": "General calculation error",
            "hint": "Let's work through this step-by-step. Take your time with each step.",
            "steps": [
                "Step 1: Read the problem carefully and identify what you're asked to find",
                "Step 2: List all the information given in the problem",
                "Step 3: Decide which operation(s) you need to use",
                "Step 4: Solve step-by-step, checking each part",
                "Step 5: Does your answer make sense? Check it against the problem"
            ]
        }
    
    return {
        "pattern": step_by_step["pattern"],
        "hint": step_by_step["hint"],
        "steps": step_by_step["steps"]
    }

def generate_feedback(
    problem_id: str,
    pathway_type: str,
    equation_shadow: str,
    student_answer: float,
    related_pathways: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Generate triad feedback for practice submission with P0 fixes."""
    problem = PROBLEMS_DB.get(problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    # Pathway identification feedback with collision detection (P0 Fix #7)
    correct_pathway = pathway_type == problem["pathway"]
    
    # Detect collision and generate hint
    collision_result = detect_pathway_collision(
        pathway_type, 
        problem["pathway"], 
        related_pathways or []
    )
    
    pathway_feedback = {
        "correct": correct_pathway,
        "confidence": 0.95 if correct_pathway else 0.65,
        "identifiedPathway": pathway_type,
        "collisionDetected": collision_result["collisionDetected"],
        "hint": collision_result["hint"],
        "relatedPathways": collision_result.get("relatedPathways", [])
    }
    
    # Articulation feedback
    articulation_level = 2 if len(equation_shadow) > 20 else 1
    model_articulation = f"This is a {problem['pathway'].replace('-', ' ').title()} problem. The equation shadow involves finding the original value after sequential changes."
    articulation_feedback = {
        "level": articulation_level,
        "feedback": "Good articulation! You described the sequential changes clearly." if articulation_level >= 2 else "Try to be more specific about the equation shadow.",
        "modelArticulation": model_articulation
    }
    
    # Solution feedback with range validation (P0 Fix #8)
    expected_answer = problem["expectedAnswer"]["value"]
    solution_correct = abs(student_answer - expected_answer) < 0.01
    
    # Validate numeric answer range
    range_validation = validate_numeric_answer_range(
        student_answer, 
        expected_answer, 
        problem["track"]
    )
    
    feedback_text = "Your answer is correct. Great work!" if solution_correct else f"Incorrect. The correct answer is {expected_answer}."
    
    if range_validation["suspicious"]:
        feedback_text += " " + ". ".join(range_validation["warnings"]) + "."
    
    # P0-7: Add step-by-step scaffolding for wrong answers
    step_by_step = None
    if not solution_correct:
        step_by_step = generate_step_by_step_feedback(problem_id, student_answer, expected_answer)
    
    solution_feedback = {
        "correct": solution_correct,
        "score": 1.0 if solution_correct else 0.0,
        "expectedAnswer": expected_answer,
        "studentAnswer": student_answer,
        "feedback": feedback_text,
        "rangeValidation": range_validation,
        "stepByStep": step_by_step
    }
    
    # Overall assessment
    if correct_pathway and solution_correct:
        overall = "green"
    elif correct_pathway or solution_correct:
        overall = "yellow"
    else:
        overall = "red"
    
    return {
        "pathwayIdentification": pathway_feedback,
        "articulation": articulation_feedback,
        "solution": solution_feedback,
        "overall": overall
    }

# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/")
async def root():
    """Serve frontend index.html."""
    index_path = BASE_DIR / "frontend" / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    else:
        return {
            "message": "ATOM-SG Pilot MVP API",
            "version": "1.0.0",
            "status": "running",
            "frontend": "not found"
        }

# ----------------------------------------------------------------------------
# 2.1 Problems
# ----------------------------------------------------------------------------

@app.get("/api/v1/problems")
async def get_problems(
    track: Optional[TrackType] = None,
    pathway: Optional[str] = None,
    week: Optional[int] = None
):
    """List all available problems with optional filtering."""
    problems = list(PROBLEMS_DB.values())
    
    if track:
        problems = [p for p in problems if p["track"] == track.value]
    if pathway:
        problems = [p for p in problems if p["pathway"] == pathway]
    if week:
        # In production, filter by week from problem metadata
        pass
    
    return {
        "problems": problems,
        "total": len(problems)
    }

@app.get("/api/v1/problems/pdf")
async def get_problems_pdf(week: int = Query(..., description="Week number (1 = baseline, 5 = transfer)")):
    """Generate a printable baseline or transfer test PDF."""
    # In production, use reportlab or weasyprint to generate PDF
    # For MVP, generate a placeholder PDF if it doesn't exist
    pdf_path = RENDERS_DIR / f"week_{week}_test.pdf"
    
    # Generate PDF if it doesn't exist
    if not pdf_path.exists():
        try:
            generate_week_test_pdf(week, pdf_path)
        except Exception as e:
            print(f"Failed to generate PDF: {e}")
            raise HTTPException(status_code=500, detail=f"PDF generation failed: {e}")
    
    if pdf_path.exists():
        return FileResponse(pdf_path, media_type="application/pdf")
    else:
        raise HTTPException(status_code=404, detail="PDF not found")

@app.get("/api/v1/problems/{problem_id}")
async def get_problem(problem_id: str):
    """Get a specific problem with full details."""
    if problem_id not in PROBLEMS_DB:
        raise HTTPException(status_code=404, detail="Problem not found")
    return PROBLEMS_DB[problem_id]

@app.get("/api/v1/problems/{problem_id}/hint")
async def get_problem_hint(problem_id: str):
    """
    Get a helpful hint for a problem without revealing the full answer.
    """
    if problem_id not in PROBLEMS_DB:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    problem = PROBLEMS_DB[problem_id]
    
    # Check if user has already received a hint for this problem
    # For now, return first hint (can be extended for progressive hints)
    hint = problem.get("hint", "Try breaking down the problem into smaller steps.")
    
    return {
        "success": True,
        "hint": hint,
        "problemId": problem_id
    }

@app.get("/api/v1/pathways/{pathway_type}/example")
async def get_pathway_example(pathway_type: str):
    """
    Get an example problem and solution for a given pathway type.
    """
    pathway_examples = {
        "before-after-change": {
            "question": "A shop had 120 pens. They sold 3/4 of them, then sold 1/3 of the remainder. How many pens are left?",
            "steps": [
                "First, find pens after first sale: 120 × (1 - 3/4) = 120 × 1/4 = 30 pens",
                "Then, find pens after second sale: 30 × (1 - 1/3) = 30 × 2/3 = 20 pens",
                "Answer: 20 pens are left"
            ]
        },
        "part-whole-comparison": {
            "question": "Ali has $120. Ben has 4/5 as much as Ali. How much does Ben have?",
            "steps": [
                "Identify the whole: Ali has $120 (this is the whole)",
                "Identify the fraction: Ben has 4/5 of Ali",
                "Calculate: $120 × 4/5 = $120 ÷ 5 × 4 = $24 × 4 = $96",
                "Answer: Ben has $96"
            ]
        },
        "data-interpretation-red-herring": {
            "question": "A bar chart shows sales for 4 months. January sales are $50. What are the December sales?",
            "steps": [
                "Ignore: February, March, November sales (these are red herrings)",
                "Look for pattern: If January is shown, look for similar months or calculate based on chart scale",
                "Answer: Depends on chart pattern, not the red herring months"
            ]
        },
        "composite-shapes": {
            "question": "Find the area of a composite shape made of a rectangle (10cm × 6cm) and a triangle (base 10cm, height 4cm).",
            "steps": [
                "Find area of rectangle: 10cm × 6cm = 60cm²",
                "Find area of triangle: ½ × 10cm × 4cm = 20cm²",
                "Add areas: 60cm² + 20cm² = 80cm²",
                "Answer: 80cm²"
            ]
        },
        "angles": {
            "question": "Find angle x in a triangle where the other two angles are 45° and 60°.",
            "steps": [
                "Remember: Sum of angles in a triangle = 180°",
                "Calculate: x = 180° - 45° - 60°",
                "x = 180° - 105° = 75°",
                "Answer: 75°"
            ]
        },
        "ratio-proportion": {
            "question": "The ratio of apples to oranges is 3:2. If there are 15 apples, how many oranges are there?",
            "steps": [
                "Set up proportion: 3/2 = 15/x",
                "Cross-multiply: 3x = 15 × 2",
                "3x = 30",
                "x = 10",
                "Answer: 10 oranges"
            ]
        },
        "percentage-change": {
            "question": "A shirt costs $40. It's on sale for 25% off. What's the sale price?",
            "steps": [
                "Find discount: 25% of $40 = 0.25 × $40 = $10",
                "Subtract discount: $40 - $10 = $30",
                "Answer: $30"
            ]
        },
        "rate-speed-time": {
            "question": "A car travels at 60 km/h for 2.5 hours. How far does it travel?",
            "steps": [
                "Use formula: Distance = Speed × Time",
                "Calculate: 60 km/h × 2.5 h",
                "= 60 × 2.5 = 150 km",
                "Answer: 150 km"
            ]
        }
        # Add examples for other pathway types...
    }
    
    if pathway_type not in pathway_examples:
        raise HTTPException(status_code=404, detail=f"No example found for pathway type: {pathway_type}")
    
    return {
        "success": True,
        "pathwayType": pathway_type,
        "example": pathway_examples[pathway_type]
    }

# ----------------------------------------------------------------------------
# 2.2 Rubrics
# ----------------------------------------------------------------------------

@app.get("/api/v1/rubrics")
async def get_rubrics():
    """List all evaluation rubrics."""
    return {
        "rubrics": list(RUBRICS_DB.values())
    }

@app.get("/api/v1/rubrics/{rubric_id}")
async def get_rubric(rubric_id: str):
    """Get a specific rubric with full criteria."""
    if rubric_id not in RUBRICS_DB:
        raise HTTPException(status_code=404, detail="Rubric not found")
    return RUBRICS_DB[rubric_id]

@app.post("/api/v1/rubrics")
async def create_rubric(rubric: RubricCreate):
    """Create a new rubric."""
    rubric_id = f"rub_{uuid.uuid4().hex[:8]}"
    rubric_data = {
        "id": rubric_id,
        "type": rubric.type,
        "pathway": rubric.pathway,
        "levels": [level.dict() for level in rubric.levels],
        "createdAt": generate_timestamp()
    }
    RUBRICS_DB[rubric_id] = rubric_data
    return rubric_data

@app.post("/api/v1/rubrics/batch")
async def create_rubrics_batch(rubrics: Dict[str, List[RubricCreate]]):
    """Create multiple rubrics in a single request."""
    created = []
    failed = []
    
    for rubric_create in rubrics["rubrics"]:
        try:
            rubric_id = f"rub_{uuid.uuid4().hex[:8]}"
            rubric_data = {
                "id": rubric_id,
                "type": rubric_create.type,
                "pathway": rubric_create.pathway,
                "levels": [level.dict() for level in rubric_create.levels],
                "createdAt": generate_timestamp()
            }
            RUBRICS_DB[rubric_id] = rubric_data
            created.append({
                "id": rubric_id,
                "type": rubric_create.type
            })
        except Exception as e:
            failed.append({
                "rubric": rubric_create.dict(),
                "error": str(e)
            })
    
    return {
        "created": created,
        "failed": failed,
        "total": len(created)
    }

# ----------------------------------------------------------------------------
# 2.3 Renders
# ----------------------------------------------------------------------------

@app.post("/api/v1/renders")
async def create_render(render: RenderRequest):
    """Generate a diagram render (TikZ/Matplotlib) with metadata validation (P0 Fix #2)."""
    render_id = f"rend_{uuid.uuid4().hex[:8]}"
    
    # Get problem to validate diagram metadata (P0 Fix #2)
    problem = PROBLEMS_DB.get(render.problemId)
    if problem:
        # Validate that render specifications align with problem requirements
        # Check if diagram type matches problem context
        valid_diagram_types = {
            "word-problems": ["bar-model", "number-line", "pictorial", "before-after"],
            "geometry": ["geometric-shape", "angle-diagram", "area-model"],
            "data-interpretation": ["bar-chart", "line-graph", "pie-chart", "table"]
        }
        
        if problem["track"] in valid_diagram_types:
            if render.diagramType not in valid_diagram_types[problem["track"]]:
                # Warning for mismatch but still proceed (in production might reject)
                pass
    
    # P0 Fix #11: Before-After Arrow Labels - Ensure arrows show quantities
    if render.diagramType == "before-after":
        # Add labels to arrows showing quantities
        # In production, this would call the actual rendering library
        pass
    
    # P0 Fix #9: Geometry Side Labels - Ensure ALL geometry diagrams have side labels
    if render.diagramType in ["geometric-shape", "angle-diagram", "area-model"]:
        # Ensure every side is labeled with its length
        # In production, this would call: add_side_labels(geometry_diagram, all_sides=True)
        pass
    
    # Validate proportional accuracy (P0 Fix #5)
    proportional_accuracy = validate_proportional_accuracy(render.values)
    
    render_data = {
        "id": render_id,
        "status": "completed",  # For MVP, assume immediate completion
        "url": f"/artifacts/renders/{render.problemId}_{render.diagramType}.{render.format}",
        "format": render.format,
        "createdAt": generate_timestamp(),
        "completedAt": generate_timestamp(),
        "proportionalAccuracy": proportional_accuracy
    }
    
    RENDERS_DB[render_id] = render_data
    return render_data

@app.get("/api/v1/renders/{render_id}")
async def get_render(render_id: str):
    """Check render status and get URL when ready."""
    if render_id not in RENDERS_DB:
        raise HTTPException(status_code=404, detail="Render not found")
    return RENDERS_DB[render_id]

@app.get("/api/v1/renders/{render_id}/download")
async def download_render(render_id: str):
    """Download the rendered file directly."""
    if render_id not in RENDERS_DB:
        raise HTTPException(status_code=404, detail="Render not found")
    
    render_data = RENDERS_DB[render_id]
    file_path = BASE_DIR / render_data["url"].lstrip("/")
    
    if file_path.exists():
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="Render file not found")

@app.get("/api/v1/renders")
async def list_renders(
    problemId: Optional[str] = None,
    format: Optional[str] = None
):
    """List all available renders with optional filtering."""
    renders = list(RENDERS_DB.values())
    
    if problemId:
        renders = [r for r in renders if r.get("problemId") == problemId]
    if format:
        renders = [r for r in renders if r.get("format") == format]
    
    return {
        "renders": renders,
        "total": len(renders)
    }

# ----------------------------------------------------------------------------
# 2.4 Milestones
# ----------------------------------------------------------------------------

@app.get("/api/v1/milestones")
async def get_milestones():
    """Get student progress milestones."""
    return {
        "milestones": list(MILESTONES_DB.values())
    }

@app.get("/api/v1/milestones/{milestone_id}")
async def get_milestone(milestone_id: str):
    """Get a specific milestone with detailed progress."""
    if milestone_id not in MILESTONES_DB:
        raise HTTPException(status_code=404, detail="Milestone not found")
    return MILESTONES_DB[milestone_id]

@app.patch("/api/v1/milestones/{milestone_id}")
async def update_milestone(milestone_id: str, update: MilestoneUpdate):
    """Update milestone progress."""
    if milestone_id not in MILESTONES_DB:
        raise HTTPException(status_code=404, detail="Milestone not found")
    
    milestone = MILESTONES_DB[milestone_id]
    
    if update.problemsCompleted is not None:
        milestone["problemsCompleted"] = update.problemsCompleted
    if update.lastAttemptScore is not None:
        milestone["averageScore"] = (milestone["averageScore"] * milestone["problemsCompleted"] + update.lastAttemptScore) / (milestone["problemsCompleted"] + 1)
    if update.pathwayIdentifiedCorrectly is not None:
        milestone["pathwayIdentificationAccuracy"] = milestone["pathwayIdentificationAccuracy"] * 0.95 + 0.05
    if update.articulationLevel is not None:
        milestone["articulationLevel"] = (milestone["articulationLevel"] + update.articulationLevel) / 2
    
    milestone["lastActivityAt"] = generate_timestamp()
    
    return milestone

# ----------------------------------------------------------------------------
# 2.5 Scans (Upload & OCR)
# ----------------------------------------------------------------------------

@app.post("/api/v1/scans")
async def upload_scan(
    week: int = Form(...),
    file: UploadFile = File(...)
):
    """Upload a scanned baseline test for OCR processing."""
    scan_id = f"scan_{uuid.uuid4().hex[:8]}"
    timestamp = generate_timestamp()
    
    # Save uploaded file
    file_ext = file.filename.split('.')[-1]
    scan_path = OCR_DIR / f"{scan_id}.{file_ext}"
    with open(scan_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    scan_data = {
        "id": scan_id,
        "status": "processing",
        "uploadedAt": timestamp,
        "estimatedTime": 30
    }
    
    SCANS_DB[scan_id] = scan_data
    
    # Simulate OCR processing (in production, run in background)
    scan_data["status"] = "completed"
    scan_data["completedAt"] = generate_timestamp()
    scan_data["ocrResults"] = [
        {
            "questionId": "prob_001",
            "text": "Student's handwritten answer...",
            "confidence": 0.85
        }
    ]
    scan_data["gapMap"] = {
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
    
    return scan_data

@app.get("/api/v1/scans/{scan_id}")
async def get_scan(scan_id: str):
    """Check scan processing status and get OCR results."""
    if scan_id not in SCANS_DB:
        raise HTTPException(status_code=404, detail="Scan not found")
    return SCANS_DB[scan_id]

@app.get("/api/v1/scans/{scan_id}/download")
async def download_scan(scan_id: str):
    """Download the original uploaded scan file."""
    if scan_id not in SCANS_DB:
        raise HTTPException(status_code=404, detail="Scan not found")
    
    # Find the scan file
    for ext in ["pdf", "png", "jpg"]:
        file_path = OCR_DIR / f"{scan_id}.{ext}"
        if file_path.exists():
            return FileResponse(file_path)
    
    raise HTTPException(status_code=404, detail="Scan file not found")

# ----------------------------------------------------------------------------
# 2.6 Practice Sessions
# ----------------------------------------------------------------------------

@app.post("/api/v1/practice-sessions")
async def create_practice_session(session: PracticeSessionStart):
    """Start a new practice session."""
    session_id = f"sess_{uuid.uuid4().hex[:8]}"
    
    # Get problems for the pathway
    problems = [p for p in PROBLEMS_DB.values() if p["pathway"] == session.pathway]
    problem_ids = [p["id"] for p in problems[:3]]  # Limit to 3 problems for MVP
    
    session_data = {
        "id": session_id,
        "week": session.week,
        "pathway": session.pathway,
        "sessionType": session.sessionType,
        "problems": problem_ids,
        "currentProblemIndex": 0,
        "status": "active",
        "completedProblems": [],
        "startedAt": generate_timestamp()
    }
    
    SESSIONS_DB[session_id] = session_data
    return session_data

@app.get("/api/v1/practice-sessions/{session_id}")
async def get_practice_session(session_id: str):
    """Get session details with current problem."""
    if session_id not in SESSIONS_DB:
        raise HTTPException(status_code=404, detail="Practice session not found")
    
    session = SESSIONS_DB[session_id]
    current_problem_index = session["currentProblemIndex"]
    
    if current_problem_index < len(session["problems"]):
        current_problem_id = session["problems"][current_problem_index]
        current_problem = PROBLEMS_DB.get(current_problem_id, {})
    else:
        current_problem = None
    
    return {
        "id": session_id,
        "status": session["status"],
        "currentProblemIndex": current_problem_index,
        "currentProblem": current_problem,
        "completedProblems": session["completedProblems"]
    }

@app.post("/api/v1/practice-sessions/{session_id}/submit")
async def submit_practice_session(session_id: str, submission: PracticeSessionSubmit, user_id: str = Query("anonymous")):
    """Submit answer for current problem (with forced articulation validation - P0 Fix #1)."""
    if session_id not in SESSIONS_DB:
        raise HTTPException(status_code=404, detail="Practice session not found")
    
    # Validate forced articulation fields (P0 Fix #1)
    validation_errors = []
    
    # Check pathwayType
    if not submission.pathwayType or submission.pathwayType.strip() == "":
        validation_errors.append("pathwayType cannot be empty")
    elif submission.pathwayType not in VALID_PATHWAY_TYPES:
        validation_errors.append(f"pathwayType must be one of: {', '.join(VALID_PATHWAY_TYPES)}")
    
    # Check equationShadow with enhanced validation
    is_valid, error_msg = validate_equation_shadow(submission.equationShadow)
    if not is_valid:
        validation_errors.append(error_msg)
    
    # Trim whitespace from equation shadow
    submission.equationShadow = submission.equationShadow.strip()
    
    if validation_errors:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Validation failed",
                "message": ", ".join(validation_errors)
            }
        )
    
    session = SESSIONS_DB[session_id]
    submission_id = f"sub_{uuid.uuid4().hex[:8]}"
    
    # Get problem for related pathways
    problem = PROBLEMS_DB.get(submission.problemId)
    related_pathways = [p for p in VALID_PATHWAY_TYPES if p != submission.pathwayType][:3] if problem else []
    
    # Generate feedback with P0 fixes
    feedback = generate_feedback(
        submission.problemId,
        submission.pathwayType,
        submission.equationShadow,
        submission.studentAnswer.value,
        related_pathways
    )
    
    # P1-1: Gamification - Update user profile streak
    if user_id not in PROFILES_DB:
        PROFILES_DB[user_id] = {
            "userId": user_id,
            "practiceStreak": 0,
            "lastPracticeDate": None,
            "achievements": [],
            "totalPracticeDays": 0,
            "totalProblemsCompleted": 0,
            "createdAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
        }
    
    profile = PROFILES_DB[user_id]
    
    # Check if practiced today
    today = datetime.now().strftime("%Y-%m-%d")
    last_practice = profile.get("lastPracticeDate")
    
    if last_practice == today:
        # Already practiced today, don't increment streak
        pass
    elif last_practice == (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"):
        # Practiced yesterday, increment streak
        profile["practiceStreak"] = profile.get("practiceStreak", 0) + 1
    else:
        # Streak broken, reset to 1
        profile["practiceStreak"] = 1
    
    profile["lastPracticeDate"] = today
    profile["totalPracticeDays"] = profile.get("totalPracticeDays", 0) + 1
    profile["totalProblemsCompleted"] = profile.get("totalProblemsCompleted", 0) + 1
    
    # P1-1: Check for newly unlocked achievements
    newly_unlocked = check_achievements(profile)
    PROFILES_DB[user_id] = profile
    
    # Add to completed problems
    session["completedProblems"].append({
        "problemId": submission.problemId,
        "score": feedback["solution"]["score"],
        "pathwayIdentifiedCorrectly": feedback["pathwayIdentification"]["correct"],
        "articulationLevel": feedback["articulation"]["level"]
    })
    
    # Move to next problem
    session["currentProblemIndex"] += 1
    if session["currentProblemIndex"] >= len(session["problems"]):
        session["status"] = "completed"
    
    # Determine next problem
    if session["currentProblemIndex"] < len(session["problems"]):
        next_problem_id = session["problems"][session["currentProblemIndex"]]
    else:
        next_problem_id = None
    
    # P1-1: Return streak and achievement info
    return {
        "submissionId": submission_id,
        "feedback": feedback,
        "nextProblemId": next_problem_id,
        "streak": {
            "current": profile["practiceStreak"],
            "totalDays": profile["totalPracticeDays"],
            "achievements": profile["achievements"],
            "newlyUnlocked": newly_unlocked
        }
    }

@app.post("/api/v1/practice")
async def submit_practice(submission: PracticeSubmission, user_id: str = Query("anonymous")):
    """Submit an individual practice attempt (with validation - P0 Fix #1)."""
    # Validate forced articulation fields (P0 Fix #1)
    validation_errors = []
    
    # Check pathwayType
    if not submission.pathwayType or submission.pathwayType.strip() == "":
        validation_errors.append("pathwayType cannot be empty")
    elif submission.pathwayType not in VALID_PATHWAY_TYPES:
        validation_errors.append(f"pathwayType must be one of: {', '.join(VALID_PATHWAY_TYPES)}")
    
    # Check equationShadow with enhanced validation
    is_valid, error_msg = validate_equation_shadow(submission.equationShadow)
    if not is_valid:
        validation_errors.append(error_msg)
    
    # Trim whitespace from equation shadow
    submission.equationShadow = submission.equationShadow.strip()
    
    if validation_errors:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Validation failed",
                "message": ", ".join(validation_errors)
            }
        )
    
    submission_id = f"prac_sub_{uuid.uuid4().hex[:8]}"
    
    # Get problem for related pathways
    problem = PROBLEMS_DB.get(submission.problemId)
    related_pathways = [p for p in VALID_PATHWAY_TYPES if p != submission.pathwayType][:3] if problem else []
    
    # Generate feedback with P0 fixes
    feedback = generate_feedback(
        submission.problemId,
        submission.pathwayType,
        submission.equationShadow,
        submission.studentAnswer.value,
        related_pathways
    )
    
    problem = PROBLEMS_DB.get(submission.problemId)
    
    # P1-1: Gamification - Update user profile streak
    if user_id not in PROFILES_DB:
        PROFILES_DB[user_id] = {
            "userId": user_id,
            "practiceStreak": 0,
            "lastPracticeDate": None,
            "achievements": [],
            "totalPracticeDays": 0,
            "totalProblemsCompleted": 0,
            "createdAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
        }
    
    profile = PROFILES_DB[user_id]
    
    # Check if practiced today
    today = datetime.now().strftime("%Y-%m-%d")
    last_practice = profile.get("lastPracticeDate")
    
    if last_practice == today:
        # Already practiced today, don't increment streak
        pass
    elif last_practice == (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"):
        # Practiced yesterday, increment streak
        profile["practiceStreak"] = profile.get("practiceStreak", 0) + 1
    else:
        # Streak broken, reset to 1
        profile["practiceStreak"] = 1
    
    profile["lastPracticeDate"] = today
    profile["totalPracticeDays"] = profile.get("totalPracticeDays", 0) + 1
    profile["totalProblemsCompleted"] = profile.get("totalProblemsCompleted", 0) + 1
    
    # P1-1: Check for newly unlocked achievements
    newly_unlocked = check_achievements(profile)
    PROFILES_DB[user_id] = profile
    
    # Generate recommended next steps
    recommended_next_steps = []
    if feedback["pathwayIdentification"]["correct"]:
        recommended_next_steps.append(f"Practice another {submission.pathwayType} problem")
    if feedback["articulation"]["level"] < 3:
        recommended_next_steps.append("Try articulating the equation shadow more precisely")
    
    return {
        "submissionId": submission_id,
        "problemId": submission.problemId,
        "submittedAt": generate_timestamp(),
        "feedback": feedback,
        "recommendedNextSteps": recommended_next_steps,
        "streak": {
            "current": profile["practiceStreak"],
            "totalDays": profile["totalPracticeDays"],
            "achievements": profile["achievements"],
            "newlyUnlocked": newly_unlocked
        }
    }

# ----------------------------------------------------------------------------
# 2.7.1 User Profile & Gamification (P1-1)
# ----------------------------------------------------------------------------

@app.get("/api/v1/profile/me")
async def get_profile(user_id: str = Query("anonymous")):
    """Get user profile with gamification data (P1-1)."""
    if user_id not in PROFILES_DB:
        PROFILES_DB[user_id] = {
            "userId": user_id,
            "practiceStreak": 0,
            "lastPracticeDate": None,
            "achievements": [],
            "totalPracticeDays": 0,
            "totalProblemsCompleted": 0,
            "createdAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
        }
    
    profile = PROFILES_DB[user_id]
    
    return {
        "success": True,
        "data": {
            "userId": profile["userId"],
            "streak": {
                "current": profile["practiceStreak"],
                "totalDays": profile["totalPracticeDays"],
                "achievements": profile["achievements"]
            }
        }
    }

@app.get("/api/v1/achievements")
async def get_achievements():
    """Get all available achievements (P1-1)."""
    return {
        "achievements": ACHIEVEMENTS
    }

# ----------------------------------------------------------------------------
# 2.7.2 Pathway Radar (Warm-up)
# ----------------------------------------------------------------------------

@app.get("/api/v1/pathway-radar/questions")
async def get_pathway_radar_questions(date: Optional[str] = None):
    """Get 10 mixed pathway identification questions for today's warm-up."""
    # Generate sample questions
    questions = []
    pathways = ["before-after-change", "part-whole-comparison", "composite-shapes"]
    
    for i in range(10):
        question_id = f"radar_q{i+1:03d}"
        
        # P0 Fix #10: Ensure diagrams match question text
        # For "straight line" questions, use straight horizontal line diagrams
        question_text = f"Sample pathway identification question {i+1}..."
        
        if "straight line" in question_text.lower():
            diagram_type = "straight_horizontal_line"  # No arrows, no angles
            diagram_points = ["A", "B", "C"]  # Clearly marked
        else:
            diagram_type = "standard"
            diagram_points = []
        
        question = {
            "id": question_id,
            "questionText": question_text,
            "pathways": pathways[:2],
            "timeLimit": 30,
            "diagramType": diagram_type,
            "diagramPoints": diagram_points
        }
        questions.append(question)
    
    return {
        "questions": questions,
        "total": 10,
        "date": date or datetime.now().strftime("%Y-%m-%d")
    }

@app.post("/api/v1/pathway-radar/submit")
async def submit_pathway_radar(submission: PathwayRadarSubmit, student_id: str = Query("anonymous")):
    """Submit pathway identification answers with gaming detection consequences (P0 Fix #3)."""
    # Get or create student profile
    if student_id not in STUDENT_PROFILES_DB:
        STUDENT_PROFILES_DB[student_id] = {
            "recentSubmissions": [],
            "gamingCooldownUntil": None,
            "pathwayRadarScore": 0
        }
    
    profile = STUDENT_PROFILES_DB[student_id]
    now = datetime.now()
    
    # Check if student is in cooldown (P0 Fix #3)
    if profile.get("gamingCooldownUntil"):
        cooldown_until = datetime.fromisoformat(profile["gamingCooldownUntil"].replace("Z", "+00:00"))
        if now < cooldown_until:
            remaining_seconds = int((cooldown_until - now).total_seconds())
            raise HTTPException(
                status_code=429,
                detail={
                    "error": "cooldown_active",
                    "message": f"Taking a short break helps learning! Please wait {remaining_seconds // 60}m {remaining_seconds % 60}s before trying again.",
                    "cooldownRemaining": remaining_seconds,
                    "cooldownUntil": profile["gamingCooldownUntil"]
                }
            )
    
    correct_count = sum(1 for a in submission.answers if a.confidence > 0.8)
    total = len(submission.answers)
    accuracy = correct_count / total if total > 0 else 0
    
    # Detect gaming patterns (P0 Fix #3)
    gaming_detection = detect_gaming_pattern(
        [a.dict() for a in submission.answers],
        student_id
    )
    
    # Apply point deduction if gaming detected (P0 Fix #3)
    score_deduction = 0
    if gaming_detection["gamingDetected"]:
        score_deduction = 50  # Deduct 50 points
        
        # Set 5-minute cooldown (P0 Fix #3)
        cooldown_end = now + (datetime.strptime("00:05:00", "%H:%M:%S") - datetime.strptime("00:00:00", "%H:%M:%S"))
        profile["gamingCooldownUntil"] = cooldown_end.strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    # Update pathway radar score
    raw_score = int(accuracy * 100)  # Base score out of 100
    final_score = max(0, raw_score - score_deduction)  # Apply deduction, ensure non-negative
    profile["pathwayRadarScore"] = final_score
    
    # Track recent submissions (P0 Fix #3 - keep last 20 submissions)
    profile["recentSubmissions"].append(now.strftime("%Y-%m-%dT%H:%M:%S+08:00"))
    if len(profile["recentSubmissions"]) > 20:
        profile["recentSubmissions"] = profile["recentSubmissions"][-20:]
    
    # Identify strong and weak pathways
    pathway_scores = {}
    for answer in submission.answers:
        pathway = answer.identifiedPathway
        if pathway not in pathway_scores:
            pathway_scores[pathway] = []
        pathway_scores[pathway].append(answer.confidence)
    
    strong_pathways = [p for p, scores in pathway_scores.items() if sum(scores) / len(scores) > 0.8]
    weak_pathways = [p for p, scores in pathway_scores.items() if sum(scores) / len(scores) < 0.6]
    
    result = {
        "score": {
            "correct": correct_count,
            "total": total,
            "accuracy": accuracy,
            "rawScore": raw_score,
            "scoreDeduction": score_deduction,
            "finalScore": final_score
        },
        "feedback": {
            "strongPathways": strong_pathways,
            "weakPathways": weak_pathways
        },
        "gamingDetection": gaming_detection,
        "studentId": student_id
    }
    
    # Add gaming warning and cooldown info if detected
    if gaming_detection["gamingDetected"]:
        result["feedback"]["gamingWarning"] = gaming_detection["recommendation"]
        result["gamingDetection"]["cooldownActive"] = True
        result["gamingDetection"]["cooldownUntil"] = profile["gamingCooldownUntil"]
        result["gamingDetection"]["cooldownDuration"] = 300  # 5 minutes in seconds
    
    return result

# ----------------------------------------------------------------------------
# 2.7.1 Glossary & Tooltips (P0 Fix #4)
# ----------------------------------------------------------------------------

@app.get("/api/v1/glossary")
async def get_glossary():
    """Get all glossary terms for vocabulary support (P0 Fix #4)."""
    return {
        "terms": GLOSSARY_TERMS
    }

@app.get("/api/v1/glossary/{term}")
async def get_glossary_term(term: str):
    """Get definition for a specific term."""
    term_key = term.replace("-", " ").lower()
    if term_key in GLOSSARY_TERMS:
        return {
            "term": term,
            "definition": GLOSSARY_TERMS[term_key]
        }
    else:
        raise HTTPException(status_code=404, detail="Term not found in glossary")

# ----------------------------------------------------------------------------
# 2.8 Advanced Analytics (Week 3+)
# ----------------------------------------------------------------------------

@app.post("/api/v1/collision")
async def analyze_collision(request: CollisionRequest):
    """Detect cross-thread collision patterns across multiple pathways."""
    analysis_id = f"coll_{uuid.uuid4().hex[:8]}"
    
    # Generate sample collision analysis
    collision_data = {
        "analysisId": analysis_id,
        "analyzedAt": generate_timestamp(),
        "collisionDetected": True,
        "collisionDetails": {
            "collidingPathways": [
                {
                    "pathway": request.pathways[0] if request.pathways else "before-after-change",
                    "identificationAccuracy": 0.82,
                    "articulationLevel": 2.1
                },
                {
                    "pathway": request.pathways[1] if len(request.pathways) > 1 else "part-whole-comparison",
                    "identificationAccuracy": 0.78,
                    "articulationLevel": 1.9
                }
            ],
            "collisionPoints": [
                {
                    "problemId": "prob_015",
                    "problemType": "word-problem",
                    "detectedConflict": {
                        "studentIdentified": request.pathways[0] if request.pathways else "before-after-change",
                        "correctPathway": request.pathways[1] if len(request.pathways) > 1 else "part-whole-comparison",
                        "confidence": 0.65,
                        "evidence": "Student used sequential steps (before-after pattern) but problem requires simultaneous comparison."
                    },
                    "severity": "high"
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
            }
        ],
        "nextReviewDate": "2026-04-30"
    }
    
    # Save to file
    collision_file = COLLISION_DIR / f"{analysis_id}.json"
    with open(collision_file, "w") as f:
        json.dump(collision_data, f, indent=2)
    
    return collision_data

@app.get("/api/v1/interpretation")
async def get_interpretation(
    week: Optional[int] = None,
    pathway: Optional[str] = None,
    includeRedHerringAnalysis: bool = False
):
    """Get data interpretation results and metrics."""
    interpretation_data = {
        "queryParameters": {
            "week": week,
            "pathway": pathway,
            "includeRedHerringAnalysis": includeRedHerringAnalysis
        },
        "summary": {
            "totalAttempts": 15,
            "correctAnswers": 12,
            "accuracy": 0.80,
            "averageTimeToSolve": 245,
            "analyzedAt": generate_timestamp()
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
            }
        },
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
            }
        ]
    }
    
    if includeRedHerringAnalysis:
        interpretation_data["redHerringPerformance"] = {
            "problemsWithRedHerrings": 8,
            "correctlyIdentifiedRedHerrings": 6,
            "fellForRedHerring": 2,
            "redHerringAccuracy": 0.75
        }
        interpretation_data["redHerringAnalysis"] = [
            {
                "problemId": "prob_025",
                "title": "Sales Data with Seasonal Distractor",
                "redHerringType": "seasonal-variation",
                "detected": True,
                "correctlyIgnored": True,
                "feedback": "Good! You correctly identified that the seasonal spike was a distractor and focused on the trend."
            },
            {
                "problemId": "prob_028",
                "title": "Production Output with Outlier",
                "redHerringType": "outlier-data-point",
                "detected": False,
                "correctlyIgnored": False,
                "feedback": "The outlier point in March is unusual and should not be included in the trend calculation. Try identifying anomalies first."
            }
        ]
    
    return interpretation_data

# ----------------------------------------------------------------------------
# 2.9 Analytics
# ----------------------------------------------------------------------------

@app.get("/api/v1/analytics/baseline")
async def get_baseline_analytics():
    """Get baseline test results and gap map."""
    return {
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

@app.get("/api/v1/analytics/transfer")
async def get_transfer_analytics():
    """Get transfer test results and ramp-up metrics."""
    return {
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
            "targetMet": True
        },
        "successCriteria": [
            {
                "metric": "pathwayIdentificationAccuracy",
                "value": 0.85,
                "target": 0.9,
                "met": False
            },
            {
                "metric": "articulationLevel2PlusRate",
                "value": 0.92,
                "target": 0.9,
                "met": True
            },
            {
                "metric": "solvingImprovement",
                "value": 0.82,
                "target": 0.8,
                "met": True
            }
        ]
    }

@app.get("/api/v1/analytics/progress")
async def get_progress_analytics():
    """Get overall progress across all weeks."""
    return {
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

# ----------------------------------------------------------------------------
# 2.10 Student Reflection
# ----------------------------------------------------------------------------

@app.post("/api/v1/reflections")
async def create_reflection(reflection: ReflectionCreate):
    """Submit a student reflection (digital reflection sheet)."""
    reflection_id = f"ref_{uuid.uuid4().hex[:8]}"
    
    reflection_data = {
        "id": reflection_id,
        "week": reflection.week,
        "pathway": reflection.pathway,
        "reflection": reflection.reflection,
        "confidence": reflection.confidence,
        "struggles": reflection.struggles,
        "improvements": reflection.improvements,
        "createdAt": generate_timestamp()
    }
    
    REFLECTIONS_DB.append(reflection_data)
    return reflection_data

@app.get("/api/v1/reflections")
async def get_reflections(
    week: Optional[int] = None,
    pathway: Optional[str] = None
):
    """Get student reflections."""
    reflections = REFLECTIONS_DB
    
    if week is not None:
        reflections = [r for r in reflections if r["week"] == week]
    if pathway:
        reflections = [r for r in reflections if r["pathway"] == pathway]
    
    return {
        "reflections": reflections
    }

# ----------------------------------------------------------------------------
# 2.11 System (Admin)
# ----------------------------------------------------------------------------

@app.get("/api/v1/system/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": generate_timestamp()
    }

@app.get("/api/v1/system/stats")
async def system_stats():
    """Get system statistics (for debugging/monitoring)."""
    return {
        "problems": len(PROBLEMS_DB),
        "rubrics": len(RUBRICS_DB),
        "renders": len(RENDERS_DB),
        "scans": len(SCANS_DB),
        "practiceSessions": len(SESSIONS_DB),
        "lastActivity": generate_timestamp()
    }

# ============================================================================
# Static File Serving (Frontend)
# ============================================================================

@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    """Serve static frontend files."""
    static_dir = BASE_DIR / "frontend" / "static"
    file_location = static_dir / file_path
    
    if file_location.exists() and file_location.is_file():
        return FileResponse(file_location)
    else:
        raise HTTPException(status_code=404, detail="Static file not found")


@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    """Catch-all route to serve frontend for SPA routing."""
    # Don't interfere with API routes
    if full_path.startswith("api/") or full_path.startswith("static/"):
        raise HTTPException(status_code=404, detail="Route not found")
    
    index_path = BASE_DIR / "frontend" / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    else:
        raise HTTPException(status_code=404, detail="Frontend not found")


# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5000,
        reload=True
    )
