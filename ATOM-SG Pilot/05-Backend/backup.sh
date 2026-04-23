#!/bin/bash

# ATOM-SG MVP Backup Script
# Creates daily backups of artifacts and logs, keeps last 30 days

set -e

BACKUP_DIR="/home/ubuntu/backups"
MAX_BACKUPS=30
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="atom-sg-backup-$DATE.tar.gz"
APP_DIR="/home/ubuntu/05-Backend"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}ATOM-SG MVP Backup Script${NC}"
echo -e "${GREEN}Date: $(date)${NC}"
echo -e "${GREEN}========================================${NC}"

# Create backup directory if it doesn't exist
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Creating backup directory: $BACKUP_DIR"
    mkdir -p "$BACKUP_DIR"
fi

# Check if app directory exists
if [ ! -d "$APP_DIR" ]; then
    echo -e "${RED}ERROR: App directory not found: $APP_DIR${NC}"
    exit 1
fi

# Check disk space
DISK_SPACE=$(df -h "$BACKUP_DIR" | tail -1 | awk '{print $4}')
echo "Available disk space: $DISK_SPACE"

# Backup artifacts
echo "Backing up artifacts directory..."
if [ -d "$APP_DIR/artifacts" ]; then
    ARTIFACTS_SIZE=$(du -sh "$APP_DIR/artifacts" | cut -f1)
    echo "Artifacts size: $ARTIFACTS_SIZE"
else
    echo -e "${YELLOW}WARNING: artifacts directory not found${NC}"
fi

# Backup logs
echo "Backing up logs directory..."
if [ -d "$APP_DIR/logs" ]; then
    LOGS_SIZE=$(du -sh "$APP_DIR/logs" | cut -f1)
    echo "Logs size: $LOGS_SIZE"
else
    echo -e "${YELLOW}WARNING: logs directory not found${NC}"
fi

# Create backup
echo "Creating backup archive: $BACKUP_NAME"
cd "$APP_DIR"

# Files to backup
BACKUP_FILES=""

if [ -d "artifacts" ]; then
    BACKUP_FILES="$BACKUP_FILES artifacts"
fi

if [ -d "logs" ]; then
    BACKUP_FILES="$BACKUP_FILES logs"
fi

if [ -f ".env" ]; then
    BACKUP_FILES="$BACKUP_FILES .env"
fi

if [ -f "docker-compose.yml" ]; then
    BACKUP_FILES="$BACKUP_FILES docker-compose.yml"
fi

if [ -f "nginx.conf" ]; then
    BACKUP_FILES="$BACKUP_FILES nginx.conf"
fi

if [ -n "$BACKUP_FILES" ]; then
    tar -czf "$BACKUP_DIR/$BACKUP_NAME" $BACKUP_FILES 2>/dev/null || {
        echo -e "${RED}ERROR: Failed to create backup archive${NC}"
        exit 1
    }
    
    BACKUP_SIZE=$(du -h "$BACKUP_DIR/$BACKUP_NAME" | cut -f1)
    echo -e "${GREEN}✓ Backup created: $BACKUP_NAME ($BACKUP_SIZE)${NC}"
else
    echo -e "${YELLOW}WARNING: No files to backup${NC}"
fi

# Clean up old backups
echo "Cleaning up old backups (keeping last $MAX_BACKUPS)..."
cd "$BACKUP_DIR"
BACKUP_COUNT=$(ls -1 atom-sg-backup-*.tar.gz 2>/dev/null | wc -l)

if [ $BACKUP_COUNT -gt $MAX_BACKUPS ]; then
    BACKUPS_TO_REMOVE=$((BACKUP_COUNT - MAX_BACKUPS))
    echo "Removing $BACKUPS_TO_REMOVE old backup(s)"
    
    ls -1tr atom-sg-backup-*.tar.gz | head -$BACKUPS_TO_REMOVE | while read OLD_BACKUP; do
        echo "Removing: $OLD_BACKUP"
        rm -f "$OLD_BACKUP"
    done
fi

# Show backup summary
echo ""
echo -e "${GREEN}Backup Summary:${NC}"
echo "----------------"
echo "Backup location: $BACKUP_DIR"
echo "Current backups: $(ls -1 atom-sg-backup-*.tar.gz 2>/dev/null | wc -l)"
echo "Latest backup: $BACKUP_NAME ($BACKUP_SIZE)"
echo "Next cleanup: After $MAX_BACKUPS backups"

# Create restore script if it doesn't exist
RESTORE_SCRIPT="$BACKUP_DIR/restore_backup.sh"
if [ ! -f "$RESTORE_SCRIPT" ]; then
    cat > "$RESTORE_SCRIPT" << 'EOF'
#!/bin/bash

# ATOM-SG MVP Restore Script
# Restores a backup created by backup.sh

set -e

BACKUP_DIR="/home/ubuntu/backups"
APP_DIR="/home/ubuntu/05-Backend"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}ATOM-SG MVP Restore Script${NC}"
echo -e "${GREEN}========================================${NC}"

# Check if backup directory exists
if [ ! -d "$BACKUP_DIR" ]; then
    echo -e "${RED}ERROR: Backup directory not found: $BACKUP_DIR${NC}"
    exit 1
fi

# List available backups
echo "Available backups:"
echo "----------------"
ls -1tr atom-sg-backup-*.tar.gz 2>/dev/null || {
    echo -e "${YELLOW}No backups found${NC}"
    exit 1
}

# Prompt for backup selection
echo ""
read -p "Enter backup filename to restore (or press Enter for latest): " BACKUP_CHOICE

if [ -z "$BACKUP_CHOICE" ]; then
    BACKUP_CHOICE=$(ls -1tr atom-sg-backup-*.tar.gz 2>/dev/null | tail -1)
    echo "Selected latest backup: $BACKUP_CHOICE"
fi

BACKUP_PATH="$BACKUP_DIR/$BACKUP_CHOICE"

# Check if backup exists
if [ ! -f "$BACKUP_PATH" ]; then
    echo -e "${RED}ERROR: Backup not found: $BACKUP_CHOICE${NC}"
    exit 1
fi

# Confirm restore
echo ""
echo -e "${YELLOW}WARNING: This will overwrite existing files in:${NC}"
echo -e "${YELLOW}  $APP_DIR${NC}"
echo ""
read -p "Are you sure you want to restore? (y/N): " CONFIRM

if [ "$CONFIRM" != "y" ] && [ "$CONFIRM" != "Y" ]; then
    echo "Restore cancelled"
    exit 0
fi

# Stop services if running
echo "Stopping services..."
if command -v docker-compose &> /dev/null; then
    cd "$APP_DIR" && docker-compose down 2>/dev/null || true
elif command -v docker &> /dev/null; then
    docker stop atom-sg-backend atom-sg-nginx 2>/dev/null || true
fi

# Restore backup
echo "Restoring backup..."
cd "$APP_DIR" && tar -xzf "$BACKUP_PATH" --overwrite

echo -e "${GREEN}✓ Backup restored successfully${NC}"

# Restart services
echo "Restarting services..."
if command -v docker-compose &> /dev/null; then
    cd "$APP_DIR" && docker-compose up -d 2>/dev/null || {
        echo -e "${YELLOW}WARNING: Failed to restart with docker-compose${NC}"
    }
elif command -v docker &> /dev/null; then
    echo -e "${YELLOW}Please restart services manually${NC}"
fi

echo ""
echo -e "${GREEN}Restore complete!${NC}"
echo "Files restored from: $BACKUP_CHOICE"
echo "Services should be restarting..."
EOF

    chmod +x "$RESTORE_SCRIPT"
    echo -e "${GREEN}✓ Restore script created: $RESTORE_SCRIPT${NC}"
fi

echo ""
echo -e "${GREEN}Backup completed successfully!${NC}"
echo "To restore, run: $RESTORE_SCRIPT"