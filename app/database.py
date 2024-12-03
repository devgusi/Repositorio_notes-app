#### Configura la conexión con la base de datos
# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cadena de conexión para PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/notes_app"

# Crea el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Crea una clase base para los modelos
Base = declarative_base()

# Crea la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para crear la base de datos (si es necesario)
def create_database():
    Base.metadata.create_all(bind=engine)
