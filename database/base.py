from sqlalchemy.ext.declarative import declarative_base
import core.config as config
import os
from sqlalchemy import create_engine
Base = declarative_base()
from sqlalchemy.orm import sessionmaker

database = config.DB
user = config.DB_USER
pw = config.DB_PASSWORD
server = config.DB_SERVER
port = config.DB_PORT
name = config.DB_NAME
DATABASE_URL = os.getenv('DATABASE_URL', f'{database}://{user}:{pw}@{server}:{port}/{name}')


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
