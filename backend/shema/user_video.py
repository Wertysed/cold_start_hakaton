from pydantic import BaseModel

class UserVideoIn(BaseModel):

    video_id: str
    cookies: str 
    mark: int



