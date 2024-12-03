###### Modelo de los Usuarios

# app/models/user.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) #ide de la tabla
    email = Column(String, unique=True, index=True) # Guarda el email
    password_hash = Column(String)  # Guarda el hash de la contraseña
