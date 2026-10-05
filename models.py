from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from database import Base


# -----------------------------
# User Table
# -----------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    password = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# -----------------------------
# Emotion History Table
# -----------------------------
class EmotionHistory(Base):

    __tablename__ = "emotion_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    user_text = Column(String, nullable=False)

    predicted_emotion = Column(String, nullable=False)

    recommendation = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )