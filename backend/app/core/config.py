from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "local"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
