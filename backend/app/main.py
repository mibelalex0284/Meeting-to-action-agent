# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.api.test_llm import router as test_llm_router

app = FastAPI(
    title="MeetIQ API",
    description="Intelligent meeting assistant and action extraction engine",
    version="0.1.0"
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(test_llm_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to MeetIQ API",
        "docs_url": "/docs",
        "health_url": "/health"
    }

@app.get("/health")
async def health():
    return {
        "status": "ok"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
