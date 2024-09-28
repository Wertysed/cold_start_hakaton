from fastapi import FastAPI, Body, Depends
from typing import Annotated
from db import Base, engine, SessionLocal 
from shema.video import VideosIn, VideosOut, Video
from depend import user_service, user_video_services, video_service
from services.users import UserService
from services.user_video import UserVideoService
from shema.user_video import UserVideoIn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
Base.metadata.create_all(bind=engine)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def hello():
    return {"hello": "Man"}


@app.post("/get_video", response_model=list[Video])
def get_video(checked_video: list[UserVideoIn], user_video_services: Annotated[UserVideoService, Depends(user_video_services)]):
    res = []
    for i in user_video_services.get_videos(checked_video):
        i = UserVideoIn.model_validate(i, from_attributes=True) 
        print(i.model_dump())
        new_video = Video(**i.model_dump(), title="Pashel", description="Ti che ne ponual")
        res.append(new_video)

    return res


