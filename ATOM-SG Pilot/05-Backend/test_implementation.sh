#!/bin/bash

# ATOM-SG Pilot MVP - Implementation Test Script
# This script verifies that all components are in place and the backend can start

echo "======================================"
echo "ATOM-SG Pilot MVP - Implementation Test"
echo "======================================"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counter
PASSED=0
FAILED=0

# Function to check file exists
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} Found: $1"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗${NC} Missing: $1"
        FAILED=$((FAILED + 1))
    fi
}

# Function to check directory exists
check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} Directory: $1"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗${NC} Missing directory: $1"
        FAILED=$((FAILED + 1))
    fi
}

echo "1. Backend Files"
echo "----------------"
check_file "main.py"
check_file "requirements.txt"
check_file "README.md"
check_file "FRONTEND-DEVELOPMENT-GUIDE.md"
echo ""

echo "2. Frontend Files"
echo "------------------"
check_file "frontend/index.html"
check_file "frontend/README.md"
echo ""

echo "3. CSS Files"
echo "-------------"
check_file "frontend/static/css/style.css"
echo ""

echo "4. JavaScript Modules"
echo "--------------------"
check_file "frontend/static/js/api.js"
check_file "frontend/static/js/navigation.js"
check_file "frontend/static/js/dashboard.js"
check_file "frontend/static/js/baseline.js"
check_file "frontend/static/js/practice.js"
check_file "frontend/static/js/pathway-radar.js"
check_file "frontend/static/js/transfer.js"
check_file "frontend/static/js/reflections.js"
check_file "frontend/static/js/canvas.js"
check_file "frontend/static/js/main.js"
echo ""

echo "5. Artifact Directories"
echo "----------------------"
check_dir "artifacts"
check_dir "artifacts/renders"
check_dir "artifacts/ocr"
check_dir "artifacts/sessions"
check_dir "artifacts/collision"
check_dir "artifacts/interpretation"
echo ""

echo "6. Documentation Files"
echo "----------------------"
check_file "../01-Projects/MVP-IMPLEMENTATION-REPORT.md"
check_file "../01-Projects/SubAgentComms.md"
check_file "../01-Projects/MVP-Backend-Alignment.md"
echo ""

echo "7. Checking Python Dependencies"
echo "----------------------------"
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}✓${NC} Python3 found: $(python3 --version)"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} Python3 not found"
    FAILED=$((FAILED + 1))
fi

if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}✓${NC} Pip3 found"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗${NC} Pip3 not found"
    FAILED=$((FAILED + 1))
fi
echo ""

echo "8. File Sizes"
echo "-------------"
if [ -f "main.py" ]; then
    SIZE=$(wc -c < main.py)
    echo -e "${GREEN}✓${NC} main.py: $SIZE bytes"
    PASSED=$((PASSED + 1))
fi

if [ -f "frontend/index.html" ]; then
    SIZE=$(wc -c < frontend/index.html)
    echo -e "${GREEN}✓${NC} frontend/index.html: $SIZE bytes"
    PASSED=$((PASSED + 1))
fi

if [ -f "frontend/static/css/style.css" ]; then
    SIZE=$(wc -c < frontend/static/css/style.css)
    echo -e "${GREEN}✓${NC} frontend/static/css/style.css: $SIZE bytes"
    PASSED=$((PASSED + 1))
fi

JS_TOTAL=0
for file in frontend/static/js/*.js; do
    if [ -f "$file" ]; then
        SIZE=$(wc -c < "$file")
        JS_TOTAL=$((JS_TOTAL + SIZE))
    fi
done
echo -e "${GREEN}✓${NC} JavaScript modules total: $JS_TOTAL bytes"
PASSED=$((PASSED + 1))
echo ""

echo "======================================"
echo "Test Summary"
echo "======================================"
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed!${NC}"
    echo ""
    echo "To start the backend server:"
    echo "  cd ATOM-SG\\ Pilot/05-Backend"
    echo "  pip install -r requirements.txt"
    echo "  python main.py"
    echo ""
    echo "Then open in browser: http://localhost:5000"
    exit 0
else
    echo -e "${RED}✗ Some checks failed. Please review the errors above.${NC}"
    exit 1
fi
