"""FastAPI entry point for the local backend."""

from fastapi import FastAPI

app = FastAPI(title="AI Knowledge Assistant", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Return application identity and process health."""
    return {
        "status": "healthy",
        "application": app.title,
        "version": app.version,
    }
