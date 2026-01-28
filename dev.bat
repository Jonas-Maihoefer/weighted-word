@echo off
echo === Starting Hybrid Dev Environment ===

:: 1. Start Database
echo [1/5] Spinning up Postgres container...
docker compose up db -d --wait

:: 2. Enter backend folder
cd backend

:: 3. Check/Create Venv
if not exist venv (
    echo [2/5] Creating virtual environment...
    python -m venv venv
)

:: 4. Activate Venv and Install Deps
echo [3/5] Syncing dependencies...
call venv\Scripts\activate
pip install -e .

:: 5. Set Local Vars
set POSTGRES_SERVER=localhost
set POSTGRES_PORT=5432
set APP_ENV=local

:: 6. Run Migrations
echo [4/5] Running Database Migrations...
alembic upgrade head

:: 7. Start Server
echo [5/5] Starting Uvicorn...
uvicorn app.main:app --reload