#!/bin/bash
# ATOM-SG MVP Backend Installation Script
# System-aware installer for macOS, Ubuntu/Debian, RHEL/CentOS, Arch Linux

set -e  # Exit on error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
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

print_step() {
    echo -e "${GREEN}==>${NC} $1"
}

# Dry-run mode
DRY_RUN=false
for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
    esac
done

# Detect OS
detect_os() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ -f /etc/os-release ]]; then
        . /etc/os-release
        OS="$ID"
    elif [[ -f /etc/redhat-release ]]; then
        OS="rhel"
    elif [[ -f /etc/arch-release ]]; then
        OS="arch"
    else
        OS="unknown"
    fi
    print_info "Detected OS: $OS"
}

# Install system packages based on OS
install_system_packages() {
    print_step "Installing system packages..."
    
    if [ "$DRY_RUN" = true ]; then
        print_info "Dry run mode - skipping package installation"
        return 0
    fi
    
    case $OS in
        macos)
            # Check if Homebrew is installed
            if ! command -v brew &> /dev/null; then
                print_error "Homebrew not found. Please install Homebrew first: https://brew.sh"
                exit 1
            fi
            brew update
            brew install tesseract python@3.11 poppler
            # Optional: install basictex for LaTeX/TikZ
            # brew install --cask basictex
            ;;
        ubuntu|debian|pop)
            sudo apt-get update
            sudo apt-get install -y \
                python3.11 \
                python3-pip \
                python3-venv \
                tesseract-ocr \
                libtesseract-dev \
                libgl1-mesa-glx \
                libglib2.0-0 \
                poppler-utils \
                fonts-dejavu
            # Optional: LaTeX for TikZ
            # sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended
            ;;
        rhel|centos|fedora)
            sudo dnf install -y \
                python3.11 \
                python3-pip \
                tesseract \
                tesseract-devel \
                mesa-libGL \
                glib2 \
                poppler-utils \
                dejavu-sans-fonts
            # Optional: LaTeX
            # sudo dnf install -y texlive-scheme-basic texlive-collection-latexextra
            ;;
        arch)
            sudo pacman -Syu --noconfirm \
                python \
                python-pip \
                tesseract \
                tesseract-data-eng \
                mesa \
                glib2 \
                poppler \
                ttf-dejavu
            # Optional: LaTeX
            # sudo pacman -S --noconfirm texlive-core texlive-latexextra
            ;;
        *)
            print_error "Unsupported OS: $OS"
            print_info "Please install the following manually:"
            print_info "- Python 3.11 or higher"
            print_info "- Tesseract OCR 5.5.2 or higher"
            print_info "- Poppler utilities (for PDF processing)"
            print_info "- GL libraries (for matplotlib)"
            exit 1
            ;;
    esac
}

# Setup Python virtual environment
setup_python_env() {
    print_step "Setting up Python virtual environment..."
    
    # Check if Python 3.11 is available
    if command -v python3.11 &> /dev/null; then
        PYTHON_CMD="python3.11"
    elif command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        # Check version
        PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
        if [[ ! "$PYTHON_VERSION" =~ ^3\.1[1-9] ]]; then
            print_warning "Python version $PYTHON_VERSION found. Python 3.11 or higher is recommended."
        fi
    else
        print_error "Python not found. Please install Python 3.11 or higher."
        exit 1
    fi
    
    if [ "$DRY_RUN" = true ]; then
        print_info "Dry run mode - skipping virtual environment creation and package installation"
        return 0
    fi
    
    # Create virtual environment
    $PYTHON_CMD -m venv venv
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Upgrade pip
    pip install --upgrade pip
    
    # Install Python dependencies
    print_step "Installing Python dependencies..."
    pip install -r requirements.txt
}

# Create configuration files
create_config_files() {
    print_step "Creating configuration files..."
    
    if [ "$DRY_RUN" = true ]; then
        print_info "Dry run mode - skipping file creation"
        return 0
    fi
    
    # Create .env.example if not exists
    if [[ ! -f .env.example ]]; then
        cat > .env.example << EOF
# ATOM-SG MVP Backend Configuration
# Copy this file to .env and adjust values

# Server configuration
PORT=5000
HOST=0.0.0.0
DEBUG=false

# File paths
ARTIFACTS_DIR=./artifacts
TESSERACT_CMD=/usr/bin/tesseract

# Rendering settings
RENDER_FORMAT=svg  # svg or png
TIKZ_ENABLED=false  # Set to true if LaTeX/TikZ is installed

# OCR settings
OCR_CONFIDENCE_THRESHOLD=0.7
OCR_LANGUAGE=eng

# Performance settings
MAX_RENDER_TIME=30
MAX_OCR_TIME=60
MAX_COLLISION_TIME=60

# Security (optional)
# CORS_ORIGINS=http://localhost:3000,http://localhost:5000
# API_KEY=your-secret-key

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/backend.log
EOF
        print_info "Created .env.example"
    fi
    
    # Create logs directory
    mkdir -p logs
    
    # Create artifacts subdirectories
    mkdir -p artifacts/{renders,ocr,sessions,collision,interpretation}
    
    # Create default .env if not exists
    if [[ ! -f .env ]]; then
        cp .env.example .env
        print_info "Created .env from .env.example (please review settings)"
    fi
}

