from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    university_id = Column(Integer, ForeignKey("universities.id"), nullable=False)
    __table_args__ = (UniqueConstraint('name', 'university_id', name='_name_university_uc'),)


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True, nullable=False)
    university_id = Column(Integer, ForeignKey("universities.id"), nullable=False)


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    university_id = Column(Integer, ForeignKey("universities.id"), nullable=False)


class ScheduleEvent(Base):
    __tablename__ = "schedule_events"
    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    classroom = Column(String)

    subject_id = Column(Integer, ForeignKey("subjects.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
    university_id = Column(Integer, ForeignKey("universities.id"), nullable=False)

    subject = relationship("Subject")
    teacher = relationship("Teacher")
    group = relationship("Group")
