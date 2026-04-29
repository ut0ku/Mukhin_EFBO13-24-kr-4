from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_success():
    response = client.post("/users", json={
        "username": "testuser",
        "age": 25,
        "email": "test@example.com",
        "password": "password123",
        "phone": "1234567890"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User created"
    assert "user_id" in data
    assert data["user"]["username"] == "testuser"

def test_create_user_age_too_low():
    response = client.post("/users", json={
        "username": "testuser",
        "age": 17,
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 422
    data = response.json()
    assert "Validation error" in data["detail"]

def test_create_user_invalid_email():
    response = client.post("/users", json={
        "username": "testuser",
        "age": 25,
        "email": "invalidemail",
        "password": "password123"
    })
    assert response.status_code == 422
    data = response.json()
    assert "Validation error" in data["detail"]

def test_create_user_password_too_short():
    response = client.post("/users", json={
        "username": "testuser",
        "age": 25,
        "email": "test@example.com",
        "password": "short"
    })
    assert response.status_code == 422
    data = response.json()
    assert "Validation error" in data["detail"]

def test_create_user_password_too_long():
    response = client.post("/users", json={
        "username": "testuser",
        "age": 25,
        "email": "test@example.com",
        "password": "verylongpasswordthatiswaytoolong"
    })
    assert response.status_code == 422
    data = response.json()
    assert "Validation error" in data["detail"]

def test_get_user_success():
    create_response = client.post("/users", json={
        "username": "getuser",
        "age": 30,
        "email": "get@example.com",
        "password": "password123"
    })
    user_id = create_response.json()["user_id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert data["user"]["username"] == "getuser"

def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"

def test_delete_user_success():
    create_response = client.post("/users", json={
        "username": "deluser",
        "age": 28,
        "email": "del@example.com",
        "password": "password123"
    })
    user_id = create_response.json()["user_id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User deleted"
    assert data["user_id"] == user_id

    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404

def test_delete_user_not_found():
    response = client.delete("/users/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"