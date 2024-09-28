from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    cookies = Column(String, unique=True)

    user_video = relationship("UserVideo", back_populates="owner")

