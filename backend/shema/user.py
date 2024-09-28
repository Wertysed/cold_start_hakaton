from pydantic import BaseModel



class UserIn(BaseModel):
    id: int
    cookies: str
