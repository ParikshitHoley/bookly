from sqlmodel import SQLModel, Field,Column
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import date, datetime

class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(sa_column=Column(pg.UUID,primary_key=True,default=uuid.uuid4,nullable=False))
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    genre: str
    rating: float
    available: bool
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP(timezone=True),default=datetime.now,nullable=False))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP(timezone=True),default=datetime.now,nullable=False))
    
    def __repr__(self):
        return f"<Book(title={self.title})>"