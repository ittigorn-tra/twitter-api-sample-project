from datetime import datetime

import pytz
import requests
from app.core.settings import Settings


class TwitterServices(object):
    _settings = Settings()
    search_recent_url = "https://api.twitter.com/2/tweets/search/recent"

    @classmethod
    def parse_datetime(cls, dt: str, localize: bool = True) -> datetime:
        parsed_dt = datetime.strptime(
            dt, cls._settings.twitter_datetime_format)

        # localize
        if localize:
            utc = pytz.utc
            parsed_dt = utc.localize(parsed_dt)
            parsed_dt = parsed_dt.astimezone(
                pytz.timezone(cls._settings.default_timezone))

        return parsed_dt

    @classmethod
    def reformat_datetime(cls, dt: str) -> str:
        parsed_dt = cls.parse_datetime(dt)
        time_str = parsed_dt.strftime('%H:%M %p - ')
        date_str = parsed_dt.strftime(' %b %Y')
        result_str = f'{time_str}{parsed_dt.day}{date_str}'
        if result_str[:1] == '0':
            result_str = result_str[1:]
        return result_str

    @classmethod
    def _bearer_oauth(cls, req):
        req.headers["Authorization"] = f"Bearer {cls._settings.twitter_bearer_token}"
        req.headers["User-Agent"] = "v2RecentSearchPython"
        return req

    @classmethod
    def _connect_to_endpoint(cls, url: str, query_params=None):
        response = requests.get(
            url, auth=cls._bearer_oauth, params=query_params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    @classmethod
    def execute_query(cls, url: str, query_params=None):
        json_response = cls._connect_to_endpoint(
            url=url, query_params=query_params)
        return json_response


# module testing
if __name__ == '__main__':
    from pprint import pprint
    query_params = {'query': '#python', 'tweet.fields': 'author_id'}
    pprint(TwitterServices.search_recent(query_params))
