from __future__ import annotations
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class StudentBase(BaseModel):
    std_name: str = Field(..., min_length=2, max_length=100)
    std_email: EmailStr = Field(...)
    department: Optional[str] = Field(None, max_length=100)

class StudentCreate(StudentBase):
    user_id: Optional[int] = None 

class StudentUpdate(BaseModel):
    std_name: Optional[str] = Field(None, min_length=2, max_length=100)
    std_email: Optional[EmailStr] = None
    department: Optional[str] = Field(None, max_length=100)
    user_id: Optional[int] = None

class EnrollmentResponseForStudent(BaseModel):
    enr_id: int
    crs_id: int
    enr_date: datetime

    class Config:
        from_attributes = True

class UserResponseForStudent(BaseModel):
    usr_id: int
    usr_name: str

    class Config:
        from_attributes = True

class StudentResponse(StudentBase):
    std_id: int
    user: Optional[UserResponseForStudent] = None
    enrollments: List[EnrollmentResponseForStudent] = []

    class Config:
        from_attributes = True




class StudentResponseForEnrollment(BaseModel):
    std_id: int
    std_name: str
    std_email: EmailStr
    department: Optional[str] = None
    
    class Config:
        from_attributes = True