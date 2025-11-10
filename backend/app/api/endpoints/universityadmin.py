from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_schedule
from app.schemas import schedule as schemas
from app.models.user import User

router = APIRouter()


@router.post("/groups/", response_model=schemas.Group)
def create_new_group(
        group_in: schemas.GroupBase,
        db: Session = Depends(deps.get_db),
        uni_admin: User = Depends(deps.get_current_university_admin)
):
    return crud_schedule.create_group(db, name=group_in.name, university_id=uni_admin.university_id)


@router.post("/teachers/", response_model=schemas.Teacher)
def create_new_teacher(
        teacher_in: schemas.TeacherBase,
        db: Session = Depends(deps.get_db),
        uni_admin: User = Depends(deps.get_current_university_admin)
):
    return crud_schedule.create_teacher(db, full_name=teacher_in.full_name, university_id=uni_admin.university_id)


@router.post("/subjects/", response_model=schemas.Subject)
def create_new_subject(
        subject_in: schemas.SubjectBase,
        db: Session = Depends(deps.get_db),
        uni_admin: User = Depends(deps.get_current_university_admin)
):
    return crud_schedule.create_subject(db, name=subject_in.name, university_id=uni_admin.university_id)
