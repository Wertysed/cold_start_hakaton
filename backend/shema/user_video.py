from pydantic import BaseModel

class UserVideoIn(BaseModel):

    video_id: str
    cookies: str 
    mark: int


class UserVideoFront(BaseModel):

    video_id: str
    mark: int


