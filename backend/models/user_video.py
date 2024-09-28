from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db import Base



class UserVideo(Base):
    __tablename__ = "user_video"
    id = Column(Integer, primary_key=True, index=True)

    cookies = Column(String, ForeignKey("users.cookies"))
    video_id = Column(String, ForeignKey("videos.id_hash"))
    mark = Column(Integer)

    owner = relationship("User", back_populates="user_video")
    video = relationship("Video", back_populates="user_video")
    

