
# app/schemas/note.py
from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: str

    class Config:
        orm_mode = True  
