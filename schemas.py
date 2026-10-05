from pydantic import BaseModel, EmailStr


# -----------------------------
# Prediction Schemas
# -----------------------------
class UserInput(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    user_text: str
    predicted_emotion: str
    recommendation: dict


# -----------------------------
# Authentication Schemas
# -----------------------------
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True