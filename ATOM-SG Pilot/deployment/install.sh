#!/bin/bash

# ATOM-SG Pilot MVP Installation Script
# Supports macOS (Homebrew) and Linux (apt/yum)

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
BACKEND_DIR="05-Backend"
REQUIREMENTS_FILE="$BACKEND_DIR/requirements.txt"
VENV_DIR="$BACKEND_DIR/venv"
PYTHON_MIN_VERSION="3.9"
PORT=5000

echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}ATOM-SG Pilot MVP Installation${NC}"
echo -e "${GREEN}==========================================${NC}"
echo ""

# Function to print status
print_status() {
    echo -e "${GREEN}[+]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[-]${NC} $1"
}

# Check if running as root
if [[ $EUID -eq 0 ]]; then
    print_warning "Running as root. It's recommended to run as a regular user."
    read -p "Continue as root? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Detect operating system
detect_os() {
    OS="unknown"
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [[ -f /etc/debian_version ]]; then
            OS="debian"
        elif [[ -f /etc/redhat-release ]]; then then
            OS="redhat"
        elif [[ -f /etc/arch-release ]]; then
            OS="arch"
        else
            OS="linux"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    else
        print_error "Unsupported operating system: $OSTYPE"
        exit 1
    fi
    print_status "Detected OS: $OS"
}

# Install system dependencies
install_system_deps() {
    print_status "Installing system dependencies..."
    
    case $OS in
        "debian"|"ubuntu")
            sudo apt-get update
            sudo apt-get install -y \
                python3 \
                python3-venv \
                python3-pip \
                tesseract-ocr \
                tesseract-ocr-eng \
                libgl1-mesa-glx \
                libglib2.0-0 \
                libsm6 \
                libxext6 \
                libxrender-dev
            # Optional: LaTeX for TikZ rendering
            # sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended
            ;;
        "redhat"|"centos"|"fedora")
            sudo yum install -y \
                python3 \
                python3-venv \
                python3-pip \
                tesseract \
                tesseract-langpack-eng \
                mesa-libGL \
                glib2 \
                libSM \
                libXext \
                libXrender
            # Optional: LaTeX
            # sudo yum install -y texlive-scheme-basic texlive-latex
            ;;
        "arch")
            sudo pacman -Syu --noconfirm \
                python \
                python-pip \
                tesseract \
                tesseract-data-eng \
                mesa \
                glib2 \
                libsm \
                libxext \
                libxrender
            # Optional: LaTeX
            # sudo pacman -S --noconfirm texlive-core texlive-latexextra
            ;;
        "macos")
            if ! command -v brew &> /dev/null; then
                print_error "Homebrew not found. Please install Homebrew first: https://brew.sh"
                exit 1
            fi
            brew update
            brew install python@3.9
            brew install tesseract
            brew install tesseract-lang
            # Optional: LaTeX
            # brew install --cask mactex
            ;;
        *)
            print_error "Unsupported OS for automatic dependency installation."
            print_warning "Please install manually: Python $PYTHON_MIN_VERSION+, Tesseract OCR, and required libraries."
            read -p "Continue with manual dependency check? (y/N): " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                exit 1
            fi
            ;;
    esac
}

# Check Python version
check_python() {
    print_status "Checking Python version..."
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_VERSION=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
        PYTHON_CMD="python"
    else
        print_error "Python not found. Please install Python $PYTHON_MIN_VERSION+"
        exit 1
    fi
    
    # Compare version
    if awk -v ver="$PYTHON_VERSION" -v min="$PYTHON_MIN_VERSION" 'BEGIN { if (ver < min) exit 1; }'; then
        print_status "Python $PYTHON_VERSION found (>= $PYTHON_MIN_VERSION required)"
    else
        print_error "Python $PYTHON_VERSION is too old. Please install Python $PYTHON_MIN_VERSION+"
        exit 1
    fi
}

# Create virtual environment
setup_venv() {
    print_status "Setting up Python virtual environment..."
    
    if [[ -d "$VENV_DIR" ]]; then
        print_warning "Virtual environment already exists at $VENV_DIR"
        read -p "Recreate? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf "$VENV_DIR"
        else
            return 0
        fi
    fi
    
    $PYTHON_CMD -m venv "$VENV_DIR"
    print_status "Virtual environment created at $VENV_DIR"
}

# Install Python dependencies
install_python_deps() {
    print_status "Installing Python dependencies..."
    
    # Activate virtual environment
    if [[ "$OS" == "macos" ]] || [[ "$OS" == "linux" ]]; then
        source "$VENV_DIR/bin/activate"
    else
        # Windows (not supported but just in case)
        source "$VENV_DIR/Scripts/activate"
    fi
    
    # Upgrade pip
    pip install --upgrade pip
    
    # Install requirements
    if [[ -f "$REQUIREMENTS_FILE" ]]; then
        pip install -r "$REQUIREMENTS_FILE"
    else
        print_error "Requirements file not found: $REQUIREMENTS_FILE"
        exit 1
    fi
    
    # Deactivate virtual environment
    deactivate
    
    print_status "Python dependencies installed"
}

