from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode, user
import models
import services
import schemas


def get_message(db: Session, message_id: str):
    return db.query(models.Message).filter(models.Message.message_id == message_id).first()


def get_message_by_user(db: Session, user_id: str):
    return db.query(models.Message).filter(models.Message.user_id == user_id)


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
    db_message = db.query(models.Message).filter(
        models.Message.message_id == message_id).first()
    db.delete(db_message)
    db.commit()
    return f"User {db_message.content} deleted"


def update_message(db: Session, message: schemas.MessageUpdate):
    db.query(models.Message).filter(
        models.Message.message_id == message.message_id).update(**user)
    db.commit
    return get_message(db, message.message_id)
