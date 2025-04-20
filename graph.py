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
        plt.text(punto.coordx+0.5, punto.coordy+0.5, punto.name, fontsize = 5, color = "green")
    for linea in g.segments:
        plt.annotate("",(linea.destination_node.coordx,linea.destination_node.coordy),(linea.origin_node.coordx,linea.origin_node.coordy),arrowprops=dict(arrowstyle="->", color="blue",lw=1.5))

    plt.margins(x=0.25,y=0.25)
    '''plt.xticks((range(0,25,5)))
    plt.yticks(range(0,25,5))'''
    plt.grid(True)
    plt.show()

#plt.plot([nameOriginNode.coordx,nameDestinationNode.coordx],[nameOriginNode.coordy,nameDestinationNode.coordy])