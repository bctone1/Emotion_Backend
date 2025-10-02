# app/models/sessions.py
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID, INET
from sqlalchemy import Index, func
from database.base import Base
from .common import gen_uuid

class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(UUID(as_uuid=True), primary_key=True, default=gen_uuid)
    user_ip = Column(INET, nullable=False, index=True)
    user_number = Column(Integer, nullable=False, index=True)
    start_time = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    end_time = Column(DateTime(timezone=True), nullable=True)
    total_duration = Column(Integer, nullable=True)  # seconds

    # 관계 정의 (Backrefs from other tables will reference this)
    # e.g. emotion_measurements -> session, content_interactions -> session
    __table_args__ = (
        Index("ix_sessions_start_time", "start_time"),
    )
