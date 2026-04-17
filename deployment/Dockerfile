# ATOM-SG Pilot MVP - Docker Container
# Multi-stage build for optimized production image

# Stage 1: Builder (install dependencies)
FROM python:3.9-slim AS builder

# Install system dependencies for OCR, rendering, and Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-eng \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libpng-dev \
    libfreetype6-dev \
    pkg-config \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Optional: LaTeX for TikZ rendering (comment out if not needed)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     texlive-latex-base \
#     texlive-latex-extra \
#     texlive-fonts-recommended \
#     && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install Python dependencies
COPY 05-Backend/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Stage 2: Runtime (minimal image)
FROM python:3.9-slim

# Install runtime system dependencies (OCR only)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-eng \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Optional: LaTeX runtime (uncomment if Stage 1 LaTeX installed)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     texlive-latex-base \
#     texlive-fonts-recommended \
#     && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser
USER appuser
WORKDIR /home/appuser

# Copy application code
COPY --chown=appuser:appuser 05-Backend ./app

WORKDIR /home/appuser/app

# Create necessary directories
RUN mkdir -p artifacts/renders artifacts/ocr artifacts/sessions artifacts/collision artifacts/interpretation

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=5000
ENV HOST=0.0.0.0
ENV DEBUG=false

# Expose the application port
EXPOSE ${PORT}

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/api/v1/system/health || exit 1

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--log-level", "info"]