# Create artifacts directories
setup_artifacts() {
    print_status "Creating artifacts directories..."
    
    mkdir -p "$BACKEND_DIR/artifacts/renders"
    mkdir -p "$BACKEND_DIR/artifacts/ocr"
    mkdir -p "$BACKEND_DIR/artifacts/sessions"
    mkdir -p "$BACKEND_DIR/artifacts/collision"
    mkdir -p "$BACKEND_DIR/artifacts/interpretation"
    
    print_status "Artifacts directories created"
}

# Create environment file
setup_env() {
    print_status "Setting up environment configuration..."
    
    if [[ ! -f "$BACKEND_DIR/.env" ]]; then
        if [[ -f "deployment/.env.example" ]]; then
            cp "deployment/.env.example" "$BACKEND_DIR/.env"
            print_status "Created .env file from example"
            print_warning "Please edit $BACKEND_DIR/.env to configure your environment"
        else
            print_warning "No .env.example found. Creating minimal .env file"
            cat > "$BACKEND_DIR/.env" << EOF
PORT=5000
HOST=0.0.0.0
DEBUG=false
TESSERACT_LANG=eng
RENDER_FORMAT=svg
EOF
        fi
    else
        print_status ".env file already exists"
    fi
}

# Create start script
create_start_script() {
    print_status "Creating start script..."
    
    cat > "$BACKEND_DIR/start.sh" << 'EOF'
#!/bin/bash
# Start script for ATOM-SG Pilot MVP

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Load environment variables
if [[ -f .env ]]; then
    set -a
    source .env
    set +a
fi

# Default values
PORT=${PORT:-5000}
HOST=${HOST:-0.0.0.0}

# Activate virtual environment
if [[ -d "venv" ]]; then
    source venv/bin/activate
else
    echo "Warning: Virtual environment not found. Using system Python."
fi

# Check if port is already in use
if command -v lsof &> /dev/null; then
    if lsof -i :$PORT &> /dev/null; then
        echo "Error: Port $PORT is already in use."
        echo "Please stop the process using port $PORT or change the PORT in .env"
        exit 1
    fi
fi

echo "Starting ATOM-SG Pilot MVP on http://$HOST:$PORT"
echo "Press Ctrl+C to stop"

# Run the application
exec uvicorn main:app --host "$HOST" --port "$PORT" --log-level info
EOF
    
    chmod +x "$BACKEND_DIR/start.sh"
    
    # Create systemd service file (Linux only)
    if [[ "$OS" == "debian" || "$OS" == "redhat" || "$OS" == "arch" ]]; then
        print_status "Creating systemd service file (optional)..."
        
        SERVICE_FILE="/etc/systemd/system/atom-sg-pilot.service"
        if [[ ! -f "$SERVICE_FILE" ]]; then
            sudo bash -c "cat > $SERVICE_FILE" << EOF
[Unit]
Description=ATOM-SG Pilot MVP Backend
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$(pwd)/$BACKEND_DIR
EnvironmentFile=$(pwd)/$BACKEND_DIR/.env
ExecStart=$(pwd)/$BACKEND_DIR/venv/bin/uvicorn main:app --host \$HOST --port \$PORT --log-level info
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
            print_status "Systemd service file created at $SERVICE_FILE"
            print_warning "To enable and start the service:"
            print_warning "  sudo systemctl daemon-reload"
            print_warning "  sudo systemctl enable atom-sg-pilot"
            print_warning "  sudo systemctl start atom-sg-pilot"
        fi
    fi
}

# Test installation
test_installation() {
    print_status "Testing installation..."
    
    # Check Tesseract
    if command -v tesseract &> /dev/null; then
        print_status "Tesseract found: $(tesseract --version 2>&1 | head -1)"
    else
        print_warning "Tesseract not found in PATH. OCR may not work."
    fi
    
    # Check Python packages
    if [[ -d "$VENV_DIR" ]]; then
        source "$VENV_DIR/bin/activate"
        if python -c "import fastapi" &> /dev/null; then
            print_status "FastAPI installed correctly"
        else
            print_error "FastAPI not installed in virtual environment"
            exit 1
        fi
        deactivate
    fi
    
    print_status "Installation test completed"
}

# Main installation flow
main() {
    detect_os
    check_python
    
    read -p "Install system dependencies? (Y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        install_system_deps
    fi
    
    setup_venv
    install_python_deps
    setup_artifacts
    setup_env
    create_start_script
    test_installation
    
    echo ""
    echo -e "${GREEN}==========================================${NC}"
    echo -e "${GREEN}Installation Complete!${NC}"
    echo -e "${GREEN}==========================================${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Edit configuration: $BACKEND_DIR/.env"
    echo "2. Start the application:"
    echo "   cd $BACKEND_DIR && ./start.sh"
    echo ""
    echo "The application will be available at: http://localhost:$PORT"
    echo ""
    echo "For Docker deployment, see deployment/docker-compose.yml"
}

# Run main function
main "$@"