from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
from servicios.estudianteService import *


def al_cerrar(padre: CTk, ventana: CTkToplevel):
    padre.wm_deiconify()
    padre.lift()
    padre.focus_force()
    ventana.grab_release()
    ventana.destroy()
    
def crear(padre: CTkToplevel, tabla:ttk.Treeview, label:CTkLabel):
    def enviar(tabla):
        est = {
            "nombre": campoNombre.get(),
            "apellido": campoApellido.get(),
            "promedio": float(campoPromedio.get()),
            "edad": int(campoEdad.get()),
            "grado": campoGrado.get(),
            "estado": True
        }
        insertEstudiante(est)
        try:
            actualizarVista(tabla, label)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "Estudiante agregado exitosamente")

    formCrear = CTkToplevel(padre)
    formCrear.title("Crear estudiante")
    formCrear.lift()
    formCrear.grab_set()
    formCrear.focus_force()
    
    CTkLabel(formCrear, text="Nombre del Estudiante").grid(row=0, column=0)
    CTkLabel(formCrear, text="Apellido del Estudiante").grid(row=1, column=0)
    CTkLabel(formCrear, text="Promedio del Estudiante").grid(row=2, column=0)
    CTkLabel(formCrear, text="Edad del Estudiante").grid(row=3, column=0)
    CTkLabel(formCrear, text="Grado del Estudiante").grid(row=4, column=0)

    campoNombre = CTkEntry(formCrear)
    campoNombre.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    campoApellido = CTkEntry(formCrear)
    campoApellido.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    campoPromedio = CTkEntry(formCrear)
    campoPromedio.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    campoEdad = CTkEntry(formCrear)
    campoEdad.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    campoGrado = CTkComboBox(formCrear, values=("1ro", "2do", "3ro", "4to", "5to", "6to"))
    campoGrado.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formCrear, text="Aceptar", command=lambda:(enviar(tabla), formCrear.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def modificar(padre: CTkToplevel, tabla:ttk.Treeview, label:CTkLabel):
    def enviar(tabla, id):
        est = {
            "idEstudiante": int(id),
            "nombre": campoNombre.get(),
            "apellido": campoApellido.get(),
            "promedio": float(campoPromedio.get()),
            "edad": int(campoEdad.get()),
            "grado": campoGrado.get(),
            "estado": True
        }
        modifyEstudiante(id, est)
        try:
            actualizarVista(tabla, label)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "Estudiante modificado exitosamente")

    #Obtener el id
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    formModificar = CTkToplevel(padre)
    formModificar.title("Modificar estudiante")
    formModificar.lift()
    formModificar.grab_set()
    formModificar.focus_force()
    
    CTkLabel(formModificar, text="Nombre del Estudiante").grid(row=0, column=0)
    CTkLabel(formModificar, text="Apellido del Estudiante").grid(row=1, column=0)
    CTkLabel(formModificar, text="Promedio del Estudiante").grid(row=2, column=0)
    CTkLabel(formModificar, text="Edad del Estudiante").grid(row=3, column=0)
    CTkLabel(formModificar, text="Grado del Estudiante").grid(row=4, column=0)

    campoNombre = CTkEntry(formModificar)
    campoNombre.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    campoApellido = CTkEntry(formModificar)
    campoApellido.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    campoPromedio = CTkEntry(formModificar)
    campoPromedio.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    campoEdad = CTkEntry(formModificar)
    campoEdad.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    campoGrado = CTkComboBox(formModificar, values=("1ro", "2do", "3ro", "4to", "5to", "6to"))
    campoGrado.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formModificar, text="Aceptar", command=lambda:(enviar(tabla, id), formModificar.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def inhabilitar(tabla:ttk.Treeview, label:CTkLabel):
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]
    
    if unableEstudiante(id) == 200:
        messagebox.showinfo("Eliminado", "Estudiante eliminado correctamente")
    else:
        messagebox.showwarning("Error", "No se pudo eliminar nada")

