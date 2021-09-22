from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


def test_root():
  response = client.get('/')
  assert response.status_code == 200
  assert response.json() == {"message": "API is working OK"}


def test_status():
  response = client.get('/status')
  assert response.status_code == 200
  assert 'root_dir'         in response.json().keys()
  assert 'environment'      in response.json().keys()


def test_get_tweets_by_a_hashtag():
  response = client.get('/hashtags/python')
  assert response.status_code == 200
  assert type(response.json()) is list


def test_get_tweets_by_a_hashtag():
  response = client.get('/users/twitter')
  assert response.status_code == 200
  assert type(response.json()) is list