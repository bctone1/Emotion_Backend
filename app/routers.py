from fastapi import APIRouter, FastAPI
from app.endpoints import session, emotion_measurements, content_interactions, performance_metrics

router = APIRouter()

router.include_router(session.router)
router.include_router(emotion_measurements.router)
router.include_router(content_interactions.router)
router.include_router(performance_metrics.router)



def register_routers(app: FastAPI) -> None:
    app.include_router(router)