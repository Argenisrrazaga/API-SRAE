# Post
  # # Estudiantes
    https://argenisrrazaga.pythonanywhere.com/estudiantes
    Parámetros: JSON {nombre, apellido}
  # # Cursos
    https://argenisrrazaga.pythonanywhere.com/cursos
    Parámetros: JSON {nombre}
  # # Asistencias
    https://argenisrrazaga.pythonanywhere.com/asistencias
    Parametros: JSON {estudiante_id, curso_id, asistio(1 o 0)}
    
# Get
  # # Estudiantes
    https://argenisrrazaga.pythonanywhere.com/estudiantes
    o https://argenisrrazaga.pythonanywhere.com/estudiantes/{{id_estudiante}}
  # # Cursos
    https://argenisrrazaga.pythonanywhere.com/cursos
    o https://argenisrrazaga.pythonanywhere.com/{{id_curso}}
  # # Asistencias
    https://argenisrrazaga.pythonanywhere.com/asistencias
    o https://argenisrrazaga.pythonanywhere.com/asistencias/{{id_asistencias}}
    
# Put
  # # Estudiantes
    https://argenisrrazaga.pythonanywhere.com/estudiantes/{{id_estudiante}}
    Parámetros: JSON {nombre, apellido}
  # # Cursos
    https://argenisrrazaga.pythonanywhere.com/cursos/{{id_curso}}
    Parámetros: JSON {nombre}
  # # Asistencias
    https://argenisrrazaga.pythonanywhere.com/asistencias/{{id_asistencia}}
    Parámetros: JSON {estudiante_id, curso_id, asistio}

# Delete
  # # Estudiantes
    https://argenisrrazaga.pythonanywhere.com/estudiantes/{{id_estudiante}}
  # # Cursos
    https://argenisrrazaga.pythonanywhere.com/cursos/{{id_curso}}
  # # Asistencias
    https://argenisrrazaga.pythonanywhere.com/asistencias/{{id_asistencia}}
