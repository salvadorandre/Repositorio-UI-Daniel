from customtkinter import *
from tkinter import ttk
from controllers.controllerEstudiante import agregarEstudiante, modificarEstudiante

def formularioEstudianteModificar(padre, tabla):
    #Obtener el ID del estudiantes

    try:
        seleccion = tabla.focus()

    
        itemSeleccionado = tabla.item(seleccion)
        valores = itemSeleccionado.get("values")
        print(valores)
        id = valores[0]
        
        
        #Configurar ventana top
        ventana = CTkToplevel(padre)    
        ventana.grab_set()
        ventana.title("Modificar estudiante")

        textoId = CTkLabel(ventana, text=f"Id: {id}")
        textoId.grid(row=0, column = 0, padx = 10, pady=10)

        campoId = CTkEntry(ventana)
        campoId.insert(0, id)
        campoId.configure(state = "disabled")
        textoId.grid(row = 0, column=1, padx = 10, pady=10)


        textoNombre = CTkLabel(ventana, text="Nombre").grid(row=1, column = 0, padx = 10, pady=10)
        campoNombre = CTkEntry(ventana)
        campoNombre.grid(row = 1, column=1, padx = 10, pady=10)

        textoApellido = CTkLabel(ventana, text="Apellido").grid(row=2, column = 0, padx = 10, pady=10)
        campoApellido = CTkEntry(ventana)
        campoApellido.grid(row = 2, column=1, padx = 10, pady=10)

        textoPromedio = CTkLabel(ventana, text="Promedio").grid(row=3, column = 0, padx = 10, pady=10)
        campoPromedio = CTkEntry(ventana)
        campoPromedio.grid(row = 3, column=1, padx = 10, pady=10)

        textoEdad = CTkLabel(ventana, text="Edad").grid(row=4, column = 0, padx = 10, pady=10)
        campoEdad = CTkEntry(ventana)
        campoEdad.grid(row = 4, column=1, padx = 10, pady=10)

        textoGrado = CTkLabel(ventana, text="Grado").grid(row=5, column = 0, padx = 10, pady=10)
        campoGrado = CTkOptionMenu(ventana, values=("1ro", "2do", "3ro", "4to", "5to", "6to"))
        campoGrado.grid(row = 5, column=1, padx = 10, pady=10)

        textoEstado = CTkLabel(ventana, text="Estado").grid(row=6, column = 0, padx = 10, pady=10)
        campoEstado = CTkCheckBox(ventana, text="Activo")
        campoEstado.grid(row = 6, column=1, padx = 10, pady=10)

        botonEnviar = CTkButton(ventana, text="Enviar", command=lambda:(modificarEstudiante(id,campoNombre,
                                                                                        campoApellido,
                                                                                        campoPromedio,
                                                                                        campoEdad,
                                                                                        campoGrado,
                                                                                        campoEstado), ventana.destroy()))
        botonEnviar.grid(row = 7, column = 0, columnspan = 2, padx = 10,  pady = 10)

        ventana.mainloop()
    except:
        print("No hay ninguna seleccion")

def formularioEstudianteAgregar(padre):
        
    #Configurar ventana top
    ventana = CTkToplevel(padre)    
    ventana.grab_set()
    ventana.title("Agregar estudiante")

    textoNombre = CTkLabel(ventana, text="Nombre").grid(row=1, column = 0, padx = 10, pady=10)
    campoNombre = CTkEntry(ventana)
    campoNombre.grid(row = 1, column=1, padx = 10, pady=10)

    textoApellido = CTkLabel(ventana, text="Apellido").grid(row=2, column = 0, padx = 10, pady=10)
    campoApellido = CTkEntry(ventana)
    campoApellido.grid(row = 2, column=1, padx = 10, pady=10)

    textoPromedio = CTkLabel(ventana, text="Promedio").grid(row=3, column = 0, padx = 10, pady=10)
    campoPromedio = CTkEntry(ventana)
    campoPromedio.grid(row = 3, column=1, padx = 10, pady=10)

    textoEdad = CTkLabel(ventana, text="Edad").grid(row=4, column = 0, padx = 10, pady=10)
    campoEdad = CTkEntry(ventana)
    campoEdad.grid(row = 4, column=1, padx = 10, pady=10)

    textoGrado = CTkLabel(ventana, text="Grado").grid(row=5, column = 0, padx = 10, pady=10)
    campoGrado = CTkOptionMenu(ventana, values=("1ro", "2do", "3ro", "4to", "5to", "6to"))
    campoGrado.grid(row = 5, column=1, padx = 10, pady=10)

    textoEstado = CTkLabel(ventana, text="Estado").grid(row=6, column = 0, padx = 10, pady=10)
    campoEstado = CTkCheckBox(ventana, text="Activo")
    campoEstado.grid(row = 6, column=1, padx = 10, pady=10)

    botonEnviar = CTkButton(ventana, text="Enviar", command=lambda:(agregarEstudiante(campoNombre,
                                                                                      campoApellido,
                                                                                      campoPromedio,
                                                                                      campoEdad,
                                                                                      campoGrado,
                                                                                      campoEstado), ventana.destroy()))
    botonEnviar.grid(row = 7, column = 0, columnspan = 2, padx = 10,  pady = 10)

    ventana.mainloop()