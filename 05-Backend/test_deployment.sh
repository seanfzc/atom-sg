#!/bin/bash
# Test deployment script for ATOM-SG MVP Backend
# Runs basic checks to ensure system is ready for pilot

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_success() {
    echo -e "${GREEN}[PASS]${NC} $1"
}

print_failure() {
    echo -e "${RED}[FAIL]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_info() {
    echo -e "[INFO] $1"
}

# Test 1: Check Python version
print_info "Test 1: Checking Python version..."
if command -v python3.11 &> /dev/null; then
    PYTHON_CMD="python3.11"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    version=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
    if [[ ! "$version" =~ ^3\.1[1-9] ]]; then
        print_warning "Python $version found (3.11+ recommended)"
    fi
else
    print_failure "Python not found"
    exit 1
fi
print_success "Python available: $($PYTHON_CMD --version)"

# Test 2: Check Tesseract
print_info "Test 2: Checking Tesseract OCR..."
if command -v tesseract &> /dev/null; then
    tesseract_version=$(tesseract --version 2>&1 | head -n1)
    print_success "Tesseract available: $tesseract_version"
else
    print_failure "Tesseract not found"
    exit 1
fi

# Test 3: Check virtual environment
print_info "Test 3: Checking Python virtual environment..."
if [[ -d "venv" ]]; then
    print_success "Virtual environment exists"
else
    print_warning "Virtual environment not found (run ./install.sh)"
fi

# Test 4: Check Python dependencies
print_info "Test 4: Checking Python dependencies..."
if [[ -d "venv" ]]; then
    source venv/bin/activate
    if python -c "import fastapi, pytesseract, matplotlib, reportlab" 2>/dev/null; then
        print_success "All required Python packages installed"
    else
        print_failure "Missing Python packages"
        exit 1
    fi
    deactivate
else
    print_warning "Skipping dependency check (no virtual environment)"
fi

# Test 5: Check directory structure
print_info "Test 5: Checking directory structure..."
required_dirs=(
    "artifacts"
    "artifacts/renders"
    "artifacts/ocr"
    "artifacts/sessions"
    "artifacts/collision"
    "artifacts/interpretation"
    "logs"
)

for dir in "${required_dirs[@]}"; do
    if [[ -d "$dir" ]]; then
        print_success "Directory exists: $dir"
    else
        print_failure "Missing directory: $dir"
        exit 1
    fi
done

# Test 6: Check configuration files
print_info "Test 6: Checking configuration files..."
if [[ -f ".env" ]]; then
    print_success ".env file exists"
else
    print_warning ".env file not found (copy from .env.example)"
fi

if [[ -f "requirements.txt" ]]; then
    print_success "requirements.txt exists"
else
    print_failure "requirements.txt missing"
    exit 1
fi

# Test 7: Check main application file
print_info "Test 7: Checking main application..."
if [[ -f "main.py" ]]; then
    print_success "main.py exists"
else
    print_failure "main.py missing"
    exit 1
fi

# Test 8: Check frontend files
print_info "Test 8: Checking frontend files..."
if [[ -f "frontend/index.html" ]]; then
    print_success "Frontend index.html exists"
else
    print_failure "Frontend index.html missing"
    exit 1
fi

# Test 9: Check backup scripts
print_info "Test 9: Checking backup scripts..."
if [[ -f "backup.sh" ]]; then
    print_success "backup.sh exists"
else
    print_warning "backup.sh not found (run ./install.sh)"
fi

if [[ -f "health_check.sh" ]]; then
    print_success "health_check.sh exists"
else
    print_warning "health_check.sh not found (run ./install.sh)"
fi

# Test 10: Check Docker artifacts (optional)
print_info "Test 10: Checking Docker artifacts..."
if [[ -f "Dockerfile" ]]; then
    print_success "Dockerfile exists"
else
    print_warning "Dockerfile not found"
fi

if [[ -f "docker-compose.yml" ]]; then
    print_success "docker-compose.yml exists"
else
    print_warning "docker-compose.yml not found"
fi

# Summary
echo ""
echo "========================================"
echo "Deployment Test Summary"
echo "========================================"
print_info "All critical tests passed!"
print_info "System is ready for deployment."
echo ""
print_info "Next steps:"
print_info "1. Review .env configuration"
print_info "2. Start backend: ./start.sh"
print_info "3. Verify API: curl http://localhost:5000/api/v1/system/health"
print_info "4. Access frontend: http://localhost:5000/"
echo ""
print_info "For production deployment, also:"
print_info "- Set up reverse proxy (nginx)"
print_info "- Configure SSL certificates"
print_info "- Set up monitoring and alerts"
print_info "- Schedule regular backups"
echo "========================================"