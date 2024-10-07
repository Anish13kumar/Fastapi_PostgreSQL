from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Users(BaseModel):
    username : str
    password : str
    class Config:
        orm_mode = True

class Users_Out(BaseModel):
    id:UUID
    username : str
    password : str
    class Config:
        orm_mode = True