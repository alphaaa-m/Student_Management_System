from sqlalchemy.orm import Session
from app.models import std as std_mod
from app.schemas import std_schema as std_sch


def get_student(db: Session, student_id: int):
    """search student by their ID."""
    return db.query(std_mod.Student).filter(std_mod.Student.std_id == student_id).first()

def get_student_by_email(db: Session, email: str):
    """search a student by their email address."""
    return db.query(std_mod.Student).filter(std_mod.Student.std_email == email).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    """search a list of students with pagination."""
    return db.query(std_mod.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: std_sch.StudentCreate):
    """create a new student in the database."""
    db_student = std_mod.Student(
        std_name=student.std_name,
        std_email=student.std_email,
        department=student.department,
        user_id=student.user_id
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student_update: std_sch.StudentUpdate):
    """update an existing student's information."""
    db_student = get_student(db, student_id)
    if not db_student:
        return None

    if student_update.std_name is not None:
        db_student.std_name = student_update.std_name
    if student_update.std_email is not None:
        db_student.std_email = student_update.std_email
    if student_update.department is not None:
        db_student.department = student_update.department
    if student_update.user_id is not None:
        db_student.user_id = student_update.user_id

    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    """delete student"""
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    return False