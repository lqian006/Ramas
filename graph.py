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
    found3 = False
    node1 = None
    node2 = None
    for node in g.nodes:
        if nameOriginNode == node.name:
            found1 = True
            node1 = node
        if nameDestinationNode == node.name:
            found2 = True
            node2 = node
    for segments in g.segments:
        if segments.origin_node == node1 and segments.destination_node == node2:
            found3 = True
    if found3:
        print("El segmento ya existe.")
        return False
    elif found1 == True and found2 == True:
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

def FileGraph (g, file_name):
    F = open("{}".format(file_name),"r")
    linea = F.readline()
    i = 0
    while linea != "\n":
        datos1 = linea.split()
        AddNode(g,Node(datos1[0],float(datos1[1]),float(datos1[2])))
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

def CreateGraph_1 ():
    G = Graph()
    AddNode(G, Node("A",1,20))
    AddNode(G, Node("B",8,17))
    AddNode(G, Node("C",15,20))
    AddNode(G, Node("D",18,15))
    AddNode(G, Node("E",2,4))
    AddNode(G, Node("F",6,5))
    AddNode(G, Node("G",12,12))
    AddNode(G, Node("H",10,3))
    AddNode(G, Node("I",19,1))
    AddNode(G, Node("J",13,5))
    AddNode(G, Node("K",3,15))
    AddNode(G, Node("L",4,10))
    AddSegment(G,"AB","A","B")
    AddSegment(G,"AE","A","E")
    AddSegment(G,"AK","A","K")
    AddSegment(G,"BA","B","A")
    AddSegment(G,"BC","B","C")
    AddSegment(G,"BF","B","F")
    AddSegment(G,"BK","B","K")
    AddSegment(G,"BG","B","G")
    AddSegment(G,"CD","C","D")
    AddSegment(G,"CG","C","G")
    AddSegment(G,"DG","D","G")
    AddSegment(G,"DH","D","H")
    AddSegment(G,"DI","D","I")
    AddSegment(G,"EF","E","F")
    AddSegment(G,"FL","F","L")
    AddSegment(G,"GB","G","B")
    AddSegment(G,"GF","G","F")
    AddSegment(G,"GH","G","H")
    AddSegment(G,"ID","I","D")
    AddSegment(G,"IJ","I","J")
    AddSegment(G,"JI","J","I")
    AddSegment(G,"KA","K","A")
    AddSegment(G,"KL","K","L")
    AddSegment(G,"LK","L","K")
    AddSegment(G,"LF","L","F")
    return G

def deletenode (g, n):
    i = 0
    node1 = None
    for node in g.nodes:
        if node.name == n:
            node1 = node
    while i < len(g.segments):
        if node1 == g.segments[i].origin_node or node1 == g.segments[i].destination_node:
            g.segments.remove(g.segments[i])
            i -= 1
        i += 1

    if node1 is None:
        return False
    else:
        g.nodes.remove(node1)
        return True

def deleteseg (g, n):
    seg = None
    for element in g.segments:
        if element.name == n:
            seg = element
    if seg is not None:
        g.segments.remove(seg)
        return True
    else:
        return False
