from fastapi import APIRouter, FastAPI
from app.endpoints import session

router = APIRouter()

router.include_router(session.router)