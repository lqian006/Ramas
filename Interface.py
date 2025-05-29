import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from Proyecto.V1.path import *
from Proyecto.test_graph import *
from Proyecto.V1.graph import *
from Proyecto.V1.node import *
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseEvent
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ---Variables globales---#
modo_click = None
segmento_click = []
Grafo1 = CreateGraph_1()
Grafo2 = Graph()

grafos = {"Grafo predeterminado": Grafo1, "Grafo modificado": Grafo2}
g_actual = Grafo1

# Variables para el estado de los botones
boton_nodo_activo = False
boton_segmento_activo = False

#---Funciones---#



def cargar_grafo_desde_explorador():
    filepaths = filedialog.askopenfilenames(
        title="Selecciona los archivos del grafo (3 archivos)",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )

    if not filepaths:
        return

    if len(filepaths) != 3:
        messagebox.showerror("Error", "Debes seleccionar exactamente 3 archivos")
        return

    try:
        global Grafo2, g_actual
        Grafo2 = Graph()  # Reiniciamos el grafo modificado

        for filepath in filepaths:
            temp_graph = LoadGraphFromFile(filepath)
            # Aquí implementa tu lógica para combinar los grafos

        g_actual = Grafo2
        grafos["Grafo modificado"] = Grafo2
        combo_grafos.set("Grafo modificado")
        mostrar_grafo_actual()
        messagebox.showinfo("Éxito", f"Grafo cargado desde {len(filepaths)} archivos")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar los archivos: {str(e)}")
        mostrar_grafo_original()


def seleccionar_grafo(event):
    global g_actual
    seleccion = combo_grafos.get()
    g_actual = grafos[seleccion]
    mostrar_grafo_actual()


def mostrar_grafo_original():
    global g_actual
    g_actual = Grafo1
    combo_grafos.set("Grafo predeterminado")
    mostrar_grafo_actual()


def mostrar_grafo_actual():
    fig, ax = plt.subplots()
    Plot(g_actual)

    # Limpiamos el frame antes de mostrar nuevo gráfico
    for widget in graph_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.config(width=700, height=600)
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    canvas.mpl_connect("button_press_event", on_click)
    canvas.draw()


def mostrar_vecinos():
    nodo = entry_vecino.get().strip()
    if nodo:
        try:
            fig, ax = plt.subplots()
            PlotNode(g_actual, nodo)
            mostrar_figura(fig)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron mostrar los vecinos: {str(e)}")
            mostrar_grafo_original()


