from pydantic import BaseModel
from app.models.user import UserRole
from .university import University


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    role: UserRole
    university_id: int | None = None


class UserInDB(UserBase):
    id: int
    role: UserRole
    university: University | None = None

    class Config:
        from_attributes = True
