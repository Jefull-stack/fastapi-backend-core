from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "CHANGE_ME"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ACCESS_SECRET_KEY: str = "CHANGE_ME"
    REFRESH_SECRET_KEY: str = "CHANGE_ME"

    model_config = {"env_file": ".env"}

settings = Settings()