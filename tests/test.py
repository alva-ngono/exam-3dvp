from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={
        "id": 1,
        "name": "Test Item",
        "price": 10.5,
        "in_stock": True
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item_by_id():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_item():
    response = client.put("/items/1", json={
        "id": 1,
        "name": "Updated Item",
        "price": 15.0,
        "in_stock": False
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"

def test_get_nonexistent_item():
    response = client.get("/items/999")
    assert response.status_code == 404
