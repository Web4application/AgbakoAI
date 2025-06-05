from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class AIRequestLog(Base):
    __tablename__ = "ai_request_logs"
    id = Column(Integer, primary_key=True, index=True)
    symptom = Column(String, index=True)
    treatment = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