# Create systemd service file (for Linux systems)
create_systemd_service() {
    if [[ "$OS" != "macos" && "$OS" != "unknown" ]]; then
        if [ "$DRY_RUN" = true ]; then
            print_info "Dry run mode - skipping systemd service file creation"
            return 0
        fi
        print_step "Creating systemd service file..."
        
        SERVICE_FILE="/etc/systemd/system/atom-sg-backend.service"
        
        if [[ -f "$SERVICE_FILE" ]]; then
            print_warning "Systemd service file already exists: $SERVICE_FILE"
            return
        fi
        
        sudo bash -c "cat > $SERVICE_FILE" << EOF
[Unit]
Description=ATOM-SG MVP Backend
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$(pwd)
EnvironmentFile=$(pwd)/.env
ExecStart=$(pwd)/venv/bin/uvicorn main:app --host \$HOST --port \$PORT
Restart=on-failure
RestartSec=10
StandardOutput=append:$(pwd)/logs/systemd.log
StandardError=append:$(pwd)/logs/systemd-error.log

[Install]
WantedBy=multi-user.target
EOF
        
        print_info "Systemd service file created at $SERVICE_FILE"
        print_info "To enable and start the service:"
        print_info "  sudo systemctl daemon-reload"
        print_info "  sudo systemctl enable atom-sg-backend"
        print_info "  sudo systemctl start atom-sg-backend"
    fi
}

# Create backup script
create_backup_script() {
    print_step "Creating backup script..."
    
    if [ "$DRY_RUN" = true ]; then
        print_info "Dry run mode - skipping backup script creation"
        return 0
    fi
    
    cat > backup.sh << 'EOF'
#!/bin/bash
# Backup script for ATOM-SG MVP Backend
# Run daily via cron to backup artifacts and configuration

set -e

BACKUP_DIR="./backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Backup artifacts and logs
echo "Creating backup: $BACKUP_FILE"
tar -czf "$BACKUP_FILE" \
    ./artifacts \
    ./logs \
    ./.env \
    ./requirements.txt \
    ./main.py \
    ./frontend 2>/dev/null || true

# Keep only last 30 backups
echo "Cleaning up old backups (keeping last 30)..."
ls -tp "$BACKUP_DIR/" | grep -v '/$' | tail -n +31 | xargs -I {} rm -- "$BACKUP_DIR/{}"

echo "Backup completed: $BACKUP_FILE"
EOF
    
    chmod +x backup.sh
    
    # Create restore script
    cat > restore_backup.sh << 'EOF'
#!/bin/bash
# Restore backup for ATOM-SG MVP Backend

set -e

BACKUP_DIR="./backups"

if [[ -z "$1" ]]; then
    echo "Usage: $0 <backup_file>"
    echo "Available backups:"
    ls -l "$BACKUP_DIR/" 2>/dev/null || echo "No backups found"
    exit 1
fi

BACKUP_FILE="$1"
if [[ ! -f "$BACKUP_FILE" ]]; then
    echo "Backup file not found: $BACKUP_FILE"
    exit 1
fi

echo "Restoring from backup: $BACKUP_FILE"
echo "WARNING: This will overwrite existing artifacts and logs!"
read -p "Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Restore cancelled"
    exit 0
fi

# Stop service if running
systemctl stop atom-sg-backend 2>/dev/null || true

# Extract backup
tar -xzf "$BACKUP_FILE"

echo "Backup restored successfully"
echo "You may need to restart the backend service"
EOF
    
    chmod +x restore_backup.sh
    
    print_info "Backup scripts created:"
    print_info "  ./backup.sh - Create backup (keep last 30)"
    print_info "  ./restore_backup.sh <file> - Restore from backup"
}

# Create health check script
create_health_check() {
    print_step "Creating health check script..."
    
    if [ "$DRY_RUN" = true ]; then
        print_info "Dry run mode - skipping health check script creation"
        return 0
    fi
    
    cat > health_check.sh << 'EOF'
#!/bin/bash
# Health check script for ATOM-SG MVP Backend

set -e

API_URL="http://localhost:5000/api/v1/system/health"
LOG_FILE="./logs/health_check.log"

# Create log directory if it doesn't exist
mkdir -p ./logs

# Check API health
echo "$(date '+%Y-%m-%d %H:%M:%S') - Health check started" >> "$LOG_FILE"

if curl -f -s --max-time 5 "$API_URL" > /dev/null; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Health check PASSED" >> "$LOG_FILE"
    echo "OK"
    exit 0
else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Health check FAILED" >> "$LOG_FILE"
    echo "FAIL"
    exit 1
fi
EOF
    
    chmod +x health_check.sh
    
    print_info "Health check script created: ./health_check.sh"
}

# Main installation process
main() {
    print_info "Starting ATOM-SG MVP Backend installation..."
    
    # Check if running as root
    if [[ $EUID -eq 0 ]]; then
        print_warning "Running as root is not recommended. Continuing anyway..."
    fi
    
    detect_os
    install_system_packages
    setup_python_env
    create_config_files
    create_systemd_service
    create_backup_script
    create_health_check
    
    print_info ""
    print_info "Installation completed successfully!"
    print_info ""
    print_info "Next steps:"
    print_info "1. Review the .env file and adjust settings if needed"
    print_info "2. Activate the virtual environment: source venv/bin/activate"
    print_info "3. Start the backend: uvicorn main:app --host 0.0.0.0 --port 5000"
    print_info "4. Open http://localhost:5000 in your browser"
    print_info ""
    print_info "For production deployment:"
    print_info "- Review and adjust the systemd service file"
    print_info "- Set up HTTPS via reverse proxy (nginx, Caddy, etc.)"
    print_info "- Configure firewall to allow port 5000"
    print_info "- Set up regular backups using cron: 0 2 * * * $(pwd)/backup.sh"
    print_info ""
    print_info "Documentation:"
    print_info "- API documentation: http://localhost:5000/docs"
    print_info "- Frontend guide: FRONTEND-DEVELOPMENT-GUIDE.md"
}

# Run main function
main "$@"