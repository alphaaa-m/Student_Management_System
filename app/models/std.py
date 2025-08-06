from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database.db import Base


class Student(Base):
    __tablename__ = "students"

    std_id = Column(Integer, primary_key=True, index=True)
    std_name = Column(String, nullable=False)
    std_email=Column(String, unique= True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.usr_id"), nullable=True)
    department=Column(String, nullable=True)

    enrollments = relationship("Enrollment", back_populates="student")
    user = relationship("User", back_populates="student")
