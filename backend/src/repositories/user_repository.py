from sqlmodel import Session, select
from models.user import User

class UserRepository:

    @staticmethod
    def get_by_email(session: Session, email: str):
        return session.exec(select(User).where(User.email == email)).first()

    @staticmethod
    def create(session: Session, user: User):
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
