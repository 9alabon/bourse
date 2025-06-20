# Backend API (Python/Flask)

This is the backend API for the Casablanca Investor Hub.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- PostgreSQL (or other configured database)

## Running the Backend

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure your database is running and configured in `app.py` (or a `config.py` file).
5. Start the Flask development server:
   ```bash
   python app.py
   ```

The API will typically be available at `http://localhost:5000`.
