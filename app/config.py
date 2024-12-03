# app/config.py

import os

class Settings:
    # Variables de configuración de la base de datos
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:admin@localhost:5432/notes_app")
    
    # Clave secreta para firmar JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "JTW_clavesecreta")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    
    # Tiempo de expiración del token en minutos
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    
    # Parámetros del servidor
    SERVER_HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", 8000))
    
    # Habilitar modo de depuración
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ["true", "1", "t"]

# Crear una instancia de la configuración
settings = Settings()
