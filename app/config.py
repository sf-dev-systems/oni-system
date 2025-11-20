import os
from functools import lru_cache
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.exists():
    load_dotenv(ENV_PATH)


class Settings:
    def __init__(self) -> None:
        self.environment = os.getenv("ENVIRONMENT", "local")

        self.SUPABASE_URL = os.getenv("SUPABASE_URL", "")
        self.SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "")
        self.supabase_url = self.SUPABASE_URL
        self.supabase_key = self.SUPABASE_ANON_KEY

        self.pinecone_api_key = os.getenv("PINECONE_API_KEY", "")
        self.pinecone_index = os.getenv("PINECONE_INDEX_NAME", "")

        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

        self.claude_api_key = os.getenv("CLAUDE_API_KEY", "")
        self.claude_model = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
