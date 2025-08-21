from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

from app.core.config import settings
from app.api.v1.api import api_router
from app.core.database import engine
from app.core.redis import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up AI Project Management API...")
    # TODO: Initialize database, Redis, and other services
    yield
    # Shutdown
    print("Shutting down AI Project Management API...")
    await redis_client.close()


app = FastAPI(
    title="AI-Powered Project Management API",
    description="Enterprise project operating system with AI copilots",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "AI-Powered Project Management API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ai-project-management-api"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
