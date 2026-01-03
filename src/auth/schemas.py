from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
import uuid

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str] | None = None
    last_name: Optional[str] | None = None
    
    
class UserRead(BaseModel):
    uid: uuid.UUID
    username: str
    email: EmailStr
    is_active: bool
    first_name: Optional[str] | None = None
    last_name: Optional[str] | None = None
    created_at: datetime
    updated_at: datetime
    