from pydantic import BaseModel
from .user import UserResponse

class BlogBase(BaseModel):
    title: str
    body: str

class BlogCreate(BlogBase):
    pass

class BlogResponse(BlogBase):
    id: int
    owner: UserResponse

    class Config:
        orm_mode = True