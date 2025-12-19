from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
import jwt

from models.user import User
from repositories.user_repository import UserRepository
from schemas.user import UserCreate
from db.session import get_session
from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        return pwd_context.verify(password, hashed)

    @staticmethod
    def create_access_token(data: dict, expires_minutes: int = 60):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
