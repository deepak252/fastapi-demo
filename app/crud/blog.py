from sqlalchemy.orm import Session
from app.models.blog import Blog
from app.schemas.blog import BlogCreate

def get_blog(db: Session, blog_id: int) -> Blog | None:
    return db.query(Blog).filter(Blog.id == blog_id).first()

def get_blogs(db: Session):
    return db.query(Blog).all()

def create_blog(db: Session, blog:BlogCreate):
    new_blog = Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(db: Session, blog_id: int):
    blog = get_blog(db, blog_id)
    if not blog:
        return False
    db.delete(blog)
    db.commit()
    return True
