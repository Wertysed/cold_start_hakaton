from pydantic import BaseModel

class Video(BaseModel):
    video_id: str
    title: str
    description: str



class Videos(BaseModel):
    videos: list[Video]


class VideosIn(Videos):
    cookies: str

class VideosOut(Videos):
    pass

