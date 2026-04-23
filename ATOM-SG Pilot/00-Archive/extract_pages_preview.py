#!/usr/bin/env python3
"""
Extract page images from PDF to inspect questions with diagrams.
"""
import fitz
import os

pdf_path = "00-Original-Exam-Papers/2025-P6-Maths-Prelim Exam-ACS Junior.pdf"
output_dir = "tmp/acs_preview"

os.makedirs(output_dir, exist_ok=True)

# Open PDF
doc = fitz.open(pdf_path)

# Extract pages 11-30 (Paper 2 questions)
for page_num in range(10, 30):  # 0-indexed, so 10 = page 11
    page = doc[page_num]

    # Render page to image
    pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))  # 1.5x zoom

    # Save as PNG
    output_path = os.path.join(output_dir, f"page_{page_num+1}.png")
    pix.save(output_path)

    print(f"Saved: {output_path}")

doc.close()

print(f"\nExtracted pages 11-30 to {output_dir}")
