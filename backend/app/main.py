from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title="Biblical Topic Distribution API",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api")
