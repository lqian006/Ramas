from node import *
from segment import *
from graph import *

g = Graph()
AddNode(g, Node("A",1,20))
AddNode(g, Node("B",8,17))
AddNode(g, Node("C",15,20))
AddNode(g, Node("D",18,15))
AddNode(g, Node("E",2,4))
AddNode(g, Node("F",6,5))
AddNode(g, Node("G",12,12))
AddNode(g, Node("H",10,3))
AddNode(g, Node("I",19,1))
AddNode(g, Node("J",13,5))
AddNode(g, Node("K",3,15))
AddNode(g, Node("L",4,10))
AddSegment(g,"AB","A","B")
AddSegment(g,"AE","A","E")
AddSegment(g,"AK","A","K")
AddSegment(g,"BA","B","A")
AddSegment(g,"BC","B","C")
AddSegment(g,"BF","B","F")
AddSegment(g,"BK","B","K")
AddSegment(g,"CD","C","D")
AddSegment(g,"CG","C","G")
AddSegment(g,"DG","D","G")
AddSegment(g,"DH","D","H")
AddSegment(g,"DI","D","I")
AddSegment(g,"EF","E","F")
AddSegment(g,"FL","F","L")
AddSegment(g,"GB","G","B")
AddSegment(g,"GF","G","F")
AddSegment(g,"GH","G","H")
AddSegment(g,"ID","I","D")
AddSegment(g,"IJ","I","J")
AddSegment(g,"JI","J","I")
AddSegment(g,"KA","K","A")
AddSegment(g,"KL","K","L")
AddSegment(g,"LK","L","K")
AddSegment(g,"LF","L","F")
for node in g.nodes:
    print(node.name)
for segment in g.segments:
    print(segment)
clos = GetClosest(g,7,19)
print(clos)
Plot(g)




#print(AddNeighbor(p1,n2))