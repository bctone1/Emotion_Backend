from sqlalchemy.orm import Session

from models.emotion_measurements import EmotionMeasurement


def create_emotion(
        db: Session,
        session_id: str,
        measurement_type: str,
        emotion_name: str,
        confidence_score: float,
        face_detection_success: bool
):
    """
    감정 측정 데이터를 DB에 저장
    """
    new_measurement = EmotionMeasurement(
        session_id=session_id,
        measurement_type=measurement_type,
        emotion_name=emotion_name,
        confidence_score=confidence_score,
        face_detection_success=face_detection_success,
    )

    db.add(new_measurement)
    db.commit()
    db.refresh(new_measurement)

    return new_measurement