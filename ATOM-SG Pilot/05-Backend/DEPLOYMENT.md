# ATOM-SG MVP Backend Deployment Guide

## Current Deployment Status (2026-04-17)

**Deployed Environment:** `atom‑forge` VM (Ubuntu 22.04 LTS ARM64, 2 vCPUs/4 GB RAM/10 GB disk)  
**URL:** `http://192.168.2.6/`  
**Status:** ✅ **Production‑ready** with all P0/P1 fixes, monitoring, backup, and security.

### Infrastructure Implemented
1. **Firewall (UFW):** Ports 80 (HTTP) and 22 (SSH) only; active
2. **Health Monitoring:** Cron job hourly at minute 0 (`health_check.sh`)
3. **Backup System:** Daily at 2 AM, keeps last 30 backups (`backup.sh`)
4. **Restore Script:** Interactive restore from backup (`restore_backup.sh`)
5. **All P0/P1 fixes:** Verified functional (articulation validation, step‑by‑step scaffolding, etc.)

### Script Locations (root directory)
- `backup.sh` – Creates compressed backups of artifacts, logs, config
- `health_check.sh` – Monitors service health, logs failures
- `restore_backup.sh` – Interactive restore procedure
- `test_deployment.sh` – Validates deployment

### Next Steps
- Manual browser testing using `MVP_FRONTEND_FUNCTIONAL_TEST_PLAN.md`
- Stakeholder review (Week 2 pilot launch: 2026‑04‑26)

---

## Deployment Options

### Option 1: Docker (Recommended for Production)

**Prerequisites:**
- Docker Engine 20.10+
- Docker Compose 2.0+ (optional but recommended)

**Steps:**
1. Clone the repository or copy the backend files
2. Navigate to the backend directory: `cd /path/to/ATOM-SG-Pilot/05-Backend`
3. Build the Docker image: `docker build -t atom-sg-backend .`
4. Run the container: `docker run -d -p 5000:5000 -v $(pwd)/artifacts:/app/artifacts -v $(pwd)/logs:/app/logs --name atom-sg-backend atom-sg-backend`

**Using Docker Compose:**
1. `docker-compose up -d` (starts in background)
2. `docker-compose logs -f` (view logs)
3. `docker-compose down` (stop)

**Health Check:**
- The container includes a health check that verifies the API is responding
- Check status: `docker ps` (look for "healthy" status)

### Option 2: System Installation (Linux/macOS)

**Prerequisites:**
- Python 3.11 or higher
- Tesseract OCR 5.5.2 or higher
- System packages: poppler-utils, GL libraries

**Automated Installation:**
1. Make the install script executable: `chmod +x install.sh`
2. Run the installer: `./install.sh`
3. Follow the prompts and review the .env file

**Manual Installation Steps:**
1. Install system packages (see install.sh for OS-specific commands)
2. Create Python virtual environment: `python3.11 -m venv venv`
3. Activate virtual environment: `source venv/bin/activate`
4. Install Python dependencies: `pip install -r requirements.txt`
5. Create artifacts directories: `mkdir -p artifacts/{renders,ocr,sessions,collision,interpretation}`
6. Create logs directory: `mkdir -p logs`
7. Copy .env.example to .env and adjust settings: `cp .env.example .env`
8. Start the backend: `uvicorn main:app --host 0.0.0.0 --port 5000`

### Option 3: Systemd Service (Linux Production)

**Steps:**
1. Run the installer: `./install.sh` (creates systemd service file)
2. Enable and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable atom-sg-backend
   sudo systemctl start atom-sg-backend
   ```
3. Check service status: `sudo systemctl status atom-sg-backend`
4. View logs: `sudo journalctl -u atom-sg-backend -f`

## Configuration

### Environment Variables

Create a `.env` file with the following variables (see `.env.example` for defaults):

```bash
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
```

### Directory Structure

```
artifacts/
├── renders/           # Generated diagrams (SVG/PNG)
├── ocr/               # Original scans + OCR results
├── sessions/          # Practice session data
├── collision/         # Collision detection analyses
└── interpretation/    # Data interpretation analyses

logs/
├── backend.log       # Application logs
├── systemd.log      # Systemd service logs (if using systemd)
└── health_check.log # Health check logs

