from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import date

from app.models import schedule as models
from app.schemas import schedule as schemas


def get_all_groups(db: Session) -> List[models.Group]:
    return db.query(models.Group).order_by(models.Group.name).all()


def get_all_teachers(db: Session) -> List[models.Teacher]:
    return db.query(models.Teacher).order_by(models.Teacher.full_name).all()


def get_all_subjects(db: Session) -> List[models.Subject]:
    return db.query(models.Subject).order_by(models.Subject.name).all()


def get_schedule_events(
        db: Session,
        group_id: Optional[int] = None,
        teacher_id: Optional[int] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
) -> List[models.ScheduleEvent]:
    query = db.query(models.ScheduleEvent)
    if group_id:
        query = query.filter(models.ScheduleEvent.group_id == group_id)
    if teacher_id:
        query = query.filter(models.ScheduleEvent.teacher_id == teacher_id)
    if start_date:
        query = query.filter(models.ScheduleEvent.start_time >= start_date)
    if end_date:
        query = query.filter(models.ScheduleEvent.start_time < (end_date + timedelta(days=1)))

    return query.order_by(models.ScheduleEvent.start_time).all()


def create_schedule_event(db: Session, event: schemas.ScheduleEventCreate) -> models.ScheduleEvent:
    db_event = models.ScheduleEvent(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def update_schedule_event(db: Session, event_id: int, event_update: schemas.ScheduleEventCreate) -> Optional[
    models.ScheduleEvent]:
    db_event = db.query(models.ScheduleEvent).filter(models.ScheduleEvent.id == event_id).first()
    if db_event:
        update_data = event_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
    return db_event


def delete_schedule_event(db: Session, event_id: int) -> Optional[models.ScheduleEvent]:
    db_event = db.query(models.ScheduleEvent).filter(models.ScheduleEvent.id == event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event
