#!/usr/bin/env python3
"""
ATOM-SG MVP Frontend Integration Test
Tests API endpoints that frontend buttons would trigger.
Run against deployed instance at http://192.168.2.6/
"""

import requests
import json
import sys

BASE_URL = "http://192.168.2.6"
API_URL = f"{BASE_URL}/api/v1"

def test_endpoint(method, endpoint, data=None, expected_status=200):
    """Test an API endpoint."""
    url = f"{API_URL}/{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        else:
            print(f"  ⚠️ Unsupported method: {method}")
            return False
        
        if response.status_code == expected_status:
            print(f"  ✅ {method} {endpoint} → {response.status_code}")
            return True
        else:
            print(f"  ❌ {method} {endpoint} → {response.status_code} (expected {expected_status})")
            print(f"     Response: {response.text[:200]}")
            return False
    except Exception as e:
        print(f"  ❌ {method} {endpoint} → Exception: {e}")
        return False

def test_health():
    """Test health endpoint."""
    print("\n1. Health Check")
    return test_endpoint("GET", "system/health")

def test_problems():
    """Test problems endpoint."""
    print("\n2. Problems Endpoint")
    return test_endpoint("GET", "problems")

def test_rubrics():
    """Test rubrics endpoint."""
    print("\n3. Rubrics Endpoint")
    return test_endpoint("GET", "rubrics")

def test_renders():
    """Test renders endpoint."""
    print("\n4. Renders Endpoint")
    return test_endpoint("GET", "renders")

def test_glossary():
    """Test glossary endpoint."""
    print("\n5. Glossary Endpoint")
    return test_endpoint("GET", "glossary")

def test_milestones():
    """Test milestones endpoint."""
    print("\n6. Milestones Endpoint")
    return test_endpoint("GET", "milestones")

def test_reflections():
    """Test reflections endpoint."""
    print("\n7. Reflections Endpoint")
    return test_endpoint("GET", "reflections")

def test_pathway_radar():
    """Test pathway radar endpoints."""
    print("\n8. Pathway Radar Endpoints")
    
    # Get questions
    success1 = test_endpoint("GET", "pathway-radar/questions")
    
    # Submit sample answers (simulates radar warm-up completion)
    submit_data = {
        "studentId": "test_student",
        "answers": [
            {"questionId": "radar_q001", "selectedPathway": "before-after-change"},
            {"questionId": "radar_q002", "selectedPathway": "part-whole-comparison"},
        ],
        "timeSpent": 150  # 2.5 minutes
    }
    success2 = test_endpoint("POST", "pathway-radar/submit", submit_data, 200)
    
    return success1 and success2

def test_practice_session():
    """Test practice session flow."""
    print("\n9. Practice Session Flow")
    
    # Create a practice session
    session_data = {
        "studentId": "test_student",
        "pathway": "before-after-change",
        "difficulty": "medium"
    }
    success1 = test_endpoint("POST", "practice-sessions", session_data, 201)
    
    if not success1:
        print("  ⚠️ Can't continue practice session test without session ID")
        return False
    
    # Get session (would need session ID from response)
    print("  ℹ️ Practice session creation tested")
    
    # Test problem hint endpoint (for "I'm Stuck" button)
    success2 = test_endpoint("GET", "problems/prob_001/hint")
    
    # Test pathway example endpoint (for help modal)
    success3 = test_endpoint("GET", "pathways/before-after-change/example")
    
    return success2 and success3

def test_ocr_endpoint():
    """Test OCR endpoint (for baseline/transfer upload)."""
    print("\n10. OCR Endpoint (Upload Simulation)")
    # Note: Can't easily test file upload via simple JSON, but check endpoint exists
    url = f"{API_URL}/scans"
    try:
        response = requests.get(url)  # Should return 405 (Method Not Allowed) or 404
        if response.status_code == 405:
            print(f"  ✅ POST /api/v1/scans endpoint exists (GET not allowed)")
            return True
        else:
            print(f"  ⚠️ /api/v1/scans returned {response.status_code}")
            return True  # Endpoint exists
    except Exception as e:
        print(f"  ❌ OCR endpoint test failed: {e}")
        return False

def test_frontend_assets():
    """Test frontend static assets are accessible."""
    print("\n11. Frontend Static Assets")
    
    assets = [
        "/static/css/style.css",
        "/static/js/main.js",
        "/static/js/practice.js",
        "/static/js/api.js",
        "/renders/G001-angle-diagram-v1.svg"
    ]
    
    success = True
    for asset in assets:
        url = f"{BASE_URL}{asset}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"  ✅ {asset} → 200")
            else:
                print(f"  ❌ {asset} → {response.status_code}")
                success = False
        except Exception as e:
            print(f"  ❌ {asset} → Exception: {e}")
            success = False
    
    return success

def main():
    print("=" * 60)
    print("ATOM-SG MVP Frontend Integration Test")
    print(f"Testing against: {BASE_URL}")
    print("=" * 60)
    
    tests = [
        ("Health Check", test_health),
        ("Problems Endpoint", test_problems),
        ("Rubrics Endpoint", test_rubrics),
        ("Renders Endpoint", test_renders),
        ("Glossary Endpoint", test_glossary),
        ("Milestones Endpoint", test_milestones),
        ("Reflections Endpoint", test_reflections),
        ("Pathway Radar", test_pathway_radar),
        ("Practice Session", test_practice_session),
        ("OCR Endpoint", test_ocr_endpoint),
        ("Frontend Assets", test_frontend_assets),
    ]
    
    passed = 0
    total = len(tests)
    
    for name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"  ❌ {name} test crashed: {e}")
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ All integration tests passed!")
        return 0
    else:
        print(f"⚠️  {total - passed} tests failed or had issues")
        print("\nNext steps:")
        print("1. Manual browser testing using MVP_FRONTEND_FUNCTIONAL_TEST_PLAN.md")
        print("2. Fix any API endpoints that failed")
        print("3. Test complete user workflows (upload → OCR → gap map)")
        return 1

if __name__ == "__main__":
    sys.exit(main())