from pydantic import BaseModel,EmailStr,Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(...,min_length=8)
    
class ShowUser(BaseModel):
     id: int
     email: EmailStr
     is_active : bool
     
     class Config():
         orm_mode = True

class data(BaseModel):
    username: str
    password: str
