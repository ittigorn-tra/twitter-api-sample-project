from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


def test_wrong_path():
  response = client.get('/wrong_path')
  assert response.status_code == 404

def test_bad_format_username():
  response = client.get('/users/สวัสดี')
  assert response.status_code == 422