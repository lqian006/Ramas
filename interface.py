import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


from graph import *
from airSpace import *

current_graph = None        #gráfica actual
currentairspace = None      #espacio aéreo actual
graphcanvas = None          #widget del canvas
figuracanvas = None         #figura que tiene la gráfica en cada instante
clic = None                 #dónde está conectada la función de detectar clic?
usonodos = False            #la opcion de detectar clic está activada?
usoseg = False              #la opcion de detectar clic está activada?
contnode = 1                #numero de nodos añadidos manualmente
contseg = 1                 #número de segmentos añadidos manualmente
contnodseg = 1
punto = None                #coordenadas del último clic
punto1 = None
punto2 = None

def detectclick(event):
    global punto
    x = round(event.xdata,3)
    y = round(event.ydata,3)
    punto = [x,y]
    print(punto)

def showcatalonia():
    global current_graph, graphcanvas, figuracanvas, contnodseg
    A = AirSpace()
    LoadAirSpace(A, "Cat")
    if graphcanvas is not None:
        graphcanvas.destroy()
    fig, ax = plt.subplots()
    PlotAirSpace(A)
    figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
    figuracanvas.draw()
    figuracanvas.mpl_connect("button_press_event", detectclick)
    graphcanvas = figuracanvas.get_tk_widget()
    graphcanvas.config(width=800, height=600)
    graphcanvas.pack()
    contnodseg = 0

def showspain():
    global current_graph, graphcanvas, figuracanvas, contnodseg
    A = AirSpace()
    LoadAirSpace(A, "Spain")
    if graphcanvas is not None:
        graphcanvas.destroy()
    fig, ax = plt.subplots()
    PlotAirSpace(A)
    figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
    figuracanvas.draw()
    figuracanvas.mpl_connect("button_press_event", detectclick)
    graphcanvas = figuracanvas.get_tk_widget()
    graphcanvas.config(width=800, height=600)
    graphcanvas.pack()
    contnodseg = 0

def showeurope():
    global current_graph, graphcanvas, figuracanvas, contnodseg, currentairspace
    A = AirSpace()
    LoadAirSpace(A, "ECAC")
    if graphcanvas is not None:
        graphcanvas.destroy()
    fig, ax = plt.subplots()
    PlotAirSpace(A)
    figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
    figuracanvas.draw()
    figuracanvas.mpl_connect("button_press_event", detectclick)
    graphcanvas = figuracanvas.get_tk_widget()
    graphcanvas.config(width=800, height=600)
    graphcanvas.pack()
    contnodseg = 0

def showexamplegraph():
    global current_graph, graphcanvas, figuracanvas, contnodseg
    current_graph = CreateGraph_1()
    if graphcanvas is not None:
        graphcanvas.destroy()
    fig, ax = plt.subplots()
    Plot(current_graph)
    figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
    figuracanvas.draw()
    figuracanvas.mpl_connect("button_press_event", detectclick)
    graphcanvas = figuracanvas.get_tk_widget()
    graphcanvas.config(width=800, height=600)
    graphcanvas.pack()
    contnodseg = 0

def showfilegraph():
    global current_graph, graphcanvas, figuracanvas
    current_graph = Graph()
    if graphcanvas is not None:
        graphcanvas.destroy()
    fig, ax = plt.subplots()
    FileGraph(current_graph, str(infile.get()))
    infile.delete(0, tk.END)
    figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
    figuracanvas.draw()
    figuracanvas.mpl_connect("button_press_event", detectclick)
    graphcanvas = figuracanvas.get_tk_widget()
    graphcanvas.config(width=800, height=600)
    graphcanvas.pack()

def shownode():
    global current_graph, graphcanvas, figuracanvas
    if graphcanvas is not None:
        graphcanvas.destroy()
    fig, ax = plt.subplots()
    PlotNode(current_graph, str(selnode.get()))
    figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
    figuracanvas.draw()
    figuracanvas.mpl_connect("button_press_event", detectclick)
    graphcanvas = figuracanvas.get_tk_widget()
    graphcanvas.config(width=800, height=600)
    graphcanvas.pack()

