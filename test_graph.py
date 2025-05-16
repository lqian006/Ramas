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
g3 = CreateGraph_1()
deletenode(g3, "B")
for node in g3.nodes:
    print(node.name)
for segment in g3.segments:
    print(segment.name)

#print(AddNeighbor(p1,n2))