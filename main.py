import os
import uvicorn
from fastapi import FastAPI
from app.endpoints import session

# FastAPI 인스턴스 생성
app = FastAPI()

# 라우터 등록
app.include_router(session.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")),
        reload=bool(int(os.getenv("RELOAD", "0"))),
    )
