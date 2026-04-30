from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User


async def create(session: AsyncSession, user: User)-> Optional[User]:
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    stmt = select(User).where(User.email == email)
    result = await session.execute(stmt)
    return result.scalars().one_or_none()


async def get_user_by_id(session: AsyncSession, id_: int) -> User | None:
    stmt = select(User).where(User.id == id_)
    result = await session.execute(stmt)
    return result.scalars().one_or_none()
