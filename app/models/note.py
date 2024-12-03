###### Modelo de Nota

# app/models/note.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True) #id de las notas
    title = Column(String, index=True) #titulo de las notas
    content = Column(Text) #contenido de las notas
    created_at = Column(DateTime, default=func.now())  # Fecha de creación
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # Fecha de actualización
    owner_id = Column(Integer, ForeignKey("users.id")) #llave foranea entre el id del usuario y las notas
    owner = relationship("User", back_populates="notes") #relación con el modelo Usuarios
