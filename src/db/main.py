from sqlmodel import SQLModel, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from src.config import config


engine: AsyncEngine = create_async_engine(
    url=config.DATABASE_URL,
    echo=True,
)

async def init_db():
    async with engine.begin() as conn:
        from src.books.module import Book
        await conn.run_sync(SQLModel.metadata.create_all)
        