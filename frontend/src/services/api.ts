import axios from 'axios';

// Configurar la URL base de la API 
const API_URL = 'http://127.0.0.1:8000/api'; // Cambia esto a tu URL real

// Crear instancia de axios con la configuración global
export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Función para obtener el token de localStorage
const getToken = () => {
  return localStorage.getItem('token');
};

// Interceptores de Axios para agregar el token JWT en los headers
api.interceptors.request.use(
  (config) => {
    const token = getToken();
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`; // Añadir token a la cabecera
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
