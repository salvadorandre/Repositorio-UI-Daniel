from customtkinter import *
from tkinter import ttk
from services.estudiantesService import insertarDatos
from views.modalEstudiante import formularioEstudianteModificar, formularioEstudianteAgregar

app = CTk()



#Configuracion visual para la tabla

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                background="gray",         # fondo de las filas
                foreground="white",         # color del texto
                rowheight=25,
                fieldbackground="gray")    # fondo cuando se edita

style.map('Treeview',
          background=[('selected', '#333333')],  # fila seleccionada
          foreground=[('selected', 'white')])

style.configure("Treeview.Heading", 
                background="black", 
                foreground="white", 
                font=('Segoe UI', 10, 'bold'))



#Ajusta de columnas de la app principal
app.resizable(height = False, width=False)
app.grid_rowconfigure(0, weight=1)        # Hace que crezca la fila 0
app.grid_columnconfigure(0, weight=1)     # Hace que crezca la columna 0

#---------------Invocacion de widgets-------------------
#Label


#Frames
espacioOpciones = CTkFrame(app, width=100)
espacioMenu = CTkFrame(app, height=200)
espacioTabla = CTkFrame(app, width=500)
espacioDetalles = CTkScrollableFrame(app)

#scrollbar
scrollbar_y = CTkScrollbar(espacioTabla, orientation="vertical")

#Botones
#Botones-Menu
verEstudiantes = CTkButton(espacioMenu, text="Estudiantes")
verProfesores = CTkButton(espacioMenu, text="Profesores")
verCursos = CTkButton(espacioMenu, text="Cursos")
verProfesorCurso = CTkButton(espacioMenu, text="Profesor-Curso")
verAsignaciones = CTkButton(espacioMenu, text="Asignaciones")
#Botones-Opcion
agregar = CTkButton(espacioOpciones, text="Agregar", command=lambda:formularioEstudianteAgregar(app))
inhabilitar = CTkButton(espacioOpciones, text="Inhabilitar")
modificar = CTkButton(espacioOpciones, text="Modificar", command=lambda:formularioEstudianteModificar(app, tabla))


#Tabla
tabla = ttk.Treeview(espacioTabla, columns=("0", "1", "2", "3", "4", "5", "6", "7"), show="headings", height=20, yscrollcommand=scrollbar_y.set)
tabla.heading("0", text="ID")
tabla.heading("1", text="Nombre")
tabla.heading("2", text="Apellido")
tabla.heading("3", text="Promedio")
tabla.heading("4", text="Edad")
tabla.heading("5", text="Grado")
tabla.heading("6", text="Estado")
tabla.heading("7", text="Asignacion")

tabla.column("0", width=50, stretch=True)

for i in range(1, 7):
    tabla.column(f"{i}", width=100, stretch=True)


espacioTabla.grid_rowconfigure(0, weight=1)
espacioTabla.grid_columnconfigure(0, weight=1)

espacioMenu.grid_columnconfigure(0, weight=1)
espacioMenu.grid_rowconfigure(0, weight=1)

espacioOpciones.grid_columnconfigure(0, weight=1)


#Organizacion de widgets
espacioMenu.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10, sticky="nsew")
espacioOpciones.grid(row = 1, column = 0, padx = 10, pady = 10, sticky="nsew")
espacioTabla.grid(row = 1, column = 1, padx = 10, pady = 10, sticky="nsew")
espacioDetalles.grid(row = 0, column = 2, rowspan = 2, padx = 10, pady=10, sticky="nsew")

verEstudiantes.grid(row = 0, column = 0, padx = 10, pady = 10, sticky="ew")
verProfesores.grid(row = 0, column = 1, padx = 10, pady = 10, sticky="ew")
verCursos.grid(row = 0, column = 2, padx = 10, pady = 10, sticky="ew")
verProfesorCurso.grid(row = 0, column = 3, padx = 10, pady = 10, sticky="ew")
verAsignaciones.grid(row = 0, column = 4, padx = 10, pady = 10, sticky="ew")

agregar.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")
inhabilitar.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "nsew")
modificar.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nsew")


tabla.grid(row=0, column=0, sticky="nsew")

#Configuraciones del scrollbar
scrollbar_y.grid(row = 0, column = 1, sticky = "ns")
scrollbar_y.configure(command=tabla.yview)

insertarDatos(tabla)

app.mainloop()
