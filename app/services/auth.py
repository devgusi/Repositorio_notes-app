####### Lógica de autenticación

# app/services/auth.py
from passlib.context import CryptContext
from app.models.user import User
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app.utils.auth import verify_token, create_access_token
from app.schemas.user import UserCreate, UserLogin
from fastapi import HTTPException

# Crear un contexto para el hash de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para crear un nuevo usuario

def create_user(user: UserCreate, db: Session):
    # Verificamos si el correo ya está en uso
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo ya esta en uso")
    
    # Creamos un nuevo usuario y lo guardamos en la base de datos
    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Recuperamos el objeto del usuario recién creado
    return new_user

def verify_user_login(user: UserLogin, db: Session):
    # Buscamos al usuario por el correo electrónico
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not check_password_hash(db_user.password_hash, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Datos de inicio de sesión incorrectos")
    
    return db_user
