from typing import List, Optional
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import crud_schedule
from app.schemas import schedule as schemas
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=schemas.ScheduleEvent, status_code=status.HTTP_201_CREATED)
def create_event(
        event: schemas.ScheduleEventCreate,
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_university_admin)
):
    return crud_schedule.create_schedule_event(db=db, event=event, university_id=current_user.university_id)


@router.put("/{event_id}", response_model=schemas.ScheduleEvent)
def update_event(
        event_id: int,
        event_update: schemas.ScheduleEventCreate,
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_university_admin)
):
    db_event = crud_schedule.update_schedule_event(db, event_id, event_update, university_id=current_user.university_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(
        event_id: int,
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_university_admin)
):
    deleted_event = crud_schedule.delete_schedule_event(db, event_id, university_id=current_user.university_id)
    if deleted_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return
