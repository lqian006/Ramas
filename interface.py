import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from graph import *

global current_graph

def canvasplot(g, space):
    fig = Figure(figsize=(6,5))
    ax = fig.add_subplot(111)
    for punto in g.nodes:
        ax.plot(punto.coordx,punto.coordy, marker = "o", color = "red")
        ax.text(punto.coordx+0.25, punto.coordy+0.25, punto.name, fontsize = 7.5, color = "green")
    for linea in g.segments:
        ax.annotate("",
                    (linea.destination_node.coordx,linea.destination_node.coordy),
                    (linea.origin_node.coordx,linea.origin_node.coordy),
                    arrowprops=dict(arrowstyle="->", color="blue",lw=1.5))
        ax.text((linea.origin_node.coordx+linea.destination_node.coordx)/2,(linea.origin_node.coordy+linea.destination_node.coordy)/2,linea.cost,fontsize=7.5)
    ax.margins(x=0.25,y=0.25)
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=space)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=0, sticky="nsew")

def canvasfile(g, file_name):
    F = open("{}".format(file_name), "r")
    linea = F.readline()
    i = 0
    while linea != "\n":
        datos1 = linea.split()
        AddNode(g, Node(datos1[0], int(datos1[1]), int(datos1[2])))
        i += 1
        linea = F.readline()
    i += 1
    linea = F.readline()
    while linea != "":
        datos2 = linea.split()
        AddSegment(g, datos2[0], datos2[1], datos2[2])
        i += 1
        linea = F.readline()
    F.close()
    canvasplot(g,canvas_picture)

def canvasplotnode(g, space, nameOrigin):
    fig = Figure(figsize=(6,5))
    ax = fig.add_subplot(111)
    node1 = None
    found = False
    neighbors = []
    for node in g.nodes:
        if node.name == nameOrigin:
            node1 = node
            found = True
    if found == False:
        return False
    ax.plot(node1.coordx, node1.coordy, color="blue", marker="o")
    ax.text(node1.coordx + 0.5, node1.coordy + 0.5, node1.name, fontsize=7.5)
    for point in node1.neighbors:
        ax.plot(point.coordx, point.coordy, color="green", marker="o")
        ax.text(point.coordx + 0.5, point.coordy + 0.5, point.name, fontsize=7.5)
        neighbors.append(point)
    for element in g.nodes:
        if element != node1 and element not in neighbors:
            ax.plot(element.coordx, element.coordy, color="gray", marker="o")
            ax.text(element.coordx + 0.25, element.coordy + 0.25, element.name, fontsize=7.5)
    for segment in neighbors:
        ax.annotate("", (segment.coordx, segment.coordy),
                     (node1.coordx, node1.coordy),
                     arrowprops=dict(arrowstyle="->", color="red", lw=1.5))
        ax.text((node1.coordx + segment.coordx) / 2,
                 (node1.coordy + segment.coordy) / 2, Distance(node1, segment), fontsize=7.5)
    ax.grid(True)
    ax.margins(x=0.25, y=0.25)

    canvas = FigureCanvasTkAgg(fig, master=space)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=0, sticky="nsew")

def showexamplegraph():
    global current_graph
    current_graph = CreateGraph_1()
    canvasplot(current_graph,canvas_picture)

def showfilegraph():
    global current_graph
    current_graph = Graph()
    canvasfile(current_graph, infile.get())

def shownode():
    global current_graph
    canvasplotnode(current_graph, canvas_picture, str(selnode.get()))

ventana = tk.Tk()
ventana.geometry("800x400")
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1, weight=3)
ventana.rowconfigure(0, weight=3)

izquierda = tk.LabelFrame(ventana, text="Control")
izquierda.grid(row=0, column=0, sticky="nsew")
izquierda.rowconfigure([0,1,2],weight=1)
izquierda.columnconfigure(0, weight=1)
derecha = tk.LabelFrame(ventana, text="Grafica")
derecha.grid(row=0, column=1, sticky="nsew")
derecha.columnconfigure(0, weight=1)
derecha.rowconfigure(0, weight=1)

button1 = tk.Button(izquierda,text="Grafico Ejemplo", command=showexamplegraph)
button1.grid(column=0, row=0, pady=5, sticky="nsew")

fileframe = tk.LabelFrame(izquierda, text="Archivos")
fileframe.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")
fileframe.columnconfigure(0, weight=1)
fileframe.rowconfigure(0, weight=1)
fileframe.rowconfigure(1, weight=1)
infile = tk.Entry(fileframe)
infile.grid(row=0, column=0 ,pady=5, sticky="nsew")
btnfile = tk.Button(fileframe, text="Cargar Grafo", command=showfilegraph)
btnfile.grid(row=1, column=0, pady=5, sticky="nsew")

nodeframe = tk.LabelFrame(izquierda, text="Nodos")
nodeframe.grid(column=0, row=2, pady=5, padx=5, sticky="nsew")
nodeframe.rowconfigure(0, weight=1)
nodeframe.rowconfigure(1, weight=1)
nodeframe.columnconfigure(0, weight=1)
selnode = tk.Entry(nodeframe)
selnode.grid(column=0, row=0, pady=5, sticky="nsew")
btnnode = tk.Button(nodeframe, text="Seleccionar Nodo", command=shownode)
btnnode.grid(column=0, row=1, pady=5, sticky="nsew")

canvas_picture = tk.Frame(derecha)
canvas_picture.grid(column=1, rowspan=5, pady=5, padx=5, sticky="nsew")
canvas_picture.columnconfigure(0, weight=1)
canvas_picture.rowconfigure(0,weight=1)

ventana.mainloop()