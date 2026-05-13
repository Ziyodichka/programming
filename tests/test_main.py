from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_item_by_id():
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_item_not_found():
    response = client.get("/api/v1/items/9999")
    assert response.status_code == 404

def test_create_item():
    new_item = {"id": 99, "name": "Test mahsulot", "description": "Test", "price": 99.9}
    response = client.post("/api/v1/items/", json=new_item)
    assert response.status_code == 201
    assert response.json()["name"] == "Test mahsulot"
