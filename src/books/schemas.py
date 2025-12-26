from pydantic import BaseModel

class bookModel(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    genre: str
    rating: float
    available: bool
    
class bookUpdateModel(BaseModel):
    title: str 
    page_count: int
    language: str
    rating: float
    available: bool   