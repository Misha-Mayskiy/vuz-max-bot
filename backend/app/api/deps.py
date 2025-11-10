from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal
from app.models.user import User, UserRole
from app.crud import crud_user
from app.schemas.token import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        uni_id: int | None = payload.get("uni_id")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username, uni_id=uni_id)
    except JWTError:
        raise credentials_exception

    user = crud_user.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception

    if user.university_id != token_data.uni_id:
        raise credentials_exception

    return user


def get_current_super_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != UserRole.SUPER_ADMIN:
        raise HTTPException(status_code=403, detail="Super admin privileges required")
    return current_user


def get_current_university_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != UserRole.UNIVERSITY_ADMIN:
        raise HTTPException(status_code=403, detail="University admin privileges required")
    if not current_user.university_id:
        raise HTTPException(status_code=403, detail="Admin is not assigned to a university")
    return current_user
