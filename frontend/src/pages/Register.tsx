import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Register: React.FC = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  // Función para manejar el registro del usuario
  const handleRegister = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/auth/register', {
        username,
        email,
        password
      });

      if (response.status === 201) {
        // Si el registro fue exitoso, redirigir al login
        navigate('/');
      }
    } catch (err: any) {
      // Manejo de errores si la API devuelve un error
      setError('Hubo un problema al registrarse. Verifique los datos e intente nuevamente.');
    }
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', maxWidth: 400, margin: 'auto', padding: 2 }}>
      <h2>Registro de Usuario</h2>
      
      {/* Campo para el nombre de usuario */}
      <TextField
        label="Username"
        variant="outlined"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        fullWidth
        margin="normal"
      />
      
      {/* Campo para el correo electrónico */}
      <TextField
        label="Email"
        variant="outlined"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        fullWidth
        margin="normal"
      />
      
      {/* Campo para la contraseña */}
      <TextField
        label="Password"
        type="password"
        variant="outlined"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        fullWidth
        margin="normal"
      />

      {/* Mostrar el error si existe */}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      
      {/* Botón de registro */}
      <Button variant="contained" onClick={handleRegister}>Registrar</Button>
    </Box>
  );
};

export default Register;
