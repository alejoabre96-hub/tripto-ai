import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
META_VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN", "tripto2026")
META_PAGE_ACCESS_TOKEN = os.getenv("META_PAGE_ACCESS_TOKEN", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
