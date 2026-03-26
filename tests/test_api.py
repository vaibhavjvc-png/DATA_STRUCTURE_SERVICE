from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_dataset():
    response = client.post("/datasets/", json={"name": "Customer"})
    assert response.status_code == 200
    assert response.json()["name"] == "Customer"


def test_add_data_element():
    dataset = client.post("/datasets/", json={"name": "Order"}).json()

    response = client.post(
        f"/datasets/{dataset['id']}/elements/",
        json={"name": "amount", "data_type": "float", "is_pii": False},
    )

    assert response.status_code == 200
    assert response.json()["name"] == "amount"