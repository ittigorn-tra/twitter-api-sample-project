from fastapi  import FastAPI
from typing import Optional
from pydantic import constr, conint

from app.core.settings import Settings

settings  = Settings()
app       = FastAPI()


@app.get('/')
async def root():
  return {'message': 'API is working OK'}


@app.get('/status')
async def server_status():
  return {
    'root_dir': settings.root_dir,
    'environment': settings.environment,
  }

@app.get('/hashtags/{hashtag}')
async def get_tweets_by_a_hashtag(hashtag: constr(min_length=1), limit: Optional[conint(gt=0)]=30) -> dict:
  results = {
    'hashtag' : hashtag,
    'limit'   : limit,
  }
  return results

@app.get('/users/{user_id}')
async def get_user_tweets(user_id: constr(min_length=1), limit: Optional[conint(gt=0)]=30) -> dict:
  results = {
    'user_id' : user_id,
    'limit'   : limit,
  }
  return results

