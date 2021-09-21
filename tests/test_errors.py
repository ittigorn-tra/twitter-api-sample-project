from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


def test_wrong_path():
  response = client.get('/wrong_path')
  assert response.status_code == 404