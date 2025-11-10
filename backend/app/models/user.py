import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class UserRole(str, enum.Enum):
    SUPER_ADMIN = "super_admin"
    UNIVERSITY_ADMIN = "university_admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    # university_id может быть NULL (только для Супер-Админа)
    university_id = Column(Integer, ForeignKey("universities.id"), nullable=True)
    university = relationship("University")
