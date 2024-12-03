import React, { useState } from 'react';
import { TextField, Button, Box, Link } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/auth/login', {
        email,
        password
      });

      const { access_token } = response.data;
      localStorage.setItem('token', access_token);
      navigate('/dashboard');
    } catch (err: any) {
      setError('Invalid email or password');
    }
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', maxWidth: 400, margin: 'auto', padding: 2 }}>
      <h2>Login</h2>
      <TextField
        label="Email"
        variant="outlined"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Password"
        type="password"
        variant="outlined"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        fullWidth
        margin="normal"
      />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <Button variant="contained" onClick={handleLogin}>Login</Button>

      {/* Enlace al registro */}
      <Link href="/register" sx={{ marginTop: 2, textAlign: 'center' }}>
        ¿No tienes una cuenta? Regístrate aquí
      </Link>
    </Box>
  );
};

export default Login;
