#llm_service.py
import logging
from typing import Optional, Any
from google import genai
from google.genai.errors import APIError
from app.core.settings import settings

# Setup logging
logger = logging.getLogger(__name__)


class LLMServiceError(Exception):
    """Custom exception class for Gemini LLM Service errors."""
    pass


class LLMService:
    """
    A service class responsible for interacting with the Google Gemini API.
    
    Encapsulates SDK initialization, model inference, and error handling.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initializes the LLMService.
        
        Args:
            api_key: Optional API key. If not provided, it reads from the GEMINI_API_KEY configuration setting.
            
        Raises:
            LLMServiceError: If no API key is found or if client initialization fails.
        """
        # Read API key from parameter or settings
        self.api_key = api_key or settings.GEMINI_API_KEY
        
        if not self.api_key:
            logger.error("GEMINI_API_KEY is not set in configuration or .env file.")
            raise LLMServiceError(
                "GEMINI_API_KEY is not configured. Please set the GEMINI_API_KEY environment variable "
                "or define it in your .env file."
            )
            
        try:
            # Initialize the Gemini client with the API key
            self.client = genai.Client(api_key=self.api_key)
            logger.info("Gemini client successfully initialized.")
        except Exception as e:
            logger.exception("Failed to initialize Gemini client.")
            raise LLMServiceError(f"Failed to initialize Gemini client: {str(e)}") from e

    def generate_text(
        self, 
        prompt: str, 
        model: str = "gemini-2.5-flash", 
        **kwargs: Any
    ) -> str:
        """
        Sends a text prompt to the specified Gemini model and returns the response.
        
        Args:
            prompt: The text prompt to send to the model.
            model: The model name to use (default: "gemini-2.5-flash").
            **kwargs: Additional configuration parameters for client.models.generate_content.
            
        Returns:
            The text response from the model.
            
        Raises:
            LLMServiceError: If the API call fails due to validation, rate limits, network issues, etc.
        """
        if not prompt:
            raise LLMServiceError("Prompt cannot be empty.")
            
        try:
            logger.info(f"Sending prompt to model '{model}'...")
            response = self.client.models.generate_content(
                model=model,
                contents=prompt,
                **kwargs
            )
            
            # Check if we got a valid response text
            if not response.text:
                logger.warning("Received empty response or response lacked text content.")
                return ""
                
            return response.text
            
        except APIError as e:
            logger.exception(f"Gemini API Error occurred: {e}")
            raise LLMServiceError(f"Gemini API returned an error (code {e.code}): {e.message}") from e
        except Exception as e:
            logger.exception(f"Unexpected error when calling Gemini API: {e}")
            raise LLMServiceError(f"An unexpected error occurred during LLM generation: {str(e)}") from e
