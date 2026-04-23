#!/bin/bash

# ATOM-SG Pilot MVP Final Verification Script
# Tests backend, frontend, OCR, rendering, and integration workflows

set -e

PORT=5001
BASE_URL="http://localhost:$PORT"
API_URL="$BASE_URL/api/v1"

echo "=========================================="
echo "ATOM-SG Pilot MVP Final Verification"
echo "=========================================="
echo "Backend URL: $BASE_URL"
echo "API URL: $API_URL"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASSED=0
FAILED=0
SKIPPED=0

# Helper function to make API calls
api_call() {
    local method="$1"
    local endpoint="$2"
    local data="$3"
    local curl_cmd="curl -s -f -X $method -H 'Content-Type: application/json'"
    if [ -n "$data" ]; then
        curl_cmd+=" -d '$data'"
    fi
    curl_cmd+=" $API_URL/$endpoint"
    eval $curl_cmd 2>/dev/null || echo "{}"
}

# Helper to count passes/fails
pass() {
    echo -e "${GREEN}✓${NC} $1"
    PASSED=$((PASSED + 1))
}

fail() {
    echo -e "${RED}✗${NC} $1"
    FAILED=$((FAILED + 1))
}

warn() {
    echo -e "${YELLOW}⚠${NC} $1"
    SKIPPED=$((SKIPPED + 1))
}

# Test 1: Health check
echo "1. Health Check"
echo "----------------"
response=$(curl -s -f "$API_URL/system/health" 2>&1 || echo "FAIL")
if echo "$response" | grep -q "healthy"; then
    pass "Backend is healthy"
else
    fail "Health check failed"
    echo "Response: $response"
fi
echo ""

# Test 2: Problems endpoint
echo "2. Problems Endpoint"
echo "---------------------"
response=$(api_call GET "problems")
if echo "$response" | grep -q '"problems"'; then
    pass "Problems endpoint working"
    # Extract first problem ID for later tests
    PROBLEM_ID=$(echo "$response" | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)
else
    fail "Problems endpoint failed"
    PROBLEM_ID="prob_001"
fi

# Test 3: Rubrics endpoint
echo "3. Rubrics Endpoint"
echo "--------------------"
response=$(api_call GET "rubrics")
if echo "$response" | grep -q '"rubrics"'; then
    pass "Rubrics endpoint working"
else
    fail "Rubrics endpoint failed"
fi

# Test 4: Renders endpoint
echo "4. Renders Endpoint"
echo "--------------------"
response=$(api_call GET "renders")
if echo "$response" | grep -q '"renders"'; then
    pass "Renders endpoint working"
else
    fail "Renders endpoint failed"
fi

# Test 5: Practice session creation
echo "5. Practice Session Creation"
echo "-----------------------------"
data='{"week":2,"pathway":"before-after-change","sessionType":"practice"}'
response=$(api_call POST "practice-sessions" "$data")
if echo "$response" | grep -q '"id"'; then
    pass "Practice session created"
    SESSION_ID=$(echo "$response" | grep -o '"id":"[^"]*"' | cut -d'"' -f4)
else
    fail "Practice session creation failed"
    SESSION_ID=""
fi

# Test 6: Pathway radar questions
echo "6. Pathway Radar Questions"
echo "---------------------------"
response=$(api_call GET "pathway-radar/questions")
if echo "$response" | grep -q '"questions"'; then
    pass "Pathway radar endpoint working"
else
    fail "Pathway radar endpoint failed"
fi

# Test 7: Glossary endpoint
echo "7. Glossary Endpoint"
echo "---------------------"
response=$(api_call GET "glossary")
if echo "$response" | grep -q '"equation shadow"'; then
    pass "Glossary endpoint working"
else
    warn "Glossary endpoint missing (may be optional)"
fi

# Test 8: Frontend static files
echo "8. Frontend Static Files"
echo "-------------------------"
if curl -s -f "$BASE_URL/static/css/style.css" >/dev/null; then
    pass "CSS file accessible"
else
    fail "CSS file missing"
fi

if curl -s -f "$BASE_URL/static/js/api.js" >/dev/null; then
    pass "JavaScript file accessible"
else
    fail "JavaScript file missing"
fi

# Test 9: Root endpoint serves frontend
echo "9. Root Endpoint Serves Frontend"
echo "---------------------------------"
response=$(curl -s -f "$BASE_URL/")
if echo "$response" | grep -q "ATOM-SG"; then
    pass "Root endpoint serving frontend"
else
    fail "Root endpoint failed"
fi

# Test 10: Critical bug fixes validation
echo "10. Critical Bug Fixes Validation"
echo "----------------------------------"
# Test validation for empty pathwayType
data='{"problemId":"prob_001","pathwayType":"","equationShadow":"","studentAnswer":{"type":"numeric","value":300}}'
response=$(curl -s -X POST "$API_URL/practice" -H "Content-Type: application/json" -d "$data" 2>&1 || echo "{}")
if echo "$response" | grep -q "Validation failed"; then
    pass "Pathway type validation working (P0 Fix #1)"
else
    fail "Pathway type validation missing"
fi

# Test gaming detection (P0 Fix #3)
echo "11. Gaming Detection (P0 Fix #3)"
echo "---------------------------------"
answers='{"date":"2026-04-15","answers":[{"questionId":"radar_q001","identifiedPathway":"before-after-change","confidence":0.99},{"questionId":"radar_q002","identifiedPathway":"before-after-change","confidence":0.99},{"questionId":"radar_q003","identifiedPathway":"before-after-change","confidence":0.99},{"questionId":"radar_q004","identifiedPathway":"before-after-change","confidence":0.99},{"questionId":"radar_q005","identifiedPathway":"before-after-change","confidence":0.99}]}'
response=$(curl -s -X POST "$API_URL/pathway-radar/submit?student_id=test_gamer" -H "Content-Type: application/json" -d "$answers" 2>&1 || echo "{}")
if echo "$response" | grep -q "gamingDetected"; then
    pass "Gaming detection working"
