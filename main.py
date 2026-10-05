from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models

from schemas import (
    UserInput,
    UserRegister,
    UserLogin
)

from auth import (
    hash_password,
    verify_password,
    create_access_token
)

from prediction import predict_emotion
from recommendation import get_recommendation

# ----------------------------------------
# Create Database Tables
# ----------------------------------------
models.Base.metadata.create_all(bind=engine)

# ----------------------------------------
# FastAPI App
# ----------------------------------------
app = FastAPI(title="AI Mental Health Support Bot")

# ----------------------------------------
# CORS Configuration
# ----------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------
# Database Session
# ----------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------------------------
# Home Route
# ----------------------------------------
@app.get("/")
def home():
    return {
        "message": "Mental Health AI Backend is Running"
    }


# ----------------------------------------
# Register User
# ----------------------------------------
@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = (
        db.query(models.User)
        .filter(models.User.email == user.email)
        .first()
    )

    if existing_user:
        return {
            "message": "Email already registered"
        }

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Registration successful"
    }


# ----------------------------------------
# Login User
# ----------------------------------------
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = (
        db.query(models.User)
        .filter(models.User.email == user.email)
        .first()
    )

    if not db_user:
        return {
            "message": "Invalid email or password"
        }

    if not verify_password(
        user.password,
        db_user.password
    ):
        return {
            "message": "Invalid email or password"
        }

    access_token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ----------------------------------------
# Predict Emotion
# ----------------------------------------
@app.post("/predict")
def predict(data: UserInput, db: Session = Depends(get_db)):

    emotion = predict_emotion(data.text)

    recommendation = get_recommendation(emotion)

    # Save prediction into SQLite
    history = models.EmotionHistory(
        user_id=1,  # Temporary until JWT user integration
        user_text=data.text,
        predicted_emotion=emotion,
        recommendation=recommendation["message"]
    )

    db.add(history)
    db.commit()

    return {
        "user_text": data.text,
        "predicted_emotion": emotion,
        "recommendation": recommendation
    }


# ----------------------------------------
# Get History
# ----------------------------------------
@app.get("/history")
def get_history(db: Session = Depends(get_db)):

    history = (
        db.query(models.EmotionHistory)
        .order_by(models.EmotionHistory.created_at.desc())
        .all()
    )

    return history