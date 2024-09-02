from fastapi.testclient import TestClient
from temp.server import app

client = TestClient(app)

def test_detect_person():
    response = client.post("/detect-person", json={"input_url": "http://example.com/image.jpg"})
    assert response.status_code == 200
    assert "task_id" in response.json()

def test_get_result():
    response = client.get("/result/some-task-id")
    assert response.status_code == 404
