import { api } from './api';



// Crear una nueva nota
export const createNote = async (note: NoteCreate) => {
  const response = await api.post('/notes', note);  // POST peticion para crear una nueva nota
  return response.data;
};

// Obtener todas las notas de un usuario
export const getNotes = async () => {
  const response = await api.get('/notes'); // GET peticion para obtener todas la notas
  return response.data;
};

// Obtener una nota específica por su ID
export const getNote = async (noteId: number) => {
  const response = await api.get(`/notes/${noteId}`); // GET peticion para obtener las notas por id
  return response.data;
};

// Actualizar una nota existente
export const updateNote = async (noteId: number, note: NoteUpdate) => {
  const response = await api.put(`/notes/${noteId}`, note); // PUT peticion para actualizar una nota
  return response.data;
};

// Eliminar una nota
export const deleteNote = async (noteId: number) => {
  const response = await api.delete(`/notes/${noteId}`); // DELETE peticion para eliminar una nota
  return response.data;
};
