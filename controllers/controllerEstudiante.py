from services.estudiantesService import createEstudiante, updateEstudiante

def agregarEstudiante(campoNombre, campoApellido, campoPromedio, campoEdad, campoGrado, campoEstado):

    n = campoNombre.get()
    a = campoApellido.get()
    p = float(campoPromedio.get())
    e = int(campoEdad.get())
    g = campoGrado.get()
    es = bool(campoEstado.get())

    estudiante = {}
    estudiante["nombre"] = n
    estudiante["apellido"] = a
    estudiante["promedio"] = p
    estudiante["edad"] = e
    estudiante["grado"] = g
    estudiante["estado"] = es
    estudiante["asignacion"] = []

    createEstudiante(estudiante)

def modificarEstudiante(id, campoNombre, campoApellido, campoPromedio, campoEdad, campoGrado, campoEstado):

    n = campoNombre.get()
    a = campoApellido.get()
    p = float(campoPromedio.get())
    e = int(campoEdad.get())
    g = campoGrado.get()
    es = bool(campoEstado.get())

    estudiante = {}
    estudiante["idEstudiante"] = id
    estudiante["nombre"] = n
    estudiante["apellido"] = a
    estudiante["promedio"] = p
    estudiante["edad"] = e
    estudiante["grado"] = g
    estudiante["estado"] = es
    estudiante["asignacion"] = []

    updateEstudiante(id, estudiante)





