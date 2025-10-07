from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas


# Authors
def create_author(db: Session, author: schemas.AuthorCreate) -> models.Author:
    db_obj = models.Author(name=author.name)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_author(db: Session, author_id: int) -> Optional[models.Author]:
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def list_authors(db: Session) -> List[models.Author]:
    return db.query(models.Author).all()


# Halls
def create_hall(db: Session, hall: schemas.HallCreate) -> models.Hall:
    db_obj = models.Hall(name=hall.name)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_hall(db: Session, hall_id: int) -> Optional[models.Hall]:
    return db.query(models.Hall).filter(models.Hall.id == hall_id).first()


# Books
def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    db_obj = models.Book(title=book.title, hall_id=book.hall_id)
    if book.author_ids:
        authors = (
            db.query(models.Author).filter(models.Author.id.in_(book.author_ids)).all()
        )
        db_obj.authors = authors
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_book(db: Session, book_id: int) -> Optional[models.Book]:
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def list_books(db: Session) -> List[models.Book]:
    return db.query(models.Book).all()


# Readers
def create_reader(db: Session, r: schemas.ReaderCreate) -> models.Reader:
    db_obj = models.Reader(name=r.name)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_reader(db: Session, reader_id: int) -> Optional[models.Reader]:
    return db.query(models.Reader).filter(models.Reader.id == reader_id).first()


# Borrowing
def borrow_book(db: Session, reader_id: int, book_id: int) -> models.Borrowing:
    # Check book availability: no active borrowing (returned_at is NULL)
    active = (
        db.query(models.Borrowing)
        .filter(
            models.Borrowing.book_id == book_id, models.Borrowing.returned_at == None
        )
        .first()
    )
    if active:
        raise ValueError("Book is already borrowed")
    br = models.Borrowing(
        reader_id=reader_id, book_id=book_id, borrowed_at=datetime.utcnow()
    )
    db.add(br)
    db.commit()
    db.refresh(br)
    return br


def return_book(db: Session, reader_id: int, book_id: int) -> models.Borrowing:
    br = (
        db.query(models.Borrowing)
        .filter(
            models.Borrowing.book_id == book_id,
            models.Borrowing.reader_id == reader_id,
            models.Borrowing.returned_at == None,
        )
        .first()
    )
    if not br:
        raise ValueError("Active borrowing not found")
    br.returned_at = datetime.utcnow()
    db.add(br)
    db.commit()
    db.refresh(br)
    return br


# Notes CRUD
def create_note(db: Session, note: schemas.NoteCreate) -> models.Note:
    db_obj = models.Note(note=note.note, description=note.description)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_note(db: Session, note_id: int) -> Optional[models.Note]:
    return db.query(models.Note).filter(models.Note.id == note_id).first()


def list_notes(db: Session) -> List[models.Note]:
    return db.query(models.Note).all()


def delete_note(db: Session, note_id: int) -> None:
    db.query(models.Note).filter(models.Note.id == note_id).delete()
    db.commit()


def update_note(
    db: Session, note_id: int, data: schemas.NoteCreate
) -> Optional[models.Note]:
    n = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not n:
        return None
    n.note = data.note
    n.description = data.description
    db.add(n)
    db.commit()
    db.refresh(n)
    return n
