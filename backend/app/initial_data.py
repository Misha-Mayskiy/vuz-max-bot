from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.crud import crud_user
from app.schemas.user import UserCreate
from app.core.config import settings
from app.models.user import UserRole


def create_first_superuser():
    db: Session = SessionLocal()
    user = crud_user.get_user_by_username(db, username=settings.FIRST_SUPERUSER_USERNAME)
    if not user:
        user_in = UserCreate(
            username=settings.FIRST_SUPERUSER_USERNAME,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            role=UserRole.SUPER_ADMIN,
            university_id=None
        )
        crud_user.create_user(db=db, user=user_in)
        print("First superuser created")
    db.close()
