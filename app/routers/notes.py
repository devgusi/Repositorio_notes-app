
###### Rutas para las notas

# app/routers/notes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.note import NoteCreate, NoteUpdate
from app.services.notes import create_note, get_notes, get_note, update_note, delete_note
from app.utils.auth import verify_token
from app.utils.auth import get_current_user

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

# Crear una nueva nota
@router.post("/api/notes")
def create_note_route(note: NoteCreate, db: Session = Depends(SessionLocal), token: str = Depends(get_current_user)):
    return create_note(note=note, db=db, token=token)

# Obtener todas las notas
@router.get("/api/notes")
def get_notes_route(db: Session = Depends(SessionLocal), token: str = Depends(get_current_user)):
    return get_notes(db=db, token=token)

# Obtener una nota por su ID
@router.get("/api/notes/{note_id}")
def get_note_route(note_id: int, db: Session = Depends(SessionLocal), token: str = Depends(get_current_user)):
    return get_note(note_id=note_id, db=db, token=token)

# Actualizar una nota
@router.put("/api/notes/{note_id}")
def update_note_route(note_id: int, note: NoteUpdate, db: Session = Depends(SessionLocal), token: str = Depends(get_current_user)):
    return update_note(note_id=note_id, note=note, db=db, token=token)

# Eliminar una nota
@router.delete("/api/notes/{note_id}")
def delete_note_route(note_id: int, db: Session = Depends(SessionLocal), token: str = Depends(get_current_user)):
    return delete_note(note_id=note_id, db=db, token=token)