def añadir_nodo():
    nombre = entry_nombre.get().strip()
    try:
        x = float(entry_x.get().strip())
        y = float(entry_y.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Coordenadas inválidas")
        return

    if nombre:
        AddNode(g_actual, Node(nombre, x, y))
        mostrar_grafo_actual()


def añadir_nodo_manualmente():
    global modo_click, boton_nodo_activo, boton_segmento_activo

    # Si ya está activo, lo desactivamos
    if boton_nodo_activo:
        modo_click = None
        boton_nodo_activo = False
        btn_nodo_manual.config(relief=tk.RAISED, bg='SystemButtonFace')

    else:
        # Desactivamos primero el modo segmento si estaba activo
        if boton_segmento_activo:
            modo_click = None
            boton_segmento_activo = False
            btn_segmento_manual.config(relief=tk.RAISED, bg='SystemButtonFace')

        # Activamos el modo nodo
        modo_click = "nodo"
        boton_nodo_activo = True
        btn_nodo_manual.config(relief=tk.SUNKEN, bg='light grey')


def añadir_segmento_manualmente():
    global modo_click, segmento_click, boton_segmento_activo, boton_nodo_activo

    # Si ya está activo, lo desactivamos
    if boton_segmento_activo:
        modo_click = None
        segmento_click.clear()
        boton_segmento_activo = False
        btn_segmento_manual.config(relief=tk.RAISED, bg='SystemButtonFace')
    else:
        # Desactivamos primero el modo nodo si estaba activo
        if boton_nodo_activo:
            modo_click = None
            boton_nodo_activo = False
            btn_nodo_manual.config(relief=tk.RAISED, bg='SystemButtonFace')

        # Activamos el modo segmento
        modo_click = "segmento"
        segmento_click.clear()
        boton_segmento_activo = True
        btn_segmento_manual.config(relief=tk.SUNKEN, bg='light grey')

def añadir_segmento():
    origen = entry_origen.get().strip()
    destino = entry_destino.get().strip()
    if origen and destino:
        AddSegment(g_actual, origen + destino, origen, destino)
        mostrar_grafo_actual()


def eliminar_nodo():
    nombre = entry_borrar.get().strip()
    if nombre:
        DeleteNode(g_actual, nombre)
        mostrar_grafo_actual()


def on_click(event):
    global modo_click, segmento_click, boton_nodo_activo, boton_segmento_activo

    if not event.inaxes:
        return

    x = event.xdata
    y = event.ydata

    if modo_click == "nodo":
        nombre = entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Nombre requerido", "Por favor, escribe un nombre para el nodo antes de hacer clic.")
            return
        AddNode(g_actual, Node(nombre, x, y))
        entry_nombre.delete(0, tk.END)
        mostrar_grafo_actual()

    elif modo_click == "segmento":
        nodo_clicado = GetClosest(g_actual, x, y)
        if nodo_clicado:
            segmento_click.append(nodo_clicado.name)
            if len(segmento_click) == 2:
                origen, destino = segmento_click
                AddSegment(g_actual, origen + destino, origen, destino)
                segmento_click.clear()
                mostrar_grafo_actual()

def guardar_grafo():
    nombre_archivo = entry_guardar.get().strip()
    if not nombre_archivo:
        nombre_archivo = "grafo_guardado.txt"
    if not nombre_archivo.endswith(".txt"):
        nombre_archivo += ".txt"
    SaveGraphToFile(g_actual, nombre_archivo)
    messagebox.showinfo("Guardado", f"Grafo guardado en {nombre_archivo}")


def nodos_alcanzables():
    nodo_inicio = entry_reachable.get().strip()
    if not nodo_inicio:
        messagebox.showwarning("Error", "Introduce el nodo de inicio")
        return

    try:
        fig, ax = plt.subplots()
        alcanzables = PlotReachable(g_actual, nodo_inicio)
        mostrar_figura(fig)

        if not alcanzables:
            messagebox.showinfo("Nodos alcanzables", f"No se encontraron nodos alcanzables desde {nodo_inicio}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron mostrar los nodos alcanzables: {str(e)}")
        mostrar_grafo_original()


def camino_mas_corto():
    origen = entry_camino_origen.get().strip()
    destino = entry_camino_destino.get().strip()
    if not origen or not destino:
        messagebox.showwarning("Error", "Introduce ambos nodos de origen y destino")
        return

    try:
        fig, ax = plt.subplots()
        camino = PlotShortestPath(g_actual, origen, destino)
        mostrar_figura(fig)

        if not camino:
            messagebox.showinfo("Camino más corto", f"No existe camino entre {origen} y {destino}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo calcular el camino más corto: {str(e)}")



def mostrar_figura(fig):
    # Limpiamos el frame antes de mostrar nuevo gráfico
    for widget in graph_frame.winfo_children():
        widget.destroy()

    try:
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.config(width=700, height=600)
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar el gráfico: {str(e)}")





# --------- INTERFAZ ---------
root = tk.Tk()
root.title("Editor de Grafos")
root.geometry("1200x700")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)
root.rowconfigure(0, weight=1)

# Contenedor del scroll
scroll_container = tk.Frame(root)
scroll_container.grid(row=0, column=0, padx=20, pady=5, sticky=tk.NSEW)

canvas_scroll = tk.Canvas(scroll_container)
scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas_scroll.yview)
canvas_scroll.configure(yscrollcommand=scrollbar.set)

# Frame con todos los botones
button_graph_frame = tk.LabelFrame(canvas_scroll, text="Opciones")
canvas_scroll.create_window((0, 0), window=button_graph_frame, anchor="nw")

# Configuración scroll
canvas_scroll.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


def actualizar_scroll(event):
    canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all"))


button_graph_frame.bind("<Configure>", actualizar_scroll)
canvas_scroll.bind_all("<MouseWheel>", lambda e: canvas_scroll.yview_scroll(int(-1 * (e.delta / 120)), "units"))

# Configuración de filas/columnas
for i in range(30):  # Reducido a 30 que es lo que necesitamos
    button_graph_frame.rowconfigure(i, weight=1)
button_graph_frame.columnconfigure(0, weight=1)

