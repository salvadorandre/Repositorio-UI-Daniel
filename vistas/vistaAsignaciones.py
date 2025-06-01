from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
from servicios.asignacionesService import *
from servicios.cursoService import *
from servicios.profesorService import *
from servicios.estudianteService import *
from servicios.aulaService import *
from PIL import Image

colorBase = "red"
    
def crear(padre: CTkFrame, tabla:ttk.Treeview):
    def enviar(tabla):

        textoEstudiante = str(campoEstudiante.get()).split("-")
        textoAula = str(campoAula.get()).split("-")

        asignacion = {
            "estudianteId": int(textoEstudiante[0]),
            "profesorCursoId": int(textoAula[0]),
            "estado": True
        }
        insertAsignacion(asignacion)
        try:
            actualizarVista(tabla)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "asignacion agregada exitosamente")

    formCrear = CTkToplevel(padre)
    formCrear.title("Crear asignacion")
    formCrear.lift()
    formCrear.grab_set()
    formCrear.focus_force()
    
    CTkLabel(formCrear, text="Estudiante").grid(row=0, column=0)
    CTkLabel(formCrear, text="Aula").grid(row=3, column=0)

    #Obtener columnas
    datos = getEstudiantes()
    estudiantes = []

    for dato in datos:
        text = str(dato["idEstudiante"]) + "-" + str(dato["nombre"])
        estudiantes.append(text)


    datos = getAulas()
    aulas = []

    for dato in datos:
        text = str(dato["idProfesorCurso"]) + "-" + str(dato["profesor"]["nombre"] + "-" + str(dato["curso"]["nombre"]))
        aulas.append(text)


    campoEstudiante = CTkComboBox(formCrear, values=estudiantes)
    campoEstudiante.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    campoAula = CTkComboBox(formCrear, values=aulas)
    campoAula.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formCrear, text="Aceptar", command=lambda:(enviar(tabla), formCrear.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def modificar(padre: CTkFrame, tabla:ttk.Treeview):
    def enviar(tabla, id):

        textoEstudiante = str(campoEstudiante.get()).split("-")
        textoAula = str(campoAula.get()).split("-")

        asignacion = {
            "idAsignacion": int(id),
            "estudianteId": int(textoEstudiante[0]),
            "profesorCursoId": int(textoAula[0]),
            "estado": True
        }
        modifyAsignacion(id, asignacion)
        try:
            actualizarVista(tabla)
        except Exception as e:
            f"[ERROR] No se pudo actualizar la tabla: {e}"
        messagebox.showinfo("Agregado", "Asignacion modificada exitosamente")

    #Obtener el id
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    formCrear = CTkToplevel(padre)
    formCrear.title("Crear asignacion")
    formCrear.lift()
    formCrear.grab_set()
    formCrear.focus_force()
    
    CTkLabel(formCrear, text="Estudiante").grid(row=0, column=0)
    CTkLabel(formCrear, text="Aula").grid(row=3, column=0)

    #Obtener columnas
    datos = getEstudiantes()
    estudiantes = []

    for dato in datos:
        text = str(dato["idEstudiante"]) + "-" + str(dato["nombre"])
        estudiantes.append(text)


    datos = getAulas()
    aulas = []

    for dato in datos:
        text = str(dato["idProfesorCurso"]) + "-" + str(dato["profesor"]["nombre"] + "-" + str(dato["curso"]["nombre"]))
        aulas.append(text)


    campoEstudiante = CTkComboBox(formCrear, values=estudiantes)
    campoEstudiante.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    campoAula = CTkComboBox(formCrear, values=aulas)
    campoAula.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formCrear, text="Aceptar", command=lambda:(enviar(tabla, id), formCrear.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def inhabilitar(tabla:ttk.Treeview):
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    if unableAsignacion(id) == 200:
        messagebox.showinfo("Eliminado", "asignacion eliminado correctamente")
    else:
        messagebox.showwarning("Error", "No se pudo eliminar nada")

def actualizarVista(tabla:ttk.Treeview):
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
            dato["idAsignacion"], 
            dato["fecha"], 
            dato["estudiante"]["nombre"],
            dato["curso"]["nombre"],
            dato["profesor"]["nombre"]
        ))
        if id_seleccionado is not None and dato["idAsignacion"] == id_seleccionado:
            nuevo_focus = fila_id

    try:
        if nuevo_focus:
            tabla.focus(nuevo_focus)
            tabla.selection_set(nuevo_focus)
            tabla.see(nuevo_focus)
    
    except:
        print("Continuemos")

def desplegarAsignaciones(padre: CTkFrame):

    imagenCrear = Image.open("assets/archivo-de-edicion.png")
    imagenModificar = Image.open("assets/pinza-para-boligrafo.png")
    imagenEliminar = Image.open("assets/basura.png")
    imagenActualizar = Image.open("assets/actualizar.png")

    icono1 = CTkImage(dark_image=imagenCrear, size=(20, 20))
    icono2 = CTkImage(dark_image=imagenModificar, size=(20, 20))
    icono3 = CTkImage(dark_image=imagenEliminar, size=(20, 20))
    icono4 = CTkImage(dark_image=imagenActualizar, size=(20, 20))



    ventana = CTkFrame(padre)
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    frameTitulo = CTkFrame(ventana, height=75, fg_color="purple")
    frameBotones = CTkFrame(ventana)
    frameTabla = CTkFrame(ventana)

    titulo = CTkLabel(frameTitulo, text="Modulo asignaciones", font=("Arial", 15, "bold"))
    btnCrear = CTkButton(frameBotones, text="", image=icono1, compound="left", command=lambda:crear(ventana, tabla))
    btnModificar = CTkButton(frameBotones, text="", image=icono2, compound="left", command=lambda:modificar(ventana, tabla))
    btnInhabilitar = CTkButton(frameBotones, text="", image=icono3, compound="left", command=lambda:(inhabilitar(tabla), actualizarVista(tabla)))
    btnActualizar = CTkButton(frameBotones, text="", image=icono4, compound="left", command=lambda:actualizarVista(tabla))

    columnas = ["idAsignacion", "fecha", "estudiante", "curso", "profesor"]

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

    #Organizacion de botones y tabla
    titulo.grid(column = 0, row=0, sticky="nsew", padx=10, pady=10)
    btnCrear.grid(column = 0, row = 0, sticky="nsew", padx=10, pady=10)
    btnModificar.grid(column = 0, row = 1, sticky="nsew", padx=10, pady=10)
    btnInhabilitar.grid(column = 0, row =2, sticky="nsew", padx=10, pady=10)
    btnActualizar.grid(column = 0, row = 3, sticky="nsew", padx=10, pady=10)


    tabla.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    scrollX.grid(row=1, column=0, sticky="ew")
    scrollY.grid(row=0, column=1, sticky="ns")

    actualizarVista(tabla)
    ventana.grid(row=0, column=0, sticky="nsew")  # o pack(), si preferís