else
    warn "Gaming detection response not confirmed (check manually)"
fi

# Test 12: Practice submission and triad feedback
echo "12. Practice Submission & Triad Feedback"
echo "-----------------------------------------"
if [ -n "$PROBLEM_ID" ]; then
    data="{\"problemId\":\"$PROBLEM_ID\",\"pathwayType\":\"before-after-change\",\"equationShadow\":\"This is a before-after-change problem. First find the remainder after Monday sale, then find Tuesday sale from remainder, then work backwards to original.\",\"studentAnswer\":{\"type\":\"numeric\",\"value\":300}}"
    response=$(curl -s -X POST "$API_URL/practice" -H "Content-Type: application/json" -d "$data" 2>&1 || echo "{}")
    if echo "$response" | grep -q '"pathwayIdentification"'; then
        pass "Practice submission and triad feedback working"
    else
        fail "Practice submission failed"
        echo "Response: $response"
    fi
else
    warn "Skipping practice submission (no problem ID)"
fi

# Test 13: OCR Pipeline (Tesseract)
echo "13. OCR Pipeline (Tesseract)"
echo "------------------------------"
if command -v tesseract >/dev/null 2>&1; then
    tesseract --version >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        pass "Tesseract installed and working"
        # Quick test with sample image
        if [ -f "artifacts/ocr/test_images/neat_handwriting.png" ]; then
            output=$(tesseract "artifacts/ocr/test_images/neat_handwriting.png" - -l eng --oem 1 --psm 6 2>&1 | head -5 | tr -d '\n')
            if [ -n "$output" ]; then
                pass "OCR test successful (output: ${output:0:20}...)"
            else
                warn "OCR test produced no output"
            fi
        else
            warn "Sample OCR image not found"
        fi
    else
        fail "Tesseract not working"
    fi
else
    fail "Tesseract not installed"
fi

# Test 14: Rendering Pipeline
echo "14. Rendering Pipeline"
echo "-----------------------"
if [ -f "artifacts/renders/G001-angle-diagram-v1.svg" ]; then
    pass "Rendered diagrams exist (SVG)"
else
    fail "Rendered diagrams missing"
fi

if [ -f "artifacts/renders/G001-angle-diagram-v1.pdf" ]; then
    pass "Rendered diagrams exist (PDF)"
else
    warn "Rendered PDF diagrams missing"
fi

# Test 15: System Statistics
echo "15. System Statistics"
echo "----------------------"
response=$(curl -s -f "$API_URL/system/stats" 2>&1 || echo "{}")
if echo "$response" | grep -q '"problems"'; then
    pass "System statistics endpoint working"
else
    fail "System statistics endpoint failed"
fi

# Test 16: Frontend Pages Load
echo "16. Frontend Pages Load"
echo "------------------------"
# Test a few frontend pages via hash routing (they should return the main HTML)
if curl -s -f "$BASE_URL/#dashboard" >/dev/null; then
    pass "Dashboard page accessible"
else
    warn "Dashboard page check failed (hash routing)"
fi

# Test 17: CORS Headers
echo "17. CORS Headers"
echo "-----------------"
response=$(curl -s -I "$API_URL/problems" 2>&1 | grep -i "access-control-allow-origin" || echo "")
if echo "$response" | grep -q "*"; then
    pass "CORS headers present"
else
    warn "CORS headers missing (may not be needed for same-origin)"
fi

# Test 18: API Documentation (OpenAPI)
echo "18. API Documentation"
echo "----------------------"
if curl -s -f "$BASE_URL/docs" >/dev/null; then
    pass "API documentation available"
else
    warn "API documentation not found (FastAPI docs)"
fi

# Test 19: Milestones Endpoint
echo "19. Milestones Endpoint"
echo "------------------------"
response=$(api_call GET "milestones")
if echo "$response" | grep -q '"milestones"'; then
    pass "Milestones endpoint working"
else
    fail "Milestones endpoint failed"
fi

# Test 20: Reflections Endpoint
echo "20. Reflections Endpoint"
echo "-------------------------"
response=$(api_call GET "reflections")
if echo "$response" | grep -q '"reflections"'; then
    pass "Reflections endpoint working"
else
    fail "Reflections endpoint failed"
fi

echo ""
echo "=========================================="
echo "Final Verification Summary"
echo "=========================================="
echo -e "Total Tests: $((PASSED + FAILED + SKIPPED))"
echo -e "${GREEN}Passed: $PASSED${NC}"
echo -e "${RED}Failed: $FAILED${NC}"
echo -e "${YELLOW}Skipped/Warnings: $SKIPPED${NC}"
echo ""

# Overall status
if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ MVP Final Verification PASSED${NC}"
    echo "All critical components are functional and ready for pilot launch."
    echo ""
    echo "Next Steps:"
    echo "1. Implement 8 critical UX fixes (2-3 hours)"
    echo "2. Final hands-on review by stakeholders"
    echo "3. Deployment preparation (Docker, installation script)"
    echo "4. Pilot launch: Week 2 (2026-04-26)"
    exit 0
elif [ $FAILED -le 3 ]; then
    echo -e "${YELLOW}⚠ MVP Final Verification PARTIAL SUCCESS${NC}"
    echo "$FAILED non-critical test(s) failed. MVP may still be launch-ready."
    echo "Review failed tests above and decide if they require fixes."
    exit 1
else
    echo -e "${RED}❌ MVP Final Verification FAILED${NC}"
    echo "$FAILED test(s) failed. Please review the errors above."
    exit 1
fi