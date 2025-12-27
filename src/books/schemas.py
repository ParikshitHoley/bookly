from pydantic import BaseModel
from datetime import date
import uuid
from typing import Optional

class bookModel(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    genre: str
    rating: float
    available: bool
    
class bookCreateModel(BaseModel):
    title: str    
    author: str
    publisher: str
    published_date: date
    page_count: int 
    language: str
    genre: str
    rating: float
    available: bool
    
    
class bookUpdateModel(BaseModel):
    title: Optional[str] = None   
    author: Optional[str] = None    
    publisher: Optional[str] = None
    published_date:  Optional[date] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
    genre: Optional[str] = None
    rating: Optional[float] = None
    available: Optional[bool] = None