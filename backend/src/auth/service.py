from passlib.context import CryptContext
from src.models.schemas import UserRegister, UserLogin
from src.auth.jwt_handler import create_access_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Base de datos in-memory (gratis y suficiente para el proyecto)
fake_users_db = {}


def register_user(user: UserRegister):
    if user.email in fake_users_db:
        return None

    hashed_password = pwd_context.hash(user.password)
    fake_users_db[user.email] = hashed_password

    return {"email": user.email}


def login_user(user: UserLogin):
    if user.email not in fake_users_db:
        return None

    hashed_password = fake_users_db[user.email]

    if not pwd_context.verify(user.password, hashed_password):
        return None

    token = create_access_token({"sub": user.email})

    return token
