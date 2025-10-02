from fastapi import Request
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.emotion_measurements import create_emotion
from database.base import get_db


router = APIRouter(
    prefix="/emotion_measurements",
    tags=["Emotion_measurements"]
)



@router.post("/create_emotion_data")
async def create_emotion_data(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    session_id = data.get("session_id")
    measurement_type = data.get("measurement_type")
    emotion_name = data.get("emotion_name")
    confidence_score = data.get("confidence_score")
    face_detection_success = data.get("face_detection_success")

    new_data = create_emotion(
        db=db,
        session_id = session_id,
        measurement_type = measurement_type,
        emotion_name = emotion_name,
        confidence_score = confidence_score,
        face_detection_success=face_detection_success
    )

    return {"message": "결과가 저장되었습니다!", "measurement_id": str(new_data.measurement_id)}
