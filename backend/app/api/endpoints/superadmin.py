from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_university, crud_user
from app.schemas.university import University, UniversityCreate
from app.schemas.user import UserCreate, UserInDB
from app.models.user import User, UserRole

router = APIRouter()


@router.post("/universities/", response_model=University)
def create_new_university(
        university_in: UniversityCreate,
        db: Session = Depends(deps.get_db),
        super_admin: User = Depends(deps.get_current_super_admin)
):
    return crud_university.create_university(db, name=university_in.name)


@router.post("/users/", response_model=UserInDB)
def create_new_user(
        user_in: UserCreate,
        db: Session = Depends(deps.get_db),
        super_admin: User = Depends(deps.get_current_super_admin)
):
    if user_in.role == UserRole.UNIVERSITY_ADMIN and not user_in.university_id:
        raise HTTPException(status_code=422, detail="University admin must be assigned to a university.")

    if user_in.role == UserRole.SUPER_ADMIN:
        user_in.university_id = None

    return crud_user.create_user(db, user=user_in)
