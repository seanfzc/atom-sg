# Multi-stage Docker build for ATOM-SG MVP Backend
# Stage 1: Builder - install compile-time dependencies and build Python packages
FROM python:3.11-slim AS builder

# Install system dependencies for building Python packages and Tesseract
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    curl \
    git \
    # Tesseract dependencies
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    # PDF processing dependencies
    libfreetype6-dev \
    libjpeg-dev \
    libpng-dev \
    # Optional: LaTeX for TikZ rendering (comment out if not needed)
    # texlive-latex-base \
    # texlive-latex-extra \
    # texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime - minimal image with only runtime dependencies
FROM python:3.11-slim

# Install runtime system dependencies (Tesseract, GL libraries for matplotlib)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1 \
    libglvnd0 \
    libglib2.0-0 \
    # Fonts for matplotlib
    fonts-dejavu \
    # PDF tools
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -u 1000 appuser && mkdir -p /app && chown -R appuser:appuser /app
USER appuser

WORKDIR /app

# Copy Python packages from builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

# Copy application code
COPY --chown=appuser:appuser . .

# Create directories for artifacts
RUN mkdir -p artifacts/renders artifacts/ocr artifacts/sessions artifacts/collision artifacts/interpretation

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/api/v1/system/health || exit 1

# Expose port
EXPOSE 5000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]