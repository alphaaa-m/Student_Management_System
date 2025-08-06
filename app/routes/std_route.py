from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud import std_crud, enr_crud
from app.schemas import std_schema, crs_schema
from app.database.db import get_db
from app.auth.scrty import get_current_user, get_admin_user
from app.models.usr import User

router = APIRouter(
    prefix="/students",
    tags=["students"],
)

@router.post("/", response_model=std_schema.StudentResponse, status_code=status.HTTP_201_CREATED)
def create_new_student(
    student: std_schema.StudentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    db_student = std_crud.get_student_by_email(db, email=student.std_email)
    if db_student:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    return std_crud.create_student(db=db, student=student)

@router.get("/", response_model=List[std_schema.StudentResponse])
def read_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
 

    students = std_crud.get_students(db, skip=skip, limit=limit)
    return students

@router.get("/{student_id}", response_model=std_schema.StudentResponse)
def read_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db_student = std_crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return db_student

@router.put("/{student_id}", response_model=std_schema.StudentResponse)
def update_student_data(
    student_id: int,
    student: std_schema.StudentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):

    db_student = std_crud.update_student(db, student_id, student)
    if db_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return db_student

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student_data(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):

    deleted = std_crud.delete_student(db, student_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return {"ok": True}

@router.get("/{student_id}/courses", response_model=List[crs_schema.CourseResponseForEnrollment])
def read_student_courses(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    courses = enr_crud.get_student_courses(db, student_id)
    if courses is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return courses
