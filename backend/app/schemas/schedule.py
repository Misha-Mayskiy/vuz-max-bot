from pydantic import BaseModel
from datetime import datetime


class GroupBase(BaseModel):
    name: str


class Group(GroupBase):
    id: int

    class Config:
        from_attributes = True


class TeacherBase(BaseModel):
    full_name: str


class Teacher(TeacherBase):
    id: int

    class Config:
        from_attributes = True


class SubjectBase(BaseModel):
    name: str


class Subject(SubjectBase):
    id: int

    class Config:
        from_attributes = True


class ScheduleEventBase(BaseModel):
    start_time: datetime
    end_time: datetime
    classroom: str
    subject_id: int
    teacher_id: int
    group_id: int


class ScheduleEventCreate(ScheduleEventBase):
    pass


class ScheduleEvent(ScheduleEventBase):
    id: int
    subject: Subject
    teacher: Teacher
    group: Group

    class Config:
        from_attributes = True
