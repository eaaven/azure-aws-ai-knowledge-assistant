"""Tests for the public health endpoint."""

from fastapi.testclient import TestClient

from app.main import app


def test_health_returns_application_status() -> None:
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "application": "AI Knowledge Assistant",
        "version": "0.1.0",
    }
