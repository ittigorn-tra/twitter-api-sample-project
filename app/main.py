from typing import Optional

from fastapi import FastAPI
from pydantic import conint, constr

from app.core.models.Hashtags import Hashtags
from app.core.models.Users import Users
from app.core.settings import Settings

settings = Settings()
app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'API is online'}


@app.get('/status')
async def server_status():
    '''
    This endpoint responds with the status of the server. This could be useful when you want to check if the server environment and variables are as expected.
    '''
    return {
        'base_dir': settings.base_dir,
        'environment': settings.environment,
    }


@app.get('/hashtags/{hashtag}')
async def get_tweets_by_a_hashtag(
        hashtag: constr(min_length=1, max_length=settings.twitter_max_query_length),
        limit:   Optional[
            conint(
                ge=settings.twitter_min_result_size,
                le=settings.twitter_max_result_size,
            )
        ] = 30) -> dict:

    '''
    This endpoint searches the most recent tweets then responds with tweets matching the query string in reverse chronological order.
    '''

    results = Hashtags.search(hashtag=hashtag, limit=limit)
    return results


@app.get('/users/{username}')
async def get_user_tweets(
    username: constr(
        min_length=1,
        max_length=settings.twitter_max_query_length,
        regex=settings.twitter_username_regex
    ),
    limit:    Optional[
        conint(
            ge=settings.twitter_min_result_size,
            le=settings.twitter_max_result_size,
        )
    ] = 30,
    exclude_retweets: Optional[bool] = True,
    exclude_replies:  Optional[bool] = True,
) -> dict:
    '''
    This endpoint searches the most recent tweets from a specific user then responds with the data in reverse chronological order.
    '''

    results = Users.search_by_username(
        username=username, limit=limit, exclude_retweets=exclude_retweets, exclude_replies=exclude_replies)
    return results
