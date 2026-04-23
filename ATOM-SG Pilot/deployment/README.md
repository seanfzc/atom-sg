# ATOM‑SG Pilot MVP - Deployment Guide

This directory contains deployment artifacts for the ATOM‑SG Pilot MVP.

## Overview

The ATOM‑SG Pilot MVP is a recognition‑first integrated training system for P6 mathematics. It consists of:

- **Backend:** FastAPI Python application (port 5000)
- **Frontend:** HTML5/JavaScript single‑page application
- **OCR Pipeline:** Tesseract 5.5.2 for handwritten answer extraction
- **Rendering Pipeline:** Matplotlib/TikZ for diagram generation

## Quick Start

### Option 1: Docker (Recommended)

```bash
# Build and run with Docker Compose
cd deployment
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop the service
docker-compose down
```

The application will be available at: http://localhost:5000

### Option 2: Local Installation

```bash
# Run the installation script
chmod +x install.sh
./install.sh

# Follow the prompts to install dependencies
# Then start the application:
cd ../05-Backend
./start.sh
```

## Deployment Options

### 1. Development / Testing
- Use Docker Compose with mounted volumes for hot‑reload
- Enable DEBUG mode for detailed error messages

### 2. Production (Single Server)
- Use Docker Compose with restart policy `unless-stopped`
- Configure reverse proxy (nginx, Apache, Caddy) for SSL termination
- Set up monitoring and log rotation

### 3. Cloud Deployment (AWS/Azure/GCP)
- Build Docker image and push to container registry
- Deploy as container service (ECS, ACI, Cloud Run)
- Configure persistent storage for artifacts

## Configuration

### Environment Variables

Copy `.env.example` to `.env` (for Docker) or `05‑Backend/.env` (for local):

```bash
# Docker
cp .env.example .env

# Local
cp .env.example ../05-Backend/.env
```

Key variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 5000 | Application port |
| `HOST` | 0.0.0.0 | Bind address |
| `DEBUG` | false | Enable debug mode |
| `TESSERACT_LANG` | eng | OCR language |
| `RENDER_FORMAT` | svg | Diagram output format |

### System Dependencies

The application requires:

- **Python 3.9+** with virtual environment
- **Tesseract OCR** 5.5.2+ with English language data
- **System libraries:** GLib, X11, Mesa (for Matplotlib)
- **Optional:** LaTeX (for TikZ rendering)

The installation script (`install.sh`) automatically installs these for:
- macOS (Homebrew)
- Debian/Ubuntu (apt)
- RHEL/CentOS/Fedora (yum)
- Arch Linux (pacman)

## Docker Details

### Image Structure

- **Base:** Python 3.9‑slim
- **System packages:** Tesseract OCR, graphics libraries
- **Python packages:** FastAPI, Uvicorn, Matplotlib, Pillow, PyTesseract
- **Volumes:** Persistent storage for artifacts (`/home/appuser/app/artifacts`)
- **Health check:** `/api/v1/system/health` endpoint

### Building Custom Image

```bash
# Build from source
docker build -t atom-sg-pilot:latest -f deployment/Dockerfile .

# Run container
docker run -p 5000:5000 -v atom-sg-artifacts:/app/artifacts atom-sg-pilot:latest
```

## Monitoring & Maintenance

### Health Checks

```bash
# Docker health status
docker-compose ps

# API health endpoint
curl http://localhost:5000/api/v1/system/health

# System statistics
curl http://localhost:5000/api/v1/system/stats
```

### Logs

```bash
# Docker logs
docker-compose logs -f

# Application logs (if using systemd)
journalctl -u atom-sg-pilot -f
```

### Backup

Critical data to back up:
- `artifacts/sessions/` – Student practice sessions
- `artifacts/renders/` – Generated diagrams
- `artifacts/ocr/` – OCR processing results

### Automation Scripts
The deployment includes several automation scripts in the `deployment/` directory:

| Script | Purpose | Usage |
|--------|---------|-------|
| `health_check.sh` | Monitor backend health, auto-restart, alerts | `./health_check.sh` |
| `setup_firewall.sh` | Configure UFW firewall for production | `sudo ./setup_firewall.sh` |
| `backup.sh` | Create compressed backups with retention | `./backup.sh` |
| `restore_backup.sh` | Restore from backup archive | `./restore_backup.sh latest` |
| `install.sh` | System-aware dependency installer | `./install.sh` |

**Quick Setup:**
```bash
# Install dependencies
./install.sh

# Setup firewall (as root)
sudo ./setup_firewall.sh

# Test deployment
cd ../05-Backend && ./test_deployment.sh

# Start services
cd ../05-Backend && ./start.sh  # or docker-compose up -d

# Configure monitoring (add to crontab)
(crontab -l 2>/dev/null; echo "*/5 * * * * cd $(pwd) && ./health_check.sh") | crontab -
(crontab -l 2>/dev/null; echo "0 2 * * * cd $(pwd) && ./backup.sh") | crontab -
```

## Troubleshooting

### Common Issues

1. **Port 5000 already in use**
   ```bash
   # Change PORT in .env or use a different port
   PORT=5001 ./start.sh
   ```

2. **Tesseract not found**
   ```bash
   # Install manually
   sudo apt-get install tesseract-ocr tesseract-ocr-eng  # Ubuntu/Debian
   brew install tesseract  # macOS
   ```

3. **Matplotlib display errors**
   - Ensure `libgl1-mesa-glx` and related libraries are installed
   - For headless servers, set `MPLBACKEND=Agg` in environment

4. **Docker container fails to start**
   ```bash
   # Check logs
   docker-compose logs atom-sg-backend
   
   # Rebuild with clean cache
   docker-compose build --no-cache
   ```

### Performance Tuning

- **OCR processing:** 3‑5 seconds per page (handwriting)
- **Diagram rendering:** 1‑2 seconds per diagram
- **API response:** < 100ms for most endpoints
- **Memory:** ~200MB for Python process + Tesseract

## Security Considerations

1. **Run as non‑root user** (Docker container already uses `appuser`)
2. **Enable firewall** to restrict access to port 5000
3. **Use HTTPS** in production (configure reverse proxy)
4. **Rotate secrets** regularly if using session signing
5. **Limit file uploads** (OCR scans) to prevent abuse

## Scaling

For pilot deployment (10‑50 students), a single server is sufficient. For larger deployments:

1. **Add database:** Replace in‑memory storage with PostgreSQL
2. **Load balancing:** Multiple backend instances behind nginx
3. **Caching:** Redis for frequently accessed data
4. **Queue processing:** Celery for async OCR and rendering tasks

## Support

- **Documentation:** See `../docs/` for API specification
- **Issues:** Check `../01‑Projects/SubAgentComms.md` for known issues
- **Testing:** Run `../05‑Backend/final_verification.sh` to verify installation

---

**Pilot Launch Timeline:** Week 2 (2026‑04‑26)
**Last Updated:** 2026‑04‑15