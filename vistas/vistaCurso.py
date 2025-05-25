from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
from servicios.cursoService import *

colorBase = "red"

def al_cerrar(padre: CTk, ventana: CTkToplevel):
    padre.wm_deiconify()
    padre.lift()
    padre.focus_force()
    ventana.destroy()
    
def crear(padre: CTkToplevel, tabla:ttk.Treeview):
    def enviar(tabla):
        cur = {
            "nombre": campoNombre.get(),
            "estado": True
        }
        insertCurso(cur)
        try:
            actualizarVista(tabla)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "Curso agregado exitosamente")

    formCrear = CTkToplevel(padre)
    formCrear.title("Crear Curso")
    formCrear.lift()
    formCrear.grab_set()
    formCrear.focus_force()
    
    CTkLabel(formCrear, text="Nombre del Curso").grid(row=0, column=0)

    campoNombre = CTkEntry(formCrear)
    campoNombre.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formCrear, text="Aceptar", command=lambda:(enviar(tabla), formCrear.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def modificar(padre: CTkToplevel, tabla:ttk.Treeview):
    def enviar(tabla, id):
        cur = {
            "idCurso": int(id),
            "nombre": campoNombre.get(),
            "estado": True
        }
        modifyCurso(id, cur)
        try:
            actualizarVista(tabla)
        except:
            print("Error actualizando")
        messagebox.showinfo("Agregado", "Curso modificado exitosamente")

    #Obtener el id
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    formModificar = CTkToplevel(padre)
    formModificar.title("Modificar Curso")
    formModificar.lift()
    formModificar.grab_set()
    formModificar.focus_force()
    
    CTkLabel(formModificar, text="Nombre del Curso").grid(row=0, column=0)

    campoNombre = CTkEntry(formModificar)
    campoNombre.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    CTkButton(formModificar, text="Aceptar", command=lambda:(enviar(tabla, id), formModificar.destroy())).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def inhabilitar(tabla:ttk.Treeview):
    seleccion = tabla.selection()
    valores = tabla.item(seleccion, "values")
    id = valores[0]

    if unableCurso(id) == 200:
        messagebox.showinfo("Eliminado", "Curso eliminado correctamente")
    else:
        messagebox.showwarning("Error", "No se pudo eliminar nada")

def actualizarVista(tabla:ttk.Treeview):

    # Guardar el ID del Curso seleccionado
    seleccion = tabla.focus()
    id_seleccionado = None
    if seleccion:
        valores = tabla.item(seleccion, "values")
        if valores:
            id_seleccionado = valores[0]  # El ID está en la primera columna

    for item in tabla.get_children():
        tabla.delete(item)

    datos = getCursos()
    for dato in datos:
        fila_id = tabla.insert("", "end", values=(dato["idCurso"], 
                                                  dato["nombre"],
                                                dato["estado"]))
        # Si coincide el ID, guardar ese item para volver a enfocarlo
        if str(dato["idCurso"]) == str(id_seleccionado):
            nuevo_focus = fila_id
        # Restaurar el enfoque y selección
    if nuevo_focus:
        tabla.focus(nuevo_focus)
        tabla.selection_set(nuevo_focus)
        tabla.see(nuevo_focus)

def desplegarCursos(padre: CTk):
    ventana = CTkToplevel(padre)
    ventana.title("Vista de Cursos")
    ventana.grab_set()
    ventana.resizable(width=False, height=False)
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)
    padre.withdraw()

    try:
        frameTitulo = CTkFrame(ventana, height=75, fg_color="pink")
        frameBotones = CTkFrame(ventana)
        frameTabla = CTkFrame(ventana)

        titulo = CTkLabel(frameTitulo, text="Modulo Cursos", font=("Arial", 15, "bold"))
        btnCrear = CTkButton(frameBotones, text="Crear Curso", command=lambda:crear(ventana, tabla))
        btnModificar = CTkButton(frameBotones, text="Modificar Curso", command=lambda:modificar(ventana, tabla))
        btnInhabilitar = CTkButton(frameBotones, text="Inhabilitar Curso", command=lambda:(inhabilitar(tabla), actualizarVista(tabla)))
        btnActualizar = CTkButton(frameBotones, text="Actualizar vista", command=lambda:actualizarVista(tabla))

        columnas = ["idCurso", "nombre", "estado"]

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

        ventana.protocol("WM_DELETE_WINDOW", lambda: al_cerrar(padre, ventana))
        ventana.wait_window()  # se detiene hasta que ventana se cierre
    
    finally:      
        padre.wm_deiconify()
        padre.lift()
        padre.focus_force()

