# azure-aws-ai-knowledge-assistant
Multi-cloud AI Knowledge Assistant built with Python, FastAPI, React, Microsoft Azure and AWS. A portfolio project focused on RAG, cloud architecture, DevOps and Infrastructure as Code.

## Current milestone: M1 – Backend Foundation

The backend currently runs locally and exposes a health endpoint. There is no
frontend, database, AI integration, or cloud service in this milestone.

## Run the backend (Windows PowerShell)

Prerequisite: Python 3.12. Run these commands from the repository root:

```powershell
cd backend
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

These commands use the virtual environment's Python directly, so activation and
PowerShell execution-policy changes are unnecessary. The environment keeps this
project's dependencies separate from other Python projects.

Open http://127.0.0.1:8000/health or, in another PowerShell window, run:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/health
```

Expected JSON response:

```json
{
  "status": "healthy",
  "application": "AI Knowledge Assistant",
  "version": "0.1.0"
}
```

Interactive API documentation is at http://127.0.0.1:8000/docs.
Stop the development server with `Ctrl+C`. `--reload` restarts it when source
files change and is intended for local development.

## Run tests

From the repository root, after installing the backend dependencies:

```powershell
cd backend
.\.venv\Scripts\python.exe -m pytest -q
```

If your terminal is already in `backend`, omit `cd backend`.

## Backend structure and decisions

- `backend/app/__init__.py` marks the application directory as a Python package.
- `backend/app/main.py` creates the FastAPI application and defines `GET /health`.
  Application title and version are shared with the endpoint response.
- `backend/tests/test_health.py` uses FastAPI's HTTP test client to check the
  response status and exact JSON body without starting a network server.
- `backend/requirements.txt` lists FastAPI, Uvicorn (the ASGI server), pytest,
  and HTTPX (required by the test client).

The health endpoint has no business logic or external dependencies, so it remains
in the entry point. Future features should separate routes from business logic.
No environment configuration is needed yet; future configurable values should
come from environment variables. Virtual environments, Python caches, `.env`
variants, and files named `*.local` or `*.local.*` are ignored by Git;
`.env.example` may be tracked as a template without secrets.

The health check only confirms that the application can answer a request; it does
not check storage or other services. Dependency ranges constrain major versions
but are not a lockfile, so installs may resolve different compatible versions.

The next logical milestone is validated local PDF/TXT upload and processing,
with routes and processing logic in separate modules and automated tests.
