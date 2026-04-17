#!/bin/bash
# Start script for ATOM-SG MVP Backend

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if .env exists
if [[ ! -f .env ]]; then
    print_warning ".env file not found. Creating from example..."
    if [[ -f .env.example ]]; then
        cp .env.example .env
        print_info "Created .env from .env.example (please review settings)"
    else
        print_error "No .env.example found. Please create a .env file."
        exit 1
    fi
fi

# Load environment variables
set -a
source .env
set +a

# Check Python virtual environment
if [[ ! -d "venv" ]]; then
    print_warning "Python virtual environment not found."
    read -p "Create virtual environment and install dependencies? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
    else
        print_info "Using system Python. Make sure dependencies are installed."
    fi
else
    source venv/bin/activate
fi

# Check Tesseract
if ! command -v "$TESSERACT_CMD" &> /dev/null; then
    print_warning "Tesseract not found at $TESSERACT_CMD"
    print_info "Please install Tesseract OCR:"
    print_info "  Ubuntu/Debian: sudo apt-get install tesseract-ocr"
    print_info "  macOS: brew install tesseract"
    print_info "Or update TESSERACT_CMD in .env"
fi

# Create required directories
mkdir -p artifacts/{renders,ocr,sessions,collision,interpretation}
mkdir -p logs

print_info "Starting ATOM-SG MVP Backend..."
print_info "Host: ${HOST:-0.0.0.0}"
print_info "Port: ${PORT:-5000}"
print_info "Debug: ${DEBUG:-false}"
print_info ""
print_info "API Documentation: http://${HOST:-localhost}:${PORT:-5000}/docs"
print_info "Frontend: http://${HOST:-localhost}:${PORT:-5000}/"
print_info ""
print_info "Press Ctrl+C to stop"

# Start the backend
exec uvicorn main:app --host "${HOST:-0.0.0.0}" --port "${PORT:-5000}" --reload