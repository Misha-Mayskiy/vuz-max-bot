from sqlalchemy.orm import declarative_base

from app.models.user import User
from app.models.schedule import Group, Teacher, Subject, ScheduleEvent

Base = declarative_base()
