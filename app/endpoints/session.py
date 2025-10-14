from fastapi import Request, Query
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.session import session_create, session_end
from database.base import get_db
from datetime import datetime, date

from sqlalchemy import func, distinct, cast, Date
from models.sessions import Session as SessionModel

router = APIRouter(
    prefix="/session",
    tags=["Session"]
)


@router.get("/stats")
async def get_session_stats(
        client_ip: str = Query(None),  # ?client_ip=... 로 받음
        db: Session = Depends(get_db)
):
    if not client_ip:
        client_ip = "unknown"

    total_users = db.query(func.count(distinct(SessionModel.user_number))).scalar()

    today = date.today()
    today_measurements = (
        db.query(func.count(SessionModel.session_id))
        .filter(cast(SessionModel.end_time, Date) == today)
        .scalar()
    )

    my_measurements = (
        db.query(func.count(SessionModel.session_id))
        .filter(SessionModel.user_ip == client_ip)
        .filter(SessionModel.end_time.isnot(None))
        .scalar()
    )

    return {
        "total_users": total_users,
        "today_measurements": today_measurements,
        "my_measurements": my_measurements,
        "user_ip": client_ip
    }


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


@router.post("/session_end")
async def end_session(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    session_id = data.get("session_id")
    end_time = data.get("end_time")

    if not session_id:
        return {"error": "session_id is required"}

    updated_session = session_end(db=db, session_id=session_id, end_time=end_time)
    if not updated_session:
        return {"error": "세션을 찾을 수 없습니다."}

    return {
        "message": "세션이 종료되었습니다!",
        "session_id": str(updated_session.session_id),
        "end_time": updated_session.end_time,
        "total_duration": updated_session.total_duration
    }
