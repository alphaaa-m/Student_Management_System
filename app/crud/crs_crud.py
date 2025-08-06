from sqlalchemy.orm import Session
from app.models import crs as crs_mod
from app.schemas import crs_schema as crs_sch


def get_course(db: Session, course_id: int):
    """search a course by its ID."""
    return db.query(crs_mod.Course).filter(crs_mod.Course.crs_id == course_id).first()

def get_course_by_code(db: Session, course_code: str):
    """search a course by its unique code."""
    return db.query(crs_mod.Course).filter(crs_mod.Course.crs_code == course_code).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    """search a list of courses with pagination."""
    return db.query(crs_mod.Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: crs_sch.CourseCreate):
    """create a new course in the database."""
    db_course = crs_mod.Course(
        crs_title=course.crs_title,
        crs_code=course.crs_code,
        credits=course.credits,
        department=course.department
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course_update: crs_sch.CourseUpdate):
    """Updates an existing course's information."""
    db_course = get_course(db, course_id)
    if not db_course:
        return None

    if course_update.crs_title is not None:
        db_course.crs_title = course_update.crs_title
    if course_update.crs_code is not None:
        db_course.crs_code = course_update.crs_code
    if course_update.credits is not None:
        db_course.credits = course_update.credits
    if course_update.department is not None:
        db_course.department = course_update.department

    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    """Deletes a course by its ID."""
    db_course = get_course(db, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
        return True
    return False
