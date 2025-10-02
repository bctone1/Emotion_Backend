# app/models/content_interactions.py
from sqlalchemy import Column, DateTime, String, Boolean, Enum, ForeignKey, Index, func
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
import enum  # ← 이 라인 추가

from models.common import gen_uuid


class ContentType(enum.Enum):
    video = "video"
    images = "images"
    meditation = "meditation"
    article = "article"

class ContentInteraction(Base):
    __tablename__ = "content_interactions"

    interaction_id = Column(UUID(as_uuid=True), primary_key=True, default=gen_uuid)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.session_id", ondelete="CASCADE"), nullable=False, index=True)
    recommended_emotion = Column(String(50), nullable=True)
    content_type = Column(Enum(ContentType, name="content_type_enum"), nullable=False)
    content_title = Column(String(255), nullable=False)
    viewing_completed = Column(Boolean, nullable=False, default=False)
    stopped_early = Column(Boolean, nullable=False, default=False)
    interaction_timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)

    __table_args__ = (
        Index("ix_content_session_interaction", "session_id", "interaction_timestamp"),
    )
