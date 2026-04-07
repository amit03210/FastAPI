# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, env_file_encoding="UTF-8"
    )

    APP_NAME: str
    APP_DESCRIPTION: str
    APP_VERSION: str
    DEBUG: bool
    SECRET_KEY: str
    DATABASE_URL: str
    ALLOWED_HOSTS: list[str]
    CONTACT_EMAIL: str

    # class Config:
    #     env_file = ".env"


settings = Settings()
print(settings.ALLOWED_HOSTS)
