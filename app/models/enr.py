from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.db import Base

class Enrollment(Base):
    __tablename__ = "enrollments"

    enr_id = Column(Integer, primary_key=True, index=True)
    std_id = Column(Integer, ForeignKey("students.std_id"), nullable=False, index=True)
    crs_id = Column(Integer, ForeignKey("courses.crs_id"), nullable=False, index=True)
    enr_date = Column(DateTime, default=func.now())

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")