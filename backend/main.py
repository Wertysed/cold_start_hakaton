from fastapi import FastAPI, Body, Depends, Cookie
from typing import Annotated
from db import Base, engine, SessionLocal 
from shema.video import VideoDB, Video
from depend import user_service, user_video_services, video_service
from services.users import UserService
from services.user_video import UserVideoService
from services.video import VideoService
from shema.user_video import UserVideoIn, UserVideoFront
from shema.cookies import Cookies
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from data_make import connect,  execute_many
from config import (
    DB_HOST,
    DB_NAME,
    DB_PASS,
    DB_USER,
    DB_PORT
)

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

param_dic = {
    "host"      : DB_HOST ,
    "database"  : DB_NAME,
    "user"      : DB_USER, 
    "password"  : DB_PASS 
}


df = pd.read_csv('video_stat.csv')
df.columns = [c.lower() for c in df.columns]
df = df.rename(columns={"video_id": "id_hash"})
arr = [c for c in df.columns if c!="id_hash" and c!="title" and c!="description" ]
df = df.drop(columns=arr)

conn = connect(param_dic)
execute_many(conn, df, 'videos')


@app.get("/")
def hello():
    return {"hello": "Man"}


@app.post("/get_video", response_model=list[Video])
def get_video(cookies: Annotated[Cookies, Cookie()], checked_video: list[UserVideoFront], user_video_services: Annotated[UserVideoService, Depends(user_video_services)]):
    res = []
    checked_video: list[UserVideoIn] = [UserVideoIn(**video.model_dump(), cookies=cookies.session_id) for video in checked_video]
    for i in user_video_services.get_videos(cookies.session_id, checked_video):
        print(i)

        i = VideoDB.model_validate(i, from_attributes=True) 
        i = Video(**i.model_dump(), video_id=i.id_hash)
        res.append(i)

    return res


