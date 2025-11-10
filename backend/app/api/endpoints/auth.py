from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.core.security import create_access_token, verify_password
from app.crud import crud_user
from app.schemas.token import Token

router = APIRouter()


@router.post("/token", response_model=Token)
def login_for_access_token(
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user = crud_user.get_user_by_username(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_data = {"sub": user.username, "uni_id": user.university_id}
    access_token = create_access_token(subject_data=token_data)
    return {"access_token": access_token, "token_type": "bearer"}
