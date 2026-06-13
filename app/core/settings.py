from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Research API"
    db_url: str = "sqlite:///./dev.db"
    redis_url: str = "redis://localhost:6379/0"

    openrouter_base_url: str
    openrouter_api_key: str
    tavily_api_key: str
    model_config = SettingsConfigDict(extra="ignore", env_file=".env")

settings = Settings() #type: ignore