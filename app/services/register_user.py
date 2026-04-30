from app.models.user import User
from pwdlib import PasswordHash
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import get_user_by_email, create
from fastapi import HTTPException

password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


async def create_user(session: AsyncSession, email: str, password: str) -> User | None:
    user = await get_user_by_email(session, email)
    if user:
        raise HTTPException(status_code=409, detail="User with this email already exists")
    new_user = User(email=email, hashed_password=get_password_hash(password))
    return await create(session, new_user)