def addnodei():
    global current_graph, graphcanvas, figuracanvas
    if current_graph is None:
        messagebox.showerror("Error","No existe grafo al que añadir el nodo.")
    else:
        AddNode(current_graph, Node(str(nodename.get()),float(nodex.get()),float(nodey.get())))
        nodename.delete(0,tk.END)
        nodex.delete(0,tk.END)
        nodey.delete(0,tk.END)
        if graphcanvas is not None:
            graphcanvas.destroy()
        fig, ax = plt.subplots()
        Plot(current_graph)
        figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
        figuracanvas.draw()
        figuracanvas.mpl_connect("button_press_event", detectclick)
        graphcanvas = figuracanvas.get_tk_widget()
        graphcanvas.config(width=800, height=600)
        graphcanvas.pack()

def addsegmenti():
    global current_graph, graphcanvas, figuracanvas
    if current_graph is None:
        messagebox.showerror("Error", "No existe grafo al que añadir el segmento.")
    elif AddSegment(current_graph, segmentname.get(), segmentorigin.get(), segmentdestination.get()):
        segmentname.delete(0, tk.END)
        segmentorigin.delete(0, tk.END)
        segmentdestination.delete(0, tk.END)
        if graphcanvas is not None:
            graphcanvas.destroy()
        fig, ax = plt.subplots()
        Plot(current_graph)
        figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
        figuracanvas.draw()
        figuracanvas.mpl_connect("button_press_event", detectclick)
        graphcanvas = figuracanvas.get_tk_widget()
        graphcanvas.config(width=800, height=600)
        graphcanvas.pack()
    else:
        messagebox.showerror("Error", "Uno de los nodos no existe en el grafo")

def deletenodei():
    global current_graph, graphcanvas, figuracanvas
    if current_graph is None:
        messagebox.showerror("Error", "No existe grafo del que borrar nodo")
    else:
        if inborrarnodo.get():
            nodoborrar = str(inborrarnodo.get())
            if not deletenode(current_graph,nodoborrar):
                messagebox.showerror("Error","No existe ese nodo en el grafo actual.")
            else:
                inborrarnodo.delete(0, tk.END)
                if graphcanvas is not None:
                    graphcanvas.destroy()
                fig, ax = plt.subplots()
                Plot(current_graph)
                figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
                figuracanvas.draw()
                figuracanvas.mpl_connect("button_press_event", detectclick)
                graphcanvas = figuracanvas.get_tk_widget()
                graphcanvas.config(width=800, height=600)
                graphcanvas.pack()
        elif inborrarseg.get():
            segborrar = str(inborrarseg.get())
            if not deleteseg(current_graph, segborrar):
                messagebox.showerror("Error", "No existe segmento con ese nombre.\nPrueba a cambiar el orden de sus nodos")
            else:
                inborrarseg.delete(0, tk.END)
                if graphcanvas is not None:
                    graphcanvas.destroy()
                fig, ax = plt.subplots()
                Plot(current_graph)
                figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
                figuracanvas.draw()
                figuracanvas.mpl_connect("button_press_event", detectclick)
                graphcanvas = figuracanvas.get_tk_widget()
                graphcanvas.config(width=800, height=600)
                graphcanvas.pack()

def createblank():
    global current_graph, graphcanvas, figuracanvas, contnodseg, usonodos, usoseg
    if graphcanvas is not None:
        graphcanvas.destroy()
    current_graph = Graph()
    fig, ax = plt.subplots()
    Plot(current_graph)
    figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
    figuracanvas.draw()
    figuracanvas.mpl_connect("button_press_event", detectclick)
    graphcanvas = figuracanvas.get_tk_widget()
    graphcanvas.config(width=800, height=600)
    graphcanvas.pack()
    contnodseg = 0
    usonodos = False
    usoseg = False
    print(usoseg, usonodos)
    btnhandseg.config(bg="#f0f0f0")
    btnhandnode.config(bg="#f0f0f0")

def savegraph():
    global current_graph
    name = insave.get()+".txt"
    F = open(name, "w")
    for nodo in current_graph.nodes:
        F.write("{} {} {}\n".format(nodo.name, nodo.coordx, nodo.coordy))
        print("{} {} {}\n".format(nodo.name, nodo.coordx, nodo.coordy))
    F.write("\n")
    for segment in current_graph.segments:
        F.write("{} {} {}\n".format(segment.name, segment.origin_node.name, segment.destination_node.name))
        print("{} {} {}\n".format(segment.name, segment.origin_node.name, segment.destination_node.name))
    F.close()
    messagebox.showinfo("Guardar grafo", "El grafo se ha guardado correctamente.")
    insave.delete(0, tk.END)

