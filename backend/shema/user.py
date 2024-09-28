from pydantic import BaseModel

class UserDB(BaseModel):
    cookies: str

class UserIn(BaseModel):
    id: int
    cookies: str
