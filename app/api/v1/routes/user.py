from fastapi import APIRouter, status, Depends
from app.schemas.user import (UserCreate, UserResponse)
from app.db.sessions import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.register_user import create_user


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user_endpoint(
    payload: UserCreate,
    session: AsyncSession = Depends(get_db),
):

    result = await create_user(session, payload.email, payload.password)
    return result

