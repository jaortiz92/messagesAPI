from sqlalchemy.orm import Session
import models
import schemas


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserRegister):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: str):
    db_user = db.query(models.User).filter(
        models.User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return f"User {db_user.email} deleted"
    return None


def update_user(db: Session, user: schemas.User):
    db.query(models.User).filter(
        models.User.user_id == user.user_id).update(**user)
    db.commit
    return get_user(db, user.user_id)
