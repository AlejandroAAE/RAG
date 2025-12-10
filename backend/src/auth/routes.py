from fastapi import APIRouter, HTTPException
from src.models.schemas import UserRegister, UserLogin, UserResponse, TokenResponse
from src.auth.service import register_user, login_user

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserRegister):
    result = register_user(user)

    if result is None:
        raise HTTPException(status_code=400, detail="User already exists")

    return {"email": user.email, "message": "User registered successfully"}


@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    token = login_user(user)

    if token is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token, "token_type": "bearer"}
