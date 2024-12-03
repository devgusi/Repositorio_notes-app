# app/__init__.py

# Este archivo hace que esta carpeta sea un paquete Python.

from .main import app  # Importamos la aplicación FastAPI para su inicialización
from .database import create_database  # Importamos la función para crear la base de datos

# Al ejecutar la aplicación, se creará la base de datos automáticamente si no existe.
create_database()

