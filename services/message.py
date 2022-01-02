# Python
from sqlalchemy.orm import Session
# App
import models
import services
import schemas


def get_message(db: Session, message_id: str):
    db_message = db.query(models.Message).filter(
        models.Message.message_id == message_id).first()
    if db_message:
        return db_message
    return None


def get_message_by_user(db: Session, user_id: str):
    return db.query(models.Message).filter(models.Message.user_id == user_id)


def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).offset(skip).limit(limit).all()


def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(**message.dict())
    db_user = services.get_user(db, message.user_id)
    if db_user:
        db_message.user = db_user
        db.add(db_message)
        db.commit()
        db.refresh(db_message)
        return db_message
    return None


def delete_message(db: Session, message_id: str):
    db_message = get_message(db, message_id)
    if db_message:
        db.delete(db_message)
        db.commit()
        return f"Message '{db_message.content}' deleted"
    return None


def update_message(db: Session, message: schemas.MessageUpdate):
    db_message = db.query(models.Message).filter(
        models.Message.message_id == message.message_id)
    if db_message:
        db_message.update(message.dict())
        db.commit()
        return get_message(db, message.message_id)
    return None
