from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field


app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=120)
    year: int = Field(..., ge=1450, le=2100)


class Book(BookCreate):
    id: int


books: Dict[int, Book] = {
    1: Book(id=1, title="Clean Code", author="Robert C. Martin", year=2008),
    2: Book(id=2, title="The Pragmatic Programmer", author="Andrew Hunt", year=1999),
}


@app.get("/books", response_model=List[Book])
def list_books(author: Optional[str] = Query(default=None)):
    # TODO: If author is provided, return only matching books.
    return list(books.values())


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = books.get(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate):
    next_id = max(books.keys(), default=0) + 1
    new_book = Book(id=next_id, **payload.model_dump())
    books[next_id] = new_book
    return new_book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, payload: BookCreate):
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    updated_book = Book(id=book_id, **payload.model_dump())
    books[book_id] = updated_book
    return updated_book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    del books[book_id]
