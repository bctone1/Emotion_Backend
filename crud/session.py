from sqlalchemy.orm import Session
from models.sessions import Session as SessionModel
from datetime import datetime

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