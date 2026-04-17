# ATOM-SG Pilot MVP Backend

FastAPI backend implementation for the ATOM-SG Pilot v4.1 Recognition-First Integrated Training system.

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure Tesseract OCR is installed:
- macOS: `brew install tesseract`
- Ubuntu: `sudo apt-get install tesseract-ocr`
- Windows: Download installer from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

3. Ensure LaTeX is installed for TikZ rendering (optional):
- macOS: `brew install mactex`
- Ubuntu: `sudo apt-get install texlive-full`

## Running the Server

Start the FastAPI server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

The API will be available at `http://localhost:5000`

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:5000/docs`
- ReDoc: `http://localhost:5000/redoc`

## Directory Structure

```
ATOM-SG Pilot/05-Backend/
├── main.py                    # FastAPI application
├── requirements.txt           # Python dependencies
├── scripts/                   # Utility scripts
│   └── ocr_pipeline.py       # OCR processing script
└── artifacts/                 # File storage
    ├── renders/              # TikZ/Matplotlib outputs
    ├── ocr/                  # Scan files + OCR results
    ├── sessions/             # Practice session data
    ├── collision/            # Collision detection analyses
    └── interpretation/       # Data interpretation analyses
```

## API Endpoints

### Core Endpoints (Week 2)
- `GET /api/v1/problems` - List problems
- `GET /api/v1/problems/{id}` - Get problem details
- `GET /api/v1/problems/pdf` - Generate baseline/transfer PDF
- `POST /api/v1/practice-sessions` - Start practice session
- `GET /api/v1/practice-sessions/{id}` - Get current problem
- `POST /api/v1/practice-sessions/{id}/submit` - Submit answer
- `POST /api/v1/practice` - Individual practice submission
- `GET /api/v1/pathway-radar/questions` - Get warm-up questions
- `POST /api/v1/pathway-radar/submit` - Submit warm-up answers
- `GET /api/v1/milestones` - Get progress
- `PATCH /api/v1/milestones/{id}` - Update progress
- `POST /api/v1/reflections` - Submit reflection
- `GET /api/v1/reflections` - View reflections

### Extended Endpoints (Week 3+)
- `POST /api/v1/collision` - Cross-thread collision detection
- `GET /api/v1/interpretation` - Data interpretation analytics
- `GET /api/v1/analytics/baseline` - Baseline results
- `GET /api/v1/analytics/transfer` - Ramp-up metrics
- `GET /api/v1/analytics/progress` - Weekly progress

## Data Storage

For MVP simplicity, all data is stored in-memory. In production, replace with:
- PostgreSQL or SQLite database
- File-based storage for artifacts
- Redis caching for performance

## OCR Processing

Use the OCR pipeline script to process PDF scans:
```bash
python scripts/ocr_pipeline.py --all
```

Or process a specific file:
```bash
python scripts/ocr_pipeline.py --pdf path/to/file.pdf
```

## Development

To run with automatic reload during development:
```bash
uvicorn main:app --reload
```

## Testing

Run pytest tests:
```bash
pytest
```

## Troubleshooting

### Tesseract not found
- Ensure Tesseract is installed and in your PATH
- On macOS: `brew install tesseract`
- On Linux: `sudo apt-get install tesseract-ocr`

### TikZ rendering fails
- Ensure LaTeX is installed
- Check TikZ syntax in problem specs
- Review logs for compilation errors

### Port already in use
- Change port in `main.py` or use: `uvicorn main:app --port 8000`

## License

Proprietary - ATOM-SG Pilot Project
