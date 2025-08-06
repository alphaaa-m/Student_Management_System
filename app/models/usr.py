from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database.db import Base

class User(Base):
    __tablename__ = "users"

    usr_id = Column(Integer, primary_key=True, index=True)
    usr_name = Column(String, unique=True, index=True, nullable=False)
    usr_password = Column(String, nullable=False)
    usr_is_admin = Column(Boolean, default=False) 
    usr_is_active = Column(Boolean, default=True)

    student = relationship("Student", back_populates="user", uselist=False)