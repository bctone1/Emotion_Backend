# app/models/performance_metrics.py
from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
from models.common import gen_uuid


class PerformanceMetric(Base):
    __tablename__ = "performance_metrics"

    metric_id = Column(UUID(as_uuid=True), primary_key=True, default=gen_uuid)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.session_id", ondelete="CASCADE"), nullable=False, index=True)
    face_detection_accuracy = Column(Float, nullable=True)   # 0..1
    emotion_confidence_avg = Column(Float, nullable=True)
    valid_measurement_rate = Column(Float, nullable=True)
    processing_time = Column(Float, nullable=True)   # milliseconds or seconds (일관된 단위 표기 필요)
    api_success_rate = Column(Float, nullable=True)  # 0..1
