from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.crud import crud_user, crud_schedule
from app.schemas.user import UserCreate
from app.models import schedule as models
from app.core.config import settings


def create_first_superuser():
    db: Session = SessionLocal()
    user = crud_user.get_user_by_username(db, username=settings.FIRST_SUPERUSER_USERNAME)
    if not user:
        user_in = UserCreate(
            username=settings.FIRST_SUPERUSER_USERNAME,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_admin=True,
        )
        crud_user.create_user(db=db, user=user_in)
        print("First superuser created")

        create_test_data(db)
    else:
        if not db.query(models.Group).first():
            create_test_data(db)
            print("Test data created")

    db.close()


def create_test_data(db: Session):
    # Groups
    group1 = models.Group(name="ИКБО-01-23")
    group2 = models.Group(name="ИНБО-02-23")
    db.add_all([group1, group2])
    db.commit()

    # Teachers
    teacher1 = models.Teacher(full_name="Иванов Иван Иванович")
    teacher2 = models.Teacher(full_name="Петров Петр Петрович")
    db.add_all([teacher1, teacher2])
    db.commit()

    # Subjects
    subject1 = models.Subject(name="Программирование на Python")
    subject2 = models.Subject(name="Базы данных")
    db.add_all([subject1, subject2])
    db.commit()
    print("Test groups, teachers, and subjects added.")
