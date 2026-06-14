from fastapi.testclient import TestClient
import copy
import pytest

from src.app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient and restore the in-memory `activities` after each test."""
    original = copy.deepcopy(activities)
    client = TestClient(app)
    yield client
    activities.clear()
    activities.update(copy.deepcopy(original))
