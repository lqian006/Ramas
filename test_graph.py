from node import *
from segment import *
from graph import *


print ("Probando el grafo...")
G = CreateGraph_1()
Plot(G)
PlotNode(G,"B")
clos = GetClosest(G,15,5)
print(clos)
clos = GetClosest(G,8,19)
print(clos)
g2 = Graph()
FileGraph(g2,"NodesFile.txt")

#print(AddNeighbor(p1,n2))