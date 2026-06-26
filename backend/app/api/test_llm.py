from fastapi import APIRouter, HTTPException, Depends
from app.schemas.llm import LLMTestRequest, LLMTestResponse
from app.services.llm_service import LLMService, LLMServiceError

router = APIRouter()

def get_llm_service() -> LLMService:
    """Dependency to retrieve an initialized LLMService instance."""
    try:
        return LLMService()
    except LLMServiceError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/test-llm", response_model=LLMTestResponse, summary="Test integration with Gemini")
async def test_llm(
    request: LLMTestRequest, 
    llm_service: LLMService = Depends(get_llm_service)
):
    """
    Sends the provided message prompt to the Gemini API and returns the response.
    
    This is used to verify end-to-end integration with the LLM provider.
    """
    try:
        response_text = llm_service.generate_text(prompt=request.message)
        return LLMTestResponse(response=response_text)
    except LLMServiceError as e:
        raise HTTPException(status_code=500, detail=str(e))
