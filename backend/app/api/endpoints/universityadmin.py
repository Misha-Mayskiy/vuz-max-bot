from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_schedule
from app.schemas import schedule as schemas
from app.models.user import User

router = APIRouter()


# --- Управление группами ---
@router.post("/groups/", response_model=schemas.Group, status_code=status.HTTP_201_CREATED)
def create_new_group(group_in: schemas.GroupBase, db: Session = Depends(deps.get_db),
                     uni_admin: User = Depends(deps.get_current_university_admin)):
    return crud_schedule.create_group(db, name=group_in.name, university_id=uni_admin.university_id)


@router.put("/groups/{group_id}", response_model=schemas.Group)
def update_existing_group(group_id: int, group_in: schemas.GroupBase, db: Session = Depends(deps.get_db),
                          uni_admin: User = Depends(deps.get_current_university_admin)):
    updated_group = crud_schedule.update_group(db, group_id=group_id, university_id=uni_admin.university_id,
                                               name=group_in.name)
    if not updated_group:
        raise HTTPException(status_code=404, detail="Group not found")
    return updated_group


@router.delete("/groups/{group_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_group(group_id: int, db: Session = Depends(deps.get_db),
                          uni_admin: User = Depends(deps.get_current_university_admin)):
    deleted_group = crud_schedule.delete_group(db, group_id=group_id, university_id=uni_admin.university_id)
    if not deleted_group:
        raise HTTPException(status_code=404, detail="Group not found")
    return


# --- Управление преподавателями ---
@router.post("/teachers/", response_model=schemas.Teacher, status_code=status.HTTP_201_CREATED)
def create_new_teacher(teacher_in: schemas.TeacherBase, db: Session = Depends(deps.get_db),
                       uni_admin: User = Depends(deps.get_current_university_admin)):
    return crud_schedule.create_teacher(db, full_name=teacher_in.full_name, university_id=uni_admin.university_id)


@router.put("/teachers/{teacher_id}", response_model=schemas.Teacher)
def update_existing_teacher(teacher_id: int, teacher_in: schemas.TeacherBase, db: Session = Depends(deps.get_db),
                            uni_admin: User = Depends(deps.get_current_university_admin)):
    updated_teacher = crud_schedule.update_teacher(db, teacher_id=teacher_id, university_id=uni_admin.university_id,
                                                   full_name=teacher_in.full_name)
    if not updated_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return updated_teacher


@router.delete("/teachers/{teacher_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_teacher(teacher_id: int, db: Session = Depends(deps.get_db),
                            uni_admin: User = Depends(deps.get_current_university_admin)):
    deleted_teacher = crud_schedule.delete_teacher(db, teacher_id=teacher_id, university_id=uni_admin.university_id)
    if not deleted_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return


# --- Управление предметами ---
@router.post("/subjects/", response_model=schemas.Subject, status_code=status.HTTP_201_CREATED)
def create_new_subject(subject_in: schemas.SubjectBase, db: Session = Depends(deps.get_db),
                       uni_admin: User = Depends(deps.get_current_university_admin)):
    return crud_schedule.create_subject(db, name=subject_in.name, university_id=uni_admin.university_id)


@router.put("/subjects/{subject_id}", response_model=schemas.Subject)
def update_existing_subject(subject_id: int, subject_in: schemas.SubjectBase, db: Session = Depends(deps.get_db),
                            uni_admin: User = Depends(deps.get_current_university_admin)):
    updated_subject = crud_schedule.update_subject(db, subject_id=subject_id, university_id=uni_admin.university_id,
                                                   name=subject_in.name)
    if not updated_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return updated_subject


@router.delete("/subjects/{subject_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_subject(subject_id: int, db: Session = Depends(deps.get_db),
                            uni_admin: User = Depends(deps.get_current_university_admin)):
    deleted_subject = crud_schedule.delete_subject(db, subject_id=subject_id, university_id=uni_admin.university_id)
    if not deleted_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return
