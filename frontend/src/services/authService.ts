// src/services/authService.ts

import axios from 'axios';
import { UserCreate, UserLogin, AuthResponse } from '../types/user';

// Crear una instancia de axios para configurar las URL base y los encabezados
const api = axios.create({
  baseURL: 'http://localhost:8000', 
  headers: {
    'Content-Type': 'application/json',
  },
});

// Registrar un nuevo usuario
export const registerUser = async (user: UserCreate) => {
  const response = await api.post('/api/auth/register', user);
  return response.data;
};

// Iniciar sesión y obtener el token JWT
export const loginUser = async (user: UserLogin) => {
  const response = await api.post('/api/auth/login', user);
  return response.data as AuthResponse;
};

// Guardar el token en el localStorage para su uso posterior
export const saveToken = (token: string) => {
  localStorage.setItem('access_token', token);
};

// Obtener el token desde el localStorage
export const getToken = () => {
  return localStorage.getItem('access_token');
};

// Eliminar el token del localStorage cuando el usuario cierre sesión
export const logout = () => {
  localStorage.removeItem('access_token');
};
