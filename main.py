from customtkinter import *
from tkinter import ttk
from vistas.vistaEstudiante import desplegarEstudiantes

set_default_color_theme("green")

def ver():
    valor = listaEstudiantes.get()

    match valor:
        case "Estudiantes":
            desplegarEstudiantes(app)
        case "Profesores":
            print("Mostrando profesores")    

app = CTk()
app.title("Sistema de Gestion educativa")


app.rowconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

titulo = CTkLabel(app, text="Gestion de Escuela", font=("Arial", 25, "bold"))

listaEstudiantes = CTkComboBox(app, values=("Estudiantes", "Profesores"))
boton = CTkButton(app, text="Abrir ventana", command=ver)


titulo.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")
listaEstudiantes.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "nsew")
boton.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nsew")


app.mainloop()