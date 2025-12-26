from fastapi import APIRouter, HTTPException, status
from src.books.book_data import books
from src.books.schemas import bookModel, bookUpdateModel
from typing import List

book_router = APIRouter()

@book_router.get("/" ,response_model=List[bookModel],status_code=status.HTTP_200_OK)  #get list of books
def get_books() -> list:
    return books

@book_router.post("/",status_code=status.HTTP_201_CREATED)  #add a new book
def add_book(book: bookModel) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    print(books)
    return {"message": "Book added successfully", "book": new_book} 

@book_router.get("/{book_id}", status_code=status.HTTP_200_OK)  #get book by id
def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
  
  

@book_router.patch("/{book_id}")  #update book by id
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
   

@book_router.delete("/{book_id}")  #delete book by id
def delete_book(book_id: int) -> dict:
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
            return {"message": "Book deleted successfully", "book": deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")