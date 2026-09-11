from datetime import datetime
from pydantic import BaseModel, EmailStr
from src.models.models import TaskPriority, TaskStatus, UserRole


# --- USER SCHEMAS ---
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True


# --- AUTH SCHEMAS ---
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None