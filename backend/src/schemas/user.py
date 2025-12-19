from sqlmodel import SQLModel
from typing import Optional

class UserCreate(SQLModel):
    email: str
    password: str

class UserRead(SQLModel):
    id: int
    email: str
