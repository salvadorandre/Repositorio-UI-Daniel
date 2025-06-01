from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from servicios.estudianteService import getEstudiantes
from servicios.profesorService import getProfesores
from servicios.aulaService import getAulas
from servicios.cursoService import getCursos
from servicios.asignacionesService import getAsignaciones


def generar_reporte_estudiante(ruta="reporte_estudiantes.pdf"):

    estudiantes = getEstudiantes()
    c = canvas.Canvas(ruta, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, height - 50, "Reporte de Estudiantes")

    c.setFont("Helvetica", 10)
    y = height - 100
    for estudiante in estudiantes:
        texto = f"{estudiante['idEstudiante']} - {estudiante['nombre']} {estudiante['apellido']}, Edad: {estudiante['edad']}, Promedio: {estudiante['promedio']}, Grado: {estudiante['grado']}"
        c.drawString(50, y, texto)
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    print("Reporte generado exitosamente.")


def generar_reporte_profesores(ruta="reporte_profesores.pdf"):

    profesores = getProfesores()
    c = canvas.Canvas(ruta, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, height - 50, "Reporte de Profesores")

    c.setFont("Helvetica", 10)
    y = height - 100
    for profesor in profesores:
        texto = f"{profesor['idProfesor']} - {profesor['nombre']}, Edad: {profesor['edad']}, Capacidad: {profesor['capacidadEstudiantes']}"
        c.drawString(50, y, texto)
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    print("Reporte generado exitosamente.")


def generar_reporte_aulas(ruta="reporte_aulas.pdf"):

    aulas = getAulas()
    c = canvas.Canvas(ruta, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, height - 50, "Reporte de Aulas")

    c.setFont("Helvetica", 10)
    y = height - 100
    for aula in aulas:
        texto = f"{aula['idProfesorCurso']} - {aula['profesor']['nombre']}, Curso: {aula['curso']['nombre']}"
        c.drawString(50, y, texto)
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    print("Reporte generado exitosamente.")


def generar_reporte_cursos(ruta="reporte_cursos.pdf"):

    cursos = getCursos()
    c = canvas.Canvas(ruta, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, height - 50, "Reporte de Cursos")

    c.setFont("Helvetica", 10)
    y = height - 100
    for curso in cursos:
        texto = f"{curso['idCurso']} - {curso['nombre']}"
        c.drawString(50, y, texto)
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    print("Reporte generado exitosamente.")


def generar_reporte_asignaciones(ruta="reporte_asignaciones.pdf"):

    asignaciones = getAsignaciones()
    c = canvas.Canvas(ruta, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, height - 50, "Reporte de Asignaciones")

    c.setFont("Helvetica", 10)
    y = height - 100
    for asignacion in asignaciones:
        texto = f"{asignacion['idAsignacion']} - {asignacion['fecha']}, Nombre: {asignacion['estudiante']['nombre']}, Curso: {asignacion['curso']['nombre']}, Profesor: {asignacion['profesor']['nombre']}"
        c.drawString(50, y, texto)
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    print("Reporte generado exitosamente.")