# Pydantic is useful for data validation and type hints.
# Create clean data models using Python classes
# pip install pydantic

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

# Here enum values behave like strings
# Can be directly used in JSON, Pydantic, FastAPI
# isinstance(Language.PYTHON, str) is True
class Language(str, Enum):
    PYTHON = "Python"
    JAVA = "Java"
    GO = "Go"

class Comment(BaseModel):
    text: Optional[str] = None

class Blog(BaseModel):
    title: str
    desc: Optional[str] = None
    is_active: bool
    language: Language = Language.JAVA
    # created_at: datetime = datetime.now() # datetime = datetime.now() is not dynamic
    created_at: datetime = Field(default_factory=datetime.now)  # dynamic time
    comments: Optional[List[Comment]] = []


# Blog(title="My title", is_active="SDf") ## ERROR: ValidationError

blog1 = Blog(title="My title", is_active=True)
print(blog1)    # My title' desc=None is_active=True language=<Language.JAVA: 'Java'> created_at=datetime.datetime(2025, 5, 24, 20, 46, 11, 73383)


# import time
# time.sleep(2)
# blog2 = Blog(title="My title", is_active=True)
# print(blog2)    d

# print(blog1.model_dump())  # {'title': 'My title', 'desc': None, 'is_active': True, 'language': <Language.JAVA: 'Java'>, 'created_at': datetime.datetime(2025, 5, 24, 20, 53, 6, 997001)}
# print(blog1.model_dump_json())  # {"title":"My title","desc":null,"is_active":true,"language":"Java","created_at":"2025-05-24T20:52:30.144370"}
# print(blog1.model_json_schema())

blog2 = Blog(title="My title", is_active=True, comments=[{"text":"First Comment"}])
print(blog2)