from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    is_admin: bool = False


class UserInDB(UserBase):
    id: int
    is_admin: bool

    class Config:
        from_attributes = True
