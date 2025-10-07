from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, constr


# Author
class AuthorCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)


class AuthorRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# Hall
class HallCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)


class HallRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# Book
class BookCreate(BaseModel):
    title: constr(strip_whitespace=True, min_length=1)
    hall_id: Optional[int] = None
    author_ids: Optional[List[int]] = []


class BookRead(BaseModel):
    id: int
    title: str
    hall: Optional[HallRead] = None
    authors: List[AuthorRead] = []

    class Config:
        orm_mode = True


# Reader
class ReaderCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)


class ReaderRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# Borrowing
class BorrowingRead(BaseModel):
    id: int
    reader_id: int
    book_id: int
    borrowed_at: datetime
    returned_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# Note
class NoteCreate(BaseModel):
    note: constr(max_length=120)
    description: Optional[constr(max_length=1024)] = None


class NoteRead(BaseModel):
    id: int
    note: str
    description: Optional[str]

    class Config:
        orm_mode = True
