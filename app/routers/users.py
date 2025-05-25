from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.dependencies import get_token_header
from app.core.db import get_db
from app.crud import user as crud_user
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(get_token_header)]
)

@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)


@router.get("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user(id, db: Session = Depends(get_db)):
    return crud_user.get_user(db, id)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id, db: Session = Depends(get_db)):
    return crud_user.delete_user(db, id)