# Selector de grafo
tk.Label(button_graph_frame, text="Selecciona un grafo").grid(row=0, column=0, padx=5, pady=2, sticky=tk.NSEW)
combo_grafos = ttk.Combobox(button_graph_frame, values=list(grafos.keys()))
combo_grafos.set("Grafo predeterminado")
combo_grafos.grid(row=1, column=0, padx=50, pady=2, sticky=tk.NSEW)
combo_grafos.bind("<<ComboboxSelected>>", seleccionar_grafo)
# --- NUEVO BOTÓN PARA CARGAR ARCHIVO ---
tk.Button(
    button_graph_frame,
    text="📂 Cargar archivo nuevo",
    command=lambda: cargar_grafo_desde_explorador()
).grid(row=2, column=0, padx=50, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)


# Mostrar grafo
tk.Button(button_graph_frame, text="Mostrar grafo original", command=mostrar_grafo_original).grid(row=3, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)

# Vecinos
tk.Label(button_graph_frame, text="Ver vecinos de nodo:").grid(row=4, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
entry_vecino = tk.Entry(button_graph_frame)
entry_vecino.grid(row=5, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
tk.Button(button_graph_frame, text="Ver vecinos", command=mostrar_vecinos).grid(row=6, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)

# Añadir nodo
tk.Label(button_graph_frame, text="Añadir nodo (Nombre, X, Y):").grid(row=7, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
entry_nombre = tk.Entry(button_graph_frame)
entry_nombre.grid(row=8, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
entry_x = tk.Entry(button_graph_frame)
entry_x.grid(row=9, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
entry_y = tk.Entry(button_graph_frame)
entry_y.grid(row=10, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
tk.Button(button_graph_frame, text="Añadir nodo", command=añadir_nodo).grid(row=11, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)

btn_nodo_manual = tk.Button(button_graph_frame, text="Añadir nodo manualmente", command=añadir_nodo_manualmente)
btn_nodo_manual.grid(row=12, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)


# Añadir segmento
tk.Label(button_graph_frame, text="Añadir segmento (Origen, Destino):").grid(row=13, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
entry_origen = tk.Entry(button_graph_frame)
entry_origen.grid(row=14, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
entry_destino = tk.Entry(button_graph_frame)
entry_destino.grid(row=15, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
tk.Button(button_graph_frame, text="Añadir segmento", command=añadir_segmento).grid(row=16, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)

btn_segmento_manual = tk.Button(button_graph_frame, text="Añadir segmento manualmente", command=añadir_segmento_manualmente)
btn_segmento_manual.grid(row=17, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)


# Eliminar nodo
tk.Label(button_graph_frame, text="Eliminar nodo:").grid(row=18, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
entry_borrar = tk.Entry(button_graph_frame)
entry_borrar.grid(row=19, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
tk.Button(button_graph_frame, text="Eliminar nodo", command=eliminar_nodo).grid(row=20, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)

# Guardar grafo
tk.Label(button_graph_frame, text="Escribe el nombre del fichero:").grid(row=21, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
entry_guardar = tk.Entry(button_graph_frame)
entry_guardar.grid(row=22, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)
tk.Button(button_graph_frame, text="Guardar grafo", command=guardar_grafo).grid(row=23, column=0, padx=50, pady=5, sticky=tk.N +tk.E +tk.W +tk.S)

# Reachable
tk.Label(button_graph_frame, text="Nodo para ver alcanzables:").grid(row=24, column=0, padx=50, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
entry_reachable = tk.Entry(button_graph_frame)
entry_reachable.grid(row=25, column=0, padx=50, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
tk.Button(button_graph_frame, text="Ver alcanzables", command=nodos_alcanzables).grid(row=26, column=0, padx=50, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

# Shortest Path
tk.Label(button_graph_frame, text="Camino más corto (Origen, Destino):").grid(row=27, column=0, padx=50, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
entry_camino_origen = tk.Entry(button_graph_frame)
entry_camino_origen.grid(row=28, column=0, padx=50, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
entry_camino_destino = tk.Entry(button_graph_frame)
entry_camino_destino.grid(row=29, column=0, padx=50, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
tk.Button(button_graph_frame, text="Mostrar camino más corto", command=camino_mas_corto).grid(row=30, column=0, padx=50, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)


# --- PARTE DERECHA DE LA INTERFAZ ---

graph_frame = tk.LabelFrame(root, text="Grafo")
graph_frame.grid(row=0, column=1, padx=20, pady=5, sticky=tk.NSEW)
graph_frame.rowconfigure(0, weight=1)
graph_frame.columnconfigure(0, weight=1)

# Mostrar grafo inicial al abrir la aplicación
mostrar_grafo_original()

root.mainloop()



