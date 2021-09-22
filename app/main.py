from fastapi  import FastAPI
from typing import Optional
from pydantic import constr, conint

from app.core.settings        import Settings
from app.core.models.Hashtags import Hashtags

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
async def get_tweets_by_a_hashtag(
  hashtag: constr(min_length=1, max_length=settings.twitter_max_query_length), 
  limit: Optional[
    conint(
      ge=settings.twitter_min_result_size, 
      le=settings.twitter_max_result_size,
    )
  ]=30) -> dict:

  results = Hashtags.search(hashtag=hashtag, limit=limit)
  
  return results

@app.get('/users/{user_id}')
async def get_user_tweets(
  user_id: constr(min_length=1, max_length=settings.twitter_max_query_length),
  limit: Optional[
    conint(
      ge=settings.twitter_min_result_size, 
      le=settings.twitter_max_result_size,
    )
  ]=30) -> dict:
  results = {
    'user_id' : user_id,
    'limit'   : limit,
  }
  return results

