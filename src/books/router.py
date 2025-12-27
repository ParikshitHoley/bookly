from fastapi import APIRouter, HTTPException, status, Depends
from src.books.book_data import books
from src.books.schemas import bookModel, bookCreateModel, bookUpdateModel
from typing import List
from datetime import date
from src.books.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession   
from src.db.main import get_session

book_router = APIRouter()

book_service = BookService()

@book_router.get("/" ,response_model=List[bookModel],status_code=status.HTTP_200_OK)  #get list of books
async def get_books(session: AsyncSession = Depends(get_session)) -> list:
    books = await book_service.get_all_books(session)
    return books

@book_router.post("/",status_code=status.HTTP_201_CREATED)  #add a new book
async def add_book(book: bookCreateModel,session: AsyncSession = Depends(get_session)) -> dict:
    new_book = await book_service.create_book(book, session)
    if new_book:
        return {"message": "Book added successfully", "book": new_book}
    raise HTTPException(status_code=400, detail="Failed to add book")

@book_router.get("/{book_id}", status_code=status.HTTP_200_OK)  #get book by id
async def get_book(book_id: str,session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book_by_id(book_id, session)
    if book:
        return book.model_dump()
    raise HTTPException(status_code=404, detail="Book not found")
  
  

@book_router.patch("/{book_id}")  #update book by id
async def update_book(book_id: str, updated_book: bookUpdateModel,session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.update_book(book_id, updated_book, session)
    if book:
        return {"message": "Book updated successfully", "book": book}
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.delete("/{book_id}")  #delete book by id
async def delete_book(book_id: str,session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.delete_book(book_id, session)
    if book:
        return {"message": "Book deleted successfully", "book": book}
    raise HTTPException(status_code=404, detail="Book not found")