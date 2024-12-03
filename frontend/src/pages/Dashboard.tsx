import React, { useState, useEffect } from 'react';
import { Box, Button, TextField } from '@mui/material';
import axios from 'axios';
import { isAuthenticated } from '../utils/auth';
import { useNavigate } from 'react-router-dom';

const Dashboard: React.FC = () => {
  const [notes, setNotes] = useState<any[]>([]);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate('/');
    } else {
      fetchNotes();
    }
  }, []);

  const fetchNotes = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/notes', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      });
      setNotes(response.data);
    } catch (error) {
      console.log('Error fetching notes');
    }
  };

  const createNote = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/api/notes', { title, content }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      });
      fetchNotes(); // Refresh notes
    } catch (error) {
      console.log('Error creating note');
    }
  };

  return (
    <Box sx={{ padding: 2 }}>
      <h2>Your Notes</h2>
      <TextField
        label="Title"
        variant="outlined"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        fullWidth
      />
      <TextField
        label="Content"
        variant="outlined"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        fullWidth
        multiline
        rows={4}
      />
      <Button onClick={createNote} variant="contained" sx={{ marginTop: 2 }}>Create Note</Button>

      <div>
        {notes.map((note) => (
          <div key={note.id}>
            <h3>{note.title}</h3>
            <p>{note.content}</p>
          </div>
        ))}
      </div>
    </Box>
  );
};

export default Dashboard;
