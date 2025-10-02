from fastapi import Request
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.performance_metrics import create_metrics
from database.base import get_db

router = APIRouter(
    prefix="/performance_metrics",
    tags=["Performance_metrics"]
)


@router.post("/create_metrics_dtaa")
async def create_metrics_dtaa(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    session_id = data.get("session_id")
    face_detection_accuracy=data.get("face_detection_accuracy")
    emotion_confidence_avg = data.get("emotion_confidence_avg")
    valid_measurement_rate = data.get("valid_measurement_rate")
    processing_time = data.get("processing_time")
    api_success_rate = data.get("api_success_rate")


    new_metrics_data = create_metrics(
        db=db,
        session_id=session_id,
        face_detection_accuracy=face_detection_accuracy,
        emotion_confidence_avg=emotion_confidence_avg,
        valid_measurement_rate=valid_measurement_rate,
        processing_time=processing_time,
        api_success_rate=api_success_rate
    )

    return {"message": "메트릭스 데이터가 등록되었습니다!", "metric_id": str(new_metrics_data.metric_id)}


