from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/blacklist")
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")


if not TELEGRAM_API_TOKEN:
    raise ValueError("TELEGRAM_API_TOKEN is not set in the environment variables")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables ")

