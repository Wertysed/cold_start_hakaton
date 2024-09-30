from pydantic import BaseModel



class Cookies(BaseModel):
    session_id: str
