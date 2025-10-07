from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .db import Base

# association table: book <-> author
book_author = Table(
    "book_author",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True),
)


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

    books = relationship("Book", secondary=book_author, back_populates="authors")


class Hall(Base):
    __tablename__ = "halls"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

    books = relationship("Book", back_populates="hall")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(1024), nullable=False)
    hall_id = Column(Integer, ForeignKey("halls.id"), nullable=True)

    hall = relationship("Hall", back_populates="books")
    authors = relationship("Author", secondary=book_author, back_populates="books")
    borrowings = relationship("Borrowing", back_populates="book")


class Reader(Base):
    __tablename__ = "readers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    borrowings = relationship("Borrowing", back_populates="reader")


class Borrowing(Base):
    __tablename__ = "borrowings"
    id = Column(Integer, primary_key=True, index=True)
    reader_id = Column(Integer, ForeignKey("readers.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    borrowed_at = Column(DateTime, default=datetime.utcnow)
    returned_at = Column(DateTime, nullable=True)

    reader = relationship("Reader", back_populates="borrowings")
    book = relationship("Book", back_populates="borrowings")


# Notes table for notesRest
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    note = Column(String(120), nullable=False)
    description = Column(String(1024), nullable=True)
