from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
from servicios.profesorService import *

colorBase = "red"

def al_cerrar(padre: CTk, ventana: CTkToplevel):
    padre.wm_deiconify()
    padre.lift()
    padre.focus_force()
    ventana.destroy()
    
def crear(padre: CTkToplevel, tabla:ttk.Treeview, label:CTkLabel):
    def enviar(tabla):
        est = {
            "nombre": campoNombre.get(),
            "edad": int(campoEdad.get()),
            "capacidadEstudiantes": int(campoCapacidad.get()),
            "estado": True
        }
        insertProfesor(est)
        try:
            actualizarVista(tabla, label)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "Profesor agregado exitosamente")

    formCrear = CTkToplevel(padre)
    formCrear.title("Crear Profesor")
    formCrear.lift()
    formCrear.grab_set()
    formCrear.focus_force()
    
    CTkLabel(formCrear, text="Nombre del Profesor").grid(row=0, column=0)
    CTkLabel(formCrear, text="Edad del Profesor").grid(row=3, column=0)
    CTkLabel(formCrear, text="Capacidad del Profesor").grid(row=4, column=0)

    campoNombre = CTkEntry(formCrear)
    campoNombre.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    campoEdad = CTkEntry(formCrear)
    campoEdad.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    campoCapacidad = CTkEntry(formCrear)
    campoCapacidad.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formCrear, text="Aceptar", command=lambda:(enviar(tabla), formCrear.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def modificar(padre: CTkToplevel, tabla:ttk.Treeview, label:CTkLabel):
    def enviar(tabla, id):
        est = {
            "idProfesor": int(id),
            "nombre": campoNombre.get(),
            "edad": int(campoEdad.get()),
            "capacidadEstudiantes": int(campoCapacidad.get()),
            "estado": True
        }
        modifyProfesor(id, est)
        try:
            actualizarVista(tabla, label)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "Profesor modificado exitosamente")

    #Obtener el id
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    formModificar = CTkToplevel(padre)
    formModificar.title("Modificar Profesor")
    formModificar.lift()
    formModificar.grab_set()
    formModificar.focus_force()
    
    CTkLabel(formModificar, text="Nombre del Profesor").grid(row=0, column=0)
    CTkLabel(formModificar, text="Edad del Profesor").grid(row=3, column=0)
    CTkLabel(formModificar, text="Capacidad del Profesor").grid(row=4, column=0)

    campoNombre = CTkEntry(formModificar)
    campoNombre.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    campoEdad = CTkEntry(formModificar)
    campoEdad.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    campoCapacidad = CTkEntry(formModificar)
    campoCapacidad.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formModificar, text="Aceptar", command=lambda:(enviar(tabla, id), formModificar.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def inhabilitar(tabla:ttk.Treeview):
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    if unableProfesor(id) == 200:
        messagebox.showinfo("Eliminado", "Profesor eliminado correctamente")
    else:
        messagebox.showwarning("Error", "No se pudo eliminar nada")

def actualizarVista(tabla:ttk.Treeview, label:CTkLabel):

    # Guardar el ID del Profesor seleccionado
    seleccion = tabla.focus()
    id_seleccionado = None
    if seleccion:
        valores = tabla.item(seleccion, "values")
        if valores:
            id_seleccionado = valores[0]  # El ID está en la primera columna

    #Cargar lista al label info
    try:
        res = getProfesor(id_seleccionado)
        lista_asignaciones = res["profesorCurso"]

        if lista_asignaciones and isinstance(lista_asignaciones, list):
            texto = ""
            for i, asignacion in enumerate(lista_asignaciones, start=1):

                id_asignacion = asignacion.get("idProfesorCurso", "N/A")
                curso_info = asignacion.get("curso", {})
                nombre_curso = curso_info.get("nombre", "N/A")

                profesor = asignacion.get("profesor")
                estado = "Activo" if asignacion.get("estado", False) else "Inactivo"

                texto += f"Asignación {i}:\n"
                texto += f"  ID Aula: {id_asignacion}\n"
                texto += f"  Curso: {nombre_curso}\n"


            label.configure(text=texto.strip())
        else:
            label.configure(text="No hay asignaciones disponibles")
    except Exception as e:
        label.configure(text="Sin info disponible")





    for item in tabla.get_children():
        tabla.delete(item)

    datos = getProfesores()
    for dato in datos:
        fila_id = tabla.insert("", "end", values=(dato["idProfesor"], 
                                        dato["nombre"], 
                                        dato["edad"],
                                        dato["capacidadEstudiantes"],
                                        dato["estado"]))
        # Si coincide el ID, guardar ese item para volver a enfocarlo
        if str(dato["idProfesor"]) == str(id_seleccionado):
            nuevo_focus = fila_id
        # Restaurar el enfoque y selección
    try:
        if nuevo_focus:
            tabla.focus(nuevo_focus)
            tabla.selection_set(nuevo_focus)
            tabla.see(nuevo_focus)
    
    except:
        print("Continuemos")

def desplegarProfesores(padre: CTk):
    ventana = CTkToplevel(padre)
    ventana.title("Vista de Profesores")
    ventana.grab_set()
    ventana.resizable(width=False, height=False)
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    try:
        frameTitulo = CTkFrame(ventana, height=75, fg_color="darkblue")
        frameBotones = CTkFrame(ventana)
        frameTabla = CTkFrame(ventana)
        frameInfo = CTkScrollableFrame(ventana)

        labelInfo = CTkLabel(frameInfo, text="Aqui ira info", wraplength=250)
        titulo = CTkLabel(frameTitulo, text="Modulo Profesores", font=("Arial", 15, "bold"))
        btnCrear = CTkButton(frameBotones, text="Crear Profesor", command=lambda:crear(ventana, tabla, labelInfo))
        btnModificar = CTkButton(frameBotones, text="Modificar Profesor", command=lambda:modificar(ventana, tabla, labelInfo))
        btnInhabilitar = CTkButton(frameBotones, text="Inhabilitar Profesor", command=lambda:(inhabilitar(tabla), actualizarVista(tabla, labelInfo)))
        btnActualizar = CTkButton(frameBotones, text="Actualizar vista", command=lambda:actualizarVista(tabla, labelInfo))

        columnas = ["idProfesor", "nombre", "edad", "capacidad", "estado"]

        tabla = ttk.Treeview(frameTabla, columns= columnas, show="headings")
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

