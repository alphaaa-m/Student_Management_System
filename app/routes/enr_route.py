from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud import enr_crud
from app.schemas import enr_schema
from app.database.db import get_db
from app.auth.scrty import get_current_user, get_admin_user
from app.models.usr import User

router = APIRouter(
    prefix="/enrollments",
    tags=["enrollments"],
)

@router.post("/", response_model=enr_schema.EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def create_enrollment_record(
    enrollment: enr_schema.EnrollmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):

    db_enrollment = enr_crud.create_enrollment(db=db, enrollment=enrollment)

    if isinstance(db_enrollment, dict) and "error" in db_enrollment:
        if db_enrollment["error"] == "Student not found":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        if db_enrollment["error"] == "Course not found":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
        if db_enrollment["error"] == "Student already enrolled in this course":
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Student is already enrolled in this course")
    
    return db_enrollment

@router.get("/", response_model=List[enr_schema.EnrollmentResponse])
def read_enrollments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    enrollments = enr_crud.get_enrollments(db, skip=skip, limit=limit)
    return enrollments

@router.get("/{enrollment_id}", response_model=enr_schema.EnrollmentResponse)
def read_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db_enrollment = enr_crud.get_enrollment(db, enrollment_id=enrollment_id)
    if db_enrollment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found")
    return db_enrollment

@router.delete("/{enrollment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_enrollment_record(
    enrollment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):

    deleted = enr_crud.delete_enrollment(db, enrollment_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found")
    return {"ok": True}
