from app.repositories.topic_repository import TopicRepository


class TopicService:

    @staticmethod
    def get_bible_distribution():
        raw = TopicRepository.load_bible_topics()
        total = sum(raw.values())

        return {
            "topics": {
                topic: count / total
                for topic, count in raw.items()
            }
        }