def actualizarVista(tabla:ttk.Treeview, label: CTkLabel):

    # Guardar el ID del estudiante seleccionado
    seleccion = tabla.focus()
    id_seleccionado = None
    if seleccion:
        valores = tabla.item(seleccion, "values")
        if valores:
            id_seleccionado = valores[0]  # El ID está en la primera columna

    #Cargar lista al label info
    try:
        res = getEstudianteById(id_seleccionado)
        asignacion = res["asignacion"]

        if asignacion and isinstance(asignacion, list):
            texto = ""
            for i, datos in enumerate(asignacion, start=1):
                curso = datos.get("curso", "N/A")
                profesor = datos.get("profesor", "N/A")
                estado = "Activo" if datos.get("estado", False) else "Inactivo"

                texto += f"Asignación {i}:\n"
                texto += f"  Curso: {curso}\n"
                texto += f"  Profesor: {profesor}\n"
                texto += f"  Estado: {estado}\n\n"

            label.configure(text=texto.strip())
        else:
            label.configure(text="No hay asignaciones disponibles")
    except:
        label.configure(text="Sin info, actualice por favor")



        

    for item in tabla.get_children():
        tabla.delete(item)

    datos = getEstudiantes()
    for dato in datos:
        fila_id = tabla.insert("", "end", values=(dato["idEstudiante"], 
                                        dato["nombre"], 
                                        dato["apellido"], 
                                        dato["promedio"],
                                        dato["edad"],
                                        dato["grado"],
                                        dato["estado"]))
        # Si coincide el ID, guardar ese item para volver a enfocarlo
        if str(dato["idEstudiante"]) == str(id_seleccionado):
            nuevo_focus = fila_id
        
        # Restaurar el enfoque y selección
    try:
        if nuevo_focus:
            tabla.focus(nuevo_focus)
            tabla.selection_set(nuevo_focus)
            tabla.see(nuevo_focus)
    
    except:
        print("Continuemos")



def actualizarInfo(event, label):
    print("Hola")


def desplegarEstudiantes(padre: CTk):
    ventana = CTkToplevel(padre)
    ventana.title("Vista de estudiantes")
    ventana.grab_set()
    ventana.resizable(width=False, height=False)
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    try:
        frameTitulo = CTkFrame(ventana, height=75, fg_color="orange")
        frameBotones = CTkFrame(ventana)
        frameTabla = CTkFrame(ventana)
        frameInfo = CTkScrollableFrame(ventana)

        labelInfo = CTkLabel(frameInfo, text="Aqui ira info", wraplength=250)
        titulo = CTkLabel(frameTitulo, text="Modulo Estudiantes", font=("Arial", 15, "bold"))
        btnCrear = CTkButton(frameBotones, text="Crear estudiante", command=lambda:crear(ventana, tabla, labelInfo))
        btnModificar = CTkButton(frameBotones, text="Modificar estudiante", command=lambda:modificar(ventana, tabla, labelInfo))
        btnInhabilitar = CTkButton(frameBotones, text="Inhabilitar estudiante", command=lambda:(inhabilitar(tabla), labelInfo, actualizarVista(tabla, labelInfo)))
        btnActualizar = CTkButton(frameBotones, text="Actualizar vista", command=lambda:actualizarVista(tabla, labelInfo))
        

        columnas = ["idEstudiante", "nombre", "apellido", "promedio", "edad", "grado", "estado"]

        tabla = ttk.Treeview(frameTabla, columns= columnas, show="headings", selectmode='browse')
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=100, anchor="center")  # Ancho y alineación


        #Configuracion de scrolls
        scrollY = CTkScrollbar(frameTabla, orientation="vertical",command=tabla.yview)
        scrollX = CTkScrollbar(frameTabla, orientation="horizontal", command=tabla.xview)
        tabla.configure(yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)

        #Organizacion de Frames
        frameTitulo.grid(column = 0, row = 0, columnspan = 2, pady = 10, padx = 10, sticky = "nsew")
        frameBotones.grid(column=0, row=1, pady = 10, padx = 10, sticky = "nsew")
        frameTabla.grid(column=1, row=1, pady = 10, padx = 10, sticky = "nsew")
        frameInfo.grid(column =2, row=0, rowspan = 2, pady = 10, padx =10, sticky = "nsew")

        #Organizacion de botones y tabla
        titulo.grid(column = 0, row=0, sticky="nsew", padx=10, pady=10)
        btnCrear.grid(column = 0, row = 0, sticky="nsew", padx=10, pady=10)
        btnModificar.grid(column = 0, row = 1, sticky="nsew", padx=10, pady=10)
        btnInhabilitar.grid(column = 0, row =2, sticky="nsew", padx=10, pady=10)
        btnActualizar.grid(column = 0, row = 3, sticky="nsew", padx=10, pady=10)
        labelInfo.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "nsew")

        tabla.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        scrollX.grid(row=1, column=0, sticky="ew")
        scrollY.grid(row=0, column=1, sticky="ns")

        actualizarVista(tabla, labelInfo)
        ventana.protocol("WM_DELETE_WINDOW", lambda: al_cerrar(padre, ventana))
        ventana.wait_window()  # se detiene hasta que ventana se cierre
    
    finally:      
        padre.wm_deiconify()
        padre.lift()
        padre.focus_force()

