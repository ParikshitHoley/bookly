
from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from typing import Optional, List,  Dict

app = FastAPI()


books =[
  {
    "id": 1,
    "title": "Atomic Habits",
    "author": "James Clear",
    "publisher": "Penguin Random House",
    "published_date": "2018-10-16",
    "page_count": 320,
    "language": "English",
    "genre": "Self-help",
    "rating": 4.8,
    "available": True
  },
  {
    "id": 2,
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "publisher": "HarperCollins",
    "published_date": "1993-05-01",
    "page_count": 208,
    "language": "English",
    "genre": "Fiction",
    "rating": 4.6,
    "available": True
  },
  {
    "id": 3,
    "title": "Deep Work",
    "author": "Cal Newport",
    "publisher": "Grand Central Publishing",
    "published_date": "2016-01-05",
    "page_count": 304,
    "language": "English",
    "genre": "Productivity",
    "rating": 4.7,
    "available": False
  },
  {
    "id": 4,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "publisher": "Prentice Hall",
    "published_date": "2008-08-11",
    "page_count": 464,
    "language": "English",
    "genre": "Programming",
    "rating": 4.9,
    "available": True
  },
  {
    "id": 5,
    "title": "Ikigai",
    "author": "Héctor García",
    "publisher": "Penguin Books",
    "published_date": "2017-04-27",
    "page_count": 208,
    "language": "English",
    "genre": "Philosophy",
    "rating": 4.5,
    "available": True
  },
  {
    "id": 6,
    "title": "Rich Dad Poor Dad",
    "author": "Robert Kiyosaki",
    "publisher": "Plata Publishing",
    "published_date": "1997-04-01",
    "page_count": 336,
    "language": "English",
    "genre": "Finance",
    "rating": 4.4,
    "available": False
  },
  {
    "id": 7,
    "title": "The Psychology of Money",
    "author": "Morgan Housel",
    "publisher": "Harriman House",
    "published_date": "2020-09-08",
    "page_count": 256,
    "language": "English",
    "genre": "Finance",
    "rating": 4.7,
    "available": True
  },
  {
    "id": 8,
    "title": "You Don't Know JS",
    "author": "Kyle Simpson",
    "publisher": "O'Reilly Media",
    "published_date": "2015-12-27",
    "page_count": 278,
    "language": "English",
    "genre": "Programming",
    "rating": 4.6,
    "available": True
  }
]


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




@app.get("/books" ,response_model=List[bookModel],status_code=status.HTTP_200_OK)  #get list of books
def get_books() -> list:
    return books

@app.post("/books",status_code=status.HTTP_201_CREATED)  #add a new book
def add_book(book: bookModel) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    print(books)
    return {"message": "Book added successfully", "book": new_book} 

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)  #get book by id
def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
  
  

@app.patch("/books/{book_id}")  #update book by id
def update_book(book_id: int, updated_book: bookUpdateModel) -> dict:
    for index, book in enumerate(books):
        if book["id"] == book_id:
            book['title'] = updated_book.title
            book['page_count'] = updated_book.page_count
            book['language'] = updated_book.language
            book['rating'] = updated_book.rating
            book['available'] = updated_book.available
            books[index] = book
            return {"message": "Book updated successfully", "book": book}
    raise HTTPException(status_code=404, detail="Book not found")
   

@app.delete("/books/{book_id}")  #delete book by id
def delete_book(book_id: int) -> dict:
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
            return {"message": "Book deleted successfully", "book": deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")