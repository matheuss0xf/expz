import pytest
from fastapi.testclient import TestClient

from app.app import app


@pytest.fixture
def client():
    return TestClient(app)  # Organizar (Arrange)
