###### Rutas de autenticación

# app/routers/auth.py
from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserLogin
from app.services.auth import create_user, verify_user_login
from app.database import SessionLocal
from fastapi import HTTPException, status

router = APIRouter()

# Registro de nuevo usuario
@router.post("/api/auth/register")
def register(user: UserCreate, db: Session = Depends(SessionLocal)):
    return create_user(user=user, db=db)

# Login de usuario (inicia sesión y devuelve el token JWT)
@router.post("/api/auth/login")
def login(user: UserLogin, db: Session = Depends(SessionLocal)):
    db_user = verify_user_login(user=user, db=db)
    # Generamos el token JWT
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
