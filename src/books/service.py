from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.module import Book
from datetime import datetime
from src.books.schemas import bookCreateModel, bookUpdateModel
from sqlmodel import select

class BookService:
    async def get_all_books(self,session:AsyncSession):
        statement = select(Book).order_by(Book.created_at.desc())
        result = await session.exec(statement)
        return result.all()
    
    async def get_book_by_id(self,book_id:str,session:AsyncSession):
        statement = select(Book).where(Book.uid == book_id)
        result = await session.exec(statement)
        book = result.first()
        return book if book else None
    
    async def create_book(self,book:bookCreateModel,session:AsyncSession):
        new_book = book.model_dump()
        db_book = Book(**new_book)
        session.add(db_book)
        await session.commit()
        await session.refresh(db_book)
        return db_book
    
    async def update_book(self,book_id:str,book:bookUpdateModel,session:AsyncSession):
        book_to_update = await self.get_book_by_id(book_id,session)
        if not book_to_update:
            return None
        book_data = book.model_dump(exclude_unset=True)
        for key, value in book_data.items():
            setattr(book_to_update, key, value) 
        book_to_update.updated_at = datetime.now()
        session.add(book_to_update) 
        await session.commit()
        await session.refresh(book_to_update)
        return book_to_update.model_dump()
    
    async def delete_book(self,book_id:str,session:AsyncSession):
        book_to_delete = await self.get_book_by_id(book_id,session)
        if not book_to_delete:
            return None
        await session.delete(book_to_delete)
        await session.commit()
        return book_to_delete