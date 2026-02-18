from typing import Optional
from pydantic import BaseModel, EmailStr

from src.database import ProjectTypes

class TestGet(BaseModel):
    title: str
    body: Optional[str]

class UserDTO(BaseModel):
    email: EmailStr
    nikename: ProjectTypes.str_256
    password: ProjectTypes.str_32

class UserRoleDTO(UserDTO):
    role_id: int

class UserCreate(UserDTO):
    is_active: bool
    
class UserRole(BaseModel):
    name: ProjectTypes.str_256
    slug: ProjectTypes.str_64

class UserRead(BaseModel):
    id: int
    email: EmailStr
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    """Структура данных внутри JWT (то, что мы расшифруем)"""
    sub: str = None  # Обычно тут хранится user_id
    role: str = None
    exp: int = None
