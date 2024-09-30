from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    id_hash = Column(String, unique=True)

    title = Column(String)
    description = Column(String)

    user_video = relationship("UserVideo", back_populates="video")

