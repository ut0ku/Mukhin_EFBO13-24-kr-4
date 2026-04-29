import pytest
from httpx import AsyncClient, ASGITransport
from faker import Faker
from main import app, users

@pytest.fixture(scope="function")
async def client():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope="function")
def faker():
    return Faker()

@pytest.fixture(autouse=True)
def clear_db():
    users.clear()
    yield

@pytest.mark.asyncio
async def test_create_user(client, faker):
    username = faker.user_name()
    age = faker.random_int(min=18, max=100)
    user_data = {"username": username, "age": age, "email": faker.email(), "password": faker.password(length=10)}

    response = await client.post("/users", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User created"
    assert "user_id" in data
    assert data["user"]["username"] == username
    assert data["user"]["age"] == age

@pytest.mark.asyncio
async def test_get_user_success(client, faker):
    username = faker.user_name()
    age = faker.random_int(min=18, max=100)
    user_data = {"username": username, "age": age, "email": faker.email(), "password": faker.password(length=10)}
    create_response = await client.post("/users", json=user_data)
    user_id = create_response.json()["user_id"]

    response = await client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert data["user"]["username"] == username

@pytest.mark.asyncio
async def test_get_user_not_found(client):
    response = await client.get("/users/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"

@pytest.mark.asyncio
async def test_delete_user_success(client, faker):
    username = faker.user_name()
    age = faker.random_int(min=18, max=100)
    user_data = {"username": username, "age": age, "email": faker.email(), "password": faker.password(length=10)}
    create_response = await client.post("/users", json=user_data)
    user_id = create_response.json()["user_id"]

    response = await client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User deleted"

    get_response = await client.get(f"/users/{user_id}")
    assert get_response.status_code == 404

@pytest.mark.asyncio
async def test_delete_user_not_found(client):
    response = await client.delete("/users/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"

@pytest.mark.asyncio
async def test_create_user_age_too_low(client, faker):
    user_data = {"username": faker.user_name(), "age": 17, "email": faker.email(), "password": faker.password(length=10)}
    response = await client.post("/users", json=user_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_create_user_invalid_email(client, faker):
    user_data = {"username": faker.user_name(), "age": faker.random_int(min=18, max=100), "email": "invalid", "password": faker.password(length=10)}
    response = await client.post("/users", json=user_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_create_user_password_too_short(client, faker):
    user_data = {"username": faker.user_name(), "age": faker.random_int(min=18, max=100), "email": faker.email(), "password": "short"}
    response = await client.post("/users", json=user_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_create_user_password_too_long(client, faker):
    user_data = {"username": faker.user_name(), "age": faker.random_int(min=18, max=100), "email": faker.email(), "password": "verylongpasswordthatiswaytoolong"}
    response = await client.post("/users", json=user_data)
    assert response.status_code == 422