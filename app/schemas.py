from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


# Author
class AuthorCreate(BaseModel):
    name: str = Field(..., min_length=1, strip_whitespace=True)


class AuthorRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# Hall
class HallCreate(BaseModel):
    name: str = Field(..., min_length=1, strip_whitespace=True)


class HallRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# Book
class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, strip_whitespace=True)
    hall_id: Optional[int] = None
    author_ids: Optional[List[int]] = Field(default_factory=list)


class BookRead(BaseModel):
    id: int
    title: str
    hall: Optional[HallRead] = None
    authors: List[AuthorRead] = Field(default_factory=list)

    class Config:
        orm_mode = True


# Reader
class ReaderCreate(BaseModel):
    name: str = Field(..., min_length=1, strip_whitespace=True)


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
    note: str = Field(..., min_length=1, max_length=120)
    description: Optional[str] = Field(default=None, max_length=1024)


class NoteRead(BaseModel):
    id: int
    note: str
    description: Optional[str]

    class Config:
        orm_mode = True
