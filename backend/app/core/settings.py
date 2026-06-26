import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """
    Centralized configuration settings for the MeetIQ application.
    """
    # FastAPI Configuration
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    
    # Gemini API Configuration
    GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY")

settings = Settings()
