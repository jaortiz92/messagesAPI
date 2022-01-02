from sqlalchemy import (
    Boolean, Column, ForeignKey,
    Integer, String, Date)
from sqlalchemy.orm import relationship

from config import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)

    messages = relationship("Message", back_populates="user")
