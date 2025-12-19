from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Nexeus RAG"
    ENV: str = "development"

    DATABASE_URL: str = "sqlite:///./nexeus.db"
    SECRET_KEY: str = "mysecretkey"

    class Config:
        env_file = ".env"
        extra = "ignore"



settings = Settings()
