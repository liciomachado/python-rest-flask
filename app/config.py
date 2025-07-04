import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", True)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")
    CAR_FUNCTION_API_KEY = os.getenv("CAR_FUNCTION_API_KEY")