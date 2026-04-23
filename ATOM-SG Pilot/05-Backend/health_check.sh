#!/bin/bash

# ATOM-SG MVP Health Check Script
# Runs via cron to monitor service health

set -e

LOG_FILE="/home/ubuntu/05-Backend/logs/health-check.log"
HEALTH_URL="http://localhost/api/v1/system/health"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Create logs directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

# Function to log messages
log() {
    echo "[$TIMESTAMP] $1" >> "$LOG_FILE"
}

# Check health endpoint
response=$(curl -s -f -o /dev/null -w "%{http_code}" "$HEALTH_URL" 2>/dev/null || echo "CURL_ERROR")

if [ "$response" = "200" ]; then
    log "HEALTHY: Service responding (HTTP 200)"
    exit 0
elif [ "$response" = "CURL_ERROR" ]; then
    log "ERROR: Cannot connect to service (curl failed)"
    exit 1
else
    log "ERROR: Service returned HTTP $response"
    exit 1
fi