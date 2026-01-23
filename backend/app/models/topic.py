from pydantic import BaseModel
from typing import Dict


class TopicDistribution(BaseModel):
    topics: Dict[str, float]
