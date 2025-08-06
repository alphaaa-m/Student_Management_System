from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional, List
from decimal import Decimal
from datetime import datetime

class CourseBase(BaseModel):
    crs_title: str = Field(..., min_length=3, max_length=200)
    crs_code: str = Field(..., min_length=3, max_length=20, unique=True) 
    credits: Decimal = Field(..., gt=0, decimal_places=2)
    department: Optional[str] = Field(None, max_length=100)

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    crs_title: Optional[str] = Field(None, min_length=3, max_length=200)
    crs_code: Optional[str] = Field(None, min_length=3, max_length=20)
    credits: Optional[Decimal] = Field(None, gt=0, decimal_places=2)
    department: Optional[str] = Field(None, max_length=100)

class EnrollmentResponseForCourse(BaseModel):
    enr_id: int
    std_id: int
    enr_date: datetime

    class Config:
        from_attributes = True

class CourseResponse(CourseBase):
    crs_id: int
    enrollments: List[EnrollmentResponseForCourse] = []

    class Config:
        from_attributes = True



class CourseResponseForEnrollment(BaseModel):
    crs_id: int
    crs_title: str
    crs_code: str
    credits: Decimal

    class Config:
        from_attributes = True