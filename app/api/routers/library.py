from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ... import crud, models, schemas
from ..deps import get_db_dep

router = APIRouter(prefix="/api/library", tags=["library"])


# Authors
@router.post("/authors/", response_model=schemas.AuthorRead)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db_dep)):
    return crud.create_author(db, author)


@router.get("/authors/", response_model=List[schemas.AuthorRead])
def list_authors(db: Session = Depends(get_db_dep)):
    return crud.list_authors(db)


# Halls
@router.post("/halls/", response_model=schemas.HallRead)
def create_hall(hall: schemas.HallCreate, db: Session = Depends(get_db_dep)):
    return crud.create_hall(db, hall)


@router.get("/halls/", response_model=List[schemas.HallRead])
def list_halls(db: Session = Depends(get_db_dep)):
    return db.query(models.Hall).all()


# Books
@router.post("/books/", response_model=schemas.BookRead)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db_dep)):
    return crud.create_book(db, book)


@router.get("/books/", response_model=List[schemas.BookRead])
def list_books(db: Session = Depends(get_db_dep)):
    return crud.list_books(db)


@router.get("/books/{book_id}/", response_model=schemas.BookRead)
def get_book(book_id: int, db: Session = Depends(get_db_dep)):
    b = crud.get_book(db, book_id)
    if not b:
        raise HTTPException(status_code=404, detail="Book not found")
    return b


# Readers
@router.post("/readers/", response_model=schemas.ReaderRead)
def create_reader(reader: schemas.ReaderCreate, db: Session = Depends(get_db_dep)):
    return crud.create_reader(db, reader)


@router.get("/readers/", response_model=List[schemas.ReaderRead])
def list_readers(db: Session = Depends(get_db_dep)):
    return db.query(models.Reader).all()


# Borrow book
@router.post("/borrow/", response_model=schemas.BorrowingRead)
def borrow(reader_id: int, book_id: int, db: Session = Depends(get_db_dep)):
    try:
        br = crud.borrow_book(db, reader_id, book_id)
        return br
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Return book
@router.post("/return/", response_model=schemas.BorrowingRead)
def return_book(reader_id: int, book_id: int, db: Session = Depends(get_db_dep)):
    try:
        br = crud.return_book(db, reader_id, book_id)
        return br
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
