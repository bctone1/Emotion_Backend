from fastapi import Request
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.content_interactions import create_content
from database.base import get_db


router = APIRouter(
    prefix="/content_interactions",
    tags=["Content_interactions"]
)


@router.post("/create_content_data")
async def create_content_data(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    session_id = data.get("session_id")
    recommended_emotion = data.get("recommended_emotion")
    content_type = data.get("content_type")
    content_title = data.get("content_title")
    viewing_completed = data.get("viewing_completed")
    stopped_early = data.get("stopped_early")
    interaction_timestamp = data.get("interaction_timestamp")

    new_content_data = create_content(
        db=db,
        session_id=session_id,
        recommended_emotion=recommended_emotion,
        content_type=content_type,
        content_title=content_title,
        viewing_completed=viewing_completed,
        stopped_early=stopped_early,
        interaction_timestamp=interaction_timestamp
    )

    return {"message": "콘텐츠 데이터가 등록되었습니다!", "interaction_id": str(new_content_data.interaction_id)}



