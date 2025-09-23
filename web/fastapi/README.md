# FastAPI Service

This workspace hosts the FastAPI backend that powers the Watt Next demo.

## Requirements

- Python 3.11+
- FastAPI available in your environment (`pip install -r requirements.txt`)

## Running Locally

1. (Optional) Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install the service dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the service through Watt:

   ```bash
   npm start
   ```

The ASGI application lives in `public/main.py` and is loaded through the `@platformatic/python` stackable.
