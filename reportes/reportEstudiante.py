from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import requests


def generar_reporte(estudiantes, ruta="reporte_estudiantes.pdf"):
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

res = requests.get("http://educate.runasp.net/api/estudiante")
generar_reporte(res.json())