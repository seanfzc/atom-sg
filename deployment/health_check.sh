#!/bin/bash

# ATOM-SG Pilot MVP - Health Check Script
# Monitors backend health and sends alerts if service is down

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
HEALTH_URL="${HEALTH_URL:-http://localhost:5000/api/v1/system/health}"
TIMEOUT="${TIMEOUT:-10}" # seconds
MAX_RETRIES="${MAX_RETRIES:-2}"
RETRY_DELAY="${RETRY_DELAY:-5}" # seconds
LOG_FILE="${LOG_FILE:-/var/log/atom-sg-health.log}"
ALERT_EMAIL="${ALERT_EMAIL:-}" # Optional: email for alerts
SERVICE_NAME="${SERVICE_NAME:-atom-sg-backend}"

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

# Log function
log() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "[$timestamp] [$level] $message" >> "$LOG_FILE"
    
    case "$level" in
        "INFO") echo -e "${GREEN}[$timestamp] [$level]${NC} $message" ;;
        "WARN") echo -e "${YELLOW}[$timestamp] [$level]${NC} $message" ;;
        "ERROR") echo -e "${RED}[$timestamp] [$level]${NC} $message" ;;
        *) echo "[$timestamp] [$level] $message" ;;
    esac
}

# Check health function
check_health() {
    local retries=0
    local response=""
    
    while [ $retries -lt $MAX_RETRIES ]; do
        log "INFO" "Checking health at: $HEALTH_URL (attempt $((retries+1))/$MAX_RETRIES)"
        
        # Use curl with timeout
        response=$(curl -s -f --max-time "$TIMEOUT" "$HEALTH_URL" 2>/dev/null || echo "CURL_FAILED")
        
        if [ "$response" != "CURL_FAILED" ]; then
            # Parse JSON response
            local status=$(echo "$response" | grep -o '"status":"[^"]*"' | cut -d'"' -f4)
            
            if [ "$status" = "healthy" ]; then
                log "INFO" "Health check PASSED: status=$status"
                return 0
            else
                log "WARN" "Health check WARNING: status=$status (expected 'healthy')"
                return 1
            fi
        else
            log "WARN" "Health check failed (timeout/connection), retrying in $RETRY_DELAY seconds..."
            sleep "$RETRY_DELAY"
            retries=$((retries + 1))
        fi
    done
    
    log "ERROR" "Health check FAILED after $MAX_RETRIES attempts"
    return 2
}

# Restart service function (Docker Compose)
restart_service() {
    log "INFO" "Attempting to restart service: $SERVICE_NAME"
    
    # Try Docker Compose restart
    if command -v docker-compose &> /dev/null; then
        cd "$(dirname "$0")" || exit 1
        if docker-compose ps "$SERVICE_NAME" &> /dev/null; then
            log "INFO" "Restarting with Docker Compose..."
            docker-compose restart "$SERVICE_NAME"
            sleep 10 # Wait for service to start
            
            # Check if restart was successful
            if docker-compose ps "$SERVICE_NAME" | grep -q "Up"; then
                log "INFO" "Service restarted successfully"
                return 0
            else
                log "ERROR" "Service failed to start after restart"
                return 1
            fi
        fi
    fi
    
    # Try systemctl if available
    if command -v systemctl &> /dev/null; then
        if systemctl list-units --full -all | grep -q "$SERVICE_NAME"; then
            log "INFO" "Restarting with systemctl..."
            systemctl restart "$SERVICE_NAME"
            sleep 5
            
            if systemctl is-active --quiet "$SERVICE_NAME"; then
                log "INFO" "Service restarted successfully (systemctl)"
                return 0
            else
                log "ERROR" "Service failed to start (systemctl)"
                return 1
            fi
        fi
    fi
    
    log "ERROR" "Could not find service manager (docker-compose or systemctl)"
    return 2
}

# Send alert function
send_alert() {
    local message="$1"
    
    log "ERROR" "SENDING ALERT: $message"
    
    # Email alert (if configured)
    if [ -n "$ALERT_EMAIL" ]; then
        echo "Subject: ATOM-SG Pilot Health Alert" > /tmp/atom-sg-alert.txt
        echo "" >> /tmp/atom-sg-alert.txt
        echo "Service: $SERVICE_NAME" >> /tmp/atom-sg-alert.txt
        echo "Time: $(date)" >> /tmp/atom-sg-alert.txt
        echo "Health URL: $HEALTH_URL" >> /tmp/atom-sg-alert.txt
        echo "Message: $message" >> /tmp/atom-sg-alert.txt
        echo "" >> /tmp/atom-sg-alert.txt
        echo "Last 10 log entries:" >> /tmp/atom-sg-alert.txt
        tail -10 "$LOG_FILE" >> /tmp/atom-sg-alert.txt
        
        mail -s "ATOM-SG Pilot Health Alert" "$ALERT_EMAIL" < /tmp/atom-sg-alert.txt 2>/dev/null || \
            log "WARN" "Failed to send email alert (mail command not available)"
        
        rm -f /tmp/atom-sg-alert.txt
    fi
    
    # TODO: Add other alert methods (Slack, Telegram, etc.) here
    log "INFO" "Consider configuring additional alert methods (Slack, Telegram, etc.)"
}

# Main execution
main() {
    log "INFO" "=========================================="
    log "INFO" "ATOM-SG Pilot MVP - Health Check"
    log "INFO" "=========================================="
    log "INFO" "Health URL: $HEALTH_URL"
    log "INFO" "Timeout: ${TIMEOUT}s"
    log "INFO" "Max retries: $MAX_RETRIES"
    log "INFO" "Log file: $LOG_FILE"
    
    # Check health
    if check_health; then
        log "INFO" "✅ Service is healthy"
        exit 0
    else
        # Health check failed
        local exit_code=$?
        
        if [ $exit_code -eq 1 ]; then
            log "WARN" "⚠️ Service is unhealthy but responding"
            send_alert "Service is unhealthy but responding. Status may be degraded."
        else
            log "ERROR" "❌ Service is DOWN or not responding"
            
            # Attempt to restart
            if restart_service; then
                log "INFO" "✅ Service restarted successfully"
                send_alert "Service was DOWN but has been successfully restarted."
            else
                log "ERROR" "❌ Failed to restart service"
                send_alert "Service is DOWN and restart attempts failed. Manual intervention required."
            fi
        fi
        
        exit $exit_code
    fi
}

# Run main function
main "$@"