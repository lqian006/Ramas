from node import *
from segment import *
from graph import *


'''print ("Probando el grafo...")
G = CreateGraph_1()
Plot(G)
PlotNode(G,"B")
clos = GetClosest(G,15,5)
print(clos)
clos = GetClosest(G,8,19)
print(clos)
g2 = Graph()
FileGraph(g2,"NodesFile.txt")'''
g3 = CreateGraph_1()
for node in g3.nodes:
    print(node.__dict__)
for segment in g3.segments:
    print(segment.__dict__)

#print(AddNeighbor(p1,n2))