import os
from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    app_name:                 str
    environment:              str
    twitter_bearer_token:     str
    BASE_DIR:                 str = os.path.join(*Path(__file__).resolve().parent.parent.parent.parts)
    twitter_min_result_size:  int = 10
    twitter_max_result_size:  int = 100
    twitter_max_query_length: int = 512
    twitter_datetime_format:  str = "%Y-%m-%dT%H:%M:%S.%fZ"
    twitter_username_regex:   str = "^[A-Za-z0-9_]{1,15}$"
    default_timezone:         str = 'Asia/Bangkok'
    pickle_protocol:          int = 4

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
