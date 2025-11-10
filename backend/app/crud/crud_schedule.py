from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import date, timedelta

from app.models import schedule as models
from app.schemas import schedule as schemas


# --- CRUD для справочников ВУЗа ---
def create_group(db: Session, name: str, university_id: int) -> models.Group:
    db_obj = models.Group(name=name, university_id=university_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_teacher(db: Session, full_name: str, university_id: int) -> models.Teacher:
    db_obj = models.Teacher(full_name=full_name, university_id=university_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_subject(db: Session, name: str, university_id: int) -> models.Subject:
    db_obj = models.Subject(name=name, university_id=university_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_all_groups(db: Session, university_id: int) -> List[models.Group]:
    return db.query(models.Group).filter(models.Group.university_id == university_id).order_by(models.Group.name).all()


def get_all_teachers(db: Session, university_id: int) -> List[models.Teacher]:
    return db.query(models.Teacher).filter(models.Teacher.university_id == university_id).order_by(
        models.Teacher.full_name).all()


def get_all_subjects(db: Session, university_id: int) -> List[models.Subject]:
    return db.query(models.Subject).filter(models.Subject.university_id == university_id).order_by(
        models.Subject.name).all()


# --- CRUD для расписания ---
def get_schedule_events(
        db: Session, university_id: int, group_id: Optional[int] = None, teacher_id: Optional[int] = None,
        start_date: Optional[date] = None, end_date: Optional[date] = None,
) -> List[models.ScheduleEvent]:
    query = db.query(models.ScheduleEvent).filter(models.ScheduleEvent.university_id == university_id)
    if group_id:
        query = query.filter(models.ScheduleEvent.group_id == group_id)
    if teacher_id:
        query = query.filter(models.ScheduleEvent.teacher_id == teacher_id)
    if start_date:
        query = query.filter(models.ScheduleEvent.start_time >= start_date)
    if end_date:
        query = query.filter(models.ScheduleEvent.start_time < (end_date + timedelta(days=1)))
    return query.order_by(models.ScheduleEvent.start_time).all()


def create_schedule_event(db: Session, event: schemas.ScheduleEventCreate, university_id: int) -> models.ScheduleEvent:
    db_event = models.ScheduleEvent(**event.model_dump(), university_id=university_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def update_schedule_event(db: Session, event_id: int, event_update: schemas.ScheduleEventCreate, university_id: int) -> \
Optional[models.ScheduleEvent]:
    db_event = db.query(models.ScheduleEvent).filter(models.ScheduleEvent.id == event_id,
                                                     models.ScheduleEvent.university_id == university_id).first()
    if db_event:
        update_data = event_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
    return db_event


def delete_schedule_event(db: Session, event_id: int, university_id: int) -> Optional[models.ScheduleEvent]:
    db_event = db.query(models.ScheduleEvent).filter(models.ScheduleEvent.id == event_id,
                                                     models.ScheduleEvent.university_id == university_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event
