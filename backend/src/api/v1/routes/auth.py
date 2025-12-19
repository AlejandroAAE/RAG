from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from db.session import get_session
from schemas.user import UserCreate, UserRead
from models.user import User
from services.auth_service import AuthService
from repositories.user_repository import UserRepository

router = APIRouter()


@router.post("/register", response_model=UserRead)
def register(user: UserCreate, session: Session = Depends(get_session)):
    existing = UserRepository.get_by_email(session, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = AuthService.hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)

    created_user = UserRepository.create(session, new_user)
    return created_user


@router.post("/login")
def login(user: UserCreate, session: Session = Depends(get_session)):
    db_user = UserRepository.get_by_email(session, user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not AuthService.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    token = AuthService.create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
