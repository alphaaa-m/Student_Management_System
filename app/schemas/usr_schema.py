from pydantic import BaseModel, Field
from typing import Optional


class UserBase(BaseModel):
    usr_name: str = Field(..., min_length=3, max_length=50)
    usr_is_admin: bool = False
    usr_is_active: bool = True

class UserCreate(UserBase):
    usr_password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    usr_name: str
    usr_password: str

class UserUpdate(BaseModel):
    usr_name: Optional[str] = Field(None, min_length=3, max_length=50)
    usr_password: Optional[str] = Field(None, min_length=6)
    usr_is_admin: Optional[bool] = None
    usr_is_active: Optional[bool] = None

class UserResponse(UserBase):
    usr_id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: Optional[str] = None