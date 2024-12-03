"# Repositorio_notes-app"  

Prueba tecnica Desarrollador Gustavo Andres Delgado Guzman

#script para las tablas de la BD

CREATE DATABASE notesapp_db;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    owner_id INTEGER,
    CONSTRAINT fk_user FOREIGN KEY(owner_id) REFERENCES users(id) ON DELETE CASCADE
);


