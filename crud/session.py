from sqlalchemy.orm import Session
from models.sessions import Session as SessionModel

def session_create(db: Session, user_number: int):
    new_session = SessionModel(user_number=user_number)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session
