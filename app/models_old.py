from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # নতুন ফিল্ডস (ট্রায়াল এবং প্রিমিয়ামের জন্য)
    is_premium = Column(Boolean, default=False)
    trial_end_date = Column(DateTime(timezone=True), nullable=True)

class ContentGeneration(Base):
    __tablename__ = "generations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    prompt = Column(String)
    result = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
