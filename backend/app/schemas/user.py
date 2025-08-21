from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=255)
    role: str = Field(default='contributor', pattern='^(owner|admin|pm|contributor|viewer)$')

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
    team_name: str = Field(..., min_length=1, max_length=255)

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    avatar: Optional[str] = None
    role: Optional[str] = Field(None, pattern='^(owner|admin|pm|contributor|viewer)$')
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: UUID
    avatar: Optional[str] = None
    is_active: bool
    is_verified: bool
    team_id: UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class UserInDB(UserResponse):
    hashed_password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
