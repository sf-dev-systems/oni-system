from typing import Optional
from supabase import create_client, Client
from .config import get_settings

_supabase_client: Optional[Client] = None


def get_supabase_client() -> Client:
    global _supabase_client
    if _supabase_client is not None:
        return _supabase_client

    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_key:
        raise RuntimeError("Supabase configuration is missing")

    _supabase_client = create_client(settings.supabase_url, settings.supabase_key)
    return _supabase_client
