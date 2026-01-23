from fastapi import APIRouter
from app.models.topic import TopicDistribution
from app.services.topic_service import TopicService

router = APIRouter()


@router.get("/", response_model=TopicDistribution)
def get_bible_topic_distribution():
    return TopicService.get_bible_distribution()
