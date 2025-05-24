from typing import Any
from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI(title="Dependency Injection")

blogs = {
    "1": "FastAPI Prerequisites",
    "2": "Building APIS",
    "3": "Background Tasks"
}

users = {
    "8": "Jamie",
    "9": "Sam",
}

# def get_blog_or_404(id: str):
#     blog = blogs.get(id)
#     if not blog:
#         raise HTTPException(detail=f"Blog with {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
#     return blog

# @app.get("/blog/{id}")
# def get_blog(blog_name: str = Depends(get_blog_or_404)):
#     return blog_name

class GetObjectOr404:
    def __init__(self, model) -> None:
        self.model = model
    
    def __call__(self, id: str) -> Any:
        obj = self.model.get(id)

        if not obj:
            raise HTTPException(detail=f"Object with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
        return obj
        

blog_dependency = GetObjectOr404(blogs)
@app.get("/blog/{id}")
def get_blog(blog_name: str = Depends(blog_dependency)):
    return blog_name


user_dependency = GetObjectOr404(users)
@app.get("/user/{id}")
def get_user(user_name: str = Depends(user_dependency)):
    return user_name

