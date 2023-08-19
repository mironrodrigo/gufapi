from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:miron@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = '0CBnDn1V2dpWdvNZwHym8hi2Ya0jkZHZ3A46fILIlgo'
    """
    Só rodar isso no terminal :point-down:
    
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1 semana em minutos

    class Config:
        case_sensitive = True


settings: Settings = Settings()