frontend/             # Frontend static files (HTML, CSS, JS)
```

## Health Monitoring

### Built-in Health Check
- Endpoint: `GET /api/v1/system/health`
- Returns 200 OK if system is healthy
- Checks: Tesseract availability, artifact directories, memory usage

### Manual Health Check
Run the health check script: `./health_check.sh`
- Returns "OK" if system is healthy
- Returns "FAIL" and non-zero exit code if unhealthy

### Automated Monitoring
Add to cron (check every 5 minutes):
```bash
*/5 * * * * cd /path/to/backend && ./health_check.sh
```

## Backup & Recovery

### Automated Backups
Run the backup script daily:
```bash
0 2 * * * cd /path/to/backend && ./backup.sh
```

This creates compressed backups in `./backups/` and keeps the last 30 backups.

### Manual Backup
```bash
./backup.sh
```

### Restore from Backup
```bash
./restore_backup.sh backups/backup_20250101_020000.tar.gz
```

## Security Considerations

### Firewall Configuration
- Allow port 5000 (or your configured port) for backend access
- If using reverse proxy, allow ports 80/443 instead

### Reverse Proxy (Recommended for Production)
Use Nginx or Caddy as a reverse proxy for:
- HTTPS/SSL termination
- Rate limiting
- Load balancing (if scaling)
- CORS handling

Example Nginx configuration (`/etc/nginx/sites-available/atom-sg`):
```nginx
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Environment-Based Secrets
- Store sensitive data in `.env` file (not in version control)
- Use different `.env` files for development/production
- Set file permissions: `chmod 600 .env`

## Performance Tuning

### System Requirements
- **Minimum:** 1 CPU core, 2GB RAM, 5GB disk space
- **Recommended:** 2 CPU cores, 4GB RAM, 10GB disk space
- **Storage:** SSD recommended for faster OCR processing

### Optimization Tips
1. **Enable caching:** Use Redis or memcached for frequent queries
2. **Increase workers:** For production, use multiple uvicorn workers:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5000 --workers 4
   ```
3. **Monitor resources:** Use `top`, `htop`, or monitoring tools
4. **Clean up old artifacts:** Implement retention policy (e.g., delete renders older than 30 days)

## Infrastructure Automation

The deployment includes several automation scripts for production readiness:

### Health Monitoring (`deployment/health_check.sh`)
- Checks backend health endpoint
- Attempts automatic restart if service is down
- Sends alerts (email) if configured
- Logs results to `/var/log/atom-sg-health.log`

**Setup:**
```bash
# Make executable
chmod +x deployment/health_check.sh

# Test manually
./deployment/health_check.sh

# Add to cron (every 5 minutes)
*/5 * * * * cd /path/to/ATOM-SG-Pilot && ./deployment/health_check.sh
```

### Firewall Configuration (`deployment/setup_firewall.sh`)
- Configures UFW firewall for production
- Allows SSH (port 22), HTTP (80), HTTPS (443), backend (5000)
- Sets default deny incoming policy

**Setup:**
```bash
# Make executable
chmod +x deployment/setup_firewall.sh

# Run as root
sudo ./deployment/setup_firewall.sh

# Customize ports (optional)
SSH_PORT=2222 HTTP_PORT=8080 sudo ./deployment/setup_firewall.sh
```

### Backup System (`deployment/backup.sh`)
- Creates compressed backups of artifacts, config, database, logs
- Implements retention policy (keeps last 30 backups)
- Suitable for cron automation

**Setup:**
```bash
# Make executable
chmod +x deployment/backup.sh

# Test backup
./deployment/backup.sh

# Add to cron (daily at 2 AM)
0 2 * * * cd /path/to/ATOM-SG-Pilot && ./deployment/backup.sh
```

### Restore Backup (`deployment/restore_backup.sh`)
- Restores from backup archive
- Interactive confirmation for safety
- Preserves existing files with backups

**Usage:**
```bash
# Make executable
chmod +x deployment/restore_backup.sh

# Restore specific backup
./deployment/restore_backup.sh backups/atom-sg-backup-20250101_020000.tar.gz

# Restore latest backup
./deployment/restore_backup.sh latest
```

### Deployment Testing (`test_deployment.sh`)
- Validates Python, Tesseract, dependencies
- Tests API endpoints
- Verifies OCR and rendering pipelines

**Usage:**
```bash
# Run deployment tests
./test_deployment.sh
```

### Complete Infrastructure Setup
For a complete infrastructure setup, run:
```bash
# 1. Install dependencies
./deployment/install.sh

