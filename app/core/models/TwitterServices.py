import os, sys, inspect
import requests

if __name__ == "__main__":
  inc_path = os.path.realpath(os.path.abspath(os.path.dirname(os.path.split(inspect.getfile(inspect.currentframe()))[0])))
  for i in range(10):
    if os.path.split(inc_path)[1].lower() == 'app': 
      inc_path = os.path.dirname(inc_path)
      break
    else: inc_path = os.path.dirname(inc_path)
  else: raise Exception('Cannot find the project root path')
  if inc_path not in sys.path: sys.path.append(inc_path)

from app.core.settings import Settings

class TwitterServices(object):
  search_url = "https://api.twitter.com/2/tweets/search/recent"

  @staticmethod
  def bearer_oauth(r, bearer_token):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

  @staticmethod
  def connect_to_endpoint(url, params, bearer_oauth):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
      raise Exception(response.status_code, response.text)
    return response.json()

  @classmethod
  def search(cls, query_params, bearer_token:str = None):
    json_response = cls.connect_to_endpoint(cls.search_url, query_params)
    return json_response

# module testing
if __name__ == '__main__':
  import os
  settings  = Settings(os.path.join('..', '..', '..', '..', 'local.env'))

  query_params = ''
  bearer_token = settings.twitter_bearer_token

  print(TwitterServices.search(query_params, bearer_token=bearer_token))