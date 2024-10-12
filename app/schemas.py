from pydantic import BaseModel
from typing import List

# Request schema
class Users(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


# Response schema (used when returning data to the client)
class Users_Out(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True

# New response model to include the db_url
class UsersResponse(BaseModel):
    db_url: str
    users: List[Users_Out]

    class Config:
        orm_mode = True