# OCR Pipeline for ATOM-SG Pilot

## Purpose
Extract text from geometry problem renders (PDFs or images) using OCR (Tesseract) and store them in the artifact repository for downstream processing.

## Dependencies
- Tesseract OCR 5.x (`brew install tesseract`)
- Python packages: `pytesseract`, `Pillow`, `PyMuPDF`, `pdfplumber`

## Pipeline Scripts
- `test_tesseract.py` – quick test of Tesseract installation and basic extraction.
- `ocr_pipeline.py` – main pipeline script that extracts text from PDFs (with selectable text fallback) or images, and saves to output directory.

## Usage
```bash
# Extract text from a PDF (with OCR fallback)
python3 ocr_pipeline.py /path/to/problem.pdf --output-dir ../05-Backend/artifacts/ocr --prefix P5-Geometry-001

# Extract text from an image
python3 ocr_pipeline.py /path/to/problem.png --output-dir ../05-Backend/artifacts/ocr --prefix P5-Geometry-001
```

## Output Naming Convention
`{ProblemID}-page-{page:03d}.txt` (e.g., `P5-Geometry-001-page-001.txt`)

## Storage
OCR outputs are stored in `ATOM-SG Pilot/05-Backend/artifacts/ocr/`. Coordinate with BackendBot for API endpoints to retrieve OCR results.

## Status
- Tesseract 5.5.2 installed and tested.
- OCR pipeline script ready.
- Awaiting geometry problem pack (T1) and rendered PDFs (T4) for full pipeline test.

## Coordination
- **BackendBot:** Provide artifact repository location (C1) and API spec (C3).
- **RenderBot:** Provide rendered PDFs (T4).
- **GeoBot:** Provide geometry problem pack (T1).

