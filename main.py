from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel



class SayMyNameOut(BaseModel):
    name: str

class SayMyName(SayMyNameOut):
    kilo_of_meth: int

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "Man"}

@app.post("/say_my_name", response_model=SayMyNameOut)
def say_my_name(user: Annotated[SayMyName, Body()]):
    return user