def handnode():
    global clic, usonodos, figuracanvas, current_graph, graphcanvas
    if not usonodos:
        usonodos = True
        clic = figuracanvas.mpl_connect("button_press_event", addhandnode)
        btnhandnode.config(bg="white")
    elif usonodos:
        usonodos = False
        figuracanvas.mpl_disconnect(clic)
        btnhandnode.config(bg="#f0f0f0")
def addhandnode(event):
    global contnode, current_graph, graphcanvas, figuracanvas, usoseg
    if usonodos:
        x = round(event.xdata,3)
        y = round(event.ydata,3)
        if AddNode(current_graph, Node("N"+str(contnode),x,y)):
            contnode += 1
        if graphcanvas is not None:
            graphcanvas.destroy()
        fig, ax = plt.subplots()
        Plot(current_graph)
        figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
        figuracanvas.draw()
        figuracanvas.mpl_connect("button_press_event", addhandnode)
        graphcanvas = figuracanvas.get_tk_widget()
        graphcanvas.config(width=800, height=600)
        graphcanvas.pack()

def handseg():
    global clic, current_graph, figuracanvas, contseg, usoseg
    if not usoseg:
        usoseg = True
        clic = figuracanvas.mpl_connect("button_press_event", addhandseg)
        btnhandseg.config(bg="white")
    elif usoseg:
        usoseg = False
        figuracanvas.mpl_disconnect(clic)
        btnhandseg.config(bg="#f0f0f0")
def addhandseg(event):
    global contseg, current_graph, graphcanvas, figuracanvas, contnodseg, punto2, punto1, usoseg, usonodos
    if usoseg:
        x = round(event.xdata, 3)
        y = round(event.ydata, 3)
        if punto1 is None:
            for node1 in current_graph.nodes:
                if round(x) == round(node1.lon) and round(y) == round(node1.lat):
                    punto1 = node1
                    break
                else:
                    punto1 = [x,y]
        elif punto1 is not None and punto2 is None:
            for node2 in current_graph.nodes:
                if round(x) == round(node2.lon) and round(y) == round(node2.lat):
                    punto2 = node2
                    break
                else:
                    punto2 = [x,y]
        print(punto1, punto2)
        if punto1 is not None and punto2 is not None:
            if punto1 not in current_graph.nodes and punto2 not in current_graph.nodes:
                AddNode(current_graph, Node("s"+str(contnodseg), punto1[0], punto1[1]))
                contnodseg += 1
                AddNode(current_graph, Node("s"+str(contnodseg), punto2[0], punto2[1]))
                contnodseg += 1
                AddSegment(current_graph, "S"+str(contseg), "s"+str(contnodseg-2), "s"+str(contnodseg-1))
                contseg += 1
            elif punto1 in current_graph.nodes and punto2 not in current_graph.nodes:
                AddNode(current_graph, Node("s"+str(contnodseg), punto2[0], punto2[1]))
                contnodseg += 1
                AddSegment(current_graph, "S"+str(contseg), punto1.name, "s"+str(contnodseg-1))
                contseg += 1
            elif punto1 not in current_graph.nodes and punto2 in current_graph.nodes:
                AddNode(current_graph, Node("s"+str(contnodseg), punto1[0], punto1[1]))
                contnodseg += 1
                AddSegment(current_graph, "S"+str(contseg), "s"+str(contnodseg-1), punto2.name)
                contseg += 1
            else:
                AddSegment(current_graph, "S"+str(contseg), punto1.name, punto2.name)
                contseg += 1
            if graphcanvas is not None:
                graphcanvas.destroy()
            fig, ax = plt.subplots()
            Plot(current_graph)
            figuracanvas = FigureCanvasTkAgg(fig, master=graphshow)
            figuracanvas.draw()
            figuracanvas.mpl_connect("button_press_event", addhandseg)
            graphcanvas = figuracanvas.get_tk_widget()
            graphcanvas.config(width=800, height=600)
            graphcanvas.pack()
            punto1, punto2 = None, None



##################################################################################################################################################
################################################### INTERFAZ #####################################################################################
##################################################################################################################################################
ventana = tk.Tk()
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=10)

izquierda = tk.LabelFrame(ventana, text="Control")
izquierda.grid(column=0, pady=5, padx=5, sticky="nsew")
derecha = tk.LabelFrame(ventana, text="Gráfica")
derecha.grid(column=1, row=0, pady=5, padx=5, sticky="nsew")


###EJEMPLO###

basic = tk.LabelFrame(izquierda, text="Controles Básicos")
basic.pack(fill=tk.BOTH, padx=5)
basic.rowconfigure([0,1,2], weight=1)
basic.columnconfigure([0,1], weight=1)

