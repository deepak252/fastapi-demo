from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .core.db import create_db_and_tables
from .routers import blogs, users

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    create_db_and_tables()
    yield
    # Shutdown logic (if any)

app = FastAPI(title="Blogs App", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={"message": str(exc.detail)},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exc)},
    )

app.include_router(blogs.router)
app.include_router(users.router)

@app.get('/')
def home():
    return {"data": "Fastapi project"}