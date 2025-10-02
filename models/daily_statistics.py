# app/models/daily_statistics.py
from sqlalchemy import Column, Date, Integer, Float
from database.base import Base

class DailyStatistics(Base):
    __tablename__ = "daily_statistics"

    date = Column(Date, primary_key=True)
    total_users = Column(Integer, nullable=False, default=0)
    daily_measurements = Column(Integer, nullable=False, default=0)
    avg_session_duration = Column(Float, nullable=True)  # seconds
