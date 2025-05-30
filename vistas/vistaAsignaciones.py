from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
from servicios.asignacionesService import *
from servicios.cursoService import *
from servicios.profesorService import *

colorBase = "red"

def al_cerrar(padre: CTk, ventana: CTkToplevel):
    padre.wm_deiconify()
    padre.lift()
    padre.focus_force()
    ventana.destroy()
    
def crear(padre: CTkToplevel, tabla:ttk.Treeview, label:CTkLabel):
    def enviar(tabla):

        textoCurso = str(campoCurso.get()).split("-")
        textoProfesor = str(campoProfesor.get()).split("-")

        asignacion = {
            "cursoId": int(textoCurso[0]),
            "profesorId": int(textoProfesor[0]),
            "estado": True
        }
        insertAsignacion(asignacion)
        try:
            actualizarVista(tabla, label)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "asignacion agregada exitosamente")

    formCrear = CTkToplevel(padre)
    formCrear.title("Crear asignacion")
    formCrear.lift()
    formCrear.grab_set()
    formCrear.focus_force()
    
    CTkLabel(formCrear, text="Profesor").grid(row=0, column=0)
    CTkLabel(formCrear, text="Curso").grid(row=3, column=0)

    #Obtener columnas
    datos = getProfesores()
    profesores = []

    for dato in datos:
        text = str(dato["idProfesor"]) + "-" + str(dato["nombre"])
        profesores.append(text)


    datos = getCursos()
    cursos = []

    for dato in datos:
        text = str(dato["idCurso"]) + "-" + str(dato["nombre"])
        cursos.append(text)


    campoProfesor = CTkComboBox(formCrear, values=profesores)
    campoProfesor.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    campoCurso = CTkComboBox(formCrear, values=cursos)
    campoCurso.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formCrear, text="Aceptar", command=lambda:(enviar(tabla), formCrear.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def modificar(padre: CTkToplevel, tabla:ttk.Treeview, label:CTkLabel):
    def enviar(tabla, id):
        textoCurso = str(campoCurso.get()).split("-")
        textoProfesor = str(campoProfesor.get()).split("-")

        asignacion = {
            "idProfesorCurso": id,
            "cursoId": int(textoCurso[0]),
            "profesorId": int(textoProfesor[0]),
            "estado": True
        }
        modifyAsignacion(id, asignacion)
        try:
            actualizarVista(tabla, label)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "asignacion modificada exitosamente")

    #Obtener el id
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    formCrear = CTkToplevel(padre)
    formCrear.title("Crear asignacion")
    formCrear.lift()
    formCrear.grab_set()
    formCrear.focus_force()
    
    CTkLabel(formCrear, text="Profesor").grid(row=0, column=0)
    CTkLabel(formCrear, text="Curso").grid(row=3, column=0)

    #Obtener columnas
    datos = getProfesores()
    profesores = []

    for dato in datos:
        text = str(dato["idProfesor"]) + "-" + str(dato["nombre"])
        profesores.append(text)


    datos = getCursos()
    cursos = []

    for dato in datos:
        text = str(dato["idCurso"]) + "-" + str(dato["nombre"])
        cursos.append(text)


    campoProfesor = CTkComboBox(formCrear, values=profesores)
    campoProfesor.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    campoCurso = CTkComboBox(formCrear, values=cursos)
    campoCurso.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formCrear, text="Aceptar", command=lambda:(enviar(tabla, id), formCrear.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


def inhabilitar(tabla:ttk.Treeview):
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    if unableAsignacion(id) == 200:
        messagebox.showinfo("Eliminado", "asignacion eliminado correctamente")
    else:
        messagebox.showwarning("Error", "No se pudo eliminar nada")

def actualizarVista(tabla:ttk.Treeview, label:CTkLabel):
    seleccion = tabla.focus()
    id_seleccionado = None



    if seleccion:
        valores = tabla.item(seleccion, "values")
        if valores and len(valores) > 0 and valores[0]:  # Aseguramos que hay ID
            try:
                id_seleccionado = int(valores[0])
            except Exception as e:
                print(f"[ERROR] ID inválido: {valores[0]}. Excepción: {e}")
                id_seleccionado = None

    for item in tabla.get_children():
        tabla.delete(item)

    datos = getAsignaciones()
    nuevo_focus = None

    for dato in datos:
        fila_id = tabla.insert("", "end", values=(
            dato["idProfesorCurso"], 
            dato["curso"]["nombre"], 
            dato["profesor"]["nombre"],
            dato["estado"]
        ))
        if id_seleccionado is not None and dato["idProfesorCurso"] == id_seleccionado:
            nuevo_focus = fila_id

    if nuevo_focus:
        tabla.focus(nuevo_focus)
        tabla.selection_set(nuevo_focus)
        tabla.see(nuevo_focus)

def desplegarasignacions(padre: CTk):
    ventana = CTkToplevel(padre)
    ventana.title("Vista de asignaciones")
    ventana.grab_set()
    ventana.resizable(width=False, height=False)
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    try:
        frameTitulo = CTkFrame(ventana, height=75, fg_color="black")
        frameBotones = CTkFrame(ventana)
        frameTabla = CTkFrame(ventana)
        frameInfo = CTkScrollableFrame(ventana)

        labelInfo = CTkLabel(frameInfo, text="Aqui ira info", wraplength=250)
        titulo = CTkLabel(frameTitulo, text="Modulo asignacions", font=("Arial", 15, "bold"))
        btnCrear = CTkButton(frameBotones, text="Crear asignacion", command=lambda:crear(ventana, tabla))
        btnModificar = CTkButton(frameBotones, text="Modificar asignacion", command=lambda:modificar(ventana, tabla))
        btnInhabilitar = CTkButton(frameBotones, text="Inhabilitar asignacion", command=lambda:(inhabilitar(tabla), actualizarVista(tabla, labelInfo)))
        btnActualizar = CTkButton(frameBotones, text="Actualizar vista", command=lambda:actualizarVista(tabla, labelInfo))

        columnas = ["idasignacion", "Curso", "Profesor"]

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

