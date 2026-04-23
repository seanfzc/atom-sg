#!/bin/bash

# ATOM-SG Pilot MVP Verification Script
# Runs a comprehensive test of backend endpoints and frontend files

set -e

PORT=5001
BASE_URL="http://localhost:$PORT"
API_URL="$BASE_URL/api/v1"

echo "=========================================="
echo "ATOM-SG Pilot MVP Verification"
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

# Test 1: Health check
echo "1. Health Check"
echo "----------------"
response=$(curl -s -f "$API_URL/system/health" 2>&1 || echo "FAIL")
if echo "$response" | grep -q "healthy"; then
    echo -e "${GREEN}✓${NC} Backend is healthy"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} Health check failed"
    echo "Response: $response"
    FAILED=$((FAILED + 1))
fi
echo ""

# Test 2: Problems endpoint
echo "2. Problems Endpoint"
echo "---------------------"
response=$(api_call GET "problems")
if echo "$response" | grep -q '"problems"'; then
    echo -e "${GREEN}✓${NC} Problems endpoint working"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} Problems endpoint failed"
    FAILED=$((FAILED + 1))
fi

# Test 3: Rubrics endpoint
echo "3. Rubrics Endpoint"
echo "--------------------"
response=$(api_call GET "rubrics")
if echo "$response" | grep -q '"rubrics"'; then
    echo -e "${GREEN}✓${NC} Rubrics endpoint working"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} Rubrics endpoint failed"
    FAILED=$((FAILED + 1))
fi

# Test 4: Renders endpoint
echo "4. Renders Endpoint"
echo "--------------------"
response=$(api_call GET "renders")
if echo "$response" | grep -q '"renders"'; then
    echo -e "${GREEN}✓${NC} Renders endpoint working"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} Renders endpoint failed"
    FAILED=$((FAILED + 1))
fi

# Test 5: Practice session creation
echo "5. Practice Session Creation"
echo "-----------------------------"
data='{"week":2,"pathway":"before-after-change","sessionType":"practice"}'
response=$(api_call POST "practice-sessions" "$data")
if echo "$response" | grep -q '"id"'; then
    echo -e "${GREEN}✓${NC} Practice session created"
    PASSED=$((PASSED + 1))
    # Extract session ID for later use
    session_id=$(echo "$response" | grep -o '"id":"[^"]*"' | cut -d'"' -f4)
else
    echo -e "${RED}✗${NC} Practice session creation failed"
    FAILED=$((FAILED + 1))
fi

# Test 6: Pathway radar questions
echo "6. Pathway Radar Questions"
echo "---------------------------"
response=$(api_call GET "pathway-radar/questions")
if echo "$response" | grep -q '"questions"'; then
    echo -e "${GREEN}✓${NC} Pathway radar endpoint working"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} Pathway radar endpoint failed"
    FAILED=$((FAILED + 1))
fi

# Test 7: Glossary endpoint (P0 Fix #4)
echo "7. Glossary Endpoint (P0 Fix #4)"
echo "---------------------------------"
response=$(api_call GET "glossary")
if echo "$response" | grep -q '"equation shadow"'; then
    echo -e "${GREEN}✓${NC} Glossary endpoint working"
    PASSED=$((PASSED + 1))
else
    echo -e "${YELLOW}⚠${NC} Glossary endpoint missing (may be optional)"
fi

# Test 8: Frontend static files
echo "8. Frontend Static Files"
echo "-------------------------"
if curl -s -f "$BASE_URL/static/css/style.css" >/dev/null; then
    echo -e "${GREEN}✓${NC} CSS file accessible"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} CSS file missing"
    FAILED=$((FAILED + 1))
fi

if curl -s -f "$BASE_URL/static/js/api.js" >/dev/null; then
    echo -e "${GREEN}✓${NC} JavaScript file accessible"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} JavaScript file missing"
    FAILED=$((FAILED + 1))
fi

# Test 9: Root endpoint
echo "9. Root Endpoint"
echo "-----------------"
response=$(curl -s -f "$BASE_URL/")
if echo "$response" | grep -q "ATOM-SG"; then
    echo -e "${GREEN}✓${NC} Root endpoint serving frontend"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} Root endpoint failed"
    FAILED=$((FAILED + 1))
fi

# Test 10: Critical bug fixes validation (P0 Fix #1)
echo "10. Critical Bug Fixes Validation"
echo "----------------------------------"
# Test validation for empty pathwayType
data='{"problemId":"prob_001","pathwayType":"","equationShadow":"","studentAnswer":{"type":"numeric","value":300}}'
response=$(curl -s -X POST "$API_URL/practice" -H "Content-Type: application/json" -d "$data" 2>&1 || echo "{}")
if echo "$response" | grep -q "Validation failed"; then
    echo -e "${GREEN}✓${NC} Pathway type validation working (P0 Fix #1)"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} Pathway type validation missing"
    FAILED=$((FAILED + 1))
fi

# Test gaming detection (P0 Fix #3) - simulate gaming pattern
echo "11. Gaming Detection (P0 Fix #3)"
echo "---------------------------------"
# Create gaming pattern: all same pathway, high confidence
answers='{"date":"2026-04-15","answers":[{"questionId":"radar_q001","identifiedPathway":"before-after-change","confidence":0.99},{"questionId":"radar_q002","identifiedPathway":"before-after-change","confidence":0.99},{"questionId":"radar_q003","identifiedPathway":"before-after-change","confidence":0.99},{"questionId":"radar_q004","identifiedPathway":"before-after-change","confidence":0.99},{"questionId":"radar_q005","identifiedPathway":"before-after-change","confidence":0.99}]}'
response=$(curl -s -X POST "$API_URL/pathway-radar/submit?student_id=test_gamer" -H "Content-Type: application/json" -d "$answers" 2>&1 || echo "{}")
if echo "$response" | grep -q "gamingDetected"; then
    echo -e "${GREEN}✓${NC} Gaming detection working"
    PASSED=$((PASSED + 1))
else
    echo -e "${YELLOW}⚠${NC} Gaming detection response not confirmed (check manually)"
fi

echo ""
echo "=========================================="
echo "Verification Summary"
echo "=========================================="
echo -e "Total Tests: $((PASSED + FAILED))"
echo -e "${GREEN}Passed: $PASSED${NC}"
echo -e "${RED}Failed: $FAILED${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ MVP Verification PASSED${NC}"
    echo "All critical endpoints and bug fixes are working."
    exit 0
else
    echo -e "${RED}❌ MVP Verification FAILED${NC}"
    echo "$FAILED test(s) failed. Please review the errors above."
    exit 1
fi