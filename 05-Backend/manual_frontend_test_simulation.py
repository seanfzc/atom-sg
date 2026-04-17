#!/usr/bin/env python3
"""
ATOM-SG MVP Manual Frontend Test Simulation
Simulates user interactions via HTTP requests to test frontend-backend integration.
Tests workflows from MVP_FRONTEND_FUNCTIONAL_TEST_PLAN.md
"""

import requests
import json
import sys
import datetime
from pathlib import Path

BASE_URL = "http://192.168.2.6"
API_URL = f"{BASE_URL}/api/v1"

class FrontendTester:
    def __init__(self):
        self.session = requests.Session()
        self.test_results = []
        self.current_session_id = None
        self.student_id = "test_student_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def log(self, message, success=None):
        """Log test result."""
        if success is True:
            prefix = "✅"
        elif success is False:
            prefix = "❌"
        else:
            prefix = "ℹ️"
        print(f"{prefix} {message}")
        
        if success is not None:
            self.test_results.append({
                "test": message,
                "success": success,
                "timestamp": datetime.datetime.now().isoformat()
            })
    
    def test_endpoint(self, method, endpoint, data=None, expected_status=200, description=None):
        """Test an API endpoint."""
        url = f"{API_URL}/{endpoint}"
        try:
            if method == "GET":
                response = self.session.get(url)
            elif method == "POST":
                headers = {"Content-Type": "application/json"}
                response = self.session.post(url, json=data, headers=headers)
            else:
                self.log(f"Unsupported method: {method}", False)
                return False
            
            if response.status_code == expected_status:
                self.log(f"{description or endpoint} → {response.status_code}", True)
                return response.json() if response.content else {}
            else:
                self.log(f"{description or endpoint} → {response.status_code} (expected {expected_status})", False)
                if response.content:
                    self.log(f"Response: {response.text[:200]}", None)
                return None
        except Exception as e:
            self.log(f"{description or endpoint} → Exception: {e}", False)
            return None
    
    def test_frontend_load(self):
        """Test that frontend loads without critical errors."""
        self.log("\n1. Frontend Load Test", None)
        
        # Test main page
        try:
            response = self.session.get(BASE_URL)
            if response.status_code == 200:
                html = response.text
                
                # Check for critical elements
                checks = [
                    ("ATOM-SG Pilot" in html, "Page title present"),
                    ("<nav" in html, "Navigation bar present"),
                    ("dashboard" in html, "Dashboard section present"),
                    ("practice.js" in html, "Practice JavaScript loaded"),
                    ("api.js" in html, "API JavaScript loaded"),
                ]
                
                all_pass = True
                for condition, msg in checks:
                    if condition:
                        self.log(f"  {msg}", True)
                    else:
                        self.log(f"  {msg}", False)
                        all_pass = False
                
                return all_pass
            else:
                self.log(f"Frontend page returned {response.status_code}", False)
                return False
        except Exception as e:
            self.log(f"Frontend load failed: {e}", False)
            return False
    
    def test_static_assets(self):
        """Test all static assets load."""
        self.log("\n2. Static Assets Test", None)
        
        assets = [
            "/static/css/style.css",
            "/static/js/main.js",
            "/static/js/api.js",
            "/static/js/practice.js",
            "/static/js/navigation.js",
            "/static/js/gamification.js",
            "/static/js/dashboard.js",
            "/static/js/glossary.js",
            "/static/js/canvas.js",
        ]
        
        all_pass = True
        for asset in assets:
            url = f"{BASE_URL}{asset}"
            try:
                response = self.session.get(url)
                if response.status_code == 200:
                    self.log(f"  {asset} → 200", True)
                else:
                    self.log(f"  {asset} → {response.status_code}", False)
                    all_pass = False
            except Exception as e:
                self.log(f"  {asset} → Exception: {e}", False)
                all_pass = False
        
        return all_pass
    
    def test_api_endpoints(self):
        """Test all API endpoints used by frontend."""
        self.log("\n3. API Endpoints Test", None)
        
        endpoints = [
            ("GET", "system/health", None, 200, "Health check"),
            ("GET", "problems", None, 200, "Problems list"),
            ("GET", "rubrics", None, 200, "Rubrics list"),
            ("GET", "renders", None, 200, "Renders list"),
            ("GET", "glossary", None, 200, "Glossary terms"),
            ("GET", "milestones", None, 200, "Milestones"),
            ("GET", "reflections", None, 200, "Reflections"),
            ("GET", "pathway-radar/questions", None, 200, "Pathway radar questions"),
        ]
        
        all_pass = True
        for method, endpoint, data, expected, desc in endpoints:
            result = self.test_endpoint(method, endpoint, data, expected, desc)
            if result is None:
                all_pass = False
        
        return all_pass
    
    def test_practice_session_workflow(self):
        """Test complete practice session workflow."""
        self.log("\n4. Practice Session Workflow", None)
        
        # 4.1 Create practice session (matches frontend practice.js)
        session_data = {
            "week": 2,
            "pathway": "before-after-change",
            "sessionType": "intervention"
        }
        
        result = self.test_endpoint("POST", "practice-sessions", session_data, 201, "Create practice session")
        if not result:
            self.log("Cannot continue practice workflow without session", False)
            return False
        
        self.current_session_id = result.get("id")
        self.log(f"Created session: {self.current_session_id}", True)
        
        # 4.2 Get session details
        self.test_endpoint("GET", f"practice-sessions/{self.current_session_id}", None, 200, "Get session details")
        
        # 4.3 Test "I'm Stuck" button endpoints
        self.test_endpoint("GET", "problems/prob_001/hint", None, 200, "Get problem hint")
        self.test_endpoint("GET", "pathways/before-after-change/example", None, 200, "Get pathway example")
        
        # 4.4 Submit a practice answer (simulating forced articulation + solution)
        submit_data = {
            "problemId": "prob_001",
            "pathwayType": "before-after-change",
            "equationShadow": "First, I need to find the total number of pens by working backwards from the remainder. I'll start with 150 pens left, then add back the pens sold on Tuesday, then Monday.",
            "studentAnswer": {"type": "numeric", "value": 300},
            "diagramAnnotations": []
        }
        
        result = self.test_endpoint("POST", f"practice-sessions/{self.current_session_id}/submit", submit_data, 200, "Submit practice answer")
        
        if result:
            # Check for P0-7 step-by-step scaffolding in response
            feedback = result.get("feedback", {})
            solution_feedback = feedback.get("solutionFeedback", {})
            step_by_step = solution_feedback.get("stepByStep")
            
            if step_by_step:
                self.log("P0-7 Step-by-step scaffolding present in response", True)
                self.log(f"  Pattern: {step_by_step.get('pattern', 'Unknown')}", True)
            else:
                self.log("P0-7 Step-by-step scaffolding not found (may not trigger for correct answer)", None)
        
        return True
    
    def test_pathway_radar_workflow(self):
        """Test pathway radar warm-up workflow."""
        self.log("\n5. Pathway Radar Workflow", None)
        
        # Get today's date in YYYY-MM-DD format (matches frontend)
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Submit radar answers (simulating frontend practice.js)
        submit_data = {
            "date": today,
            "answers": [
                {"questionId": "radar_q001", "identifiedPathway": "before-after-change", "confidence": 0.8},
                {"questionId": "radar_q002", "identifiedPathway": "part-whole-comparison", "confidence": 0.7},
            ]
        }
        
        result = self.test_endpoint("POST", "pathway-radar/submit", submit_data, 200, "Submit pathway radar")
        
        if result:
            # Check for P0-2 gaming detection language
            if "gamingDetected" in result:
                gaming_msg = result.get("gamingMessage", "")
                if "Let's Take a Short Break" in gaming_msg or "We Noticed You're Answering Very Quickly" in gaming_msg:
                    self.log("P0-2 Gaming detection language present (supportive tone)", True)
                else:
                    self.log(f"Gaming message: {gaming_msg[:100]}", None)
        
        return result is not None
    
    def test_reflections_workflow(self):
        """Test reflections submission workflow."""
        self.log("\n6. Reflections Workflow", None)
        
        reflection_data = {
            "week": 2,
            "pathway": "before-after-change",
            "reflection": "I learned how to identify before-after-change problems by looking for sequential changes over time.",
            "confidence": 4.0,
            "struggles": ["calculations", "time-management"],
            "improvements": ["better-accuracy", "clearer-articulation"]
        }
        
        result = self.test_endpoint("POST", "reflections", reflection_data, 201, "Submit reflection")
        return result is not None
    
    def test_p0_p1_fixes_in_frontend(self):
        """Check that P0/P1 fixes are present in frontend code."""
        self.log("\n7. P0/P1 Fixes Verification", None)
        
        # Load practice.js to check for specific fixes
        try:
            response = self.session.get(f"{BASE_URL}/static/js/practice.js")
            if response.status_code == 200:
                practice_js = response.text
                
                checks = [
                    ("stepByStep" in practice_js, "P0-7 Step-by-step scaffolding code"),
                    ("gamingDetected" in practice_js, "P0-2 Gaming detection"),
                    ("stuckButton" in practice_js, "P0-3 'I'm Stuck' button"),
                    ("articulationError" in practice_js, "P0-1 Articulation validation"),
                    ("minimum 50 characters" in practice_js or "minLength" in practice_js, "P0-1 Min 50 chars"),
                    ("glossaryButton" in practice_js, "P0-5 Glossary button"),
                    ("achievement" in practice_js.lower(), "P1-1 Gamification"),
                    ("streak" in practice_js.lower(), "P1-1 Streak tracking"),
                ]
                
                all_pass = True
                for condition, description in checks:
                    if condition:
                        self.log(f"  {description}", True)
                    else:
                        self.log(f"  {description}", False)
                        all_pass = False
                
                return all_pass
            else:
                self.log("Could not load practice.js", False)
                return False
        except Exception as e:
            self.log(f"Error checking frontend code: {e}", False)
            return False
    
    def test_diagram_accessibility(self):
        """Test that geometry diagrams are accessible."""
        self.log("\n8. Diagram Accessibility Test", None)
        
        # Test a few key diagrams that were fixed in P0-6
        diagrams = [
            "G001-angle-diagram-v1.svg",
            "G017-cuboid-v1.svg",
            "G010-composite-shape-v1.svg",
            "G025-pie-chart-v1.svg",
            "G018-cuboid-v1.svg"
        ]
        
        all_pass = True
        for diagram in diagrams:
            url = f"{BASE_URL}/renders/{diagram}"
            try:
                response = self.session.get(url)
                if response.status_code == 200:
                    self.log(f"  {diagram} → 200", True)
                    
                    # Quick check for unit labels in G017
                    if diagram == "G017-cuboid-v1.svg":
                        content = response.text
                        if "l=" in content and "cm" in content:
                            self.log(f"    G017 has unit labels (cm)", True)
                        else:
                            self.log(f"    G017 may be missing unit labels", False)
                            
                else:
                    self.log(f"  {diagram} → {response.status_code}", False)
                    all_pass = False
            except Exception as e:
                self.log(f"  {diagram} → Exception: {e}", False)
                all_pass = False
        
        return all_pass
    
    def run_all_tests(self):
        """Run all test suites."""
        print("=" * 70)
        print("ATOM-SG MVP Manual Frontend Test Simulation")
        print(f"Testing: {BASE_URL}")
        print(f"Student ID: {self.student_id}")
        print("=" * 70)
        
        tests = [
            ("Frontend Load", self.test_frontend_load),
            ("Static Assets", self.test_static_assets),
            ("API Endpoints", self.test_api_endpoints),
            ("Practice Session", self.test_practice_session_workflow),
            ("Pathway Radar", self.test_pathway_radar_workflow),
            ("Reflections", self.test_reflections_workflow),
            ("P0/P1 Fixes", self.test_p0_p1_fixes_in_frontend),
            ("Diagrams", self.test_diagram_accessibility),
        ]
        
        results = {}
        for name, test_func in tests:
            try:
                success = test_func()
                results[name] = success
            except Exception as e:
                self.log(f"Test '{name}' crashed: {e}", False)
                results[name] = False
        
        # Summary
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        
        passed = sum(1 for v in results.values() if v)
        total = len(results)
        
        for name, success in results.items():
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{status} {name}")
        
        print(f"\nOverall: {passed}/{total} test suites passed ({passed/total*100:.1f}%)")
        
        # Recommendations
        print("\n" + "=" * 70)
        print("RECOMMENDATIONS")
        print("=" * 70)
        
        if passed == total:
            print("✅ All automated tests passed!")
            print("Next: Proceed with manual browser testing using MVP_FRONTEND_FUNCTIONAL_TEST_PLAN.md")
            print("Focus on visual UI, canvas interactions, and complete workflow testing.")
        else:
            print("⚠️ Some tests failed. Focus on fixing:")
            for name, success in results.items():
                if not success:
                    print(f"  - {name}")
            
            print("\nAfter fixes, run manual browser testing.")
        
        # Save results
        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "base_url": BASE_URL,
            "student_id": self.student_id,
            "results": results,
            "details": self.test_results
        }
        
        report_path = Path(__file__).parent / "frontend_test_report.json"
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"\nDetailed report saved to: {report_path}")
        
        return passed == total

def main():
    tester = FrontendTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()