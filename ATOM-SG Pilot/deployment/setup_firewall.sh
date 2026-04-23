#!/bin/bash

# ATOM-SG Pilot MVP - Firewall Setup Script
# Configures UFW firewall for production deployment

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Default ports
SSH_PORT="${SSH_PORT:-22}"
HTTP_PORT="${HTTP_PORT:-80}"
HTTPS_PORT="${HTTPS_PORT:-443}"
BACKEND_PORT="${BACKEND_PORT:-5000}"

# Log function
log() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    case "$level" in
        "INFO") echo -e "${GREEN}[$timestamp] [$level]${NC} $message" ;;
        "WARN") echo -e "${YELLOW}[$timestamp] [$level]${NC} $message" ;;
        "ERROR") echo -e "${RED}[$timestamp] [$level]${NC} $message" ;;
        *) echo "[$timestamp] [$level] $message" ;;
    esac
}

# Check if running as root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        log "ERROR" "This script must be run as root (use sudo)"
        exit 1
    fi
}

# Detect OS
detect_os() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS="$NAME"
        VERSION="$VERSION_ID"
    else
        OS=$(uname -s)
        VERSION=$(uname -r)
    fi
    
    log "INFO" "Detected OS: $OS $VERSION"
}

# Check if UFW is available
check_ufw() {
    if ! command -v ufw &> /dev/null; then
        log "WARN" "UFW not found. Installing..."
        
        case "$OS" in
            *Ubuntu*|*Debian*)
                apt-get update
                apt-get install -y ufw
                ;;
            *CentOS*|*RedHat*|*Fedora*)
                yum install -y ufw || dnf install -y ufw
                ;;
            *)
                log "ERROR" "Cannot install UFW automatically on $OS"
                log "INFO" "Please install UFW manually and run this script again"
                exit 1
                ;;
        esac
        
        if ! command -v ufw &> /dev/null; then
            log "ERROR" "Failed to install UFW"
            exit 1
        fi
    fi
    
    log "INFO" "UFW is available"
}

# Setup firewall rules
setup_firewall() {
    log "INFO" "Setting up firewall rules..."
    
    # Reset to default (allow outgoing, deny incoming)
    log "INFO" "Resetting UFW to defaults..."
    ufw --force reset
    
    # Set default policies
    log "INFO" "Setting default policies: deny incoming, allow outgoing"
    ufw default deny incoming
    ufw default allow outgoing
    
    # Allow SSH
    log "INFO" "Allowing SSH on port $SSH_PORT"
    ufw allow "$SSH_PORT"/tcp comment 'SSH'
    
    # Allow HTTP/HTTPS (for nginx reverse proxy)
    if [ "$HTTP_PORT" != "disabled" ]; then
        log "INFO" "Allowing HTTP on port $HTTP_PORT"
        ufw allow "$HTTP_PORT"/tcp comment 'HTTP'
    fi
    
    if [ "$HTTPS_PORT" != "disabled" ]; then
        log "INFO" "Allowing HTTPS on port $HTTPS_PORT"
        ufw allow "$HTTPS_PORT"/tcp comment 'HTTPS'
    fi
    
    # Allow backend port (if not using reverse proxy)
    if [ "$BACKEND_PORT" != "disabled" ] && [ "$BACKEND_PORT" != "$HTTP_PORT" ] && [ "$BACKEND_PORT" != "$HTTPS_PORT" ]; then
        log "INFO" "Allowing backend on port $BACKEND_PORT"
        ufw allow "$BACKEND_PORT"/tcp comment 'ATOM-SG Backend'
    fi
    
    # Enable UFW
    log "INFO" "Enabling UFW..."
    ufw --force enable
    
    # Show status
    log "INFO" "Firewall status:"
    ufw status verbose
}

# Setup rate limiting (optional)
setup_rate_limiting() {
    log "INFO" "Setting up rate limiting..."
    
    # Create rate limiting rules file
    local rules_file="/etc/ufw/before.rules"
    
    # Add rate limiting for HTTP/HTTPS (if using)
    if [ "$HTTP_PORT" != "disabled" ]; then
        log "INFO" "Adding rate limiting for HTTP port $HTTP_PORT"
        # Note: UFW doesn't have built-in rate limiting, would need iptables rules
        # For simplicity, we'll just log this as a recommendation
        log "WARN" "Rate limiting configuration requires custom iptables rules"
        log "INFO" "Consider using nginx rate limiting for HTTP/HTTPS traffic"
    fi
    
    log "INFO" "Rate limiting setup complete (configuration logged)"
}

# Create application-specific rule file
create_app_rules() {
    log "INFO" "Creating application-specific firewall rules..."
    
    local app_rules_dir="/etc/ufw/applications.d"
    local app_rules_file="$app_rules_dir/atom-sg-pilot"
    
    mkdir -p "$app_rules_dir"
    
    cat > "$app_rules_file" << EOF
[ATOM-SG-Pilot]
title=ATOM-SG Pilot MVP
description=Recognition-First Integrated Training System for P6 Mathematics
ports=$BACKEND_PORT/tcp
EOF
    
    log "INFO" "Application rules file created: $app_rules_file"
    
    # Update UFW to recognize application
    ufw app update ATOM-SG-Pilot 2>/dev/null || true
}

# Test firewall configuration
test_firewall() {
    log "INFO" "Testing firewall configuration..."
    
    # Check if UFW is active
    if ! ufw status | grep -q "Status: active"; then
        log "ERROR" "UFW is not active"
        return 1
    fi
    
    # Check if SSH is allowed
    if ! ufw status | grep -q "$SSH_PORT/tcp.*ALLOW"; then
        log "WARN" "SSH port $SSH_PORT may not be properly configured"
    fi
    
    # Check if HTTP is allowed (if enabled)
    if [ "$HTTP_PORT" != "disabled" ] && ! ufw status | grep -q "$HTTP_PORT/tcp.*ALLOW"; then
        log "WARN" "HTTP port $HTTP_PORT may not be properly configured"
    fi
    
    log "INFO" "Firewall configuration test complete"
    return 0
}

# Main execution
main() {
    log "INFO" "=========================================="
    log "INFO" "ATOM-SG Pilot MVP - Firewall Setup"
    log "INFO" "=========================================="
    
    check_root
    detect_os
    check_ufw
    create_app_rules
    setup_firewall
    setup_rate_limiting
    
    if test_firewall; then
        log "INFO" "✅ Firewall setup completed successfully"
        log "INFO" ""
        log "INFO" "IMPORTANT: Ensure SSH port $SSH_PORT is accessible"
        log "INFO" "If you lose SSH access, you may need console access to fix"
        log "INFO" ""
        log "INFO" "Firewall rules summary:"
        ufw status numbered
    else
        log "ERROR" "❌ Firewall setup failed"
        exit 1
    fi
}

# Run main function
main "$@"