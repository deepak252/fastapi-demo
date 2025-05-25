from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.db import get_db

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db  # override here

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"data": "Fastapi project"}


def test_create_item():
    response = client.post(
        "/blogs/",
        json = {
            "title": "Blog1",
            "body": "body1"
        }
    )
    assert response.status_code == 200