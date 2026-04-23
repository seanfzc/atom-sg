#!/usr/bin/env python3
"""
Quick test to verify backend serves frontend correctly.
"""
import requests
import time
import subprocess
import sys
import os

def test_frontend_serving():
    # Start backend in subprocess
    print("Starting backend on port 5002...")
    proc = subprocess.Popen(
        ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5002"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )
    
    # Wait for startup
    time.sleep(3)
    
    try:
        # Test root endpoint (should return HTML)
        print("Testing root endpoint...")
        resp = requests.get("http://localhost:5002/", timeout=5)
        print(f"Status: {resp.status_code}")
        print(f"Content-Type: {resp.headers.get('content-type')}")
        if "text/html" in resp.headers.get('content-type', ''):
            print("✓ Root serves HTML")
        else:
            print("✗ Root does not serve HTML")
            print(f"Response: {resp.text[:200]}")
        
        # Test API endpoint
        print("\nTesting API health endpoint...")
        resp = requests.get("http://localhost:5002/api/v1/system/health", timeout=5)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            print("✓ API health endpoint works")
        else:
            print("✗ API health endpoint failed")
        
        # Test static file serving
        print("\nTesting static file serving...")
        resp = requests.get("http://localhost:5002/static/css/style.css", timeout=5)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            print("✓ Static CSS file served")
        else:
            print("✗ Static CSS file not found")
        
        # Test catch-all route for SPA
        print("\nTesting SPA catch-all route...")
        resp = requests.get("http://localhost:5002/practice", timeout=5)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200 and "text/html" in resp.headers.get('content-type', ''):
            print("✓ SPA route serves HTML")
        else:
            print("✗ SPA route failed")
            
    except Exception as e:
        print(f"Error during testing: {e}")
    finally:
        # Kill backend
        print("\nStopping backend...")
        proc.terminate()
        proc.wait(timeout=5)
    
    print("\nTest completed.")

if __name__ == "__main__":
    test_frontend_serving()