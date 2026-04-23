#!/usr/bin/env python3
"""
Unit tests for Persona-Aware API endpoints.
Tests all new endpoints: persona classification, adaptive problem selection,
gaming detection, and persona-aware feedback.
"""

import sys
import json
import unittest
from datetime import datetime
from fastapi.testclient import TestClient

# Import the FastAPI app
from main import app, PERSONA_PROFILES_DB, STUDENT_ATTEMPTS_DB, GAMING_DETECTION_HISTORY, SESSIONS_DB

client = TestClient(app)


class TestPersonaClassification(unittest.TestCase):
    """Tests for /personas/classify endpoint."""
    
    def setUp(self):
        """Clear persona profiles before each test."""
        PERSONA_PROFILES_DB.clear()
    
    def test_classify_cautious_perfectionist(self):
        """Test classification of cautious perfectionist persona."""
        request_data = {
            "student_id": "test_student_001",
            "baseline_results": {
                "accuracy_by_pathway": {"before-after-change": 0.85, "part-whole-comparison": 0.80},
                "average_time_per_problem": 200.0,
                "help_usage_rate": 0.1,
                "confidence_calibration_score": 0.6,
                "completion_rate": 0.95
            },
            "behavioral_data": {
                "session_speeds": [180, 220, 190, 210, 200],
                "help_requests": 1,
                "hint_usage_pattern": "selective",
                "retry_patterns": {"prob_001": 2, "prob_002": 1},
                "pause_patterns": [5.0, 8.0, 6.0],
                "confidence_vs_accuracy": [{"confidence": 0.5, "accuracy": 0.9}]
            }
        }
        
        response = client.post("/api/v1/personas/classify", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("persona_id", data)
        self.assertIn("persona_type", data)
        self.assertIn("confidence_score", data)
        self.assertIn("characteristics", data)
        
        self.assertEqual(data["persona_id"], "pers_test_student_001")
        self.assertGreaterEqual(data["confidence_score"], 0.0)
        self.assertLessEqual(data["confidence_score"], 1.0)
    
    def test_classify_confident_rusher(self):
        """Test classification of confident rusher persona."""
        request_data = {
            "student_id": "test_student_002",
            "baseline_results": {
                "accuracy_by_pathway": {"before-after-change": 0.55, "part-whole-comparison": 0.50},
                "average_time_per_problem": 25.0,
                "help_usage_rate": 0.0,
                "confidence_calibration_score": 0.95,
                "completion_rate": 0.70
            },
            "behavioral_data": {
                "session_speeds": [20, 15, 30, 25, 20],
                "help_requests": 0,
                "hint_usage_pattern": "never",
                "retry_patterns": {},
                "pause_patterns": [0.5, 0.3, 0.4],
                "confidence_vs_accuracy": [{"confidence": 0.95, "accuracy": 0.5}]
            }
        }
        
        response = client.post("/api/v1/personas/classify", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("persona_type", data)
        # Should lean toward confident_rusher or gaming_the_system
        self.assertIn(data["persona_type"], ["confident_rusher", "gaming_the_system"])
    
    def test_classify_help_seeking_dependent(self):
        """Test classification of help-seeking dependent persona."""
        request_data = {
            "student_id": "test_student_003",
            "baseline_results": {
                "accuracy_by_pathway": {"before-after-change": 0.65},
                "average_time_per_problem": 150.0,
                "help_usage_rate": 0.8,
                "confidence_calibration_score": 0.4,
                "completion_rate": 0.80
            },
            "behavioral_data": {
                "session_speeds": [120, 180, 140],
                "help_requests": 8,
                "hint_usage_pattern": "immediate",
                "retry_patterns": {"prob_001": 3},
                "pause_patterns": [2.0],
                "confidence_vs_accuracy": [{"confidence": 0.3, "accuracy": 0.7}]
            }
        }
        
        response = client.post("/api/v1/personas/classify", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("persona_type", data)
    
    def test_get_persona_profile(self):
        """Test retrieving a persona profile."""
        # First classify a student
        request_data = {
            "student_id": "test_student_004",
            "baseline_results": {
                "accuracy_by_pathway": {"before-after-change": 0.80},
                "average_time_per_problem": 120.0,
                "help_usage_rate": 0.2,
                "confidence_calibration_score": 0.8,
                "completion_rate": 0.90
            },
            "behavioral_data": {
                "session_speeds": [100, 120, 140],
                "help_requests": 2,
                "hint_usage_pattern": "selective"
            }
        }
        
        client.post("/api/v1/personas/classify", json=request_data)
        
        # Now retrieve the profile
        response = client.get("/api/v1/personas/pers_test_student_004/profile")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("id", data)
        self.assertIn("persona_type", data)
        self.assertIn("confidence_score", data)
        self.assertIn("characteristics", data)
        self.assertIn("recommendations", data)
        self.assertIn("scaffolding_level", data["recommendations"])
        self.assertIn("feedback_style", data["recommendations"])
    
    def test_get_nonexistent_persona(self):
        """Test retrieving a non-existent persona profile."""
        response = client.get("/api/v1/personas/pers_nonexistent/profile")
        self.assertEqual(response.status_code, 404)


class TestAdaptiveProblemSelection(unittest.TestCase):
    """Tests for /problems/adaptive endpoint."""
    
    def setUp(self):
        """Clear attempt history before each test."""
        STUDENT_ATTEMPTS_DB.clear()
        PERSONA_PROFILES_DB.clear()
    
    def test_adaptive_selection_basic(self):
        """Test basic adaptive problem selection."""
        response = client.get("/api/v1/problems/adaptive?student_id=test_adaptive_001")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("problem_id", data)
        self.assertIn("problem", data)
        self.assertIn("scaffolding_level", data)
        self.assertIn("selection_reason", data)
        self.assertIn("persona_alignment", data)
        self.assertIn("estimated_time", data)
        
        # Verify problem structure
        problem = data["problem"]
        self.assertIn("id", problem)
        self.assertIn("title", problem)
        self.assertIn("pathway", problem)
        self.assertIn("difficulty", problem)
    
    def test_adaptive_selection_with_pathway(self):
        """Test adaptive selection with target pathway."""
        response = client.get(
            "/api/v1/problems/adaptive?student_id=test_adaptive_002&target_pathway=before-after-change"
        )
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data["problem"]["pathway"], "before-after-change")
    
    def test_adaptive_selection_with_difficulty(self):
        """Test adaptive selection with preferred difficulty."""
        response = client.get(
            "/api/v1/problems/adaptive?student_id=test_adaptive_003&preferred_difficulty=easy"
        )
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("problem", data)
    
    def test_adaptive_selection_excludes_recent(self):
        """Test that recent problems are excluded."""
        # Add some attempts
        STUDENT_ATTEMPTS_DB["test_adaptive_004"] = [
            {"problem_id": "prob_001", "pathway": "before-after-change", "is_correct": True, "timestamp": "2026-04-19T10:00:00+08:00"},
            {"problem_id": "prob_002", "pathway": "data-interpretation-red-herring", "is_correct": False, "timestamp": "2026-04-19T10:05:00+08:00"}
        ]
        
        response = client.get(
            "/api/v1/problems/adaptive?student_id=test_adaptive_004&exclude_recent=true"
        )
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        # Should not return prob_001 or prob_002
        self.assertNotIn(data["problem_id"], ["prob_001", "prob_002"])


class TestGamingDetection(unittest.TestCase):
    """Tests for /sessions/{id}/detect-gaming endpoint."""
    
    def setUp(self):
        """Create a test session before each test."""
        GAMING_DETECTION_HISTORY.clear()
        SESSIONS_DB.clear()
        
        # Create a test session
        SESSIONS_DB["test_session_001"] = {
            "id": "test_session_001",
            "status": "active",
            "problems": ["prob_001", "prob_002", "prob_003"],
            "currentProblemIndex": 0
        }
    
    def test_gaming_detection_low_risk(self):
        """Test gaming detection with normal behavior (low risk)."""
        request_data = {
            "answers": [
                {"value": 300, "confidence": 0.8, "is_correct": True},
                {"value": 75, "confidence": 0.9, "is_correct": True}
            ],
            "speed_data": [120, 150, 180],
            "help_requests": 1
        }
        
        response = client.post("/api/v1/sessions/test_session_001/detect-gaming", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("risk_level", data)
        self.assertIn("confidence", data)
        self.assertIn("evidence", data)
        self.assertIn("intervention_suggestion", data)
        
        self.assertEqual(data["risk_level"], "LOW")
        self.assertFalse(data["cooldown_recommended"])
    
    def test_gaming_detection_impossible_speed(self):
        """Test detection of impossible speed (high risk)."""
        request_data = {
            "answers": [
                {"value": 300, "confidence": 0.9, "is_correct": False},
                {"value": 300, "confidence": 0.9, "is_correct": False}
            ],
            "speed_data": [5, 3, 4],  # Impossibly fast
            "help_requests": 0
        }
        
        response = client.post("/api/v1/sessions/test_session_001/detect-gaming", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn(data["risk_level"], ["MEDIUM", "HIGH"])
        
        # Check for impossible speed evidence
        evidence_types = [e["pattern_type"] for e in data["evidence"]]
        self.assertIn("impossible_speed", evidence_types)
    
    def test_gaming_detection_repetitive_answers(self):
        """Test detection of repetitive answer patterns."""
        request_data = {
            "answers": [
                {"value": 42, "confidence": 0.95, "is_correct": False},
                {"value": 42, "confidence": 0.95, "is_correct": False},
                {"value": 42, "confidence": 0.95, "is_correct": False}
            ],
            "speed_data": [20, 15, 18],
            "help_requests": 0
        }
        
        response = client.post("/api/v1/sessions/test_session_001/detect-gaming", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        
        # Check for repetitive answer evidence
        evidence_types = [e["pattern_type"] for e in data["evidence"]]
        self.assertIn("repetitive_answers", evidence_types)
    
    def test_gaming_detection_help_abuse(self):
        """Test detection of help abuse."""
        request_data = {
            "answers": [
                {"value": 300, "confidence": 0.5, "is_correct": True},
                {"value": 75, "confidence": 0.6, "is_correct": True}
            ],
            "speed_data": [30, 25],
            "help_requests": 5  # Help on most problems
        }
        
        response = client.post("/api/v1/sessions/test_session_001/detect-gaming", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        
        # Check for help abuse evidence
        evidence_types = [e["pattern_type"] for e in data["evidence"]]
        self.assertIn("help_abuse", evidence_types)
    
    def test_gaming_detection_overconfidence(self):
        """Test detection of overconfidence mismatch."""
        request_data = {
            "answers": [
                {"value": 100, "confidence": 0.95, "is_correct": False},
                {"value": 200, "confidence": 0.95, "is_correct": False},
                {"value": 150, "confidence": 0.95, "is_correct": False}
            ],
            "speed_data": [40, 35, 45],
            "help_requests": 0
        }
        
        response = client.post("/api/v1/sessions/test_session_001/detect-gaming", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        
        # Check for overconfidence evidence
        evidence_types = [e["pattern_type"] for e in data["evidence"]]
        self.assertIn("overconfidence_mismatch", evidence_types)
    
    def test_gaming_detection_nonexistent_session(self):
        """Test gaming detection on non-existent session."""
        request_data = {
            "answers": [],
            "speed_data": [],
            "help_requests": 0
        }
        
        response = client.post("/api/v1/sessions/nonexistent/detect-gaming", json=request_data)
        self.assertEqual(response.status_code, 404)


class TestPersonaAwareFeedback(unittest.TestCase):
    """Tests for /feedback/persona-aware endpoint."""
    
    def setUp(self):
        """Clear databases before each test."""
        PERSONA_PROFILES_DB.clear()
        STUDENT_ATTEMPTS_DB.clear()
        
        # Create a test persona profile
        PERSONA_PROFILES_DB["pers_test_feedback_001"] = {
            "id": "pers_test_feedback_001",
            "student_id": "test_feedback_001",
            "persona_type": "cautious_perfectionist",
            "confidence_score": 0.85,
            "characteristics": {
                "speed_pattern": "slow_deliberate",
                "help_seeking_frequency": "selective",
                "accuracy_tendency": "high_accuracy_low_speed",
                "engagement_level": "high",
                "frustration_threshold": "low",
                "confidence_calibration": "underconfident"
            },
            "recommendations": {
                "scaffolding_level": "minimal",
                "feedback_style": "process_focused",
                "pacing_strategy": "self_paced_no_pressure",
                "intervention_triggers": ["excessive_time_on_problem"],
                "motivational_tactics": ["praise_thoroughness"]
            },
            "created_at": "2026-04-19T10:00:00+08:00",
            "updated_at": "2026-04-19T10:00:00+08:00",
            "version": 1
        }
    
    def test_persona_aware_feedback_correct_answer(self):
        """Test persona-aware feedback for correct answer."""
        request_data = {
            "student_id": "test_feedback_001",
            "attempt_data": {
                "problem_id": "prob_001",
                "pathway_type": "before-after-change",
                "equation_shadow": "Original - Sold Monday - Sold Tuesday = Remaining",
                "student_answer": {"type": "numeric", "value": 300},
                "time_spent_seconds": 180,
                "help_used": False,
                "hints_viewed": 0,
                "confidence": 0.7,
                "is_correct": True
            }
        }
        
        response = client.post("/api/v1/feedback/persona-aware", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("affective_feedback", data)
        self.assertIn("strategic_feedback", data)
        self.assertIn("next_step_recommendation", data)
        self.assertIn("scaffolding_adjustment", data)
        
        # For cautious perfectionist with correct answer
        self.assertIn("careful", data["affective_feedback"].lower())
    
    def test_persona_aware_feedback_incorrect_answer(self):
        """Test persona-aware feedback for incorrect answer."""
        request_data = {
            "student_id": "test_feedback_001",
            "attempt_data": {
                "problem_id": "prob_001",
                "pathway_type": "before-after-change",
                "equation_shadow": "Some equation shadow text here",
                "student_answer": {"type": "numeric", "value": 150},
                "time_spent_seconds": 200,
                "help_used": True,
                "hints_viewed": 1,
                "confidence": 0.5,
                "is_correct": False
            }
        }
        
        response = client.post("/api/v1/feedback/persona-aware", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        
        # For cautious perfectionist with incorrect answer
        self.assertIn("okay", data["affective_feedback"].lower())
        self.assertIn("motivational_message", data)
    
    def test_persona_aware_feedback_confident_rusher(self):
        """Test feedback for confident rusher persona."""
        # Create confident rusher profile
        PERSONA_PROFILES_DB["pers_test_feedback_002"] = {
            "id": "pers_test_feedback_002",
            "student_id": "test_feedback_002",
            "persona_type": "confident_rusher",
            "confidence_score": 0.80,
            "characteristics": {
                "speed_pattern": "fast_rushed",
                "help_seeking_frequency": "rare",
                "accuracy_tendency": "low_accuracy_high_speed",
                "engagement_level": "medium",
                "frustration_threshold": "medium",
                "confidence_calibration": "overconfident"
            },
            "recommendations": {
                "scaffolding_level": "high",
                "feedback_style": "accuracy_focused",
                "pacing_strategy": "enforced_deliberation",
                "intervention_triggers": ["too_fast_submission"],
                "motivational_tactics": ["challenge_to_slow_down"]
            },
            "created_at": "2026-04-19T10:00:00+08:00",
            "updated_at": "2026-04-19T10:00:00+08:00",
            "version": 1
        }
        
        request_data = {
            "student_id": "test_feedback_002",
            "attempt_data": {
                "problem_id": "prob_001",
                "pathway_type": "before-after-change",
                "equation_shadow": "Quick answer",
                "student_answer": {"type": "numeric", "value": 300},
                "time_spent_seconds": 20,
                "help_used": False,
                "hints_viewed": 0,
                "confidence": 0.95,
                "is_correct": True
            }
        }
        
        response = client.post("/api/v1/feedback/persona-aware", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        
        # For confident rusher, should encourage slowing down
        self.assertIn("slow", data["strategic_feedback"].lower())
    
    def test_persona_aware_feedback_no_profile(self):
        """Test feedback when no persona profile exists (defaults to balanced)."""
        request_data = {
            "student_id": "unknown_student",
            "attempt_data": {
                "problem_id": "prob_001",
                "pathway_type": "before-after-change",
                "equation_shadow": "Test equation shadow",
                "student_answer": {"type": "numeric", "value": 300},
                "time_spent_seconds": 120,
                "help_used": False,
                "hints_viewed": 0,
                "confidence": 0.8,
                "is_correct": True
            }
        }
        
        response = client.post("/api/v1/feedback/persona-aware", json=request_data)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("affective_feedback", data)
        self.assertIn("strategic_feedback", data)


class TestPersonaTypesEndpoint(unittest.TestCase):
    """Tests for /personas/types endpoint."""
    
    def test_get_persona_types(self):
        """Test retrieving all persona types."""
        response = client.get("/api/v1/personas/types")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("persona_types", data)
        self.assertEqual(len(data["persona_types"]), 6)  # 6 persona types
        
        for pt in data["persona_types"]:
            self.assertIn("type", pt)
            self.assertIn("name", pt)
            self.assertIn("characteristics", pt)
            self.assertIn("recommendations", pt)


class TestStudentAdaptiveHistory(unittest.TestCase):
    """Tests for /students/{id}/adaptive-history endpoint."""
    
    def setUp(self):
        """Clear attempt history before each test."""
        STUDENT_ATTEMPTS_DB.clear()
    
    def test_get_adaptive_history_empty(self):
        """Test getting history for student with no attempts."""
        response = client.get("/api/v1/students/test_history_001/adaptive-history")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data["student_id"], "test_history_001")
        self.assertEqual(data["total_attempts"], 0)
        self.assertEqual(data["recent_attempts"], [])
    
    def test_get_adaptive_history_with_data(self):
        """Test getting history for student with attempts."""
        # Add some attempts
        STUDENT_ATTEMPTS_DB["test_history_002"] = [
            {"problem_id": "prob_001", "pathway": "before-after-change", "is_correct": True, "timestamp": "2026-04-19T10:00:00+08:00"},
            {"problem_id": "prob_002", "pathway": "data-interpretation-red-herring", "is_correct": False, "timestamp": "2026-04-19T10:05:00+08:00"},
            {"problem_id": "prob_003", "pathway": "angles", "is_correct": True, "timestamp": "2026-04-19T10:10:00+08:00"}
        ]
        
        response = client.get("/api/v1/students/test_history_002/adaptive-history")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data["student_id"], "test_history_002")
        self.assertEqual(data["total_attempts"], 3)
        self.assertEqual(len(data["recent_attempts"]), 3)
    
    def test_get_adaptive_history_with_limit(self):
        """Test getting history with limit parameter."""
        # Add many attempts
        STUDENT_ATTEMPTS_DB["test_history_003"] = [
            {"problem_id": f"prob_{i:03d}", "pathway": "before-after-change", "is_correct": True, "timestamp": f"2026-04-19T10:{i:02d}:00+08:00"}
            for i in range(50)
        ]
        
        response = client.get("/api/v1/students/test_history_003/adaptive-history?limit=10")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(len(data["recent_attempts"]), 10)


class TestSystemStats(unittest.TestCase):
    """Tests for updated system stats endpoint."""
    
    def test_system_stats_includes_persona_data(self):
        """Test that system stats includes persona-related counts."""
        response = client.get("/api/v1/system/stats")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("personaProfiles", data)
        self.assertIn("gamingDetections", data)
        self.assertIn("studentAttempts", data)


class TestIntegration(unittest.TestCase):
    """Integration tests for persona-aware workflow."""
    
    def setUp(self):
        """Clear all databases before integration tests."""
        PERSONA_PROFILES_DB.clear()
        STUDENT_ATTEMPTS_DB.clear()
        GAMING_DETECTION_HISTORY.clear()
        SESSIONS_DB.clear()
    
    def test_full_persona_workflow(self):
        """Test the complete persona-aware workflow."""
        student_id = "integration_student_001"
        
        # Step 1: Classify persona
        classify_request = {
            "student_id": student_id,
            "baseline_results": {
                "accuracy_by_pathway": {"before-after-change": 0.75},
                "average_time_per_problem": 150.0,
                "help_usage_rate": 0.3,
                "confidence_calibration_score": 0.7,
                "completion_rate": 0.85
            },
            "behavioral_data": {
                "session_speeds": [120, 150, 180],
                "help_requests": 2,
                "hint_usage_pattern": "selective"
            }
        }
        
        response = client.post("/api/v1/personas/classify", json=classify_request)
        self.assertEqual(response.status_code, 200)
        persona_data = response.json()
        persona_id = persona_data["persona_id"]
        
        # Step 2: Get persona profile
        response = client.get(f"/api/v1/personas/{persona_id}/profile")
        self.assertEqual(response.status_code, 200)
        
        # Step 3: Get adaptive problem
        response = client.get(f"/api/v1/problems/adaptive?student_id={student_id}")
        self.assertEqual(response.status_code, 200)
        problem_data = response.json()
        problem_id = problem_data["problem_id"]
        
        # Step 4: Submit attempt and get persona-aware feedback
        feedback_request = {
            "student_id": student_id,
            "attempt_data": {
                "problem_id": problem_id,
                "pathway_type": problem_data["problem"]["pathway"],
                "equation_shadow": "Test equation shadow for integration test",
                "student_answer": {"type": "numeric", "value": 300},
                "time_spent_seconds": 120,
                "help_used": False,
                "hints_viewed": 0,
                "confidence": 0.8,
                "is_correct": True
            }
        }
        
        response = client.post("/api/v1/feedback/persona-aware", json=feedback_request)
        self.assertEqual(response.status_code, 200)
        
        # Step 5: Check attempt was recorded
        response = client.get(f"/api/v1/students/{student_id}/adaptive-history")
        self.assertEqual(response.status_code, 200)
        history_data = response.json()
        self.assertEqual(history_data["total_attempts"], 1)


def run_tests():
    """Run all tests and return results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestPersonaClassification))
    suite.addTests(loader.loadTestsFromTestCase(TestAdaptiveProblemSelection))
    suite.addTests(loader.loadTestsFromTestCase(TestGamingDetection))
    suite.addTests(loader.loadTestsFromTestCase(TestPersonaAwareFeedback))
    suite.addTests(loader.loadTestsFromTestCase(TestPersonaTypesEndpoint))
    suite.addTests(loader.loadTestsFromTestCase(TestStudentAdaptiveHistory))
    suite.addTests(loader.loadTestsFromTestCase(TestSystemStats))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
