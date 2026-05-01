from fastapi.testclient import TestClient

from elochess.api.app import app

client = TestClient(app)


def test_update_elo() -> None:
    """Test the update Elo API route."""
    payload = {
        "current_rating": 1500,
        "opponent_ratings": [1400, 1600],
        "score": 1.5,
    }

    response = client.post("/update/elo", json=payload)

    assert response.status_code == 200
    assert response.json() == {"rating": 1510}


def test_update_dwz() -> None:
    """Test the update DWZ API route."""
    payload = {
        "current_rating": 1500,
        "opponent_ratings": [1400, 1600],
        "score": 1.5,
    }

    response = client.post("/update/dwz", json=payload)

    assert response.status_code == 200
    assert response.json() == {"rating": 1518}
