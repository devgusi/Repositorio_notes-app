####### Lógica de operaciones CRUD de notas

# app/services/notes.py
from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate
from fastapi import HTTPException

# Crear una nueva nota
def create_note(note: NoteCreate, db: Session, token: str):
    # Extraemos el email del token JWT
    user_email = verify_token(token).get("sub")
    
    # Buscamos al usuario que está creando la nota
    db_user = db.query(User).filter(User.email == user_email).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Creamos la nueva nota asociada al usuario
    db_note = Note(title=note.title, content=note.content, owner_id=db_user.id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# Obtener todas las notas de un usuario
def get_notes(db: Session, token: str):
    # Extraemos el email del token JWT
    user_email = verify_token(token).get("sub")
    
    # Buscamos al usuario que está haciendo la consulta
    db_user = db.query(User).filter(User.email == user_email).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Obtenemos todas las notas del usuario
    notes = db.query(Note).filter(Note.owner_id == db_user.id).all()
    return notes

# Obtener una nota específica por su ID
def get_note(note_id: int, db: Session, token: str):
    # Extraemos el email del token JWT
    user_email = verify_token(token).get("sub")
    
    # Buscamos al usuario que está haciendo la consulta
    db_user = db.query(User).filter(User.email == user_email).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Obtenemos la nota por su ID
    db_note = db.query(Note).filter(Note.id == note_id, Note.owner_id == db_user.id).first()
    
    if db_note is None:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    
    return db_note

# Actualizar una nota existente
def update_note(note_id: int, note: NoteUpdate, db: Session, token: str):
    # Extraemos el email del token JWT
    user_email = verify_token(token).get("sub")
    
    # Buscamos al usuario que está haciendo la modificación
    db_user = db.query(User).filter(User.email == user_email).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Buscamos la nota a actualizar
    db_note = db.query(Note).filter(Note.id == note_id, Note.owner_id == db_user.id).first()
    
    if db_note is None:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    
    # Actualizamos los datos de la nota
    db_note.title = note.title
    db_note.content = note.content
    db_note.version += 1  # Incrementamos la versión para manejo de concurrencia optimista
    
    db.commit()
    db.refresh(db_note)
    return db_note

# Eliminar una nota
def delete_note(note_id: int, db: Session, token: str):
    # Extraemos el email del token JWT
    user_email = verify_token(token).get("sub")
    
    # Buscamos al usuario que está haciendo la eliminación
    db_user = db.query(User).filter(User.email == user_email).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Buscamos la nota a eliminar
    db_note = db.query(Note).filter(Note.id == note_id, Note.owner_id == db_user.id).first()
    
    if db_note is None:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    
    # Eliminamos la nota
    db.delete(db_note)
    db.commit()
    return {"message": "Nota eliminada correctament"}
