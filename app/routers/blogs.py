from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.dependencies import get_token_header
from app.core.db import get_db
from app.crud import blog as crud_blog
from app.schemas.blog import BlogCreate, BlogResponse
from typing import List

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"],
    dependencies=[Depends(get_token_header)]
)

@router.get("/", response_model=List[BlogResponse])
async def get_blogs(db: Session = Depends(get_db)):
    return crud_blog.get_blogs(db)

@router.get("/{id}", response_model=BlogResponse)
async def get_blog(id, db: Session = Depends(get_db)):
    return crud_blog.get_blog(db, id)

@router.post("/", response_model=BlogResponse, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    return crud_blog.create_blog(db, blog)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_blog(id, db: Session = Depends(get_db)):
    return crud_blog.delete_blog(db, id)

