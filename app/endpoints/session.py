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

    # start_time이 없으면 현재 시간으로 설정
    if start_time:

        start_time = datetime.fromisoformat(start_time)
    else:
        start_time = None

    new_session = session_create(
        db=db,
        user_number=user_number,
        user_ip=user_ip,
        start_time=start_time
    )

    return {"message": "Session created!", "session_id": str(new_session.session_id)}