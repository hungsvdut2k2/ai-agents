from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_DEFAULT_MODEL: str 
    PERPLEXITY_API_KEY: str
settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
