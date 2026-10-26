# Azure & AWS AI Knowledge Assistant

## Project Overview

This is a portfolio project designed to demonstrate
Cloud Engineering, AI Engineering, DevOps and
multi-cloud architecture skills.

The application must be developed incrementally.

## Technology Stack

### Backend
- Python
- FastAPI
- SQLite
- SQLite FTS5
- PyMuPDF
- Pytest

### Frontend
- React
- TypeScript
- Vite

### Infrastructure
- Docker Compose
- GitHub Actions
- Microsoft Azure (future)
- Amazon AWS (future)

## Version 0.1 Scope

The first version must run locally.

Features:
- Document upload
- PDF/TXT processing
- Document metadata management
- Keyword search
- Search result citations
- React dashboard

Do not implement AI features in v0.1.

Do not introduce cloud services in v0.1.

## Architecture Principles

1. Follow modular architecture.
2. Separate API routes from business logic.
3. Use configuration through environment variables.
4. Never hardcode API keys or secrets.
5. Keep the application cloud-portable.
6. Implement automated tests.
7. Use Python type hints.
8. Use clear and maintainable code.
9. Avoid unnecessary dependencies.
10. Document important architectural decisions.

## Security

- Validate uploaded file types and sizes.
- Prevent path traversal vulnerabilities.
- Never commit secrets or user-uploaded files.
- Avoid exposing internal error details.

## Development Workflow

For every implementation task:

1. Inspect the repository.
2. Explain the implementation plan.
3. Make the smallest necessary changes.
4. Run relevant tests.
5. Summarize the implementation.
6. Explain how the code works.
7. Do not commit or push without approval.

## Learning Requirement

This project is intended for learning.

After each implementation:

- Explain important concepts.
- Identify architectural decisions.
- Explain potential weaknesses.
- Suggest the next logical milestone.