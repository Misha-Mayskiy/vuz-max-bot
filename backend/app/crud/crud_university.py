from sqlalchemy.orm import Session
from app.models.university import University


def create_university(db: Session, name: str) -> University:
    db_university = University(name=name)
    db.add(db_university)
    db.commit()
    db.refresh(db_university)
    return db_university
