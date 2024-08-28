import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Project"
    upload_folder: str = "app/static/uploads/"
    output_folder: str = "app/static/output/"

    class Config:
        env_file = ".env"

settings = Settings()
