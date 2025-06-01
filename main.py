from customtkinter import *
from vistas.vistaEstudiante import desplegarEstudiantes
from vistas.vistaProfesor import desplegarProfesores
from vistas.vistaCurso import desplegarCursos
from vistas.vistaAula import desplegarAulas
from vistas.vistaAsignaciones import desplegarAsignaciones
from vistas.vistaReportes import desplegarReportes
from PIL import Image

set_default_color_theme("blue")
set_appearance_mode("light")

def ver(opcion):
    valor = opcion
    print(opcion)
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

def cambiarTema():
    valor = switchApariencia.get()
    if(valor == 1):
        set_appearance_mode("dark")
    else:
        set_appearance_mode("light")

app = CTk()
app.title("Sistema de Gestion educativa")
app.resizable(width=False, height=False)

app.rowconfigure(0, weight=1)
app.columnconfigure(1, weight=1)


frameTabla = CTkFrame(app)

img = Image.open("assets/logo.png")
imagen = CTkImage(dark_image = img, size=(200, 150))
labelImagen = CTkLabel(app, image= imagen, text = "")

titulo = CTkLabel(app, text="Gestion de Escuela", font=("Arial", 25, "bold"))

listaEstudiantes = CTkComboBox(app, values=("Estudiantes", "Profesores", "Cursos"), command=ver)

btnAsignacionEst = CTkButton(app, text="Asignar Estudiantes", command=asignarEstudiantes)
btnAsignacionProf = CTkButton(app, text="Asignar Aulas", command=asignarProfesor)
btnReportes = CTkButton(app, text="Generar reportes", command=lambda:desplegarReportes(app))

switchApariencia = CTkSwitch(app, text="Modo oscuro",command=cambiarTema)


labelImagen.grid(row = 0, column = 0,padx = 10, pady = 10)
titulo.grid(row = 1, column = 0, padx = 10, pady = 10)

listaEstudiantes.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nsew")

btnAsignacionEst.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "nsew" )
btnAsignacionProf.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "nsew" )

btnReportes.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = "nsew")

frameTabla.grid(row = 0, column = 1, rowspan = 8, pady=10, padx=10, sticky = "nsew")

switchApariencia.grid(row=7, column = 0, sticky = "nsew")



app.mainloop()