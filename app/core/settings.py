import os
from pydantic import BaseSettings



class Settings(BaseSettings):
  app_name:                 str
  environment:              str
  twitter_bearer_token:     str
  root_dir:                 str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  twitter_max_result_size:  int = 100
  twitter_max_query_length: int = 512

  class Config:
    env_file          = '.env'
    env_file_encoding = 'utf-8'