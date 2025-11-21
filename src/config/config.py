from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    EXPIRES_MIN: int
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
