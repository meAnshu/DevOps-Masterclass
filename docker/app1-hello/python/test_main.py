import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_status_code(client):
    """Test that the root endpoint returns 200"""
    response = client.get("/")
    assert response.status_code == 200


def test_hello_returns_json(client):
    """Test that the response is JSON"""
    response = client.get("/")
    assert response.content_type == "application/json"


def test_hello_message(client):
    """Test that the response contains the expected message"""
    response = client.get("/")
    data = response.get_json()
    assert "message" in data
    assert "Hello from Simple App (Python Flask)" in data["message"]


def test_hello_contains_env(client):
    """Test that the response contains env field"""
    response = client.get("/")
    data = response.get_json()
    assert "env" in data


def test_hello_contains_container(client):
    """Test that the response contains container field"""
    response = client.get("/")
    data = response.get_json()
    assert "container" in data
