# crud/performance_metrics.py
from sqlalchemy.orm import Session
from models.performance_metrics import PerformanceMetric


def create_metrics(
    db: Session,
    session_id: str,
    face_detection_accuracy: float,
    emotion_confidence_avg: float,
    valid_measurement_rate: float,
    processing_time: float,
    api_success_rate: float,
):
    new_metrics = PerformanceMetric(
        session_id=session_id,
        face_detection_accuracy=face_detection_accuracy,
        emotion_confidence_avg=emotion_confidence_avg,
        valid_measurement_rate=valid_measurement_rate,
        processing_time=processing_time,
        api_success_rate=api_success_rate,
    )

    db.add(new_metrics)
    db.commit()
    db.refresh(new_metrics)

    return new_metrics