buttonCat = tk.Button(basic, text="Cataluña", command=showcatalonia)
buttonCat.grid(row = 0, column = 0, pady=5, padx=5, sticky="ew")
buttonSp = tk.Button(basic, text="España", command=showspain)
buttonSp.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
buttonEu = tk.Button(basic, text="Europa", command=showeurope)
buttonEu.grid(row=0, column=2, pady=5, padx=5, sticky="ew")

create = tk.Button(basic, text="Crear Grafo", command=createblank)
create.grid(row = 1, column = 0, rowspan=3, padx=5, pady=5)
example = tk.Button(basic, text="Ejemplo", command=showexamplegraph)
example.grid(row=1, column=2, padx=5, pady=5)


###FICHERO###

fichero = tk.LabelFrame(izquierda, text="Fichero")
fichero.columnconfigure(0, weight=1)
fichero.columnconfigure(1, weight=5)
fichero.rowconfigure([0,1], weight=1)
fichero.pack(fill=tk.BOTH, padx=5)
    #LEYENDA DEL CUADRO#
filetext = tk.Label(fichero, text="Nombre de archivo:")
filetext.grid(row=0, column=0, pady=5, sticky="w")
    #CUADRO DE TEXTO#
infile = tk.Entry(fichero)
infile.grid(row=0, column=1, pady=5, padx=5, sticky="nsew")
    #BOTÓN#
btnfile = tk.Button(fichero, text="Cargar Grafo", command=showfilegraph)
btnfile.grid(row=1, column=0, columnspan=2, pady=5)


###VER VECINOS DE NODOS###

nodefr = tk.LabelFrame(izquierda, text="Ver Nodo")
nodefr.columnconfigure(0, weight=1)
nodefr.columnconfigure(1, weight=5)
nodefr.rowconfigure([0,1], weight=1)
nodefr.pack(fill=tk.BOTH, padx=5)
    #LEYENDA DEL CUADRO#
selnodtext = tk.Label(nodefr, text="Nombre del nodo:")
selnodtext.grid(row=0, column=0, pady=5, sticky="w")
    #CUADRO DE TEXTO#
selnode = tk.Entry(nodefr)
selnode.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    #BOTÓN#
btnnode = tk.Button(nodefr, text="Seleccionar Nodo", command=shownode)
btnnode.grid(row=1, column=0, columnspan=2, pady=5)


###AÑADIR NODO###

addnodefr = tk.LabelFrame(izquierda, text="Añadir Nodo")
addnodefr.rowconfigure([0,1,2,3], weight=1)
addnodefr.columnconfigure(0,weight=1)
addnodefr.columnconfigure(1,weight=5)
addnodefr.pack(fill=tk.BOTH, padx=5, pady=5)
    #LEYENDA NOMBRE#
nnametext = tk.Label(addnodefr,text="Nombre:")
nnametext.grid(row=0, column=0, pady=5, sticky="ew")
    #CUADRO DE TEXTO#
nodename = tk.Entry(addnodefr)
nodename.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    #LEYENDA COORDENADA X#
xtext = tk.Label(addnodefr, text="Coordenada X:")
xtext.grid(row=1, column=0, pady=5, sticky="ew")
    #CUADRO DE TEXTO#
nodex = tk.Entry(addnodefr)
nodex.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    #LEYENDA COORDENADA Y#
ytext = tk.Label(addnodefr, text="Coordenada Y:")
ytext.grid(row=2, column=0, pady=5, sticky="ew")
    #CUADRO DE TEXTO#
nodey = tk.Entry(addnodefr)
nodey.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    #BOTÓN AÑADIR NODO#
btnaddnode = tk.Button(addnodefr, text="Añadir Nodo", command=addnodei)
btnaddnode.grid(row=3, column=1, padx=5, pady=5)
    #BOTÓN AÑADIR NODO MANUALMENTE#
btnhandnode = tk.Button(addnodefr, text="Añadir Nodo A Mano", command=handnode)
btnhandnode.grid(row=3, column=0, padx=5, pady=5)


###AÑADIR SEGMENTO###

addsegmentfr = tk.LabelFrame(izquierda, text="Añadir Segmento")
addsegmentfr.rowconfigure([0,1,2,3], weight=1)
addsegmentfr.columnconfigure(0, weight=1)
addsegmentfr.columnconfigure(0, weight=5)
addsegmentfr.pack(fill=tk.BOTH, padx=5, pady=5)
    #LEYENDA NOMBRE SEGMENTO#
