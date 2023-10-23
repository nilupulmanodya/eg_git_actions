import pytest
from server1.main import APP

def test_request_example(client):
    response = client.get("/")
    assert b"<p>Hello, World!</p>" in response.data


def test_return_sum(client):
    response = client.post("/sum/", json={
  "first_val": 40,
  "second_val": 60
})
    assert response.status_code == 200
    assert response.data.decode("utf-8")=="100"


def test_return_difference(client):
    test_data = {
        "first_val": 10,
        "second_val": 8
    }
    response = client.post("/subtract/", json=test_data)

    assert response.status_code == 200
    assert response.data.decode("utf-8")== "2"


def test_return_product(client):
    test_data = {
        "first_val": 8,
        "second_val": 2
    }
    response = client.post("/multiplication/", json=test_data)

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "16"


def test_return_dividend(client):
    test_data = {
        "first_val": 8,
        "second_val": 2
    }
    response = client.post("/division/", json=test_data)

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "4.0"
