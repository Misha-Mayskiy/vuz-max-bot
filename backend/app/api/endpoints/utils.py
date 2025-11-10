from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import crud_schedule
from app.schemas import schedule as schemas

router = APIRouter()


@router.get("/groups", response_model=List[schemas.Group])
def read_groups(db: Session = Depends(deps.get_db)):
    """Получить список всех групп."""
    return crud_schedule.get_all_groups(db)


@router.get("/teachers", response_model=List[schemas.Teacher])
def read_teachers(db: Session = Depends(deps.get_db)):
    """Получить список всех преподавателей."""
    return crud_schedule.get_all_teachers(db)


@router.get("/subjects", response_model=List[schemas.Subject])
def read_subjects(db: Session = Depends(deps.get_db)):
    """Получить список всех предметов."""
    return crud_schedule.get_all_subjects(db)
