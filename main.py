from customtkinter import *
from vistas.vistaEstudiante import desplegarEstudiantes
from vistas.vistaProfesor import desplegarProfesores
from vistas.vistaCurso import desplegarCursos
from vistas.vistaAula import desplegarAulas
from vistas.vistaAsignaciones import desplegarAsignaciones
from vistas.vistaReportes import desplegarReportes

set_default_color_theme("green")

def ver():
    valor = listaEstudiantes.get()
    limpiarFrame()
    match valor:
        case "Estudiantes":
            desplegarEstudiantes(frameTabla)
        case "Profesores":
            desplegarProfesores(frameTabla)
        case "Cursos":
            desplegarCursos(frameTabla)

def limpiarFrame():
    for widget in frameTabla.winfo_children():
        widget.destroy()

def asignarProfesor():
    limpiarFrame()
    desplegarAulas(frameTabla)

def asignarEstudiantes():
    limpiarFrame()
    desplegarAsignaciones(frameTabla)


app = CTk()
app.title("Sistema de Gestion educativa")


app.rowconfigure(0, weight=1)
app.columnconfigure(1, weight=1)


frameTabla = CTkFrame(app)

titulo = CTkLabel(app, text="Gestion de Escuela", font=("Arial", 25, "bold"))

listaEstudiantes = CTkComboBox(app, values=("Estudiantes", "Profesores", "Cursos"))
boton = CTkButton(app, text="Abrir ventana", command=ver)

btnAsignacionEst = CTkButton(app, text="Asignar Estudiantes", command=asignarEstudiantes)
btnAsignacionProf = CTkButton(app, text="Asignar Aulas", command=asignarProfesor)

btnReportes = CTkButton(app, text="Generar reportes", command=lambda:desplegarReportes(app))


titulo.grid(row = 0, column = 0, padx = 10, pady = 10)
listaEstudiantes.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nsew")
boton.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "nsew")

btnAsignacionEst.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "nsew" )
btnAsignacionProf.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "nsew" )

btnReportes.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = "nsew")

frameTabla.grid(row = 0, column = 1, rowspan = 6, pady=10, padx=10, sticky = "nsew")



app.mainloop()