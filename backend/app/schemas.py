from pydantic import BaseModel

class UserCreate(BaseModel):

    name:str
    email:str
    password:str
    goal:str


class LoginSchema(BaseModel):

    email:str
    password:str