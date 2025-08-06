from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models import enr as enr_mod 
from app.models import std as std_mod 
from app.models import crs as crs_mod 
from app.schemas import enr_schema as enr_sch


def get_enrollment(db: Session, enrollment_id: int):
    """search an enrollment by its ID."""
    return db.query(enr_mod.Enrollment).filter(enr_mod.Enrollment.enr_id == enrollment_id).first()

def get_enrollments(db: Session, skip: int = 0, limit: int = 100):
    """search a list of enrollments with pagination."""
    return db.query(enr_mod.Enrollment).offset(skip).limit(limit).all()

def create_enrollment(db: Session, enrollment: enr_sch.EnrollmentCreate):
    """
    Creates a new enrollment.
    Checks if student and course exist before creating.
    """
    student_exists = db.query(std_mod.Student).filter(std_mod.Student.std_id == enrollment.std_id).first()
    course_exists = db.query(crs_mod.Course).filter(crs_mod.Course.crs_id == enrollment.crs_id).first()

    if not student_exists:
        return {"error": "Student not found"}
    if not course_exists:
        return {"error": "Course not found"}

    existing_enrollment = db.query(enr_mod.Enrollment).filter( 
        and_(
            enr_mod.Enrollment.std_id == enrollment.std_id, 
            enr_mod.Enrollment.crs_id == enrollment.crs_id 
        )
    ).first()
    if existing_enrollment:
        return {"error": "Student already enrolled in this course"}

    db_enrollment = enr_mod.Enrollment(
        std_id=enrollment.std_id,
        crs_id=enrollment.crs_id
    )
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def delete_enrollment(db: Session, enrollment_id: int):
    """delete an enrollment by its ID."""
    db_enrollment = get_enrollment(db, enrollment_id)
    if db_enrollment:
        db.delete(db_enrollment)
        db.commit()
        return True
    return False

def get_student_courses(db: Session, student_id: int):
    """list all courses a specific student is enrolled in."""
    student = db.query(std_mod.Student).filter(std_mod.Student.std_id == student_id).first()
    if not student:
        return None
    return [enrollment.course for enrollment in student.enrollments]

def get_course_students(db: Session, course_id: int):
    """Lists all students enrolled in a specific course."""
    course = db.query(crs_mod.Course).filter(crs_mod.Course.crs_id == course_id).first()
    if not course:
        return None
    return [enrollment.student for enrollment in course.enrollments]