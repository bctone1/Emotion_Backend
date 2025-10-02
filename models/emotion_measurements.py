# app/models/emotion_measurements.py
from sqlalchemy import Column, DateTime, Float, Boolean, Enum, ForeignKey, String, Index, func
from sqlalchemy.dialects.postgresql import UUID
from database.base import Base
import enum

from models.common import gen_uuid


class MeasurementType(enum.Enum):
    primary = "primary"
    secondary = "secondary"

class EmotionMeasurement(Base):
    __tablename__ = "emotion_measurements"

    measurement_id = Column(UUID(as_uuid=True), primary_key=True, default=gen_uuid)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.session_id", ondelete="CASCADE"), nullable=False, index=True)
    measurement_type = Column(Enum(MeasurementType, name="measurement_type_enum"), nullable=False)
    emotion_name = Column(String(50), nullable=False)
    confidence_score = Column(Float, nullable=False)  # 0.0 ~ 1.0
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    face_detection_success = Column(Boolean, default=True, nullable=False)

    __table_args__ = (
        Index("ix_em_measure_session_time", "session_id", "timestamp"),
    )
