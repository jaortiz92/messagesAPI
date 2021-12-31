from sqlalchemy import (
    Column, ForeignKey,
    String, DateTime)
from sqlalchemy.orm import relationship

from config import Base


class Message(Base):
    __tablename__ = "messages"

    message_id = Column(String, primary_key=True, index=True)
    create_at = Column(DateTime)
    update_at = Column(DateTime)

    user_id = Column(String, ForeignKey("users.user_id"))
    user = relationship("User", back_populates="messages")
