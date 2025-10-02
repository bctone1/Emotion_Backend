import os
import uvicorn
from fastapi import FastAPI
from app.endpoints import session
from fastapi.middleware.cors import CORSMiddleware
from app.routers import register_routers

# FastAPI 인스턴스 생성
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
register_routers(app)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")),
        reload=bool(int(os.getenv("RELOAD", "0"))),
    )
