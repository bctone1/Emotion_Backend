# app/models/emotion_changes.py
from sqlalchemy import Column, String, Boolean, Float, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
import enum

from models.common import gen_uuid


class ChangeDirection(enum.Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"

class EmotionChange(Base):
    __tablename__ = "emotion_changes"

    change_id = Column(UUID(as_uuid=True), primary_key=True, default=gen_uuid)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.session_id", ondelete="CASCADE"), nullable=False, index=True)
    before_emotion = Column(String(50), nullable=False)
    after_emotion = Column(String(50), nullable=False)
    before_confidence = Column(Float, nullable=True)
    after_confidence = Column(Float, nullable=True)
    emotion_changed = Column(Boolean, nullable=False)
    change_direction = Column(Enum(ChangeDirection, name="change_direction_enum"), nullable=True)
