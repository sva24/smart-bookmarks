from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int
    email: EmailStr = Field(
        ..., description="User email", json_schema_extra={"example": "test@example.com"}
    )
    hashed_password: str

   class Config:
        orm_mode = True

