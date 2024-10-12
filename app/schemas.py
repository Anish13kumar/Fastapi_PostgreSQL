from pydantic import BaseModel

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
