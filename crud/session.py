from sqlalchemy.orm import Session
from models.sessions import Session as SessionModel
from datetime import datetime, timezone


def session_create(db: Session, user_number: int, user_ip: str, start_time: datetime = None):
    new_session = SessionModel(
        user_number=user_number,
        user_ip=user_ip,
        start_time=start_time or datetime.utcnow()
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session


def session_end(db: Session, session_id: str, end_time: datetime = None):
    # 세션 객체 가져오기
    session_obj = db.query(SessionModel).filter(SessionModel.session_id == session_id).first()
    if not session_obj:
        return None

    # end_time이 없으면 현재 UTC 시간으로
    if end_time is None:
        end_time = datetime.now(timezone.utc)

    # end_time이 문자열로 들어온 경우 변환
    if isinstance(end_time, str):
        try:
            end_time = datetime.fromisoformat(end_time)
        except ValueError:
            raise ValueError(f"Invalid datetime format for end_time: {end_time}")

    session_obj.end_time = end_time

    if session_obj.start_time:
        # total_duration 계산 (초 단위)
        session_obj.total_duration = int((end_time - session_obj.start_time).total_seconds())

    db.commit()
    db.refresh(session_obj)
    return session_obj
