from customtkinter import *
from reportes.reportes import generar_reporte_estudiante, generar_reporte_profesores, generar_reporte_aulas, generar_reporte_cursos, generar_reporte_asignaciones

def estudiante():
    generar_reporte_estudiante()

def profesores():
    generar_reporte_profesores()

def cursos():
    generar_reporte_cursos()

def aulas():
    generar_reporte_aulas()

def asignaciones():
    generar_reporte_asignaciones()


def desplegarReportes(app):
    ventana = CTkToplevel(app)
    ventana.title("Imprimir reportes")
    ventana.grab_set()

    btnEst = CTkButton(ventana, text="Imprimir estudiantes", command=estudiante)
    btnProf = CTkButton(ventana, text="Imprimir profesores", command=profesores)
    btnCur = CTkButton(ventana, text="Imprimir cursos", command=cursos)
    btnAul = CTkButton(ventana, text="Imprimir aulas", command=aulas)
    btnAsig = CTkButton(ventana, text="Imprimir asignaciones", command=asignaciones)

    btnEst.grid(row = 0, column = 0, padx=10, pady = 10, sticky = "nsew")
    btnProf.grid(row = 0, column = 1, padx=10, pady = 10, sticky = "nsew")
    btnCur.grid(row = 1, column = 0, padx=10, pady = 10, sticky = "nsew")
    btnAul.grid(row = 1, column = 1, padx=10, pady = 10, sticky = "nsew")
    btnAsig.grid(row = 2, column = 0, columnspan = 2, padx=10, pady = 10, sticky = "nsew")

    ventana.wait_window()
