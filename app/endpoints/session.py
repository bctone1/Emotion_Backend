from urllib.request import Request

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.session import session_create
from database.base import get_db

router = APIRouter(
    prefix="/session",
    tags=["Session"]
)

@router.post("/create")
def create_session(request: Request, db: Session = Depends(get_db)):

    new_session = session_create(db=db, user_number=1)
    return {"message": "Session created!", "session_id": str(new_session.session_id)}