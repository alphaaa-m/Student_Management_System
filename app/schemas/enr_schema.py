from __future__ import annotations
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class EnrollmentBase(BaseModel):
    std_id: int = Field(..., description="ID of the student to enroll")
    crs_id: int = Field(..., description="ID of the course to enroll in")

class EnrollmentCreate(EnrollmentBase):
    pass

class StudentResponseForEnrollment(BaseModel):
    std_id: int
    std_name: str
    std_email: EmailStr

    class Config:
        from_attributes = True

class CourseResponseForEnrollment(BaseModel):
    crs_id: int
    crs_title: str
    crs_code: str

    class Config:
        from_attributes = True

class EnrollmentResponse(EnrollmentBase):
    enr_id: int
    enr_date: datetime

    student: StudentResponseForEnrollment
    course: CourseResponseForEnrollment

    class Config:
        from_attributes = True