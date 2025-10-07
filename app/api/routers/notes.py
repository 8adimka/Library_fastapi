from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ... import crud, schemas
from ..deps import get_db_dep

router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/", response_model=List[schemas.NoteRead])
def list_notes(db: Session = Depends(get_db_dep)):
    return crud.list_notes(db)


@router.get("/{note_id}/", response_model=schemas.NoteRead)
def get_note(note_id: int, db: Session = Depends(get_db_dep)):
    n = crud.get_note(db, note_id)
    if not n:
        raise HTTPException(status_code=404, detail="Note not found")
    return n


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db_dep)):
    n = crud.create_note(db, note)
    return {"id": n.id}


@router.delete("/{note_id}/", status_code=status.HTTP_200_OK)
def delete_note(note_id: int, db: Session = Depends(get_db_dep)):
    if not crud.get_note(db, note_id):
        raise HTTPException(status_code=404, detail="Note not found")
    crud.delete_note(db, note_id)
    return {}


@router.put("/{note_id}/", status_code=status.HTTP_200_OK)
def update_note(
    note_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db_dep)
):
    updated = crud.update_note(db, note_id, note)
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return {}
