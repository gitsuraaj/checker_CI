from loan_app import app
import pytest
import json

@pytest.fixture
def client():
    return app.test_client()
def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200


def test_prediction(client):
    test_data = {
"Gender":"Male",
"Married": "Unmarried",
"ApplicantIncome": 50000,
"Credit_History": 1.0,
"LoanAmount": 500000
}

    resp = client.post("/predict", json=test_data)
    assert resp.status_code == 200
    assert resp.json == {'loan_approval_status: ': 'Rejected'}


