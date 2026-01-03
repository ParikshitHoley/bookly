from typing import AsyncGenerator
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession


engine: AsyncEngine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
)

# create sessionmaker once at module level
async_session = async_sessionmaker(bind=engine,class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        # import models so SQLModel metadata is populated
        from src.books.module import Book
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session