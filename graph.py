from numpy.ma.core import indices

from node import *
from segment import *
import matplotlib.pyplot as plt
import math

class Graph:
    def __init__(self):
        self.nodes = []
        self.segments = []

def AddNode(g,n):
    i = 0
    encont = False
    while i < len(g.nodes) and encont == False:
        if n.coordx == g.nodes[i].coordx and n.coordy == g.nodes[i].coordy:
            encont = True
        else:
            i += 1
    if encont == True:
        return False
    else:
        g.nodes.append(n)
        return True

def AddSegment  (g, name, nameOriginNode, nameDestinationNode):
    found1 = False
    found2 = False
    node1 = None
    node2 = None
    for node in g.nodes:
        if nameOriginNode == node.name:
            found1 = True
            node1 = node
        if nameDestinationNode == node.name:
            found2 = True
            node2 = node
    if found1 == True and found2 == True:
        g.segments.append(segment(name,node1,node2))
    else:
        print("Uno de los nodos no está en la llista de nodos.")
        return False
    r = AddNeighbor(node1,node2)
    if r == True:
        return True

def GetClosest (g,x,y):
    min = 9999999999999.9
    men = 0
    for node in g.nodes:
        dist = math.sqrt((node.coordx - x) ** 2 + (node.coordy - y) ** 2)
        if dist < min:
            min = dist
            men = node.name
    return men

def Plot (g):
    for punto in g.nodes:
        plt.plot(punto.coordx,punto.coordy, marker = "o", color = "red")
        plt.text(punto.coordx+0.25, punto.coordy+0.25, punto.name, fontsize = 7.5, color = "green")
    for linea in g.segments:
        plt.annotate("",(linea.destination_node.coordx,linea.destination_node.coordy),(linea.origin_node.coordx,linea.origin_node.coordy),arrowprops=dict(arrowstyle="->", color="blue",lw=1.5))
        plt.text((linea.origin_node.coordx+linea.destination_node.coordx)/2,(linea.origin_node.coordy+linea.destination_node.coordy)/2,linea.cost,fontsize=7.5)
    plt.margins(x=0.25,y=0.25)
    plt.grid(True)
    plt.show()

def PlotNode (g, nameOrigin):
    node1 = None
    found = False
    neighbors = []
    for node in g.nodes:
        if node.name == nameOrigin:
            node1 = node
            found = True
    if found == False:
        return False
    plt.plot(node1.coordx, node1.coordy, color="blue", marker="o")
    plt.text(node1.coordx+0.5, node1.coordy+0.5, node1.name, fontsize=7.5)
    for point in node1.neighbors:
        plt.plot(point.coordx, point.coordy, color="green", marker="o")
        plt.text(point.coordx+0.5, point.coordy+0.5, point.name, fontsize=7.5)
        neighbors.append(point)
    for element in g.nodes:
        if element != node1 and element not in neighbors:
            plt.plot(element.coordx, element.coordy, color="gray", marker="o")
            plt.text(element.coordx+0.25, element.coordy+0.25, element.name, fontsize=7.5)
    for segment in neighbors:
        plt.annotate("", (segment.coordx, segment.coordy),
                     (node1.coordx, node1.coordy),
                     arrowprops=dict(arrowstyle="->", color="red", lw=1.5))
        plt.text((node1.coordx + segment.coordx) / 2,
                 (node1.coordy + segment.coordy) / 2, Distance(node1,segment), fontsize=7.5)
    plt.grid(True)
    plt.margins(x=0.25,y=0.25)
    plt.show()

def FileGraph (g, file_name):
    F = open("{}".format(file_name),"r")
    linea = F.readline()
    i = 0
    while linea != "\n":
        datos1 = linea.split()
        AddNode(g,Node(datos1[0],int(datos1[1]),int(datos1[2])))
        i += 1
        linea = F.readline()
    i += 1
    linea = F.readline()
    while linea != "":
        datos2 = linea.split()
        AddSegment(g,datos2[0],datos2[1],datos2[2])
        i += 1
        linea = F.readline()
    F.close()
    Plot(g)

'''for node in g.nodes:
    plt.plot(node.coordx,node.coordy,marker="o",color="blue")
    plt.text(node.coordx+0.5,node.coordy+0.5,node.name,fontsize=5)
for element in g.segments:
    plt.annotate("",(element.destination_node.coordx,element.destination_node.coordy),(element.origin_node.coordx,element.origin_node.coordy),arrowprops=dict(arrowstyle="->", color="red", lw=1.5))
    plt.text((element.origin_node.coordx+element.destination_node.coordx)/2,(element.origin_node.coordy+element.destination_node.coordy)/2,element.cost,fontsize=5)
plt.grid(True)
plt.show()'''