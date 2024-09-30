from fastapi import Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from repositories.user_video import UserVideoRepository
from repositories.users import UserRepository
from repositories.video import VideoRepository
from services.user_video import UserVideoService
from services.users import UserService
from services.video import VideoService


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))

def user_video_services(db: Session = Depends(get_db)):
    return UserVideoService(UserVideoRepository(db), UserRepository(db), VideoRepository(db))

def video_service(db: Session = Depends(get_db)):
    return VideoService(VideoRepository(db))

