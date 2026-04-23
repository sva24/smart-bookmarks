from pydantic import BaseModel, Field, EmailStr, Password



class UserCreate(BaseModel):
    id: int
    email: EmailStr = Field(
        ..., description="User email", json_schema_extra={"example": "test@example.com"}
    )
    password: Password

   class Config:
        orm_mode = True


class UserResponse(BaseModel):
    email: EmailStr = Field(
        ..., description="User email", json_schema_extra={"example": "test@example.com"}
    )



class UserUpdate(BaseModel):
    email: EmailStr = Field(
        ..., description="User email", json_schema_extra={"example": "test@example.com"}
    )
    password: str


class UserDelete(BaseModel):
    email: EmailStr = Field(
        ..., description="User email", json_schema_extra={"example": "test@example.com"}
    )
    password: str
