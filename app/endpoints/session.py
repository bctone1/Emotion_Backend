from fastapi import Request
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.session import session_create
from database.base import get_db
from datetime import datetime

router = APIRouter(
    prefix="/session",
    tags=["Session"]
)


@router.post("/session_create")
async def create_session(request: Request, db: Session = Depends(get_db)):
    data = await request.json()

    user_number = data.get("user_number")
    user_ip = data.get("user_ip")
    start_time = data.get("start_time")

    if not user_number or not user_ip:
        return {"error": "user_number and user_ip are required"}

    new_session = session_create(
        db=db,
        user_number=user_number,
        user_ip=user_ip,
        start_time=start_time
    )

    return {"message": "세션이 생성되었습니다!", "session_id": str(new_session.session_id)}