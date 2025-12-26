
from fastapi import FastAPI
from src.books.router import book_router

version = "v1"
app = FastAPI(
    version=version,
    title="Bookly API",
    description="An API to manage a collection of books.",
)

app.include_router(book_router,prefix=f'/api/{version}/books',tags=["books"])








