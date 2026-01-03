

from sqlmodel import SQLModel, Field,Column
import uuid
import sqlalchemy.dialects.postgresql as pg
from typing import Optional
from pydantic import EmailStr
from datetime import datetime

class User(SQLModel,table=True ):
    __tablename__ = "users"
    uid:uuid.UUID = Field(sa_column=Column(pg.UUID, primary_key=True, nullable=False, default=uuid.uuid4))
    username:str = Field(max_length=15,nullable=False, unique=True)
    email:EmailStr = Field(max_length=50,nullable=False, unique=True)
    hashed_password:str = Field(nullable=False,exclude=True)
    is_active:bool = Field(default=True,nullable=False)
    first_name:Optional[str] = Field(max_length=30,nullable=True)
    last_name:Optional[str] = Field(max_length=30,nullable=True)
    created_at:datetime = Field(sa_column=Column(pg.TIMESTAMP(timezone=True), default=datetime.now, nullable=False))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP(timezone=True), default=datetime.now, nullable=False))
    
    def __repr__(self):
        return f"<User (username={self.username})>"