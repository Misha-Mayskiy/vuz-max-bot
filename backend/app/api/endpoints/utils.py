from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.api import deps
from app.crud import crud_schedule
from app.schemas import schedule as schemas
from app.models.user import User

router = APIRouter()


@router.get("/schedule/", response_model=List[schemas.ScheduleEvent])
def read_schedule(
        group_id: Optional[int] = None, teacher_id: Optional[int] = None, start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_user)
):
    if not current_user.university_id:
        return []
    events = crud_schedule.get_schedule_events(
        db, university_id=current_user.university_id, group_id=group_id, teacher_id=teacher_id, start_date=start_date,
        end_date=end_date
    )
    return events


@router.get("/groups", response_model=List[schemas.Group])
def read_groups(db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)):
    if not current_user.university_id: return []
    return crud_schedule.get_all_groups(db, university_id=current_user.university_id)


@router.get("/teachers", response_model=List[schemas.Teacher])
def read_teachers(db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)):
    if not current_user.university_id: return []
    return crud_schedule.get_all_teachers(db, university_id=current_user.university_id)


@router.get("/subjects", response_model=List[schemas.Subject])
def read_subjects(db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)):
    if not current_user.university_id: return []
    return crud_schedule.get_all_subjects(db, university_id=current_user.university_id)