# 2. Setup firewall (as root)
sudo ./deployment/setup_firewall.sh

# 3. Test deployment
./test_deployment.sh

# 4. Start services
./start.sh  # or docker-compose up -d

# 5. Configure monitoring (add to crontab)
(crontab -l 2>/dev/null; echo "*/5 * * * * cd $(pwd) && ./deployment/health_check.sh") | crontab -
(crontab -l 2>/dev/null; echo "0 2 * * * cd $(pwd) && ./deployment/backup.sh") | crontab -
```

## Troubleshooting

### Common Issues

#### 1. Tesseract Not Found
**Error:** `TesseractNotFoundError: tesseract is not installed or it's not in your PATH`
**Solution:**
- Install Tesseract: `apt-get install tesseract-ocr` (Ubuntu) or `brew install tesseract` (macOS)
- Verify installation: `tesseract --version`
- Update TESSERACT_CMD in .env if installed in non-standard location

#### 2. Missing GL Libraries (Matplotlib)
**Error:** `ImportError: libGL.so.1: cannot open shared object file`
**Solution:**
- Install GL libraries: `apt-get install libgl1-mesa-glx` (Ubuntu) or equivalent for your OS

#### 3. Port Already in Use
**Error:** `[Errno 98] Address already in use`
**Solution:**
- Change PORT in .env file
- Kill existing process: `sudo lsof -ti:5000 | xargs kill -9`
- Use different port: `uvicorn main:app --port 5001`

#### 4. Permission Denied for Artifacts Directory
**Solution:**
- Ensure user has write permissions: `chmod -R 755 artifacts`
- For Docker: ensure volume mount permissions are correct

### Logs Location
- Application logs: `logs/backend.log`
- Systemd logs: `sudo journalctl -u atom-sg-backend`
- Docker logs: `docker logs atom-sg-backend`

### Debug Mode
Set `DEBUG=true` in `.env` for detailed error messages and stack traces.

## Pilot Launch Checklist

### Pre-Launch (Week Before)
- [ ] Backend deployed and tested
- [ ] Health checks passing
- [ ] Backup system configured
- [ ] Monitoring set up (logs, alerts)
- [ ] Security review completed (firewall, permissions)
- [ ] Performance test completed (load testing)
- [ ] Documentation updated (this guide, API docs)

### Day Before Launch
- [ ] Final backup taken
- [ ] System resources verified (disk space, memory)
- [ ] All services restarted and healthy
- [ ] Frontend accessible at target URL
- [ ] Communication sent to stakeholders

### Launch Day
- [ ] Morning health check completed
- [ ] Monitor logs for errors
- [ ] Verify first user can access system
- [ ] Performance monitoring active
- [ ] Support team briefed and ready

### Post-Launch (First Week)
- [ ] Daily health checks
- [ ] Backup verification
- [ ] Performance monitoring
- [ ] User feedback collection
- [ ] Bug triage and prioritization

## Support & Maintenance

### Regular Maintenance Tasks
1. **Daily:** Check health status and logs
2. **Weekly:** Verify backups and disk space
3. **Monthly:** Update dependencies (security patches)
4. **Quarterly:** Review security configuration

### Contact Information
- **Technical Support:** [Your contact information]
- **Emergency Contact:** [24/7 contact if available]
- **Documentation:** [Link to full documentation]

### Escalation Procedures
1. **Level 1:** Application restart (`systemctl restart atom-sg-backend`)
2. **Level 2:** Server restart and diagnostics
3. **Level 3:** Developer engagement for bug fixes

## Appendix

### API Endpoints Summary
See `API.md` for complete API documentation.

### Frontend Integration
The frontend is a static HTML5 application located in `frontend/` directory.
- Main entry point: `frontend/index.html`
- Static assets: `frontend/static/`
- No build process required - works directly in browser

### Testing
Run verification script: `./verify_mvp.sh`
- Tests all API endpoints
- Verifies OCR pipeline
- Validates rendering functionality

### Development
For development, use:
```bash
source venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

---

*Last Updated: 2026-04-16*  
*Version: 1.0.0*