from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 모델을 모두 import 해야 metadata에 등록됨
from models import sessions
from models import emotion_changes
from models import performance_metrics
from models import emotion_measurements
from models import daily_statistics
from models import content_interactions


# from .sessions import Session
# from .content_interactions import ContentInteraction
# from .emotion_changes import EmotionChange
