interface NoteUpdate {
    // Propiedades que se pueden actualizar en una nota
    title?: string;
    content?: string;
  }


  interface NoteCreate {
    // Propiedades que se pueden crear  una nota
    title?: string;
    content?: string;
  }

  interface NoteDelete {
    // Propiedades que se pueden eliminar  una nota
    id ?: number;
  }