snametext = tk.Label(addsegmentfr, text="Nombre:")
snametext.grid(row=0, column=0, pady=5, sticky="ew")
    #CUADRO DE TEXTO#
segmentname = tk.Entry(addsegmentfr)
segmentname.grid(row=0, column=1, pady=5, padx=5, sticky="nsew")
    #LEYENDA ORÍGEN SEGMENTO#
segorigtext = tk.Label(addsegmentfr, text="Orígen:")
segorigtext.grid(row=1, column=0, pady=5, sticky="ew")
    #CUADRO DE TEXTO#
segmentorigin = tk.Entry(addsegmentfr)
segmentorigin.grid(row=1, column=1, pady=5, padx=5, sticky="nsew")
    #LEYENDA DESTINO SEGMENTO#
segdesttext = tk.Label(addsegmentfr, text="Destino:")
segdesttext.grid(row=2, column=0, pady=5, sticky="ew")
    #CUADRO DE TEXTO#
segmentdestination = tk.Entry(addsegmentfr)
segmentdestination.grid(row=2, column=1, pady=5, padx=5, sticky="nsew")
    #BOTÓN AÑADIR SEGMENTO#
btnaddseg = tk.Button(addsegmentfr, text="Añadir Segmento", command=addsegmenti)
btnaddseg.grid(row=3, column=1, padx=5, pady=5)
    #BOTÓN AÑADIR SEGMENTO MANUALMENTE#
btnhandseg = tk.Button(addsegmentfr, text="Añadir Seg. A Mano", command=handseg)
btnhandseg.grid(row=3, column=0, padx=5, pady=5)


###BORRAR NODO###

borrarnodofr = tk.LabelFrame(izquierda, text="Borrar Nodo")
borrarnodofr.columnconfigure(0, weight=1)
borrarnodofr.columnconfigure(1,weight=5)
borrarnodofr.rowconfigure([0,1,2],weight=1)
borrarnodofr.pack(fill=tk.BOTH, padx=5, pady=5)
    #LEYENDA DEL CUADRO#
borrnodotext = tk.Label(borrarnodofr, text="Nombre del nodo:")
borrnodotext.grid(row=0, column=0, pady=5)
    #CUADRO DE TEXTO#
inborrarnodo = tk.Entry(borrarnodofr)
inborrarnodo.grid(row=0, column=1, pady=5, padx=5, sticky="nsew")
    #LEYENDA BORAR SEGMENTO#
borrarsegtxt = tk.Label(borrarnodofr, text="Nombre del segmento")
borrarsegtxt.grid(row=1, column=0, pady=5)
    #CUADRO DE TEXTO#
inborrarseg = tk.Entry(borrarnodofr)
inborrarseg.grid(row=1, column=1, pady=5, padx=5, sticky="nsew")
    #BOTÓN BORRAR NODO#
btnborrarnodo = tk.Button(borrarnodofr, text="Borrar Nodo / Segmento", command=deletenodei)
btnborrarnodo.grid(row=2, column=0, columnspan=2, pady=5)


'''###VER SHORTEST PATH###

vershtpath = tk.Button(izquierda, text="Ver Shortest Path", command=showshortpath)
vershtpath.pack(pady=5, padx=5)'''

###MOSTRAR GRAFO###
graphshow = tk.Frame(derecha)
graphshow.pack(fill=tk.BOTH)
graphcanvas = tk.Canvas(graphshow, width=800, height=600)
graphcanvas.pack()

###GUARDAR GRAFO###
saving = tk.LabelFrame(derecha, text="Guardar grafo")
saving.rowconfigure([0,1], weight=1)
saving.columnconfigure(0, weight=1)
saving.columnconfigure(1, weight=5)
saving.pack(padx=5, pady=5, fill=tk.BOTH, side="bottom")
    #LEYENDA NOMBRE ARCHIVO#
insavetxt = tk.Label(saving, text="Nombre del archivo:")
insavetxt.grid(row=0, column=0)
    #CUADRO DE TEXTO#
insave = tk.Entry(saving)
insave.grid(row=0, column=1, sticky="ew", padx=5)
    #BOTÓN GUARDAR GRAFO#
save = tk.Button(saving, text="Guardar grafo", command=savegraph)
save.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()

#dividir la interfaz en tres: control(mostrar ejemplo, crear grafo, ver nodo, ver camino mas corto) y visualizacion, grafica, editor de gráfica(añadir nodos, segmentos, borrar nodos y/o segmentos)