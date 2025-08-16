from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy models


# class PostSchema(PostBase):
#     id: int
#     created_at: datetime
#     owner_id: int
#     owner: UserOut


class PostBase(BaseModel):
    title: str
    content: str
    published: bool

class PostSchema(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    model_config = ConfigDict(from_attributes=True)

class PostWithVotes(PostSchema):
    votes: int


class PostOut(PostSchema):
    
    Post:PostSchema
    votes:int
    class Config:
        from_attributes = True  # Ensure Pydantic can handle SQLAlchemy objects


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int
    
class Vote(BaseModel):
    post_id:int
    dir: int=Field(ge=0,le=1)
    
    
