import os
from pydantic import BaseSettings



class Settings(BaseSettings):
  app_name:         str
  environment:      str
  root_dir:         str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

  class Config:
    env_file          = '.env'
    env_file_encoding = 'utf-8'