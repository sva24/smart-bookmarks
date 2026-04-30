from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):

    email: EmailStr = Field(
        ..., description="User email", json_schema_extra={"example": "test@example.com"}
    )
    password: str = Field(
        ..., description="password", json_schema_extra={"example": "p@s$w0rD"}
    )


class UserResponse(BaseModel):

    email: EmailStr = Field(
        ..., description="User email", json_schema_extra={"example": "test@example.com"}
    )
    class Config:
        from_attributes = True



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
