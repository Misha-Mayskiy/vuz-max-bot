from typing import List, Optional
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import crud_schedule
from app.schemas import schedule as schemas
from app.models.user import User

router = APIRouter()


@router.get("/", response_model=List[schemas.ScheduleEvent])
def read_schedule(
        group_id: Optional[int] = None,
        teacher_id: Optional[int] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        db: Session = Depends(deps.get_db)
):
    """
    Получить отфильтрованный список событий в расписании.
    Доступно всем аутентифицированным пользователям.
    """
    events = crud_schedule.get_schedule_events(
        db, group_id, teacher_id, start_date, end_date
    )
    return events


@router.post("/", response_model=schemas.ScheduleEvent, status_code=status.HTTP_201_CREATED)
def create_event(
        event: schemas.ScheduleEventCreate,
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_admin_user)
):
    """
    Создать новое событие в расписании.
    Только для администраторов.
    """
    return crud_schedule.create_schedule_event(db=db, event=event)


@router.put("/{event_id}", response_model=schemas.ScheduleEvent)
def update_event(
        event_id: int,
        event_update: schemas.ScheduleEventCreate,
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_admin_user)
):
    """
    Обновить событие в расписании по ID.
    Только для администраторов.
    """
    db_event = crud_schedule.update_schedule_event(db, event_id, event_update)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(
        event_id: int,
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_admin_user)
):
    """
    Удалить событие из расписания по ID.
    Только для администраторов.
    """
    deleted_event = crud_schedule.delete_schedule_event(db, event_id)
    if deleted_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return
