from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
from servicios.aulaService import *
from servicios.cursoService import *
from servicios.profesorService import *
from PIL import Image

colorBase = "red"
    
def crear(padre: CTkFrame, tabla:ttk.Treeview, label:CTkLabel):
    def enviar(tabla):

        textoCurso = str(campoCurso.get()).split("-")
        textoProfesor = str(campoProfesor.get()).split("-")

        aula = {
            "cursoId": int(textoCurso[0]),
            "profesorId": int(textoProfesor[0]),
            "estado": True
        }
        insertAula(aula)
        try:
            actualizarVista(tabla, label)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "Aula agregada exitosamente")

    formCrear = CTkToplevel(padre)
    formCrear.title("Crear Aula")
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

def modificar(padre: CTkFrame, tabla:ttk.Treeview, label:CTkLabel):
    def enviar(tabla, id):
        textoCurso = str(campoCurso.get()).split("-")
        textoProfesor = str(campoProfesor.get()).split("-")

        aula = {
            "idProfesorCurso": id,
            "cursoId": int(textoCurso[0]),
            "profesorId": int(textoProfesor[0]),
            "estado": True
        }
        modifyAula(id, aula)
        try:
            actualizarVista(tabla, label)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "Aula modificada exitosamente")

    #Obtener el id
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    formCrear = CTkToplevel(padre)
    formCrear.title("Crear Aula")
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

    if unableAula(id) == 200:
        messagebox.showinfo("Eliminado", "Aula eliminado correctamente")
    else:
        messagebox.showwarning("Error", "No se pudo eliminar nada")

def actualizarVista(tabla:ttk.Treeview, label:CTkLabel, buscar = None):

    try:
        filtro = buscar.get()
    except:
        filtro = ""


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

    if id_seleccionado is not None:
        total = getTotalAula(id_seleccionado)
        label.configure(text=f"Estudiantes asignados: {total}")
    else:
        label.configure(text="No hay información")




    for item in tabla.get_children():
        tabla.delete(item)

    datos = getAulas()
    nuevo_focus = None

    for dato in datos:

        if (filtro.lower() in str(dato["idProfesorCurso"]).lower()) or (filtro.lower() in str(dato["curso"]["nombre"]).lower()) or (filtro.lower() in str(dato["profesor"]["nombre"]).lower()):
            fila_id = tabla.insert("", "end", values=(
                dato["idProfesorCurso"], 
                dato["curso"]["nombre"], 
                dato["profesor"]["nombre"],
                dato["estado"]
            ))
        if id_seleccionado is not None and dato["idProfesorCurso"] == id_seleccionado:
            nuevo_focus = fila_id

    try:
        if nuevo_focus:
            tabla.focus(nuevo_focus)
            tabla.selection_set(nuevo_focus)
            tabla.see(nuevo_focus)
    
    except:
        print("Continuemos")

def desplegarAulas(padre: CTkFrame):

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

    frameTitulo = CTkFrame(ventana, height=75, fg_color="black")
    frameBotones = CTkFrame(ventana)
    frameTabla = CTkFrame(ventana)
    frameInfo = CTkScrollableFrame(ventana)

    labelInfo = CTkLabel(frameInfo, text="Aqui ira info", wraplength=250)
    titulo = CTkLabel(frameTitulo, text="Modulo Aulas", font=("Arial", 15, "bold"), text_color="white")
    btnCrear = CTkButton(frameBotones, text="", image=icono1, compound="left", command=lambda:crear(ventana, tabla, labelInfo))
    btnModificar = CTkButton(frameBotones, text="", image=icono2, compound="left", command=lambda:modificar(ventana, tabla, labelInfo))
    btnInhabilitar = CTkButton(frameBotones, text="", image=icono3, compound="left", command=lambda:(inhabilitar(tabla), actualizarVista(tabla, labelInfo)))
    btnActualizar = CTkButton(frameBotones, text="", image=icono4, compound="left", command=lambda:actualizarVista(tabla, labelInfo))

    columnas = ["idAula", "Curso", "Profesor"]

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

    #Buscador
    buscador = CTkEntry(frameTitulo, width=300)
    botonBuscar = CTkButton(frameTitulo, text="Buscar", command=lambda:actualizarVista(tabla, labelInfo, buscador))


    #Organizacion de botones y tabla
    titulo.grid(column = 0, row=0, sticky="nsew", padx=10, pady=10)

    buscador.grid(column = 1, row = 0, sticky ="ew", pady = 10, padx = 10)
    botonBuscar.grid(column = 2, row= 0, sticky = "ew", pady = 10, padx = 10)

    btnCrear.grid(column = 0, row = 0, sticky="nsew", padx=10, pady=10)
    btnModificar.grid(column = 0, row = 1, sticky="nsew", padx=10, pady=10)
    btnInhabilitar.grid(column = 0, row =2, sticky="nsew", padx=10, pady=10)
    btnActualizar.grid(column = 0, row = 3, sticky="nsew", padx=10, pady=10)
    labelInfo.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "nsew")

    tabla.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    scrollX.grid(row=1, column=0, sticky="ew")
    scrollY.grid(row=0, column=1, sticky="ns")

    actualizarVista(tabla, labelInfo)
    ventana.grid(row=0, column=0, sticky="nsew")  # o pack(), si preferís

