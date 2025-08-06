from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database.db import Base

class Course(Base):
    __tablename__ = "courses"

    crs_id = Column(Integer, primary_key=True, index=True)
    crs_title = Column(String, nullable=False, unique=True, index=True)
    crs_code = Column(String, unique=True, nullable=False, index=True)
    credits= Column(Numeric, nullable=False)
    department= Column(String, nullable=True)

    enrollments = relationship("Enrollment", back_populates="course")
