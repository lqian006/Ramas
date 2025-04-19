from node import *
from segment import *
from graph import *

p1 = Node()
p1.name = "Casa"
p1.coordx = 0.0
p1.coordy = 0.0
n2 = Node()
n2.name = "Insti"
n2.coordx = 3.0
n2.coordy = 4.0
n3 = Node()
n3.name = "Tienda"
n3.coordx = 5.0
n3.coordy = 3.5
s1 = segment("Seg1",p1,n2)
s1.cost = Distance(p1,n2)
s2 = segment("Seg",n2,n3)
s2.cost = Distance(n2,n3)
g1 = Graph()

print(AddSegment(g1,p1,n2))
print(p1.neighbors)
print(g1.nodes)
print(g1.segments)
AddNode(g1,p1)
print(g1.nodes)


#print(AddNeighbor(p1,n2))