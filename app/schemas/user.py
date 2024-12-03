# Schema de los Usuario
# app/schemas/user.py
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

# El esquema que se utiliza al devolver los datos del usuario tras el login
class UserOut(BaseModel):
    email: str

    class Config:
        orm_mode = True  # Esto es necesario para que Pydantic pueda trabajar con objetos de SQLAlchemy
