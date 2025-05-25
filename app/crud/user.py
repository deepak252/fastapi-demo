from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id==user_id).first()

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    # hashed_pw = get_password_hash(user.password)
    # db_user = User(email=user.email, hashed_password=hashed_pw)
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user

def delete_user(db:Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True