from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import crs_crud, enr_crud
from app.schemas import crs_schema, std_schema
from app.database.db import get_db
from app.auth.scrty import get_current_user, get_admin_user
from app.models.usr import User

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
)

@router.post("/", response_model=crs_schema.CourseResponse, status_code=status.HTTP_201_CREATED)
def create_new_course(
    course: crs_schema.CourseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    
    db_course = crs_crud.get_course_by_code(db, course_code=course.crs_code)
    if db_course:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course with this code already exists"
        )
    return crs_crud.create_course(db=db, course=course)

@router.get("/", response_model=List[crs_schema.CourseResponse])
def read_courses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    courses = crs_crud.get_courses(db, skip=skip, limit=limit)
    return courses

@router.get("/{course_id}", response_model=crs_schema.CourseResponse)
def read_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    db_course = crs_crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return db_course

@router.put("/{course_id}", response_model=crs_schema.CourseResponse)
def update_course_data(
    course_id: int,
    course: crs_schema.CourseUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    
    db_course = crs_crud.update_course(db, course_id, course)
    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return db_course

@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course_data(
    course_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    
    deleted = crs_crud.delete_course(db, course_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return {"ok": True}

@router.get("/{course_id}/students", response_model=List[std_schema.StudentResponseForEnrollment])
def read_course_students(
    course_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    students = enr_crud.get_course_students(db, course_id)
    if students is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return students
