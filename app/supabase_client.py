from supabase import create_client
from app.config import settings

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)


def get_supabase_client():
    return supabase
