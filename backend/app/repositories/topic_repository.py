import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "bible_topics.json"


class TopicRepository:

    @staticmethod
    def load_bible_topics():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
