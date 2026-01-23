from fastapi import APIRouter
from app.api.v1.endpoints import health, topics, analysis

router = APIRouter()
router.include_router(health.router, tags=["health"])
router.include_router(topics.router, prefix="/topics", tags=["topics"])
router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
